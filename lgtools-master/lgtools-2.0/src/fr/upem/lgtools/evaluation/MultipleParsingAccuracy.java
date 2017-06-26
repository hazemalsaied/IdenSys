/**
 * 
 */
package fr.upem.lgtools.evaluation;

import java.util.Collection;
import java.util.LinkedList;

/**
 * @author Mathieu
 *
 */
public class MultipleParsingAccuracy extends ParsingAccuracy {
    Collection<ParsingAccuracy> accuracies = new LinkedList<ParsingAccuracy>();
	
	static interface AccuracyAverage{
		double compute(ParsingAccuracy acc);
	}
	
	public void add(ParsingAccuracy acc){
		accuracies.add(acc);
	}
	
	public static double compute(Collection<ParsingAccuracy> accuracies, AccuracyAverage av){
		int n = accuracies.size();
		double res = 0.0;
		for(ParsingAccuracy sc:accuracies){
			res += av.compute(sc);
		}
		return res/n;
	}
	
	@Override
	public double getUAS() {
		return compute(accuracies, new AccuracyAverage(){

			@Override
			public double compute(ParsingAccuracy acc) {
				return acc.getUAS();
			}
			
		});
	}

	@Override
	public double getLAS() {
		return compute(accuracies, new AccuracyAverage(){

			@Override
			public double compute(ParsingAccuracy acc) {
				return acc.getLAS();
			}
			
		});
	}

	@Override
	public double getExactMatch() {
		return compute(accuracies, new AccuracyAverage(){

			@Override
			public double compute(ParsingAccuracy acc) {
				return acc.getExactMatch();
			}
			
		});
	}

	@Override
	public Collection<? extends Score> getLabelScores() {
		//TODO
		return null;
	}

	@Override
	public Score getNonMweScore() {
		MultipleScore msc = new MultipleScore("Non-MWE");
		for(ParsingAccuracy acc:accuracies){
			msc.add(acc.getNonMweScore());
		}
		
		return msc;
	}

}
