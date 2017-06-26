/**
 * 
 */
package fr.upem.lgtools.parser;

import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.Collections;
import java.util.Iterator;
import java.util.LinkedList;
import java.util.List;
import java.util.Set;

import fr.upem.lgtools.parser.features.FeatureVector;
import fr.upem.lgtools.parser.model.TransitionBasedModel;
import fr.upem.lgtools.parser.transitions.Transition;
import fr.upem.lgtools.text.DepTreebank;
import fr.upem.lgtools.text.Sentence;
import fr.upem.lgtools.text.Unit;


/**
 * @author Mathieu
 *
 */
public abstract class TransitionBasedSystem<T extends Analysis> {
     final TransitionBasedModel<T> tbm;
     
     
     public TransitionBasedSystem(TransitionBasedModel<T> tbm){
    	 this.tbm = tbm;
     }
	
     
     public TransitionBasedModel<T> getModel(){
    	 return tbm;
     }
     
     
     private void initSentence(Sentence s){
    	 for(Unit u:s.getUnits()){
    		 u.setShead(-1);
    		 u.setPredictedLhead(0);
    		 u.setPredictedSlabel(null);
    	 }
    	 
     }
     
     public T greedyParse(Sentence s, ExternalData data){
    	initSentence(s);
 		Configuration<T> c = tbm.getInitialConfiguration(s,false);
 		//System.err.println(s.getTokens());
 		//System.err.println(tbm.getModel());
 		//System.err.println();
 		//System.err.println(s.getTokenSequence(false));
 		while(!c.isTerminal()){
 			FeatureVector fv = tbm.extractFeatures(c,data);
 			//System.err.println(c.getSentence().getUnits());
			Transition<T> t = tbm.getBestValidTransition(fv,c);
			//Transition<T> o = tbm.getBestCorrectTransition(fv,c);
			//System.err.println(tbm.getTransitions());
		    //System.err.println(tbm.getValidTransitions(c));
		    //System.err.println(c);
		    //System.err.println("PRED: "+t);
			
			//System.err.println("G: "+o);
			
			//System.err.println(c.getAnalyses());
 			c = t.performAll(c);
 			//System.err.println("JJ");
 		}
 		//System.err.println("CCC");
 		//System.err.println(s.getTokenSequence(true));
 		//System.err.println(s.getTokenSequence(false));
 		return c.getAnalyses();
 	}
    
     
     private boolean beamHasOnlyTerminalConfigurations(LinkedList<ParseHypothesis<T>> beam){
    	 for(ParseHypothesis<T> h:beam){
    		 if(!h.getConfiguration().isTerminal()){
    			 return false;
    		 }
    	 }
    	 return true;
     }
     
     
     /*
     private FeatureVector addFeatureVectors(FeatureVector fv1, FeatureVector fv2){
    	 FeatureVector fv = new FeatureVector(tbm.getFeatures());
    	 for(Feature f:fv1){
    		 fv.add(f);
    	 }
    	 for(Feature f:fv2){
    		 fv.add(f);
    	 }
    	 
    	 return fv;
    	 
     }
     */
     
     
     private static <T extends Analysis> LinkedList<ParseHypothesis<T>> prune(LinkedList<ParseHypothesis<T>> newBeam, int k){
    	 LinkedList<ParseHypothesis<T>> beam = new LinkedList<ParseHypothesis<T>>();
		 Iterator<ParseHypothesis<T>> it = newBeam.iterator();
		 for(int i = 0 ; i < k ; i++){
			 if(it.hasNext()){
				 ParseHypothesis<T> ph = it.next(); 
			    beam.add(ph);
			    //System.err.print(ph.getScore()+ "#");
			 }
		 }
		 return beam;
     }
     
     
     private static <T extends Analysis> boolean goldIsOffTheBeam(List<ParseHypothesis<T>> beam){
    	 
    	 for(ParseHypothesis<T> h:beam){
    		if(h.isGold()){
    			return false;
    		} 
    	 }    	 
    	 return true;
     }
     
     
     public ParseHypothesis<T> beamSearchParse(Sentence s, int k, boolean returnWhenFail, ExternalData data){
    	 Configuration<T> c0 = tbm.getInitialConfiguration(s,false);
    	 ParseHypothesis<T> h0 = new ParseHypothesis<T>(c0, 0.0, new FeatureVector(tbm.getFeatures()),null,true,null);
    	 LinkedList<ParseHypothesis<T>> beam = new LinkedList<ParseHypothesis<T>>();
    	 beam.add(h0);
    	 ParseHypothesis<T> gold = h0;
    	     	 
    	 //System.err.println(units);
    	 
    	 while(!beamHasOnlyTerminalConfigurations(beam)){    	     
    		 
    		 LinkedList<ParseHypothesis<T>> newBeam = new LinkedList<ParseHypothesis<T>>();
    		 for(ParseHypothesis<T> h:beam){
    			 //System.err.println("START="+h);
    			 Configuration<T> c = h.getConfiguration();
    			 FeatureVector fv = tbm.extractFeatures(c,data);
    			 Set<Transition<T>> transitions = tbm.getValidTransitions(c);
    			 //System.err.println(transitions);
    			 if(transitions.isEmpty()){
    				 newBeam.add(h);
    			 }
    			 else{  
    				 
    				 for(Transition<T> t:transitions){
    				     double newScore = tbm.getScore(fv,t);
    				     Configuration<T> newConfig = Configurations.createDefaultConfiguration(c); 
    				     //System.err.println("NEW="+newConfig);
    				     //System.err.println("OLD="+c);
    				     newConfig = t.performAll(newConfig);
    				     newConfig.getHistory().add(t.id());
    				     boolean isGold = h.isGold();
    				     if(returnWhenFail && isGold){
    				    	 isGold = newConfig.getAnalyses().isGold(s.getTokens());    
    				    	 //System.err.println(isGold);
    				     }    				     
    				     ParseHypothesis<T> newHyp = new ParseHypothesis<T>(newConfig, newScore, fv, h,isGold,t);
    				     
    				     newBeam.add(newHyp);
    				     if(isGold){
    				    	 gold = newHyp;
    				     }
    				 } 
    				 Collections.sort(newBeam);
    			 }    			 
    		 } 
    		 
    		 beam = prune(newBeam,k);
    		 //for(ParseHypothesis<T> h:beam){
    			 //System.err.println("DEST="+h);
    		 //}
    		 //System.err.println(beam);
    		 //ParseHypothesis<T> h1 = beam.getFirst();
    		 //System.err.println(h1.getTransition()+"="+h1.getConfiguration());
    		 
    		 if(returnWhenFail && goldIsOffTheBeam(beam)){
    			 //System.err.println("OFFBEAM");
    			 ParseHypothesis<T> h = beam.getFirst();
    			 h.setGoldHypothesis(gold);
    			 
    			 return h;    			 
    		 }
			 //System.err.println();
			 
			 //ParseHypothesis<T> ht = beam.getFirst();
			 //System.err.println(ht.getConfiguration());
    	 }
    	 ParseHypothesis<T> h = beam.getFirst();
    	 h.setGoldHypothesis(gold);
    	 return h;
    	 
     }
     
     
     
