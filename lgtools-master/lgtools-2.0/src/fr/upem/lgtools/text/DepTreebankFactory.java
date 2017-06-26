package fr.upem.lgtools.text;

import java.util.Iterator;
import java.util.NoSuchElementException;

public class DepTreebankFactory {
	
	public static DepTreebank filter(final DepTreebank tb, final FilterTreebank filter){
		return new DepTreebank() {
			
			@Override
			public int size() {
				return tb.size();
			}
			
			
			
			@Override
			public Iterator<Sentence> iterator() {
				
				return new Iterator<Sentence>() {
                    Iterator<Sentence> it = tb.iterator();
                    Sentence nextSentence = null;
                    
					@Override
					public boolean hasNext() {
						if(nextSentence == null){
							boolean stop = false;
							while(it.hasNext() && !stop){
								nextSentence = it.next();
								if(filter.accept(nextSentence)){
									stop = true;
								}
								else{
									nextSentence = null;
								}
							}
							
						}
						return nextSentence != null;
					}

					@Override
					public Sentence next() {
						if(!hasNext()){
							throw new NoSuchElementException();
						}
						Sentence s = nextSentence;
						nextSentence = null;
						return s;
					}

					@Override
					public void remove() {
						throw new UnsupportedOperationException();
						
					}
				};
			}
		};
		
	}
	
	
	public static DepTreebank limitSize(final DepTreebank tb,final int n){
		return new DepTreebank() {
			
			@Override
			public Iterator<Sentence> iterator() {
				
				return new Iterator<Sentence>() {
					int cnt = 0;
					Iterator<Sentence> it = tb.iterator();

					@Override
					public boolean hasNext() {
						
						return it.hasNext() && cnt < n;
					}

					@Override
					public Sentence next() {
						if(!hasNext()){
							throw new NoSuchElementException();
						}
						cnt++;
						return it.next();
					}

					@Override
					public void remove() {
						throw new IllegalStateException();
					}
				};
			}
			
			@Override
			public int size() {
				return tb.size();
			}
			
		};
		
	}
	
	
	
	
	
	public static DepTreebank filterNonProjective(DepTreebank tb){
		return filter(tb, new FilterTreebank() {
			
			@Override
			public boolean accept(Sentence sentence) {
				return Utils.isProjectiveSentence(sentence);
			}
		});
		
	}

	public static DepTreebank filterOverlappingMWE(DepTreebank tb){
		return filter(tb, new FilterTreebank() {
			
			@Override
			public boolean accept(Sentence sentence) {
				return !Utils.hasOverlappingMWE(sentence);
			}
		});
		
	}
	
	
}
