package fr.upem.lgtools.parser;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStreamReader;

import com.martiansoftware.jsap.JSAPException;

import fr.upem.lgtools.evaluation.Evaluation;
import fr.upem.lgtools.evaluation.MultipleEvaluation;
import fr.upem.lgtools.evaluation.SimpleEvaluation;
import fr.upem.lgtools.parser.arcstandard.ArcStandardTransitionBasedParserModel;
import fr.upem.lgtools.parser.arcstandard.BaselineFullyMWEAwareArcStandardTransitionBasedModel;
import fr.upem.lgtools.parser.arcstandard.ImplicitCmpFullyMWEAwareArcStandardTransitionBasedModel;
import fr.upem.lgtools.parser.arcstandard.SimpleUnlabeledMergeArcStandardTransitionBasedParserModel;
import fr.upem.lgtools.process.SentenceProcessComposition;
import fr.upem.lgtools.process.TreebankEvaluations;
import fr.upem.lgtools.process.TreebankIO;
import fr.upem.lgtools.process.TreebankProcesses;
import fr.upem.lgtools.text.BufferedDepTreebank;
import fr.upem.lgtools.text.DepTreebank;
import fr.upem.lgtools.text.DepTreebankFactory;
import fr.upem.lgtools.text.StreamDepTreebank;
import fr.upem.lgtools.text.StreamDepTreebank.ReaderType;

public class Parser {
	
	
	private final static int N_EXP = 4;




	public static DepTreebank readTreebank(String filename) throws FileNotFoundException{
		return readTreebank(filename,-1);
	}

	 public static DepTreebank readTreebank(String filename,int size) throws FileNotFoundException{
		BufferedReader reader = new BufferedReader(new InputStreamReader(new FileInputStream(filename)));
		DepTreebank gold = new BufferedDepTreebank(new StreamDepTreebank(reader));
		if(size >= 0){
			gold = DepTreebankFactory.limitSize(gold, size);
		}
		return gold;
	}


