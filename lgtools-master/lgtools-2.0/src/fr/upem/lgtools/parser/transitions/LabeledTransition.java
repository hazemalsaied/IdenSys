/**
 * 
 */
package fr.upem.lgtools.parser.transitions;

import fr.upem.lgtools.parser.Analysis;

/**
 * @author Matthieu Constant
 *
 */

public abstract class LabeledTransition<T extends Analysis> extends AbstractTransition<T> {
    final protected String label;
	
	public LabeledTransition(String type,String label) {
		super(type);
		this.label = label;
	}

	@Override
	public String id() {		
		return Transitions.constructTransitionId(super.type, label);
	}

	
	

		
	
}
