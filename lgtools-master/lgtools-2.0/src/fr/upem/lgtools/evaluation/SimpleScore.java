/**
 * 
 */
package fr.upem.lgtools.evaluation;

/**
 * @author Mathieu
 *
 */
public class SimpleScore extends Score {
	int  gold = 0;
	int predicted = 0;
	int good = 0;
	
	
	public SimpleScore(String name){
		super(name);
	}
	
	
	public void addGold(){
		gold++;
	}
	
	public void addPredicted(){
		predicted++;
	}
	
	public void addGood(){
		good++;
	}
	
	@Override
	public double getPrecision(){
		return good/(double)predicted;
	}
	
	
	@Override
	public double getRecall(){
		return good/(double)gold;
	}
	
	@Override
	public double getFscore(){
		double r = getRecall();
		double p = getPrecision();
		return 2*r*p/(r+p);
		
	}
	
	@Override
	public String toString() {
		//return super.toString()+ "  ("+good+"/s="+predicted+"/g="+gold+")";
		return super.toString();
	}
}
