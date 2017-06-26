/**
 * 
 */
package fr.upem.lgtools.parser.transitions;

/**
 * @author Mathieu Constant
 *
 */
public class Transitions {
	private final static String SEP = "#";
	
	public static <T> String getLabel(String transitionId){
		String[] tab = transitionId.split(SEP);
		if(tab.length == 1){
			return null;
		}
		return tab[1];
	}
	
	public static <T> String getType(String transitionId){
		String[] tab = transitionId.split(SEP);		
		return tab[0];
	}
	
	public static <T> String constructTransitionId(String type,String label){
		if(label == null){
			return type;
		}
		return type+SEP+label;
	}
	

}
