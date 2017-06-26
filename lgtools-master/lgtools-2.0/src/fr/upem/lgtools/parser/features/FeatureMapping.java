/**
 * 
 */
package fr.upem.lgtools.parser.features;

import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.util.Collection;

/**
 * @author Mathieu Constant
 *
 */
public abstract class FeatureMapping {
	final static int HASHMAP_MAPPING = 1;
	final static int HASH_MAPPING = 2;
   final protected int max;  
	
   FeatureMapping(int max){
	   this.max = (max == Integer.highestOneBit(max))?max: Integer.highestOneBit(max) << 1;
   }
	
   public int getFeatureId(String feat){
	   	return getFeatureId(feat,false);
   }
   
   public int getFeatureIdWithMemory(String feat){
	   	return getFeatureId(feat,true);
  }
   
   abstract public int getFeatureId(String feat, boolean withMemoryIfPossible);
   abstract public Collection<String> getFeatures();
   abstract public int mappingType();
   abstract public void read(DataInputStream in) throws IOException ;
   abstract public void write(DataOutputStream out) throws IOException ;
   
   public int featureCapacity(){
	   return max;
   }
   
   @Override
	public String toString() {
	   StringBuilder sb = new StringBuilder("{");
		for(String f:getFeatures()){
			sb.append(f).append("->").append(getFeatureId(f)).append(", ");
		}
		sb.append("}");
		return sb.toString();
	}
   
   public static FeatureMapping createFeatureMapping(int type, int capacity){
	   switch(type){
	   case HASHMAP_MAPPING:
		   return new HashMapFeatureMapping(capacity);
	   case HASH_MAPPING:
		   return new HashFeatureMapping(capacity);
	   default:
		   throw new IllegalStateException("The feature mapping type "+type+ " does not exist!");
	   }   
		   
   }
   
}
