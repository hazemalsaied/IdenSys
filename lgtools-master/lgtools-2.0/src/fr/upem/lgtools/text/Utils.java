package fr.upem.lgtools.text;

import java.io.BufferedWriter;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.io.UnsupportedEncodingException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.TreeSet;

public class Utils {
	
	
	private static String feats(Map<String,String> feats){
		StringBuilder sb = new StringBuilder();
		if(feats.size() == 0){
			return "_";
		}
		for(String att:feats.keySet()){
			sb.append("|").append(att).append("=").append(feats.get(att));			
		}
		sb.deleteCharAt(0);
		return sb.toString();
		
	}
	
	
	private static void writeUnit(BufferedWriter out, Unit u) throws IOException{
		out.write(u.getId()+"\t"+u.getForm()+"\t"+u.getLemma()+"\t"+u.getCpos());
		out.write("\t"+u.getPos()+"\t"+feats(u.getFeatures()));
		out.write("\t"+u.getPredictedSheadId()+"\t"+u.getPredictedSlabel());
		out.write("\t"+u.getGoldSheadId()+"\t"+u.getGoldSlabel());
		out.write("\n");
		
	}
	
	private static void writeMergedUnit(BufferedWriter out, Unit u,Map<Integer,Integer> map) throws IOException{
		out.write(map.get(u.getId())+"\t"+u.getForm()+"\t"+u.getLemma()+"\t"+u.getCpos());
		out.write("\t"+u.getPos()+"\t"+feats(u.getFeatures()));
		out.write("\t"+map.get(u.getPredictedSheadId())+"\t"+u.getPredictedSlabel());
		out.write("\t"+map.get(u.getGoldSheadId())+"\t"+u.getGoldSlabel());
		out.write("\n");
		
	}
	
	private static void writeUnitInXConll(BufferedWriter out, Unit u) throws IOException{
		out.write(u.getId()+"\t"+Arrays.toString(u.getPositions())+"\t"+u.getForm()+"\t"+u.getLemma()+"\t"+u.getCpos());
		out.write("\t"+u.getPos()+"\t"+feats(u.getFeatures()));
		out.write("\t"+u.getPredictedSheadId()+"\t"+u.getPredictedSlabel());
		out.write("\t"+u.getGoldSheadId()+"\t"+u.getGoldSlabel());
		out.write("\t"+u.getPredictedLheadId()+"\t"+u.getGoldLHead());
		out.write("\n");
		
	}
	
	
	public static void writeSentenceInXConll(BufferedWriter out,Sentence s) throws IOException{
		
		for(Unit u:s.getUnits()){
			writeUnitInXConll(out,u);
		}
		out.write("\n");
	}
	
	
public static void writeSentenceInConll(BufferedWriter out,Sentence s) throws IOException{
		for(Unit u:s.getTokens()){
			writeUnit(out,u);
			
		}
		out.write("\n");
	}
	
	
	
	
	public static BufferedWriter openBufferedWriter(String filename) throws UnsupportedEncodingException, FileNotFoundException{
		return new BufferedWriter(new OutputStreamWriter(new FileOutputStream(filename), "UTF-8"));
	}
	
	
	public static void saveTreebankInConll(DepTreebank tb,String filename) throws IOException{
		BufferedWriter out = new BufferedWriter(new OutputStreamWriter(new FileOutputStream(filename), "UTF-8"));
		for(Sentence s:tb){
			for(Unit u:s.getTokens()){
				writeUnit(out,u);
			}
			out.write("\n");
		}
		out.close();			
	}
	
