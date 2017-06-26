/**
 * 
 */
package fr.upem.lgtools.parser;

import java.util.List;

import fr.upem.lgtools.text.Unit;

/**
 * @author Matthieu Constant
 *
 */
public interface Analysis{
	public Analysis copy();
	public boolean isBeingProcessed(Unit unit);
	public void setAsBeingProcessed(Unit unit);
	public boolean isGold(List<Unit> units);
	
}
