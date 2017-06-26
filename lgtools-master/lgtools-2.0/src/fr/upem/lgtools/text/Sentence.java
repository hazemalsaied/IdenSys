/**
 * 
 */
package fr.upem.lgtools.text;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

/**
 * @author mconstant
 *
 */
public class Sentence {
	private static final Unit ROOT = UnitFactory.createRootUnit();
	private final List<Unit> units = new ArrayList<Unit>(); 
	private final int size; //token count 
	private final HashMap<Integer,Unit> map = new HashMap<Integer, Unit>();
	
	public Sentence(List<Unit> units){
		this.units.addAll(units);
		for(Unit u:units){
			map.put(u.getId(), u);
		}
		this.size = tokenCount();		
	}
	
	private int tokenCount(){
		int cnt = 0;
		for(Unit u:units){
			if(u.isMWE()){
				return cnt;
			}
			cnt++;
		}
		return units.size();
	}
	
	
	
	/**
	 * Constructor which deeply copy input sentence 
	 * 
	 * @param s input sentence
	 */
	
	public Sentence(Sentence s){
		for(Unit u:s.getUnits()){
			add(new Unit(u));
		}
		this.size = s.size;
	}
	
	
	public Unit get(int id){
		//System.err.println(map);
		Unit u = map.get(id);
		return u == null?ROOT:u; 
	}
	
	public boolean add(Unit u){
		if(map.containsKey(u.getId())){
			return false;
		}
		map.put(u.getId(), u);
		return units.add(u);
		
	}
	
	public List<Unit> getTokens(){
		return units.subList(0, size);		
	}
	
	public List<Unit> getUnits(){
		//System.err.println(map);
		return units;		
	}
	
	public List<Unit> getMWUnits(){
		return units.subList(size,units.size());
	}
	
	
	/**
	 * 
	 * @return the sequence of tokens after merging of irregular/fixed MWEs
	 */
	
	public List<Unit> getTokenSequence(boolean goldAnnotation){
		
		return Utils.getUnitSequence(goldAnnotation,getUnits().size(),this,getTokens(),true);
		
	}
	
	/**
	 * 
	 * @return the sequence of units after merging of all MWEs
	 */
	
	public List<Unit> getUnitSequence(boolean goldAnnotation){
		return Utils.getUnitSequence(goldAnnotation,getUnits().size(),this,getTokens(),false);
		
	}
	
	
	@Override
	public String toString() {
		StringBuffer sb = new StringBuffer();
		for(Unit u:units){
			sb.append(u);	
		}		
		return sb.toString();
	}

}
