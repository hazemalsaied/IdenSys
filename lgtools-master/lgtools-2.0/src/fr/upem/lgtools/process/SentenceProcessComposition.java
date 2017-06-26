/**
 * 
 */
package fr.upem.lgtools.process;

import java.util.LinkedList;
import java.util.List;

import fr.upem.lgtools.evaluation.SimpleEvaluation;
import fr.upem.lgtools.text.Sentence;

/**
 * @author Mathieu Constant
 *
 */
public class SentenceProcessComposition implements SentenceProcess {
	private final List<SentenceProcess> transformers = new LinkedList<SentenceProcess>();
	
	public void add(SentenceProcess st){
		transformers.add(st);
	}

	@Override
	public Sentence apply(Sentence s, SimpleEvaluation eval) {
		
		for(SentenceProcess st:transformers){
			s = st.apply(s,eval);
		}
		
		return s;
	}

	@Override
	public void initProcess() {
		for(SentenceProcess sp:transformers){
			sp.initProcess();
		}
		
	}

	@Override
	public void endProcess() {
		for(SentenceProcess sp:transformers){
			sp.endProcess();
		}
		
	}
	
	
	
	
}
