README
------
This is the README file for the Spanish language.

Corpora
-------
All annotated data come from one of these sources:
1. `Ancora`: The original Ancora corpus (see reference below).
2. `Ancora_UD`: The Universal Dependencies version of the Ancora Corpus.
3. `IXA_UD`: A corpus compiled by the IXA group in the University of the Basque country and processed with the UD tools.

Extra corpus data
-----------------
The train and test PARSEME-TSV file is perfectly aligned to a CoNLL-U file.
  * Lemmas (CoNLL-U): Available in the two UD corpora (automatically annotated).
  * POS-tags (CoNLL-U): Available in the two UD corpora. The tagset is [Universal POS-tags](http://universaldependencies.org/u/pos).
  * Morphological features (CoNLL-U): Available in the two UD corpora (automatically annotated).
  * Dependency relations (CoNLL-U): Available in the two UD corpora (automatically annotated). The inventory is [Universal Dependency Relations](http://universaldependencies.org/u/dep).
  * No-space information (PARSEME-TSV): Available (automatically annotated) for Ancora. Not available for the UD corpora.
  
Tokenization
------------
  * Hyphens: Always split as a single token in UD.
  * Contractions: In the Ancora corpus contractions are kept as a single unit (not-split). In the UD corpora, most of them are split.
  
Annotation
----------
VMWEs in this language are annotated for the following categories: ID, LVC, IReflV, OTH.

Authors
----------
The VMWEs annotations were performed by the following annotators (in alphabetical order): Cristina Aceta, Itziar Aduriz, Uxoa Iñurrieta, Héctor Martínez Alonso, Carla Parra Escartín, Belem Priego.

License
----------
The VMEs annotations are distributed under the terms of the [CC-BY v4](https://creativecommons.org/licenses/by/4.0/) license.
The lemmas, POS and morphological features, contained in CONNL-U files are distributed under the terms of:
  * the [CC-BY v4](https://creativecommons.org/licenses/by/4.0/) license for the IXA corpus,
  * the GNU General Public License v.3 ([GNU GPL v.3](https://www.gnu.org/licenses/gpl.html)) for the [Ancora](http://universaldependencies.org/#es_ancora) corpus.

Contact
----------
carla.parra@adaptcentre.ie

Reference:
----------
Mariona Taulé, Aina Peris and Horacio Rodríguez (2016) [Iarg-AnCora: Spanish corpus annotated with implicit arguments](http://dx.doi.org/10.1007/s10579-015-9334-3), in Language Resources and Evaluation 50(3), pp. 549--584.


