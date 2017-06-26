/**
 * 
 */
package fr.upem.lgtools.parser.mwereco;



import fr.upem.lgtools.parser.Configuration;
import fr.upem.lgtools.parser.Container;
import fr.upem.lgtools.parser.DepTree;
import fr.upem.lgtools.parser.ExternalData;
import fr.upem.lgtools.parser.features.FeatureExtractor;
import fr.upem.lgtools.parser.features.FeatureMapping;
import fr.upem.lgtools.parser.features.FeatureUtils;
import fr.upem.lgtools.parser.features.FeatureVector;
import fr.upem.lgtools.text.Unit;

/**
 * @author Mathieu
 *
 */
public class MweFeatureExtractor implements FeatureExtractor<DepTree> {
	FeatureMapping featureMapping;
	
	public MweFeatureExtractor(FeatureMapping featureMapping) {
		this.featureMapping = featureMapping;
	}
	
	private void extractLexicalFeatures(Configuration<DepTree> configuration, FeatureVector feats){
		Container buffer = configuration.getFirstBuffer();
		Container stack= configuration.getFirstStack();
		//feats.add("BIAS");
		//feats.add("EMPTY2");
		Unit s0u = FeatureUtils.getUnit(stack.peekFirst());
		Unit s1u = FeatureUtils.getUnit(stack.peekSecond());
		Unit b0u = FeatureUtils.getUnit(buffer.peekFirst());
		//Unit b1u = getSecondElementInBuffer(buffer);
		
		FeatureUtils.addUnitFeatures("lex:s0u", s0u,feats,configuration);
		FeatureUtils.addUnitFeatures("lex:s1u", s1u,feats,configuration);
		
		FeatureUtils.addUnitPairFeatures("lex:s0u_s1u",s0u,s1u,feats,configuration);	
		FeatureUtils.addUnitPairFeatures("lex:s0u_b0u",s0u,b0u,feats,configuration);
		
		FeatureUtils.addUnitTripletFeatures("lex:s1u_s0u_b0u",s1u,s0u,b0u,feats,configuration);	
	}
	
	private void extract(Configuration<DepTree> configuration, FeatureVector feats){
		Container buffer = configuration.getFirstBuffer();
		Container stack = configuration.getFirstStack();
		
		Unit s0u = FeatureUtils.getUnit(stack.peekFirst());
		Unit s1u = FeatureUtils.getUnit(stack.peekSecond());
		Unit s2u = FeatureUtils.getUnit(stack.peekThird());
		Unit b0u = FeatureUtils.getUnit(buffer.peekFirst());
		Unit b1u = FeatureUtils.getUnit(buffer.peekSecond());
		Unit b2u = FeatureUtils.getUnit(buffer.peekThird());
		
		
		feats.add("BIAS");
		FeatureUtils.addUnitFeatures("s0u", s0u,feats,configuration);
		FeatureUtils.addUnitFeatures("s1u", s1u,feats,configuration);
		FeatureUtils.addUnitFeatures("s2u", s2u,feats,configuration);
		FeatureUtils.addUnitFeatures("b0u", b0u,feats,configuration);
		FeatureUtils.addUnitFeatures("b1u", b1u,feats,configuration);
		FeatureUtils.addUnitFeatures("b2u", b2u,feats,configuration);
		FeatureUtils.addUnitPairFeatures("s0u_b0u",s0u,b0u,feats,configuration);
		FeatureUtils.addUnitPairFeatures("b0u_b1u",b0u,b1u,feats,configuration);
		
		
		FeatureUtils.addUnitTripletFeatures("s2u_s1u_s0u",s2u,s1u,s0u,feats,configuration);
		FeatureUtils.addUnitTripletFeatures("s1u_s0u_b0u",s1u,s0u,b0u,feats,configuration);
		FeatureUtils.addUnitTripletFeatures("s0u_b0u_b1u",s0u,b0u,b1u,feats,configuration);
		FeatureUtils.addUnitTripletFeatures("b0u_b1u_b2u",b0u,b1u,b2u,feats,configuration);

		
		FeatureUtils.addUnitTripletFeatures("s0u_b0u_b1u",s0u,b0u,b1u,feats,configuration);
		FeatureUtils.addHistoryFeatures(configuration,feats);
	}
	
	
	@Override
	public FeatureVector perform(Configuration<DepTree> configuration, ExternalData data) {
		FeatureVector feats = new FeatureVector(featureMapping);
		//extractLexicalFeatures(configuration, feats);
		extract(configuration, feats);
		return feats;
		
	}
	

}
