README
------
This is the README file for the Brazilian Portuguese language.

Corpora
-------
All annotated data come from one of these sources (subcorpora):
1. `DG`: 19,040 sentences from the Diário Gaúcho newspaper.
2. `UD`: 4,000 sentences from the training data of the Universal Dependencies v1.4 treebank for Brazilian Portuguese.

The distribution of the subcorpora in our dataset is as follows:
 * `train`: 17000 sentences from DG, followed by 2640 sentences from UD
 * `test`: 1240 sentences from DG, followd by 1360 sentences from UD

Extra corpus data
-----------------
The train and test PARSEME-TSV file is perfectly aligned to a CoNLL-U file.

* Lemmas (CoNLL-U): Available (automatically annotated).
* POS-tags (CoNLL-U): Available (automatically annotated for DG, manually annotated for UD). The tagset is [Universal POS-tags](http://universaldependencies.org/u/pos).
* Morphological features (CoNLL-U): Available (automatically annotated).
* Dependency relations (CoNLL-U): Available (automatically annotated for DG, manually annotated for UD). The inventory is [Universal Dependency Relations](http://universaldependencies.org/u/dep).
* No-space information (PARSEME-TSV): Available (automatically annotated) for DG. Not available for UD.

Automatic annotation was performed by [UDPipe](https://ufal.mff.cuni.cz/udpipe) using in-house models trained on UD 1.4 corpora.

Tokenization
------------
* Hyphens: Not reliably tokenized in DG. Always split as a single token in UD.
* Contractions: Most contractions are kept as a single unit (not-split).  In the DG corpus, _ao_ is split as two tokens _a_ and _o_.

Known issues
------------
* Single-token `IReflV`s: The hyphenization inconsistency between DG and UD is relevant for reflexive verbs with proclisis, where the clitic appears after the verb with a hyphen (e.g. _queixar-se_ lit. _complain-self_ 'to complain'). They do not have the same tokenization in both subcorpora. For example, _queixar-se_ is a single token annotated as `IReflV` in DG, whereas it consists of three tokens _queixar - se_ in UD. In the latter case, the hyphen is **not** annotated as part of the `IReflV`. We intend to fix it in future versions.
* Lemmas: The quality of the automatic lemmatizer is limited because it was learned on a small European Portuguese corpus (UD-Portuguese) which does not use exactly the same tokenization as our corpora.
* Merging "ea" and "eo": The UD corpus strangely merges "e"+"a" and "e"+"o" at some places.  We have left the surface untouched (as "ea" and "eo"), to be able to keep the same tokenization as in the original corpus. These tokens contain "e+o" as lemma.

Annotation
----------
VMWEs in this language have been annotated by a single annotator per file. The following [categories](http://parsemefr.lif.univ-mrs.fr/guidelines-hypertext/?page=030_Categories_of_VMWEs) are used: ID, LVC, IReflV, OTH.

Licence
-------
The full dataset is licensed under **Creative Commons Non-Commercial Share-Alike 4.0** licence [CC-BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)

Authors
-------
Helena Caseli, Silvio Cordeiro, Carlos Ramisch, Renata Ramisch, Aline Villavicencio, Leonardo Zilio.

Contact
-------
{carlos.ramisch,silvio.cordeiro}@lif.univ-mrs.fr

