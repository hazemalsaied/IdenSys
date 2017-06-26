/**
 * 
 */
package fr.upem.lgtools.parser;

import com.martiansoftware.jsap.FlaggedOption;
import com.martiansoftware.jsap.JSAP;
import com.martiansoftware.jsap.JSAPException;
import com.martiansoftware.jsap.JSAPResult;
import com.martiansoftware.jsap.Switch;

/**
 * @author Mathieu Constant
 *
 */
public class Parameters {
	private static final String MODEL_OPT = "model";
	private static final String PROJECTIVE_OPT = "projective";
	private static final String TRAINSIZE_OPT = "size";
	private static final String TRAIN_OPT = "train";
	private static final String INPUT_OPT = "input";
	private static final String OUTPUT_OPT = "output";
	private static final String ITER_OPT = "iters";
	private static final String MODEL_SIZE_OPT = "msize";
	private static final String REPEAT_OPT = "repeat";
	private static final String RIGHT_MERGE_STRATEGY = "right";
	private static final String IMPLICIT_COMPLETE_STRATEGY = "implicit";
	private static final String CONSTRAINED_MERGE_STRATEGY = "constrained";
	private static final String FIXED_MWE_ONLY = "fixed_only";
	private static final String NO_SYNTACTIC_ANALYSIS = "nosyntax";
	private static final String BASELINE = "baseline";
	private static final String XCONLL_INPUT = "xconll";
	
	private static final String EXTERNAL_OPT = "external";
	
	public int iters;
	public int modelSize;
	public int trainSize;
	public int repeats;
	public String output;
	public String input;
	public String model;
	public String train;
	public boolean rightMerge;
	public boolean implicitComplete;
	public boolean constrainedMerge;
	public boolean fixedMweOnly;
	public boolean noSyntax;
	public boolean baseline;
	public boolean projective;
	public boolean xconll;
	public String external;
	
	
	
	
	public Parameters(String[] args) throws JSAPException {
		JSAP jsap = createJSAP();
		JSAPResult config = jsap.parse(args);
		if(!config.success()){
			exit(jsap);
		}
		
		input = config.getString(INPUT_OPT);
		output = config.getString(OUTPUT_OPT);
		model = config.getString(MODEL_OPT);
		train = config.getString(TRAIN_OPT);
		external = config.getString(EXTERNAL_OPT);
		trainSize = config.getInt(TRAINSIZE_OPT);
		iters = config.getInt(ITER_OPT);
		modelSize = config.getInt(MODEL_SIZE_OPT);
		repeats = config.getInt(REPEAT_OPT);
		rightMerge = config.getBoolean(RIGHT_MERGE_STRATEGY);
		implicitComplete = config.getBoolean(IMPLICIT_COMPLETE_STRATEGY);
		constrainedMerge = config.getBoolean(CONSTRAINED_MERGE_STRATEGY);
		fixedMweOnly = config.getBoolean(FIXED_MWE_ONLY);
		noSyntax = config.getBoolean(NO_SYNTACTIC_ANALYSIS);
		baseline = config.getBoolean(BASELINE);
		projective = config.getBoolean(PROJECTIVE_OPT);
		xconll = config.getBoolean(XCONLL_INPUT);
		
		if(!rightMerge && constrainedMerge){
			throw new IllegalStateException("The constrained merge strategy can only be applied with a right merge strategy!!");
		}
		if(iters <= 0){
			throw new IllegalStateException("number of training iterations should be positive");
		}
		if(modelSize <= 0){
			throw new IllegalStateException("number of feature identifiers should be positive");
		}
		
		if(repeats <= 0){
			throw new IllegalStateException("number of repeats should be positive");
		}
		
	}
	
