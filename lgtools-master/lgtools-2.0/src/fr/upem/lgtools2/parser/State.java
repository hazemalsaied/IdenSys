/**
 * 
 */
package fr.upem.lgtools2.parser;

import fr.upem.lgtools.parser.Container;

/**
 * @author Mathieu
 * 
 * represents a state of syntactic parser
 *
 */
public class State {
	final Container lexicalStack;
	final Container syntacticStack;
	final Container buffer;
	final State previous;
	//Transition transition;
	
	public State(){
		lexicalStack = new Container();
		syntacticStack = new Container();
		buffer = new Container();
		previous = null;
	}
	
	public State(State state){
		lexicalStack = new Container(state.lexicalStack);
		syntacticStack = new Container(state.syntacticStack);
		buffer = new Container(state.buffer);
		previous = state; //really?
	}

}
