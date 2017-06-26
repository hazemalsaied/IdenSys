/**
 * 
 */
package fr.upem.lgtools.parser.mwereco;

import java.io.IOException;
import java.util.Collection;
import java.util.LinkedList;

import fr.upem.lgtools.parser.Configuration;
import fr.upem.lgtools.parser.Container;
import fr.upem.lgtools.parser.DepTree;
import fr.upem.lgtools.parser.features.FeatureExtractor;
import fr.upem.lgtools.parser.features.FeatureMapping;
import fr.upem.lgtools.parser.model.ProjectiveTransitionBasedDependencyParserModel;
import fr.upem.lgtools.parser.transitions.ShiftTransition;
import fr.upem.lgtools.parser.transitions.Transition;
import fr.upem.lgtools.text.DepTreebank;
import fr.upem.lgtools.text.Sentence;
import fr.upem.lgtools.text.Unit;

/**
 * @author Matthieu Constant
 *
 */
public class MweRecognizerModel extends
		ProjectiveTransitionBasedDependencyParserModel {

	final String SHIFT = "SH";
	final String MERGE = "ME";
	final String COMPLETE = "CMP";
	
	
	public MweRecognizerModel(FeatureMapping fm,
			DepTreebank tb) {
		super(fm, tb);		
	}



	public MweRecognizerModel(String filename) throws IOException {
		super(filename);		
	}

	
	
	String getMerge(Configuration<DepTree> configuration){

		Container stack = configuration.getFirstStack();
		if(stack.size() > 2){
			Unit u1 = stack.pop();
			Unit u2 = stack.peekFirst();
			stack.push(u1);
			if(!u2.hasGoldLexicalHead() || !u1.hasGoldLexicalHead()){
				return null;
			}

			

			int l1 = u2.getGoldLHead();
			int l2 = u1.getGoldLHead();

			if(l1 == l2){				
				return configuration.getUnit(l1).getPos();
			}
		}
		return null;
	}





	boolean completeIsPossible(Configuration<DepTree> configuration){
		Container stack = configuration.getFirstStack();
		if(stack.size() > 1){
			Unit u = stack.peekFirst();
			if(!u.hasGoldLexicalHead()){
				return true;
			}
		}
		return false;

	}

	
	
	
	
	/* (non-Javadoc)
	 * @see fr.upem.lgtools.parser.model.TransitionBasedModel2#staticOracle(fr.upem.lgtools.parser.Configuration)
	 */
	@Override
	public Transition<DepTree> staticOracle(Configuration<DepTree> configuration) {
		String label;

		//if MERGE is possible do MERGE
		if((label = getMerge(configuration)) != null){
			return transitions.getTransition(MERGE, label);
		}

		//if COMPLETE is possible do COMPLETE
		if(completeIsPossible(configuration)){
			return transitions.getTransition(COMPLETE, null);
		}

		return transitions.getTransition(SHIFT, null);
	}

	
	private String getMergeUnitLabel(Unit u, Sentence s){
		return u.isMWE()?u.getPos():null;		
	}
	
	/* (non-Javadoc)
	 * @see fr.upem.lgtools.parser.model.TransitionBasedModel2#createLabelDependentTransition(fr.upem.lgtools.text.Unit)
	 */
	@Override
	protected Transition<DepTree> createLabelDependentTransition(Unit unit,Sentence s) {
		String label = getMergeUnitLabel(unit, s);
        return label != null?createTransition(MERGE,label):null;	
    }
	

	/* (non-Javadoc)
	 * @see fr.upem.lgtools.parser.model.TransitionBasedModel2#createTransition(java.lang.String, java.lang.String)
	 */
	@Override
	protected Transition<DepTree> createTransition(String type, String label) {
		
		if(MERGE.equals(type)){
			return new MergeTransition(MERGE,label);
		}
		if(COMPLETE.equals(type)){
			return new CompleteTransition(COMPLETE);
		}
		if(SHIFT.equals(type)){
		    return new ShiftTransition<DepTree>(SHIFT);
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
		transitions.add(createTransition(COMPLETE,null));
        return transitions;
	}

	
	@Override
	protected FeatureExtractor<DepTree> getFeatureExtractor(FeatureMapping fm) {
		return new MweFeatureExtractor(fm);
	}
	
}
