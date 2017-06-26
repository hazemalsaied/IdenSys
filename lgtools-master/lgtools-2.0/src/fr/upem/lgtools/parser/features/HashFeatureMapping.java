/**
 * 
 */
package fr.upem.lgtools.parser.features;

import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.util.Collection;

/**
 * @author Mathieu
 *
 */
public class HashFeatureMapping extends FeatureMapping {
     final int modulo;
     
	
	public HashFeatureMapping(int max) {
		super(max);
		modulo = this.max - 1;
	}



	@Override
	public Collection<String> getFeatures() {		
		return null;
	}



	@Override
	public int mappingType() {
		return FeatureMapping.HASH_MAPPING;
	}



	@Override
	public int getFeatureId(String feat, boolean withMemoryIfPossible) {
		/*
		int hashcode = 0;
		 
		for(int i=0;i<feat.length();i++) {
		  //hashcode = 31*hashcode + feat.charAt(i); //non-optimized too much
		  hashcode = (hashcode << 5) - hashcode + feat.charAt(i);
		}
         */
		// hashcode must be comprised between 0 and max */
		
		int hashcode = feat.hashCode();
		hashcode = hashcode&modulo; //hashcode must be lower than max
		hashcode = hashcode<0?-hashcode:hashcode; //hashcode must be positive
		
		
		return hashcode;
	}



	@Override
	public void read(DataInputStream in) throws IOException {
		
		
	}



	@Override
	public void write(DataOutputStream out) throws IOException {
		out.writeInt(mappingType());
		
	}


	
	
	

}
