package fr.upem.lgtools.parser.model;

import fr.upem.lgtools.parser.features.Feature;
import fr.upem.lgtools.parser.features.FeatureVector;

public class Model {
	private final double[] weights;
	private final int nFeatures;
	private final int nLabels;
	private final boolean[] activatedFeatures;
	
		 
	
	
	public Model(int nFeatures,int nLabels){
		this.nLabels = nLabels;
		weights = new double[nFeatures*nLabels];
		this.nFeatures = nFeatures;
		this.activatedFeatures = new boolean[nFeatures];
		
	}
	
	public void setModel(Model newModel){
		if(newModel.nFeatures != this.nFeatures || newModel.nLabels != this.nLabels || newModel.weights.length != this.weights.length){
			throw new IllegalStateException("Cannot set new model if does not same feature and label counts.");
		}
		System.arraycopy(newModel.weights, 0, this.weights, 0, this.weights.length);
	}
	
	
	public Model getAveragedModel(Model averaged, double cnt){
		//TODO: test sizes of models to check compatibility
		Model newModel = new Model(averaged.nFeatures,averaged.nLabels);
		for(int i = 0; i < weights.length ; i++){
			newModel.weights[i] = this.weights[i] - (averaged.weights[i]/cnt);
		}
		return newModel;
		
	}
	
	

	private int getId(int label, int feat){
		return nFeatures*label+ feat;		
	}
	
	
	public static int nextNonZero(int i,Model m){
		while(i < m.weights.length && m.weights[i] == 0 ){
			i++;
		}
		return i;
	}
	
	
	public double getWeight(int i){
		return weights[i];
	}
	
	
	public static boolean compareModels(Model m1, Model m2){
		if(m1.nFeatures != m2.nFeatures){
			System.err.println("Number of features!");
			return false;
		}
		if(m1.nLabels != m2.nLabels){
			System.err.println("Number of labels!");
			return false;
		}
		
		int cnt = 0;
		for(int i = 0 ; i < m1.nFeatures * m1.nLabels ; i++){
			if(m1.weights[i] != m2.weights[i]){
				cnt++;
				//System.err.println(m1.weights[i] + "<>" + m2.weights[i]);
			}
			
		}
		System.err.println(cnt);
		
		return (cnt == 0);
	}
	
	
	public static boolean isEmptyFeatureId(Model m, int f){
		
		for(int l = 0 ; l < m.getLabelCount() ; l++){
			if(m.weights[m.getId(l,f)] != 0.0){
				return false;
			}
		}
		return true;
	}
	
	public static int getNonEmptyFeatureIdCount(Model m){
		int cnt = 0;
		for(int f = 0 ; f < m.getFeatureCount() ; f++){
			
			if(!isEmptyFeatureId(m,f)){
				cnt++;
			}
		}
		return cnt;
	}
	
	
	public static void getNonEmptyIdDistribution(Model m){
		int last = -1;
		boolean first = true;
		for(int f = 0 ; f < m.getFeatureCount() ; f++){
			if(!isEmptyFeatureId(m,f)){
				if(first){
					System.err.println("First non empty id:"+f);
					first = false;
				}
				last =f;
					
			}
		}
		System.err.println("Last non empty id:"+ last);
	}
	
	
	
	/**
	 * 
	 * Sets a weight to a feature with respect to a label
	 * 
	 * @param feat
	 * @param label
	 * @param weight
	 */
	
	
	public void set(int feat, int label, double weight){
		/*
		if(feat >= nFeatures || feat < 0){
			throw new IllegalArgumentException("feature "+feat+" does not exist!");
		}
		if(label < 0 || label >= nLabels){
	    	throw new IllegalArgumentException("Label "+ label + " does not exist!");
	    }*/
		weights[getId(label, feat)] = weight;
		
	}
	
	
	/**
	 * Sets a weight at a given index in array weights
	 * 
	 * @param index 
	 * @param weight
	 */
	
	public void set(int index,double weight){
		weights[index] = weight;
	}
	
	
	/**
	 * gets the weight of a feature with respect to a label
	 * 
	 * @param feat
	 * @param label
	 * @return weight of a feature with respect to a label
	 */
	
	
	public double get(int feat, int label){
		/*
		if(feat >= nFeatures || feat < 0){
			throw new IllegalArgumentException("feature "+feat+" does not exist!");
		}
		if(label < 0 || label >= nLabels){
	    	throw new IllegalArgumentException("Label "+ label + "does not exist!");
	    }*/
		return weights[getId(label, feat)];
	}
	
	/**
	 * 
	 * @return the number of labels
	 */
	
	public int getLabelCount(){
		return nLabels;
	}
	
	/**
	 * 
	 * @return the number of features
	 */
	
	public int getFeatureCount(){
		return nFeatures;
	}
	
	
	
	
	
	
	/**
	 * 
	 * @param feature
	 * @param updatePlus indicates weither the update should be positive (true value) or negative (false value)
	 */
	/*
	private void update(Feature feature, int label, boolean updatePlus){
		int feat = feature.getFeat();
	    if(feat >= nFeatures || feat < 0){
			//double[] tmp = new double[2*weights.length];
			//System.arraycopy(weights, 0, tmp, 0, weights.length);
			//weights = tmp;
	    	throw new IllegalArgumentException("feature "+feat+" does not exist!");
		}
	    if(label < 0 || label >= nLabels){
	    	throw new IllegalArgumentException("Label "+ label + "does not exist!");
	    }
	    int id = getId(label,feat);
	    
	    if(updatePlus){
	    	weights[id] += feature.getValue();	
	    }
	    else{
	    	weights[id] -= feature.getValue();
	    }
		 
	}
	*/
	
	/*
	private void update(Feature feature){
		update(feature,true);
	}*/
	
	
	
	public void updatePlus(FeatureVector feats, int label){
		updatePlus(feats, label, 1.0);
	}
	
	public void updatePlus(FeatureVector feats, int label,double coef){
	    for(Feature feat:feats){
	    	int id = getId(label,feat.getFeat());
		     weights[id] += coef*feat.getValue();
		     activatedFeatures[feat.getFeat()] = true;
	    }	
	}
	
	
	public void updateMinus(FeatureVector feats, int label){
		updateMinus(feats, label, 1.0);
	}
	
	public void updateMinus(FeatureVector feats, int label, double coef){
		for(Feature feat:feats){
	    	int id = getId(label,feat.getFeat());
		     weights[id] -= coef*feat.getValue();	
	    }
	}
	
	
  
	
	
	public double score(FeatureVector feats,int label){
		double sc = 0.0;
		for(Feature f:feats){
			double w = f.getValue();
			int fid = f.getFeat();
			sc += w*weights[getId(label,fid)];
		}
		return sc;
	}
	
	public int getActivatedFeatureCount(){
	    int cnt = 0;
		for( boolean a:activatedFeatures){
			if(a){
			  cnt++;
			}
		}
		return cnt;
	}
	
	
	
	
	@Override
	public String toString() {
		StringBuilder sb = new StringBuilder();
		for(int l = 0 ; l < getLabelCount();l++){
			sb.append(l);
			for(int f = 0 ; f < getFeatureCount() ; f++){
				sb.append("\t").append(weights[getId(l,f)]);
			}
			sb.append("\n");
		}
		return sb.toString();
	}
	
	
}
