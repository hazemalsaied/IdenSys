/**
 * 
 */
package fr.upem.lgtools.parser.model;

import java.io.IOException;

import fr.upem.lgtools.parser.features.FeatureMapping;
import fr.upem.lgtools.text.DepTreebank;
import fr.upem.lgtools.text.DepTreebankFactory;

/**
 * @author Matthieu Constant
 *
 */
public abstract class ProjectiveTransitionBasedDependencyParserModel extends
		TransitionBasedDependencyParserModel {

	

	public ProjectiveTransitionBasedDependencyParserModel(FeatureMapping fm,
			DepTreebank tb) {
		super(fm, tb,true);
		
	}


	public ProjectiveTransitionBasedDependencyParserModel(String filename) throws IOException {
		super(filename);
		
	}


	/* (non-Javadoc)
	 * @see fr.upem.lgtools.parser.model.TransitionBasedModel2filter(fr.upem.lgtools.text.DepTreebank)
	 */
	@Override
	public DepTreebank filter(DepTreebank tb) {		
		return DepTreebankFactory.filterNonProjective(tb);
	}

	
}
