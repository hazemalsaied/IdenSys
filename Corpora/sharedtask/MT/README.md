README
------
This is the README file for the Maltese language.


Corpora
-------
All annotated data come from Korpus Malti version 3 (news section). More info can be found [here](http://mlrs.research.um.edu.mt/).


Extra corpus data
-----------------
* Trial data: the PARSEME-TSV contains no extra corpus data.

* Training and testing data:
  * Lemmas/semitic roots (CoNLL-U): Available (automatically annotated; no full coverage; where a lemma is not found, the word form is reproduced).
  * POS-tags (CoNLL-U): Available (automatically annotated). The tagset is defined [here](http://mlrs.research.um.edu.mt/resources/malti03/tagset30.html).
  * Morphological features (CoNLL-U): Not available.
  * No-space information (PARSEME-TSV): Available (automatically annotated).


Tokenization
------------
* Definite articles and prepositions: The definite article, which is a clitic, is tokenised into a separate token. This is usually separated by a hyphen from its host word (il- ħin is tokenised as "il-" and "ħin"). This is also true of prepositions, when they are definite (mill-ħin = "mill-" + "ħin"). Note, however, that we represent the preposition-article as one token, and the host word as another  (so even though "mill-" = "minn + il-", these are not separated).


Annotation
----------
VMWEs in this language are annotated for the following categories: ID, LVC, OTH.


Authors
-------
The VMWEs annotations were performed by (in alphabetical order) Greta Attard, Kirsty Azzopardi, Janice Bonnici, Jael Busuttil, Alison Farrugia, Luke Galea, Sara Anne Galea, Anabelle Gatt, Amanda Muscat, Nicole Tabone, and Marc Tanti.


License
-------
The data are distributed under the terms of the Creative Commons license [CC-BY v4](https://creativecommons.org/licenses/by/4.0/).


Contact
-------
lonneke.vanderplas@um.edu.mt
