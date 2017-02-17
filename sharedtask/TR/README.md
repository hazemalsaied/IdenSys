README
------
This is the README file for the Turkish language.


Corpora
-------
All annotated data come from Turkish newspaper sources.
The Turkish dataset is annotated according to the PARSEME Shared Task on Automatic Identification of Verbal Multiword Expressions Guidelines and
the following publication (\cite{ciclingkubra}):

Kübra Adalı, Tutkum Dinç, Memduh Gokirmak and Gülşen Eryiğit. 2016. Comprehensive annotation of multiword expressions for Turkish. 
In TurCLing 2016, The First International Conference on Turkic Computational Linguistics at CICLING 2016, pages 60–66, Konya, Turkey, April.
 
Extra corpus data
-----------------
The train and test PARSEME-TSV file is perfectly aligned to a CoNLL-U file.

* Lemmas (CoNLL-U): Available (automatically annotated by ITU NLP pipeline http://tools.nlp.itu.edu.tr/ \cite{itunlp}).
* POS-tags (CoNLL-U): Available (automatically annotated by ITU NLP pipeline http://tools.nlp.itu.edu.tr \cite{itunlp} and mapped to Universal POS-tags as explained in \cite{sulubacak-EtAl:2016:COLING}).
* Morphological features (CoNLL-U): Available (automatically annotated by ITU NLP pipeline http://tools.nlp.itu.edu.tr \cite{itunlp} and mapped to Universal POS-tags as explained in \cite{sulubacak-EtAl:2016:COLING}).
* Dependency relations (CoNLL-U): Available (automatically annotated by ITU NLP pipeline http://tools.nlp.itu.edu.tr \cite{itunlp} and mapped to Universal Dependencies as explained in \cite{sulubacak-EtAl:2016:COLING}).

Umut Sulubacak, Memduh Gokirmak, Francis Tyers, Çağrı Çöltekin, Joakim Nivre, and Gülşen Eryiğit. 2016a. Universal dependencies for Turkish. In Proceedings of the 26th International Conference on Computational Linguistics , COLING’16, Osaka, Japan, December.
Gülşen Eryiğit. ITU Turkish NLP Web Interface. In Proceedings of the Demonstrations at the 14th Conference of the European Chapter of the Association for Computational Linguistics (EACL 2014). Gothenburg, Sweden, April 2014

Tokenization: 
------------
* The inflectional group (IG) formalism  has become the de facto standard in parsing Turkish. 
According to the formalism, orthographic tokens are divided into morphosyntactic words from derivational boundaries. \cite{sulubacak-EtAl:2016:COLING}
As a result, the token numbers in the CoNLL-U file may be higher then the data.parsemetsv file for sentences containing such words.


Annotation
----------
VMWEs in this language are annotated for the following categories: ID, LVC, OTH.

The Turkish annotated corpus consists of 17500 sentences in total.
Language Leader: Gülşen Eryiğit (contact: gulsen.cebiroglu@itu.edu.tr)
The annotation team consists of 4 members: Kübra Adalı, Tutkum Dinç, Ayşenur Miral, Mert Boz.

Copyright information
----------
Creative Commons  CC-BY-NC-SA License.
https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode

Citation information
----------
Please refer to the following 3 publications while using the Turkish dataset:
@InProceedings{ciclingkubra,
  author = {Adal{\i}, Kübra and Din\c{c}, Tutkum and Gokirmak, Memduh and Eryi\u{g}it, G\"{u}l\c{s}en},
  title = {Comprehensive Annotation of Multiword Expressions for Turkish},
  booktitle = {TurCLing 2016, The First International Conference on Turkic Computational Linguistics at CICLING 2016},
  month = {April},
  year = {2016},
  address = {Konya, Turkey},
  pages={60--66}
}

Licence
-------
The full dataset is licensed under **Creative Commons Non-Commercial Share-Alike 4.0** licence [CC-BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)

@InProceedings{sulubacak-EtAl:2016:COLING,
  author    = {Sulubacak, Umut  and  Gokirmak, Memduh  and  Tyers, Francis  and  \c{C}\"{o}ltekin, \c{C}a\u{g}ri  and  Nivre, Joakim  and  Eryi\u{g}it, G\"{u}l\c{s}en},
  title     = {Universal Dependencies for Turkish},
  booktitle = {Proceedings of COLING 2016, the 26th International Conference on Computational Linguistics},
  month     = {December},
  year      = {2016},
  address   = {Osaka, Japan},
  publisher = {The COLING 2016 Organizing Committee},
  pages     = {3444--3454},
  url       = {http://aclweb.org/anthology/C16-1325}
}
@InProceedings{itunlp,
  author = {Eryi{\u g}it, G{\"u}l{\c s}en},
  title = {{ITU} {T}urkish {NLP} Web Service},
  booktitle = {Proceedings of the Demonstrations at the 14th Conference of the European Chapter of the Association for Computational Linguistics (EACL)},
  month = {April},
  year = {2014},
  address = {Gothenburg, Sweden},
  publisher = {Association for Computational Linguistics},
}
