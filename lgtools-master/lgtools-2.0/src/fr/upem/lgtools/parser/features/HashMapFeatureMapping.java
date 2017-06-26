/**
 * 
 */
package fr.upem.lgtools.parser.features;

import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.util.Collection;
import java.util.HashMap;
import java.util.Map;

/**
 * @author Mathieu
 *
 */
public class HashMapFeatureMapping extends FeatureMapping{
	

	private final Map<String, Integer> features;
	
	public HashMapFeatureMapping(int max) {
		super(max);
		features = new HashMap<String,Integer>();
	}
	
	public HashMapFeatureMapping(int max, Map<String,Integer> map){
		super(max);
		features = map;
	}
	
	@Override
	public int mappingType() {
		return FeatureMapping.HASHMAP_MAPPING;
	}
	
	// to be used at parsing time
	public int getFeatureId(String feat){		
		return getFeatureId(feat,false);
	}

	
	@Override
	public int getFeatureId(String feat, boolean withMemoryIfPossible) {
		Integer id = features.get(feat);
		if(id == null){
			if(!withMemoryIfPossible){
				return -1;
			}
			else{
				if(features.size() == featureCapacity()){
					throw new IllegalStateException("Number of features is too large: it should not exceed "+features.size());
				}
			}
			
			id = features.size();
			features.put(feat, id);
		}
		
		return id;
		
	}
	
	
	

	@Override
	public void read(DataInputStream in)  throws IOException{
		int nFeats = in.readInt();
		
		for(int f = 0 ; f < nFeats; f++){
			String fval = in.readUTF();
			int fid = in.readInt();
			this.features.put(fval, fid);
		}
		
	}

	@Override
	public void write(DataOutputStream out) throws IOException {
		out.writeInt(FeatureMapping.HASHMAP_MAPPING); 
		int nFeats = getFeatures().size();
		out.writeInt(nFeats);
		for(String k:getFeatures()){
			out.writeUTF(k);
			out.writeInt(getFeatureId(k));
		}
	}

	@Override
	public Collection<String> getFeatures() {		
		return features.keySet();
	}

}
