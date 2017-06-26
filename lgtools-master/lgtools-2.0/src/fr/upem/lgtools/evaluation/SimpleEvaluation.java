/**
 * 
 */
package fr.upem.lgtools.evaluation;

/**
 * @author Mathieu
 *
 */
public class SimpleEvaluation extends Evaluation{
	private final ParsingAccuracy parsingAccuracy;
    private final Score mwes;
    private final Score fixedMwes;
    private final Score suas;
    private final Score slas;
    
    
    
    
    
	/**
	 * @param parsingAccuracy
	 * @param mwes
	 * @param fixedMwes
	 * @param suas
	 * @param slas
	 */
	/*public SimpleEvaluation(ParsingAccuracy parsingAccuracy, Score mwes, Score fixedMwes,
			Score suas, Score slas) {

		this.parsingAccuracy = parsingAccuracy;
		this.mwes = mwes;
		this.fixedMwes = fixedMwes;
		this.suas = suas;
		this.slas = slas;
	}*/
	
	public SimpleEvaluation() {
		this.parsingAccuracy = new SimpleParsingAccuracy();
		this.mwes = new SimpleScore("MWE");
		this.fixedMwes = new SimpleScore("Fixed MWE");
		this.slas = new SimpleScore("SLAS");
		this.suas = new SimpleScore("SUAS");
	}
	
	
	
	
	
	
	@Override
	public ParsingAccuracy getParsingAccuracy() {
		return parsingAccuracy;
	}
	@Override
	public Score getMweAccuracy() {
		return mwes;
	}
	@Override
	public Score getFixedMweAccuracy() {
		return fixedMwes;
	}
	@Override
	public Score getSUAS() {
		return suas;
	}
	@Override
	public Score getSLAS() {
		return slas;
	}
    
    
    
    
}
