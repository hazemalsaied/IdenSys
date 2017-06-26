/*
 * 
 */
package fr.upem.lgtools.parser;

import fr.upem.lgtools.parser.features.FeatureVector;
import fr.upem.lgtools.parser.transitions.Transition;

/**
 * 
 * @author Mathieu Constant
 *
 */
public class ParseHypothesis<T extends Analysis> implements Comparable<ParseHypothesis<T>>{
	private final Configuration<T> configuration;
	private final boolean isGold;
	private final double score;
	private final FeatureVector features;
	private final ParseHypothesis<T> previous;
	private ParseHypothesis<T> goldHypothesis;
	private final Transition<T> transition;
	
	/**
	 * @param configuration
	 * @param score
	 * @param features
	 */
	public ParseHypothesis(Configuration<T> configuration, double score, FeatureVector features,ParseHypothesis<T> previous,boolean isGold,Transition<T> transition) {
		this.configuration = configuration;
		this.score = score;
		this.features = features;
		this.previous = previous;
		this.isGold = isGold;
		this.transition = transition;
	}
	
	
	
	
	public ParseHypothesis<T> getGoldHypothesis() {
		return goldHypothesis;
	}




	public Transition<T> getTransition() {
		return transition;
	}




	public void setGoldHypothesis(ParseHypothesis<T> goldHypothesis) {
		this.goldHypothesis = goldHypothesis;
	}




	public Configuration<T> getConfiguration() {
		return configuration;
	}
	
	public double getScore() {
		return score;
	}
	
	public FeatureVector getFeatures() {
		return features;
	}


	public ParseHypothesis<T> getPrevious() {
		return previous;
	}


	@Override
	public int compareTo(ParseHypothesis<T> arg0) {		
		return new Double(arg0.score).compareTo(this.score);
	}

	
	public boolean isGold(){
		return isGold;
	}
	
	@Override
	public String toString() {
		if(transition == null){
			return "NULL-HYP\n";
		}
		return "HYP:"+configuration.toString()+"\n---"+isGold+"=="+score+"=="+transition.toString()+"---\n";
	}
	
	
	
}
