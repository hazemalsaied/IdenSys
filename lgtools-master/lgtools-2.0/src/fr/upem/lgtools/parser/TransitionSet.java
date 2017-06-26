/**
 * 
 */
package fr.upem.lgtools.parser;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Iterator;
import java.util.List;
import java.util.Map;

import fr.upem.lgtools.parser.transitions.Transition;
import fr.upem.lgtools.parser.transitions.Transitions;

/**
 * @author mconstant
 *
 */
public class TransitionSet<T extends Analysis> implements Iterable<Transition<T>>{	
	private final List<Transition<T>> transitions = new ArrayList<Transition<T>>();
	private final Map<String,Transition<T>> map = new HashMap<String, Transition<T>>();
	private final Map<String,Integer> transitionIds = new HashMap<String,Integer>();
	
	
	public boolean contains(Transition<T> transition){
		return map.containsKey(transition.id());		
	}
	
	
	private String getTransitionId(String type, String label){
		//System.err.println(type+"=="+label);
		return Transitions.constructTransitionId(type, label);
	}
	
	
	public  Transition<T> getTransition(int index){
		return transitions.get(index);
	}
	
	public  Transition<T> getTransition(String id){
		return map.get(id);
	}
	
	public  Transition<T> getTransition(String type, String label){
		//System.err.println(type+"="+label);
		//System.err.println(getTransitionId(type,label));
		return getTransition(getTransitionId(type,label));
	}
	
	public int getTransitionIndex(Transition<T> transition){
		//System.err.println(transition);
		return transitionIds.get(transition.id());
	}
	
		
	public void add(Transition<T> transition){
		transitions.add(transition);
		map.put(transition.id(), transition);
		transitionIds.put(transition.id(),transitions.size() - 1);
	}
	
	public int size(){
		return transitions.size();
	}


	@Override
	public Iterator<Transition<T>> iterator() {
		return new Iterator<Transition<T>>() {
            Iterator<Transition<T>> it = transitions.iterator();
			@Override
			public boolean hasNext() {				
				return it.hasNext();
			}

			@Override
			public Transition<T> next() {				
				return it.next();
			}

			@Override
			public void remove() {
				throw new UnsupportedOperationException();
			}
			
		};
	}
	
	
	@Override
	public String toString() {		
		return transitions.toString();
	}

}
