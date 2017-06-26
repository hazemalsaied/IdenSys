/**
 * 
 */
package fr.upem.lgtools.parser.model;

import java.io.IOException;

import fr.upem.lgtools.parser.Configuration;
import fr.upem.lgtools.parser.Configurations;
import fr.upem.lgtools.parser.DepTree;
import fr.upem.lgtools.parser.arcstandard.DefaultFeatureExtractor;
import fr.upem.lgtools.parser.arcstandard.ParserUtils;
import fr.upem.lgtools.parser.features.FeatureExtractor;
import fr.upem.lgtools.parser.features.FeatureMapping;
import fr.upem.lgtools.text.DepTreebank;
import fr.upem.lgtools.text.Sentence;
import fr.upem.lgtools.text.Unit;

/**
 * @author Matthieu Constant
 *
 */
public abstract class TransitionBasedDependencyParserModel extends
		TransitionBasedModel<DepTree> {

	public TransitionBasedDependencyParserModel(FeatureMapping fm,
			DepTreebank tb,boolean isProjective) {
		super(fm, tb,isProjective);
		
	}

	public TransitionBasedDependencyParserModel(String filename) throws IOException {
		super(filename);		
	}

	
	@Override
	public Configuration<DepTree> getInitialConfiguration(Sentence s,boolean needsGold) {
		DepTree t = needsGold?ParserUtils.createGoldTree(s):null;
		return Configurations.createDefaultConfiguration(s, 1, 1, t);
	}

	
	@Override
	public void updateSentenceAfterAnalysis(Sentence s, DepTree analysis) {
		for(Unit u:s.getUnits()){
			//System.err.println(u);
			u.setShead(analysis.getHead(u.getId()));			
			u.setPredictedSlabel(analysis.getlabel(u.getId()));
			int lh = analysis.getLexicalNodeId(u.getId());
			u.setPredictedLhead(lh);	
		}
		
	}

	@Override
	protected FeatureExtractor<DepTree> getFeatureExtractor(FeatureMapping fm) {		
		return new DefaultFeatureExtractor(fm);
	}
	
	

}
