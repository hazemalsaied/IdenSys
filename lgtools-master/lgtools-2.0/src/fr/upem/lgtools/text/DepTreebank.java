package fr.upem.lgtools.text;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Iterator;
import java.util.List;

public abstract class DepTreebank implements Iterable<Sentence>{

	public int size(){
		Iterator<Sentence> it = iterator();
		int cnt = 0;
		while(it.hasNext()){
			cnt++;
		}
		return cnt;
	}
	
	
	
	public DepTreebank shuffle() {
		
		final List<Sentence> shuffled = new ArrayList<Sentence>();
		Iterator<Sentence> it = iterator(); 
		while(it.hasNext()){
			shuffled.add(it.next());
		}
		
		Collections.shuffle(shuffled);
		return new DepTreebank() {
			
			@Override
			public Iterator<Sentence> iterator() {
				return shuffled.iterator();
			}
		};
		
	}
	
			
}
