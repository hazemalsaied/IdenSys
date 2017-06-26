package fr.upem.lgtools.parser.transitions;

import fr.upem.lgtools.parser.Analysis;
import fr.upem.lgtools.parser.Configuration;

public interface Transition<T extends Analysis> {
	public Configuration<T> performAll(Configuration<T> configuration);
	public boolean isValid(Configuration<T> configuration);
	public String id();
		
}
