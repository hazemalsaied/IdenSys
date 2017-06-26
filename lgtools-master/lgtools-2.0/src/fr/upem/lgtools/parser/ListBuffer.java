/**
 * 
 */
package fr.upem.lgtools.parser;

import java.util.Iterator;
import java.util.LinkedList;

import fr.upem.lgtools.text.Sentence;
import fr.upem.lgtools.text.Unit;

/**
 * @author Mathieu Constant
 *
 */
public class ListBuffer implements Buffer{
	private final LinkedList<Unit> list;
	
	public ListBuffer(Sentence s){
		list = new LinkedList<Unit>(s.getTokens());
	}
	
	public ListBuffer(ListBuffer lb){
		list = new LinkedList<Unit>(lb.list);
	}
	

	@Override
	public Iterator<Unit> iterator() {
		return list.iterator();
	}

	@Override
	public Unit get(int index) {
		return list.get(index);
	}

	@Override
	public Unit next() {
		return list.removeFirst();
	}

	@Override
	public int size() {
		return list.size();
	}

	@Override
	public void push(Unit u) {
		list.addFirst(u);
	}
	
	@Override
	public String toString() {
		return list.toString();
	}

}
