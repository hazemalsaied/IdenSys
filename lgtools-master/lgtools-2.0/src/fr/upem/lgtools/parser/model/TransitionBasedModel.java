package fr.upem.lgtools.parser.model;
import java.io.BufferedInputStream;
import java.io.BufferedOutputStream;
import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.util.Collection;
import java.util.HashSet;
import java.util.Set;
import java.util.zip.GZIPInputStream;
import java.util.zip.GZIPOutputStream;

import fr.upem.lgtools.parser.Analysis;
import fr.upem.lgtools.parser.Configuration;
import fr.upem.lgtools.parser.ExternalData;
import fr.upem.lgtools.parser.TransitionSet;
import fr.upem.lgtools.parser.features.FeatureExtractor;
import fr.upem.lgtools.parser.features.FeatureMapping;
import fr.upem.lgtools.parser.features.FeatureVector;
import fr.upem.lgtools.parser.transitions.Transition;
import fr.upem.lgtools.parser.transitions.Transitions;
import fr.upem.lgtools.text.DepTreebank;
import fr.upem.lgtools.text.Sentence;
import fr.upem.lgtools.text.Unit;

/**
 * 
 */

/**
 * @author Matthieu Constant
 *
 */
public abstract class TransitionBasedModel<T extends Analysis> {
	protected final FeatureMapping features;
	private Model model;
	protected final TransitionSet<T> transitions = new TransitionSet<T>();
	private final FeatureExtractor<T> extractor;
	private boolean isProjective;
	
	
	
	
	
	public boolean isProjective(){
		//System.err.println("PROJ="+this.isProjective);
		return this.isProjective;
	}
	
	
	// constructor used before training
	public TransitionBasedModel(FeatureMapping fm,DepTreebank tb,boolean isProjective){
		this.isProjective = isProjective;
		createTransitions(tb);
		extractor = getFeatureExtractor(fm);
		features = fm;
		//System.err.println(features.featureCapacity()+"---"+transitions.size());
		model = new Model(features.featureCapacity(),transitions.size());		
	}
	
	
	
	
	// constructor used before parsing
	public TransitionBasedModel(String filename) throws IOException{
		GZIPInputStream gin = new GZIPInputStream(new BufferedInputStream(new FileInputStream(filename)));
		DataInputStream in = new DataInputStream(gin);
		int nFeatCapacity = in.readInt();
		int nLabels = in.readInt();

		//System.err.println(nFeatCapacity);
		//System.err.println(nLabels);
		//System.err.println(nFeats);
		this.features = FeatureMapping.createFeatureMapping(in.readInt(),nFeatCapacity);
		this.features.read(in);
		
			
		for(int l = 0 ; l < nLabels ; l++){
			String id = in.readUTF();
			//System.err.println(id);
		   this.transitions.add(createTransition(Transitions.getType(id),Transitions.getLabel(id)));
		}
		
		this.model = new Model(nFeatCapacity,nLabels);
		int n = model.getFeatureCount() * model.getLabelCount();
		int i = 0;
		while(i < n){
			int nZeros = in.readInt(); 
			i+=nZeros;
			//System.err.println(nZeros+" "+i+" "+n);
			if(i < n){
				model.set(i,in.readDouble());
			}
			i++;
			
		}
		in.close();
			
			
			extractor = getFeatureExtractor(features);
			//System.err.println(features.featureCapacity()+"---"+transitions.size());
	}
	

	public void setModel(Model newModel){
		//model.setModel(newModel);
		this.model = newModel;
	}
	
	public Model getAveragedModel(Model averaged, int cnt){
		return model.getAveragedModel(averaged,cnt);
	}
	
	
	
	public Model getModel(){
		return model;
	}
	
	
	public int getFeatureCount(){
		return model.getFeatureCount();
	}
	
	public int getLabelCount(){
		return model.getLabelCount();
	}
	
	
	
	public TransitionSet<T> getTransitions(){
		return transitions;
	}
	
		
    public FeatureMapping getFeatures() {
		return features;
	}

	public void save(String filename) throws IOException{
		
		GZIPOutputStream gout = new GZIPOutputStream(new BufferedOutputStream(new FileOutputStream(filename))); 
		DataOutputStream out = new DataOutputStream(gout);
		
		out.writeInt(model.getFeatureCount());
		out.writeInt(model.getLabelCount());
		features.write(out);
		
		
		for(int l = 0 ; l < model.getLabelCount() ; l++){
			out.writeUTF(transitions.getTransition(l).id());
		}
		int n = model.getFeatureCount()*model.getLabelCount();
		int i = 0;
		while(i < n){
			int tmp = Model.nextNonZero(i, model);
			out.writeInt(tmp-i);
			if(tmp<n){
			  out.writeDouble(model.getWeight(tmp));
			}
			i = tmp + 1;
		}
		out.close();
	}
	
	
	//external abstract methods
	abstract public Configuration<T> getInitialConfiguration(Sentence s,boolean needsGold);
	
