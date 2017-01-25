README
------
This is the README file for the Hungarian language.


Corpora
-------
All annotated data come from the Szeged Dependency Treebank.


Extra corpus data
-----------------
The PARSEME-TSV file is perfectly aligned to a CoNLL-U file, which includes the following data:

* Lemmas (Column 3): Available (manually annotated).
* POS-tags (Column 4): Available (manually annotated). The tagset is MSD.
* Morphological features (Column 6): Available (manually annotated). The tagset is MSD.
* Dependency heads and relations (Columns 7 and 8): Available (manually annotated). The inventory is the original annotation of the Szeged Dependency Treebank.

The PARSEME-TSV file contains the follwoing information:
* No-space information (PARSEME-TSV): Available (automatically annotated).
* VMWE annotation (PARSEME-TSV): Available (manually annotated).


Tokenization
------------
Manually annotated for all the files.


Annotation
----------
VMWEs in this language have been annotated by a single annotator per file.
The following [categories](http://parsemefr.lif.univ-mrs.fr/guidelines-hypertext/?page=030_Categories_of_VMWEs) are used: ID, LVC, VPC, OTH.


Authors
----------
All VMWEs annotations were performed by Viktória Kovács, Katalin Ilona Simkó and Veronika Vincze.


License
----------
The VMEs annotations are distributed under the terms of the [CC-BY v4](https://creativecommons.org/licenses/by/4.0/) license.
The lemmas, POS and morphological features, contained in CONNL-U files are distributed under the terms of the GNU General Public License v.3 ([GNU GPL v.3](https://www.gnu.org/licenses/gpl.html)).

Contact
----------
vinczev@inf.u-szeged.hu
