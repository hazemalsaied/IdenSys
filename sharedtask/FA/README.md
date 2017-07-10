README
------
This is the README file from the PARSEME verbal multiword expressions (VMWEs) corpus for Farsi (aka Persian).

Corpora
-------
All the annotated data come from a subset of the Farsi section of the MULTEXT-East "1984" annotated corpus 4.0 (for further information, see https://www.clarin.si/repository/xmlui/handle/11356/1043 ).

The present data extend and modify the previous corpora by:
* Adding the verbal multiword expression annotation layer, according to the PARSEME shared task [guidelines](http://parsemefr.lif.univ-mrs.fr/guidelines-hypertext/). 
* Where necessary, manually annotated part-of-speech tags in the original corpus are edited for further consistency with the PARSEME shared task guidelines; notably, all the verbs in VMWEs are annotated with tags started with `Vl'. These manually tagged morphosyntactic information are provided alongside the data (for further information about the tag-set see http://nl.ijs.si/ME/V4/msd/html/msd-fa.html).
* Transforming them into the [parseme-tsv](http://typo.uni-konstanz.de/parseme/index.php/2-general/184-parseme-shared-task-format-of-the-final-annotation) format (CoNLL-like)


Extra corpus data
-----------------
The train and test PARSEME-TSV files are aligned with the 10-column [CoNLL-U](http://universaldependencies.org/format.html) files. Here are some details on the latter file:

* ID (column 1): Word index, integer starting at 1 for each new sentence.
* FORM (column 2): Word form or punctuation symbol.
* LEMMA (column 3): Available. Gold annotations.
* UPOSTAG (column 4): Available. Automatically converted from the manually annotated MULTEXT tagset. The tagset is the [Universal POS-tags](http://universaldependencies.org/u/pos).
* XPOSTAG (column 5): Available. Gold morphosyntactic annotations originated from the MULTEXT-East "1984" annotated corpus 4.0 distribution. The format of these annotations is that are described in http://nl.ijs.si/ME/V4/msd/html/msd-fa.html.

Tokenization, Transliteration, and Encoding
------------
Manual tokenization is performed according to the guidelines set for the tokenization of the Farsi section of the MULTEXT-East "1984" [1], which implements recommendations by Iran's Academy of Farsi Language and Literature. Accordingly, where necessary, the zero-width non-joiner (ZWNJ) -- Unicode character 0x200C -- is used.

Short vowels are not transliterated in the corpus except for the ezafe markers at the end of words (i.e., Unicode character 0x0650).

The distributed trial/train/test data are encoded in UTF-8. 

Annotation
----------
VMWEs in this language have been annotated by a single annotator per file. For this release of the data, no categorization for the annotated VMWEs is provided.

Authors
----------
All VMWEs annotations were performed by Behrang Qasemizadeh.

License
----------
This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License (http://creativecommons.org/licenses/by-nc-sa/4.0/). 

The Farsi section of the MULTEXT-East "1984" annotated corpus 4.0, of which this data set is originated from, is published under MULTEXT-East licence: Freely available for non-commercial use with permission of Behrang QasemiZadeh, and provided that this Header is included in its entirety with any copy distributed.

Issues
----------
Despite our best efforts, you may find errors in the dataset. Please kindely report that to zadeh@phil.hhu.de. 

Contact
----------
zadeh@phil.hhu.de
agata.savary@univ-tours.fr

[1] Qasemizadeh and Rahimi. Persian in MULTEXT-East Framework. FinTAL 2006, DOI: 10.1007/11816508_54.
[2] Iran's Academy of Farsi Language and Literature. Official Farsi Orthography. ISBN: 964-7531-13-3, 3rd Edition, 2005. 
