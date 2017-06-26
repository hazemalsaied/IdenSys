/**
 * 
 */
package fr.upem.lgtools.evaluation;

import java.util.Collection;
import java.util.LinkedList;
import java.util.List;

/**
 * @author Mathieu
 *
 */
public class MultipleScore extends Score {
	private final List<Score> scores = new LinkedList<Score>();
	
	public MultipleScore(String evalName) {
		super(evalName);
	}
    
	public static double compute(Collection<Score> scores, ScoreAverage av){
		int n = scores.size();
		double res = 0.0;
		for(Score sc:scores){
			res += av.compute(sc);
		}
		return res/n;
	}
	
	public void add(Score sc){
		scores.add(sc);
	}
	
	
	@Override
	double getPrecision() {
		return compute(scores,new ScoreAverage() {
			
			@Override
			public double compute(Score sc) {
				return sc.getPrecision();
			}
		});
		
	}

	@Override
	double getRecall() {
		
		return compute(scores,new ScoreAverage() {
			
			@Override
			public double compute(Score sc) {
				return sc.getRecall();
			}
		});
	}

	@Override
	double getFscore() {
		return compute(scores, new ScoreAverage() {
			
			@Override
			public double compute(Score sc) {
				return sc.getFscore();
			}
		});
	}

	
	
}
