package fr.upem.lgtools.evaluation;

import fr.upem.lgtools.text.DepTreebank;

public class ParsingResult {
	private final DepTreebank treebank;
	private final ParsingAccuracy acccuracy;
	/**
	 * @param treebank
	 * @param acccuracy
	 */
	public ParsingResult(DepTreebank treebank, ParsingAccuracy acccuracy) {
		this.treebank = treebank;
		this.acccuracy = acccuracy;
	}
	
	
	public DepTreebank getTreebank() {
		return treebank;
	}
	public ParsingAccuracy getAcccuracy() {
		return acccuracy;
	}
	
	
	
	

}
