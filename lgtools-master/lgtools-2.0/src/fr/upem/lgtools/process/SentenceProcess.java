/**
 * 
 */
package fr.upem.lgtools.process;

import fr.upem.lgtools.evaluation.SimpleEvaluation;
import fr.upem.lgtools.text.Sentence;

/**
 * @author Mathieu
 *
 */
public interface SentenceProcess {
	public void initProcess();
    public Sentence apply(Sentence s, SimpleEvaluation eval);
    public void endProcess();
}


