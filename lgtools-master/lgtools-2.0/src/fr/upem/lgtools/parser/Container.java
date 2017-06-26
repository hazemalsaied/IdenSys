/**
 * 
 */
package fr.upem.lgtools.parser;

import java.util.Iterator;
import java.util.List;
import java.util.NoSuchElementException;

import fr.upem.lgtools.text.Unit;

/**
 * @author Mathieu Constant
 *
 */
public class Container implements Iterable<Unit>{

	
	
	Element head;
	int size = 0;
	
	public Container(){
		head = null;
	}
	
	public Container(Container c){
		head = c.head;
	}
	
	public Container(Unit... units){
		head = null;
		for(int i= units.length - 1 ; i >= 0 ; i--){
		   addFirst(units[i]);	
		}
	}
	
	public Container(List<Unit> units){
		this(units.toArray(new Unit[units.size()]));
	}
	
	public int size(){
		return size;
	}
	
	private void addFirst(Unit u){
		Element h = new Element(u,head);
		head = h;
		size++;
	}
	
	public boolean isEmpty(){
		return head == null;
	}
	
	
	//pop version for buffer
	
	public Unit read(){
		return pop();
	}
	
	
	public void push(Unit u){
		addFirst(u);
	}
	
	
	public Unit pop(){
		if(isEmpty()){
			throw new IllegalStateException("Cannot pop as container is empty!");
		}
		Element h = head;
		head = head.getNext();
		size--;
		return h.getUnit();
	}

	public Unit peekFirst(){
		return head ==null?null:head.getUnit();
	}
	
	public Unit peekSecond(){
		if(head == null){
			return null;
		}
		Element next = head.getNext();
		return next == null?null:next.getUnit();
	}
	
	public Unit peekThird(){
		return peek(2);
	}
	
	
	public Unit peek(int i){
		Element current = head;
		int cnt = 0;
		while(current != null){
			if(cnt == i){
				return current.getUnit();
			}
			current = current.getNext();
			cnt++;
		}
		return null;
	}
	
	
	
	@Override
	public Iterator<Unit> iterator() {
		return new Iterator<Unit>(){
			Element current = head;

			@Override
			public boolean hasNext() {
				return current != null;
			}

			@Override
			public Unit next() {
				if(!hasNext()){
					throw new NoSuchElementException();
				}
				Element e = current;
				current = current.getNext();
				return e.getUnit();
			}

			@Override
			public void remove() {
				throw new IllegalStateException("Cannot remove elements from iterator");
			}
			
		};
	}

	@Override
	public String toString() {
		StringBuilder sb = new StringBuilder("(");
		for(Unit u:this){
			sb.append(u.toString());
			sb.append(", ");
		}
		sb.append(")");
		return sb.toString();
	}
	
	
	
	

}