	public static void saveTreebankInXConll(DepTreebank tb,String filename) throws IOException{
		BufferedWriter out = new BufferedWriter(new OutputStreamWriter(new FileOutputStream(filename), "UTF-8"));
		for(Sentence s:tb){
			writeSentenceInXConll(out, s);
		}
		out.close();			
	}
	
	
	private static boolean isCrossing(int i1, int j1, int i2, int j2){
		int tmp = i1;
		i1 = Math.min(i1, j1);
		j1 = Math.max(tmp,j1);
		tmp = i2;
		i2 = Math.min(i2, j2);
		j2 = Math.max(tmp,j2);
		//System.err.println(i1+","+j1+":"+i2+","+j2);
		if(i1 < i2 && i2 < j1 && j1 < j2){
			return true;
		}
		return false;
	}
	
	
	
	
	public static boolean hasOverlappingMWE(Sentence sentence){
		
		//very costly
		for(Unit u:sentence.getTokenSequence(true)){
			 for(Unit v:sentence.getTokenSequence(true)){
				 if(u == v){
					 continue;
				 }
				 if(u.isGoldFixedMWE(sentence) && v.isGoldFixedMWE(sentence)){
					Unit w = u.getUnitFirstTokenPosition() < v.getUnitFirstTokenPosition()?u:v;
					Unit z = u == w?v:u;
					if(w.getUnitLastTokenPosition() >= z.getUnitFirstTokenPosition()){
						//System.err.println(Arrays.toString(w.getPositions()));
						//System.err.println(Arrays.toString(z.getPositions()));
						System.err.println(sentence.getTokenSequence(true));
						System.err.println("Sentence has overlapping fixed MWEs!!");
						return true;
					}
					 
					 
					 
				 }
			 }
		}
		return false;
	}
	
	
	
	
	
	public static boolean isProjectiveSentence(Sentence sentence){
		//Necessary condition: fixed MWEs must be contiguous
		
		
		for(Unit u:sentence.getTokenSequence(true)){
			int[] positions = u.getPositions();
			//patch: some mwe u may not be fixed (because of stupid implementation that did not generalize for embeddings)
			if(u.isRegularMWE(sentence,true)){
				Unit c = null;
				for(int i:positions){
					c = sentence.get(i);
					if(c.isFixedMWE(sentence, true)){
						break;
					}
				}
				positions = c.getPositions();
			}
			
			
			
			Arrays.sort(positions);
			int pos0 = positions[0];
			for(int i = 1; i < positions.length ; i++){
				int pos1 = positions[i];
				if(pos1 != pos0 + 1){
					System.err.println("Sentence with non-contiguous fixed expressions");
					System.err.println(u+"---"+Arrays.toString(positions));
					System.err.println(sentence.getTokenSequence(true));
					return false;
				}
				pos0 = pos1;
				
			}
			
		}
		
		//Standard non-projectivity test
		for(Unit u1:sentence.getTokenSequence(true)){
			for(Unit u2:sentence.getTokenSequence(true)){
				if(u1 != u2){
					
					int j1 = sentence.get(u1.getGoldSheadId()).getUnitFirstTokenPosition();
					Unit u = sentence.get(u2.getGoldSheadId());
					//System.err.println(u2+"=="+u1);
					
					int j2 = u.getUnitFirstTokenPosition();
					int i1 = u1.getUnitFirstTokenPosition();
					int i2 = u2.getUnitFirstTokenPosition();
					if(isCrossing(i1,j1,i2,j2)){
						//System.err.println(u1.getGoldSheadId());
						  //System.err.println(u1+"--"+i1+" "+j1);
						  //System.err.println(u2+"--"+i2+" "+j2);
						 //System.err.println(sentence);
						System.err.println("Non projective sentence (class Utils)");
						//System.err.println(sentence);
								return false;
					}
					
				}

			}

		}
		
		
		
		return true;
	}

	
	final static private Comparator<Unit> COMP = new Comparator<Unit>() {

		@Override
		public int compare(Unit o1, Unit o2) {
			return new Integer(o1.getUnitFirstTokenPosition()).compareTo(o2.getUnitFirstTokenPosition());
		}
	};
	
	
	public static Map<Integer,Collection<Unit>> getGoldChildren(Sentence s){
		HashMap<Integer,Collection<Unit>> children = new HashMap<Integer, Collection<Unit>>();

		
		for(Unit u:s.getTokenSequence(true)){
			//System.err.println(u+"=="+u.getGoldSheadId());
			if(u.hasGoldSyntacticHead()){
				int h = u.getGoldSheadId();
				//Unit head = s.get(h);
				Collection<Unit> ch = children.get(h);
				if(ch == null){
					ch = new TreeSet<Unit>(COMP);
					//ch = new LinkedList<Unit>();
					children.put(h, ch);
				}
				ch.add(u);
			}
		}
		
		
		return children;
	}
	
	
	private static List<Unit> getLeftChildren(Collection<Unit> l,Unit node){
		LinkedList<Unit> res = new LinkedList<Unit>();
		if(l == null){
			return Collections.emptyList();
		}
		int n = node.getUnitFirstTokenPosition();
		//System.err.println("###"+node+"="+n);
		for(Unit u:l){
			
			int c = u.getUnitFirstTokenPosition();
			//System.err.println(u+">>>"+c);
			if(c < n){
				res.add(u);	
			}
			
		}
		//System.err.println(res);
		return res;
	}
	
