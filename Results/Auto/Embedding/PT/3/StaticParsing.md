## Sentence No. 14549 - 
se a criança **tem** uma **alimentação** equilibrada , **faz** **uso** de frutas e verduras diariamente e **tem** o **peso** e a **altura** dentro do esperado para a idade , com certeza ela poderá **fazer** **uso** do chocolate sem medo . 
### Existing MWEs: 
1- **tem alimentação** (LVC)Tokens : 
tem
alimentação


2- **faz uso** (LVC)Tokens : 
faz
uso


3- **tem peso** (LVC)Tokens : 
tem
peso


4- **tem altura** (LVC), Interleaving Tokens : 
tem
altura


5- **fazer uso** (LVC)Tokens : 
fazer
uso





0- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [se, a, criança ,.. ]



1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [se]   B= [a, criança, tem ,.. ]



2- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [a, criança, tem ,.. ]



3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [a]   B= [criança, tem, uma ,.. ]



4- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [criança, tem, uma ,.. ]



5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [criança]   B= [tem, uma, alimentação ,.. ]



6- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [tem, uma, alimentação ,.. ]



7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [tem]   B= [uma, alimentação, equilibrada ,.. ]



8- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [tem, uma]   B= [alimentação, equilibrada, , ,.. ]



9- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [tem]   B= [alimentação, equilibrada, , ,.. ]



10- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [tem, alimentação]   B= [equilibrada, ,, faz ,.. ]



11- **MERGE_AS_LVC**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[tem, alimentação]]   B= [equilibrada, ,, faz ,.. ]



12- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [equilibrada, ,, faz ,.. ]



13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [equilibrada]   B= [,, faz, uso ,.. ]



14- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, faz, uso ,.. ]



15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [faz, uso, de ,.. ]



16- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [faz, uso, de ,.. ]



17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [faz]   B= [uso, de, frutas ,.. ]



18- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [faz, uso]   B= [de, frutas, e ,.. ]



19- **MERGE_AS_LVC**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[faz, uso]]   B= [de, frutas, e ,.. ]



20- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [de, frutas, e ,.. ]



21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [de]   B= [frutas, e, verduras ,.. ]



22- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [frutas, e, verduras ,.. ]



23- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [frutas]   B= [e, verduras, diariamente ,.. ]



24- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [e, verduras, diariamente ,.. ]



25- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [e]   B= [verduras, diariamente, e ,.. ]



26- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [verduras, diariamente, e ,.. ]



27- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [verduras]   B= [diariamente, e, tem ,.. ]



28- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [diariamente, e, tem ,.. ]



29- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [diariamente]   B= [e, tem, o ,.. ]



30- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [e, tem, o ,.. ]



31- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [e]   B= [tem, o, peso ,.. ]



32- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [tem, o, peso ,.. ]



33- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [tem]   B= [o, peso, e ,.. ]



34- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [tem, o]   B= [peso, e, a ,.. ]



35- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [tem]   B= [peso, e, a ,.. ]



36- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [tem, peso]   B= [e, a, altura ,.. ]



37- **MERGE_AS_LVC**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[tem, peso]]   B= [e, a, altura ,.. ]



38- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [e, a, altura ,.. ]



39- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [e]   B= [a, altura, dentro ,.. ]



40- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [a, altura, dentro ,.. ]



41- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [a]   B= [altura, dentro, do ,.. ]



42- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [altura, dentro, do ,.. ]



43- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [altura]   B= [dentro, do, esperado ,.. ]



44- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [dentro, do, esperado ,.. ]



45- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [dentro]   B= [do, esperado, para ,.. ]



46- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [do, esperado, para ,.. ]



47- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [do]   B= [esperado, para, a ,.. ]



48- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [esperado, para, a ,.. ]



49- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [esperado]   B= [para, a, idade ,.. ]



50- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [para, a, idade ,.. ]



51- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [para]   B= [a, idade, , ,.. ]



52- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [a, idade, , ,.. ]



53- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [a]   B= [idade, ,, com ,.. ]



54- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [idade, ,, com ,.. ]



55- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [idade]   B= [,, com, certeza ,.. ]



56- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, com, certeza ,.. ]



57- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [com, certeza, ela ,.. ]



58- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [com, certeza, ela ,.. ]



59- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [com]   B= [certeza, ela, poderá ,.. ]



60- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [certeza, ela, poderá ,.. ]



61- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [certeza]   B= [ela, poderá, fazer ,.. ]



62- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ela, poderá, fazer ,.. ]



63- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ela]   B= [poderá, fazer, uso ,.. ]



64- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [poderá, fazer, uso ,.. ]



65- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [poderá]   B= [fazer, uso, do ,.. ]



66- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [fazer, uso, do ,.. ]



67- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [fazer]   B= [uso, do, chocolate ,.. ]



68- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [fazer, uso]   B= [do, chocolate, sem ,.. ]



69- **MERGE_AS_LVC**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[fazer, uso]]   B= [do, chocolate, sem ,.. ]



70- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [do, chocolate, sem ,.. ]



71- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [do]   B= [chocolate, sem, medo ,.. ]



72- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [chocolate, sem, medo ,.. ]



73- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [chocolate]   B= [sem, medo, . ,.. ]



74- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [sem, medo, . ,.. ]



75- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [sem]   B= [medo, . ,.. ]



76- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [medo, . ,.. ]



77- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [medo]   B= [.]



78- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [.]



79- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [ ]



80- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

## Sentence No. 13361 - 
engravidar nesse período , como vocês diriam , é **marcar** **bobeira** , é **pagar** **mico** , é ter que agüentar os adultos **se** **intrometendo** mais na suas vidas , é perder a **liberdade** que se **tem** num só instante da nossa existência , quando se é jovem . 
### Existing MWEs: 
1- **marcar bobeira** (LVC)Tokens : 
marcar
bobeira


2- **pagar mico** (LVC)Tokens : 
pagar
mico


3- **se intrometendo** (IReflV)Tokens : 
se
intrometendo


4- **liberdade tem** (LVC)Tokens : 
liberdade
tem





0- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [engravidar, nesse, período ,.. ]



1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [engravidar]   B= [nesse, período, , ,.. ]



2- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [nesse, período, , ,.. ]



3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [nesse]   B= [período, ,, como ,.. ]



4- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [período, ,, como ,.. ]



5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [período]   B= [,, como, vocês ,.. ]



6- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, como, vocês ,.. ]



7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [como, vocês, diriam ,.. ]



8- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [como, vocês, diriam ,.. ]



9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [como]   B= [vocês, diriam, , ,.. ]



10- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [vocês, diriam, , ,.. ]



11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [vocês]   B= [diriam, ,, é ,.. ]



12- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [diriam, ,, é ,.. ]



13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [diriam]   B= [,, é, marcar ,.. ]



14- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, é, marcar ,.. ]



15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [é, marcar, bobeira ,.. ]



16- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [é, marcar, bobeira ,.. ]



17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [é]   B= [marcar, bobeira, , ,.. ]



18- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [marcar, bobeira, , ,.. ]



19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [marcar]   B= [bobeira, ,, é ,.. ]



20- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [marcar, bobeira]   B= [,, é, pagar ,.. ]



21- **MERGE_AS_LVC**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[marcar, bobeira]]   B= [,, é, pagar ,.. ]



22- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, é, pagar ,.. ]



23- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [é, pagar, mico ,.. ]



24- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [é, pagar, mico ,.. ]



25- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [é]   B= [pagar, mico, , ,.. ]



26- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [pagar, mico, , ,.. ]



27- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [pagar]   B= [mico, ,, é ,.. ]



28- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [pagar, mico]   B= [,, é, ter ,.. ]



29- **MERGE_AS_LVC**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[pagar, mico]]   B= [,, é, ter ,.. ]



30- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, é, ter ,.. ]



31- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [é, ter, que ,.. ]



32- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [é, ter, que ,.. ]



33- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [é]   B= [ter, que, agüentar ,.. ]



34- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ter, que, agüentar ,.. ]



35- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ter]   B= [que, agüentar, os ,.. ]



36- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [que, agüentar, os ,.. ]



37- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [que]   B= [agüentar, os, adultos ,.. ]



38- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [agüentar, os, adultos ,.. ]



39- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [agüentar]   B= [os, adultos, se ,.. ]



40- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [os, adultos, se ,.. ]



41- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [os]   B= [adultos, se, intrometendo ,.. ]



42- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [adultos, se, intrometendo ,.. ]



43- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [adultos]   B= [se, intrometendo, mais ,.. ]



44- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [se, intrometendo, mais ,.. ]



45- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [se]   B= [intrometendo, mais, na ,.. ]



46- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [se, intrometendo]   B= [mais, na, suas ,.. ]



47- **MERGE_AS_IReflV**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[se, intrometendo]]   B= [mais, na, suas ,.. ]



48- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [mais, na, suas ,.. ]



49- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [mais]   B= [na, suas, vidas ,.. ]



50- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [na, suas, vidas ,.. ]



51- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [na]   B= [suas, vidas, , ,.. ]



52- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [suas, vidas, , ,.. ]



53- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [suas]   B= [vidas, ,, é ,.. ]



54- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [vidas, ,, é ,.. ]



55- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [vidas]   B= [,, é, perder ,.. ]



56- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, é, perder ,.. ]



57- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [é, perder, a ,.. ]



58- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [é, perder, a ,.. ]



59- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [é]   B= [perder, a, liberdade ,.. ]



60- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [perder, a, liberdade ,.. ]



61- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [perder]   B= [a, liberdade, que ,.. ]



62- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [a, liberdade, que ,.. ]



63- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [a]   B= [liberdade, que, se ,.. ]



64- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [liberdade, que, se ,.. ]



65- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [liberdade]   B= [que, se, tem ,.. ]



66- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [liberdade, que]   B= [se, tem, num ,.. ]



67- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [liberdade]   B= [se, tem, num ,.. ]



68- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [liberdade, se]   B= [tem, num, só ,.. ]



69- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [liberdade]   B= [tem, num, só ,.. ]



70- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [liberdade, tem]   B= [num, só, instante ,.. ]



71- **MERGE_AS_LVC**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[liberdade, tem]]   B= [num, só, instante ,.. ]



72- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [num, só, instante ,.. ]



73- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [num]   B= [só, instante, da ,.. ]



74- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [só, instante, da ,.. ]



75- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [só]   B= [instante, da, nossa ,.. ]



76- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [instante, da, nossa ,.. ]



77- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [instante]   B= [da, nossa, existência ,.. ]



78- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [da, nossa, existência ,.. ]



79- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [da]   B= [nossa, existência, , ,.. ]



80- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [nossa, existência, , ,.. ]



81- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [nossa]   B= [existência, ,, quando ,.. ]



82- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [existência, ,, quando ,.. ]



83- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [existência]   B= [,, quando, se ,.. ]



84- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, quando, se ,.. ]



85- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [quando, se, é ,.. ]



86- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [quando, se, é ,.. ]



87- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [quando]   B= [se, é, jovem ,.. ]



88- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [se, é, jovem ,.. ]



89- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [se]   B= [é, jovem, . ,.. ]



90- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [é, jovem, . ,.. ]



91- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [é]   B= [jovem, . ,.. ]



92- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [jovem, . ,.. ]



93- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [jovem]   B= [.]



94- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [.]



95- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [ ]



96- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

## Sentence No. 913 - 
no olímpico , com uma vantagem que não era pequena , o grêmio **levou** um **banho** de bola do juventude , **perdeu** o jogo , **a** **cabeça** , **deu** **adeus** a o gauchão e provou que carece , com urgência , de qualidade para enfrentar as duras batalhas da copa do brasil e do brasileirão . 
### Existing MWEs: 
1- **levou banho** (LVC)Tokens : 
levou
banho


2- **perdeu a cabeça** (ID)Tokens : 
perdeu
a
cabeça


3- **deu adeus** (LVC)Tokens : 
deu
adeus





0- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [no, olímpico, , ,.. ]



1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [no]   B= [olímpico, ,, com ,.. ]



2- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [olímpico, ,, com ,.. ]



3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [olímpico]   B= [,, com, uma ,.. ]



4- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, com, uma ,.. ]



5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [com, uma, vantagem ,.. ]



6- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [com, uma, vantagem ,.. ]



7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [com]   B= [uma, vantagem, que ,.. ]



8- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [uma, vantagem, que ,.. ]



9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [uma]   B= [vantagem, que, não ,.. ]



10- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [vantagem, que, não ,.. ]



11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [vantagem]   B= [que, não, era ,.. ]



12- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [que, não, era ,.. ]



13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [que]   B= [não, era, pequena ,.. ]



14- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [não, era, pequena ,.. ]



15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [não]   B= [era, pequena, , ,.. ]



16- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [era, pequena, , ,.. ]



17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [era]   B= [pequena, ,, o ,.. ]



18- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [pequena, ,, o ,.. ]



19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [pequena]   B= [,, o, grêmio ,.. ]



20- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, o, grêmio ,.. ]



21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [o, grêmio, levou ,.. ]



22- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [o, grêmio, levou ,.. ]



23- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [o]   B= [grêmio, levou, um ,.. ]



24- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [grêmio, levou, um ,.. ]



25- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [grêmio]   B= [levou, um, banho ,.. ]



26- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [levou, um, banho ,.. ]



27- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [levou]   B= [um, banho, de ,.. ]



28- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [levou, um]   B= [banho, de, bola ,.. ]



29- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [levou]   B= [banho, de, bola ,.. ]



30- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [levou, banho]   B= [de, bola, do ,.. ]



31- **MERGE_AS_LVC**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[levou, banho]]   B= [de, bola, do ,.. ]



32- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [de, bola, do ,.. ]



33- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [de]   B= [bola, do, juventude ,.. ]



34- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [bola, do, juventude ,.. ]



35- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [bola]   B= [do, juventude, , ,.. ]



36- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [do, juventude, , ,.. ]



37- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [do]   B= [juventude, ,, perdeu ,.. ]



38- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [juventude, ,, perdeu ,.. ]



39- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [juventude]   B= [,, perdeu, o ,.. ]



40- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, perdeu, o ,.. ]



41- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [perdeu, o, jogo ,.. ]



42- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [perdeu, o, jogo ,.. ]



43- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [perdeu]   B= [o, jogo, , ,.. ]



44- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [perdeu, o]   B= [jogo, ,, a ,.. ]



45- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [perdeu]   B= [jogo, ,, a ,.. ]



46- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [perdeu, jogo]   B= [,, a, cabeça ,.. ]



47- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [perdeu]   B= [,, a, cabeça ,.. ]



48- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [perdeu, ,]   B= [a, cabeça, , ,.. ]



49- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [perdeu]   B= [a, cabeça, , ,.. ]



50- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [perdeu, a]   B= [cabeça, ,, deu ,.. ]



51- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [perdeu, a, cabeça]   B= [,, deu, adeus ,.. ]



52- WHITE_MERGE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [perdeu, [a, cabeça]]   B= [,, deu, adeus ,.. ]



53- **MERGE_AS_ID**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[perdeu, [a, cabeça]]]   B= [,, deu, adeus ,.. ]



54- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, deu, adeus ,.. ]



55- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [deu, adeus, a ,.. ]



56- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [deu, adeus, a ,.. ]



57- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [deu]   B= [adeus, a, o ,.. ]



58- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [deu, adeus]   B= [a, o, gauchão ,.. ]



59- **MERGE_AS_LVC**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[deu, adeus]]   B= [a, o, gauchão ,.. ]



60- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [a, o, gauchão ,.. ]



61- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [a]   B= [o, gauchão, e ,.. ]



62- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [o, gauchão, e ,.. ]



63- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [o]   B= [gauchão, e, provou ,.. ]



64- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [gauchão, e, provou ,.. ]



65- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [gauchão]   B= [e, provou, que ,.. ]



66- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [e, provou, que ,.. ]



67- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [e]   B= [provou, que, carece ,.. ]



68- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [provou, que, carece ,.. ]



69- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [provou]   B= [que, carece, , ,.. ]



70- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [que, carece, , ,.. ]



71- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [que]   B= [carece, ,, com ,.. ]



72- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [carece, ,, com ,.. ]



73- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [carece]   B= [,, com, urgência ,.. ]



74- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, com, urgência ,.. ]



75- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [com, urgência, , ,.. ]



76- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [com, urgência, , ,.. ]



77- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [com]   B= [urgência, ,, de ,.. ]



78- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [urgência, ,, de ,.. ]



79- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [urgência]   B= [,, de, qualidade ,.. ]



80- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, de, qualidade ,.. ]



81- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [de, qualidade, para ,.. ]



82- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [de, qualidade, para ,.. ]



83- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [de]   B= [qualidade, para, enfrentar ,.. ]



84- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [qualidade, para, enfrentar ,.. ]



85- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [qualidade]   B= [para, enfrentar, as ,.. ]



86- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [para, enfrentar, as ,.. ]



87- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [para]   B= [enfrentar, as, duras ,.. ]



88- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [enfrentar, as, duras ,.. ]



89- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [enfrentar]   B= [as, duras, batalhas ,.. ]



90- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [as, duras, batalhas ,.. ]



91- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [as]   B= [duras, batalhas, da ,.. ]



92- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [duras, batalhas, da ,.. ]



93- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [duras]   B= [batalhas, da, copa ,.. ]



94- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [batalhas, da, copa ,.. ]



95- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [batalhas]   B= [da, copa, do ,.. ]



96- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [da, copa, do ,.. ]



97- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [da]   B= [copa, do, brasil ,.. ]



98- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [copa, do, brasil ,.. ]



99- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [copa]   B= [do, brasil, e ,.. ]



100- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [do, brasil, e ,.. ]



101- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [do]   B= [brasil, e, do ,.. ]



102- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [brasil, e, do ,.. ]



103- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [brasil]   B= [e, do, brasileirão ,.. ]



104- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [e, do, brasileirão ,.. ]



105- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [e]   B= [do, brasileirão, . ,.. ]



106- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [do, brasileirão, . ,.. ]



107- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [do]   B= [brasileirão, . ,.. ]



108- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [brasileirão, . ,.. ]



109- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [brasileirão]   B= [.]



110- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [.]



111- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [ ]



112- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

## Sentence No. 1222 - 
para **se** **candidatar** às vagas , as interessadas devem **entrar** **em** **contato** com a ong pelo e-mail : maesocial@aldeiasinfantis.org.br . como a partir do mês de julho o sistema analógico será desativado , a recomendação é que os usuários procurem **realizar** a **troca** até o final de junho . 
### Existing MWEs: 
3- **se candidatar** (IReflV)Tokens : 
se
candidatar


1- **entrar em contato** (LVC)Tokens : 
entrar
em
contato


2- **realizar troca** (LVC)Tokens : 
realizar
troca





0- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [para, se, candidatar ,.. ]



1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [para]   B= [se, candidatar, às ,.. ]



2- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [se, candidatar, às ,.. ]



3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [se]   B= [candidatar, às, vagas ,.. ]



4- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [se, candidatar]   B= [às, vagas, , ,.. ]



5- **MERGE_AS_IReflV**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[se, candidatar]]   B= [às, vagas, , ,.. ]



6- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [às, vagas, , ,.. ]



7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [às]   B= [vagas, ,, as ,.. ]



8- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [vagas, ,, as ,.. ]



9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [vagas]   B= [,, as, interessadas ,.. ]



10- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, as, interessadas ,.. ]



11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [as, interessadas, devem ,.. ]



12- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [as, interessadas, devem ,.. ]



13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [as]   B= [interessadas, devem, entrar ,.. ]



14- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [interessadas, devem, entrar ,.. ]



15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [interessadas]   B= [devem, entrar, em ,.. ]



16- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [devem, entrar, em ,.. ]



17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [devem]   B= [entrar, em, contato ,.. ]



18- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [entrar, em, contato ,.. ]



19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [entrar]   B= [em, contato, com ,.. ]



20- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [entrar, em]   B= [contato, com, a ,.. ]



21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [entrar, em, contato]   B= [com, a, ong ,.. ]



22- WHITE_MERGE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [entrar, [em, contato]]   B= [com, a, ong ,.. ]



23- **MERGE_AS_LVC**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[entrar, [em, contato]]]   B= [com, a, ong ,.. ]



24- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [com, a, ong ,.. ]



25- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [com]   B= [a, ong, pelo ,.. ]



26- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [a, ong, pelo ,.. ]



27- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [a]   B= [ong, pelo, e-mail ,.. ]



28- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ong, pelo, e-mail ,.. ]



29- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ong]   B= [pelo, e-mail, : ,.. ]



30- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [pelo, e-mail, : ,.. ]



31- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [pelo]   B= [e-mail, :, maesocial@aldeiasinfantis.org.br ,.. ]



32- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [e-mail, :, maesocial@aldeiasinfantis.org.br ,.. ]



33- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [e-mail]   B= [:, maesocial@aldeiasinfantis.org.br, . ,.. ]



34- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [:, maesocial@aldeiasinfantis.org.br, . ,.. ]



35- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [:]   B= [maesocial@aldeiasinfantis.org.br, ., como ,.. ]



36- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [maesocial@aldeiasinfantis.org.br, ., como ,.. ]



37- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [maesocial@aldeiasinfantis.org.br]   B= [., como, a ,.. ]



38- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [., como, a ,.. ]



39- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [como, a, partir ,.. ]



40- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [como, a, partir ,.. ]



41- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [como]   B= [a, partir, do ,.. ]



42- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [a, partir, do ,.. ]



43- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [a]   B= [partir, do, mês ,.. ]



44- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [partir, do, mês ,.. ]



45- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [partir]   B= [do, mês, de ,.. ]



46- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [do, mês, de ,.. ]



47- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [do]   B= [mês, de, julho ,.. ]



48- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [mês, de, julho ,.. ]



49- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [mês]   B= [de, julho, o ,.. ]



50- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [de, julho, o ,.. ]



51- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [de]   B= [julho, o, sistema ,.. ]



52- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [julho, o, sistema ,.. ]



53- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [julho]   B= [o, sistema, analógico ,.. ]



54- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [o, sistema, analógico ,.. ]



55- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [o]   B= [sistema, analógico, será ,.. ]



56- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [sistema, analógico, será ,.. ]



57- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [sistema]   B= [analógico, será, desativado ,.. ]



58- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [analógico, será, desativado ,.. ]



59- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [analógico]   B= [será, desativado, , ,.. ]



60- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [será, desativado, , ,.. ]



61- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [será]   B= [desativado, ,, a ,.. ]



62- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [desativado, ,, a ,.. ]



63- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [desativado]   B= [,, a, recomendação ,.. ]



64- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, a, recomendação ,.. ]



65- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [a, recomendação, é ,.. ]



66- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [a, recomendação, é ,.. ]



67- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [a]   B= [recomendação, é, que ,.. ]



68- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [recomendação, é, que ,.. ]



69- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [recomendação]   B= [é, que, os ,.. ]



70- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [é, que, os ,.. ]



71- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [é]   B= [que, os, usuários ,.. ]



72- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [que, os, usuários ,.. ]



73- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [que]   B= [os, usuários, procurem ,.. ]



74- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [os, usuários, procurem ,.. ]



75- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [os]   B= [usuários, procurem, realizar ,.. ]



76- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [usuários, procurem, realizar ,.. ]



77- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [usuários]   B= [procurem, realizar, a ,.. ]



78- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [procurem, realizar, a ,.. ]



79- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [procurem]   B= [realizar, a, troca ,.. ]



80- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [realizar, a, troca ,.. ]



81- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [realizar]   B= [a, troca, até ,.. ]



82- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [realizar, a]   B= [troca, até, o ,.. ]



83- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [realizar]   B= [troca, até, o ,.. ]



84- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [realizar, troca]   B= [até, o, final ,.. ]



85- **MERGE_AS_LVC**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[realizar, troca]]   B= [até, o, final ,.. ]



86- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [até, o, final ,.. ]



87- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [até]   B= [o, final, de ,.. ]



88- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [o, final, de ,.. ]



89- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [o]   B= [final, de, junho ,.. ]



90- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [final, de, junho ,.. ]



91- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [final]   B= [de, junho, . ,.. ]



92- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [de, junho, . ,.. ]



93- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [de]   B= [junho, . ,.. ]



94- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [junho, . ,.. ]



95- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [junho]   B= [.]



96- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [.]



97- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [ ]



98- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

## Sentence No. 2718 - 
quem **está** **com** alguma **infecção** aguda , **febre** ou **tem** algum **antecedente** alérgico deve consultar um médico antes de receber a dose . 
### Existing MWEs: 
1- **está com febre** (LVC)Tokens : 
está
com
febre


2- **está com infecção** (LVC), Interleaving Tokens : 
está
com
infecção


3- **tem antecedente** (LVC)Tokens : 
tem
antecedente





0- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [quem, está, com ,.. ]



1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [quem]   B= [está, com, alguma ,.. ]



2- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [está, com, alguma ,.. ]



3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [está]   B= [com, alguma, infecção ,.. ]



4- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [está, com]   B= [alguma, infecção, aguda ,.. ]



5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [está, com, alguma]   B= [infecção, aguda, , ,.. ]



6- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [está, com]   B= [infecção, aguda, , ,.. ]



7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [está, com, infecção]   B= [aguda, ,, febre ,.. ]



8- WHITE_MERGE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [está, [com, infecção]]   B= [aguda, ,, febre ,.. ]



9- **MERGE_AS_LVC**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[está, [com, infecção]]]   B= [aguda, ,, febre ,.. ]



10- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [aguda, ,, febre ,.. ]



11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [aguda]   B= [,, febre, ou ,.. ]



12- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, febre, ou ,.. ]



13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [febre, ou, tem ,.. ]



14- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [febre, ou, tem ,.. ]



15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [febre]   B= [ou, tem, algum ,.. ]



16- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [febre, ou]   B= [tem, algum, antecedente ,.. ]



17- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [febre]   B= [tem, algum, antecedente ,.. ]



18- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [febre, tem]   B= [algum, antecedente, alérgico ,.. ]



19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [febre, tem, algum]   B= [antecedente, alérgico, deve ,.. ]



20- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [febre, tem]   B= [antecedente, alérgico, deve ,.. ]



21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [febre, tem, antecedente]   B= [alérgico, deve, consultar ,.. ]



22- **MERGE_AS_LVC**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [febre, [tem, antecedente]]   B= [alérgico, deve, consultar ,.. ]



23- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [febre]   B= [alérgico, deve, consultar ,.. ]



24- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [febre, alérgico]   B= [deve, consultar, um ,.. ]



25- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [febre]   B= [deve, consultar, um ,.. ]



26- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [febre, deve]   B= [consultar, um, médico ,.. ]



27- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [febre]   B= [consultar, um, médico ,.. ]



28- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [febre, consultar]   B= [um, médico, antes ,.. ]



29- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [febre]   B= [um, médico, antes ,.. ]



30- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [febre, um]   B= [médico, antes, de ,.. ]



31- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [febre]   B= [médico, antes, de ,.. ]



32- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [febre, médico]   B= [antes, de, receber ,.. ]



33- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [febre]   B= [antes, de, receber ,.. ]



34- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [febre, antes]   B= [de, receber, a ,.. ]



35- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [febre]   B= [de, receber, a ,.. ]



36- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [febre, de]   B= [receber, a, dose ,.. ]



37- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [febre]   B= [receber, a, dose ,.. ]



38- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [febre, receber]   B= [a, dose, . ,.. ]



39- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [febre]   B= [a, dose, . ,.. ]



40- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [febre, a]   B= [dose, . ,.. ]



41- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [febre]   B= [dose, . ,.. ]



42- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [febre, dose]   B= [.]



43- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [febre]   B= [.]



44- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [febre, .]   B= [ ]



45- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [febre]   B= [ ]



46- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

