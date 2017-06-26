/**
 * 
 */
package fr.upem.lgtools.parser.arcstandard;

import fr.upem.lgtools.parser.Configuration;
import fr.upem.lgtools.parser.DepTree;
import fr.upem.lgtools.parser.transitions.ShiftTransition;

/**
 * @author Mathieu
 *
 */
public class ShiftTransitionForFullSystem extends ShiftTransition<DepTree> {
    private final boolean withConstrainedMerge;
	
	public ShiftTransitionForFullSystem(String type, boolean withConstrainedMerge) {
		super(type);
		this.withConstrainedMerge = withConstrainedMerge;
	}
	
	@Override
	public boolean isValid(Configuration<DepTree> configuration) {
		if(!ParserUtils.passContrainedMergeCondition(withConstrainedMerge, configuration)){
			return false;
		}
		return super.isValid(configuration);
	}
	

}
