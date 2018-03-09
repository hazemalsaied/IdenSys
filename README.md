A simple transition-based system for the identification of the verbal multword expressions. 
 
This system has participated in the competition of MWE Shared task - EACL 2017 (Valencia, Spain).

**Corpora**: Data sets proposed by MWE Shared task - EACL 2017 (Valencia, Spain).

**Results**: results of experiments on 18 languages with multiple reports reflecting the progress of the identification process.

**SourceCode**: The folder Src


Overview of the source code:

The identifier runs using identify function (identifier.py).
The input of the system is a set of configurations:
1- the language you want to test and its feature group (This should be represented as a json file in "Experiments/xp").
N.B. configuration files with our preferred feature group are available in 'Experiments/Langs'.

2- The mode of evaluation:

A- Debug mode: used during development for faster execution time;
B- Test Mode: using the full version of Shared task train and test data sets;
C- Cross validation mode: A 5-fold cross validation evaluation over the  Shared task train data (No shuffle used).

The actual version is very light (No reports, no analysis and no code for additional experiments).

A good start to understand the code is to start with the identifier script and to follow the code.

**N.B:**The folder script contain multiple secondary scripts used for
1- **baseline.py**: creating a baseline system for identifying Sharedtask MWE using string matching techniques
2- **marmot.py** and **mateParsing.py** which were used to generate the automatic annotation (POS tags and syntaxic annotations) for languages whose annotations where manulally annotated (FR, CS, HU, and PL).



*Citation:*

Al Saied, H., Constant, M., & Candito, M. (2017). The atilf-llf system for parseme shared task: a transition-based verbal multiword expression tagger. In Proceedings of the 13th Workshop on Multiword Expressions (MWE 2017) (pp. 127-132).




