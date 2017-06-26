/**
 * 
 */
package fr.upem.lgtools2.parser;

import fr.upem.lgtools.parser.Container;
import fr.upem.lgtools.text.Unit;

/**
 * @author Mathieu
 *
 */
public class NewTest {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		Container c = new Container();

		c.push(new Unit(0,"XXX",0));
		c.push(new Unit(1,"YYY",1));
		c.push(new Unit(2,"ZZZ",2));
		c.push(new Unit(3,"AAA",3));
		System.err.println(c.peekFirst());
		System.err.println(c.peekSecond());
		System.err.println(c.peekThird());
		System.err.println(c.peek(0));
		System.err.println(c.peek(3));
		System.err.println(c.peek(4));
		System.err.println(c.size());
		c.pop();
		c.pop();
		System.err.println(c.size());
		System.err.println(c);
		System.err.println(c.peekThird());;
		c.pop();
		c.pop();
		
		//c.pop();
		
	}

}
