/**
 * 
 */
package fr.upem.lgtools.parser.arcstandard;

import fr.upem.lgtools.parser.Configuration;
import fr.upem.lgtools.parser.DepArc;
import fr.upem.lgtools.parser.DepTree;
import fr.upem.lgtools.text.Sentence;
import fr.upem.lgtools.text.Unit;

/**
 * @author Mathieu
 *
 */
public class ParserUtils {

	
	static boolean unitIsSyntacticallyCompleted(Unit u, DepTree tree, Sentence s){
          //System.err.println(u);
          //System.err.println(tree.getHead(u.getId()));
          if(tree.hasIncomingArc(u.getId())){
        	  //System.err.println("Incoming");
        	  return true;
          }
          boolean res = false;
          for(int d:tree.getReverseLinks(u.getId())){
        	  if(!unitIsSyntacticallyCompleted(s.get(d), tree, s)){
        		  return false;
        	  }
        	  res = true;
          }
          
          return res;
	}

	
	static Unit getLexicalUnitFromComponent(Unit u, DepTree tree, Sentence s){
		int h = tree.getFurtherLinkedNode(u.getId());
		//System.err.println("xxx"+h+"-->"+u+"-->"+s.get(h));
		//System.err.println(s.getUnits());
		
		return s.get(h);
	}
 

	public static boolean passContrainedMergeCondition(boolean withConstrainedMerge, Configuration<DepTree> configuration){
		if(withConstrainedMerge && configuration.getPreviousTransition().startsWith(FullyMWEAwareArcStandardTransitionBasedModel.MERGE)){
			return false;
		}
		return true;
	}
	
	
	public static DepTree createGoldTree(Sentence s){
		DepTree tree = new DepTree(s.getUnits().size() + 1);
		for(Unit u:s.getUnits()){
			if(u.hasGoldSyntacticHead()){
			    tree.addArc(new DepArc(u.getGoldSheadId(), u.getGoldSlabel(), u.getId()));
			}
			if(u.hasGoldLexicalHead()){
				
				tree.addLinks(u.getGoldLHead(),u.getId());
			}
		}
		return tree;
	}
	
}