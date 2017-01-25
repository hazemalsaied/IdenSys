README
------
Welcome to the data repository of the [PARSEME Shared Task on Verbal Multi-Word Expressions Identification](http://typo.uni-konstanz.de/parseme/index.php/2-general/142-parseme-shared-task-on-automatic-detection-of-verbal-mwes).

This repository contains corpora in multiple languages.
Corpora are human-annotated with occurrences of Verbal Multiword Expressions (VMWEs).

You can download this repository as a [ZIP file](https://gitlab.com/parseme/sharedtask-data/repository/archive.zip?ref=master).


Corpora
-------
Human annotations can be found for multiple language directories,
such as `FR` for French, `DE` for German, `PL` for Polish, etc.
Inside each language directory, you may find these files:

* `README.md`: A description of the available data for that given language.
* ~~`trial.parsemetsv`: Trial file with an example of the final data (released mid-December/2016).~~[^1]
* `train.parsemetsv`: Training data (to be released early January/2017).
* `test.blind.parsemetsv`: The blind test data (to be released by the end of January/2017).
* `test.parsemetsv`: The gold test data (to be released after the shared task)
* `stats.md`: Number of sentences, tokens and annotated VMWEs in train/test.

The PARSEME-TSV files contain human annotation of VMWEs.
Depending on the language, these files may also be paired with a CoNLL-U file
for extra information (check the language-specific `README.md` files).

Note: For some languages, the UPOSTAG and DEPREL fields of their
CoNLL-U file may contain data that is not in the universal UD format. We thought it
would be useful to provide this information nevertheless.


Scripts
-------
The `bin` directory contains useful scripts.

* `bin/evaluate.py`: script for evaluating machine predictions against human annotations.
* `bin/checkParsemeTsvFormat.py`: script for checking if the prediction file is in the proper format.

--------------------------------

[^1]: Trial data was removed from the current release in order to avoid confusion.

