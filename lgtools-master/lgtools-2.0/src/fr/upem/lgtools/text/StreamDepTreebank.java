package fr.upem.lgtools.text;

import java.io.BufferedReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;
import java.util.NoSuchElementException;

public class StreamDepTreebank extends DepTreebank {

   public static enum ReaderType{
	   CONLL,XCONLL,CONLLU
   }
	
   private BufferedReader reader;
   private final ReaderType readerType;
	
	public StreamDepTreebank(BufferedReader reader) {
		this.reader = reader;
		this.readerType = ReaderType.CONLL;
	}
	
	public StreamDepTreebank(BufferedReader reader,ReaderType readerType) {
		this.reader = reader;
		this.readerType = readerType;
	}
	
	
	

	@Override
	public Iterator<Sentence> iterator() {
		return new Iterator<Sentence>() {

			private boolean canDoReading = true;
			private Sentence currentSentence;
			
			
			private boolean isValidLine(String line){
				
				
				if(line.startsWith("#")) return false;
				String[]tab = line.split("\t");
				if(tab[0].contains("-")){					
					return false;				
				}
				return true;
			}
			
			private Sentence readSentence() throws IOException{
				List<Unit> units = new ArrayList<Unit>();
				String line;
				if(reader == null){
					return null;
				}				
				while(((line = reader.readLine())!=null) && (!line.isEmpty())){
					//System.err.println("##"+line);
					if(isValidLine(line)){
						switch(readerType){
						case CONLL:{
							units.add(UnitFactory.createUnitFromConllString(line));
							break;
						}
						case XCONLL:{
							units.add(UnitFactory.createUnitFromXConllString(line));
							break;
						}
						case CONLLU:{
							units.add(UnitFactory.createUnitFromConlluString(line));
							break;
						}
						default:{
							throw new IllegalStateException(readerType+" is an unknown CONLL-like format");
						}

						}
						
					}
					//System.err.println(line);
				}

				if(line == null){
					//reader.close(); //to be closed externally
					reader = null;
				}
				return units.isEmpty()?null:new Sentence(units);
			}

			
			
			@Override
			public boolean hasNext() {
				if(canDoReading){
					try {
						currentSentence = readSentence();  
					} catch (IOException e) {
						throw new RuntimeException(e);
					}
				}
				canDoReading = false;
				return currentSentence != null; 
			}

			@Override
			public Sentence next() {
				if(!hasNext()){
					throw new NoSuchElementException();
				}
				 canDoReading = true;
                 return currentSentence;		
			}

			@Override
			public void remove() {
				throw new UnsupportedOperationException("Removal of a sentence is forbidden !!");
			}
			
		};
	}



}
