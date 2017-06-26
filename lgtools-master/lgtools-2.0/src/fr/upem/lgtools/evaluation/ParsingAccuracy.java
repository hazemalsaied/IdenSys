package fr.upem.lgtools.evaluation;

import java.util.Collection;

public abstract class ParsingAccuracy {
	
	
	
	abstract public double getUAS();
	abstract public double getLAS();
	abstract public double getExactMatch();
	abstract public Collection<? extends Score> getLabelScores();
	abstract public Score getNonMweScore();
	
	
	

		
	@Override
	public String toString(){
		//String res = "UAS="+getUAS()+", LAS="+getLAS() + ", ExactMatch="+getExactMatch()+"\n";
		String res = "\t"+getUAS()+"\t"+getLAS();
		/*for(Score sc:getLabelScores()){
			res += sc.toString()+"\n";
		}
		res += getNonMweScore().toString(); */
		return res;
	}
	
	
}
