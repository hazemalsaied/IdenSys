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
public class MultiwordTokenOnlyClassifier implements BinaryMWEClassifier {

	/* (non-Javadoc)
	 * @see fr.upem.lgtools.orchestration.BinaryMWEClassifier#isMultiwordToken()
	 */
	@Override
	public boolean isMultiwordToken(List<Unit> mwe,DepTree context) {
		return true;
	}

}