	 public static DepTreebank readXConllTreebank(String filename,int size) throws FileNotFoundException{
			BufferedReader reader = new BufferedReader(new InputStreamReader(new FileInputStream(filename)));
			DepTreebank gold = new BufferedDepTreebank(new StreamDepTreebank(reader,ReaderType.XCONLL));
			if(size >= 0){
				gold = DepTreebankFactory.limitSize(gold, size);
			}
			return gold;
		}
	 

/*

	


	public static TransitionBasedSystem<DepTree> trainFullSystem(String filename,String model, int iter, int limit, boolean baseline) throws IOException{
		DepTreebank tb = readTreebank(filename,limit);
		tb = DepTreebankFactory.mergeFixedMWEs(tb);
		tb = DepTreebankFactory.mergeRegularMWEs(tb, Constants.REG_MWE);

		Utils.saveTreebankInXConll(tb, "merged.conll");
		tb = DepTreebankFactory.binarizeMWE(tb, false);
		Utils.saveTreebankInXConll(tb, "binarized.conll");

			
			FeatureMapping fm = new  HashFeatureMapping(4000000);
			FullyMWEAwareArcStandardTransitionBasedModel tbm = baseline?new BaselineFullyMWEAwareArcStandardTransitionBasedModel(fm,tb):new ImplicitCmpFullyMWEAwareArcStandardTransitionBasedModel(fm,tb);
			TransitionBasedSystem<DepTree> parser = new PerceptronTransitionBasedSystem<DepTree>(tbm);
			parser.staticOracleTrain(tb, model,iter);
			fm = null;
			tbm = null;
			parser = null;
			
		return null;
	}



	public static Evaluation parseWithFullSystem(String filename,String model,String output, int limit, boolean baseline) throws IOException{
		
		DepTreebank tb = readTreebank(filename,limit);
		
		FullyMWEAwareArcStandardTransitionBasedModel tbm = baseline?new BaselineFullyMWEAwareArcStandardTransitionBasedModel(model):new ImplicitCmpFullyMWEAwareArcStandardTransitionBasedModel(model);
		TransitionBasedSystem<DepTree> parser = new PerceptronTransitionBasedSystem<DepTree>(tbm);
		//System.err.println(tbm.getTransitions());
		ParsingResult res = parser.greedyParseTreebankAndEvaluate(tb,Constants.MWE_LABEL);
		//ParsingResult res = parser.oracleParseTreebankAndEvaluate(tb);
		tb = DepTreebankFactory.unbinarizeMWE(res.getTreebank(), false);
		tb = DepTreebankFactory.mergeFixedMWEs(tb);
		tb = DepTreebankFactory.mergeRegularMWEs(tb, Constants.REG_MWE);
		Utils.saveTreebankInXConll(tb, output);
		SegmentationAccuracy fixedMwes = SimpleSegmentationAccuracy.computeSegmentationAccuracy(tb,true);
		System.err.println("\nFixed MWEs only:\n"+fixedMwes);
		SegmentationAccuracy mwes = SimpleSegmentationAccuracy.computeSegmentationAccuracy(tb,false);
		System.err.println("\nAll MWEs:\n"+mwes);
		List<SimpleScore> scores = SimpleSegmentationAccuracy.computeMergeParsingScore(tb);
		System.err.println(scores.get(0));
		System.err.println(scores.get(1));
		

		tb = DepTreebankFactory.unmergeFixedMWE(tb, Constants.MWE_LABEL);
		tb = DepTreebankFactory.removeMwePOSInLabels(tb, Constants.MWE_LABEL);
		ParsingAccuracy acc = SimpleParsingAccuracy.computeParsingAccuracy(tb,Constants.MWE_LABEL);
		System.err.println(acc);
		return new SimpleEvaluation(acc, mwes, fixedMwes, scores.get(0), scores.get(1));


	}




	public static void train(String filename,String model, int iter, int limit, boolean withFixedMweOnly) throws IOException{
		DepTreebank tb = readTreebank(filename,limit);
		if(withFixedMweOnly){
			tb = DepTreebankFactory.removeRegularMWEs(tb);
		}

		System.err.println("Model for baseline system");
		FeatureMapping fm = new  HashFeatureMapping(2000000);
		ArcStandardTransitionBasedParserModel tbm = new ArcStandardTransitionBasedParserModel(fm,tb);
		TransitionBasedSystem<DepTree> parser = new PerceptronTransitionBasedSystem<DepTree>(tbm);
		parser.staticOracleTrain(tb, model,iter);
		parser = null;
		tbm = null;
		fm = null;

	}


	public static Evaluation parse(String filename,String model,String output, int limit, boolean withFixedMweOnly) throws IOException{
		DepTreebank tb = readTreebank(filename,limit);
		ArcStandardTransitionBasedParserModel tbm = new ArcStandardTransitionBasedParserModel(model);
		TransitionBasedSystem<DepTree> parser = new PerceptronTransitionBasedSystem<DepTree>(tbm);
		ParsingResult res = parser.greedyParseTreebankAndEvaluate(tb,Constants.MWE_LABEL);		
		tb = DepTreebankFactory.mergeFixedMWEs(res.getTreebank());
		if(!withFixedMweOnly){
			tb = DepTreebankFactory.mergeRegularMWEs(tb, Constants.REG_MWE);
		}
		
		tb = DepTreebankFactory.removeMwePOSInLabels(tb, Constants.MWE_LABEL);

		
		SegmentationAccuracy fixedMwes = SimpleSegmentationAccuracy.computeSegmentationAccuracy(tb,true);
		System.err.println(fixedMwes);
		SegmentationAccuracy mwes = null;
		if(!withFixedMweOnly){
			mwes = SimpleSegmentationAccuracy.computeSegmentationAccuracy(tb,false);
			System.err.println(mwes);
		}
		
		List<SimpleScore> scores = SimpleSegmentationAccuracy.computeMergeParsingScore(tb);
		System.err.println(scores.get(0));
		System.err.println(scores.get(1));
		


		DepTreebank tmp = DepTreebankFactory.removeMwePOSInLabels(res.getTreebank(), Constants.MWE_LABEL);
		if(withFixedMweOnly){
			tmp = DepTreebankFactory.removeRegularMWEs(tmp);
		}
		
		ParsingAccuracy acc = SimpleParsingAccuracy.computeParsingAccuracy(tmp,Constants.MWE_LABEL);
		Utils.saveTreebankInXConll(tmp, output);
		System.err.println(acc);
		return new SimpleEvaluation(acc, mwes, fixedMwes, scores.get(0), scores.get(1));

	}


	public static void trainWithMerge(String filename,String model, int iter, int limit) throws IOException{
		DepTreebank tb = readTreebank(filename,limit);
		tb = DepTreebankFactory.removeRegularMWEs(tb);
		tb = DepTreebankFactory.mergeFixedMWEs(tb);
		Utils.saveTreebankInXConll(tb, "merged.conll");
		tb = DepTreebankFactory.binarizeMWE(tb, false);
		Utils.saveTreebankInXConll(tb, "binarized.conll");

		FeatureMapping fm = new  HashFeatureMapping(2000000);
		SimpleMergeArcStandardTransitionBasedParserModel tbm = new SimpleLabeledMergeArcStandardTransitionBasedParserModel(fm,tb);
		TransitionBasedSystem<DepTree> parser = new PerceptronTransitionBasedSystem<DepTree>(tbm);
		parser.staticOracleTrain(tb, model,iter);
		parser = null;
		fm = null;
		tbm = null;
	}
	
	 public static Evaluation parseWithMerge(String filename,String model,String output,int limit) throws IOException{
		DepTreebank tb = readTreebank(filename,limit);
		SimpleMergeArcStandardTransitionBasedParserModel tbm = new SimpleLabeledMergeArcStandardTransitionBasedParserModel(model);
		TransitionBasedSystem<DepTree> parser = new PerceptronTransitionBasedSystem<DepTree>(tbm);
		ParsingResult res = parser.greedyParseTreebankAndEvaluate(tb,Constants.MWE_LABEL);

		tb = DepTreebankFactory.removeRegularMWEs(res.getTreebank());
		tb = DepTreebankFactory.unMergeMWE(tb, Constants.MWE_LABEL);
		tb = DepTreebankFactory.removeMwePOSInLabels(tb, Constants.MWE_LABEL);
		
		ParsingAccuracy acc = SimpleParsingAccuracy.computeParsingAccuracy(tb,Constants.MWE_LABEL);
		System.err.println(acc);
		Utils.saveTreebankInXConll(tb, output);
		tb = DepTreebankFactory.mergeFixedMWEs(tb);
		SegmentationAccuracy fixedMwes = SimpleSegmentationAccuracy.computeSegmentationAccuracy(tb,true);
		System.err.println(fixedMwes);
		
		List<SimpleScore> scores = SimpleSegmentationAccuracy.computeMergeParsingScore(tb);
		System.err.println(scores.get(0));
		System.err.println(scores.get(1));
		
		return new SimpleEvaluation(acc, null, fixedMwes, scores.get(0), scores.get(1));
	}
	*/
	
	
	
	
	
	
	
	
	private static void train(Parameters parameters) throws IOException{
		System.err.println("--------- New model  -----");
		//ArcStandardTransitionBasedParserModel tbm = null;
		
		DepTreebank tb; 
		if(parameters.xconll){
		  tb = readXConllTreebank(parameters.train,parameters.trainSize); //treebank in conll format; MWEs with specific arc labels (MWE_LABEL for fixed MWEs; REG_MWE for regular MWEs) 
		}
		else{
			tb = readTreebank(parameters.train,parameters.trainSize);
		}
		  SentenceProcessComposition spc = new SentenceProcessComposition();
		  spc.add(TreebankProcesses.copyGold());
		  //spc.add(TreebankIO.saveInXConll("tmpx.conll"));
		if(!parameters.fixedMweOnly){
			//trainFullSystem(parameters.train, parameters.model, parameters.iters, -1, true);
			if(parameters.baseline){
				if(parameters.xconll){
				   spc.add(TreebankProcesses.unmergeRegularMWE());
				}
				spc.add(TreebankIO.saveInXConll("tmp.conll"));
			}
			else{
				//spc.add(TreebankIO.saveInXConll("tmp.conll"));
				spc.add(TreebankProcesses.mergeFixedMWEs());
				spc.add(TreebankProcesses.mergeRegularMWEs());
				//spc.add(TreebankIO.saveInXConll("tmp1.conll"));
				spc.add(TreebankProcesses.binarizeMWE(false));
				//spc.add(TreebankIO.saveInXConll("tmp.conll"));
				
			}
			
		}
		else{
			spc.add(TreebankProcesses.removeRegularMWEs());//in case treebank contains regular MWEs
			//spc.add(TreebankProcesses.removeMwePosInLabels());  //put an option in case one wants to keep mwe pos label
			//spc.add(TreebankIO.saveInXConll("tmp1.conll"));
			
			if(parameters.baseline){
				//spc.add(TreebankIO.saveInXConll("tmp.conll"));
				
				
			}
			else{
				spc.add(TreebankProcesses.mergeFixedMWEs());
				spc.add(TreebankProcesses.binarizeMWE(false));
				//spc.add(TreebankIO.saveInXConll("tmp.conll"));
				
				
				
				
			//trainWithMerge(parameters.train, parameters.model, parameters.iters, -1);	
			}
		}
		

		
		TreebankProcesses.staticOracleTrain(tb, spc, parameters);
	}
	
	
	private static ArcStandardTransitionBasedParserModel getModel(Parameters parameters,String model) throws IOException{
		if(parameters.baseline){
	         return new ArcStandardTransitionBasedParserModel(model);		
		}
		else{
		     if(parameters.fixedMweOnly){
				return new SimpleUnlabeledMergeArcStandardTransitionBasedParserModel(model);
		     }
		     else{
		    	 if(parameters.implicitComplete){
		    		 return new ImplicitCmpFullyMWEAwareArcStandardTransitionBasedModel(model,false);	 
		    	 }
		    	 else{
		    		 return new BaselineFullyMWEAwareArcStandardTransitionBasedModel(model);	 
		    	 }
		    	 
		    	 
		     }
		}
		
		
	}
	
