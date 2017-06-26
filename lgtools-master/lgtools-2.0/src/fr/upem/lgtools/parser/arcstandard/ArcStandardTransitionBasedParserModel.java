/**
 * 
 */
package fr.upem.lgtools.parser.arcstandard;

import java.io.IOException;
import java.util.Collection;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.Set;

import fr.upem.lgtools.parser.Configuration;
import fr.upem.lgtools.parser.Container;
import fr.upem.lgtools.parser.DepTree;
import fr.upem.lgtools.parser.features.FeatureMapping;
import fr.upem.lgtools.parser.model.TransitionBasedDependencyParserModel;
import fr.upem.lgtools.parser.transitions.ShiftTransition;
import fr.upem.lgtools.parser.transitions.Transition;
import fr.upem.lgtools.text.DepTreebank;
import fr.upem.lgtools.text.DepTreebankFactory;
import fr.upem.lgtools.text.Sentence;
import fr.upem.lgtools.text.Unit;

/**
 * @author mconstant
 *
 */

public class ArcStandardTransitionBasedParserModel extends
		TransitionBasedDependencyParserModel {

	final String SHIFT = "SH";
	final String LEFT_ARC = "LA";
	final String RIGHT_ARC = "RA";
	final String SWAP = "SW";

	
	public ArcStandardTransitionBasedParserModel(FeatureMapping fm,
			DepTreebank tb,boolean isProjective) {
		super(fm, tb,isProjective);		
		
	}


	
	
	

	public ArcStandardTransitionBasedParserModel(String filename) throws IOException {
		super(filename);
	}

	
	
	
	
	/**
	 * 
	 * @param configuration
	 * @return the label of the LA transition to be applied; null when LA transition is not valid
	 */
	
	String getLeftArcLabel(Configuration<DepTree> configuration){
		Container stack = configuration.getFirstStack();
		if(stack.size() > 2){
			Unit u1 = stack.pop();
			Unit u2 = stack.peekFirst();
			stack.push(u1);
			if(u2.getGoldSheadId() == u1.getId() && hasAllItsDependents(u2,configuration)){
				return u2.getGoldSlabel();
			}
		}
		return null;
	}
	
	public static boolean hasAllItsDependents(Unit d,Configuration<DepTree> c){
		int id = d.getId();
		Set<Integer> goldChildren = new HashSet<Integer>(c.getGoldAnalyses().getChildren(id));
		Set<Integer> children = new HashSet<Integer>(c.getAnalyses().getChildren(id));
		if(goldChildren.size() != children.size()){
			return false;
		}
		goldChildren.retainAll(children);
		
		
		/*
		Sentence s = c.getSentence();
		List<Unit> buffer = Utils.getUnitSequence(true,s.getUnits().size(),s,c.getFirstBuffer(),true); //only irregular MWEs
		//System.err.println("RA"+buffer);
		for(Unit u:buffer){
			
			Unit r = u;
			if(!u.hasGoldLexicalHead()){
			  r = u.findGoldLexicalRoot(c.getSentence());
			}
			if(id == r.getGoldSheadId()) return false;
		}
		*/
		return goldChildren.size() == children.size();
	}
	
	
	/**
	 * 
	 * @param configuration
	 * @return The label of the RA transition to be applied; null when LA transition is not valid
	 */
	
	
	String getRightArcLabel(Configuration<DepTree> configuration){
		Container stack = configuration.getFirstStack();
		if(stack.size() >= 2){
			Unit u1 = stack.pop();
			Unit u2 = stack.peekFirst();
			stack.push(u1);
			if(u1.getGoldSheadId() == u2.getId() && hasAllItsDependents(u1,configuration)){
				
				return u1.getGoldSlabel();
			}
		}
		return null;
	}
	
	private boolean isLastMweElement(Unit e,Unit mwe){
		int last = mwe.getUnitLastTokenPosition();
		int ep = e.getUnitLastTokenPosition();
		return last == ep;
	}
	
	private boolean isFirstMweElement(Unit e,Unit mwe){
		int first = mwe.getUnitFirstTokenPosition();
		int ep = e.getUnitFirstTokenPosition();
		return first == ep;
	}
	
	
    private boolean isAlienUnitInMWE(Unit u1, Unit u2, Sentence s){
    	if(u1.hasGoldLexicalHead()){
			 int lh = u1.getGoldLHead();
			 Unit lhu = s.get(lh);
			if(lhu.isGoldFixedMWE(s) && !isLastMweElement(u1, lhu) && u2.getGoldLHead() != lh){
				//System.err.println("HH");
				return true;
			} 
		 }
    	if(u2.hasGoldLexicalHead()){
    		int lh = u2.getGoldLHead();
			 Unit lhu = s.get(lh);
			 if(lhu.isGoldFixedMWE(s) && !isFirstMweElement(u2, lhu) && u1.getGoldLHead() != lh){
				 //System.err.println("HH");
					return true;
				}
    	}
    	
    	return false;
    }
	
	
	private boolean swapIsRequired(Configuration<DepTree> configuration){
		 Container stack = configuration.getFirstStack();
		 if(stack.size() < 3){
			 return false;
		 }
		 Unit s0 = stack.pop();
		 Unit s1 = stack.peekFirst();
		 stack.push(s0);
		 
		 Sentence s=configuration.getSentence();
		 if(isAlienUnitInMWE(s1, s0, s)){
			 //System.err.println(SWAP+configuration);
			 
			 return true;
		 }
		 if(!s1.hasGoldSyntacticHead() || !s0.hasGoldSyntacticHead()){
			 return false;
		 }
		 //System.err.println("hhh");
		 //System.err.println(s0);
		 //System.err.println(s1);
		 int s0p = configuration.getProjectiveOrderPosition(s0);
		 int s1p = configuration.getProjectiveOrderPosition(s1);
		 //System.err.println(s0+"="+s1+"="+s0p+","+s1p+"--->"+(s0p < s1p));
		return s0p < s1p;
	}
	

	/* (non-Javadoc)
	 * @see fr.upem.lgtools.parser.model.TransitionBasedModel2#staticOracle(fr.upem.lgtools.parser.Configuration)
	 */
	@Override
	public Transition<DepTree> staticOracle(Configuration<DepTree> configuration) {
		String label;
		// if LA is possible, then LA
		if((label = getLeftArcLabel(configuration)) != null){
			//System.err.println("Oracle: LA+"+label);
			return transitions.getTransition(LEFT_ARC, label);
		}
		
		//if RA is possible, then RA
		if((label = getRightArcLabel(configuration)) != null){
			//System.err.println("Oracle: RA+"+label);
			return transitions.getTransition(RIGHT_ARC, label);
		}
		
		//if SWAP is possible, then SWAP
		
		if(!isProjective()){
			if(swapIsRequired(configuration)){
				//System.err.println("Oracle: RA+"+label);
				
				return transitions.getTransition(SWAP, label);
			}
		}
		
		//System.err.println("Oracle: SH");
		//default: SH				
		return transitions.getTransition(SHIFT, null);
	}

	
	
	/* (non-Javadoc)
	 * @see fr.upem.lgtools.parser.model.TransitionBasedModel2#createLabelDependentTransition(fr.upem.lgtools.text.Unit)
	 */
	@Override
	protected Transition<DepTree> createLabelDependentTransition(Unit unit,Sentence s) {
		if(!unit.hasGoldSyntacticHead()){
			return null;
		} 
		String label = unit.getGoldSlabel();
		int head = s.get(unit.getGoldSheadId()).getUnitFirstTokenPosition();
		int current = unit.getUnitFirstTokenPosition();
		
		
		if(head > current){ // head after current:: LA
			return createTransition(LEFT_ARC, label);			
		}
		// head before current:: RA
		return createTransition(RIGHT_ARC, label);		
	}

	/* (non-Javadoc)
	 * @see fr.upem.lgtools.parser.model.TransitionBasedModel2#createTransition(java.lang.String, java.lang.String)
	 */
	@Override
	protected Transition<DepTree> createTransition(String type, String label) {
		if(SHIFT.equals(type)){
		    return new ShiftTransition<DepTree>(SHIFT);
		}
		if(LEFT_ARC.equals(type)){
			return new LeftArcTransition(LEFT_ARC, label);
		}
		if(RIGHT_ARC.equals(type)){
			return new RightArcTransition(RIGHT_ARC, label);
		}
		if(SWAP.equals(type) && !isProjective()){
			return new SwapTransition<DepTree>(SWAP);
		}
		throw new IllegalStateException("Transition "+type + " is not allowed!");
	}

	/* (non-Javadoc)
	 * @see fr.upem.lgtools.parser.model.TransitionBasedModel2#createLabelIndependentTransitions()
	 */
	@Override
	protected Collection<Transition<DepTree>> createLabelIndependentTransitions() {
		Collection<Transition<DepTree>> transitions = new LinkedList<Transition<DepTree>>();
		transitions.add(createTransition(SHIFT,null));
		//System.err.println("create SH");
		if(!isProjective()){
			//System.err.println("create SWAP");
		   transitions.add(createTransition(SWAP,null));
		}
        return transitions;
	}



	@Override
	public DepTreebank filter(DepTreebank tb) {
		if(isProjective()){
			return DepTreebankFactory.filterNonProjective(tb);
		}
		return DepTreebankFactory.filterOverlappingMWE(tb);
	}

}
