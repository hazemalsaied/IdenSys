# lgtools

To cite this tool, please use the following reference:

Matthieu Constant and Joakim Nivre. 2016. A Transition-based System for Joint Lexical and Syntactic Analysis. *54th Annual Meeting of the Association for Computational Linguistics (ACL'16)*


## How to use the tool

You first need to download the JSAP-2.1 library.

For both training and parsing, the tool requires a conll file as input.
It is necessary to have the 7th and 9th columns (HEAD) identical and 8th and 10th columns (LABEL) identical as well.


### Training  a model

java -Xmx8g -cp lgtools.jar:JSAP-2.1.jar fr/upem/lgtools/parser/Parser -m _model_ -t _train-dataset_ -p

- _model_ is the path of the model you want to build
- _train-dataset_ is the path of the training dataset in the conll format
- "-p" idenicates that we apply projective parsing algorithm

### Parsing a text

java -Xmx8g -cp lgtools.jar:JSAP-2.1.jar fr/upem/lgtools/parser/Parser -m _model_ -i _test-dataset_ -o _output_

- _model_ is the path of the model to be applied
- _test-dataset_ is the path of the input dataset to be tested
- _output_ is the path of the output (parsed text)


The tool also prints out evaluation score on the test data set:


EVAL Fscore(MWE) Fscore(Fixed_MWE) Nan Nan UAS LAS


