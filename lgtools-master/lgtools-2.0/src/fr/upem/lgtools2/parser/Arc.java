/**
 * 
 */
package fr.upem.lgtools2.parser;

import fr.upem.lgtools.text.Unit;

/**
 * @author Mathieu Constant
 *
 */
public class Arc {
	private final Unit head;
	private final Unit modifier;
	private final String label;
	/**
	 * @param head
	 * @param modifier
	 * @param label
	 */
	public Arc(Unit head, Unit modifier, String label) {
		super();
		this.head = head;
		this.modifier = modifier;
		this.label = label;
	}
	
	
	public Unit getHead() {
		return head;
	}
	
	public Unit getModifier() {
		return modifier;
	}
	
	public String getLabel() {
		return label;
	}
	
	
	

}
