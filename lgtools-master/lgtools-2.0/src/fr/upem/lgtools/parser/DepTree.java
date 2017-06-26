package fr.upem.lgtools.parser;

import java.util.AbstractSet;
import java.util.Arrays;
import java.util.Collection;
import java.util.Collections;
import java.util.HashSet;
import java.util.Iterator;
import java.util.List;
import java.util.Set;

import fr.upem.lgtools.text.Unit;

public class DepTree implements Analysis{
	private Set<DepArc>[] nodeChildren;
	private DepArc[] reverse;
	private DepArc[] leftMostDependencies;
	private DepArc[] rightMostDependencies;
	private int[] links;
	private Set<Integer>[] reverseLinks;
	private Set<Unit> beingProcessed = new HashSet<Unit>();
	
	@SuppressWarnings("unchecked")
	public DepTree(int size){
		nodeChildren = (Set<DepArc>[])new Set<?>[size];
		reverseLinks = (Set<Integer>[])new Set<?>[size];
		reverse = new DepArc[size];
		leftMostDependencies = new DepArc[size];	
		rightMostDependencies = new DepArc[size];
		links = new int[size];
		//System.err.println("INIT: " +nodeCount);
	}
	
	public void addArc(DepArc a){
		
		int dep = a.getDep();
		int h = a.getHead();
		
		if(reverse[dep] != null){
			throw new IllegalStateException("Node "+dep+ " has already a parent");
		}
		
		if(nodeChildren[h] == null){
			nodeChildren[h] = new HashSet<DepArc>();
		}
		nodeChildren[h].add(a);
		reverse[dep] = a;
		if(h < a.getDep()){  //case of a right dependency
			if(rightMostDependencies[h] == null || rightMostDependencies[h].getDep() < dep){
				rightMostDependencies[h] = a;			
			}
		}
		else{ //case of a left dependency
			if(leftMostDependencies[h] == null || leftMostDependencies[h].getDep() > dep){
				leftMostDependencies[h] = a;			
			}
			
		}
	}
	
	public boolean nodeHasChildren(int i){
		return nodeChildren[i] == null?false:!nodeChildren[i].isEmpty();
	}
	
	
	public void addLinks(int node, int i){
		addLinks(node,i,-1);
	}
	
	
	public void addLinks(int node, int i, int j){
		if(node >= nodeChildren.length){
			nodeChildren = Arrays.copyOf(nodeChildren, nodeChildren.length *2);
			reverseLinks = Arrays.copyOf(reverseLinks, reverseLinks.length *2);
			reverse = Arrays.copyOf(reverse, reverse.length *2);
			leftMostDependencies = Arrays.copyOf(leftMostDependencies, leftMostDependencies.length *2);
			rightMostDependencies = Arrays.copyOf(rightMostDependencies, rightMostDependencies.length *2);
			links = Arrays.copyOf(links, links.length * 2);
		}
		links[i] = node;
		if(j!=-1){
		    links[j] = node;
		}
		Set<Integer> rlinks = reverseLinks[node];
		if(rlinks == null){
			rlinks = new HashSet<Integer>();
			reverseLinks[node] = rlinks;
		}
		rlinks.add(i);
		if(j != -1){
		   rlinks.add(j);
		}
		
	}
	
	public Collection<Integer> getReverseLinks(int node){
		return reverseLinks[node] == null?Collections.<Integer>emptySet():reverseLinks[node];
	}
	
	public int getFurtherLinkedNode(int node){
		int h = node;
		//System.err.println(h+"---"+links[h]);
		while(links[h] > 0){
			h = links[h];
			
		}
		//System.err.println("xxx:"+h);
		return h;
	}
	
	public DepArc[] getArcs(){
		return reverse;
	}
	
	@Override
	public Analysis copy(){
		DepTree tree = new DepTree(reverse.length);
		for(DepArc a:reverse){
			if(a != null){
			  tree.addArc(a);
			}
		}		
		return tree;
	}
	
	
	public DepArc[] getLeftMostDependencies() {
		return leftMostDependencies;
	}

	public DepArc[] getRightMostDependencies() {
		return rightMostDependencies;
	}

	
	public boolean hasIncomingArc(int node){
		return reverse[node] != null;
	}
	
	public int getHead(int node){
		if(reverse[node] == null){
			return -1;
		}
		return reverse[node].getHead();
	}

	public String getlabel(int node){
		if(reverse[node] == null){
			return null;
		}
		return reverse[node].getLabel();
	}
	
	public int getLexicalNodeId(int node){
		return links[node];
	}
	
	public boolean hasLexicalHead(int node){
		return links[node] > 0;
	}
	
	
	public Set<Integer> getChildren(final int node){
		if(node < 0 || node >= reverse.length){
			
			return Collections.emptySet();
		}
		return new AbstractSet<Integer>() {

			@Override
			public Iterator<Integer> iterator() {
				
				return new Iterator<Integer>() {
					private final Iterator<DepArc> it = nodeChildren[node] == null?Collections.<DepArc>emptySet().iterator():nodeChildren[node].iterator();

					
					
					@Override
					public boolean hasNext() {						
						return it.hasNext();
					}

					@Override
					public Integer next() {						
						return it.next().getDep();
					}

					@Override
					public void remove() {
						throw new IllegalStateException("Cannot remove dep arcs");
						
					}
					
					
				};
			}

			@Override
			public int size() {				
				return nodeChildren[node] == null?0:nodeChildren[node].size();
			}
		};
		
		
	}

	@Override
	public String toString() {		
		return Arrays.toString(reverse)+"\n"+Arrays.toString(links);
	}

	@Override
	public boolean isGold(List<Unit> units) {
		//System.err.println(units);
		for(DepArc a:reverse){
			if(a != null){
				int d = a.getDep();
				int h = a.getHead();
				String l = a.getLabel();
				Unit u = units.get(d - 1);
				
				if(u.getGoldSheadId() != h || !l.equals(u.getGoldSlabel())){
					return false;
				}				
			}
		}
		return true;
	}

	@Override
	public boolean isBeingProcessed(Unit unit) {
		return beingProcessed.contains(unit);
	}

	@Override
	public void setAsBeingProcessed(Unit unit) {
		beingProcessed.add(unit);
	}
	
	
}
