/**
 * 
 */
package fr.upem.lgtools.evaluation;

/**
 * @author Matthieu Constant
 *
 */
public class SegmentationAccuracy {
	private final String eval;
	private int predictedMWECount = 0;
	private int goldMWECount = 0;
	private int sentenceCount = 0;
	private int goldUnitCount = 0;
	private int predictedUnitCount = 0;
	private int goodUnitCount = 0;
	private int goodMWECount = 0;
	private int exactSegmentationCount = 0;
	
	
	
	
	
	/**
	 * @param eval
	 */
	public SegmentationAccuracy(String eval) {
		
		this.eval = eval;
	}

	public double getPrecision(){
		return goodUnitCount/(double)predictedUnitCount;
	}
	
	public double getMWEPrecision(){
		return goodMWECount/(double)predictedMWECount;
	}
	
	
	public double getRecall(){
		return goodUnitCount/(double)goldUnitCount;
	}
	
	public double getMWERecall(){
		return goodMWECount/(double)goldMWECount;
	}
	
	public double getExact(){
		return exactSegmentationCount/(double)sentenceCount;
		
	}
	
	
	public double getFscore(){
		double r = getRecall();
		double p = getPrecision();
		return 2*r*p/(r+p);
	}
	
	public double getMWEFscore(){
		double r = getMWERecall();
		double p = getMWEPrecision();
		return 2*r*p/(r+p);
	}
	
	
	public void addSentence(){
		sentenceCount++;
	}
	
	public void addGoldUnit(){
		goldUnitCount++;
	}
	 
	public void addPredictedUnit(){
		predictedUnitCount++;
	}
	
	public void addGoodUnit(){
		goodUnitCount++;
	}
	
	public void addGoodMWE(){
		goodMWECount++;
	}
	
	public void addExactSegmentation(){
		exactSegmentationCount++;
	}
	
	public void addPredictedMWE(){
		predictedMWECount++;
	}
	
	public void addGoldMWE(){
		goldMWECount++;
	}
	
	
	
	

	@Override
	public String toString() {
		String res = eval+":\nSegmentation: r="+getRecall()+", p="+getPrecision()+", f="+getFscore()+", exact="+getExact()+"\n";
		res += "MWEs: r="+getMWERecall()+", p="+getMWEPrecision()+", f="+getMWEFscore()+"\n";
		
		return res;
	}
	
}
