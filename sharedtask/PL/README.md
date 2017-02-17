README
------
This is the README file from the PARSEME verbal multiword expressions (VMWEs) corpus for Polish.

Corpora
-------
All the annotated data come from one of these sources:
1. `PCC`: [Polish Coreference Corpus](http://zil.ipipan.waw.pl/PolishCoreferenceCorpus), the 21 "long" texts from this corpus are included, 36,000 tokens, Rzeczpospolita newspaper.
2. `NKJP`: [National Corpus of Polish](http://clip.ipipan.waw.pl/NationalCorpusOfPolish), all texts from daily newspapers are included, i.e. those whose identifiers start with 130-2, 130-3 or 130-5.

The present data extend and modify the previous corpora by:
* adding the verbal multiword expression annotation layer, according to the PARSEME shared task [guidelines](http://parsemefr.lif.univ-mrs.fr/guidelines-hypertext/).
* transforming them into the [parseme-tsv](http://typo.uni-konstanz.de/parseme/index.php/2-general/184-parseme-shared-task-format-of-the-final-annotation) format (CoNLL-like)
* adding the automatically generated layer of syntactic dependencies (see below for details)

Extra corpus data
-----------------
The train and test PARSEME-TSV file is aligned with the 10-column [CoNLL-U](http://universaldependencies.org/format.html) file. Here are some details on the latter file:

* LEMMA (column 3): Available. Manually double-annotated and adjudicated for the NKJP files, automatically annotated for the PCC files.
* UPOSTAG (column 4): Available. Automatically converted from the manually annotated NKJP tagset, with the [Polish UD conversion table](http://universaldependencies.org/docs/tagset-conversion/pl-ipipan-uposf.html). The tagset is the [Universal POS-tags](http://universaldependencies.org/u/pos).
* XPOSTAG (column 5): Available. Manually double-annotated and adjudicated for the NKJP files, automatically annotated for the PCC files. The [NKJP tagset](http://nkjp.pl/poliqarp/help/ense2.html) is used .
* FEATS (column 6): Available. Automatically converted from the from the manually annotated NKJP tagset, with the [Polish UD conversion table](http://universaldependencies.org/docs/tagset-conversion/pl-ipipan-uposf.html) extended with some missing categories and feature combinations. The UD tagset is used [Universal features](http://universaldependencies.org/u/feat/index.html)
* HEAD (column 7): Available. Automatically annotated by [UDPipe](https://ufal.mff.cuni.cz/udpipe) with the Polish [model version 1.2-160523](https://lindat.mff.cuni.cz/repository/xmlui/handle/11234/1-1659). 
* DEPREL (column 8): Available. Automatically annotated by [UDPipe](https://ufal.mff.cuni.cz/udpipe) with the Polish [model version 1.2-160523](https://lindat.mff.cuni.cz/repository/xmlui/handle/11234/1-1659). The tagset is [Universal Dependency Relations](http://universaldependencies.org/u/dep).
* DEPS (column 9): Not available.
* MISC (column 10): No-space information available. Manually double-annotated and adjudicated for the NKJP files, automatically annotated for the PCC files.

Tokenization
------------
Manually double-annotated and adjudicated for the NKJP files, automatically annotated for the PCC files.

Annotation
----------
VMWEs in this language have been annotated by a single annotator per file. The following [categories](http://parsemefr.lif.univ-mrs.fr/guidelines-hypertext/?page=030_Categories_of_VMWEs) are used: ID, IReflV, LVC, OTH.

Authors
----------
All VMWEs annotations were performed by Agata Savary.

License
----------
The VMWEs annotations are distributed under the terms of the [CC-BY v4](https://creativecommons.org/licenses/by/4.0/) license.
The lemmas, POS-tags, morphological features, and dependency relations, contained in CONNL-U files, are distributed under the terms of the GNU General Public License v.3 ([GNU GPL v.3](https://www.gnu.org/licenses/gpl.html)).

Contact
----------
agata.savary@univ-tours.fr

