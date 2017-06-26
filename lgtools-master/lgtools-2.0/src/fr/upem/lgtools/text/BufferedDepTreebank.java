package fr.upem.lgtools.text;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

public class BufferedDepTreebank extends DepTreebank {
    private final List<Sentence> sentences = new ArrayList<Sentence>();	
	
    public BufferedDepTreebank(DepTreebank tb){
    	for(Sentence s:tb){
    		sentences.add(s);    		
    	}
    	
    }
    
    
	@Override
	public Iterator<Sentence> iterator() {
		return sentences.iterator();
	}

	
	@Override
	public int size() {
		return sentences.size();
	}
	
	

	
}
