README
------
This is the README file for the Slovenian language.


Corpora
-------
All annotated data come from ssj500k training corpus, which is available and described here:
* CLARIN.SI repository: http://hdl.handle.net/11356/1052
* Description: http://eng.slovenscina.eu/tehnologije/ucni-korpus

The present data extend and modify the previous corpora by:
* adding the verbal multiword expression annotation layer, according to the PARSEME shared task [guidelines](http://parsemefr.lif.univ-mrs.fr/guidelines-hypertext/).
* transforming them into the [parseme-tsv](http://typo.uni-konstanz.de/parseme/index.php/2-general/184-parseme-shared-task-format-of-the-final-annotation) format (CoNLL-like)
* adding the automatically generated layer of syntactic dependencies (see below for details)


Extra corpus data
-----------------
The train and test PARSEME-TSV file is aligned with the 10-column CoNLL-U file. Here are some details on the latter file:

* LEMMA (column 3): Available (manually annotated).
* POS-tag (column 4): Available (manually annotated). The tagset is [JOS](http://nl.ijs.si/jos/josMSD-en.html).
* (column 5): NOT available (Morphological features are encoded in the tag after the first letter representing POS).
* (column 6): NOT available (Morphological features are encoded in the tag after the first letter representing POS).
* HEAD (column 7): Head of dependency relations available (manually annotated). The system is described in [JOS/SSJ](http://eng.slovenscina.eu/tehnologije/razclenjevalnik).
* DEPREL (column 8): Dependecy relations available (manually annotated). The inventory is described in [JOS/SSJ](http://eng.slovenscina.eu/tehnologije/razclenjevalnik).
* DEPS (column 9): Not available.
* MISC (column 10): No-space information NOT available (included in the tsv file). 


Tokenization
------------
* Language-specific tokenization rules are applied. Tokenization is manually checked in the corpus.


Annotation
----------
Sentences from 1 to 8641 have been annotated by two annotators per file. Sentences from 8642 to 11411 have been annotated by one annotator per file. VMWEs in this language are annotated for the following categories: ID, LVC, VPC, IReflV, OTH.


Authors
----------
All VMWEs annotations were performed by Polona Gantar, Taja Kuzman and Simon Krek.


License
----------
The data are distributed under the terms of the [Creative Commons BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).


Contact
----------
simon.krek@ijs.si
