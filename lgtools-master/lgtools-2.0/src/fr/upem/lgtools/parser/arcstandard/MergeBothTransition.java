package fr.upem.lgtools.parser.arcstandard;

import java.util.ArrayList;

import fr.upem.lgtools.parser.Configuration;
import fr.upem.lgtools.parser.Container;
import fr.upem.lgtools.parser.DepTree;
import fr.upem.lgtools.parser.transitions.LabeledTransition;
import fr.upem.lgtools.parser.transitions.TransitionUtils;
import fr.upem.lgtools.text.Unit;

public class MergeBothTransition extends LabeledTransition<DepTree> {
    boolean withConstrainedMerge = false;
	
	public MergeBothTransition(String type,String label) {
		super(type,label);
	}
	
	public MergeBothTransition(String type,String label, boolean withConstrainedMerge) {
		super(type,label);
		this.withConstrainedMerge = withConstrainedMerge;
	}
	

	
	@Override
	public Configuration<DepTree> perform(Configuration<DepTree> configuration) {
		Container stack = configuration.getFirstStack();
		Container lexStack = null;
		boolean hasMoreStacks = configuration.stackCount() >= 2;
		if(hasMoreStacks){
			lexStack = configuration.getSecondStack();	
		}
		
		ArrayList<Container> stacks = new ArrayList<Container>();
		Unit u0 = stack.pop();
		Unit u1 = stack.pop();
		stacks.add(stack);
		if(hasMoreStacks){
			lexStack.pop();
			lexStack.pop();
			stacks.add(lexStack);
		}
		
		//System.err.println(stacks.size());
		return TransitionUtils.performMerge(configuration,label,u1,u0,stacks);
	}

	
	@Override
	public boolean isValid(Configuration<DepTree> configuration) {
		if(!ParserUtils.passContrainedMergeCondition(withConstrainedMerge,configuration)){
			return false;
		}
		Container stack = configuration.getFirstStack();
		DepTree tree = configuration.getAnalyses();
		if(stack.size() <= 2){
			return false;
		}
		boolean res = true;
		Unit u0 = stack.pop();
		Unit u1 = stack.pop();
		if(tree.nodeHasChildren(u0.getId()) || tree.nodeHasChildren(u1.getId())){ //if u0 or u1 has children, transition not valid (as we're dealing with fixed expressions)
			res = false;
		}
		
		stack.push(u1);  //stack in initial state of this method call
		stack.push(u0);
		
		boolean hasMoreStacks = configuration.stackCount() >= 2;
		if(hasMoreStacks){
			Container lexStack = configuration.getSecondStack();
			if(lexStack.size() <= 2){
				res = false;
			}
			Unit u02 = lexStack.pop();
			Unit u12 = lexStack.peekFirst();
			lexStack.push(u02);
			if(u02.getId() != u0.getId() || u12.getId() != u1.getId()){
				res = false;
			}
			
		}
		
		/*if(res){
			System.err.println("ICI");
		}*/
		return res;
	}

	
	
	
}
