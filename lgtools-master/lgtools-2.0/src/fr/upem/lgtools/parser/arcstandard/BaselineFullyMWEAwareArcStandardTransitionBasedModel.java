/**
 * 
 */
package fr.upem.lgtools.parser.arcstandard;

import java.io.IOException;

import fr.upem.lgtools.parser.DepTree;
import fr.upem.lgtools.parser.features.FeatureMapping;
import fr.upem.lgtools.parser.transitions.Transition;
import fr.upem.lgtools.text.DepTreebank;

/**
 * @author Mathieu
 *
 */
public class BaselineFullyMWEAwareArcStandardTransitionBasedModel extends FullyMWEAwareArcStandardTransitionBasedModel {

	/**
	 * @param fm
	 * @param tb
	 */
	public BaselineFullyMWEAwareArcStandardTransitionBasedModel(FeatureMapping fm, DepTreebank tb, boolean projective) {
		super(fm, tb,projective);
		
	}

	/**
	 * @param filename
	 * @throws IOException
	 */
	public BaselineFullyMWEAwareArcStandardTransitionBasedModel(String filename) throws IOException {
		super(filename);
	
	}
	
	@Override
	protected Transition<DepTree> createTransition(String type, String label) {
		if(MERGE_BOTH.equals(type)){
			return new MergeBothTransition(MERGE_BOTH,label); 
		}
		if(MERGE.equals(type)){
			return new MergeTransition(MERGE,label);
		}
		if(COMPLETE.equals(type)){
			return new CompleteTransition(COMPLETE);
		}
		return super.createTransition(type, label);
	}

	@Override
	boolean hasImplicitCompleteTransition() {
		return false;
	}
	
	
	
}
