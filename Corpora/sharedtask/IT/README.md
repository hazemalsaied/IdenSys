README
------
This is the README file for the Italian language.


Corpus
-------
All annotated data comes from the [PAISÀ corpus](http://www.corpusitaliano.it/en/) converted to CoNLL-U format (added two additional fields with underscores)
It is distributed under Creative Commons license, Attribution-ShareAlike and Attribution-Noncommercial-ShareAlike. 

The distribution of the subcorpora in our dataset is as follows:
 * `train`: 15721 sentences from `it_blog`, `it_wikinews` and `it_wikipedia`.
 * `test`: 1279 sentences from `it_blog` files.


Extra corpus data
-----------------
The train and test PARSEME-TSV file is perfectly aligned to a CoNLL-U file.

* Lemmas (CoNLL-U): Available (automatically annotated).
* POS-tags (CoNLL-U): Available (automatically annotated). The tagset is the [ISST-TANL Tagsets](http://www.corpusitaliano.it/static/documents/POS_ISST-TANL-tagset-web.pdf).
* Morphological features (CoNLL-U): Available (automatically annotated).
* Dependency relations (CoNLL-U):Available (automatically annotated). The inventory is [Universal Dependency Relations](https://web.archive.org/web/20130721035454/http://poesix1.ilc.cnr.it/ISST-TANL-DEPtagset-web.pdf).
* No-space information (PARSEME-TSV): Available (automatically annotated).


Tokenization
------------
* The tokenization follows the original tokenization of the PAISÀ corpus


Annotation
----------
VMWEs in this language are annotated for the following categories: LVC, ID, IReflV, VPC, OTH.


Licence
-------
The full dataset is licensed under **Creative Commons Non-Commercial Share-Alike 4.0** licence [CC-BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).

Authors
-------
Johanna Monti, Valeria Caruso, Maria Pia di Buono, Anna De Santis, Annalisa Raffone , Federico Sangati.

Contact
-------
`jmonti@unior.it` or `federico.sangati@gmail.com`