	abstract public Transition<T> staticOracle(Configuration<T> configuration);
	abstract public DepTreebank filter(DepTreebank tb); //used to filter gold treebank for training, with respect to system constraints
	abstract public void updateSentenceAfterAnalysis(Sentence s,T analysis);
	
	//internal abstract methods
	abstract protected FeatureExtractor<T> getFeatureExtractor(FeatureMapping fm);
	abstract protected Transition<T> createLabelDependentTransition(Unit unit,Sentence s);	
	abstract protected Transition<T> createTransition(String type, String label);	
	abstract protected Collection<Transition<T>> createLabelIndependentTransitions();	
	
	
	public double getActivatedFeatureRatio(){
		return model.getActivatedFeatureCount()/(double)model.getFeatureCount();
	}
	
	
	
		
	private void createTransitions(DepTreebank tb){	
		for(Transition<T> t:createLabelIndependentTransitions()){
			addTransition(t);
		}
		for(Sentence s:tb){
		for(Unit u:s.getUnits()){
				  Transition<T> t = createLabelDependentTransition(u,s);
				  if(t != null){
				     addTransition(t);
				  }
			}
		}
	}
	
	
	private void addTransition(Transition<T> transition){
		if(transition == null){
			return;
		}
		if(!transitions.contains(transition)){
			transitions.add(transition);	
		}
		
	}
	
	
	public FeatureVector extractFeatures(Configuration<T> configuration,ExternalData data){
		return extractor.perform(configuration,data);
	}

	
	public Set<Transition<T>> getValidTransitions(Configuration<T> config){
		Set<Transition<T>> set = new HashSet<Transition<T>>();
		for(Transition<T> t:transitions){
			if(t.isValid(config)){
				set.add(t);
			}
		}
		return set;
	}
	
	
	public Set<Transition<T>> getCorrectTransitions(Configuration<T> config){
		Set<Transition<T>> set = new HashSet<Transition<T>>();
		set.add(staticOracle(config));
		return set;
	}
	
	
	
	
	public Transition<T> getBestValidTransition(FeatureVector fv,Configuration<T> c){		
		return getBestTransition(fv, getValidTransitions(c));
	}
	
	public Transition<T> getBestCorrectTransition(FeatureVector fv, Configuration<T> c){
		return getBestTransition(fv,getCorrectTransitions(c));
	}
	
	
	
	public double getScore(FeatureVector feats, Transition<T> transition){
		int l = transitions.getTransitionIndex(transition);
		return model.score(feats,l);
	}
	
	
	
	private Transition<T> getBestTransition(FeatureVector feats, Set<Transition<T>> possibleTransitions){
		double bestSc = -Double.MAX_VALUE;
		Transition<T> bestTransition = null;
		for(int l = 0 ; l < transitions.size(); l++){
			Transition<T> t = transitions.getTransition(l);
			if(possibleTransitions.contains(t)){ 
			  
			  double sc = model.score(feats,l);
			  //System.err.println(sc+"-->"+t);
			  if(sc > bestSc){
				bestSc = sc;
				bestTransition = t;
			  }
			  //System.out.println(bestLabel);
			}
		}
		//System.err.println("BEST:"+bestTransition);
		return bestTransition;
		
		
	}
		
	
	
	public void update(FeatureVector feats, Transition<T> ot, Transition<T> pt){
		//System.err.println(ot+" "+pt);
		model.updatePlus(feats, transitions.getTransitionIndex(ot));
		model.updateMinus(feats, transitions.getTransitionIndex(pt));		
	}
	
	public void update(FeatureVector feats, Transition<T> ot, Transition<T> pt,Model averaged,double coef){
		update(feats, ot,pt);
	
		averaged.updatePlus(feats, transitions.getTransitionIndex(ot),coef);
		averaged.updateMinus(feats, transitions.getTransitionIndex(pt),coef);	
		
	}
	
	
	
	
	@Override
	public String toString() {		
		//return transitions.toString()+"\n"+features.toString()+"\n"+model.toString();
		return transitions.toString();
	}
	
}
