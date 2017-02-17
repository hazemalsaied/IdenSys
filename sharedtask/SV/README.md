README
------
This is the README file for the Swedish language.


Corpora
-------
All annotated data comes from scrambled sentences of the newspaper
Göteborgs Posten, downloaded from Korp at Språkbanken i Gothenburg
(gp2013: Newspaper text Göteborgs Posten).


Extra corpus data
-----------------
The train and test PARSEME-TSV file is perfectly aligned to a CoNLL-U file.

* Lemmas (CoNLL-U): Available (automatically annotated by [UDPipe](https://ufal.mff.cuni.cz/udpipe)).
* POS-tags (CoNLL-U): Available (automatically annotated by [UDPipe](https://ufal.mff.cuni.cz/udpipe)). The tagset is [Universal POS-tags](http://universaldependencies.org/u/pos).
* Morphological features (CoNLL-U): Available (automatically annotated by [UDPipe](https://ufal.mff.cuni.cz/udpipe)).
* Dependency relations (CoNLL-U): Available (automatically annotated by [UDPipe](https://ufal.mff.cuni.cz/udpipe)). The inventory is [Universal Dependency Relations](http://universaldependencies.org/u/dep).
* No-space information (PARSEME-TSV): Available (automatically annotated).


Tokenization
------------
The data was downloaded in a tokenized format provided by Korp.


Annotation
----------
VMWEs in this language are annotated for the following categories: ID, LVC, IReflV, OTH, VPC

Authors
----------
All VMWEs annotations were performed by Joakim Nivre and Sara Stymne.

License
----------
All VMMEs annotations are distributed under the terms of the [CC-BY v4](https://creativecommons.org/licenses/by/4.0/) license.
The lemmas, POS-tags, morphological features and dependency tags (contained in the CoNLL-U files) are distributed under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license, i.e. the same license as the [Swedish Universal Dependencies data](http://universaldependencies.org/#sv), on which [UDPipe](https://ufal.mff.cuni.cz/udpipe) was trained.

Contact
----------
Joakim Nivre (joakim.nivre@lingfil.uu.se)

