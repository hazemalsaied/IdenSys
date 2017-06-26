/**
 * 
 */
package fr.upem.lgtools.evaluation;

import java.util.LinkedList;
import java.util.List;

/**
 * @author Mathieu
 *
 */
public class MultipleEvaluation extends Evaluation {
    private List<Evaluation> evaluations = new LinkedList<Evaluation>();
	
	
    public void add(Evaluation eval){
    	evaluations.add(eval);
    }
    
	@Override
	public ParsingAccuracy getParsingAccuracy() {
		MultipleParsingAccuracy mpa = new MultipleParsingAccuracy();
		boolean empty = true;
		for(Evaluation e:evaluations){
			if(e.getParsingAccuracy() != null){
				empty = false;
				mpa.add(e.getParsingAccuracy());
			}
		}
		return empty?null:mpa;
	}

	@Override
	public Score getMweAccuracy() {
		MultipleScore msc = new MultipleScore("MWE");
		boolean empty = true;
		for(Evaluation e:evaluations){
			if(e.getMweAccuracy() != null){
				empty = false;
				msc.add(e.getMweAccuracy());
			}
		}
		return empty?null:msc;
		
	}

	@Override
	public Score getFixedMweAccuracy() {
		MultipleScore msa = new MultipleScore("Fixed MWE");
		boolean empty = true;
		for(Evaluation e:evaluations){
			if(e.getFixedMweAccuracy() != null){
				empty = false;
				msa.add(e.getFixedMweAccuracy());
			}
		}
		return empty?null:msa;
	}

	@Override
	public Score getSUAS() {
		MultipleScore msc = new MultipleScore("SUAS");
		boolean empty = true;
		for(Evaluation e:evaluations){
			if(e.getSUAS() != null){
				empty = false;
				msc.add(e.getSUAS());
			}
		}
		return empty?null:msc;
	}

	@Override
	public Score getSLAS() {
		MultipleScore msc = new MultipleScore("SLAS");
		boolean empty = true;
		for(Evaluation e:evaluations){
			if(e.getSLAS() != null){
				empty = false;
				msc.add(e.getSLAS());
			}
		}
		return empty?null:msc;
	}

}
