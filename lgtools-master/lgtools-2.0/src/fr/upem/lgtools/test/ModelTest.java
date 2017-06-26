package fr.upem.lgtools.test;

import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertTrue;

import org.junit.Test;

import fr.upem.lgtools.parser.model.Model;

public class ModelTest {

	@Test
	public void testGetSet() {
		Model model =new Model(5,3);
		for(int f = 0; f < model.getFeatureCount() ; f++){
			for(int l=0;l < model.getLabelCount() ; l++){
				model.set(f,l,f+l);
				assertFalse(model.get(f, l) != (f+l));
			}
		}
		
		assertTrue(true);
	}

	/*
	private FeatureVector featuresAllVal(int nFeats,double val){
		FeatureVector feats = new FeatureVector();
		for(int f = 0 ; f < nFeats ; f++){
			feats.add(new Feature(f, val));
		}
		return feats;
	}
	*/
	
	
	private Model fillSum(){
		Model model =new Model(5,3);
		int nFeats = model.getFeatureCount() ;
		for(int f = 0; f < nFeats; f++){
			for(int l=0;l < model.getLabelCount() ; l++){
				model.set(f,l,f+l);
			}
		}
		return model;
	}
	
	private Model fillVal(int val){
		Model model =new Model(5,3);
		int nFeats = model.getFeatureCount() ;
		for(int f = 0; f < nFeats; f++){
			for(int l=0;l < model.getLabelCount() ; l++){
				model.set(f,l,val);
			}
		}
		return model;
	}
	
	private Model fillValIncrement(){
		Model model =new Model(5,3);
		int nFeats = model.getFeatureCount() ;
		for(int f = 0; f < nFeats; f++){
			for(int l=0;l < model.getLabelCount() ; l++){
				model.set(f,l,l);
			}
		}
		return model;
	}
	
	/*
	
	@Test
	public void testScoreAllFeatures(){
		Model model = fillVal(2);
		FeatureVector feats = featuresAllVal(model.getFeatureCount(),1.0);
		for(int l=0;l < model.getLabelCount() ; l++){
			assertFalse(model.score(feats, l) != 2*model.getFeatureCount());
		}
		
		//model.score(feats, label);
	}
	
	*/
	
/*
	@Test
	public void testUpdateIterableOfFeatureInt() {
		Model model = fillSum();
		List<Feature> feats = featuresAllVal(model.getFeatureCount(),1.0);
		
		int nFeats = model.getFeatureCount() ;
		
		for(int l=0;l < model.getLabelCount() ; l++){
			model.update(feats, l,false);
		}
		
		for(int f = 0; f < nFeats ; f++){
			for(int l=0;l < model.getLabelCount() ; l++){
				assertFalse(model.get(f, l) != (f+l-1.0));
			}
		} 
		assertTrue(true);
	}

	*/
	
	

}
