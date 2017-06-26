/**
 * 
 */
package fr.upem.lgtools.parser.arcstandard;

import java.io.IOException;

import fr.upem.lgtools.parser.features.FeatureMapping;
import fr.upem.lgtools.text.DepTreebank;

/**
 * @author Mathieu Constant
 *
 */
public class SimpleUnlabeledMergeArcStandardTransitionBasedParserModel
		extends SimpleMergeArcStandardTransitionBasedParserModel {

	public SimpleUnlabeledMergeArcStandardTransitionBasedParserModel(FeatureMapping fm, DepTreebank tb,boolean isProjective) {
		super(fm, tb,isProjective);
	}

	
	
	
	/**
	 * @param filename
	 * @throws IOException
	 */
	public SimpleUnlabeledMergeArcStandardTransitionBasedParserModel(String filename) throws IOException {
		super(filename);
	}




	@Override
	public boolean isWithLabeledMerge() {
		return false;
	}
	
	

}
