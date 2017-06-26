/**
 * 
 */
package fr.upem.lgtools.parser;

import java.util.List;

import fr.upem.lgtools.text.Sentence;
import fr.upem.lgtools.text.Unit;

/**
 * @author Mathieu
 *
 */
public interface Configuration<T extends Analysis> {

	List<String> getHistory();

	boolean isTerminal();

	T getAnalyses();

	Container getFirstStack();

	Container getSecondStack();

	Sentence getSentence();

	Unit getUnit(int l1);

	Container getFirstBuffer();

	T getGoldAnalyses();

	int getProjectiveOrderPosition(Unit s0);

	int stackCount();

	String getPreviousTransition();

	void addAction(String id);


}
