## Sentence No. 11335 - 
É saber **ter** **frieza** , **determinação** e **espírito** competitivo . 
### Existing MWEs: 
1- **ter frieza** (LVC)

2- **ter determinação** (LVC, 1), Interleaving 

3- **ter espírito** (LVC), Interleaving 

black Merge Num : 0 Interleaving Num: 2


0- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [É, saber, ter ,.. ]



1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [É]   B= [saber, ter, frieza ,.. ]



2- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [saber, ter, frieza ,.. ]



3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [saber]   B= [ter, frieza, , ,.. ]



4- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ter, frieza, , ,.. ]



5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ter]   B= [frieza, ,, determinação ,.. ]



6- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [frieza, ,, determinação ,.. ]



7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [frieza]   B= [,, determinação, e ,.. ]



8- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, determinação, e ,.. ]



9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [determinação, e, espírito ,.. ]



10- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [determinação, e, espírito ,.. ]



11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [determinação]   B= [e, espírito, competitivo ,.. ]



12- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [e, espírito, competitivo ,.. ]



13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [e]   B= [espírito, competitivo, . ,.. ]



14- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [espírito, competitivo, . ,.. ]



15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [espírito]   B= [competitivo, . ,.. ]



16- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [competitivo, . ,.. ]



17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [competitivo]   B= [.]



18- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [.]



19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [ ]



20- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

## Sentence No. 14830 - 
**fazer** **bondade** para quem **faz** o **mal** é deixar de **fazer** o **bem** a quem merece , é como dar remédio a quem não quer ser curado . 
### Existing MWEs: 
1- **fazer bondade** (LVC)

2- **faz mal** (LVC, 5)

3- **fazer bem** (LVC, 5)

### Identified MWEs: 
1- **fazer bem** (LVC)

black Merge Num : 0 Interleaving Num: 0


0- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [fazer, bondade, para ,.. ]



1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [fazer]   B= [bondade, para, quem ,.. ]



2- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [bondade, para, quem ,.. ]



3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [bondade]   B= [para, quem, faz ,.. ]



4- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [para, quem, faz ,.. ]



5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [para]   B= [quem, faz, o ,.. ]



6- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [quem, faz, o ,.. ]



7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [quem]   B= [faz, o, mal ,.. ]



8- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [faz, o, mal ,.. ]



9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [faz]   B= [o, mal, é ,.. ]



10- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [o, mal, é ,.. ]



11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [o]   B= [mal, é, deixar ,.. ]



12- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [mal, é, deixar ,.. ]



13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [mal]   B= [é, deixar, de ,.. ]



14- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [é, deixar, de ,.. ]



15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [é]   B= [deixar, de, fazer ,.. ]



16- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [deixar, de, fazer ,.. ]



17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [deixar]   B= [de, fazer, o ,.. ]



18- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [de, fazer, o ,.. ]



19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [de]   B= [fazer, o, bem ,.. ]



20- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [fazer, o, bem ,.. ]



21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [fazer]   B= [o, bem, a ,.. ]



22- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [fazer, o]   B= [bem, a, quem ,.. ]



23- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [fazer]   B= [bem, a, quem ,.. ]



24- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [fazer, bem]   B= [a, quem, merece ,.. ]



25- **MERGE_AS_LVC**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[fazer, bem]]   B= [a, quem, merece ,.. ]



26- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [a, quem, merece ,.. ]



27- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [a]   B= [quem, merece, , ,.. ]



28- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [quem, merece, , ,.. ]



29- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [quem]   B= [merece, ,, é ,.. ]



30- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [merece, ,, é ,.. ]



31- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [merece]   B= [,, é, como ,.. ]



32- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, é, como ,.. ]



33- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [é, como, dar ,.. ]



34- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [é, como, dar ,.. ]



35- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [é]   B= [como, dar, remédio ,.. ]



36- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [como, dar, remédio ,.. ]



37- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [como]   B= [dar, remédio, a ,.. ]



38- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [dar, remédio, a ,.. ]



39- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [dar]   B= [remédio, a, quem ,.. ]



40- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [remédio, a, quem ,.. ]



41- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [remédio]   B= [a, quem, não ,.. ]



42- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [a, quem, não ,.. ]



43- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [a]   B= [quem, não, quer ,.. ]



44- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [quem, não, quer ,.. ]



45- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [quem]   B= [não, quer, ser ,.. ]



46- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [não, quer, ser ,.. ]



47- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [não]   B= [quer, ser, curado ,.. ]



48- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [quer, ser, curado ,.. ]



49- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [quer]   B= [ser, curado, . ,.. ]



50- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ser, curado, . ,.. ]



51- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ser]   B= [curado, . ,.. ]



52- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [curado, . ,.. ]



53- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [curado]   B= [.]



54- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [.]



55- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [ ]



56- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

## Sentence No. 19010 - 
bola **correndo** **solta** no gramado do divino , quando roni ( daniel rocha ) **sofre** uma **falta** e vai **bater** o **pênalti** . 
### Existing MWEs: 
1- **correndo solta** (ID)

2- **sofre falta** (LVC)

3- **bater pênalti** (LVC)

### Identified MWEs: 
1- **sofre falta** (LVC)

black Merge Num : 0 Interleaving Num: 0


0- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [bola, correndo, solta ,.. ]



1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [bola]   B= [correndo, solta, no ,.. ]



2- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [correndo, solta, no ,.. ]



3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [correndo]   B= [solta, no, gramado ,.. ]



4- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [solta, no, gramado ,.. ]



5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [solta]   B= [no, gramado, do ,.. ]



6- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [no, gramado, do ,.. ]



7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [no]   B= [gramado, do, divino ,.. ]



8- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [gramado, do, divino ,.. ]



9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [gramado]   B= [do, divino, , ,.. ]



10- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [do, divino, , ,.. ]



11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [do]   B= [divino, ,, quando ,.. ]



12- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [divino, ,, quando ,.. ]



13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [divino]   B= [,, quando, roni ,.. ]



14- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, quando, roni ,.. ]



15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [quando, roni, ( ,.. ]



16- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [quando, roni, ( ,.. ]



17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [quando]   B= [roni, (, daniel ,.. ]



18- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [roni, (, daniel ,.. ]



19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [roni]   B= [(, daniel, rocha ,.. ]



20- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [(, daniel, rocha ,.. ]



21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [(]   B= [daniel, rocha, ) ,.. ]



22- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [daniel, rocha, ) ,.. ]



23- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [daniel]   B= [rocha, ), sofre ,.. ]



24- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [rocha, ), sofre ,.. ]



25- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [rocha]   B= [), sofre, uma ,.. ]



26- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [), sofre, uma ,.. ]



27- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [)]   B= [sofre, uma, falta ,.. ]



28- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [sofre, uma, falta ,.. ]



29- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [sofre]   B= [uma, falta, e ,.. ]



30- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [sofre, uma]   B= [falta, e, vai ,.. ]



31- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [sofre]   B= [falta, e, vai ,.. ]



32- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [sofre, falta]   B= [e, vai, bater ,.. ]



33- **MERGE_AS_LVC**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[sofre, falta]]   B= [e, vai, bater ,.. ]



34- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [e, vai, bater ,.. ]



35- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [e]   B= [vai, bater, o ,.. ]



36- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [vai, bater, o ,.. ]



37- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [vai]   B= [bater, o, pênalti ,.. ]



38- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [bater, o, pênalti ,.. ]



39- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [bater]   B= [o, pênalti, . ,.. ]



40- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [o, pênalti, . ,.. ]



41- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [o]   B= [pênalti, . ,.. ]



42- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [pênalti, . ,.. ]



43- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [pênalti]   B= [.]



44- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [.]



45- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [ ]



46- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

## Sentence No. 155 - 
minhas esposas me deixaram porque eu não as **deixava** **em** **paz** nunca , queria **ter** **relações** a toda hora e , se assim não fosse , satisfazia-me manualmente , quase sem parar . 
### Existing MWEs: 
1- **deixava em paz** (ID)

2- **ter relações** (LVC, 6)

