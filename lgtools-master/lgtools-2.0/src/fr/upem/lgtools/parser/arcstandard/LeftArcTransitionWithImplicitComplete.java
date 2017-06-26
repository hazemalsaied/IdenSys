/**
 * 
 */
package fr.upem.lgtools.parser.arcstandard;

import fr.upem.lgtools.parser.Configuration;
import fr.upem.lgtools.parser.Container;
import fr.upem.lgtools.parser.DepTree;
import fr.upem.lgtools.text.Unit;

/**
 * @author Mathieu
 *
 */
public class LeftArcTransitionWithImplicitComplete extends LeftArcTransition {
	boolean withImplicit = false;
	
	
	public LeftArcTransitionWithImplicitComplete(String type, String label) {
		super(type, label);
	}

	
	
	
	Unit getTargetUnitForCompletion(Configuration<DepTree> configuration){
		Container stack = configuration.getFirstStack();
		Unit u0 = stack.pop();
		Unit u = stack.peekFirst();
		stack.push(u0);
		return ParserUtils.getLexicalUnitFromComponent(u, configuration.getAnalyses(), configuration.getSentence());
		
	}
	
	void completeUnit(Unit u,Configuration<DepTree> configuration){
		Container stack = configuration.getSecondStack();
		Unit u0 = stack.pop();
		Unit u1 = stack.pop();
		//System.err.println("LA:");
		//System.err.println(configuration);
		//System.err.println(u+" "+u0+" "+u1);
		if(u == u0){
			stack.push(u1);
			return;
		}
		else{
			if(u == u1){
			   stack.push(u0);
			   return;
			}
		}
		throw new IllegalStateException("Cannot complete top-1 or top-2 element in lexical stack during implicit complete!");
	}
	
	
	
	
	@Override
	public Configuration<DepTree> perform(Configuration<DepTree> configuration) {
		Unit u = getTargetUnitForCompletion(configuration);
		withImplicit = false;
		configuration = super.perform(configuration);
		
		if(ParserUtils.unitIsSyntacticallyCompleted(u, configuration.getAnalyses(),configuration.getSentence())){
			completeUnit(u,configuration);
			withImplicit = true;
		}
		return configuration;
	}
	
	@Override
	public String toString(){
		String res = super.toString();
		return withImplicit?res+"-CMP":res;
	}

}
