/**
 * 
 */
package fr.upem.lgtools.text;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * @author Mathieu Constant
 *
 * Represents a text unit: may be a token, a multiword expression, or a "subtoken" (e.g. the token 'du' may have two subtokens in French 'de' and 'le')
 *
 */


public class Unit {	
	private final static String DUMMY="_";
	
	 private final int id;
     private final String form;
     private final int[] positions;
     private String lemma;
     private String cpos;
     private String goldCpos;
     private String pos;
     private String goldPos;
     private final HashMap<String,String> feats = new HashMap<String, String>();
     private Boolean predictedSeg;
     private Boolean goldSeg;
     
     
     private int shead = -1;  //syntactic head
     private String slabel;
   //Some day: unit may have several syntactic parents
     
     
     private int goldShead = -1;  //gold syntactic head
     private String goldSlabel;  //gold label
     
     private int lhead;  // lexical head  
     private int goldLHead;  // lexical head 
     
     
     private final List<Integer> subunits = new ArrayList<Integer>();  //list of subunits??  one-token compounds?   

     
     
     /**
      * Constructor which deeply copy input unit
      * 
      * @param u input unit
      */
     
     public Unit(int id,Unit u,int... positions){
    	 this.id = id;
    	 this.form = u.form;
    	 //this.positions = Arrays.copyOf(u.positions,u.positions.length);
    	 this.positions = positions;
    	 this.lemma = u.lemma;
    	 this.cpos = u.cpos;
    	 this.pos = u.pos;
    	 this.feats.putAll(u.feats);
    	 this.shead = u.shead;
    	 this.slabel = u.slabel;
    	 this.goldShead = u.goldShead;
    	 this.goldSlabel = u.goldSlabel;
    	 this.lhead = u.lhead;
    	 this.goldLHead = u.goldLHead;
    	 this.subunits.addAll(u.subunits);
    	   	 
     }
     
     public Unit(Unit u){
    	 this(u.getId(),u,Arrays.copyOf(u.positions,u.positions.length));
     }
     
	

	public Unit(int id, String form, int... positions) {
		this.id = id;
		this.form = form;
		this.positions = positions;
	}

	
	public boolean isMWE(){
		return positions.length > 1;
	}
	
	public boolean isRegularMWE(Sentence s,boolean goldAnnotation){
		return isMWE() && !isFixedMWE(s,goldAnnotation);
	}
	
	
	public boolean isFixedMWE(Sentence s,boolean goldAnnotation){
		if(!isMWE()){
			return false;
		}
		for(int i:getPositions()){
      	    Unit c = s.get(i);
      	    if(c.hasSyntacticHead(goldAnnotation)){
      	    	return false;
      	    }
        }
		return true;
	}
	
	
	public boolean isGoldFixedMWE(Sentence s){
		return isFixedMWE(s, true);
	}
	
	public boolean isPredictedFixedMWE(Sentence s){
		return isFixedMWE(s, false);
	}
	
	
	public boolean isDiscontiguous(Sentence s){
		return isMWE() && (positions[0] + positions.length - 1 != positions[positions.length -1]);
	}
	
	
	public String getGoldPOSPattern(Sentence s){
		StringBuilder sb = new StringBuilder();
		for(int i:getPositions()){
			sb.append("_");
			sb.append(s.get(i).goldPos);
		}
		return sb.substring(1);
		
	}
	
	
	public String getPOSPattern(Sentence s){
		StringBuilder sb = new StringBuilder();
		for(int i:getPositions()){
			sb.append("_");
			sb.append(s.get(i).pos);
		}
		return sb.substring(1);
		
	}
	
	public boolean hasGoldSyntacticHead(){
		return getGoldSheadId() != -1;
	}
	
	public boolean hasPredictedSyntacticHead(){
		return getPredictedSheadId() != -1;
	}
	
	public boolean hasSyntacticHead(boolean goldAnnotation){
		return goldAnnotation?hasGoldSyntacticHead():hasPredictedSyntacticHead();
	}
	
	public boolean hasGoldLexicalHead(){
		return getGoldLHead() > 0;
	}
	
	
	public boolean hasPredictedLexicalHead(){
		return getPredictedLheadId() > 0;
	}
	
	
	public boolean hasLexicalHead(boolean goldAnnotation){
		return goldAnnotation?hasGoldLexicalHead():hasPredictedLexicalHead();
	}
	
	
	public Unit findPredictedLexicalRoot(Sentence s){
		Unit root = this;
		//System.err.println(root);
		int lh;
		while((lh = root.getPredictedLheadId()) > 0){
			root = s.get(lh);
		}
		return root;
	}
	
	
	public Unit findGoldLexicalRoot(Sentence s){
		Unit root = this;
		//System.err.println(root);
		int lh;
		while((lh = root.getGoldLHead()) > 0){
			root = s.get(lh);
		}
		return root;
	}
	
	
	public Unit GetGoldLexicalParent(Sentence s){
		int l = this.getGoldLHead();
		if(l > 0){
			return s.get(l);
		}
		return null;
	}
	
	
	public int getUnitFirstTokenPosition(){
		return positions[0];
	}
	
	public int getUnitLastTokenPosition(){
		return positions[positions.length - 1];
	}
	
	
	public boolean isPredictedMWE(Sentence s){
		if(!isMWE()){
			return false;
		}
		if(predictedSeg != null){
			return predictedSeg;
		}
		for(int c:positions){
			Unit tok = s.get(c);
			Unit lroot = tok.findPredictedLexicalRoot(s);
			if(lroot != this){
				predictedSeg = false;
				return predictedSeg;
			}
		}
		predictedSeg = true;
		return predictedSeg;
	}
	