### Identified MWEs: 
1- **ter relações** (LVC)

black Merge Num : 0 Interleaving Num: 0


0- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [minhas, esposas, me ,.. ]



1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [minhas]   B= [esposas, me, deixaram ,.. ]



2- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [esposas, me, deixaram ,.. ]



3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [esposas]   B= [me, deixaram, porque ,.. ]



4- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [me, deixaram, porque ,.. ]



5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [me]   B= [deixaram, porque, eu ,.. ]



6- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [deixaram, porque, eu ,.. ]



7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [deixaram]   B= [porque, eu, não ,.. ]



8- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [porque, eu, não ,.. ]



9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [porque]   B= [eu, não, as ,.. ]



10- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [eu, não, as ,.. ]



11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [eu]   B= [não, as, deixava ,.. ]



12- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [não, as, deixava ,.. ]



13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [não]   B= [as, deixava, em ,.. ]



14- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [as, deixava, em ,.. ]



15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [as]   B= [deixava, em, paz ,.. ]



16- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [deixava, em, paz ,.. ]



17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [deixava]   B= [em, paz, nunca ,.. ]



18- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [em, paz, nunca ,.. ]



19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [em]   B= [paz, nunca, , ,.. ]



20- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [paz, nunca, , ,.. ]



21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [paz]   B= [nunca, ,, queria ,.. ]



22- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [nunca, ,, queria ,.. ]



23- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [nunca]   B= [,, queria, ter ,.. ]



24- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, queria, ter ,.. ]



25- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [queria, ter, relações ,.. ]



26- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [queria, ter, relações ,.. ]



27- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [queria]   B= [ter, relações, a ,.. ]



28- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ter, relações, a ,.. ]



29- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ter]   B= [relações, a, toda ,.. ]



30- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ter, relações]   B= [a, toda, hora ,.. ]



31- **MERGE_AS_LVC**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[ter, relações]]   B= [a, toda, hora ,.. ]



32- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [a, toda, hora ,.. ]



33- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [a]   B= [toda, hora, e ,.. ]



34- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [toda, hora, e ,.. ]



35- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [toda]   B= [hora, e, , ,.. ]



36- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [hora, e, , ,.. ]



37- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [hora]   B= [e, ,, se ,.. ]



38- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [e, ,, se ,.. ]



39- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [e]   B= [,, se, assim ,.. ]



40- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, se, assim ,.. ]



41- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [se, assim, não ,.. ]



42- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [se, assim, não ,.. ]



43- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [se]   B= [assim, não, fosse ,.. ]



44- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [assim, não, fosse ,.. ]



45- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [assim]   B= [não, fosse, , ,.. ]



46- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [não, fosse, , ,.. ]



47- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [não]   B= [fosse, ,, satisfazia-me ,.. ]



48- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [fosse, ,, satisfazia-me ,.. ]



49- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [fosse]   B= [,, satisfazia-me, manualmente ,.. ]



50- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, satisfazia-me, manualmente ,.. ]



51- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [satisfazia-me, manualmente, , ,.. ]



52- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [satisfazia-me, manualmente, , ,.. ]



53- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [satisfazia-me]   B= [manualmente, ,, quase ,.. ]



54- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [manualmente, ,, quase ,.. ]



55- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [manualmente]   B= [,, quase, sem ,.. ]



56- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, quase, sem ,.. ]



57- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [quase, sem, parar ,.. ]



58- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [quase, sem, parar ,.. ]



59- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [quase]   B= [sem, parar, . ,.. ]



60- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [sem, parar, . ,.. ]



61- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [sem]   B= [parar, . ,.. ]



62- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [parar, . ,.. ]



63- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [parar]   B= [.]



64- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [.]



65- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [ ]



66- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

## Sentence No. 160 - 
o espetáculo **faz** **parte** da **turnê** 25 anos de rock , que os músicos vêm **fazendo** pelo brasil , em comemoração a os 25 anos de fundação das duas bandas , que surgiram em 1982 . 
### Existing MWEs: 
1- **faz parte** (ID, 24)

2- **turnê fazendo** (LVC)

