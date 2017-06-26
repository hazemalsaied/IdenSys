/**
 * 
 */
package fr.upem.lgtools.parser.features;

import java.util.Collection;
import java.util.HashSet;

/**
 * @author Matthieu Constant
 *
 */
public class HashFeatureMappingWithMemory extends HashFeatureMapping {
    private final HashSet<String> features = new HashSet<String>();
	
	public HashFeatureMappingWithMemory(int max) {
		super(max);		
	}

	@Override
	public Collection<String> getFeatures() {		
		return features;
	}

	@Override
	public int getFeatureId(String feat, boolean withMemoryIfPossible) {
		if(withMemoryIfPossible){
			features.add(feat);
		}
		return super.getFeatureId(feat, withMemoryIfPossible);
	}
	
	
	

}
