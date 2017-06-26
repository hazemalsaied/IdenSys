/**
 * 
 */
package fr.upem.lgtools.orchestration.binary;

import java.util.List;

import fr.upem.lgtools.parser.DepTree;
import fr.upem.lgtools.text.Unit;

/**
 * @author Mathieu
 *
 */
public class MultiwordSubtreeOnlyClassifier implements BinaryMWEClassifier{

	@Override
	public boolean isMultiwordToken(List<Unit> mwe,DepTree context) {
		return false;
	}
	

}
