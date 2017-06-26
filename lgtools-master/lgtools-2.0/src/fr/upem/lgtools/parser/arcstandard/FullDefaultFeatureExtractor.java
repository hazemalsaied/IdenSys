/**
 * 
 */
package fr.upem.lgtools.parser.arcstandard;



import fr.upem.lgtools.parser.Configuration;
import fr.upem.lgtools.parser.Container;
import fr.upem.lgtools.parser.DepTree;
import fr.upem.lgtools.parser.ExternalData;
import fr.upem.lgtools.parser.features.FeatureMapping;
import fr.upem.lgtools.parser.features.FeatureUtils;
import fr.upem.lgtools.parser.features.FeatureVector;
import fr.upem.lgtools.text.Sentence;
import fr.upem.lgtools.text.Unit;

/**
 * @author Mathieu
 *
 */
public class FullDefaultFeatureExtractor extends DefaultFeatureExtractor {

	public FullDefaultFeatureExtractor(FeatureMapping featureMapping) {
		super(featureMapping);
	}
	
	private void extractLexicalFeatures(Configuration<DepTree> configuration, FeatureVector feats){
		Container buffer = configuration.getFirstBuffer();
		Container stack= configuration.getSecondStack();
		//feats.add("BIAS");
		//feats.add("EMPTY2");
		Unit s0u = FeatureUtils.getUnit(stack.peekFirst());
		Unit s1u = FeatureUtils.getUnit(stack.peekSecond());
		//Unit s2u = FeatureUtils.getThirdElementInStack(stack);
		Unit b0u = FeatureUtils.getUnit(buffer.peekFirst());
		Unit b1u = FeatureUtils.getUnit(buffer.peekSecond());
		//Unit b2u = FeatureUtils.getThirdElementInBuffer(buffer);
		
		FeatureUtils.addUnitFeatures("lex:s0u", s0u,feats,configuration);
		FeatureUtils.addUnitFeatures("lex:s1u", s1u,feats,configuration);
		
		
		
		//FeatureUtils.addUnitFeatures("lex:s2u", s2u,feats,configuration);
		FeatureUtils.addUnitFeatures("lex:b0u", b0u,feats,configuration);
		//FeatureUtils.addUnitFeatures("lex:b1u", b1u,feats,configuration);
		//FeatureUtils.addUnitFeatures("lex:b2u", b2u,feats,configuration);
		
		
		FeatureUtils.addUnitPairFeatures("lex:s0u_s1u",s0u,s1u,feats,configuration);	
		FeatureUtils.addUnitPairFeatures("lex:s0u_b0u",s0u,b0u,feats,configuration);
		
		//FeatureUtils.addUnitTripletFeatures("lex:s2u_s1u_s0u",s2u,s1u,s0u,feats,configuration);
		FeatureUtils.addUnitTripletFeatures("lex:s1u_s0u_b0u",s1u,s0u,b0u,feats,configuration);
		FeatureUtils.addUnitTripletFeatures("lex:s0u_b0u_b1u",s0u,b0u,b1u,feats,configuration);
		
		//FeatureUtils.addDistanceFeature("lex:dist_s0u_s1u",s1u,s0u,feats);
		
	}
	
	
	private static void addCombinedLexicalAndSyntacticFeatures(String fid,Unit u,Configuration<DepTree> configuration, FeatureVector feats){
		DepTree tree = configuration.getAnalyses();
		int lexid = tree.getFurtherLinkedNode(u.getId());
		feats.add(fid+"_mwe"+(lexid>0?"yes":"no"));
		if(lexid > 0){
		   Unit mwe = configuration.getSentence().get(lexid);
		   feats.add(fid+"_mwet"+mwe.getPos());
		   feats.add(fid+"_mwec"+mwe.getCpos());
		   
		   feats.add(fid+"_mwef"+mwe.getForm());
		   feats.add(fid+"_mwel"+mwe.getLemma());
		}
	}
	
