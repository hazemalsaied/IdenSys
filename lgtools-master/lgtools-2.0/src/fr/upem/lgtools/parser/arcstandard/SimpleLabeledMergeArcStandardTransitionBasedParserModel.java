/**
 * 
 */
package fr.upem.lgtools.parser.arcstandard;

import java.io.IOException;

import fr.upem.lgtools.parser.features.FeatureMapping;
import fr.upem.lgtools.text.DepTreebank;

/**
 * @author Mathieu
 *
 */
public class SimpleLabeledMergeArcStandardTransitionBasedParserModel
		extends SimpleMergeArcStandardTransitionBasedParserModel {

	public SimpleLabeledMergeArcStandardTransitionBasedParserModel(FeatureMapping fm, DepTreebank tb,boolean isProjective) {
		super(fm, tb,isProjective);
	}

	@Override
	public boolean isWithLabeledMerge() {
		return true;
	}

	/**
	 * @param filename
	 * @throws IOException
	 */
	public SimpleLabeledMergeArcStandardTransitionBasedParserModel(String filename) throws IOException {
		super(filename);
	}
	
	

}
