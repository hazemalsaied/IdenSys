/**
 * 
 */
package fr.upem.lgtools.parser.arcstandard;

import java.util.ArrayList;

import fr.upem.lgtools.parser.Configuration;
import fr.upem.lgtools.parser.Container;
import fr.upem.lgtools.parser.DepTree;
import fr.upem.lgtools.parser.transitions.LabeledTransition;
import fr.upem.lgtools.parser.transitions.TransitionUtils;
import fr.upem.lgtools.text.Unit;

/**
 * @author Matthieu Constant
 *
 */
public class MergeTransition extends LabeledTransition<DepTree> {
    boolean withConstrainedMerge = false;
	
	public MergeTransition(String type, String label) {
		super(type, label);
	}

	public MergeTransition(String type, String label, boolean withConstrainedMerge) {
		super(type, label);
		this.withConstrainedMerge = withConstrainedMerge;
	}
	
	
	@Override
	public Configuration<DepTree> perform(Configuration<DepTree> configuration) {
		Container stack = configuration.getSecondStack();
		ArrayList<Container> stacks = new ArrayList<Container>();
		Unit u0 = stack.pop();
		Unit u1 = stack.pop();
		stacks.add(stack);
		return TransitionUtils.performMerge(configuration,label,u1,u0,stacks);
	}

	@Override
	public boolean isValid(Configuration<DepTree> configuration) {
		if(!ParserUtils.passContrainedMergeCondition(withConstrainedMerge, configuration)){
			return false;
		}
		Container stack = configuration.getSecondStack();
		if(stack.size() < 3){
			return false;
		}
		
		
		return true;
	}

	
	
}
