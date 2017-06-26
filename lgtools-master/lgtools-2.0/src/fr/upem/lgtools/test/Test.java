package fr.upem.lgtools.test;

import java.io.IOException;

import fr.upem.lgtools.evaluation.Evaluation;
import fr.upem.lgtools.evaluation.SimpleEvaluation;
import fr.upem.lgtools.parser.DepTree;
import fr.upem.lgtools.parser.ExternalData;
import fr.upem.lgtools.parser.Parser;
import fr.upem.lgtools.parser.PerceptronTransitionBasedSystem;
import fr.upem.lgtools.parser.TransitionBasedSystem;
import fr.upem.lgtools.parser.mwereco.MweRecognizerModel;
import fr.upem.lgtools.process.SentenceProcessComposition;
import fr.upem.lgtools.process.TreebankEvaluations;
import fr.upem.lgtools.process.TreebankIO;
import fr.upem.lgtools.process.TreebankProcesses;
import fr.upem.lgtools.text.DepTreebank;

public class Test {
   
	
	public static TransitionBasedSystem<DepTree> trainMweSystem(String filename,String model, int iter, int limit, boolean withFixedMweOnly) throws IOException{
		DepTreebank tb = Parser.readTreebank(filename,limit);
		SentenceProcessComposition spc = new SentenceProcessComposition();
		spc.add(TreebankProcesses.mergeFixedMWEs());
		if(!withFixedMweOnly){
		   spc.add(TreebankProcesses.mergeRegularMWEs());
		}
		
		spc.add(TreebankProcesses.binarizeMWE(false));
		spc.add(TreebankIO.saveInXConll("tmp.conll"));
		TreebankProcesses.staticOracleMweTrain(tb, spc, model,iter);
		return null;
	}

	
	public static Evaluation parseWithMweSystem(String filename,String model,String output, int limit, boolean withFixedMweOnly) throws IOException{
		DepTreebank tb = Parser.readTreebank(filename,limit);
		MweRecognizerModel tbm = new MweRecognizerModel(model);
		TransitionBasedSystem<DepTree> parser = new PerceptronTransitionBasedSystem<DepTree>(tbm);
		SimpleEvaluation eval =new SimpleEvaluation();
		SentenceProcessComposition spc = new SentenceProcessComposition();
		

		
		spc.add(TreebankProcesses.greedyParse(parser, new ExternalData(null))); 
		spc.add(TreebankIO.saveInXConll("tmp.conll"));
		spc.add(TreebankProcesses.unbinarizeMWE(false));
        spc.add(TreebankProcesses.unlabelMWEArcs());
		
		spc.add(TreebankProcesses.mergeFixedMWEs());
		if(!withFixedMweOnly){
		spc.add(TreebankProcesses.mergeRegularMWEs());
		}
		
		spc.add(TreebankEvaluations.computeSegmentationAccuracy(false));
		
		spc.add(TreebankProcesses.fixedMWEAsTokens(false));
		
		spc.add(TreebankIO.saveInConll("mtmp.conll"));
		//spc.add(TreebankIO.saveInMergedConll("mtmp.conll"));
		//spc.add(TreebankProcesses.multipleTokensAsFixedMwe());
		//spc.add(TreebankIO.saveInXConll("mtmp2.conll"));
		TreebankProcesses.processTreebank(tb, spc, eval);
		//Utils.saveTreebankInXConll(tb, output);
		return eval;
	}
	
	
	
	/**
	 * @param args
	 * @throws IOException 
	 */
	public static void main(String[] args) throws IOException {
		/*DepTreebank tb = Parser.readXConllTreebank("en.ewt-test.xconll", -1);
		SentenceProcessComposition spc = new SentenceProcessComposition();
		spc.add(TreebankIO.saveInXConll("tt.conll"));
		TreebankProcesses.processTreebank(tb, spc, null);
		*/
		
		/*DepTreebank tb = Parser.readTreebank("data/acl2016/fr-acl14-train.conllu", -1);
		
		SentenceProcessComposition spc = new SentenceProcessComposition();
		spc.add(TreebankProcesses.mergeFixedMWEs());
		//spc.add(TreebankProcesses.mergeRegularMWEs());
		spc.add(TreebankProcesses.fixedMWEAsTokens(true));
		
		spc.add(TreebankIO.saveInConll("mergedTrain.conll"));
		spc.initProcess();
		DepTreebank res = TreebankProcesses.prepareTreebank(tb, spc, null);
		
		
		
		int nTokens = 0;
		int nUnits = 0;
		int nFixed = 0;
		int nSentences = 0;
		for(Sentence s:res){
			//System.err.println(s.getTokenSequence(true));
			for(Unit u:s.getTokenSequence(true)){
			
				if(u.isFixedMWE(s, true)){
					nFixed++;
				}
			}
			
			nTokens += s.getTokens().size();
			nUnits += s.getMWUnits().size();
			nSentences++;
		}
		spc.endProcess();*/ 
		/*
		tb = Parser.readXConllTreebank("en.ewt-train.xconll", -1);
		for(Sentence s:tb){
			nTokens += s.getTokens().size();
			nUnits += s.getMWUnits().size();
			
		}*/
		/*
		System.err.println(nSentences);
		System.err.println(nTokens);
		
		System.err.println(nUnits);
		System.err.println(nFixed);
		*/
		trainMweSystem("data/acl2016/fr-acl14-train.conllu", "models/acl2016/fr-acl14-train.conllu.imwe.0.final", 5,-1,true);
		//trainMweSystem("data/acl2016/fr-acl14-train.conllu", "models/acl2016/fr-acl14-train.conllu.imwe.1.final", 5,-1,true);
		//trainMweSystem("data/acl2016/fr-acl14-train.conllu", "models/acl2016/fr-acl14-train.conllu.imwe.2.final", 5,-1,true);
		//System.err.println(parseWithMweSystem("data/acl2016/fr-acl14-dev.conllu", "mwemodel.final", "res-mwe.conll",-1,true));
		//System.err.println(parseWithMweSystem("data/acl2016/fr-acl14-test.conllu", "mwemodel.final", "res-mwe.conll",-1,true));
		
		//MultipleEvaluation me = new MultipleEvaluation();
		//Parser.trainWithMerge("data/clean/fa-ud-train.conllu", "tmp", 15,-1);
		//Parser.parseWithMerge("data/clean/fa-ud-dev.conllu", "tmp.final","tmp.conll",-1);
		
		//trainFullSystem("tune-train.acl14.joint.predmorph.lexcpd.conll", "fullmodel", 6,-1,true,N_EXP);
		
		//parseWithFullSystem("dev.acl14.joint.predmorph.lexcpd.conll", "fullmodel.final", "res-full.conll",-1,false);
		
		  //trainMweSystem("tune-train.acl14.joint.predmorph.lexcpd.conll", "mwemodel", 1,-1,false);
		  //Evaluation e = parseWithMweSystem("tune-test.acl14.joint.predmorph.lexcpd.conll", "mwemodel.final", "res-mwe.conll",-1,false);
		  //me.add(e);
		
		//System.err.println("------------------");
		//System.err.println(me);
		
		//Parser.train("data/clean/fa-ud-train.conllu", "tmp-std", 5,-1,true);
		
		//train("tune-train.acl14.joint.predmorph.lexcpd.conll", "basemodel-3", 6,-1,false);
		//Parser.parse("data/clean/fa-ud-dev.conllu", "tmp-std.final", "tmp.conll",-1,true);
		 
		
	}

}
