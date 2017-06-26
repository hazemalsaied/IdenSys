/**
 * 
 */
package fr.upem.lgtools.evaluation;

import java.util.Collection;
import java.util.HashMap;
import java.util.Map;

/**
 * @author Mathieu
 *
 */
public class SimpleParsingAccuracy extends ParsingAccuracy {
	private int sentenceCount = 0;
	private int unitCount = 0;
	private int lasCount = 0;
	private int uasCount = 0;
	private int exactMatchCount = 0;
	private Map<String,SimpleScore> labelScores = new HashMap<String, SimpleScore>();
	private SimpleScore nonMweScore = new SimpleScore("Non-MWE LAS"); 


	public SimpleScore getLabelScore(String label){
		SimpleScore sc = labelScores.get(label);
		if(sc == null){
			sc = new SimpleScore(label+" LAS");
			labelScores.put(label, sc);
		}
		return sc;
	}


	@Override
	public Collection<? extends Score> getLabelScores(){
		return labelScores.values();
	}

	

/*
	public static ParsingAccuracy computeParsingAccuracy(DepTreebank tb, String mweLabel){
		SimpleParsingAccuracy acc = new SimpleParsingAccuracy();
		for(Sentence s:tb){
			acc.addSentence();
			computeParsingAccuracy(s,acc,mweLabel);
		}
		return acc;
	}
*/
	
	


	public void addUnit(){
		unitCount++;
	}

	public void addLabeledMatch(){
		lasCount++;
	}

	public void addUnlabeledMatch(){
		uasCount++;
	}

	public void addExactMatch(){
		exactMatchCount++;
	}

	public void addSentence(){
		sentenceCount++;
	}

	@Override
	public double getLAS(){
		return lasCount/(double)unitCount;		
	}

	@Override
	public double getUAS(){
		return uasCount/(double)unitCount;		
	}

	@Override
	public double getExactMatch(){
		return exactMatchCount/(double)sentenceCount;
	}


	@Override
	public Score getNonMweScore() {
		return nonMweScore;
	}

	
	
	public void addNonMweGood(){
		nonMweScore.addGood();
	}
	
	public void addNonMweGold(){
		nonMweScore.addGold();
	}
	
	public void addNonMwePredicted(){
		nonMweScore.addPredicted();
	}
	
	
}
