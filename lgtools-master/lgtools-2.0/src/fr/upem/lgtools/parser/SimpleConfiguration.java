package fr.upem.lgtools.parser;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;

import fr.upem.lgtools.text.Sentence;
import fr.upem.lgtools.text.Unit;
import fr.upem.lgtools.text.UnitFactory;
import fr.upem.lgtools.text.Utils;

public class SimpleConfiguration<T extends Analysis> implements Configuration<T>{
	private final static String NONE = "";
	private final Sentence sentence;
	private final Map<Unit,Integer> projectiveOrderPositions;
	private final Container[] buffers;
    private final Container[] stacks;
    private final T analyses;
    private final T goldAnalyses;
    
    private final List<String> history = new ArrayList<String>();
    
    
    //units is a list of non-root units
	public SimpleConfiguration(Sentence s,T analyses, T goldAnalysis, int nBuffers, int nStacks){
    	/*if(units == null){
    		throw new IllegalArgumentException("List of units cannot be null");
    	}
    	if(units.isEmpty()){
    		throw new IllegalArgumentException("List of units cannot be empty");
    	}*/
    	if(nBuffers < 1){
    		throw new IllegalArgumentException("There should be at least one buffer (instead of "+nBuffers + ")");
    	}
    	if(nStacks < 1){
    		throw new IllegalArgumentException("There should be at least one stack (instead of "+nStacks + ")");
    	}
    	
    	Unit root = UnitFactory.createRootUnit();
    	buffers = new Container[nBuffers];
    	for(int i = 0 ; i < nBuffers ; i++){
    		buffers[i] = new Container(s.getTokens());    		
    	}
    	stacks =  new Container[nStacks];
    	for(int i = 0 ; i < nStacks ; i++){
    		  stacks[i] = new Container();
    		  stacks[i].push(root);
    		  
    	}
    	this.sentence = s;
    	//this.projectiveOrderPositions = null;
    	this.projectiveOrderPositions = Utils.getProjectiveOrderPositions(s);
    	this.analyses = analyses;
    	this.goldAnalyses = goldAnalysis;
    }
    
	
	/*
	 * A REVOIR
	 * 
	 */
	
   @SuppressWarnings("unchecked")
   public SimpleConfiguration(SimpleConfiguration<T> configuration){

	   buffers = new Container[configuration.buffers.length];
	   for(int i = 0 ; i < configuration.buffers.length ; i++){
		   buffers[i] = new Container(configuration.buffers[i]);    		
	   }
	   stacks =  new Container[configuration.stacks.length];
	   for(int i = 0 ; i < configuration.stacks.length ; i++){
		   stacks[i] = new Container(configuration.stacks[i]);   		  

	   }
	   this.sentence = configuration.sentence;
	   this.projectiveOrderPositions = Utils.getProjectiveOrderPositions(this.sentence);
	   this.analyses = (T)configuration.analyses.copy();
	   this.goldAnalyses = configuration.goldAnalyses;

   }

   
   public int getProjectiveOrderPosition(Unit u){
	   /*if(projectiveOrderPositions.get(u) == null){
		   System.err.println("Proj Position "+u);
	   }*/
	   return projectiveOrderPositions.get(u);
   }
    
   public Sentence getSentence(){
	   return sentence;
   }
   
   public void addUnit(Unit u){
	   sentence.add(u);
   }
   
   
    public Unit getUnit(int id){
    	return sentence.get(id);
    }
    
    public Container getStack(int index){
    	return stacks[index];
    }
    
    
    public Container getFirstStack(){
    	return stacks[0];
    }

    public Container getSecondStack(){
    	if(stacks.length < 2){
    		throw new IllegalArgumentException("To get the second stack, there should be at leat two stacks");
    	}
    	return stacks[1];
    }
    

	public Container getFirstBuffer() {
		return buffers[0];
	}

	
	public void addAction(String action){
		this.history.add(action);
	}
	
	public String getPreviousTransition(){
		if(history.size() < 1){
			return NONE;
		}
		return history.get(history.size() - 1);
	}

	public T getAnalyses() {
		return analyses;
	}

	public T getGoldAnalyses() {
		return goldAnalyses;
	}

	@Override
	public List<String> getHistory() {
		return history;
	}
    
	public int stackCount(){
		return stacks.length;
	}
    
	public int bufferCount(){
		return buffers.length;
	}

	public boolean isTerminal(){
		//buffers must be empty
		for(Container buffer:buffers){
			if(buffer.size() != 0){
				return false;
			}
		}
		
		for(Container stack:stacks){
			if(stack.size() > 1){
				return false;
			}
		}
		
		return true;
	}
	
	@Override
	public String toString() {
		String res = getFirstStack().toString()+""+getFirstBuffer().toString()+"\n";
		if(stackCount() > 1){
		    res += getSecondStack()+"\n";
		}
		return res;
	}
	
	public List<Unit> getUnits(){
		return sentence.getUnits();
	}
	
}