	private static JSAP createJSAP() throws JSAPException{
		JSAP jsap = new JSAP();

		FlaggedOption opt;
		Switch sw;
		
		sw = new Switch(RIGHT_MERGE_STRATEGY)
		.setLongFlag(RIGHT_MERGE_STRATEGY)
		.setShortFlag('R');
		sw.setHelp("set right merge strategy (default: left merge strategy)");
		jsap.registerParameter(sw);
		
		sw = new Switch(IMPLICIT_COMPLETE_STRATEGY)
		.setLongFlag(IMPLICIT_COMPLETE_STRATEGY)
		.setShortFlag('I');
		sw.setHelp("set implicit complete strategy (default: explicit complete)");
		jsap.registerParameter(sw);
		
		sw = new Switch(CONSTRAINED_MERGE_STRATEGY)
		.setLongFlag(CONSTRAINED_MERGE_STRATEGY)
		.setShortFlag('C');
		sw.setHelp("set constrained merge strategy which implies right merge strategy (default: non constraint on merge)");
		jsap.registerParameter(sw);
		
		sw = new Switch(BASELINE)
		.setLongFlag(BASELINE)
		.setShortFlag('B');
		sw.setHelp("apply baseline with arc labels specific to MWEs  (default: apply new system with merge transitions)");
		jsap.registerParameter(sw);
		
		sw = new Switch(FIXED_MWE_ONLY)
		.setLongFlag(FIXED_MWE_ONLY)
		.setShortFlag('F');
		sw.setHelp("identify fixed MWE only (default: identify all MWEs)");
		jsap.registerParameter(sw);
		
		sw = new Switch(NO_SYNTACTIC_ANALYSIS)
		.setLongFlag(NO_SYNTACTIC_ANALYSIS)
		.setShortFlag(JSAP.NO_SHORTFLAG);
		sw.setHelp("No syntactic analysis is performed (default: syntactic analysis is performed)");
		jsap.registerParameter(sw);
		
		sw = new Switch(XCONLL_INPUT)
				.setLongFlag(XCONLL_INPUT)
				.setShortFlag('X');
				sw.setHelp("input text in xconll format");
				jsap.registerParameter(sw);
		
		sw = new Switch(PROJECTIVE_OPT)
				.setLongFlag(PROJECTIVE_OPT)
				.setShortFlag('p');
				sw.setHelp("perform projective training");
				jsap.registerParameter(sw);
		
		opt = new FlaggedOption(MODEL_OPT)
		.setStringParser(JSAP.STRING_PARSER)
		.setRequired(true)
		.setShortFlag('m')
		.setLongFlag(MODEL_OPT);
		opt.setHelp("Path of the model (without extension)");
		jsap.registerParameter(opt);

		opt = new FlaggedOption(TRAIN_OPT)
		.setStringParser(JSAP.STRING_PARSER)
		.setRequired(false)
		.setShortFlag('t')
		.setLongFlag(TRAIN_OPT);
		opt.setHelp("Path of training treebank (conll format)");
		jsap.registerParameter(opt);
		
		opt = new FlaggedOption(TRAINSIZE_OPT)
				.setStringParser(JSAP.INTEGER_PARSER)
				.setRequired(false)
				.setDefault("-1")
				.setShortFlag('s')
				.setLongFlag(TRAINSIZE_OPT);
				opt.setHelp("Size of training dataset: default, all dataset.");
				jsap.registerParameter(opt);
		
		opt = new FlaggedOption(INPUT_OPT)
		.setStringParser(JSAP.STRING_PARSER)
		.setRequired(false)
		.setShortFlag('i')
		.setLongFlag(INPUT_OPT);
		opt.setHelp("Path of input text (conll format)");
		jsap.registerParameter(opt);
		
		opt = new FlaggedOption(OUTPUT_OPT)
		.setStringParser(JSAP.STRING_PARSER)
		.setRequired(false)
		.setShortFlag('o')
		.setLongFlag(OUTPUT_OPT);
		opt.setHelp("Path of output text (xconll format)");
		jsap.registerParameter(opt);
		
		opt = new FlaggedOption(ITER_OPT)
		.setStringParser(JSAP.INTEGER_PARSER)
		.setRequired(false)
		.setShortFlag(JSAP.NO_SHORTFLAG)
		.setLongFlag(ITER_OPT);
		opt.setDefault("6");
		opt.setHelp("number of training iterations (default: 6)");
		jsap.registerParameter(opt);
		
		opt = new FlaggedOption(MODEL_SIZE_OPT)
		.setStringParser(JSAP.INTEGER_PARSER)
		.setRequired(false)
		.setShortFlag(JSAP.NO_SHORTFLAG)
		.setLongFlag(MODEL_SIZE_OPT);
		opt.setDefault("1000000");
		opt.setHelp("size of model: max. number of feature identifiers (default: 1000000)");
		jsap.registerParameter(opt);
		
		opt = new FlaggedOption(REPEAT_OPT)
		.setStringParser(JSAP.INTEGER_PARSER)
		.setRequired(false)
		.setShortFlag(JSAP.NO_SHORTFLAG)
		.setLongFlag(REPEAT_OPT);
		opt.setDefault("1");
		opt.setHelp("Number of times experiment is repeated (default: 1)");
		jsap.registerParameter(opt);
		
		opt = new FlaggedOption(EXTERNAL_OPT)
				.setStringParser(JSAP.STRING_PARSER)
				.setRequired(false)
				.setLongFlag(EXTERNAL_OPT);
				opt.setHelp("Path of external resource file");
				jsap.registerParameter(opt);
		
		
		
		return jsap;
	}
	
	private static void exit(JSAP jsap){
		System.err.print("Usage: ");
		System.err.print("java "+Parser.class.getCanonicalName()+" ");
		System.err.println(jsap.getUsage());
		System.err.print(jsap.getHelp());
		System.exit(1);
	}
	
}
