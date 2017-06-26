/**
 * 
 */
package fr.upem.lgtools.parser;

import fr.upem.lgtools.text.Sentence;

/**
 * @author mconstant
 *
 */
public class Configurations {
	
	public static <T extends Analysis> Configuration<T> createDefaultConfiguration(Configuration<T> c){
		return new SimpleConfiguration<T>((SimpleConfiguration<T>)c);
		
	}
	
	public static Configuration<DepTree> createDefaultConfiguration(Sentence s,int bufferCount, int stackCount, DepTree goldTree){
		return new SimpleConfiguration<DepTree>(s, new DepTree(s.getUnits().size() + 1),goldTree, bufferCount, stackCount);
		//return new SimpleConfiguration<T>();
		
	}
	

}