     public T oracleParse(Sentence s){
  		Configuration<T> c = tbm.getInitialConfiguration(s,true);
  		while(!c.isTerminal()){
  			//System.err.println(c);
  			Transition<T> t = tbm.staticOracle(c); 
  			//System.err.println(t);
  			c = t.performAll(c);
  		}
  		return c.getAnalyses();
  	}
     
   
     private static interface ParsingMethod<A>{
    	 public A parse(Sentence s);
     }
     
     
 	
 	public DepTreebank parseTreebank(final DepTreebank tb, final ParsingMethod<T> pm) throws FileNotFoundException{
 		return new DepTreebank() {

			@Override
			public Iterator<Sentence> iterator() {
				return new Iterator<Sentence>() {
					Iterator<Sentence> it = tb.iterator();
                    int cnt = 0;
					@Override
					public boolean hasNext() {
						return it.hasNext();
					}

					@Override
					public Sentence next() {
						Sentence s = it.next();
						T analysis = pm.parse(s);
			 			//System.err.println(analysis);
			 			tbm.updateSentenceAfterAnalysis(s,analysis); 
			 			//System.err.println(s.getTokenSequence(false));
			 			cnt++;
			 			if(cnt%300 == 0){
			 				System.err.println(cnt+" sentences parsed.");
			 			}
						return s;
					}

					@Override
					public void remove() {
						throw new IllegalStateException();

					}
				};
			}
		};
 		/*
 		int cnt = 0;
 		for(Sentence s:tb){
 			T analysis = pm.parse(s);
 			//System.err.println(analysis);
 			tbm.updateSentenceAfterAnalysis(s,analysis); 
 			//System.err.println(s.getTokenSequence(false));
 			cnt++;
 			if(cnt%300 == 0){
 				System.err.println(cnt+" sentences parsed.");
 			} 			
 		} 
 		
 		return tb;
 		*/
 	}
    
/* 	
public ParsingResult parseTreebankAndEvaluate(DepTreebank tb, ParsingMethod<T> pm, String mweLabel) throws IOException{
 	   tb = parseTreebank(tb,pm); 
 	  //Utils.saveTreebankInXConll(tb, "tmp.conll");
 	   ParsingAccuracy eval = SimpleParsingAccuracy.computeParsingAccuracy(tb,mweLabel);
	   //System.err.println(eval);
 		return new ParsingResult(tb,eval);
 		
 	}
	
 	
public ParsingResult oracleParseTreebankAndEvaluate(DepTreebank tb, String mweLabel) throws IOException{
	  return parseTreebankAndEvaluate(tb, new ParsingMethod<T>() {

		@Override
		public T parse(Sentence s) {
			return oracleParse(s);
		}
		  
	},mweLabel);
	}

 */    
 	
/*	
public ParsingResult greedyParseTreebankAndEvaluate(DepTreebank tb, String mweLabel) throws IOException{
  return parseTreebankAndEvaluate(tb, new ParsingMethod<T>() {

	@Override
	public T parse(Sentence s) {
		return greedyParse(s);
	}
	  
}, mweLabel);
}
*/

/*
public ParsingResult beamSearchParseTreebankAndEvaluate(DepTreebank tb,final int k, String mweLabel) throws IOException{
	  return parseTreebankAndEvaluate(tb, new ParsingMethod<T>() {

		@Override
		public T parse(Sentence s) {
			return beamSearchParse(s, k,false).getConfiguration().getAnalyses();
		}
		  
	}, mweLabel);
	}


  

   public void inexactSearchTrain(DepTreebank tb, String modelFilename, int iterations,int beamSize) throws IOException{
	   inexactSearchTrain(tb, null, modelFilename, iterations,beamSize);
   }
   

    
     
     public void staticOracleTrain(DepTreebank tb, String modelFilename, int iterations) throws IOException{
    	 staticOracleTrain(tb, null, modelFilename, iterations);
     }
     
  */   
 	 abstract public void staticOracleTrain(DepTreebank tb, DepTreebank dev, String modelFilename, int iterations, ExternalData data) throws IOException;
 	 abstract void inexactSearchTrain(DepTreebank tb, DepTreebank dev, String modelFilename, int iterations, int beamSize, ExternalData data) throws IOException;
}
