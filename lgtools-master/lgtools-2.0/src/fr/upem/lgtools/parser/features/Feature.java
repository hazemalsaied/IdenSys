/**
 * 
 */
package fr.upem.lgtools.parser.features;

/**
 * @author Mathieu Constant
 *
 */
public class Feature {
	private final int feat;
	private final double value;
	
	/**
	 * @param attribute
	 * @param value
	 */
	public Feature(int feat, double value) {
		this.feat = feat;
		this.value = value;

	}
	
	/**
	 * 
	 * @param feat
	 */
	public Feature(int feat){
		this(feat,1.0);
	}
	
	
	public int getFeat() {
		return feat;
	}
	
	

	public double getValue() {
		return value;
	}
	
	
	

}
