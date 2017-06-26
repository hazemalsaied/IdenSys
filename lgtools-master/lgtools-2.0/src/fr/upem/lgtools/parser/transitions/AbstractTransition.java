/**
 * 
 */
package fr.upem.lgtools.parser.transitions;

import fr.upem.lgtools.parser.Analysis;
import fr.upem.lgtools.parser.Configuration;

/**
 * @author Matthieu Constant
 *
 */
public abstract class AbstractTransition<T extends Analysis> implements Transition<T> {
	final String type;
	
	public AbstractTransition(String type) {
		this.type = type;
	}
		
	@Override
	public String id() {		
		return type;
	}

	
	@Override
	public String toString(){
		return id();
	}

	@Override
	public int hashCode() {
		final int prime = 31;
		int result = 1;
		String id = id();
		result = prime * result + ((id == null) ? 0 : id.hashCode());
		return result;
	}

	@SuppressWarnings("unchecked")
	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		AbstractTransition<T> other = (AbstractTransition<T>) obj;
		String id = id();
		String oid = other.id();
		if (id == null) {
			if (oid != null)
				return false;
		} else if (!id.equals(oid))
			return false;
		return true;
	}
	
	public abstract Configuration<T> perform(Configuration<T> configuration);
	
	@Override
	public Configuration<T> performAll(Configuration<T> configuration) {
		Configuration<T> c = perform(configuration);
		c.addAction(this.id());
		return c;
	}
	
	
}
