package fr.upem.lgtools.parser;

public class DepArc {
	private final int head;
	private final String label;
	private final int dep;
	
	public DepArc(int head, String label, int dep) {
		this.head = head;
		this.label = label;
		this.dep = dep;
	}

	public int getHead() {
		return head;
	}

	public String getLabel() {
		return label;
	}

	public int getDep() {
		return dep;
	}

	
	@Override
	public String toString() {		
		return "("+head+","+label+","+dep+")";
	}
	
	
}
