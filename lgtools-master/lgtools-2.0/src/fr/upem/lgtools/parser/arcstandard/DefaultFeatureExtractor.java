/*
 * 
 */
package fr.upem.lgtools.parser.arcstandard;
        
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
 * @author Mathieu Constant
 *
 */
public class DefaultFeatureExtractor implements FeatureExtractor<DepTree> {
	
	final FeatureMapping fm;
	
	public DefaultFeatureExtractor(FeatureMapping featureMapping){
		this.fm = featureMapping;
	}
	
	
	
    
	
	
	
	
	
	
	
	
	
	
    
	
	@Override
	public FeatureVector perform(fr.upem.lgtools.parser.Configuration<DepTree> config, ExternalData data) {
		FeatureVector feats = new FeatureVector(fm);
		extract("",config, config.getFirstStack(),feats);
		return feats;
	};
	
	
	FeatureVector extract(String prefix,Configuration<DepTree> configuration,Container stack, FeatureVector feats) {
		
		
		Container buffer = configuration.getFirstBuffer();
		//feats.add("BIAS");
		//feats.add("EMPTY2");
		Unit s0u = FeatureUtils.getUnit(stack.peekFirst());
		Unit s1u = FeatureUtils.getUnit(stack.peekSecond());
		Unit s2u = FeatureUtils.getUnit(stack.peekThird());
		Unit b0u = FeatureUtils.getUnit(buffer.peekFirst());
		Unit b1u = FeatureUtils.getUnit(buffer.peekSecond());
		Unit b2u = FeatureUtils.getUnit(buffer.peekThird());
		//System.err.println(configuration);
		//System.err.println("STACK//"+s0u.getForm()+"::"+s1u.getForm()+"::"+s2u.getForm());
		//System.err.println("BUFFER//"+b0u.getForm()+"::"+b1u.getForm()+"::"+b2u.getForm());
		//System.err.println("LEFTMOST LEFT DEPS//"+lmds0u.getForm()+"::"+lmds1u.getForm());
		//System.err.println("RIGHTMOST RIGHT DEPS//"+rmds0u.getForm()+"::"+rmds1u.getForm());
		
		//addSubtreeFeatures("s0u",s0u,configuration,feats);
		//addSubtreeFeatures("s1u",s1u,configuration,feats);
		
		
		FeatureUtils.addDistanceFeature(prefix+"dist_s0u_s1u",s1u,s0u,feats);
		//addDistanceFeature("dist_s1u_s2u",s2u,s1u,feats);
		//addDistanceFeature("dist_s0u_b0u",s0u,b0u,feats);
		
		
		FeatureUtils.addUnitFeatures(prefix+"s0u", s0u,feats,configuration);
		FeatureUtils.addUnitFeatures(prefix+"s1u", s1u,feats,configuration);
		FeatureUtils.addUnitFeatures(prefix+"s2u", s2u,feats,configuration);
		FeatureUtils.addUnitFeatures(prefix+"b0u", b0u,feats,configuration);
		FeatureUtils.addUnitFeatures(prefix+"b1u", b1u,feats,configuration);
		FeatureUtils.addUnitFeatures(prefix+"b2u", b2u,feats,configuration);
		
		//FeatureUtils.addSubTreeFeatures(prefix+"dep_b0u",b0u,configuration,feats);
		FeatureUtils.addSubTreeFeatures(prefix+"dep_s0u",s0u,configuration,feats);				
		FeatureUtils.addSubTreeFeatures(prefix+"dep_s1u",s1u,configuration,feats);
		//FeatureUtils.addSubTreeFeatures(prefix+"dep_s2u",s2u,configuration,feats);
		//addUnitFeatures("lmdb1u", lmdb1u,feats);
		//addUnitFeatures("rmdb0u", rmdb0u,feats);
		//addUnitFeatures("rmdb1u", rmdb1u,feats);
		
		//addUnitComponents("comp_s0u",s0u,configuration,feats);
		//addUnitComponents("comp_s1u",s1u,configuration,feats);
		
	
		//addUnitPairFeatures("s0u_s1u",s0u,s1u,feats);	
		FeatureUtils.addUnitPairFeatures(prefix+"s0u_b0u",s0u,b0u,feats,configuration);
		FeatureUtils.addUnitPairFeatures(prefix+"b0u_b1u",b0u,b1u,feats,configuration);
		//addUnitPairFeatures("b1u_b2u",b1u,b2u,feats);
		
		
		FeatureUtils.addUnitTripletFeatures(prefix+"s2u_s1u_s0u",s2u,s1u,s0u,feats,configuration);
		FeatureUtils.addUnitTripletFeatures(prefix+"s1u_s0u_b0u",s1u,s0u,b0u,feats,configuration);
		FeatureUtils.addUnitTripletFeatures(prefix+"s0u_b0u_b1u",s0u,b0u,b1u,feats,configuration);
		FeatureUtils.addUnitTripletFeatures(prefix+"b0u_b1u_b2u",b0u,b1u,b2u,feats,configuration);

		
		FeatureUtils.addUnitTripletFeatures(prefix+"s0u_b0u_b1u",s0u,b0u,b1u,feats,configuration);
		FeatureUtils.addHistoryFeatures(configuration,feats);
	
		
		//FeatureUtils.addSpecificMweFeatures(prefix, configuration, feats, s0u,s1u);
		
		//addHistoryFeatures(configuration, feats);
		//addLeftMostDependencyFeatures("lmd_s0u", configuration, s0u, feats);
		//addLeftMostDependencyFeatures("lmd_s1u", configuration, s1u, feats);
		
		//addRightMostDependencyFeatures("rmd_s0u", configuration, s0u, feats);
		//addRightMostDependencyFeatures("rmd_s1u", configuration, s1u, feats);
		
		
		/*
		if(stack.size() - 2 >= 0){
		  Unit s1u = stack.get(stack.size() - 2);
		  addUnitFeatures("s1u", s1u,feats);
		  addUnitPairFeatures("s0u_s1u",s0u,s1u,feats);
		  if(buffer.size() > 0){
			  Unit b0u = buffer.get(0);
			  addUnitTripletFeatures("s0u_s1u_b0u",s0u,s1u,b0u,feats);			  
		  }
		}
		*/
		/*
		if(buffer.size() > 0){
			Unit b0u = buffer.get(0);
			addUnitFeatures("b0u", b0u,feats);
			addUnitPairFeatures("s0u_b0u",s0u,b0u,feats);
		}
		if(buffer.size() > 1){
			Unit b0u = buffer.get(0);
			Unit b1u = buffer.get(1);
			addUnitFeatures("b1u", b1u,feats);
			addUnitPairFeatures("b0u_b1u",b0u,b1u,feats);
			addUnitTripletFeatures("b0u_b1u_s0u",b0u,b1u,s0u,feats);
		}*/
		return feats;
	}
	
	
	
	

}
