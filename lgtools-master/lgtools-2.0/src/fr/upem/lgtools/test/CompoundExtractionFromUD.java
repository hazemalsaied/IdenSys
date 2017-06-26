/**
 * 
 */
package fr.upem.lgtools.test;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.InputStreamReader;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.Set;

import fr.upem.lgtools.text.BufferedDepTreebank;
import fr.upem.lgtools.text.DepTreebank;
import fr.upem.lgtools.text.DepTreebankFactory;
import fr.upem.lgtools.text.Sentence;
import fr.upem.lgtools.text.StreamDepTreebank;
import fr.upem.lgtools.text.StreamDepTreebank.ReaderType;
import fr.upem.lgtools.text.Unit;

/**
 * @author mconstant
 *
 */
public class CompoundExtractionFromUD {

	private static interface Filter{
		boolean accept(List<Unit> u);
	}
	
	
	public static DepTreebank readTreebank(String filename) throws FileNotFoundException{
		return readTreebank(filename,-1);
	}

	 public static DepTreebank readTreebank(String filename,int size) throws FileNotFoundException{
		BufferedReader reader = new BufferedReader(new InputStreamReader(new FileInputStream(filename)));
		DepTreebank gold = new BufferedDepTreebank(new StreamDepTreebank(reader,ReaderType.CONLLU));
		if(size >= 0){
			gold = DepTreebankFactory.limitSize(gold, size);
		}
		return gold;
	}
	
	 
	 public static Map<Unit,List<Unit>> getCompoundChildren(Sentence s){
		 Map<Unit,List<Unit>> children = new HashMap<Unit, List<Unit>>();
		 for(Unit u:s.getTokens()){
			 int h = u.getGoldSheadId();
			 String l = u.getGoldSlabel();
			 //System.err.println(l);
			 if(l.equals("compound")){
				 //System.err.println(l);
				 Unit head = s.get(h);
				 List<Unit> ch = children.get(head);
				 if(ch == null){
					 ch = new LinkedList<Unit>();
					 children.put(head, ch);
				 }
				 ch.add(u);
			 }		 
		 }
		 
		 return children;
	 }
	 
	 
	 public static List<Unit> getCompound(Unit u, Map<Unit,List<Unit>> children){
		 LinkedList<Unit> cmp =  new LinkedList<Unit>();
		 cmp.add(u);
		 List<Unit> ch = children.get(u);
		 if(ch != null){
			 for(Unit v:ch){
				 List<Unit> tmp = getCompound(v,children);
				 cmp.addAll(tmp);
			 }		 
		 }
		 return cmp;		 
	 }
	 
	 
	public static void main(String[] args) throws FileNotFoundException {
		DepTreebank tb = readTreebank("ud-treebanks-v1.3/UD_French/fr-ud-train.conllu");
		Filter englishFilter = new Filter() {
			
			@Override
			public boolean accept(List<Unit> mwe) {
				for(Unit u:mwe){
					if(!u.getPos().equals("NN")&&!u.getPos().equals("NNS")&&!u.getPos().equals("JJ")){					
						return false;
					}
				}
				return true;
			}
		};
		
Filter frenchFilter = new Filter() {
			
			@Override
			public boolean accept(List<Unit> mwe) {
				
				return true;
			}
		};
		
		Set<String> mwes = new HashSet<String>();
		
		for(Sentence s:tb){
			Map<Unit,List<Unit>> map = getCompoundChildren(s);
			for(Unit u:s.getTokens()){
				List<Unit> list =  getCompound(u,map);
				if(list.size() > 1){
					Collections.sort(list,new Comparator<Unit>() {

						@Override
						public int compare(Unit arg0, Unit arg1) {						
							return arg0.getId() - arg1.getId();
						}

					});
					//if(englishFilter.accept(list)){
					if(frenchFilter.accept(list)){
					   String st = "";
					   String pos = "";
					   for(Unit v:list){
						   st += "_"+v.getForm();
						   pos += "_"+v.getPos();
					   }
					   
					   mwes.add(st.substring(1)+"\t"+pos.substring(1));
					}
				}

			}
		}
        for(String w:mwes){
        	System.out.println(w);
        }	
		
	}
	
}
