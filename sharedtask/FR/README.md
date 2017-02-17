README
------
This is the README file for the French language.


Corpora
-------
The verbal MWEs have been annotated:
1. `sequoia`: The Sequoia Treebank
2. `ud_1_4`: The Universal Dependencies 1.4 treebank for French


Extra corpus data
-----------------
The train and test PARSEME-TSV file is perfectly aligned to a CoNLL-U file. 

* Lemmas (CoNLL-U): Available
* POS-tags (CoNLL-U): Available (manually annotated). The tagset for UD is [Universal POS-tags](http://universaldependencies.org/u/pos). The tagset for the Sequoia treebank is described in the [Sequoia documentation](http://passage.inria.fr/deepwiki/node/594#Categories_morpho-syntaxiques) (in French).
* Morphological features (CoNLL-U): Available
* Dependency relations (CoNLL-U): Available (manually annotated). The inventory is [Universal Dependency Relations](http://universaldependencies.org/u/dep) for UD, and [Sequoia surface dependencies](http://passage.inria.fr/deepwiki/node/594#Fonctions_grammaticales) for the Sequoia treebank. 
* No-space information (PARSEME-TSV): Available for both sources (automatically annotated).


Tokenization
------------
* sequoia corpus: the original tokenization of the sequoia corpus has been converted into that of the UD 1.4 French data.

So for both sources we have the UD 1.4 tokenization, in which the following contractions appear as multi-word tokens (e.g. 1-2 au), split into words:
E.g. : Au soleil
```
1-2 Au
1 à
2 le
3 soleil
```

The list of contractions is:
```
au
auquel
aux
auxquelles
auxquels
des
desquelles
du
duquel
```

Note that the only ambiguous case are "des" / "du". Depending on the context, these tokens are either a plain determiner, or are split into preposition "de" + determiner "le" / "les".

Annotation
----------
VMWEs in this language are annotated for the following categories: ID, LVC, IReflV, OTH.

Authors
----------
The VMWEs annotations were performed by Marie Candito, Mathieu Constant, Caroline Pasquer, Yannick Parmentier, Carlos Ramisch, Jean-Yves Antoine.

Licence
----------
The VMEs annotations are distributed under the terms of the [CC-BY v4 license](https://creativecommons.org/licenses/by/4.0/). As far as the CONLL-U files are concerned, the UD part of the corpus is under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) and the Sequoia part is under [LGPL-LR](http://infolingu.univ-mlv.fr/DonneesLinguistiques/Lexiques-Grammaires/lgpllr.html). UD sentences can be identified by their `sentid` prefixed with `fr-ud`.
 
Contact
----------
`marie.candito@gmail.com`

