/**
 * 
 */
package fr.upem.lgtools2.parser;

/**
 * @author Mathieu
 *
 */
interface Transition {
	public State perform(State state);
	public boolean isValid(State state);

}