	private static List<Unit> getRightChildren(Collection<Unit> l,Unit node){
		LinkedList<Unit> res = new LinkedList<Unit>();
		if(l == null){
			return Collections.emptyList();
		}
		int n = node.getUnitFirstTokenPosition();
		//System.err.println("==>"+node+"="+n);
		for(Unit u:l){
			//System.err.println(u);
			int c = u.getUnitFirstTokenPosition();
			if(c > n){
				res.add(u);	
			}
		}
		//System.err.println(res);
		return res;
	}
	
	
	
	
	private static LinkedList<Unit> traverse(int node,  Map<Integer,Collection<Unit>> children, Sentence s){
		LinkedList<Unit> ordered = new LinkedList<Unit>();
		Unit n = s.get(node);
		Collection<Unit> ch = children.get(node);
		//System.err.println(node+"="+ch);
		
		
		
		for(Unit u:getLeftChildren(ch, n)){
			ordered.addAll(traverse(u.getId(),children,s));
		}
		ordered.add(n);
		
		for(Unit u:getRightChildren(ch, n)){
			ordered.addAll(traverse(u.getId(),children,s));
		}
		
		return ordered;
	}
	
	public static Map<Unit,Integer> getProjectiveOrderPositions(Sentence s){
		 Map<Integer,Collection<Unit>> children = getGoldChildren(s);
		 //System.err.println("ICI");
		 //System.err.println("=="+s);
		LinkedList<Unit> ordered = traverse(0,children,s); 
		Map<Unit,Integer> positions = new HashMap<Unit, Integer>();
		//System.err.println("="+ordered);
		//System.err.println("="+children);
		int cnt = 0;
		for(Unit u:ordered){
			positions.put(u, cnt);
			cnt++;
		}
		 return positions;
		 
	}
	
	
	//awful patch to deal with embedding
	
	public static Unit patchGetLexicalRoot(Sentence s,Unit initial, Unit current,boolean goldAnnotation){
		if(current.isRegularMWE(s, goldAnnotation)){
			//try to find the initial one in children
			for(int i: current.getPositions()){
				Unit v = s.get(i);
				if(initial == v){
					return v;
				}
			}
			//if initial one not found, get first fixed one
			for(int i: current.getPositions()){
				Unit v = s.get(i);
				if(v.isFixedMWE(s, goldAnnotation)){
					return v;
				}
			}
			
		}
		
		return current;
	}
	
	
	
	public static List<Unit> getUnitSequence(boolean goldAnnotation, int sizeMax, Sentence s, Iterable<Unit> initialTokenList,boolean onlyFixedMwe){
		List<Unit> tokens = new ArrayList<Unit>();
		boolean[] handled = new boolean[sizeMax+1];
	    //System.err.println(initialTokenList);
		for(Unit u:initialTokenList){
			Unit r = u;
			if(goldAnnotation){
				if(!onlyFixedMwe || !u.hasGoldSyntacticHead()){
				   r = u.findGoldLexicalRoot(s);
				}
				
			}
			else{
				if(!onlyFixedMwe || !u.hasPredictedSyntacticHead()){
				   r = u.findPredictedLexicalRoot(s);
				}
				
			}
			r = patchGetLexicalRoot(s,u,r,goldAnnotation);
			//System.err.println(u);
			//System.err.println(r);
			
		    if(!handled[r.getId()]){
				handled[r.getId()] = true;
				tokens.add(r);
			}
			
		}
		return tokens;
	}
	
	
	
	
	
}