### Identified MWEs: 
1- **faz parte** (ID)

black Merge Num : 0 Interleaving Num: 0


0- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [o, espetáculo, faz ,.. ]



1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [o]   B= [espetáculo, faz, parte ,.. ]



2- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [espetáculo, faz, parte ,.. ]



3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [espetáculo]   B= [faz, parte, da ,.. ]



4- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [faz, parte, da ,.. ]



5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [faz]   B= [parte, da, turnê ,.. ]



6- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [faz, parte]   B= [da, turnê, 25 ,.. ]



7- **MERGE_AS_ID**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[faz, parte]]   B= [da, turnê, 25 ,.. ]



8- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [da, turnê, 25 ,.. ]



9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [da]   B= [turnê, 25, anos ,.. ]



10- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [turnê, 25, anos ,.. ]



11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [turnê]   B= [25, anos, de ,.. ]



12- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [25, anos, de ,.. ]



13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [25]   B= [anos, de, rock ,.. ]



14- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [anos, de, rock ,.. ]



15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [anos]   B= [de, rock, , ,.. ]



16- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [de, rock, , ,.. ]



17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [de]   B= [rock, ,, que ,.. ]



18- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [rock, ,, que ,.. ]



19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [rock]   B= [,, que, os ,.. ]



20- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, que, os ,.. ]



21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [que, os, músicos ,.. ]



22- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [que, os, músicos ,.. ]



23- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [que]   B= [os, músicos, vêm ,.. ]



24- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [os, músicos, vêm ,.. ]



25- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [os]   B= [músicos, vêm, fazendo ,.. ]



26- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [músicos, vêm, fazendo ,.. ]



27- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [músicos]   B= [vêm, fazendo, pelo ,.. ]



28- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [vêm, fazendo, pelo ,.. ]



29- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [vêm]   B= [fazendo, pelo, brasil ,.. ]



30- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [fazendo, pelo, brasil ,.. ]



31- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [fazendo]   B= [pelo, brasil, , ,.. ]



32- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [pelo, brasil, , ,.. ]



33- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [pelo]   B= [brasil, ,, em ,.. ]



34- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [brasil, ,, em ,.. ]



35- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [brasil]   B= [,, em, comemoração ,.. ]



36- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, em, comemoração ,.. ]



37- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [em, comemoração, a ,.. ]



38- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [em, comemoração, a ,.. ]



39- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [em]   B= [comemoração, a, os ,.. ]



40- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [comemoração, a, os ,.. ]



41- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [comemoração]   B= [a, os, 25 ,.. ]



42- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [a, os, 25 ,.. ]



43- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [a]   B= [os, 25, anos ,.. ]



44- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [os, 25, anos ,.. ]



45- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [os]   B= [25, anos, de ,.. ]



46- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [25, anos, de ,.. ]



47- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [25]   B= [anos, de, fundação ,.. ]



48- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [anos, de, fundação ,.. ]



49- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [anos]   B= [de, fundação, das ,.. ]



50- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [de, fundação, das ,.. ]



51- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [de]   B= [fundação, das, duas ,.. ]



52- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [fundação, das, duas ,.. ]



53- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [fundação]   B= [das, duas, bandas ,.. ]



54- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [das, duas, bandas ,.. ]



55- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [das]   B= [duas, bandas, , ,.. ]



56- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [duas, bandas, , ,.. ]



57- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [duas]   B= [bandas, ,, que ,.. ]



58- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [bandas, ,, que ,.. ]



59- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [bandas]   B= [,, que, surgiram ,.. ]



60- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, que, surgiram ,.. ]



61- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [que, surgiram, em ,.. ]



62- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [que, surgiram, em ,.. ]



63- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [que]   B= [surgiram, em, 1982 ,.. ]



64- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [surgiram, em, 1982 ,.. ]



65- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [surgiram]   B= [em, 1982, . ,.. ]



66- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [em, 1982, . ,.. ]



67- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [em]   B= [1982, . ,.. ]



68- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [1982, . ,.. ]



69- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [1982]   B= [.]



70- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [.]



71- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [ ]



72- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

