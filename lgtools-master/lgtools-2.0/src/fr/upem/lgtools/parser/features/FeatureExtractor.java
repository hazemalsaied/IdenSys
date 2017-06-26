/**
 * 
 */
package fr.upem.lgtools.parser.features;

import fr.upem.lgtools.parser.Analysis;
import fr.upem.lgtools.parser.Configuration;
import fr.upem.lgtools.parser.ExternalData;

/**
 * @author Mathieu Constant
 *
 */
public interface FeatureExtractor<T extends Analysis> {
      public FeatureVector perform(Configuration<T> config, ExternalData data);
}