	private static Evaluation simpleParse(Parameters parameters, String model, ExternalData data) throws IOException{
		
		DepTreebank tb;
		if(parameters.xconll){
			tb = readXConllTreebank(parameters.input,-1);
		}
		else{
		   tb = readTreebank(parameters.input);
		}
		ArcStandardTransitionBasedParserModel tbm = getModel(parameters,model);
		TransitionBasedSystem<DepTree> parser = new PerceptronTransitionBasedSystem<DepTree>(tbm);
		SimpleEvaluation eval =new SimpleEvaluation();
		SentenceProcessComposition spc = new SentenceProcessComposition();

		
		spc.add(TreebankProcesses.greedyParse(parser,data));
		
		if(parameters.baseline){
		    spc.add(TreebankEvaluations.computeParsingAccuracy());
		    if(parameters.output != null){
				spc.add(TreebankIO.saveInConll(parameters.output));
			}
		}
		else{
			if(parameters.output != null){
				//spc.add(TreebankProcesses.unbinarizeMWE(false));
				//spc.add(TreebankIO.saveInXConll(parameters.output+".xconll"));
			}
			spc.add(TreebankProcesses.unbinarizeMWE(false));
			
		}
		
		//spc.add(TreebankIO.saveInXConll("tmp.conll"));
		
		
		
		if(parameters.fixedMweOnly){
			spc.add(TreebankProcesses.removeRegularMWEs());//in case treebank contains regular MWEs
			
	    }
		
		//spc.add(TreebankProcesses.unlabelMWEArcs());
		if(parameters.baseline){
		   spc.add(TreebankProcesses.mergeFixedMWEs());
		
		   spc.add(TreebankProcesses.mergeRegularMWEs());
		}
		
		spc.add(TreebankEvaluations.computeSegmentationAccuracy(false));
		spc.add(TreebankEvaluations.computeSegmentationAccuracy(true));
		//spc.add(TreebankEvaluations.computeSegmentationParsingScore());
		
		
		//spc.add(TreebankIO.saveInXConll("out.conll"));
		spc.add(TreebankProcesses.unmergeFixedMWE());
		//spc.add(TreebankIO.saveInXConll("unmerge.conll"));
		
		
		
		/*
		if(parameters.output != null){
			spc.add(TreebankIO.saveInXConll(parameters.output));
		}
		*/
	   
	   
	    
	   if(!parameters.baseline){
	    spc.add(TreebankEvaluations.computeParsingAccuracy());
	    
		if(parameters.output != null){
			spc.add(TreebankIO.saveInConll(parameters.output));
		}
		
	   }
	    
		
		TreebankProcesses.processTreebank(tb, spc, eval);
		
		return eval;
	}
	
	
	private static void parse(Parameters parameters) throws IOException{
		ExternalData data = new ExternalData(parameters.external);
		if(parameters.repeats > 1){
			MultipleEvaluation meval = new MultipleEvaluation();
		   
			   for(int i = 0 ; i < parameters.repeats ; i++){
				   System.err.println("Parsing model "+i);
				   Evaluation eval = simpleParse(parameters, parameters.model+"-"+i+".final",data);
				   meval.add(eval);
				    
			   }
		   //System.out.println("Global evaluation ");
		   System.out.println(parameters.model);
			   System.out.println(meval);
		}
		else{
			System.err.println(parameters.model);
			System.out.println(simpleParse(parameters, parameters.model+".final",data));
		}
		
	}
	
	
	public static void main(String[] args) throws JSAPException, IOException {
		Parameters parameters = new Parameters(args);
			
		
		System.err.println("Model: "+parameters.model);
		System.err.println("Train dataset: "+parameters.train);
		System.err.println("Input: "+parameters.input);
		System.err.println("Output: "+parameters.output);
		System.err.println("Model size: "+parameters.modelSize);
		System.err.println("Iterations: "+parameters.iters);
		System.err.println("Repeat:"+parameters.repeats);
		System.err.println("Size: "+parameters.trainSize);
		System.err.println("Projective: "+parameters.projective);
		System.err.println("External resource: "+parameters.external);
		
		if(parameters.train != null){
			train(parameters);    
		}
		
		if(parameters.input != null){
			parse(parameters);
		}
		
		
		
		
		//full system
		    //baseline
		    //merge
		         //no constraints (left/right)
		         //implicit complete (left/right)
		         //constrained merge with implicit complete (right)
		         
		
		//fixed MWE system
		    //baseline
		    //merge
		        //right
		        //left
		
		//no syntactic
		    //fixed MWE
		         //baseline
		         //merge
		              //right
		              //left
		    //all MWEs
		         //baseline
		         //merge
		             //right
		             //left
		
	}

}
