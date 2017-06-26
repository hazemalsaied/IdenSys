package fr.upem.lgtools.parser;

import java.io.IOException;
import java.util.Iterator;

import fr.upem.lgtools.evaluation.SimpleEvaluation;
import fr.upem.lgtools.parser.arcstandard.ArcStandardTransitionBasedParserModel;
import fr.upem.lgtools.parser.arcstandard.ImplicitCmpFullyMWEAwareArcStandardTransitionBasedModel;
import fr.upem.lgtools.parser.mwereco.MweRecognizerModel;
import fr.upem.lgtools.process.SentenceProcessComposition;
import fr.upem.lgtools.process.TreebankEvaluations;
import fr.upem.lgtools.process.TreebankIO;
import fr.upem.lgtools.process.TreebankProcesses;
import fr.upem.lgtools.text.DepTreebank;
import fr.upem.lgtools.text.Sentence;

public class PipelineParser {

	
	
	public static void main(String[] args) throws IOException {
		String filename="data/acl2016/fr-acl14-test.conllu";
		String mmodel="models/acl2016/fr-acl14-train.conllu.imwe.0.final.final";
		String pmodel="models/acl2016/fr-acl14-train.conllu.pipe.impl.0.final.final";
		boolean isBaseline = false;
		
		DepTreebank tb = Parser.readTreebank(filename,-1);
		MweRecognizerModel tbm = new MweRecognizerModel(mmodel);
		TransitionBasedSystem<DepTree> parser = new PerceptronTransitionBasedSystem<DepTree>(tbm);
		SimpleEvaluation eval =new SimpleEvaluation();
		SentenceProcessComposition spc = new SentenceProcessComposition();
		ExternalData data = new ExternalData(null);

		
		spc.add(TreebankProcesses.greedyParse(parser,data)); 
		spc.add(TreebankProcesses.unbinarizeMWE(false));
        spc.add(TreebankProcesses.unlabelMWEArcs());
		
		spc.add(TreebankProcesses.mergeFixedMWEs());
		
		
		spc.add(TreebankEvaluations.computeSegmentationAccuracy(false));
		
		spc.add(TreebankProcesses.fixedMWEAsTokens(false));
		
		spc.add(TreebankIO.saveInConll("mtmp.conll"));
		
		
		
		ArcStandardTransitionBasedParserModel tbp;
		if(isBaseline){
		  tbp = new ArcStandardTransitionBasedParserModel(pmodel);
		}
		else{
			tbp = new ImplicitCmpFullyMWEAwareArcStandardTransitionBasedModel(pmodel,true);
		}
		parser = new PerceptronTransitionBasedSystem<DepTree>(tbp);
		spc.add(TreebankProcesses.greedyParse(parser,data));
		spc.add(TreebankProcesses.unbinarizeMWE(false));
		spc.add(TreebankIO.saveInXConll("raw.xconll"));
		
		spc.add(TreebankProcesses.multipleTokensAsFixedMwe());
		//if(isBaseline){
		  spc.add(TreebankProcesses.mergeRegularMWEs());
		//}
		spc.add(TreebankIO.saveInXConll("tmp.xconll"));
	
		SentenceProcessComposition spc2 = new SentenceProcessComposition();
       spc2.add(TreebankProcesses.unlabelMWEArcs());
		
		spc2.add(TreebankProcesses.mergeFixedMWEs());
		
		spc2.add(TreebankProcesses.mergeRegularMWEs());
		spc2.add(TreebankIO.saveInXConll("tmp2.xconll"));
		
		
		spc.initProcess();
		spc2.initProcess();
		DepTreebank tb2 = TreebankProcesses.prepareTreebank(tb, spc2, eval); 
		DepTreebank res = TreebankProcesses.prepareTreebank(tb, spc, eval); 
		Iterator<Sentence> it = tb2.iterator();
		for(Sentence p:res){
			Sentence g = it.next();
			TreebankEvaluations.segEvaluation(p, g, eval,true);
			TreebankEvaluations.segEvaluation(p, g, eval,false);
			TreebankEvaluations.parsingEvaluation(p, g, eval);
		}
		System.err.println(eval);
		spc.endProcess();
		spc2.endProcess();

	}

}
