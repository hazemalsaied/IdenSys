/**
 * 
 */
package fr.upem.lgtools.parser.transitions;

import fr.upem.lgtools.parser.Analysis;
import fr.upem.lgtools.parser.Configuration;
import fr.upem.lgtools.parser.Container;
import fr.upem.lgtools.text.Unit;

/**
 * @author Mathieu Constant
 *
 */
public class ShiftTransition<T extends Analysis> extends AbstractTransition<T>{
	
	public ShiftTransition(String type) {
		super(type);
		
	}

	@Override
	public Configuration<T> perform(Configuration<T> configuration) {
		if(!isValid(configuration)){
			throw new IllegalStateException("The buffer should not be empty before performing a SHIFT!");
		}
		Container buffer = configuration.getFirstBuffer();
		Unit u = buffer.read();
		Container stack = configuration.getFirstStack();
		stack.push(u);
		if(configuration.stackCount() >= 2 && !configuration.getAnalyses().isBeingProcessed(u)){
			Container lexstack = configuration.getSecondStack();
			lexstack.push(u);
			configuration.getAnalyses().setAsBeingProcessed(u);
		}
		return configuration;
	}

	@Override
	public boolean isValid(Configuration<T> configuration) {
		Container buffer = configuration.getFirstBuffer();
		return buffer.size() != 0;
	}

	
}
