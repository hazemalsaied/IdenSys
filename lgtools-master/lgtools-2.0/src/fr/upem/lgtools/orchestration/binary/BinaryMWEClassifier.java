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
public interface BinaryMWEClassifier {
     public boolean isMultiwordToken(List<Unit> mwe,DepTree context);
 	
}


