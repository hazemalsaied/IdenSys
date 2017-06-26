package fr.upem.lgtools.text;


public class UnitFactory {
	private final static int ROOT_ID = 0;
	private final static int NULL_ID = -1;
	private final static String ROOT_FORM = "_ROOT_";
	private final static String CONLL_DELIM = "\t";
	private final static int CONLL_ID = 0;
	private final static int CONLL_FORM = 1;
	private final static int CONLL_LEMMA = 2;
	private final static int CONLL_CPOS = 3;
	private final static int CONLL_POS = 4;
	private final static int CONLL_FEATS = 5;
	private final static String CONLL_FEATS_DELIM = "\\|";
	private final static String CONLL_FEAT_DELIM = "=";
	private final static int CONLL_HEAD = 6;
	private final static int CONLL_LABEL = 7;
	private final static int CONLL_GOLD_HEAD = 8;
	private final static int CONLL_GOLD_LABEL = 9;
	private final static int XCONLL_GOLD_LEXICAL_ID = 11;
	private final static int XCONLL_LEXICAL_ID = 10;
	private final static int XCONLL_POSITIONS = 12;
	private final static String DUMMY = "_";
	
	public static Unit createNullUnit(){
		Unit u = new Unit(NULL_ID,DUMMY,NULL_ID);
		u.setGoldShead(-1);
		u.setShead(-1);
		return 	u;
	}
	
	public static Unit createRootUnit(){
		return new Unit(ROOT_ID,ROOT_FORM,ROOT_ID);		
	}
	
	
	
	private static void parseFeats(Unit u, String feats){
		if(feats.equals(DUMMY)){
			return;
		}
		String[] tab = feats.split(CONLL_FEATS_DELIM);
	    for(String f:tab){
	    	
	    	String[] ftab = f.split(CONLL_FEAT_DELIM);	    	
	    	if(ftab.length != 2){
	    		throw new IllegalStateException("Feature "+f+ " is illegal: format is attribute=value");
	    	}
	    	u.addFeature(ftab[0], ftab[1]);
	    }
		
	}
	
	public static Unit createUnitFromConllString(String line){
		String[] tab = line.split(CONLL_DELIM);
		Unit u = new Unit(Integer.parseInt(tab[CONLL_ID]), tab[CONLL_FORM], Integer.parseInt(tab[CONLL_ID]));
		u.setLemma(tab[CONLL_LEMMA].equals(DUMMY)?null:tab[CONLL_LEMMA]);
		u.setCpos(tab[CONLL_CPOS].equals(DUMMY)?null:tab[CONLL_CPOS]);
		u.setPos(tab[CONLL_POS]);  //compulsary non-dummy field
		parseFeats(u,tab[CONLL_FEATS]);
		//predicted arcs
		int sh = tab[CONLL_HEAD].equals(DUMMY)?-1:Integer.parseInt(tab[CONLL_HEAD]); 
		u.setShead(sh);
		u.setPredictedSlabel(tab[CONLL_LABEL]);
		// gold arcs
		sh = tab[CONLL_GOLD_HEAD].equals(DUMMY)?-1:Integer.parseInt(tab[CONLL_GOLD_HEAD]); 
		u.setGoldShead(sh);
		u.setGoldSlabel(tab[CONLL_GOLD_LABEL]);
		
		return u;
	}
	
	public static Unit createUnitFromXConllString(String line){
		String[] tab = line.split(CONLL_DELIM);
		
		//unit positions
		String positions = tab[XCONLL_POSITIONS];
		if(positions.equals(DUMMY)){
			positions = tab[CONLL_ID];
		}
		String[] p = positions.split(",");
		int ids[] = new int[p.length];
		int i = 0;
		for(String id:p){
			ids[i] = Integer.parseInt(id);
			i++;
		}
		
		Unit u = new Unit(Integer.parseInt(tab[CONLL_ID]), tab[CONLL_FORM], ids);
		u.setLemma(tab[CONLL_LEMMA].equals(DUMMY)?null:tab[CONLL_LEMMA]);
		u.setCpos(tab[CONLL_CPOS].equals(DUMMY)?null:tab[CONLL_CPOS]);
		u.setPos(tab[CONLL_POS]);  //compulsary non-dummy field
		parseFeats(u,tab[CONLL_FEATS]);
		//predicted arcs
		int sh = tab[CONLL_HEAD].equals(DUMMY)?-1:Integer.parseInt(tab[CONLL_HEAD]); 
		u.setShead(sh);
		u.setPredictedSlabel(tab[CONLL_LABEL]);
		// gold arcs
		sh = tab[CONLL_GOLD_HEAD].equals(DUMMY)?-1:Integer.parseInt(tab[CONLL_GOLD_HEAD]); 
		u.setGoldShead(sh);
		u.setGoldSlabel(tab[CONLL_GOLD_LABEL]);
		
		//predicted lexical links
		int lh = tab[XCONLL_LEXICAL_ID].equals(DUMMY)?0:Integer.parseInt(tab[XCONLL_LEXICAL_ID]); 
		u.setPredictedLhead(lh);
		lh = tab[XCONLL_GOLD_LEXICAL_ID].equals(DUMMY)?0:Integer.parseInt(tab[XCONLL_GOLD_LEXICAL_ID]); 
		u.setGoldLHead(lh);
		
		
		
		return u;
	}
	
	public static Unit createUnitFromConlluString(String line){
		String[] tab = line.split(CONLL_DELIM);
		Unit u = new Unit(Integer.parseInt(tab[CONLL_ID]), tab[CONLL_FORM], Integer.parseInt(tab[CONLL_ID]));
		u.setLemma(tab[CONLL_LEMMA].equals(DUMMY)?null:tab[CONLL_LEMMA]);
		u.setCpos(tab[CONLL_CPOS].equals(DUMMY)?null:tab[CONLL_CPOS]);
		u.setPos(tab[CONLL_POS]);  //compulsary non-dummy field
		parseFeats(u,tab[CONLL_FEATS]);
		//predicted arcs
		int sh = tab[CONLL_HEAD].equals(DUMMY)?-1:Integer.parseInt(tab[CONLL_HEAD]); 
		u.setShead(sh);
		u.setPredictedSlabel(tab[CONLL_LABEL]);
		// gold arcs
		u.setGoldShead(sh);
		u.setGoldSlabel(tab[CONLL_LABEL]);
		
		return u;
	}
	
	
}
