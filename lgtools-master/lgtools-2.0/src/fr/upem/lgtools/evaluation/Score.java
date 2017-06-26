/**
 * 
 */
package fr.upem.lgtools.evaluation;

/**
 * @author Mathieu Constant
 *
 */
public abstract class Score {
	final String evalName;
	public Score(String evalName){
		this.evalName = evalName;
	}
	
	abstract double getPrecision();
	abstract double getRecall();
	abstract double getFscore();
	
	
	@Override
	public String toString() {
		//return evalName + ": p="+getPrecision()+ ", r="+getRecall()+", f="+getFscore();
		return "\t"+getFscore();
	}
	

}
