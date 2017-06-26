/**
 * 
 */
package fr.upem.lgtools.process;

import java.io.BufferedWriter;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.UnsupportedEncodingException;

import fr.upem.lgtools.evaluation.SimpleEvaluation;
import fr.upem.lgtools.text.Sentence;
import fr.upem.lgtools.text.Utils;

/**
 * @author Mathieu Constant
 *
 */
public class TreebankIO {
	
	public static SentenceProcess saveInConll(final String filename){
		return new SentenceProcess() {
			private BufferedWriter out;
			
			
			@Override
			public Sentence apply(Sentence s, SimpleEvaluation eval) {
				try{
				   Utils.writeSentenceInConll(out, s);
				}
				catch(IOException e){
					throw new RuntimeException(e);
				}
				return s;
			}

			@Override
			public void initProcess() {
				
				try {
					out = Utils.openBufferedWriter(filename);
				} catch (UnsupportedEncodingException e) {
					throw new RuntimeException(e);
				} catch (FileNotFoundException e) {
					throw new RuntimeException(e);
				}
				
			}

			@Override
			public void endProcess() {
				try {
					out.close();
				} catch (IOException e) {
					throw new RuntimeException(e);
				}
			}
		};
	}
	
	
	
	
	public static SentenceProcess saveInXConll(final String filename){
		return new SentenceProcess() {
			private BufferedWriter out;
			
			
			@Override
			public Sentence apply(Sentence s, SimpleEvaluation eval) {
				try{
				   Utils.writeSentenceInXConll(out, s);
				}
				catch(IOException e){
					throw new RuntimeException(e);
				}
				return s;
			}

			@Override
			public void initProcess() {
				
				try {
					out = Utils.openBufferedWriter(filename);
				} catch (UnsupportedEncodingException e) {
					throw new RuntimeException(e);
				} catch (FileNotFoundException e) {
					throw new RuntimeException(e);
				}
				
			}

			@Override
			public void endProcess() {
				try {
					out.close();
				} catch (IOException e) {
					throw new RuntimeException(e);
				}
			}
		};
	}

}
