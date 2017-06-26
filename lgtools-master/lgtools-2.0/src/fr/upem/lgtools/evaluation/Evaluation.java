package fr.upem.lgtools.evaluation;



public abstract class Evaluation {
  public abstract ParsingAccuracy getParsingAccuracy();
  public abstract Score getMweAccuracy();
  public abstract Score getFixedMweAccuracy();
  public abstract Score getSUAS();
  public abstract Score getSLAS();
  
  @Override
	public String toString() {
	   //String res = "EVALUATION:\n";
	   String res = "EVAL";
	   Score mwe = getMweAccuracy();
       res += mwe ==null?"":mwe.toString();
       mwe = getFixedMweAccuracy();
       res += mwe ==null?"":mwe.toString();
       Score sas = getSLAS();
       res += sas ==null?"":sas.toString();
       sas = getSUAS();
       res += sas ==null?"":sas.toString();
       ParsingAccuracy acc = getParsingAccuracy();
       res += acc==null?"":acc.toString();
		return res;
	}
}
