/**
 * 
 */
package fr.upem.lgtools.parser;

import fr.upem.lgtools.text.Unit;

/**
 * @author Mathieu Constant
 *
 */
public interface Buffer extends Iterable<Unit>{

	/**
	 * 
	 * @param index
	 * @return the unit at position index in the buffer
	 */
	
	public Unit get(int index);
	
	/**
	 * 
	 * @return the next unit in buffer (and remove it from buffer)
	 */
	public Unit next();
	
	
	/**
	 * 
	 * @return the number of units in the buffer
	 */
	public int size();
	
	/**
	 * push a unit on buffer
	 * 
	 * @param u unit to be pushed
	 */
	
	public void push(Unit u);
	
}