    private static boolean isMultiword(int node,int initial){
    	return node != initial;
    }
	
	
	private static void addCombinedLexicalAndSyntacticPairFeatures(String fid,Unit u1,Unit u2,Configuration<DepTree> configuration, FeatureVector feats){
		DepTree tree = configuration.getAnalyses();
		int u1id = u1.getId();
		int u2id = u2.getId();
		int lex1id = tree.getFurtherLinkedNode(u1id);
		int lex2id = tree.getFurtherLinkedNode(u2id);
		Sentence s = configuration.getSentence();

		
        if(isMultiword(lex2id,u2id) && isMultiword(lex1id,u1id)){
        	Unit mwe1 = s.get(lex1id);
        	Unit mwe2 = s.get(lex2id);
        	
        	feats.add(fid+"_sharedmwe:"+((lex1id == lex2id) ?"yes":"no"));
        	if(mwe1 == mwe2){ //elements belong to the same MWE (internal structure)
        		feats.add(fid+"_sharedmwe_patt_u1t"+mwe1.getPOSPattern(s)+"/"+u1.getPos());
        		feats.add(fid+"_sharedmwe_patt_u1c"+mwe1.getPOSPattern(s)+"/"+u1.getCpos());
        		
        		feats.add(fid+"_sharedmwe_patt_u2t"+mwe1.getPOSPattern(s)+"/"+u2.getPos());
        		feats.add(fid+"_sharedmwe_patt_u2c"+mwe1.getPOSPattern(s)+"/"+u2.getCpos());
        		
        		feats.add(fid+"_sharedmwe_patt_u1t_u2t"+mwe1.getPOSPattern(s)+"/"+u1.getPos()+"/"+u2.getPos());
        		feats.add(fid+"_sharedmwe_patt_u1c_u2c"+mwe1.getPOSPattern(s)+"/"+u1.getCpos()+"/"+u2.getCpos());
        		
        	}
        	else{
        		FeatureUtils.addUnitPairFeatures(fid+"u_u", mwe1, mwe2, feats, configuration);
        	}
        	//System.err.println("33333"+u1+"/"+u2);
        	
        }
        else{
        	//external arcs
        	if(isMultiword(lex1id,u1id)){
    			Unit mwe = s.get(lex1id);
    		    FeatureUtils.addUnitPairFeatures(fid+"u_u", mwe, u2, feats, configuration);
    		    //System.err.println("1111:"+u1+"/"+u2+"/"+mwe);
    		}
            if(isMultiword(lex2id,u2id)){
            	Unit mwe = s.get(lex2id);
    		    FeatureUtils.addUnitPairFeatures(fid+"u_u", u1,mwe, feats, configuration);
    		    //System.err.println("22222"+u1+"/"+u2+"/"+mwe);
    		}	
        }
		/*
		
		if(lex1id > 0 && lex2id > 0){
			
			//System.err.println("HHH");
			feats.add(fid+"_sharedmwe:"+((lex1id == lex2id) ?"yes":"no"));
			if(lex1id == lex2id){
				Unit mwe = configuration.getSentence().get(lex1id);
				feats.add(fid+"_sharedmwet:"+mwe.getPos());
				feats.add(fid+"_sharedmwec:"+mwe.getCpos());
				feats.add(fid+"_sharedmwettt:"+mwe.getPos()+"/"+u1.getPos()+"/"+u2.getPos());
				feats.add(fid+"_sharedmwetcc:"+mwe.getPos()+"/"+u1.getCpos()+"/"+u2.getCpos());
				feats.add(fid+"_sharedmwef"+mwe.getForm());
				feats.add(fid+"_sharedmwel"+mwe.getLemma());
				//System.err.println(fid+"_sharedmwettt"+mwe.getPos()+"/"+u1.getPos()+"/"+u2.getPos());
			}
		}
		else{
			if(lex1id > 0){
				Unit mwe = configuration.getSentence().get(lex1id);
				feats.add(fid+"_mwef_c"+mwe.getForm()+"/"+u2.getCpos());
				feats.add(fid+"_mwef_t"+mwe.getForm()+"/"+u2.getPos());
				feats.add(fid+"_mwef_f"+mwe.getForm()+"/"+u2.getForm());
				feats.add(fid+"_mwet_f"+mwe.getPos()+"/"+u2.getForm());
				feats.add(fid+"_mwet_t"+mwe.getPos()+"/"+u2.getPos());
				feats.add(fid+"_mwet_c"+mwe.getPos()+"/"+u2.getCpos());
			}
			
			
		}
		*/
		
	}
	
	private void extractCombinedLexicalAndSyntacticFeatures(Configuration<DepTree> configuration, FeatureVector feats){
		//Buffer buffer = configuration.getFirstBuffer();
		Container synStack= configuration.getFirstStack();
		//Deque<Unit> synStack= configuration.getFirstStack();
		if(synStack.size() <= 2){
			return;
		}
		
		Unit s0u = synStack.pop();
		Unit s1u = synStack.peekFirst();
		synStack.push(s0u);
		addCombinedLexicalAndSyntacticFeatures("both:s0u", s0u, configuration, feats);
		addCombinedLexicalAndSyntacticFeatures("both:s1u", s1u, configuration, feats);
		addCombinedLexicalAndSyntacticPairFeatures("both:s0u_s1u",s0u,s1u,configuration,feats);
		//Unit s1u = FeatureUtils.getSecondElementInStack(stack);
		//Unit b0u = FeatureUtils.getFirstElementInBuffer(buffer);
		
	}
	
	
	@Override
	public FeatureVector perform(Configuration<DepTree> configuration, ExternalData data) {
		FeatureVector feats = new FeatureVector(fm);
		/*Deque<Unit> stack = configuration.getFirstStack();
		Buffer b = configuration.getFirstBuffer();
		Unit s0u = stack.peek();
		Unit s1u = DefaultFeatureExtractor.getSecondElementInStack(stack);
		Unit b0u = DefaultFeatureExtractor.getFirstElementInBuffer(b);
		feats.add("s0u_f="+s0u.getForm());
		feats.add("s1u_f="+s1u.getForm());
		feats.add("b0u_f="+b0u.getForm());*/
		//System.err.println("ICI");
		extract("syn",configuration, configuration.getFirstStack(),feats);
		extractLexicalFeatures(configuration, feats); // first option
		//extractCombinedLexicalAndSyntacticFeatures(configuration, feats); //second option
		
		//extract("stack2",configuration, configuration.getSecondStack(),feats);
		return feats;
		
	}
	

}
