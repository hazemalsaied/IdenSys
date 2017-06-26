## Sentence No. 672 - 
me **da** **igual** que pueda **tener** **repercusión** dentro de el campo , pero **estoy** **en** el **deber** de avisar lo " , explicó ferreira , quien confesó que el árbitro madrileño no le **trae** " buenos **recuerdos** " . 
### Existing MWEs: 
2- **da igual** (ID)

4- **tener repercusión** (LVC)

1- **estoy en deber** (LVC)

3- **trae recuerdos** (ID)

black Merge Num : 0 Interleaving Num: 0


0- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [me, da, igual ,.. ]



1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [me]   B= [da, igual, que ,.. ]



2- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [da, igual, que ,.. ]



3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [da]   B= [igual, que, pueda ,.. ]



4- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [da, igual]   B= [que, pueda, tener ,.. ]



5- **MERGE_AS_ID**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[da, igual]]   B= [que, pueda, tener ,.. ]



6- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [que, pueda, tener ,.. ]



7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [que]   B= [pueda, tener, repercusión ,.. ]



8- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [pueda, tener, repercusión ,.. ]



9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [pueda]   B= [tener, repercusión, dentro ,.. ]



10- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [tener, repercusión, dentro ,.. ]



11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [tener]   B= [repercusión, dentro, de ,.. ]



12- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [tener, repercusión]   B= [dentro, de, el ,.. ]



13- **MERGE_AS_LVC**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[tener, repercusión]]   B= [dentro, de, el ,.. ]



14- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [dentro, de, el ,.. ]



15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [dentro]   B= [de, el, campo ,.. ]



16- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [de, el, campo ,.. ]



17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [de]   B= [el, campo, , ,.. ]



18- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [el, campo, , ,.. ]



19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [el]   B= [campo, ,, pero ,.. ]



20- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [campo, ,, pero ,.. ]



21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [campo]   B= [,, pero, estoy ,.. ]



22- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, pero, estoy ,.. ]



23- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [pero, estoy, en ,.. ]



24- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [pero, estoy, en ,.. ]



25- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [pero]   B= [estoy, en, el ,.. ]



26- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [estoy, en, el ,.. ]



27- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [estoy]   B= [en, el, deber ,.. ]



28- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [estoy, en]   B= [el, deber, de ,.. ]



29- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [estoy, en, el]   B= [deber, de, avisar ,.. ]



30- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [estoy, en]   B= [deber, de, avisar ,.. ]



31- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [estoy, en, deber]   B= [de, avisar, lo ,.. ]



32- **WHITE_MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [estoy, [en, deber]]   B= [de, avisar, lo ,.. ]



33- **MERGE_AS_LVC**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[estoy, [en, deber]]]   B= [de, avisar, lo ,.. ]



34- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [de, avisar, lo ,.. ]



35- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [de]   B= [avisar, lo, " ,.. ]



36- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [avisar, lo, " ,.. ]



37- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [avisar]   B= [lo, ", , ,.. ]



38- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [lo, ", , ,.. ]



39- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [lo]   B= [", ,, explicó ,.. ]



40- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [", ,, explicó ,.. ]



41- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= ["]   B= [,, explicó, ferreira ,.. ]



42- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, explicó, ferreira ,.. ]



43- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [explicó, ferreira, , ,.. ]



44- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [explicó, ferreira, , ,.. ]



45- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [explicó]   B= [ferreira, ,, quien ,.. ]



46- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ferreira, ,, quien ,.. ]



47- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ferreira]   B= [,, quien, confesó ,.. ]



48- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, quien, confesó ,.. ]



49- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [quien, confesó, que ,.. ]



50- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [quien, confesó, que ,.. ]



51- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [quien]   B= [confesó, que, el ,.. ]



52- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [confesó, que, el ,.. ]



53- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [confesó]   B= [que, el, árbitro ,.. ]



54- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [que, el, árbitro ,.. ]



55- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [que]   B= [el, árbitro, madrileño ,.. ]



56- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [el, árbitro, madrileño ,.. ]



57- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [el]   B= [árbitro, madrileño, no ,.. ]



58- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [árbitro, madrileño, no ,.. ]



59- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [árbitro]   B= [madrileño, no, le ,.. ]



60- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [madrileño, no, le ,.. ]



61- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [madrileño]   B= [no, le, trae ,.. ]



62- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [no, le, trae ,.. ]



63- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [no]   B= [le, trae, " ,.. ]



64- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [le, trae, " ,.. ]



65- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [le]   B= [trae, ", buenos ,.. ]



66- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [trae, ", buenos ,.. ]



67- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [trae]   B= [", buenos, recuerdos ,.. ]



68- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [trae, "]   B= [buenos, recuerdos, " ,.. ]



69- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [trae]   B= [buenos, recuerdos, " ,.. ]



70- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [trae, buenos]   B= [recuerdos, ", . ,.. ]



71- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [trae]   B= [recuerdos, ", . ,.. ]



72- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [trae, recuerdos]   B= [", . ,.. ]



73- **MERGE_AS_ID**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[trae, recuerdos]]   B= [", . ,.. ]



74- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [", . ,.. ]



75- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= ["]   B= [.]



76- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [.]



77- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [ ]



78- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

## Sentence No. 6 - 
el presidente de el principado , vicente alvarez areces , **se** **mostró** hoy **partidario** de que el psoe celebre antes de el verano un congreso en el que se elija una nueva ejecutiva y de dejar para más tarde el debate sobre los **cambios** que deben **introducir** se en el partido . 
### Existing MWEs: 
1- **se mostró** (IReflV), Embedded 

2- **se mostró partidario** (ID)

3- **cambios introducir** (ID)

black Merge Num : 0 Interleaving Num: 0


0- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [el, presidente, de ,.. ]



1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [el]   B= [presidente, de, el ,.. ]



2- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [presidente, de, el ,.. ]



3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [presidente]   B= [de, el, principado ,.. ]



4- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [de, el, principado ,.. ]



5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [de]   B= [el, principado, , ,.. ]



6- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [el, principado, , ,.. ]



7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [el]   B= [principado, ,, vicente ,.. ]



8- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [principado, ,, vicente ,.. ]



9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [principado]   B= [,, vicente, alvarez ,.. ]



10- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, vicente, alvarez ,.. ]



11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [vicente, alvarez, areces ,.. ]



12- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [vicente, alvarez, areces ,.. ]



13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [vicente]   B= [alvarez, areces, , ,.. ]



14- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [alvarez, areces, , ,.. ]



15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [alvarez]   B= [areces, ,, se ,.. ]



16- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [areces, ,, se ,.. ]



17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [areces]   B= [,, se, mostró ,.. ]



18- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, se, mostró ,.. ]



19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [se, mostró, hoy ,.. ]



20- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [se, mostró, hoy ,.. ]



21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [se]   B= [mostró, hoy, partidario ,.. ]



22- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [se, mostró]   B= [hoy, partidario, de ,.. ]



23- **MERGE_AS_IReflV**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[se, mostró]]   B= [hoy, partidario, de ,.. ]



24- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[se, mostró]  hoy]   B= [partidario, de, que ,.. ]



25- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[se, mostró]]   B= [partidario, de, que ,.. ]



26- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[se, mostró]  partidario]   B= [de, que, el ,.. ]



27- **MERGE_AS_ID**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[[se, mostró]  partidario]]   B= [de, que, el ,.. ]



28- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [de, que, el ,.. ]



29- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [de]   B= [que, el, psoe ,.. ]



30- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [que, el, psoe ,.. ]



31- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [que]   B= [el, psoe, celebre ,.. ]



32- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [el, psoe, celebre ,.. ]



33- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [el]   B= [psoe, celebre, antes ,.. ]



34- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [psoe, celebre, antes ,.. ]



35- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [psoe]   B= [celebre, antes, de ,.. ]



36- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [celebre, antes, de ,.. ]



37- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [celebre]   B= [antes, de, el ,.. ]



38- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [antes, de, el ,.. ]



39- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [antes]   B= [de, el, verano ,.. ]



40- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [de, el, verano ,.. ]



41- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [de]   B= [el, verano, un ,.. ]



42- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [el, verano, un ,.. ]



43- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [el]   B= [verano, un, congreso ,.. ]



44- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [verano, un, congreso ,.. ]



45- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [verano]   B= [un, congreso, en ,.. ]



46- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [un, congreso, en ,.. ]



47- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [un]   B= [congreso, en, el ,.. ]



48- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [congreso, en, el ,.. ]



49- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [congreso]   B= [en, el, que ,.. ]



50- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [en, el, que ,.. ]



51- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [en]   B= [el, que, se ,.. ]



52- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [el, que, se ,.. ]



53- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [el]   B= [que, se, elija ,.. ]



54- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [que, se, elija ,.. ]



55- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [que]   B= [se, elija, una ,.. ]



56- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [se, elija, una ,.. ]



57- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [se]   B= [elija, una, nueva ,.. ]



58- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [elija, una, nueva ,.. ]



59- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [elija]   B= [una, nueva, ejecutiva ,.. ]



60- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [una, nueva, ejecutiva ,.. ]



61- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [una]   B= [nueva, ejecutiva, y ,.. ]



62- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [nueva, ejecutiva, y ,.. ]



63- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [nueva]   B= [ejecutiva, y, de ,.. ]



64- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ejecutiva, y, de ,.. ]



65- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ejecutiva]   B= [y, de, dejar ,.. ]



66- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [y, de, dejar ,.. ]



67- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [y]   B= [de, dejar, para ,.. ]



68- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [de, dejar, para ,.. ]



69- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [de]   B= [dejar, para, más ,.. ]



70- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [dejar, para, más ,.. ]



71- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [dejar]   B= [para, más, tarde ,.. ]



72- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [para, más, tarde ,.. ]



73- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [para]   B= [más, tarde, el ,.. ]



74- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [más, tarde, el ,.. ]



75- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [más]   B= [tarde, el, debate ,.. ]



76- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [tarde, el, debate ,.. ]



77- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [tarde]   B= [el, debate, sobre ,.. ]



78- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [el, debate, sobre ,.. ]



79- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [el]   B= [debate, sobre, los ,.. ]



80- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [debate, sobre, los ,.. ]



81- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [debate]   B= [sobre, los, cambios ,.. ]



82- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [sobre, los, cambios ,.. ]



83- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [sobre]   B= [los, cambios, que ,.. ]



84- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [los, cambios, que ,.. ]



85- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [los]   B= [cambios, que, deben ,.. ]



86- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [cambios, que, deben ,.. ]



87- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [cambios]   B= [que, deben, introducir ,.. ]



88- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [cambios, que]   B= [deben, introducir, se ,.. ]



89- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [cambios]   B= [deben, introducir, se ,.. ]



90- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [cambios, deben]   B= [introducir, se, en ,.. ]



91- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [cambios]   B= [introducir, se, en ,.. ]



92- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [cambios, introducir]   B= [se, en, el ,.. ]



93- **MERGE_AS_ID**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[cambios, introducir]]   B= [se, en, el ,.. ]



94- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [se, en, el ,.. ]



95- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [se]   B= [en, el, partido ,.. ]



96- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [en, el, partido ,.. ]



97- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [en]   B= [el, partido, . ,.. ]



98- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [el, partido, . ,.. ]



99- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [el]   B= [partido, . ,.. ]



100- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [partido, . ,.. ]



101- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [partido]   B= [.]



102- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [.]



103- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [ ]



104- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

## Sentence No. 436 - 
cuando abandonaban el palacio de la zarzuela en dirección a la capital , **tuvieron** también **ocasión** de ver a los reyes , que regresaban a su residencia desde el pardo tras haber **dado** la **bienvenida** a el presidente argentino , fernando de la rúa , y quienes mandaron detener su coche y **se** **bajaron** a saludar los a todos , explicó a efe iker echevarría . 
### Existing MWEs: 
1- **tuvieron ocasión** (LVC)

2- **dado bienvenida** (LVC)

3- **se bajaron** (IReflV)

black Merge Num : 0 Interleaving Num: 0


0- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [cuando, abandonaban, el ,.. ]



1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [cuando]   B= [abandonaban, el, palacio ,.. ]



2- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [abandonaban, el, palacio ,.. ]



3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [abandonaban]   B= [el, palacio, de ,.. ]



4- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [el, palacio, de ,.. ]



5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [el]   B= [palacio, de, la ,.. ]



6- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [palacio, de, la ,.. ]



7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [palacio]   B= [de, la, zarzuela ,.. ]



8- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [de, la, zarzuela ,.. ]



9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [de]   B= [la, zarzuela, en ,.. ]



10- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [la, zarzuela, en ,.. ]



11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [la]   B= [zarzuela, en, dirección ,.. ]



12- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [zarzuela, en, dirección ,.. ]



13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [zarzuela]   B= [en, dirección, a ,.. ]



14- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [en, dirección, a ,.. ]



15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [en]   B= [dirección, a, la ,.. ]



16- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [dirección, a, la ,.. ]



17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [dirección]   B= [a, la, capital ,.. ]



18- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [a, la, capital ,.. ]



19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [a]   B= [la, capital, , ,.. ]



20- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [la, capital, , ,.. ]



21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [la]   B= [capital, ,, tuvieron ,.. ]



22- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [capital, ,, tuvieron ,.. ]



23- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [capital]   B= [,, tuvieron, también ,.. ]



24- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, tuvieron, también ,.. ]



25- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [tuvieron, también, ocasión ,.. ]



26- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [tuvieron, también, ocasión ,.. ]



27- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [tuvieron]   B= [también, ocasión, de ,.. ]



28- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [tuvieron, también]   B= [ocasión, de, ver ,.. ]



29- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [tuvieron]   B= [ocasión, de, ver ,.. ]



30- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [tuvieron, ocasión]   B= [de, ver, a ,.. ]



31- **MERGE_AS_LVC**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[tuvieron, ocasión]]   B= [de, ver, a ,.. ]



32- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [de, ver, a ,.. ]



33- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [de]   B= [ver, a, los ,.. ]



34- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ver, a, los ,.. ]



35- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ver]   B= [a, los, reyes ,.. ]



36- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [a, los, reyes ,.. ]



37- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [a]   B= [los, reyes, , ,.. ]



38- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [los, reyes, , ,.. ]



39- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [los]   B= [reyes, ,, que ,.. ]



40- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [reyes, ,, que ,.. ]



41- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [reyes]   B= [,, que, regresaban ,.. ]



42- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, que, regresaban ,.. ]



43- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [que, regresaban, a ,.. ]



44- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [que, regresaban, a ,.. ]



45- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [que]   B= [regresaban, a, su ,.. ]



46- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [regresaban, a, su ,.. ]



47- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [regresaban]   B= [a, su, residencia ,.. ]



48- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [a, su, residencia ,.. ]



49- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [a]   B= [su, residencia, desde ,.. ]



50- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [su, residencia, desde ,.. ]



51- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [su]   B= [residencia, desde, el ,.. ]



52- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [residencia, desde, el ,.. ]



53- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [residencia]   B= [desde, el, pardo ,.. ]



54- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [desde, el, pardo ,.. ]



55- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [desde]   B= [el, pardo, tras ,.. ]



56- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [el, pardo, tras ,.. ]



57- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [el]   B= [pardo, tras, haber ,.. ]



58- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [pardo, tras, haber ,.. ]



59- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [pardo]   B= [tras, haber, dado ,.. ]



60- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [tras, haber, dado ,.. ]



61- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [tras]   B= [haber, dado, la ,.. ]



62- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [haber, dado, la ,.. ]



63- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [haber]   B= [dado, la, bienvenida ,.. ]



64- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [dado, la, bienvenida ,.. ]



65- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [dado]   B= [la, bienvenida, a ,.. ]



66- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [dado, la]   B= [bienvenida, a, el ,.. ]



67- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [dado]   B= [bienvenida, a, el ,.. ]



68- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [dado, bienvenida]   B= [a, el, presidente ,.. ]



69- **MERGE_AS_LVC**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[dado, bienvenida]]   B= [a, el, presidente ,.. ]



70- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [a, el, presidente ,.. ]



71- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [a]   B= [el, presidente, argentino ,.. ]



72- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [el, presidente, argentino ,.. ]



73- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [el]   B= [presidente, argentino, , ,.. ]



74- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [presidente, argentino, , ,.. ]



75- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [presidente]   B= [argentino, ,, fernando ,.. ]



76- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [argentino, ,, fernando ,.. ]



77- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [argentino]   B= [,, fernando, de ,.. ]



78- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, fernando, de ,.. ]



79- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [fernando, de, la ,.. ]



80- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [fernando, de, la ,.. ]



81- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [fernando]   B= [de, la, rúa ,.. ]



82- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [de, la, rúa ,.. ]



83- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [de]   B= [la, rúa, , ,.. ]



84- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [la, rúa, , ,.. ]



85- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [la]   B= [rúa, ,, y ,.. ]



86- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [rúa, ,, y ,.. ]



87- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [rúa]   B= [,, y, quienes ,.. ]



88- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, y, quienes ,.. ]



89- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [y, quienes, mandaron ,.. ]



90- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [y, quienes, mandaron ,.. ]



91- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [y]   B= [quienes, mandaron, detener ,.. ]



92- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [quienes, mandaron, detener ,.. ]



93- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [quienes]   B= [mandaron, detener, su ,.. ]



94- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [mandaron, detener, su ,.. ]



95- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [mandaron]   B= [detener, su, coche ,.. ]



96- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [detener, su, coche ,.. ]



97- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [detener]   B= [su, coche, y ,.. ]



98- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [su, coche, y ,.. ]



99- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [su]   B= [coche, y, se ,.. ]



100- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [coche, y, se ,.. ]



101- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [coche]   B= [y, se, bajaron ,.. ]



102- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [y, se, bajaron ,.. ]



103- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [y]   B= [se, bajaron, a ,.. ]



104- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [se, bajaron, a ,.. ]



105- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [se]   B= [bajaron, a, saludar ,.. ]



106- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [se, bajaron]   B= [a, saludar, los ,.. ]



107- **MERGE_AS_IReflV**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[se, bajaron]]   B= [a, saludar, los ,.. ]



108- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [a, saludar, los ,.. ]



109- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [a]   B= [saludar, los, a ,.. ]



110- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [saludar, los, a ,.. ]



111- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [saludar]   B= [los, a, todos ,.. ]



112- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [los, a, todos ,.. ]



113- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [los]   B= [a, todos, , ,.. ]



114- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [a, todos, , ,.. ]



115- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [a]   B= [todos, ,, explicó ,.. ]



116- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [todos, ,, explicó ,.. ]



117- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [todos]   B= [,, explicó, a ,.. ]



118- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, explicó, a ,.. ]



119- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [explicó, a, efe ,.. ]



120- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [explicó, a, efe ,.. ]



121- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [explicó]   B= [a, efe, iker ,.. ]



122- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [a, efe, iker ,.. ]



123- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [a]   B= [efe, iker, echevarría ,.. ]



124- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [efe, iker, echevarría ,.. ]



125- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [efe]   B= [iker, echevarría, . ,.. ]



126- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [iker, echevarría, . ,.. ]



127- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [iker]   B= [echevarría, . ,.. ]



128- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [echevarría, . ,.. ]



129- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [echevarría]   B= [.]



130- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [.]



131- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [ ]



132- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

