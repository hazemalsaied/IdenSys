/**
 * 
 */
package fr.upem.lgtools.process;

import java.util.HashSet;
import java.util.Iterator;
import java.util.List;
import java.util.Set;

import fr.upem.lgtools.evaluation.SimpleEvaluation;
import fr.upem.lgtools.evaluation.SimpleParsingAccuracy;
import fr.upem.lgtools.evaluation.SimpleScore;
import fr.upem.lgtools.parser.Constants;
import fr.upem.lgtools.text.Sentence;
import fr.upem.lgtools.text.Unit;

/**
 * @author Mathieu Constant
 *
 */
public class TreebankEvaluations {
	
	
	public static void  parsingEvaluation(Sentence predicteds, Sentence golds, SimpleEvaluation eval){
		SimpleParsingAccuracy acc = (SimpleParsingAccuracy)eval.getParsingAccuracy();   //Cast should be safe, but check!!!
		acc.addSentence();
		boolean exact = true;
		Iterator<Unit> it = golds.getTokens().iterator(); 
		for(Unit up:predicteds.getTokens()){
			Unit ug = it.next();
			//System.err.println(u);
			acc.addUnit();
			String glabel = ug.getGoldSlabel();
			String plabel = up.getPredictedSlabel();
			SimpleScore glscore = acc.getLabelScore(glabel);
			SimpleScore plscore = acc.getLabelScore(plabel);
			glscore.addGold();
			plscore.addPredicted();
			if(!glabel.startsWith(Constants.MWE_LABEL)){
				acc.addNonMweGold();
			}
			if(!plabel.startsWith(Constants.MWE_LABEL)){
				acc.addNonMwePredicted();
			}

			if(ug.getGoldSheadId() == up.getPredictedSheadId()){
				acc.addUnlabeledMatch();


				if(glabel.equals(plabel)){
					acc.addLabeledMatch();
					glscore.addGood(); //glscore and plscore are the same
					if(!plabel.startsWith(Constants.MWE_LABEL)){
						acc.addNonMweGood();
					}
				}
				else{
					exact = false;
				}

			}
			else{
				exact = false;
			}

		}
		if(exact){
			acc.addExactMatch();
		}
	}
	
	
	public static SentenceProcess computeParsingAccuracy(){
		return new AbstractSentenceProcess(){

			@Override
			public Sentence apply(Sentence s, SimpleEvaluation eval) {
				SimpleParsingAccuracy acc = (SimpleParsingAccuracy)eval.getParsingAccuracy();   //Cast should be safe, but check!!!
				acc.addSentence();
				boolean exact = true;
				for(Unit u:s.getTokens()){
					//System.err.println(u);
					acc.addUnit();
					String glabel = u.getGoldSlabel();
					String plabel = u.getPredictedSlabel();
					SimpleScore glscore = acc.getLabelScore(glabel);
					SimpleScore plscore = acc.getLabelScore(plabel);
					glscore.addGold();
					plscore.addPredicted();
					if(!glabel.startsWith(Constants.MWE_LABEL)){
						acc.addNonMweGold();
					}
					if(!plabel.startsWith(Constants.MWE_LABEL)){
						acc.addNonMwePredicted();
					}

					if(u.getGoldSheadId() == u.getPredictedSheadId()){
						acc.addUnlabeledMatch();


						if(glabel.equals(plabel)){
							acc.addLabeledMatch();
							glscore.addGood(); //glscore and plscore are the same
							if(!plabel.startsWith(Constants.MWE_LABEL)){
								acc.addNonMweGood();
							}
						}
						else{
							exact = false;
						}

					}
					else{
						exact = false;
					}

				}
				if(exact){
					acc.addExactMatch();
				}
			
				return s;
			}
			
		};
		
	}
	
	
	
