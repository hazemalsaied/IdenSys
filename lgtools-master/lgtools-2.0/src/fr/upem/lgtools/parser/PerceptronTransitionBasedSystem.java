/**
 * 
 */
package fr.upem.lgtools.parser;

import java.io.IOException;

import fr.upem.lgtools.parser.features.FeatureVector;
import fr.upem.lgtools.parser.model.Model;
import fr.upem.lgtools.parser.model.TransitionBasedModel;
import fr.upem.lgtools.parser.transitions.Transition;
import fr.upem.lgtools.text.DepTreebank;
import fr.upem.lgtools.text.Sentence;
import fr.upem.lgtools.text.Utils;

/**
 * @author Mathieu
 *
 */
public class PerceptronTransitionBasedSystem<T extends Analysis> extends TransitionBasedSystem<T> {

	public PerceptronTransitionBasedSystem(TransitionBasedModel<T> tbm) {
		super(tbm);
	}

	
	@Override
	public void inexactSearchTrain(DepTreebank tb, DepTreebank dev, String modelFilename, int iterations, int k, ExternalData data) throws IOException{
		tb = tbm.filter(tb);
	   	 Model averaged = new Model(tbm.getFeatureCount(),tbm.getLabelCount());
	   	int step = 1;
	   	for(int i = 0 ; i < iterations ; i++){
	   		 System.err.println("Iteration "+ (i+1));
	   		 int cnt = 0;
	   		 int sent = 0;
	   		 int total = 0;
	   		 
	   		for(Sentence gold:tb.shuffle()){
	   			sent++;
	   			if(sent % 1000 == 0){System.err.println("Processed "+ sent+ " sentences");}
	   			ParseHypothesis<T> hyp = beamSearchParse(gold, k, true, data);
	   			System.err.println("Result parse:");
	   			System.err.println(hyp);
	   			if(!hyp.isGold()){
	   				tbm.update(hyp.getFeatures(),hyp.getGoldHypothesis().getTransition(),hyp.getTransition(),averaged,step);
	   				System.err.println(hyp.getGoldHypothesis().getTransition()+"=="+hyp.getTransition());
	   			}
	   			step++;
	   			cnt += hyp.getConfiguration().getHistory().size();
	   			total += gold.getTokens().size()*2;	   			
	   		}
	   		System.err.println("Accuracy on training transition sequence: "+((double)cnt)/total+ "  ("+cnt+"/"+total+")");
	       	 System.err.println("Number of sentences: "+sent);	   	    
	   	}   	
	   	tbm.setModel(tbm.getAveragedModel(averaged,step));
	   	 tbm.save(modelFilename+".final");
	   	 System.err.println("Done.");
	}
	
	
	
	@Override
	public void staticOracleTrain(DepTreebank tb, DepTreebank dev, String modelFilename, int iterations, ExternalData data) throws IOException{
	 
   	 tb = tbm.filter(tb);
   	 Model averaged = new Model(tbm.getFeatureCount(),tbm.getLabelCount());
   	 System.err.println(tbm.getTransitions());
   	 int step = 1;
   	 for(int i = 0 ; i < iterations ; i++){
   		 System.err.println("Iteration "+ (i+1));
   		 int cnt = 0;
   		 int sent = 0;
   		 int total = 0;
   		 int unkTransBug = 0;
   		 int illegalStateBug = 0;
   		 
   		 boolean stop = false;
   		 for(Sentence gold:tb.shuffle()){
   			 sent++;
   			 if(sent % 500 == 0){System.err.println("Processed "+ sent+ " sentences");}
   			 Configuration<T> c = tbm.getInitialConfiguration(gold,true);
   			 stop = false;
   			 //System.err.println("#############################");
   			//System.err.println(gold.getTokenSequence(true));
   			 //if(!Utils.isProjectiveSentence(c.getSentence())){
   				//System.err.println(gold.getTokenSequence(true));
   			     //System.err.println("NON PROJECTIVE");
   			 //System.err.println(c.getProjectiveOrderPosition());
   			 //}
   			 
   			 while(!c.isTerminal() && !stop){
   				 FeatureVector fv = tbm.extractFeatures(c,data);
   				 Transition<T> pt = tbm.getBestValidTransition(fv,c);
   				 Transition<T> ot = tbm.getBestCorrectTransition(fv,c);
   				 
   				 if(ot == null){
   					 System.err.println("Unknown transition due to SWAP in non-projective sentence?");
   					System.err.println(gold.getTokenSequence(true));
   					unkTransBug++; 
   					break;
   				 }
   				 
   				//if(!Utils.isProjectiveSentence(c.getSentence())){
   				//System.err.println("CONF="+c);
   				//System.err.println("valid: "+tbm.getValidTransitions(c));
   				//System.err.println(c.getHistory());
   				  
   				//System.err.println(c.getAnalyses());
   				 
   				 //System.err.println("gold="+ot+"--predicted="+pt);
   				//}
   				 
   				//System.err.println("PT "+pt);
   				//System.err.println("OT "+ot);
   				//System.err.println(c.getSentence().getUnits());
   				
   				//System.err.println("CONF="+c);
   				//System.err.println("COPY="+new Configuration<T>(c));
   				 if(pt.equals(ot)){ // true prediction
   					 //System.err.println("true="+ot);
   					 try{
   					   c = pt.performAll(c);
   					 }
   					 catch(IllegalStateException e){
   						System.err.println("Illegal state in parser due to embedding or conversion:");
   	   					System.err.println(gold.getTokenSequence(true));
   	   				illegalStateBug++;
   	   					break;
   					 }
   					 cnt++;
   				 }
   				 else{  //false prediction
   					 //System.err.println("true="+ot+"--false="+pt);
   				     //System.err.println("valid: "+tbm.getValidTransitions(c));
   					 tbm.update(fv,ot,pt,averaged,step);
   					 stop = false;//early update if stop == true
   					 if(!stop){
   						 try{
   					    c = ot.performAll(c);
   						 }
   						 catch(IllegalStateException e){
   						System.err.println("Illegal state in parser due to embedding or conversion:");
   	   					System.err.println(gold.getTokenSequence(true));
   	   				illegalStateBug++; 
   	   					break;
   					 }
   					 }
   				 }
   				
   				 
   				 total++;
   				 //System.err.println(c);
   				 //System.err.println(tbm);
   				step++;
   			 }
   			 //System.err.println(c.getAnalyses());
   			 
   		 }
   		/* 
   		 * TODO: add this but be clever!
   		 * 
   		 * if(dev != null){
   			 Model old = tbm.getModel();
   			Model a = tbm.getAveragedModel(averaged,step);
   			tbm.setModel(a);
   			greedyParseTreebankAndEvaluate(dev);
   			a = null;
   			tbm.setModel(old);
   			
   		 }*/
   		 
   		 //TransitionBasedModel2.save(tbm, modelFilename+"."+(i+1));
   		 System.err.println("Accuracy on training transition sequence: "+((double)cnt)/total+ "  ("+cnt+"/"+total+")");
   		 System.err.println("Ratio of activated features: "+tbm.getActivatedFeatureRatio());
	       	 System.err.println("Number of sentences: "+sent);
	       	 System.err.println("Sentences with bugs: "+unkTransBug+ " unknown trans. and "+ illegalStateBug + " illegal state bugs");
   	 }
   	 tbm.setModel(tbm.getAveragedModel(averaged,step));
   	 tbm.save(modelFilename+".final");
   	 System.err.println("Done.");
   	 
    }
	
	
}
