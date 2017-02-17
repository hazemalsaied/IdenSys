README
------
This is the README file for the Czech language.

Corpora
-------
All annotated data come from one of these newspapers:
1. Lidové noviny (daily newspapers), 1991, 1994, 1995
2. Mladá fronta Dnes (daily newspapers), 1992
3. Českomoravský Profit (business weekly), 1994
4. Vesmír (scientific journal), 1992, 1993


Extra corpus data
-----------------
The train and test PARSEME-TSV file is perfectly aligned to a CoNLL-U file.

* Lemmas (CoNLL-U): Available (manually checked).
* POS-tags (CoNLL-U): Available (automatically annotated and mainly manually checked). The tagset is [Universal POS tag](http://universaldependencies.org/u/pos/index.html) in 4th column and [POS](https://ufal.mff.cuni.cz/pdt/Morphology_and_Tagging/Doc/hmptagqr.html#POS) and [SUBPOS](https://ufal.mff.cuni.cz/pdt/Morphology_and_Tagging/Doc/hmptagqr.html#SUBPOS) position in Prague positional tagset in 5th column.
* Morphological features (CoNLL-U): Available (automatically annotated, usually manually checked).
* Dependency relations (CoNLL-U): Not available.
* No-space information (PARSEME-TSV): Available (manually annotated).


Tokenization
------------
* Hyphens: Always split as a single token, resulting in three tokens out of "chceme-li".

* Contractions: Most contractions are kept as a single unit (not-split).


Annotation
----------
VMWEs in this language are annotated for the following categories: ID, LVC, IReflV, OTH.

Authors
----------
All VMWEs annotations were performed by Alla Bémová, Eva Buráňová,
Jakub Dotlačil, Milena Hnátková, Natalia Klyueva, Marie Mikulová,
Kateřina Součková, Magda Ševčíková, Pavel Šidák, Jana Šindlerová,
Eva Šťastná, Zdeňka Urešová, Pavlína Vimmrová, Eduard Bejček,
Petr Pajas, and Pavel Straňák.

License
----------
The data are distributed under the terms of the Creative Commons license
([CC-BY-NC-SA](http://creativecommons.org/licenses/by-nc-sa/3.0/)).

Contact
----------
bejcek@ufal.mff.cuni.cz