	/*
	public static List<Score> computeMergeParsingScore(DepTreebank tb){
		Score uas = new Score("muas");
		Score las = new Score("mlas");
		for(Sentence s:tb){
			computeMergeParsingScore(s,uas,las);
		}
		
		return Arrays.asList(uas,las);
	}
	*/
	
	
	public static SentenceProcess computeSegmentationParsingScore(){
		return new AbstractSentenceProcess() {
			
			@Override
			public Sentence apply(Sentence s, SimpleEvaluation eval) {
				SimpleScore las = (SimpleScore)eval.getSLAS(); //TODO: cats should be safe but check!
				SimpleScore uas = (SimpleScore)eval.getSUAS(); //TODO: cats should be safe but check!
				for(Unit u:s.getTokenSequence(true)){
					uas.addGold();
					las.addGold();
					if(u.getGoldSheadId() == u.getPredictedSheadId()){
						uas.addGood();
						if(u.getGoldSlabel().equals(u.getPredictedSlabel())){
							las.addGood();
						}
					}
				}
				for(@SuppressWarnings("unused") Unit u:s.getTokenSequence(false)){
					uas.addPredicted();
					las.addPredicted();
				}
				return s;
			}
		};
	}
	
	
	
	
	
	
	
	public static void  segEvaluation(Sentence predicteds, Sentence golds, SimpleEvaluation eval,boolean onlyFixedMwe){
		SimpleScore acc = onlyFixedMwe?(SimpleScore)eval.getFixedMweAccuracy():(SimpleScore)eval.getMweAccuracy();  //TODO: cast should be safe but check!
		List<Unit> gold= onlyFixedMwe?golds.getTokenSequence(true):golds.getUnitSequence(true);
		List<Unit> predicted = onlyFixedMwe?predicteds.getTokenSequence(false):predicteds.getUnitSequence(false);
		//System.err.println(gold);
		//System.err.println(predicted);
		//System.err.println();
		Set<Unit> goldmwes = new HashSet<Unit>();
		for(Unit u:gold){
			if(u.isMWE()){
				//System.err.println(u);
				goldmwes.add(u);
				acc.addGold();
			}
			
		}
		Set<Unit> predmwes = new HashSet<Unit>();
		for(Unit u:predicted){
			if(u.isMWE()){
				predmwes.add(u);
				acc.addPredicted();
				if(goldmwes.contains(u)){
					acc.addGood();
				}
			}
		}
		
	}
	
	public static SentenceProcess computeSegmentationAccuracy(final boolean onlyFixedMwe){
		return new AbstractSentenceProcess(){

			@Override
			public Sentence apply(Sentence s, SimpleEvaluation eval) {
			
				SimpleScore acc = onlyFixedMwe?(SimpleScore)eval.getFixedMweAccuracy():(SimpleScore)eval.getMweAccuracy();  //TODO: cast should be safe but check!
				List<Unit> gold= onlyFixedMwe?s.getTokenSequence(true):s.getUnitSequence(true);
				List<Unit> predicted = onlyFixedMwe?s.getTokenSequence(false):s.getUnitSequence(false);
				//System.err.println(gold);
				//System.err.println(predicted);
				//System.err.println();
				Set<Unit> goldmwes = new HashSet<Unit>();
				for(Unit u:gold){
					if(u.isMWE()){
						//System.err.println(u);
						goldmwes.add(u);
						acc.addGold();
					}
					
				}
				Set<Unit> predmwes = new HashSet<Unit>();
				for(Unit u:predicted){
					if(u.isMWE()){
						predmwes.add(u);
						acc.addPredicted();
						if(goldmwes.contains(u)){
							acc.addGood();
						}
					}
				}
				
				//evaluation(s, s, eval, onlyFixedMwe);
				
				
				return s;
			}
			
		};
		
		
	}
	
	
	
	/*
	public static SegmentationAccuracy computeSegmentationAccuracy(DepTreebank tb, boolean onlyFixedMwe){
		SegmentationAccuracy acc = new SegmentationAccuracy(onlyFixedMwe?"FixedMWEs":"All MWEs");
		for(Sentence s:tb){
			acc.addSentence();
			computeSegmentationAccuracy(s,acc,onlyFixedMwe);
		}
		return acc;
		
	}*/
		
}