	public boolean isGoldMWE(Sentence s){
		if(!isMWE()){
			return false;
		}
		if(goldSeg != null){
			return goldSeg;
		}
		for(int c:positions){
			Unit tok = s.get(c);
			Unit lroot = tok.findGoldLexicalRoot(s);
			if(lroot != this){
				goldSeg = false;
				return goldSeg;
			}
		}
		goldSeg = true;
		return goldSeg;
	}
	
	
	
	public String getLemma() {
		return lemma;
	}

	public void setLemma(String lemma) {
		this.lemma = lemma;
	}

	public String getCpos() {
		return cpos;
	}

	public void setCpos(String cpos) {
		this.cpos = cpos;
	}
	
	
	public String getGoldCpos() {
		return goldCpos;
	}

	public void setGoldCpos(String cpos) {
		this.goldCpos = cpos;
	}

	public String getPos() {
		return pos;
	}
	
	public String getGoldPos() {
		return goldPos;
	}

	public void setGoldPos(String goldPos) {
		this.goldPos = goldPos;
	}
	
	public void setPos(String pos) {
		this.pos = pos;
	}

	public int getPredictedSheadId() {
		return shead;
	}
	
	public int getSHead(boolean goldAnnotation){
		return goldAnnotation?getGoldSheadId():getPredictedSheadId();
	}

	
	
	
	public int getGoldSheadId() {
		return goldShead;
	}

	public void setGoldShead(int goldShead) {
		this.goldShead = goldShead;
	}
	
	

	public String getGoldSlabel() {
		return goldSlabel == null?DUMMY:goldSlabel;
	}

	public void setGoldSlabel(String goldSlabel) {
		this.goldSlabel = goldSlabel;
	}

	
	public void setShead(int shead) {
		this.shead = shead;
	}

	public String getPredictedSlabel() {
		return slabel==null?DUMMY:slabel;
	}
	
	public String getSLabel(boolean goldAnnotation){
		return goldAnnotation?getGoldSlabel():getPredictedSlabel();
	}
	

	public void setPredictedSlabel(String slabel) {
		this.slabel = slabel;
	}
   
	public void setSlabel(String label, boolean goldAnnotation){
		if(goldAnnotation){
			setGoldSlabel(label);
		}
		else{
			setPredictedSlabel(label);
		}
	}  
	

	public int getLheadId(boolean goldAnnotation){
		return goldAnnotation?getGoldLHead():getPredictedLheadId();
	}
	
	
	public int getPredictedLheadId() {
		return lhead;
	}

	
	public void setPredictedLhead(int lhead) {
		this.lhead = lhead;
	}

	
	public void setLhead(int lhead,boolean goldAnnotation) {
		if(goldAnnotation){
			setGoldLHead(lhead);
		}
		else{
			setPredictedLhead(lhead);
		}
	}
	
	
	
	
	public int getGoldLHead() {
		return goldLHead;
	}




	public void setGoldLHead(int goldLHead) {
		this.goldLHead = goldLHead;
	}




	public int getId() {
		return id;
	}

	public String getForm() {
		return form;
	}

	public int[] getPositions() {
		return positions;
	}

	
	public List<Integer> getTokenPositions(Sentence s){
		ArrayList<Integer> list = new ArrayList<Integer>();
		
		if(positions.length == 1){
			list.add(positions[0]);
		}
		else{
		for(int i:positions){
			
				Unit u = s.get(i);
				list.addAll(u.getTokenPositions(s));
				//System.err.println(s);
				
				
			}
		
		}
		
		
		
		return list;
		
	}
	
	
	
	public void addFeature(String att,String val){
		feats.put(att, val);
	}
	
	public String getFeature(String att){
		return feats.get(att);
	}

	public Map<String,String> getFeatures(){
		return feats;
	}
	
	
	public List<Integer> getSubunits() {
		return subunits;
	}
	
	public boolean isRoot(){
		return id == 0;
	}
	

	
	public boolean isGoldLexicalRoot(){
		return getGoldLHead() <= 0;
	}
	
	public boolean isPredictedLexicalRoot(){
		return getPredictedLheadId() <= 0;
	}
	
	
	public boolean isPredictedSeg() {
		return predictedSeg;
	}




	public void setPredictedSeg(boolean predictedSeg) {
		this.predictedSeg = predictedSeg;
	}




	public boolean isGoldSeg() {
		return goldSeg;
	}




	public void setGoldSeg(boolean goldSeg) {
		this.goldSeg = goldSeg;
	}


	private static boolean areEqual(Unit u, Unit v){
		int[] pu = u.getPositions();
		int[] pv = v.getPositions();
		if(pu.length != pv.length){
			return false;
		}
		for(int i = 0 ; i < pu.length ; i++){
			if(pu[i] != pv[i]){
				return false;
			}
		}
		return true;
	}
	
	@Override
	public boolean equals(Object obj) {
		if(!(obj instanceof Unit)){
			return false;
		}
		Unit u = (Unit) obj;
		return areEqual(u, this);
	}
	

	@Override
	public int hashCode() {
		return Arrays.hashCode(positions);
	}
	
	

	@Override
	public String toString(){
		/*StringBuilder sb = new StringBuilder();
		sb.append(id)
		   .append("\t")
		   .append(form)
		   .append("\t")
		   .append(lemma).append(Arrays.toString(positions))
		   .append("\t")
		   .append(cpos)
		   .append("\t")
		   .append(pos)
		   .append("\t")
		   .append(feats)
		   .append("\t")
		   .append(shead).append("\t").append(slabel)
		   .append("\n");	
		*/
		/*sb.append(id).append(":").append(form).append(":").append(shead)
		   .append(":").append(slabel);*/
		//return sb.toString();
		return form+"("+id+","+pos+":"+positions.length+")";
	}
     
     
}