## Sentence No. 921 - 
acusado en múltiples ocasiones por sus adversarios de " **hacer** **trampas** " para ganar las elecciones y denunciado por admitir las violaciones a los derechos humanos y la corrupción administrativa , balaguer , sin embargo , **está** **en** **la** **mira** de sus adversarios , quienes **se** **cuidan** de no tocar lo " ni con el pétalo de una rosa " . 
### Existing MWEs: 
1- **hacer trampas** (LVC)

2- **está en la mira** (ID)

3- **se cuidan** (IReflV)

black Merge Num : 0 Interleaving Num: 0


0- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [acusado, en, múltiples ,.. ]



1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [acusado]   B= [en, múltiples, ocasiones ,.. ]



2- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [en, múltiples, ocasiones ,.. ]



3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [en]   B= [múltiples, ocasiones, por ,.. ]



4- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [múltiples, ocasiones, por ,.. ]



5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [múltiples]   B= [ocasiones, por, sus ,.. ]



6- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ocasiones, por, sus ,.. ]



7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ocasiones]   B= [por, sus, adversarios ,.. ]



8- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [por, sus, adversarios ,.. ]



9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [por]   B= [sus, adversarios, de ,.. ]



10- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [sus, adversarios, de ,.. ]



11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [sus]   B= [adversarios, de, " ,.. ]



12- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [adversarios, de, " ,.. ]



13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [adversarios]   B= [de, ", hacer ,.. ]



14- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [de, ", hacer ,.. ]



15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [de]   B= [", hacer, trampas ,.. ]



16- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [", hacer, trampas ,.. ]



17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= ["]   B= [hacer, trampas, " ,.. ]



18- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [hacer, trampas, " ,.. ]



19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [hacer]   B= [trampas, ", para ,.. ]



20- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [hacer, trampas]   B= [", para, ganar ,.. ]



21- **MERGE_AS_LVC**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[hacer, trampas]]   B= [", para, ganar ,.. ]



22- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [", para, ganar ,.. ]



23- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= ["]   B= [para, ganar, las ,.. ]



24- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [para, ganar, las ,.. ]



25- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [para]   B= [ganar, las, elecciones ,.. ]



26- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ganar, las, elecciones ,.. ]



27- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ganar]   B= [las, elecciones, y ,.. ]



28- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [las, elecciones, y ,.. ]



29- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [las]   B= [elecciones, y, denunciado ,.. ]



30- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [elecciones, y, denunciado ,.. ]



31- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [elecciones]   B= [y, denunciado, por ,.. ]



32- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [y, denunciado, por ,.. ]



33- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [y]   B= [denunciado, por, admitir ,.. ]



34- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [denunciado, por, admitir ,.. ]



35- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [denunciado]   B= [por, admitir, las ,.. ]



36- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [por, admitir, las ,.. ]



37- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [por]   B= [admitir, las, violaciones ,.. ]



38- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [admitir, las, violaciones ,.. ]



39- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [admitir]   B= [las, violaciones, a ,.. ]



40- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [las, violaciones, a ,.. ]



41- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [las]   B= [violaciones, a, los ,.. ]



42- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [violaciones, a, los ,.. ]



43- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [violaciones]   B= [a, los, derechos ,.. ]



44- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [a, los, derechos ,.. ]



45- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [a]   B= [los, derechos, humanos ,.. ]



46- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [los, derechos, humanos ,.. ]



47- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [los]   B= [derechos, humanos, y ,.. ]



48- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [derechos, humanos, y ,.. ]



49- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [derechos]   B= [humanos, y, la ,.. ]



50- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [humanos, y, la ,.. ]



51- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [humanos]   B= [y, la, corrupción ,.. ]



52- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [y, la, corrupción ,.. ]



53- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [y]   B= [la, corrupción, administrativa ,.. ]



54- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [la, corrupción, administrativa ,.. ]



55- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [la]   B= [corrupción, administrativa, , ,.. ]



56- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [corrupción, administrativa, , ,.. ]



57- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [corrupción]   B= [administrativa, ,, balaguer ,.. ]



58- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [administrativa, ,, balaguer ,.. ]



59- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [administrativa]   B= [,, balaguer, , ,.. ]



60- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, balaguer, , ,.. ]



61- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [balaguer, ,, sin ,.. ]



62- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [balaguer, ,, sin ,.. ]



63- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [balaguer]   B= [,, sin, embargo ,.. ]



64- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, sin, embargo ,.. ]



65- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [sin, embargo, , ,.. ]



66- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [sin, embargo, , ,.. ]



67- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [sin]   B= [embargo, ,, está ,.. ]



68- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [embargo, ,, está ,.. ]



69- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [embargo]   B= [,, está, en ,.. ]



70- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, está, en ,.. ]



71- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [está, en, la ,.. ]



72- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [está, en, la ,.. ]



73- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [está]   B= [en, la, mira ,.. ]



74- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [está, en]   B= [la, mira, de ,.. ]



75- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [está, en, la]   B= [mira, de, sus ,.. ]



76- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [está, en, la, mira]   B= [de, sus, adversarios ,.. ]



77- **WHITE_MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [está, en, [la, mira]]   B= [de, sus, adversarios ,.. ]



78- **WHITE_MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [está, [en, [la, mira]]]   B= [de, sus, adversarios ,.. ]



79- **MERGE_AS_ID**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[está, [en, [la, mira]]]]   B= [de, sus, adversarios ,.. ]



80- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [de, sus, adversarios ,.. ]



81- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [de]   B= [sus, adversarios, , ,.. ]



82- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [sus, adversarios, , ,.. ]



83- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [sus]   B= [adversarios, ,, quienes ,.. ]



84- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [adversarios, ,, quienes ,.. ]



85- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [adversarios]   B= [,, quienes, se ,.. ]



86- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, quienes, se ,.. ]



87- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [quienes, se, cuidan ,.. ]



88- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [quienes, se, cuidan ,.. ]



89- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [quienes]   B= [se, cuidan, de ,.. ]



90- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [se, cuidan, de ,.. ]



91- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [se]   B= [cuidan, de, no ,.. ]



92- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [se, cuidan]   B= [de, no, tocar ,.. ]



93- **MERGE_AS_IReflV**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[se, cuidan]]   B= [de, no, tocar ,.. ]



94- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [de, no, tocar ,.. ]



95- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [de]   B= [no, tocar, lo ,.. ]



96- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [no, tocar, lo ,.. ]



97- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [no]   B= [tocar, lo, " ,.. ]



98- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [tocar, lo, " ,.. ]



99- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [tocar]   B= [lo, ", ni ,.. ]



100- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [lo, ", ni ,.. ]



101- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [lo]   B= [", ni, con ,.. ]



102- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [", ni, con ,.. ]



103- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= ["]   B= [ni, con, el ,.. ]



104- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ni, con, el ,.. ]



105- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ni]   B= [con, el, pétalo ,.. ]



106- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [con, el, pétalo ,.. ]



107- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [con]   B= [el, pétalo, de ,.. ]



108- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [el, pétalo, de ,.. ]



109- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [el]   B= [pétalo, de, una ,.. ]



110- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [pétalo, de, una ,.. ]



111- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [pétalo]   B= [de, una, rosa ,.. ]



112- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [de, una, rosa ,.. ]



113- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [de]   B= [una, rosa, " ,.. ]



114- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [una, rosa, " ,.. ]



115- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [una]   B= [rosa, ", . ,.. ]



116- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [rosa, ", . ,.. ]



117- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [rosa]   B= [", . ,.. ]



118- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [", . ,.. ]



119- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= ["]   B= [.]



120- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [.]



121- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [ ]



122- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

## Sentence No. 944 - 
también **se** **mostró** **partidario** de aplicar el denominado " modelo regata " , que **da** **prioridad** de entrada a aquellos países que " mejor están preparados " por encima de grupos preseleccionados . 
### Existing MWEs: 
2- **se mostró** (IReflV), Embedded 

3- **se mostró partidario** (ID)

1- **da prioridad** (LVC)

black Merge Num : 0 Interleaving Num: 0


0- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [también, se, mostró ,.. ]



1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [también]   B= [se, mostró, partidario ,.. ]



2- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [se, mostró, partidario ,.. ]



3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [se]   B= [mostró, partidario, de ,.. ]



4- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [se, mostró]   B= [partidario, de, aplicar ,.. ]



5- **MERGE_AS_IReflV**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[se, mostró]]   B= [partidario, de, aplicar ,.. ]



6- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[se, mostró]  partidario]   B= [de, aplicar, el ,.. ]



7- **MERGE_AS_ID**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[[se, mostró]  partidario]]   B= [de, aplicar, el ,.. ]



8- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [de, aplicar, el ,.. ]



9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [de]   B= [aplicar, el, denominado ,.. ]



10- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [aplicar, el, denominado ,.. ]



11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [aplicar]   B= [el, denominado, " ,.. ]



12- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [el, denominado, " ,.. ]



13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [el]   B= [denominado, ", modelo ,.. ]



14- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [denominado, ", modelo ,.. ]



15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [denominado]   B= [", modelo, regata ,.. ]



16- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [", modelo, regata ,.. ]



17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= ["]   B= [modelo, regata, " ,.. ]



18- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [modelo, regata, " ,.. ]



19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [modelo]   B= [regata, ", , ,.. ]



20- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [regata, ", , ,.. ]



21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [regata]   B= [", ,, que ,.. ]



22- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [", ,, que ,.. ]



23- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= ["]   B= [,, que, da ,.. ]



24- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, que, da ,.. ]



25- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [que, da, prioridad ,.. ]



26- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [que, da, prioridad ,.. ]



27- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [que]   B= [da, prioridad, de ,.. ]



28- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [da, prioridad, de ,.. ]



29- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [da]   B= [prioridad, de, entrada ,.. ]



30- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [da, prioridad]   B= [de, entrada, a ,.. ]



31- **MERGE_AS_LVC**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[da, prioridad]]   B= [de, entrada, a ,.. ]



32- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [de, entrada, a ,.. ]



33- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [de]   B= [entrada, a, aquellos ,.. ]



34- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [entrada, a, aquellos ,.. ]



35- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [entrada]   B= [a, aquellos, países ,.. ]



36- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [a, aquellos, países ,.. ]



37- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [a]   B= [aquellos, países, que ,.. ]



38- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [aquellos, países, que ,.. ]



39- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [aquellos]   B= [países, que, " ,.. ]



40- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [países, que, " ,.. ]



41- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [países]   B= [que, ", mejor ,.. ]



42- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [que, ", mejor ,.. ]



43- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [que]   B= [", mejor, están ,.. ]



44- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [", mejor, están ,.. ]



45- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= ["]   B= [mejor, están, preparados ,.. ]



46- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [mejor, están, preparados ,.. ]



47- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [mejor]   B= [están, preparados, " ,.. ]



48- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [están, preparados, " ,.. ]



49- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [están]   B= [preparados, ", por ,.. ]



50- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [preparados, ", por ,.. ]



51- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [preparados]   B= [", por, encima ,.. ]



52- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [", por, encima ,.. ]



53- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= ["]   B= [por, encima, de ,.. ]



54- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [por, encima, de ,.. ]



55- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [por]   B= [encima, de, grupos ,.. ]



56- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [encima, de, grupos ,.. ]



57- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [encima]   B= [de, grupos, preseleccionados ,.. ]



58- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [de, grupos, preseleccionados ,.. ]



59- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [de]   B= [grupos, preseleccionados, . ,.. ]



60- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [grupos, preseleccionados, . ,.. ]



61- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [grupos]   B= [preseleccionados, . ,.. ]



62- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [preseleccionados, . ,.. ]



63- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [preseleccionados]   B= [.]



64- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [.]



65- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [ ]



66- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

