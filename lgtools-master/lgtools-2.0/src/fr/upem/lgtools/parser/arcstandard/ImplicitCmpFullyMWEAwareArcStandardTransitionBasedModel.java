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
public class ImplicitCmpFullyMWEAwareArcStandardTransitionBasedModel
		extends FullyMWEAwareArcStandardTransitionBasedModel {
    boolean withConstrainedMerge = false;
	
	public ImplicitCmpFullyMWEAwareArcStandardTransitionBasedModel(FeatureMapping fm, DepTreebank tb, boolean withConstrainedMerge,boolean projective) {
		super(fm, tb,projective);  //withConstrainedMerge = true does not work because of super
	   	this.withConstrainedMerge = withConstrainedMerge;
	   	//System.err.println(this.withConstrainedMerge);
	}
	
	/**
	 * @param fm
	 * @param tb
	 */
	public ImplicitCmpFullyMWEAwareArcStandardTransitionBasedModel(FeatureMapping fm, DepTreebank tb,boolean isProjective) {
		super(fm, tb,isProjective);
		
	}

	

	public ImplicitCmpFullyMWEAwareArcStandardTransitionBasedModel(String filename, boolean withConstrainedMerge) throws IOException {
		super(filename);
		this.withConstrainedMerge = withConstrainedMerge;
		
	}
	
	
	@Override
	protected Transition<DepTree> createTransition(String type, String label) {
		//System.err.println(withConstrainedMerge);
		//withConstrainedMerge = true;
		if(MERGE_BOTH.equals(type)){
			return new MergeBothTransition(MERGE_BOTH,label,withConstrainedMerge); 
		}
		if(MERGE.equals(type)){
			return new MergeTransition(MERGE,label,withConstrainedMerge);
		}
		
		if(SHIFT.equals(type)){
		    return new ShiftTransitionForFullSystem(SHIFT,withConstrainedMerge);
		}
		
		if(SWAP.equals(type) && !isProjective()){
			return new SwapTransition<DepTree>(SWAP);
			
		}
		    
		if(LEFT_ARC.equals(type)){
			return new LeftArcTransitionWithImplicitComplete(LEFT_ARC, label);
		}
		if(RIGHT_ARC.equals(type)){
			return new RightArcTransitionWithImplicitComplete(RIGHT_ARC, label);
		}
		throw new IllegalStateException("Transition "+type + " is not allowed!");
	}
	
	
	@Override
	boolean hasImplicitCompleteTransition() {
		return true;
	}

	
	
	
	

}
