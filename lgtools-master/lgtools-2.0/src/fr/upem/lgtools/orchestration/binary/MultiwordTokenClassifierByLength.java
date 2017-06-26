/**
 * 
 */
package fr.upem.lgtools.orchestration.binary;

import java.util.List;

import fr.upem.lgtools.parser.DepTree;
import fr.upem.lgtools.text.Unit;

/**
 * @author Mathieu Constant
 *
 */
public class MultiwordTokenClassifierByLength implements BinaryMWEClassifier {

	private final int lengthThreshold;
	private final boolean testForMultiwordTokens;
	
	
	
	/**
	 * @param lengthThreshold
	 * @param testForMultiwordTokens
	 */
	public MultiwordTokenClassifierByLength(int lengthThreshold, boolean testForMultiwordTokens) {
		this.lengthThreshold = lengthThreshold;
		this.testForMultiwordTokens = testForMultiwordTokens;
	}



	/* (non-Javadoc)
	 * @see fr.upem.lgtools.orchestration.binary.BinaryMWEClassifier#isMultiwordToken()
	 */
	@Override
	public boolean isMultiwordToken(List<Unit> mwe,DepTree context) {
		return testForMultiwordTokens?mwe.size() < lengthThreshold:mwe.size() > lengthThreshold;
	}

}
