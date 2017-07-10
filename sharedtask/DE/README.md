README
------
This is the README file for the German language.

Corpora
-------
All annotated data come from the annual workshop on statistical
machine translation, [WMT 2015](http://statmt.org/wmt15/translation-task.html#download)
news2013: News Crawl: articles from 2013 (Bojar et al. 2016).

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
The tokenization was performed using the WMT script for German tokenization.


Annotation
----------
VMWEs in this language are annotated for the following categories: ID, LVC, IReflV, OTH, VPC.

Authors
----------
All VMWEs annotations were performed by Fabienne Cap and Glorianna Jagfeld.

License
----------
All VMWEs annotations are distributed under the terms of the [CC-BY v4](https://creativecommons.org/licenses/by/4.0/) license.
The lemmas, POS-tags, morphological features and dependency tags (contained in the CoNLL-U files) are distributed under the [CC BY-NC-SA 3.0 US](https://creativecommons.org/licenses/by-nc-sa/3.0/us/) license, i.e. the same license as the [German Universal Dependencies data](http://universaldependencies.org/#de), on which [UDPipe](https://ufal.mff.cuni.cz/udpipe) was trained.

Contact
----------
fabienne.cap@lingfil.uu.se

References
----------
Bojar et al. 2016 "Findings of the 2016 conference on machine translation (WMT16)". In Proceedings of the First Conference on Machine Translation.

@inproceedings{bojar2016findings,
  title={Findings of the 2016 conference on machine translation (WMT16)},
  author={Bojar, Ondrej and Chatterjee, Rajen and Federmann, Christian and Graham, Yvette and Haddow, Barry and Huck, Matthias and Yepes, Antonio Jimeno and Koehn, Philipp and Logacheva, Varvara and Monz, Christof and others},
  booktitle={Proceedings of the First Conference on Machine Translation (WMT)},
  volume={2},
  pages={131--198},
  year={2016}
}

