/**
 * 
 */
package fr.upem.lgtools.parser;

import fr.upem.lgtools.text.Unit;

/**
 * @author Mathieu
 *
 */
public class Element {
	private final Unit unit;
	private final Element next;
	
	Element(Unit unit, Element next){
		this.unit = unit;
		this.next = next;
	}

	public Unit getUnit() {
		return unit;
	}

	public Element getNext() {
		return next;
	}
	
	
	public boolean hasNext(){
		return next == null;
	}
	

}
