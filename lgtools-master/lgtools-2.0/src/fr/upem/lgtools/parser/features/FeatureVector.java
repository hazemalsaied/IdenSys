/**
 * 
 */
package fr.upem.lgtools.parser.features;

import java.util.Iterator;
import java.util.LinkedList;
import java.util.List;

/**
 * @author mconstant
 *
 */
public class FeatureVector implements Iterable<Feature>{
	private final List<Feature> features = new LinkedList<Feature>();
	private final FeatureMapping featureMapping;
	
	
	
	public FeatureVector(FeatureMapping featureMapping) {
		this.featureMapping = featureMapping;
	}


	public void add(String feat){
		features.add(new Feature(featureMapping.getFeatureIdWithMemory(feat)));
	}
	
	public void add(Feature feat){
		features.add(feat);
	}


	@Override
	public Iterator<Feature> iterator() {		
		return new Iterator<Feature>() {
			Iterator<Feature> it = features.iterator();
			
			@Override
			public boolean hasNext() {				
				return it.hasNext();
			}

			@Override
			public Feature next() {
				return it.next();
			}

			@Override
			public void remove() {
				throw new UnsupportedOperationException();
			}
			
		};
	}
	
	
	
}
