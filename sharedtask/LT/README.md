README
------
This is the README file for the Lithuanian language.


Corpora
-------
All annotated data come from one source:
1. DELFI - Lithuanian news portal http://www.delfi.lt/. Texts are published during one month period (2016-08-01 - 2016-09-01) and belong to 9 topics: car review, lifestyle, science, people, news, projects, sport, business, various.



Extra corpus data
-----------------
No CoNLL-U file, only PARSEME-TSV files.

* No-space information: Available (automatically annotated).


Tokenization
------------

* URLs: are not recognized and might be split in parts.
* Numbers: float numbers are preserved as single tokens, unless there are spaces in the middle of the number.
* Abbreviations: dots are tokenized apart from words, e.g., prof. is tokenized as two tokens "prof" and ".".
* Each orthographic word separated by spaces is considered as a single token.


Annotation
----------
VMWEs in this language are annotated for the following categories: ID, LVC.

Authors
----------
The VMWEs annotations were performed by Jolanta Kovalevskaitė, Erika Rimkutė.
The corpus data were prepared by Ieva Bumbulienė, Loic Boizou.

License
----------
The data are distributed under the terms of the [CC-BY-NC-SA](https://creativecommons.org/licenses/by-nc-sa/4.0/) license.

Contact
----------
Jolanta Kovalevskaitė: jolanta.kovalevskaite@vdu.lt
Loic Boizou: lboizou@gmail.com
