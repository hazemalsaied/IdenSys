## Sentence No. 408 - 
Keletą metų stypčiojusi vietoje , Prancūzijos automobilių rinka , kuri yra antra pagal dydį Europoje po Vokietijos , 2015 m . šovė į viršų .
### Existing MWEs: 
1- **stypčiojusi vietoje** (ID)
2- **šovė į viršų** (ID)



0- &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Keletą, metų, stypčiojusi ,.. ]

B0Token: Keletą, B0_LastThreeLetters: tą, B1Token: metų, B1_LastThreeLetters: tų, 

1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Keletą]   B= [metų, stypčiojusi, vietoje ,.. ]

B0Token: metų, B0_LastThreeLetters: tų, B1Token: stypčiojusi, B1_LastThreeLetters: usi, S0B0Distance: 1, S0B0Token: Keletą_metų, S0B1Token: Keletą_stypčiojusi, S0B2Token: Keletą_vietoje, S0Token: Keletą, S0_LastThreeLetters: tą, StackLength: 1, 

2- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [metų, stypčiojusi, vietoje ,.. ]

B0Token: metų, B0_LastThreeLetters: tų, B1Token: stypčiojusi, B1_LastThreeLetters: usi, transitionHistoryLength1: 0, 

3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [metų]   B= [stypčiojusi, vietoje, , ,.. ]

B0Token: stypčiojusi, B0_LastThreeLetters: usi, B1Token: vietoje, B1_LastThreeLetters: oje, S0B0Distance: 1, S0B0Token: metų_stypčiojusi, S0B1Token: metų_vietoje, S0B2Token: metų_,, S0Token: metų, S0_LastThreeLetters: tų, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, 

4- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [stypčiojusi, vietoje, , ,.. ]

B0Token: stypčiojusi, B0_LastThreeLetters: usi, B1Token: vietoje, B1_LastThreeLetters: oje, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [stypčiojusi]   B= [vietoje, ,, Prancūzijos ,.. ]

B0Token: vietoje, B0_LastThreeLetters: oje, B1Token: ,, B1_LastThreeLetters: ,, S0B0Distance: 1, S0B0Token: stypčiojusi_vietoje, S0B1Token: stypčiojusi_,, S0B2Token: stypčiojusi_Prancūzijos, S0Token: stypčiojusi, S0_LastThreeLetters: usi, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

6- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [stypčiojusi, vietoje]   B= [,, Prancūzijos, automobilių ,.. ]

B0Token: ,, B0_LastThreeLetters: ,, B1Token: Prancūzijos, B1_LastThreeLetters: jos, S0B0Distance: 1, S0B0Token: vietoje_,, S0B1Token: vietoje_Prancūzijos, S0B2Token: vietoje_automobilių, S0S1Distance: 1, S0Token: vietoje, S0_LastThreeLetters: oje, S1B0Token: stypčiojusi_,, S1S0B0Token: stypčiojusi_vietoje_,, S1S0Token: stypčiojusi_vietoje, S1Token: stypčiojusi, S1_LastThreeLetters: usi, StackLength: 2, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

7- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[stypčiojusi, vietoje]]   B= [,, Prancūzijos, automobilių ,.. ]

B0Token: ,, B0_LastThreeLetters: ,, B1Token: Prancūzijos, B1_LastThreeLetters: jos, S0B0Distance: 1, S0B0Token: stypčiojusi_vietoje_,, S0B1Token: stypčiojusi_vietoje_Prancūzijos, S0B2Token: stypčiojusi_vietoje_automobilių, S0Token: stypčiojusi_vietoje, StackLength: 1, transitionHistoryLength1: 0, transitionHistoryLength2: 00, transitionHistoryLength3: 002, 

8- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, Prancūzijos, automobilių ,.. ]

B0Token: ,, B0_LastThreeLetters: ,, B1Token: Prancūzijos, B1_LastThreeLetters: jos, transitionHistoryLength1: 1, transitionHistoryLength2: 10, transitionHistoryLength3: 100, 

9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [Prancūzijos, automobilių, rinka ,.. ]

B0Token: Prancūzijos, B0_LastThreeLetters: jos, B1Token: automobilių, B1_LastThreeLetters: ių, S0B0Distance: 1, S0B0Token: ,_Prancūzijos, S0B1Token: ,_automobilių, S0B2Token: ,_rinka, S0Token: ,, S0_LastThreeLetters: ,, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 21, transitionHistoryLength3: 210, 

10- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Prancūzijos, automobilių, rinka ,.. ]

B0Token: Prancūzijos, B0_LastThreeLetters: jos, B1Token: automobilių, B1_LastThreeLetters: ių, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 021, 

11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Prancūzijos]   B= [automobilių, rinka, , ,.. ]

B0Token: automobilių, B0_LastThreeLetters: ių, B1Token: rinka, B1_LastThreeLetters: nka, S0B0Distance: 1, S0B0Token: Prancūzijos_automobilių, S0B1Token: Prancūzijos_rinka, S0B2Token: Prancūzijos_,, S0Token: Prancūzijos, S0_LastThreeLetters: jos, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

12- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [automobilių, rinka, , ,.. ]

B0Token: automobilių, B0_LastThreeLetters: ių, B1Token: rinka, B1_LastThreeLetters: nka, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [automobilių]   B= [rinka, ,, kuri ,.. ]

B0Token: rinka, B0_LastThreeLetters: nka, B1Token: ,, B1_LastThreeLetters: ,, S0B0Distance: 1, S0B0Token: automobilių_rinka, S0B1Token: automobilių_,, S0B2Token: automobilių_kuri, S0Token: automobilių, S0_LastThreeLetters: ių, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

14- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [rinka, ,, kuri ,.. ]

B0Token: rinka, B0_LastThreeLetters: nka, B1Token: ,, B1_LastThreeLetters: ,, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [rinka]   B= [,, kuri, yra ,.. ]

B0Token: ,, B0_LastThreeLetters: ,, B1Token: kuri, B1_LastThreeLetters: uri, S0B0Distance: 1, S0B0Token: rinka_,, S0B1Token: rinka_kuri, S0B2Token: rinka_yra, S0Token: rinka, S0_LastThreeLetters: nka, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

16- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, kuri, yra ,.. ]

B0Token: ,, B0_LastThreeLetters: ,, B1Token: kuri, B1_LastThreeLetters: uri, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [kuri, yra, antra ,.. ]

B0Token: kuri, B0_LastThreeLetters: uri, B1Token: yra, B1_LastThreeLetters: yra, S0B0Distance: 1, S0B0Token: ,_kuri, S0B1Token: ,_yra, S0B2Token: ,_antra, S0Token: ,, S0_LastThreeLetters: ,, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

18- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [kuri, yra, antra ,.. ]

B0Token: kuri, B0_LastThreeLetters: uri, B1Token: yra, B1_LastThreeLetters: yra, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [kuri]   B= [yra, antra, pagal ,.. ]

B0Token: yra, B0_LastThreeLetters: yra, B1Token: antra, B1_LastThreeLetters: tra, S0B0Distance: 1, S0B0Token: kuri_yra, S0B1Token: kuri_antra, S0B2Token: kuri_pagal, S0Token: kuri, S0_LastThreeLetters: uri, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

20- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [yra, antra, pagal ,.. ]

B0Token: yra, B0_LastThreeLetters: yra, B1Token: antra, B1_LastThreeLetters: tra, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [yra]   B= [antra, pagal, dydį ,.. ]

B0Token: antra, B0_LastThreeLetters: tra, B1Token: pagal, B1_LastThreeLetters: gal, S0B0Distance: 1, S0B0Token: yra_antra, S0B1Token: yra_pagal, S0B2Token: yra_dydį, S0Token: yra, S0_LastThreeLetters: yra, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

22- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [antra, pagal, dydį ,.. ]

B0Token: antra, B0_LastThreeLetters: tra, B1Token: pagal, B1_LastThreeLetters: gal, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

23- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [antra]   B= [pagal, dydį, Europoje ,.. ]

B0Token: pagal, B0_LastThreeLetters: gal, B1Token: dydį, B1_LastThreeLetters: dį, S0B0Distance: 1, S0B0Token: antra_pagal, S0B1Token: antra_dydį, S0B2Token: antra_Europoje, S0Token: antra, S0_LastThreeLetters: tra, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

24- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [pagal, dydį, Europoje ,.. ]

B0Token: pagal, B0_LastThreeLetters: gal, B1Token: dydį, B1_LastThreeLetters: dį, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

25- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [pagal]   B= [dydį, Europoje, po ,.. ]

B0Token: dydį, B0_LastThreeLetters: dį, B1Token: Europoje, B1_LastThreeLetters: oje, S0B0Distance: 1, S0B0Token: pagal_dydį, S0B1Token: pagal_Europoje, S0B2Token: pagal_po, S0Token: pagal, S0_LastThreeLetters: gal, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

26- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [dydį, Europoje, po ,.. ]

B0Token: dydį, B0_LastThreeLetters: dį, B1Token: Europoje, B1_LastThreeLetters: oje, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

27- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [dydį]   B= [Europoje, po, Vokietijos ,.. ]

B0Token: Europoje, B0_LastThreeLetters: oje, B1Token: po, B1_LastThreeLetters: po, S0B0Distance: 1, S0B0Token: dydį_Europoje, S0B1Token: dydį_po, S0B2Token: dydį_Vokietijos, S0Token: dydį, S0_LastThreeLetters: dį, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

28- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Europoje, po, Vokietijos ,.. ]

B0Token: Europoje, B0_LastThreeLetters: oje, B1Token: po, B1_LastThreeLetters: po, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

29- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Europoje]   B= [po, Vokietijos, , ,.. ]

B0Token: po, B0_LastThreeLetters: po, B1Token: Vokietijos, B1_LastThreeLetters: jos, S0B0Distance: 1, S0B0Token: Europoje_po, S0B1Token: Europoje_Vokietijos, S0B2Token: Europoje_,, S0Token: Europoje, S0_LastThreeLetters: oje, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

30- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [po, Vokietijos, , ,.. ]

B0Token: po, B0_LastThreeLetters: po, B1Token: Vokietijos, B1_LastThreeLetters: jos, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

31- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [po]   B= [Vokietijos, ,, 2015 ,.. ]

B0Token: Vokietijos, B0_LastThreeLetters: jos, B1Token: ,, B1_LastThreeLetters: ,, S0B0Distance: 1, S0B0Token: po_Vokietijos, S0B1Token: po_,, S0B2Token: po_2015, S0Token: po, S0_LastThreeLetters: po, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

32- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Vokietijos, ,, 2015 ,.. ]

B0Token: Vokietijos, B0_LastThreeLetters: jos, B1Token: ,, B1_LastThreeLetters: ,, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

33- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Vokietijos]   B= [,, 2015, m ,.. ]

B0Token: ,, B0_LastThreeLetters: ,, B1Token: 2015, B1_LastThreeLetters: 015, S0B0Distance: 1, S0B0Token: Vokietijos_,, S0B1Token: Vokietijos_2015, S0B2Token: Vokietijos_m, S0Token: Vokietijos, S0_LastThreeLetters: jos, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

34- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, 2015, m ,.. ]

B0Token: ,, B0_LastThreeLetters: ,, B1Token: 2015, B1_LastThreeLetters: 015, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

35- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [2015, m, . ,.. ]

B0Token: 2015, B0_LastThreeLetters: 015, B1Token: m, B1_LastThreeLetters: m, S0B0Distance: 1, S0B0Token: ,_2015, S0B1Token: ,_m, S0B2Token: ,_., S0Token: ,, S0_LastThreeLetters: ,, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

36- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [2015, m, . ,.. ]

B0Token: 2015, B0_LastThreeLetters: 015, B1Token: m, B1_LastThreeLetters: m, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

37- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [2015]   B= [m, ., šovė ,.. ]

B0Token: m, B0_LastThreeLetters: m, B1Token: ., B1_LastThreeLetters: ., S0B0Distance: 1, S0B0Token: 2015_m, S0B1Token: 2015_., S0B2Token: 2015_šovė, S0Token: 2015, S0_LastThreeLetters: 015, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

38- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [m, ., šovė ,.. ]

B0Token: m, B0_LastThreeLetters: m, B1Token: ., B1_LastThreeLetters: ., transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

39- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [m]   B= [., šovė, į ,.. ]

B0Token: ., B0_LastThreeLetters: ., B1Token: šovė, B1_LastThreeLetters: vė, S0B0Distance: 1, S0B0Token: m_., S0B1Token: m_šovė, S0B2Token: m_į, S0Token: m, S0_LastThreeLetters: m, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

40- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [., šovė, į ,.. ]

B0Token: ., B0_LastThreeLetters: ., B1Token: šovė, B1_LastThreeLetters: vė, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

41- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [šovė, į, viršų ,.. ]

B0Token: šovė, B0_LastThreeLetters: vė, B1Token: į, B1_LastThreeLetters: į, S0B0Distance: 1, S0B0Token: ._šovė, S0B1Token: ._į, S0B2Token: ._viršų, S0Token: ., S0_LastThreeLetters: ., StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

42- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [šovė, į, viršų ,.. ]

B0Token: šovė, B0_LastThreeLetters: vė, B1Token: į, B1_LastThreeLetters: į, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

43- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [šovė]   B= [į, viršų, . ,.. ]

B0Token: į, B0_LastThreeLetters: į, B1Token: viršų, B1_LastThreeLetters: �ų, S0B0Distance: 1, S0B0Token: šovė_į, S0B1Token: šovė_viršų, S0B2Token: šovė_., S0Token: šovė, S0_LastThreeLetters: vė, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

44- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [šovė, į]   B= [viršų, . ,.. ]

B0Token: viršų, B0_LastThreeLetters: �ų, B1Token: ., B1_LastThreeLetters: ., S0B0Distance: 1, S0B0Token: į_viršų, S0B1Token: į_., S0S1Distance: 1, S0Token: į, S0_LastThreeLetters: į, S1B0Token: šovė_viršų, S1S0B0Token: šovė_į_viršų, S1S0Token: šovė_į, S1Token: šovė, S1_LastThreeLetters: vė, StackLength: 2, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

45- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [šovė, į, viršų]   B= [.]

B0Token: ., B0_LastThreeLetters: ., S0B0Distance: 1, S0B0Token: viršų_., S0S1Distance: 1, S0Token: viršų, S0_LastThreeLetters: �ų, S1B0Token: į_., S1S0B0Token: į_viršų_., S1S0Token: į_viršų, S1Token: į, S1_LastThreeLetters: į, StackLength: 3, transitionHistoryLength1: 0, transitionHistoryLength2: 00, transitionHistoryLength3: 002, 

46- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [šovė, [į, viršų]]   B= [.]

B0Token: ., B0_LastThreeLetters: ., S0B0Distance: 1, S0B0Token: į_viršų_., S0Token: į_viršų, S1B0Token: šovė_., S1S0B0Token: šovė_į_viršų_., S1S0Token: šovė_į_viršų, S1Token: šovė, S1_LastThreeLetters: vė, StackLength: 2, transitionHistoryLength1: 0, transitionHistoryLength2: 00, transitionHistoryLength3: 000, 

47- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[šovė, [į, viršų]]]   B= [.]

B0Token: ., B0_LastThreeLetters: ., S0B0Distance: 1, S0B0Token: šovė_į_viršų_., S0Token: šovė_į_viršų, StackLength: 1, transitionHistoryLength1: 1, transitionHistoryLength2: 10, transitionHistoryLength3: 100, 

48- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [.]

B0Token: ., B0_LastThreeLetters: ., transitionHistoryLength1: 1, transitionHistoryLength2: 11, transitionHistoryLength3: 110, 

49- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [ ]

S0Token: ., S0_LastThreeLetters: ., StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 21, transitionHistoryLength3: 211, 

50- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

## Sentence No. 1048 - 
Darome prielaidą , kad užsakovas gali priimti sprendimą ir nenaudoti šio korpuso tam , kad nugesintų gandų bangą ir numalšintų ažiotažą , kilusį tarp dalies gyventojų . “
### Existing MWEs: 
1- **priimti sprendimą** (LVC)
2- **nugesintų bangą** (ID)



0- &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Darome, prielaidą, , ,.. ]

B0Token: Darome, B0_LastThreeLetters: ome, B1Token: prielaidą, B1_LastThreeLetters: dą, 

1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Darome]   B= [prielaidą, ,, kad ,.. ]

B0Token: prielaidą, B0_LastThreeLetters: dą, B1Token: ,, B1_LastThreeLetters: ,, S0B0Distance: 1, S0B0Token: Darome_prielaidą, S0B1Token: Darome_,, S0B2Token: Darome_kad, S0Token: Darome, S0_LastThreeLetters: ome, StackLength: 1, 

2- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [prielaidą, ,, kad ,.. ]

B0Token: prielaidą, B0_LastThreeLetters: dą, B1Token: ,, B1_LastThreeLetters: ,, transitionHistoryLength1: 0, 

3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [prielaidą]   B= [,, kad, užsakovas ,.. ]

B0Token: ,, B0_LastThreeLetters: ,, B1Token: kad, B1_LastThreeLetters: kad, S0B0Distance: 1, S0B0Token: prielaidą_,, S0B1Token: prielaidą_kad, S0B2Token: prielaidą_užsakovas, S0Token: prielaidą, S0_LastThreeLetters: dą, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, 

4- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, kad, užsakovas ,.. ]

B0Token: ,, B0_LastThreeLetters: ,, B1Token: kad, B1_LastThreeLetters: kad, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [kad, užsakovas, gali ,.. ]

B0Token: kad, B0_LastThreeLetters: kad, B1Token: užsakovas, B1_LastThreeLetters: vas, S0B0Distance: 1, S0B0Token: ,_kad, S0B1Token: ,_užsakovas, S0B2Token: ,_gali, S0Token: ,, S0_LastThreeLetters: ,, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

6- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [kad, užsakovas, gali ,.. ]

B0Token: kad, B0_LastThreeLetters: kad, B1Token: užsakovas, B1_LastThreeLetters: vas, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [kad]   B= [užsakovas, gali, priimti ,.. ]

B0Token: užsakovas, B0_LastThreeLetters: vas, B1Token: gali, B1_LastThreeLetters: ali, S0B0Distance: 1, S0B0Token: kad_užsakovas, S0B1Token: kad_gali, S0B2Token: kad_priimti, S0Token: kad, S0_LastThreeLetters: kad, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

8- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [užsakovas, gali, priimti ,.. ]

B0Token: užsakovas, B0_LastThreeLetters: vas, B1Token: gali, B1_LastThreeLetters: ali, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [užsakovas]   B= [gali, priimti, sprendimą ,.. ]

B0Token: gali, B0_LastThreeLetters: ali, B1Token: priimti, B1_LastThreeLetters: mti, S0B0Distance: 1, S0B0Token: užsakovas_gali, S0B1Token: užsakovas_priimti, S0B2Token: užsakovas_sprendimą, S0Token: užsakovas, S0_LastThreeLetters: vas, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

10- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [gali, priimti, sprendimą ,.. ]

B0Token: gali, B0_LastThreeLetters: ali, B1Token: priimti, B1_LastThreeLetters: mti, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [gali]   B= [priimti, sprendimą, ir ,.. ]

B0Token: priimti, B0_LastThreeLetters: mti, B1Token: sprendimą, B1_LastThreeLetters: mą, S0B0Distance: 1, S0B0Token: gali_priimti, S0B1Token: gali_sprendimą, S0B2Token: gali_ir, S0Token: gali, S0_LastThreeLetters: ali, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

12- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [priimti, sprendimą, ir ,.. ]

B0Token: priimti, B0_LastThreeLetters: mti, B1Token: sprendimą, B1_LastThreeLetters: mą, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [priimti]   B= [sprendimą, ir, nenaudoti ,.. ]

B0Token: sprendimą, B0_LastThreeLetters: mą, B1Token: ir, B1_LastThreeLetters: ir, S0B0Distance: 1, S0B0Token: priimti_sprendimą, S0B1Token: priimti_ir, S0B2Token: priimti_nenaudoti, S0Token: priimti, S0_LastThreeLetters: mti, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

14- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [priimti, sprendimą]   B= [ir, nenaudoti, šio ,.. ]

B0Token: ir, B0_LastThreeLetters: ir, B1Token: nenaudoti, B1_LastThreeLetters: oti, S0B0Distance: 1, S0B0Token: sprendimą_ir, S0B1Token: sprendimą_nenaudoti, S0B2Token: sprendimą_šio, S0S1Distance: 1, S0Token: sprendimą, S0_LastThreeLetters: mą, S1B0Token: priimti_ir, S1S0B0Token: priimti_sprendimą_ir, S1S0Token: priimti_sprendimą, S1Token: priimti, S1_LastThreeLetters: mti, StackLength: 2, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

15- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[priimti, sprendimą]]   B= [ir, nenaudoti, šio ,.. ]

B0Token: ir, B0_LastThreeLetters: ir, B1Token: nenaudoti, B1_LastThreeLetters: oti, S0B0Distance: 1, S0B0Token: priimti_sprendimą_ir, S0B1Token: priimti_sprendimą_nenaudoti, S0B2Token: priimti_sprendimą_šio, S0Token: priimti_sprendimą, StackLength: 1, transitionHistoryLength1: 0, transitionHistoryLength2: 00, transitionHistoryLength3: 002, 

16- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ir, nenaudoti, šio ,.. ]

B0Token: ir, B0_LastThreeLetters: ir, B1Token: nenaudoti, B1_LastThreeLetters: oti, transitionHistoryLength1: 1, transitionHistoryLength2: 10, transitionHistoryLength3: 100, 

17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ir]   B= [nenaudoti, šio, korpuso ,.. ]

B0Token: nenaudoti, B0_LastThreeLetters: oti, B1Token: šio, B1_LastThreeLetters: �io, S0B0Distance: 1, S0B0Token: ir_nenaudoti, S0B1Token: ir_šio, S0B2Token: ir_korpuso, S0Token: ir, S0_LastThreeLetters: ir, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 21, transitionHistoryLength3: 210, 

18- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [nenaudoti, šio, korpuso ,.. ]

B0Token: nenaudoti, B0_LastThreeLetters: oti, B1Token: šio, B1_LastThreeLetters: �io, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 021, 

19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [nenaudoti]   B= [šio, korpuso, tam ,.. ]

B0Token: šio, B0_LastThreeLetters: �io, B1Token: korpuso, B1_LastThreeLetters: uso, S0B0Distance: 1, S0B0Token: nenaudoti_šio, S0B1Token: nenaudoti_korpuso, S0B2Token: nenaudoti_tam, S0Token: nenaudoti, S0_LastThreeLetters: oti, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

20- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [šio, korpuso, tam ,.. ]

B0Token: šio, B0_LastThreeLetters: �io, B1Token: korpuso, B1_LastThreeLetters: uso, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [šio]   B= [korpuso, tam, , ,.. ]

B0Token: korpuso, B0_LastThreeLetters: uso, B1Token: tam, B1_LastThreeLetters: tam, S0B0Distance: 1, S0B0Token: šio_korpuso, S0B1Token: šio_tam, S0B2Token: šio_,, S0Token: šio, S0_LastThreeLetters: �io, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

22- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [korpuso, tam, , ,.. ]

B0Token: korpuso, B0_LastThreeLetters: uso, B1Token: tam, B1_LastThreeLetters: tam, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

23- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [korpuso]   B= [tam, ,, kad ,.. ]

B0Token: tam, B0_LastThreeLetters: tam, B1Token: ,, B1_LastThreeLetters: ,, S0B0Distance: 1, S0B0Token: korpuso_tam, S0B1Token: korpuso_,, S0B2Token: korpuso_kad, S0Token: korpuso, S0_LastThreeLetters: uso, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

24- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [tam, ,, kad ,.. ]

B0Token: tam, B0_LastThreeLetters: tam, B1Token: ,, B1_LastThreeLetters: ,, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

25- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [tam]   B= [,, kad, nugesintų ,.. ]

B0Token: ,, B0_LastThreeLetters: ,, B1Token: kad, B1_LastThreeLetters: kad, S0B0Distance: 1, S0B0Token: tam_,, S0B1Token: tam_kad, S0B2Token: tam_nugesintų, S0Token: tam, S0_LastThreeLetters: tam, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

26- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, kad, nugesintų ,.. ]

B0Token: ,, B0_LastThreeLetters: ,, B1Token: kad, B1_LastThreeLetters: kad, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

27- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [kad, nugesintų, gandų ,.. ]

B0Token: kad, B0_LastThreeLetters: kad, B1Token: nugesintų, B1_LastThreeLetters: tų, S0B0Distance: 1, S0B0Token: ,_kad, S0B1Token: ,_nugesintų, S0B2Token: ,_gandų, S0Token: ,, S0_LastThreeLetters: ,, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

28- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [kad, nugesintų, gandų ,.. ]

B0Token: kad, B0_LastThreeLetters: kad, B1Token: nugesintų, B1_LastThreeLetters: tų, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

29- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [kad]   B= [nugesintų, gandų, bangą ,.. ]

B0Token: nugesintų, B0_LastThreeLetters: tų, B1Token: gandų, B1_LastThreeLetters: dų, S0B0Distance: 1, S0B0Token: kad_nugesintų, S0B1Token: kad_gandų, S0B2Token: kad_bangą, S0Token: kad, S0_LastThreeLetters: kad, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

30- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [nugesintų, gandų, bangą ,.. ]

B0Token: nugesintų, B0_LastThreeLetters: tų, B1Token: gandų, B1_LastThreeLetters: dų, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

31- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [nugesintų]   B= [gandų, bangą, ir ,.. ]

B0Token: gandų, B0_LastThreeLetters: dų, B1Token: bangą, B1_LastThreeLetters: gą, S0B0Distance: 1, S0B0Token: nugesintų_gandų, S0B1Token: nugesintų_bangą, S0B2Token: nugesintų_ir, S0Token: nugesintų, S0_LastThreeLetters: tų, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

32- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [nugesintų, gandų]   B= [bangą, ir, numalšintų ,.. ]

B0Token: bangą, B0_LastThreeLetters: gą, B1Token: ir, B1_LastThreeLetters: ir, S0B0Distance: 1, S0B0Token: gandų_bangą, S0B1Token: gandų_ir, S0B2Token: gandų_numalšintų, S0S1Distance: 1, S0Token: gandų, S0_LastThreeLetters: dų, S1B0Token: nugesintų_bangą, S1S0B0Token: nugesintų_gandų_bangą, S1S0Token: nugesintų_gandų, S1Token: nugesintų, S1_LastThreeLetters: tų, StackLength: 2, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

33- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [nugesintų]   B= [bangą, ir, numalšintų ,.. ]

B0Token: bangą, B0_LastThreeLetters: gą, B1Token: ir, B1_LastThreeLetters: ir, S0B0Distance: 2, S0B0Token: nugesintų_bangą, S0B1Token: nugesintų_ir, S0B2Token: nugesintų_numalšintų, S0Token: nugesintų, S0_LastThreeLetters: tų, StackLength: 1, transitionHistoryLength1: 0, transitionHistoryLength2: 00, transitionHistoryLength3: 002, 

34- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [nugesintų, bangą]   B= [ir, numalšintų, ažiotažą ,.. ]

B0Token: ir, B0_LastThreeLetters: ir, B1Token: numalšintų, B1_LastThreeLetters: tų, S0B0Distance: 1, S0B0Token: bangą_ir, S0B1Token: bangą_numalšintų, S0B2Token: bangą_ažiotažą, S0S1Distance: 2, S0Token: bangą, S0_LastThreeLetters: gą, S1B0Token: nugesintų_ir, S1S0B0Token: nugesintų_bangą_ir, S1S0Token: nugesintų_bangą, S1Token: nugesintų, S1_LastThreeLetters: tų, StackLength: 2, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 200, 

35- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[nugesintų, bangą]]   B= [ir, numalšintų, ažiotažą ,.. ]

B0Token: ir, B0_LastThreeLetters: ir, B1Token: numalšintų, B1_LastThreeLetters: tų, S0B0Distance: 1, S0B0Token: nugesintų_bangą_ir, S0B1Token: nugesintų_bangą_numalšintų, S0B2Token: nugesintų_bangą_ažiotažą, S0Token: nugesintų_bangą, StackLength: 1, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

36- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ir, numalšintų, ažiotažą ,.. ]

B0Token: ir, B0_LastThreeLetters: ir, B1Token: numalšintų, B1_LastThreeLetters: tų, transitionHistoryLength1: 1, transitionHistoryLength2: 10, transitionHistoryLength3: 102, 

37- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ir]   B= [numalšintų, ažiotažą, , ,.. ]

B0Token: numalšintų, B0_LastThreeLetters: tų, B1Token: ažiotažą, B1_LastThreeLetters: �ą, S0B0Distance: 1, S0B0Token: ir_numalšintų, S0B1Token: ir_ažiotažą, S0B2Token: ir_,, S0Token: ir, S0_LastThreeLetters: ir, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 21, transitionHistoryLength3: 210, 

38- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [numalšintų, ažiotažą, , ,.. ]

B0Token: numalšintų, B0_LastThreeLetters: tų, B1Token: ažiotažą, B1_LastThreeLetters: �ą, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 021, 

39- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [numalšintų]   B= [ažiotažą, ,, kilusį ,.. ]

B0Token: ažiotažą, B0_LastThreeLetters: �ą, B1Token: ,, B1_LastThreeLetters: ,, S0B0Distance: 1, S0B0Token: numalšintų_ažiotažą, S0B1Token: numalšintų_,, S0B2Token: numalšintų_kilusį, S0Token: numalšintų, S0_LastThreeLetters: tų, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

40- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ažiotažą, ,, kilusį ,.. ]

B0Token: ažiotažą, B0_LastThreeLetters: �ą, B1Token: ,, B1_LastThreeLetters: ,, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

41- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ažiotažą]   B= [,, kilusį, tarp ,.. ]

B0Token: ,, B0_LastThreeLetters: ,, B1Token: kilusį, B1_LastThreeLetters: sį, S0B0Distance: 1, S0B0Token: ažiotažą_,, S0B1Token: ažiotažą_kilusį, S0B2Token: ažiotažą_tarp, S0Token: ažiotažą, S0_LastThreeLetters: �ą, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

42- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, kilusį, tarp ,.. ]

B0Token: ,, B0_LastThreeLetters: ,, B1Token: kilusį, B1_LastThreeLetters: sį, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

43- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [kilusį, tarp, dalies ,.. ]

B0Token: kilusį, B0_LastThreeLetters: sį, B1Token: tarp, B1_LastThreeLetters: arp, S0B0Distance: 1, S0B0Token: ,_kilusį, S0B1Token: ,_tarp, S0B2Token: ,_dalies, S0Token: ,, S0_LastThreeLetters: ,, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

44- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [kilusį, tarp, dalies ,.. ]

B0Token: kilusį, B0_LastThreeLetters: sį, B1Token: tarp, B1_LastThreeLetters: arp, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

45- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [kilusį]   B= [tarp, dalies, gyventojų ,.. ]

B0Token: tarp, B0_LastThreeLetters: arp, B1Token: dalies, B1_LastThreeLetters: ies, S0B0Distance: 1, S0B0Token: kilusį_tarp, S0B1Token: kilusį_dalies, S0B2Token: kilusį_gyventojų, S0Token: kilusį, S0_LastThreeLetters: sį, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

46- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [tarp, dalies, gyventojų ,.. ]

B0Token: tarp, B0_LastThreeLetters: arp, B1Token: dalies, B1_LastThreeLetters: ies, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

47- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [tarp]   B= [dalies, gyventojų, . ,.. ]

B0Token: dalies, B0_LastThreeLetters: ies, B1Token: gyventojų, B1_LastThreeLetters: jų, S0B0Distance: 1, S0B0Token: tarp_dalies, S0B1Token: tarp_gyventojų, S0B2Token: tarp_., S0Token: tarp, S0_LastThreeLetters: arp, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

48- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [dalies, gyventojų, . ,.. ]

B0Token: dalies, B0_LastThreeLetters: ies, B1Token: gyventojų, B1_LastThreeLetters: jų, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

49- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [dalies]   B= [gyventojų, ., “ ,.. ]

B0Token: gyventojų, B0_LastThreeLetters: jų, B1Token: ., B1_LastThreeLetters: ., S0B0Distance: 1, S0B0Token: dalies_gyventojų, S0B1Token: dalies_., S0B2Token: dalies_“, S0Token: dalies, S0_LastThreeLetters: ies, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

50- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [gyventojų, ., “ ,.. ]

B0Token: gyventojų, B0_LastThreeLetters: jų, B1Token: ., B1_LastThreeLetters: ., transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

51- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [gyventojų]   B= [., “ ,.. ]

B0Token: ., B0_LastThreeLetters: ., B1Token: “, B1_LastThreeLetters: “, S0B0Distance: 1, S0B0Token: gyventojų_., S0B1Token: gyventojų_“, S0Token: gyventojų, S0_LastThreeLetters: jų, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

52- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [., “ ,.. ]

B0Token: ., B0_LastThreeLetters: ., B1Token: “, B1_LastThreeLetters: “, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

53- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [“]

B0Token: “, B0_LastThreeLetters: “, S0B0Distance: 1, S0B0Token: ._“, S0Token: ., S0_LastThreeLetters: ., StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

54- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [“]

B0Token: “, B0_LastThreeLetters: “, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

55- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [“]   B= [ ]

S0Token: “, S0_LastThreeLetters: “, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

56- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

## Sentence No. 1469 - 
Pasak A . Gališanskytės , D . Štraupaitė yra išreiškusi norą duoti parodymus , naudojasi šia teise , tačiau atvykti duoti parodymų turi ne kada nori , o kada kviečiama .
### Existing MWEs: 
1- **duoti parodymus** (LVC)
2- **duoti parodymų** (LVC)



0- &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Pasak, A, . ,.. ]

B0Token: Pasak, B0_LastThreeLetters: sak, B1Token: A, B1_LastThreeLetters: A, 

1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Pasak]   B= [A, ., Gališanskytės ,.. ]

B0Token: A, B0_LastThreeLetters: A, B1Token: ., B1_LastThreeLetters: ., S0B0Distance: 1, S0B0Token: Pasak_A, S0B1Token: Pasak_., S0B2Token: Pasak_Gališanskytės, S0Token: Pasak, S0_LastThreeLetters: sak, StackLength: 1, 

2- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [A, ., Gališanskytės ,.. ]

B0Token: A, B0_LastThreeLetters: A, B1Token: ., B1_LastThreeLetters: ., transitionHistoryLength1: 0, 

3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [A]   B= [., Gališanskytės, , ,.. ]

B0Token: ., B0_LastThreeLetters: ., B1Token: Gališanskytės, B1_LastThreeLetters: ės, S0B0Distance: 1, S0B0Token: A_., S0B1Token: A_Gališanskytės, S0B2Token: A_,, S0Token: A, S0_LastThreeLetters: A, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, 

4- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [., Gališanskytės, , ,.. ]

B0Token: ., B0_LastThreeLetters: ., B1Token: Gališanskytės, B1_LastThreeLetters: ės, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [Gališanskytės, ,, D ,.. ]

B0Token: Gališanskytės, B0_LastThreeLetters: ės, B1Token: ,, B1_LastThreeLetters: ,, S0B0Distance: 1, S0B0Token: ._Gališanskytės, S0B1Token: ._,, S0B2Token: ._D, S0Token: ., S0_LastThreeLetters: ., StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

6- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Gališanskytės, ,, D ,.. ]

B0Token: Gališanskytės, B0_LastThreeLetters: ės, B1Token: ,, B1_LastThreeLetters: ,, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Gališanskytės]   B= [,, D, . ,.. ]

B0Token: ,, B0_LastThreeLetters: ,, B1Token: D, B1_LastThreeLetters: D, S0B0Distance: 1, S0B0Token: Gališanskytės_,, S0B1Token: Gališanskytės_D, S0B2Token: Gališanskytės_., S0Token: Gališanskytės, S0_LastThreeLetters: ės, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

8- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, D, . ,.. ]

B0Token: ,, B0_LastThreeLetters: ,, B1Token: D, B1_LastThreeLetters: D, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [D, ., Štraupaitė ,.. ]

B0Token: D, B0_LastThreeLetters: D, B1Token: ., B1_LastThreeLetters: ., S0B0Distance: 1, S0B0Token: ,_D, S0B1Token: ,_., S0B2Token: ,_Štraupaitė, S0Token: ,, S0_LastThreeLetters: ,, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

10- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [D, ., Štraupaitė ,.. ]

B0Token: D, B0_LastThreeLetters: D, B1Token: ., B1_LastThreeLetters: ., transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [D]   B= [., Štraupaitė, yra ,.. ]

B0Token: ., B0_LastThreeLetters: ., B1Token: Štraupaitė, B1_LastThreeLetters: tė, S0B0Distance: 1, S0B0Token: D_., S0B1Token: D_Štraupaitė, S0B2Token: D_yra, S0Token: D, S0_LastThreeLetters: D, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

12- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [., Štraupaitė, yra ,.. ]

B0Token: ., B0_LastThreeLetters: ., B1Token: Štraupaitė, B1_LastThreeLetters: tė, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [Štraupaitė, yra, išreiškusi ,.. ]

B0Token: Štraupaitė, B0_LastThreeLetters: tė, B1Token: yra, B1_LastThreeLetters: yra, S0B0Distance: 1, S0B0Token: ._Štraupaitė, S0B1Token: ._yra, S0B2Token: ._išreiškusi, S0Token: ., S0_LastThreeLetters: ., StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

14- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Štraupaitė, yra, išreiškusi ,.. ]

B0Token: Štraupaitė, B0_LastThreeLetters: tė, B1Token: yra, B1_LastThreeLetters: yra, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Štraupaitė]   B= [yra, išreiškusi, norą ,.. ]

B0Token: yra, B0_LastThreeLetters: yra, B1Token: išreiškusi, B1_LastThreeLetters: usi, S0B0Distance: 1, S0B0Token: Štraupaitė_yra, S0B1Token: Štraupaitė_išreiškusi, S0B2Token: Štraupaitė_norą, S0Token: Štraupaitė, S0_LastThreeLetters: tė, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

16- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [yra, išreiškusi, norą ,.. ]

B0Token: yra, B0_LastThreeLetters: yra, B1Token: išreiškusi, B1_LastThreeLetters: usi, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [yra]   B= [išreiškusi, norą, duoti ,.. ]

B0Token: išreiškusi, B0_LastThreeLetters: usi, B1Token: norą, B1_LastThreeLetters: rą, S0B0Distance: 1, S0B0Token: yra_išreiškusi, S0B1Token: yra_norą, S0B2Token: yra_duoti, S0Token: yra, S0_LastThreeLetters: yra, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

18- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [išreiškusi, norą, duoti ,.. ]

B0Token: išreiškusi, B0_LastThreeLetters: usi, B1Token: norą, B1_LastThreeLetters: rą, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [išreiškusi]   B= [norą, duoti, parodymus ,.. ]

B0Token: norą, B0_LastThreeLetters: rą, B1Token: duoti, B1_LastThreeLetters: oti, S0B0Distance: 1, S0B0Token: išreiškusi_norą, S0B1Token: išreiškusi_duoti, S0B2Token: išreiškusi_parodymus, S0Token: išreiškusi, S0_LastThreeLetters: usi, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

20- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [norą, duoti, parodymus ,.. ]

B0Token: norą, B0_LastThreeLetters: rą, B1Token: duoti, B1_LastThreeLetters: oti, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [norą]   B= [duoti, parodymus, , ,.. ]

B0Token: duoti, B0_LastThreeLetters: oti, B1Token: parodymus, B1_LastThreeLetters: mus, S0B0Distance: 1, S0B0Token: norą_duoti, S0B1Token: norą_parodymus, S0B2Token: norą_,, S0Token: norą, S0_LastThreeLetters: rą, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

22- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [duoti, parodymus, , ,.. ]

B0Token: duoti, B0_LastThreeLetters: oti, B1Token: parodymus, B1_LastThreeLetters: mus, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

23- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [duoti]   B= [parodymus, ,, naudojasi ,.. ]

B0Token: parodymus, B0_LastThreeLetters: mus, B1Token: ,, B1_LastThreeLetters: ,, S0B0Distance: 1, S0B0Token: duoti_parodymus, S0B1Token: duoti_,, S0B2Token: duoti_naudojasi, S0Token: duoti, S0_LastThreeLetters: oti, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

24- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [duoti, parodymus]   B= [,, naudojasi, šia ,.. ]

B0Token: ,, B0_LastThreeLetters: ,, B1Token: naudojasi, B1_LastThreeLetters: asi, S0B0Distance: 1, S0B0Token: parodymus_,, S0B1Token: parodymus_naudojasi, S0B2Token: parodymus_šia, S0S1Distance: 1, S0Token: parodymus, S0_LastThreeLetters: mus, S1B0Token: duoti_,, S1S0B0Token: duoti_parodymus_,, S1S0Token: duoti_parodymus, S1Token: duoti, S1_LastThreeLetters: oti, StackLength: 2, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

25- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[duoti, parodymus]]   B= [,, naudojasi, šia ,.. ]

B0Token: ,, B0_LastThreeLetters: ,, B1Token: naudojasi, B1_LastThreeLetters: asi, S0B0Distance: 1, S0B0Token: duoti_parodymus_,, S0B1Token: duoti_parodymus_naudojasi, S0B2Token: duoti_parodymus_šia, S0Token: duoti_parodymus, StackLength: 1, transitionHistoryLength1: 0, transitionHistoryLength2: 00, transitionHistoryLength3: 002, 

26- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, naudojasi, šia ,.. ]

B0Token: ,, B0_LastThreeLetters: ,, B1Token: naudojasi, B1_LastThreeLetters: asi, transitionHistoryLength1: 1, transitionHistoryLength2: 10, transitionHistoryLength3: 100, 

27- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [naudojasi, šia, teise ,.. ]

B0Token: naudojasi, B0_LastThreeLetters: asi, B1Token: šia, B1_LastThreeLetters: �ia, S0B0Distance: 1, S0B0Token: ,_naudojasi, S0B1Token: ,_šia, S0B2Token: ,_teise, S0Token: ,, S0_LastThreeLetters: ,, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 21, transitionHistoryLength3: 210, 

28- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [naudojasi, šia, teise ,.. ]

B0Token: naudojasi, B0_LastThreeLetters: asi, B1Token: šia, B1_LastThreeLetters: �ia, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 021, 

29- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [naudojasi]   B= [šia, teise, , ,.. ]

B0Token: šia, B0_LastThreeLetters: �ia, B1Token: teise, B1_LastThreeLetters: ise, S0B0Distance: 1, S0B0Token: naudojasi_šia, S0B1Token: naudojasi_teise, S0B2Token: naudojasi_,, S0Token: naudojasi, S0_LastThreeLetters: asi, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

30- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [šia, teise, , ,.. ]

B0Token: šia, B0_LastThreeLetters: �ia, B1Token: teise, B1_LastThreeLetters: ise, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

31- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [šia]   B= [teise, ,, tačiau ,.. ]

B0Token: teise, B0_LastThreeLetters: ise, B1Token: ,, B1_LastThreeLetters: ,, S0B0Distance: 1, S0B0Token: šia_teise, S0B1Token: šia_,, S0B2Token: šia_tačiau, S0Token: šia, S0_LastThreeLetters: �ia, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

32- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [teise, ,, tačiau ,.. ]

B0Token: teise, B0_LastThreeLetters: ise, B1Token: ,, B1_LastThreeLetters: ,, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

33- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [teise]   B= [,, tačiau, atvykti ,.. ]

B0Token: ,, B0_LastThreeLetters: ,, B1Token: tačiau, B1_LastThreeLetters: iau, S0B0Distance: 1, S0B0Token: teise_,, S0B1Token: teise_tačiau, S0B2Token: teise_atvykti, S0Token: teise, S0_LastThreeLetters: ise, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

34- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, tačiau, atvykti ,.. ]

B0Token: ,, B0_LastThreeLetters: ,, B1Token: tačiau, B1_LastThreeLetters: iau, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

35- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [tačiau, atvykti, duoti ,.. ]

B0Token: tačiau, B0_LastThreeLetters: iau, B1Token: atvykti, B1_LastThreeLetters: kti, S0B0Distance: 1, S0B0Token: ,_tačiau, S0B1Token: ,_atvykti, S0B2Token: ,_duoti, S0Token: ,, S0_LastThreeLetters: ,, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

36- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [tačiau, atvykti, duoti ,.. ]

B0Token: tačiau, B0_LastThreeLetters: iau, B1Token: atvykti, B1_LastThreeLetters: kti, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

37- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [tačiau]   B= [atvykti, duoti, parodymų ,.. ]

B0Token: atvykti, B0_LastThreeLetters: kti, B1Token: duoti, B1_LastThreeLetters: oti, S0B0Distance: 1, S0B0Token: tačiau_atvykti, S0B1Token: tačiau_duoti, S0B2Token: tačiau_parodymų, S0Token: tačiau, S0_LastThreeLetters: iau, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

38- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [atvykti, duoti, parodymų ,.. ]

B0Token: atvykti, B0_LastThreeLetters: kti, B1Token: duoti, B1_LastThreeLetters: oti, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

39- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [atvykti]   B= [duoti, parodymų, turi ,.. ]

B0Token: duoti, B0_LastThreeLetters: oti, B1Token: parodymų, B1_LastThreeLetters: mų, S0B0Distance: 1, S0B0Token: atvykti_duoti, S0B1Token: atvykti_parodymų, S0B2Token: atvykti_turi, S0Token: atvykti, S0_LastThreeLetters: kti, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

40- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [duoti, parodymų, turi ,.. ]

B0Token: duoti, B0_LastThreeLetters: oti, B1Token: parodymų, B1_LastThreeLetters: mų, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

41- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [duoti]   B= [parodymų, turi, ne ,.. ]

B0Token: parodymų, B0_LastThreeLetters: mų, B1Token: turi, B1_LastThreeLetters: uri, S0B0Distance: 1, S0B0Token: duoti_parodymų, S0B1Token: duoti_turi, S0B2Token: duoti_ne, S0Token: duoti, S0_LastThreeLetters: oti, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

42- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [duoti, parodymų]   B= [turi, ne, kada ,.. ]

B0Token: turi, B0_LastThreeLetters: uri, B1Token: ne, B1_LastThreeLetters: ne, S0B0Distance: 1, S0B0Token: parodymų_turi, S0B1Token: parodymų_ne, S0B2Token: parodymų_kada, S0S1Distance: 1, S0Token: parodymų, S0_LastThreeLetters: mų, S1B0Token: duoti_turi, S1S0B0Token: duoti_parodymų_turi, S1S0Token: duoti_parodymų, S1Token: duoti, S1_LastThreeLetters: oti, StackLength: 2, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

43- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[duoti, parodymų]]   B= [turi, ne, kada ,.. ]

B0Token: turi, B0_LastThreeLetters: uri, B1Token: ne, B1_LastThreeLetters: ne, S0B0Distance: 1, S0B0Token: duoti_parodymų_turi, S0B1Token: duoti_parodymų_ne, S0B2Token: duoti_parodymų_kada, S0Token: duoti_parodymų, StackLength: 1, transitionHistoryLength1: 0, transitionHistoryLength2: 00, transitionHistoryLength3: 002, 

44- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [turi, ne, kada ,.. ]

B0Token: turi, B0_LastThreeLetters: uri, B1Token: ne, B1_LastThreeLetters: ne, transitionHistoryLength1: 1, transitionHistoryLength2: 10, transitionHistoryLength3: 100, 

45- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [turi]   B= [ne, kada, nori ,.. ]

B0Token: ne, B0_LastThreeLetters: ne, B1Token: kada, B1_LastThreeLetters: ada, S0B0Distance: 1, S0B0Token: turi_ne, S0B1Token: turi_kada, S0B2Token: turi_nori, S0Token: turi, S0_LastThreeLetters: uri, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 21, transitionHistoryLength3: 210, 

46- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ne, kada, nori ,.. ]

B0Token: ne, B0_LastThreeLetters: ne, B1Token: kada, B1_LastThreeLetters: ada, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 021, 

47- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ne]   B= [kada, nori, , ,.. ]

B0Token: kada, B0_LastThreeLetters: ada, B1Token: nori, B1_LastThreeLetters: ori, S0B0Distance: 1, S0B0Token: ne_kada, S0B1Token: ne_nori, S0B2Token: ne_,, S0Token: ne, S0_LastThreeLetters: ne, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

48- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [kada, nori, , ,.. ]

B0Token: kada, B0_LastThreeLetters: ada, B1Token: nori, B1_LastThreeLetters: ori, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

49- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [kada]   B= [nori, ,, o ,.. ]

B0Token: nori, B0_LastThreeLetters: ori, B1Token: ,, B1_LastThreeLetters: ,, S0B0Distance: 1, S0B0Token: kada_nori, S0B1Token: kada_,, S0B2Token: kada_o, S0Token: kada, S0_LastThreeLetters: ada, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

50- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [nori, ,, o ,.. ]

B0Token: nori, B0_LastThreeLetters: ori, B1Token: ,, B1_LastThreeLetters: ,, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

51- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [nori]   B= [,, o, kada ,.. ]

B0Token: ,, B0_LastThreeLetters: ,, B1Token: o, B1_LastThreeLetters: o, S0B0Distance: 1, S0B0Token: nori_,, S0B1Token: nori_o, S0B2Token: nori_kada, S0Token: nori, S0_LastThreeLetters: ori, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

52- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, o, kada ,.. ]

B0Token: ,, B0_LastThreeLetters: ,, B1Token: o, B1_LastThreeLetters: o, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

53- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [o, kada, kviečiama ,.. ]

B0Token: o, B0_LastThreeLetters: o, B1Token: kada, B1_LastThreeLetters: ada, S0B0Distance: 1, S0B0Token: ,_o, S0B1Token: ,_kada, S0B2Token: ,_kviečiama, S0Token: ,, S0_LastThreeLetters: ,, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

54- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [o, kada, kviečiama ,.. ]

B0Token: o, B0_LastThreeLetters: o, B1Token: kada, B1_LastThreeLetters: ada, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

55- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [o]   B= [kada, kviečiama, . ,.. ]

B0Token: kada, B0_LastThreeLetters: ada, B1Token: kviečiama, B1_LastThreeLetters: ama, S0B0Distance: 1, S0B0Token: o_kada, S0B1Token: o_kviečiama, S0B2Token: o_., S0Token: o, S0_LastThreeLetters: o, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

56- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [kada, kviečiama, . ,.. ]

B0Token: kada, B0_LastThreeLetters: ada, B1Token: kviečiama, B1_LastThreeLetters: ama, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

57- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [kada]   B= [kviečiama, . ,.. ]

B0Token: kviečiama, B0_LastThreeLetters: ama, B1Token: ., B1_LastThreeLetters: ., S0B0Distance: 1, S0B0Token: kada_kviečiama, S0B1Token: kada_., S0Token: kada, S0_LastThreeLetters: ada, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

58- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [kviečiama, . ,.. ]

B0Token: kviečiama, B0_LastThreeLetters: ama, B1Token: ., B1_LastThreeLetters: ., transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

59- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [kviečiama]   B= [.]

B0Token: ., B0_LastThreeLetters: ., S0B0Distance: 1, S0B0Token: kviečiama_., S0Token: kviečiama, S0_LastThreeLetters: ama, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

60- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [.]

B0Token: ., B0_LastThreeLetters: ., transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

61- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [ ]

S0Token: ., S0_LastThreeLetters: ., StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

62- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

## Sentence No. 5337 - 
Pradėjusi didelio masto saugumo tarnybų pertvarkymą , Turkija siekė padidinti civilių institucijų įtaką , taip pat sustiprinti prezidento galias vykdyti priežiūrą , kad būtų užkirstas bet kokia galimybė įvykdyti perversmą .
### Existing MWEs: 
1- **vykdyti priežiūrą** (LVC)
2- **įvykdyti perversmą** (LVC)



0- &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Pradėjusi, didelio, masto ,.. ]

B0Token: Pradėjusi, B0_LastThreeLetters: usi, B1Token: didelio, B1_LastThreeLetters: lio, 

1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Pradėjusi]   B= [didelio, masto, saugumo ,.. ]

B0Token: didelio, B0_LastThreeLetters: lio, B1Token: masto, B1_LastThreeLetters: sto, S0B0Distance: 1, S0B0Token: Pradėjusi_didelio, S0B1Token: Pradėjusi_masto, S0B2Token: Pradėjusi_saugumo, S0Token: Pradėjusi, S0_LastThreeLetters: usi, StackLength: 1, 

2- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [didelio, masto, saugumo ,.. ]

B0Token: didelio, B0_LastThreeLetters: lio, B1Token: masto, B1_LastThreeLetters: sto, transitionHistoryLength1: 0, 

3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [didelio]   B= [masto, saugumo, tarnybų ,.. ]

B0Token: masto, B0_LastThreeLetters: sto, B1Token: saugumo, B1_LastThreeLetters: umo, S0B0Distance: 1, S0B0Token: didelio_masto, S0B1Token: didelio_saugumo, S0B2Token: didelio_tarnybų, S0Token: didelio, S0_LastThreeLetters: lio, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, 

4- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [masto, saugumo, tarnybų ,.. ]

B0Token: masto, B0_LastThreeLetters: sto, B1Token: saugumo, B1_LastThreeLetters: umo, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [masto]   B= [saugumo, tarnybų, pertvarkymą ,.. ]

B0Token: saugumo, B0_LastThreeLetters: umo, B1Token: tarnybų, B1_LastThreeLetters: bų, S0B0Distance: 1, S0B0Token: masto_saugumo, S0B1Token: masto_tarnybų, S0B2Token: masto_pertvarkymą, S0Token: masto, S0_LastThreeLetters: sto, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

6- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [saugumo, tarnybų, pertvarkymą ,.. ]

B0Token: saugumo, B0_LastThreeLetters: umo, B1Token: tarnybų, B1_LastThreeLetters: bų, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [saugumo]   B= [tarnybų, pertvarkymą, , ,.. ]

B0Token: tarnybų, B0_LastThreeLetters: bų, B1Token: pertvarkymą, B1_LastThreeLetters: mą, S0B0Distance: 1, S0B0Token: saugumo_tarnybų, S0B1Token: saugumo_pertvarkymą, S0B2Token: saugumo_,, S0Token: saugumo, S0_LastThreeLetters: umo, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

8- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [tarnybų, pertvarkymą, , ,.. ]

B0Token: tarnybų, B0_LastThreeLetters: bų, B1Token: pertvarkymą, B1_LastThreeLetters: mą, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [tarnybų]   B= [pertvarkymą, ,, Turkija ,.. ]

B0Token: pertvarkymą, B0_LastThreeLetters: mą, B1Token: ,, B1_LastThreeLetters: ,, S0B0Distance: 1, S0B0Token: tarnybų_pertvarkymą, S0B1Token: tarnybų_,, S0B2Token: tarnybų_Turkija, S0Token: tarnybų, S0_LastThreeLetters: bų, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

10- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [pertvarkymą, ,, Turkija ,.. ]

B0Token: pertvarkymą, B0_LastThreeLetters: mą, B1Token: ,, B1_LastThreeLetters: ,, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [pertvarkymą]   B= [,, Turkija, siekė ,.. ]

B0Token: ,, B0_LastThreeLetters: ,, B1Token: Turkija, B1_LastThreeLetters: ija, S0B0Distance: 1, S0B0Token: pertvarkymą_,, S0B1Token: pertvarkymą_Turkija, S0B2Token: pertvarkymą_siekė, S0Token: pertvarkymą, S0_LastThreeLetters: mą, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

12- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, Turkija, siekė ,.. ]

B0Token: ,, B0_LastThreeLetters: ,, B1Token: Turkija, B1_LastThreeLetters: ija, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [Turkija, siekė, padidinti ,.. ]

B0Token: Turkija, B0_LastThreeLetters: ija, B1Token: siekė, B1_LastThreeLetters: kė, S0B0Distance: 1, S0B0Token: ,_Turkija, S0B1Token: ,_siekė, S0B2Token: ,_padidinti, S0Token: ,, S0_LastThreeLetters: ,, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

14- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Turkija, siekė, padidinti ,.. ]

B0Token: Turkija, B0_LastThreeLetters: ija, B1Token: siekė, B1_LastThreeLetters: kė, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Turkija]   B= [siekė, padidinti, civilių ,.. ]

B0Token: siekė, B0_LastThreeLetters: kė, B1Token: padidinti, B1_LastThreeLetters: nti, S0B0Distance: 1, S0B0Token: Turkija_siekė, S0B1Token: Turkija_padidinti, S0B2Token: Turkija_civilių, S0Token: Turkija, S0_LastThreeLetters: ija, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

16- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [siekė, padidinti, civilių ,.. ]

B0Token: siekė, B0_LastThreeLetters: kė, B1Token: padidinti, B1_LastThreeLetters: nti, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [siekė]   B= [padidinti, civilių, institucijų ,.. ]

B0Token: padidinti, B0_LastThreeLetters: nti, B1Token: civilių, B1_LastThreeLetters: ių, S0B0Distance: 1, S0B0Token: siekė_padidinti, S0B1Token: siekė_civilių, S0B2Token: siekė_institucijų, S0Token: siekė, S0_LastThreeLetters: kė, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

18- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [padidinti, civilių, institucijų ,.. ]

B0Token: padidinti, B0_LastThreeLetters: nti, B1Token: civilių, B1_LastThreeLetters: ių, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [padidinti]   B= [civilių, institucijų, įtaką ,.. ]

B0Token: civilių, B0_LastThreeLetters: ių, B1Token: institucijų, B1_LastThreeLetters: jų, S0B0Distance: 1, S0B0Token: padidinti_civilių, S0B1Token: padidinti_institucijų, S0B2Token: padidinti_įtaką, S0Token: padidinti, S0_LastThreeLetters: nti, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

20- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [civilių, institucijų, įtaką ,.. ]

B0Token: civilių, B0_LastThreeLetters: ių, B1Token: institucijų, B1_LastThreeLetters: jų, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [civilių]   B= [institucijų, įtaką, , ,.. ]

B0Token: institucijų, B0_LastThreeLetters: jų, B1Token: įtaką, B1_LastThreeLetters: ką, S0B0Distance: 1, S0B0Token: civilių_institucijų, S0B1Token: civilių_įtaką, S0B2Token: civilių_,, S0Token: civilių, S0_LastThreeLetters: ių, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

22- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [institucijų, įtaką, , ,.. ]

B0Token: institucijų, B0_LastThreeLetters: jų, B1Token: įtaką, B1_LastThreeLetters: ką, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

23- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [institucijų]   B= [įtaką, ,, taip ,.. ]

B0Token: įtaką, B0_LastThreeLetters: ką, B1Token: ,, B1_LastThreeLetters: ,, S0B0Distance: 1, S0B0Token: institucijų_įtaką, S0B1Token: institucijų_,, S0B2Token: institucijų_taip, S0Token: institucijų, S0_LastThreeLetters: jų, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

24- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [įtaką, ,, taip ,.. ]

B0Token: įtaką, B0_LastThreeLetters: ką, B1Token: ,, B1_LastThreeLetters: ,, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

25- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [įtaką]   B= [,, taip, pat ,.. ]

B0Token: ,, B0_LastThreeLetters: ,, B1Token: taip, B1_LastThreeLetters: aip, S0B0Distance: 1, S0B0Token: įtaką_,, S0B1Token: įtaką_taip, S0B2Token: įtaką_pat, S0Token: įtaką, S0_LastThreeLetters: ką, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

26- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, taip, pat ,.. ]

B0Token: ,, B0_LastThreeLetters: ,, B1Token: taip, B1_LastThreeLetters: aip, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

27- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [taip, pat, sustiprinti ,.. ]

B0Token: taip, B0_LastThreeLetters: aip, B1Token: pat, B1_LastThreeLetters: pat, S0B0Distance: 1, S0B0Token: ,_taip, S0B1Token: ,_pat, S0B2Token: ,_sustiprinti, S0Token: ,, S0_LastThreeLetters: ,, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

28- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [taip, pat, sustiprinti ,.. ]

B0Token: taip, B0_LastThreeLetters: aip, B1Token: pat, B1_LastThreeLetters: pat, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

29- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [taip]   B= [pat, sustiprinti, prezidento ,.. ]

B0Token: pat, B0_LastThreeLetters: pat, B1Token: sustiprinti, B1_LastThreeLetters: nti, S0B0Distance: 1, S0B0Token: taip_pat, S0B1Token: taip_sustiprinti, S0B2Token: taip_prezidento, S0Token: taip, S0_LastThreeLetters: aip, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

30- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [pat, sustiprinti, prezidento ,.. ]

B0Token: pat, B0_LastThreeLetters: pat, B1Token: sustiprinti, B1_LastThreeLetters: nti, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

31- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [pat]   B= [sustiprinti, prezidento, galias ,.. ]

B0Token: sustiprinti, B0_LastThreeLetters: nti, B1Token: prezidento, B1_LastThreeLetters: nto, S0B0Distance: 1, S0B0Token: pat_sustiprinti, S0B1Token: pat_prezidento, S0B2Token: pat_galias, S0Token: pat, S0_LastThreeLetters: pat, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

32- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [sustiprinti, prezidento, galias ,.. ]

B0Token: sustiprinti, B0_LastThreeLetters: nti, B1Token: prezidento, B1_LastThreeLetters: nto, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

33- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [sustiprinti]   B= [prezidento, galias, vykdyti ,.. ]

B0Token: prezidento, B0_LastThreeLetters: nto, B1Token: galias, B1_LastThreeLetters: ias, S0B0Distance: 1, S0B0Token: sustiprinti_prezidento, S0B1Token: sustiprinti_galias, S0B2Token: sustiprinti_vykdyti, S0Token: sustiprinti, S0_LastThreeLetters: nti, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

34- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [prezidento, galias, vykdyti ,.. ]

B0Token: prezidento, B0_LastThreeLetters: nto, B1Token: galias, B1_LastThreeLetters: ias, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

35- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [prezidento]   B= [galias, vykdyti, priežiūrą ,.. ]

B0Token: galias, B0_LastThreeLetters: ias, B1Token: vykdyti, B1_LastThreeLetters: yti, S0B0Distance: 1, S0B0Token: prezidento_galias, S0B1Token: prezidento_vykdyti, S0B2Token: prezidento_priežiūrą, S0Token: prezidento, S0_LastThreeLetters: nto, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

36- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [galias, vykdyti, priežiūrą ,.. ]

B0Token: galias, B0_LastThreeLetters: ias, B1Token: vykdyti, B1_LastThreeLetters: yti, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

37- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [galias]   B= [vykdyti, priežiūrą, , ,.. ]

B0Token: vykdyti, B0_LastThreeLetters: yti, B1Token: priežiūrą, B1_LastThreeLetters: rą, S0B0Distance: 1, S0B0Token: galias_vykdyti, S0B1Token: galias_priežiūrą, S0B2Token: galias_,, S0Token: galias, S0_LastThreeLetters: ias, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

38- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [vykdyti, priežiūrą, , ,.. ]

B0Token: vykdyti, B0_LastThreeLetters: yti, B1Token: priežiūrą, B1_LastThreeLetters: rą, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

39- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [vykdyti]   B= [priežiūrą, ,, kad ,.. ]

B0Token: priežiūrą, B0_LastThreeLetters: rą, B1Token: ,, B1_LastThreeLetters: ,, S0B0Distance: 1, S0B0Token: vykdyti_priežiūrą, S0B1Token: vykdyti_,, S0B2Token: vykdyti_kad, S0Token: vykdyti, S0_LastThreeLetters: yti, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

40- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [vykdyti, priežiūrą]   B= [,, kad, būtų ,.. ]

B0Token: ,, B0_LastThreeLetters: ,, B1Token: kad, B1_LastThreeLetters: kad, S0B0Distance: 1, S0B0Token: priežiūrą_,, S0B1Token: priežiūrą_kad, S0B2Token: priežiūrą_būtų, S0S1Distance: 1, S0Token: priežiūrą, S0_LastThreeLetters: rą, S1B0Token: vykdyti_,, S1S0B0Token: vykdyti_priežiūrą_,, S1S0Token: vykdyti_priežiūrą, S1Token: vykdyti, S1_LastThreeLetters: yti, StackLength: 2, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

41- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[vykdyti, priežiūrą]]   B= [,, kad, būtų ,.. ]

B0Token: ,, B0_LastThreeLetters: ,, B1Token: kad, B1_LastThreeLetters: kad, S0B0Distance: 1, S0B0Token: vykdyti_priežiūrą_,, S0B1Token: vykdyti_priežiūrą_kad, S0B2Token: vykdyti_priežiūrą_būtų, S0Token: vykdyti_priežiūrą, StackLength: 1, transitionHistoryLength1: 0, transitionHistoryLength2: 00, transitionHistoryLength3: 002, 

42- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, kad, būtų ,.. ]

B0Token: ,, B0_LastThreeLetters: ,, B1Token: kad, B1_LastThreeLetters: kad, transitionHistoryLength1: 1, transitionHistoryLength2: 10, transitionHistoryLength3: 100, 

43- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [kad, būtų, užkirstas ,.. ]

B0Token: kad, B0_LastThreeLetters: kad, B1Token: būtų, B1_LastThreeLetters: tų, S0B0Distance: 1, S0B0Token: ,_kad, S0B1Token: ,_būtų, S0B2Token: ,_užkirstas, S0Token: ,, S0_LastThreeLetters: ,, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 21, transitionHistoryLength3: 210, 

44- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [kad, būtų, užkirstas ,.. ]

B0Token: kad, B0_LastThreeLetters: kad, B1Token: būtų, B1_LastThreeLetters: tų, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 021, 

45- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [kad]   B= [būtų, užkirstas, bet ,.. ]

B0Token: būtų, B0_LastThreeLetters: tų, B1Token: užkirstas, B1_LastThreeLetters: tas, S0B0Distance: 1, S0B0Token: kad_būtų, S0B1Token: kad_užkirstas, S0B2Token: kad_bet, S0Token: kad, S0_LastThreeLetters: kad, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

46- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [būtų, užkirstas, bet ,.. ]

B0Token: būtų, B0_LastThreeLetters: tų, B1Token: užkirstas, B1_LastThreeLetters: tas, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

47- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [būtų]   B= [užkirstas, bet, kokia ,.. ]

B0Token: užkirstas, B0_LastThreeLetters: tas, B1Token: bet, B1_LastThreeLetters: bet, S0B0Distance: 1, S0B0Token: būtų_užkirstas, S0B1Token: būtų_bet, S0B2Token: būtų_kokia, S0Token: būtų, S0_LastThreeLetters: tų, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

48- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [užkirstas, bet, kokia ,.. ]

B0Token: užkirstas, B0_LastThreeLetters: tas, B1Token: bet, B1_LastThreeLetters: bet, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

49- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [užkirstas]   B= [bet, kokia, galimybė ,.. ]

B0Token: bet, B0_LastThreeLetters: bet, B1Token: kokia, B1_LastThreeLetters: kia, S0B0Distance: 1, S0B0Token: užkirstas_bet, S0B1Token: užkirstas_kokia, S0B2Token: užkirstas_galimybė, S0Token: užkirstas, S0_LastThreeLetters: tas, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

50- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [bet, kokia, galimybė ,.. ]

B0Token: bet, B0_LastThreeLetters: bet, B1Token: kokia, B1_LastThreeLetters: kia, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

51- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [bet]   B= [kokia, galimybė, įvykdyti ,.. ]

B0Token: kokia, B0_LastThreeLetters: kia, B1Token: galimybė, B1_LastThreeLetters: bė, S0B0Distance: 1, S0B0Token: bet_kokia, S0B1Token: bet_galimybė, S0B2Token: bet_įvykdyti, S0Token: bet, S0_LastThreeLetters: bet, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

52- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [kokia, galimybė, įvykdyti ,.. ]

B0Token: kokia, B0_LastThreeLetters: kia, B1Token: galimybė, B1_LastThreeLetters: bė, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

53- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [kokia]   B= [galimybė, įvykdyti, perversmą ,.. ]

B0Token: galimybė, B0_LastThreeLetters: bė, B1Token: įvykdyti, B1_LastThreeLetters: yti, S0B0Distance: 1, S0B0Token: kokia_galimybė, S0B1Token: kokia_įvykdyti, S0B2Token: kokia_perversmą, S0Token: kokia, S0_LastThreeLetters: kia, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

54- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [galimybė, įvykdyti, perversmą ,.. ]

B0Token: galimybė, B0_LastThreeLetters: bė, B1Token: įvykdyti, B1_LastThreeLetters: yti, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

55- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [galimybė]   B= [įvykdyti, perversmą, . ,.. ]

B0Token: įvykdyti, B0_LastThreeLetters: yti, B1Token: perversmą, B1_LastThreeLetters: mą, S0B0Distance: 1, S0B0Token: galimybė_įvykdyti, S0B1Token: galimybė_perversmą, S0B2Token: galimybė_., S0Token: galimybė, S0_LastThreeLetters: bė, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

56- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [įvykdyti, perversmą, . ,.. ]

B0Token: įvykdyti, B0_LastThreeLetters: yti, B1Token: perversmą, B1_LastThreeLetters: mą, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

57- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [įvykdyti]   B= [perversmą, . ,.. ]

B0Token: perversmą, B0_LastThreeLetters: mą, B1Token: ., B1_LastThreeLetters: ., S0B0Distance: 1, S0B0Token: įvykdyti_perversmą, S0B1Token: įvykdyti_., S0Token: įvykdyti, S0_LastThreeLetters: yti, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

58- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [įvykdyti, perversmą]   B= [.]

B0Token: ., B0_LastThreeLetters: ., S0B0Distance: 1, S0B0Token: perversmą_., S0S1Distance: 1, S0Token: perversmą, S0_LastThreeLetters: mą, S1B0Token: įvykdyti_., S1S0B0Token: įvykdyti_perversmą_., S1S0Token: įvykdyti_perversmą, S1Token: įvykdyti, S1_LastThreeLetters: yti, StackLength: 2, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

59- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[įvykdyti, perversmą]]   B= [.]

B0Token: ., B0_LastThreeLetters: ., S0B0Distance: 1, S0B0Token: įvykdyti_perversmą_., S0Token: įvykdyti_perversmą, StackLength: 1, transitionHistoryLength1: 0, transitionHistoryLength2: 00, transitionHistoryLength3: 002, 

60- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [.]

B0Token: ., B0_LastThreeLetters: ., transitionHistoryLength1: 1, transitionHistoryLength2: 10, transitionHistoryLength3: 100, 

61- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [ ]

S0Token: ., S0_LastThreeLetters: ., StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 21, transitionHistoryLength3: 210, 

62- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

## Sentence No. 6225 - 
Vokietijos transporto priemonių kontrolieriaus įstaiga KBA uždegė žalią šviesą „ Opel “ dyzeliniams varikliams , ant kurių buvo kritęs įtarimų šešėlis , esą juose naudojama programinė įranga , skirta nuslėpti tikruosius duomenis apie aplinkai daromą žalą , skelbia „ Bild am Sonntag “ .
### Existing MWEs: 
1- **uždegė žalią šviesą** (ID)
2- **kritęs šešėlis** (ID)



0- &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Vokietijos, transporto, priemonių ,.. ]

B0Token: Vokietijos, B0_LastThreeLetters: jos, B1Token: transporto, B1_LastThreeLetters: rto, 

1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Vokietijos]   B= [transporto, priemonių, kontrolieriaus ,.. ]

B0Token: transporto, B0_LastThreeLetters: rto, B1Token: priemonių, B1_LastThreeLetters: ių, S0B0Distance: 1, S0B0Token: Vokietijos_transporto, S0B1Token: Vokietijos_priemonių, S0B2Token: Vokietijos_kontrolieriaus, S0Token: Vokietijos, S0_LastThreeLetters: jos, StackLength: 1, 

2- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [transporto, priemonių, kontrolieriaus ,.. ]

B0Token: transporto, B0_LastThreeLetters: rto, B1Token: priemonių, B1_LastThreeLetters: ių, transitionHistoryLength1: 0, 

3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [transporto]   B= [priemonių, kontrolieriaus, įstaiga ,.. ]

B0Token: priemonių, B0_LastThreeLetters: ių, B1Token: kontrolieriaus, B1_LastThreeLetters: aus, S0B0Distance: 1, S0B0Token: transporto_priemonių, S0B1Token: transporto_kontrolieriaus, S0B2Token: transporto_įstaiga, S0Token: transporto, S0_LastThreeLetters: rto, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, 

4- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [priemonių, kontrolieriaus, įstaiga ,.. ]

B0Token: priemonių, B0_LastThreeLetters: ių, B1Token: kontrolieriaus, B1_LastThreeLetters: aus, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [priemonių]   B= [kontrolieriaus, įstaiga, KBA ,.. ]

B0Token: kontrolieriaus, B0_LastThreeLetters: aus, B1Token: įstaiga, B1_LastThreeLetters: iga, S0B0Distance: 1, S0B0Token: priemonių_kontrolieriaus, S0B1Token: priemonių_įstaiga, S0B2Token: priemonių_KBA, S0Token: priemonių, S0_LastThreeLetters: ių, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

6- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [kontrolieriaus, įstaiga, KBA ,.. ]

B0Token: kontrolieriaus, B0_LastThreeLetters: aus, B1Token: įstaiga, B1_LastThreeLetters: iga, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [kontrolieriaus]   B= [įstaiga, KBA, uždegė ,.. ]

B0Token: įstaiga, B0_LastThreeLetters: iga, B1Token: KBA, B1_LastThreeLetters: KBA, S0B0Distance: 1, S0B0Token: kontrolieriaus_įstaiga, S0B1Token: kontrolieriaus_KBA, S0B2Token: kontrolieriaus_uždegė, S0Token: kontrolieriaus, S0_LastThreeLetters: aus, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

8- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [įstaiga, KBA, uždegė ,.. ]

B0Token: įstaiga, B0_LastThreeLetters: iga, B1Token: KBA, B1_LastThreeLetters: KBA, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [įstaiga]   B= [KBA, uždegė, žalią ,.. ]

B0Token: KBA, B0_LastThreeLetters: KBA, B1Token: uždegė, B1_LastThreeLetters: gė, S0B0Distance: 1, S0B0Token: įstaiga_KBA, S0B1Token: įstaiga_uždegė, S0B2Token: įstaiga_žalią, S0Token: įstaiga, S0_LastThreeLetters: iga, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

10- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [KBA, uždegė, žalią ,.. ]

B0Token: KBA, B0_LastThreeLetters: KBA, B1Token: uždegė, B1_LastThreeLetters: gė, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [KBA]   B= [uždegė, žalią, šviesą ,.. ]

B0Token: uždegė, B0_LastThreeLetters: gė, B1Token: žalią, B1_LastThreeLetters: ią, S0B0Distance: 1, S0B0Token: KBA_uždegė, S0B1Token: KBA_žalią, S0B2Token: KBA_šviesą, S0Token: KBA, S0_LastThreeLetters: KBA, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

12- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [uždegė, žalią, šviesą ,.. ]

B0Token: uždegė, B0_LastThreeLetters: gė, B1Token: žalią, B1_LastThreeLetters: ią, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [uždegė]   B= [žalią, šviesą, „ ,.. ]

B0Token: žalią, B0_LastThreeLetters: ią, B1Token: šviesą, B1_LastThreeLetters: są, S0B0Distance: 1, S0B0Token: uždegė_žalią, S0B1Token: uždegė_šviesą, S0B2Token: uždegė_„, S0Token: uždegė, S0_LastThreeLetters: gė, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

14- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [uždegė, žalią]   B= [šviesą, „, Opel ,.. ]

B0Token: šviesą, B0_LastThreeLetters: są, B1Token: „, B1_LastThreeLetters: „, S0B0Distance: 1, S0B0Token: žalią_šviesą, S0B1Token: žalią_„, S0B2Token: žalią_Opel, S0S1Distance: 1, S0Token: žalią, S0_LastThreeLetters: ią, S1B0Token: uždegė_šviesą, S1S0B0Token: uždegė_žalią_šviesą, S1S0Token: uždegė_žalią, S1Token: uždegė, S1_LastThreeLetters: gė, StackLength: 2, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [uždegė, žalią, šviesą]   B= [„, Opel, “ ,.. ]

B0Token: „, B0_LastThreeLetters: „, B1Token: Opel, B1_LastThreeLetters: pel, S0B0Distance: 1, S0B0Token: šviesą_„, S0B1Token: šviesą_Opel, S0B2Token: šviesą_“, S0S1Distance: 1, S0Token: šviesą, S0_LastThreeLetters: są, S1B0Token: žalią_„, S1S0B0Token: žalią_šviesą_„, S1S0Token: žalią_šviesą, S1Token: žalią, S1_LastThreeLetters: ią, StackLength: 3, transitionHistoryLength1: 0, transitionHistoryLength2: 00, transitionHistoryLength3: 002, 

16- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [uždegė, [žalią, šviesą]]   B= [„, Opel, “ ,.. ]

B0Token: „, B0_LastThreeLetters: „, B1Token: Opel, B1_LastThreeLetters: pel, S0B0Distance: 1, S0B0Token: žalią_šviesą_„, S0B1Token: žalią_šviesą_Opel, S0B2Token: žalią_šviesą_“, S0Token: žalią_šviesą, S1B0Token: uždegė_„, S1S0B0Token: uždegė_žalią_šviesą_„, S1S0Token: uždegė_žalią_šviesą, S1Token: uždegė, S1_LastThreeLetters: gė, StackLength: 2, transitionHistoryLength1: 0, transitionHistoryLength2: 00, transitionHistoryLength3: 000, 

17- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[uždegė, [žalią, šviesą]]]   B= [„, Opel, “ ,.. ]

B0Token: „, B0_LastThreeLetters: „, B1Token: Opel, B1_LastThreeLetters: pel, S0B0Distance: 1, S0B0Token: uždegė_žalią_šviesą_„, S0B1Token: uždegė_žalią_šviesą_Opel, S0B2Token: uždegė_žalią_šviesą_“, S0Token: uždegė_žalią_šviesą, StackLength: 1, transitionHistoryLength1: 1, transitionHistoryLength2: 10, transitionHistoryLength3: 100, 

18- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [„, Opel, “ ,.. ]

B0Token: „, B0_LastThreeLetters: „, B1Token: Opel, B1_LastThreeLetters: pel, transitionHistoryLength1: 1, transitionHistoryLength2: 11, transitionHistoryLength3: 110, 

19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [„]   B= [Opel, “, dyzeliniams ,.. ]

B0Token: Opel, B0_LastThreeLetters: pel, B1Token: “, B1_LastThreeLetters: “, S0B0Distance: 1, S0B0Token: „_Opel, S0B1Token: „_“, S0B2Token: „_dyzeliniams, S0Token: „, S0_LastThreeLetters: „, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 21, transitionHistoryLength3: 211, 

20- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Opel, “, dyzeliniams ,.. ]

B0Token: Opel, B0_LastThreeLetters: pel, B1Token: “, B1_LastThreeLetters: “, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 021, 

21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Opel]   B= [“, dyzeliniams, varikliams ,.. ]

B0Token: “, B0_LastThreeLetters: “, B1Token: dyzeliniams, B1_LastThreeLetters: ams, S0B0Distance: 1, S0B0Token: Opel_“, S0B1Token: Opel_dyzeliniams, S0B2Token: Opel_varikliams, S0Token: Opel, S0_LastThreeLetters: pel, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

22- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [“, dyzeliniams, varikliams ,.. ]

B0Token: “, B0_LastThreeLetters: “, B1Token: dyzeliniams, B1_LastThreeLetters: ams, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

23- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [“]   B= [dyzeliniams, varikliams, , ,.. ]

B0Token: dyzeliniams, B0_LastThreeLetters: ams, B1Token: varikliams, B1_LastThreeLetters: ams, S0B0Distance: 1, S0B0Token: “_dyzeliniams, S0B1Token: “_varikliams, S0B2Token: “_,, S0Token: “, S0_LastThreeLetters: “, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

24- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [dyzeliniams, varikliams, , ,.. ]

B0Token: dyzeliniams, B0_LastThreeLetters: ams, B1Token: varikliams, B1_LastThreeLetters: ams, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

25- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [dyzeliniams]   B= [varikliams, ,, ant ,.. ]

B0Token: varikliams, B0_LastThreeLetters: ams, B1Token: ,, B1_LastThreeLetters: ,, S0B0Distance: 1, S0B0Token: dyzeliniams_varikliams, S0B1Token: dyzeliniams_,, S0B2Token: dyzeliniams_ant, S0Token: dyzeliniams, S0_LastThreeLetters: ams, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

26- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [varikliams, ,, ant ,.. ]

B0Token: varikliams, B0_LastThreeLetters: ams, B1Token: ,, B1_LastThreeLetters: ,, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

27- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [varikliams]   B= [,, ant, kurių ,.. ]

B0Token: ,, B0_LastThreeLetters: ,, B1Token: ant, B1_LastThreeLetters: ant, S0B0Distance: 1, S0B0Token: varikliams_,, S0B1Token: varikliams_ant, S0B2Token: varikliams_kurių, S0Token: varikliams, S0_LastThreeLetters: ams, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

28- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, ant, kurių ,.. ]

B0Token: ,, B0_LastThreeLetters: ,, B1Token: ant, B1_LastThreeLetters: ant, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

29- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [ant, kurių, buvo ,.. ]

B0Token: ant, B0_LastThreeLetters: ant, B1Token: kurių, B1_LastThreeLetters: ių, S0B0Distance: 1, S0B0Token: ,_ant, S0B1Token: ,_kurių, S0B2Token: ,_buvo, S0Token: ,, S0_LastThreeLetters: ,, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

30- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ant, kurių, buvo ,.. ]

B0Token: ant, B0_LastThreeLetters: ant, B1Token: kurių, B1_LastThreeLetters: ių, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

31- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ant]   B= [kurių, buvo, kritęs ,.. ]

B0Token: kurių, B0_LastThreeLetters: ių, B1Token: buvo, B1_LastThreeLetters: uvo, S0B0Distance: 1, S0B0Token: ant_kurių, S0B1Token: ant_buvo, S0B2Token: ant_kritęs, S0Token: ant, S0_LastThreeLetters: ant, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

32- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [kurių, buvo, kritęs ,.. ]

B0Token: kurių, B0_LastThreeLetters: ių, B1Token: buvo, B1_LastThreeLetters: uvo, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

33- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [kurių]   B= [buvo, kritęs, įtarimų ,.. ]

B0Token: buvo, B0_LastThreeLetters: uvo, B1Token: kritęs, B1_LastThreeLetters: ęs, S0B0Distance: 1, S0B0Token: kurių_buvo, S0B1Token: kurių_kritęs, S0B2Token: kurių_įtarimų, S0Token: kurių, S0_LastThreeLetters: ių, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

34- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [buvo, kritęs, įtarimų ,.. ]

B0Token: buvo, B0_LastThreeLetters: uvo, B1Token: kritęs, B1_LastThreeLetters: ęs, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

35- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [buvo]   B= [kritęs, įtarimų, šešėlis ,.. ]

B0Token: kritęs, B0_LastThreeLetters: ęs, B1Token: įtarimų, B1_LastThreeLetters: mų, S0B0Distance: 1, S0B0Token: buvo_kritęs, S0B1Token: buvo_įtarimų, S0B2Token: buvo_šešėlis, S0Token: buvo, S0_LastThreeLetters: uvo, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

36- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [kritęs, įtarimų, šešėlis ,.. ]

B0Token: kritęs, B0_LastThreeLetters: ęs, B1Token: įtarimų, B1_LastThreeLetters: mų, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

37- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [kritęs]   B= [įtarimų, šešėlis, , ,.. ]

B0Token: įtarimų, B0_LastThreeLetters: mų, B1Token: šešėlis, B1_LastThreeLetters: lis, S0B0Distance: 1, S0B0Token: kritęs_įtarimų, S0B1Token: kritęs_šešėlis, S0B2Token: kritęs_,, S0Token: kritęs, S0_LastThreeLetters: ęs, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

38- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [kritęs, įtarimų]   B= [šešėlis, ,, esą ,.. ]

B0Token: šešėlis, B0_LastThreeLetters: lis, B1Token: ,, B1_LastThreeLetters: ,, S0B0Distance: 1, S0B0Token: įtarimų_šešėlis, S0B1Token: įtarimų_,, S0B2Token: įtarimų_esą, S0S1Distance: 1, S0Token: įtarimų, S0_LastThreeLetters: mų, S1B0Token: kritęs_šešėlis, S1S0B0Token: kritęs_įtarimų_šešėlis, S1S0Token: kritęs_įtarimų, S1Token: kritęs, S1_LastThreeLetters: ęs, StackLength: 2, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

39- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [kritęs]   B= [šešėlis, ,, esą ,.. ]

B0Token: šešėlis, B0_LastThreeLetters: lis, B1Token: ,, B1_LastThreeLetters: ,, S0B0Distance: 2, S0B0Token: kritęs_šešėlis, S0B1Token: kritęs_,, S0B2Token: kritęs_esą, S0Token: kritęs, S0_LastThreeLetters: ęs, StackLength: 1, transitionHistoryLength1: 0, transitionHistoryLength2: 00, transitionHistoryLength3: 002, 

40- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [kritęs, šešėlis]   B= [,, esą, juose ,.. ]

B0Token: ,, B0_LastThreeLetters: ,, B1Token: esą, B1_LastThreeLetters: są, S0B0Distance: 1, S0B0Token: šešėlis_,, S0B1Token: šešėlis_esą, S0B2Token: šešėlis_juose, S0S1Distance: 2, S0Token: šešėlis, S0_LastThreeLetters: lis, S1B0Token: kritęs_,, S1S0B0Token: kritęs_šešėlis_,, S1S0Token: kritęs_šešėlis, S1Token: kritęs, S1_LastThreeLetters: ęs, StackLength: 2, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 200, 

41- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[kritęs, šešėlis]]   B= [,, esą, juose ,.. ]

B0Token: ,, B0_LastThreeLetters: ,, B1Token: esą, B1_LastThreeLetters: są, S0B0Distance: 1, S0B0Token: kritęs_šešėlis_,, S0B1Token: kritęs_šešėlis_esą, S0B2Token: kritęs_šešėlis_juose, S0Token: kritęs_šešėlis, StackLength: 1, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

42- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, esą, juose ,.. ]

B0Token: ,, B0_LastThreeLetters: ,, B1Token: esą, B1_LastThreeLetters: są, transitionHistoryLength1: 1, transitionHistoryLength2: 10, transitionHistoryLength3: 102, 

43- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [esą, juose, naudojama ,.. ]

B0Token: esą, B0_LastThreeLetters: są, B1Token: juose, B1_LastThreeLetters: ose, S0B0Distance: 1, S0B0Token: ,_esą, S0B1Token: ,_juose, S0B2Token: ,_naudojama, S0Token: ,, S0_LastThreeLetters: ,, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 21, transitionHistoryLength3: 210, 

44- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [esą, juose, naudojama ,.. ]

B0Token: esą, B0_LastThreeLetters: są, B1Token: juose, B1_LastThreeLetters: ose, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 021, 

45- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [esą]   B= [juose, naudojama, programinė ,.. ]

B0Token: juose, B0_LastThreeLetters: ose, B1Token: naudojama, B1_LastThreeLetters: ama, S0B0Distance: 1, S0B0Token: esą_juose, S0B1Token: esą_naudojama, S0B2Token: esą_programinė, S0Token: esą, S0_LastThreeLetters: są, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

46- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [juose, naudojama, programinė ,.. ]

B0Token: juose, B0_LastThreeLetters: ose, B1Token: naudojama, B1_LastThreeLetters: ama, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

47- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [juose]   B= [naudojama, programinė, įranga ,.. ]

B0Token: naudojama, B0_LastThreeLetters: ama, B1Token: programinė, B1_LastThreeLetters: nė, S0B0Distance: 1, S0B0Token: juose_naudojama, S0B1Token: juose_programinė, S0B2Token: juose_įranga, S0Token: juose, S0_LastThreeLetters: ose, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

48- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [naudojama, programinė, įranga ,.. ]

B0Token: naudojama, B0_LastThreeLetters: ama, B1Token: programinė, B1_LastThreeLetters: nė, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

49- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [naudojama]   B= [programinė, įranga, , ,.. ]

B0Token: programinė, B0_LastThreeLetters: nė, B1Token: įranga, B1_LastThreeLetters: nga, S0B0Distance: 1, S0B0Token: naudojama_programinė, S0B1Token: naudojama_įranga, S0B2Token: naudojama_,, S0Token: naudojama, S0_LastThreeLetters: ama, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

50- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [programinė, įranga, , ,.. ]

B0Token: programinė, B0_LastThreeLetters: nė, B1Token: įranga, B1_LastThreeLetters: nga, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

51- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [programinė]   B= [įranga, ,, skirta ,.. ]

B0Token: įranga, B0_LastThreeLetters: nga, B1Token: ,, B1_LastThreeLetters: ,, S0B0Distance: 1, S0B0Token: programinė_įranga, S0B1Token: programinė_,, S0B2Token: programinė_skirta, S0Token: programinė, S0_LastThreeLetters: nė, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

52- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [įranga, ,, skirta ,.. ]

B0Token: įranga, B0_LastThreeLetters: nga, B1Token: ,, B1_LastThreeLetters: ,, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

53- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [įranga]   B= [,, skirta, nuslėpti ,.. ]

B0Token: ,, B0_LastThreeLetters: ,, B1Token: skirta, B1_LastThreeLetters: rta, S0B0Distance: 1, S0B0Token: įranga_,, S0B1Token: įranga_skirta, S0B2Token: įranga_nuslėpti, S0Token: įranga, S0_LastThreeLetters: nga, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

54- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, skirta, nuslėpti ,.. ]

B0Token: ,, B0_LastThreeLetters: ,, B1Token: skirta, B1_LastThreeLetters: rta, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

55- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [skirta, nuslėpti, tikruosius ,.. ]

B0Token: skirta, B0_LastThreeLetters: rta, B1Token: nuslėpti, B1_LastThreeLetters: pti, S0B0Distance: 1, S0B0Token: ,_skirta, S0B1Token: ,_nuslėpti, S0B2Token: ,_tikruosius, S0Token: ,, S0_LastThreeLetters: ,, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

56- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [skirta, nuslėpti, tikruosius ,.. ]

B0Token: skirta, B0_LastThreeLetters: rta, B1Token: nuslėpti, B1_LastThreeLetters: pti, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

57- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [skirta]   B= [nuslėpti, tikruosius, duomenis ,.. ]

B0Token: nuslėpti, B0_LastThreeLetters: pti, B1Token: tikruosius, B1_LastThreeLetters: ius, S0B0Distance: 1, S0B0Token: skirta_nuslėpti, S0B1Token: skirta_tikruosius, S0B2Token: skirta_duomenis, S0Token: skirta, S0_LastThreeLetters: rta, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

58- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [nuslėpti, tikruosius, duomenis ,.. ]

B0Token: nuslėpti, B0_LastThreeLetters: pti, B1Token: tikruosius, B1_LastThreeLetters: ius, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

59- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [nuslėpti]   B= [tikruosius, duomenis, apie ,.. ]

B0Token: tikruosius, B0_LastThreeLetters: ius, B1Token: duomenis, B1_LastThreeLetters: nis, S0B0Distance: 1, S0B0Token: nuslėpti_tikruosius, S0B1Token: nuslėpti_duomenis, S0B2Token: nuslėpti_apie, S0Token: nuslėpti, S0_LastThreeLetters: pti, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

60- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [tikruosius, duomenis, apie ,.. ]

B0Token: tikruosius, B0_LastThreeLetters: ius, B1Token: duomenis, B1_LastThreeLetters: nis, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

61- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [tikruosius]   B= [duomenis, apie, aplinkai ,.. ]

B0Token: duomenis, B0_LastThreeLetters: nis, B1Token: apie, B1_LastThreeLetters: pie, S0B0Distance: 1, S0B0Token: tikruosius_duomenis, S0B1Token: tikruosius_apie, S0B2Token: tikruosius_aplinkai, S0Token: tikruosius, S0_LastThreeLetters: ius, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

62- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [duomenis, apie, aplinkai ,.. ]

B0Token: duomenis, B0_LastThreeLetters: nis, B1Token: apie, B1_LastThreeLetters: pie, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

63- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [duomenis]   B= [apie, aplinkai, daromą ,.. ]

B0Token: apie, B0_LastThreeLetters: pie, B1Token: aplinkai, B1_LastThreeLetters: kai, S0B0Distance: 1, S0B0Token: duomenis_apie, S0B1Token: duomenis_aplinkai, S0B2Token: duomenis_daromą, S0Token: duomenis, S0_LastThreeLetters: nis, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

64- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [apie, aplinkai, daromą ,.. ]

B0Token: apie, B0_LastThreeLetters: pie, B1Token: aplinkai, B1_LastThreeLetters: kai, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

65- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [apie]   B= [aplinkai, daromą, žalą ,.. ]

B0Token: aplinkai, B0_LastThreeLetters: kai, B1Token: daromą, B1_LastThreeLetters: mą, S0B0Distance: 1, S0B0Token: apie_aplinkai, S0B1Token: apie_daromą, S0B2Token: apie_žalą, S0Token: apie, S0_LastThreeLetters: pie, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

66- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [aplinkai, daromą, žalą ,.. ]

B0Token: aplinkai, B0_LastThreeLetters: kai, B1Token: daromą, B1_LastThreeLetters: mą, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

67- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [aplinkai]   B= [daromą, žalą, , ,.. ]

B0Token: daromą, B0_LastThreeLetters: mą, B1Token: žalą, B1_LastThreeLetters: lą, S0B0Distance: 1, S0B0Token: aplinkai_daromą, S0B1Token: aplinkai_žalą, S0B2Token: aplinkai_,, S0Token: aplinkai, S0_LastThreeLetters: kai, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

68- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [daromą, žalą, , ,.. ]

B0Token: daromą, B0_LastThreeLetters: mą, B1Token: žalą, B1_LastThreeLetters: lą, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

69- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [daromą]   B= [žalą, ,, skelbia ,.. ]

B0Token: žalą, B0_LastThreeLetters: lą, B1Token: ,, B1_LastThreeLetters: ,, S0B0Distance: 1, S0B0Token: daromą_žalą, S0B1Token: daromą_,, S0B2Token: daromą_skelbia, S0Token: daromą, S0_LastThreeLetters: mą, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

70- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [žalą, ,, skelbia ,.. ]

B0Token: žalą, B0_LastThreeLetters: lą, B1Token: ,, B1_LastThreeLetters: ,, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

71- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [žalą]   B= [,, skelbia, „ ,.. ]

B0Token: ,, B0_LastThreeLetters: ,, B1Token: skelbia, B1_LastThreeLetters: bia, S0B0Distance: 1, S0B0Token: žalą_,, S0B1Token: žalą_skelbia, S0B2Token: žalą_„, S0Token: žalą, S0_LastThreeLetters: lą, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

72- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, skelbia, „ ,.. ]

B0Token: ,, B0_LastThreeLetters: ,, B1Token: skelbia, B1_LastThreeLetters: bia, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

73- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [skelbia, „, Bild ,.. ]

B0Token: skelbia, B0_LastThreeLetters: bia, B1Token: „, B1_LastThreeLetters: „, S0B0Distance: 1, S0B0Token: ,_skelbia, S0B1Token: ,_„, S0B2Token: ,_Bild, S0Token: ,, S0_LastThreeLetters: ,, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

74- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [skelbia, „, Bild ,.. ]

B0Token: skelbia, B0_LastThreeLetters: bia, B1Token: „, B1_LastThreeLetters: „, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

75- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [skelbia]   B= [„, Bild, am ,.. ]

B0Token: „, B0_LastThreeLetters: „, B1Token: Bild, B1_LastThreeLetters: ild, S0B0Distance: 1, S0B0Token: skelbia_„, S0B1Token: skelbia_Bild, S0B2Token: skelbia_am, S0Token: skelbia, S0_LastThreeLetters: bia, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

76- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [„, Bild, am ,.. ]

B0Token: „, B0_LastThreeLetters: „, B1Token: Bild, B1_LastThreeLetters: ild, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

77- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [„]   B= [Bild, am, Sonntag ,.. ]

B0Token: Bild, B0_LastThreeLetters: ild, B1Token: am, B1_LastThreeLetters: am, S0B0Distance: 1, S0B0Token: „_Bild, S0B1Token: „_am, S0B2Token: „_Sonntag, S0Token: „, S0_LastThreeLetters: „, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

78- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Bild, am, Sonntag ,.. ]

B0Token: Bild, B0_LastThreeLetters: ild, B1Token: am, B1_LastThreeLetters: am, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

79- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Bild]   B= [am, Sonntag, “ ,.. ]

B0Token: am, B0_LastThreeLetters: am, B1Token: Sonntag, B1_LastThreeLetters: tag, S0B0Distance: 1, S0B0Token: Bild_am, S0B1Token: Bild_Sonntag, S0B2Token: Bild_“, S0Token: Bild, S0_LastThreeLetters: ild, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

80- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [am, Sonntag, “ ,.. ]

B0Token: am, B0_LastThreeLetters: am, B1Token: Sonntag, B1_LastThreeLetters: tag, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

81- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [am]   B= [Sonntag, “, . ,.. ]

B0Token: Sonntag, B0_LastThreeLetters: tag, B1Token: “, B1_LastThreeLetters: “, S0B0Distance: 1, S0B0Token: am_Sonntag, S0B1Token: am_“, S0B2Token: am_., S0Token: am, S0_LastThreeLetters: am, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

82- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Sonntag, “, . ,.. ]

B0Token: Sonntag, B0_LastThreeLetters: tag, B1Token: “, B1_LastThreeLetters: “, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

83- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Sonntag]   B= [“, . ,.. ]

B0Token: “, B0_LastThreeLetters: “, B1Token: ., B1_LastThreeLetters: ., S0B0Distance: 1, S0B0Token: Sonntag_“, S0B1Token: Sonntag_., S0Token: Sonntag, S0_LastThreeLetters: tag, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

84- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [“, . ,.. ]

B0Token: “, B0_LastThreeLetters: “, B1Token: ., B1_LastThreeLetters: ., transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

85- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [“]   B= [.]

B0Token: ., B0_LastThreeLetters: ., S0B0Distance: 1, S0B0Token: “_., S0Token: “, S0_LastThreeLetters: “, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

86- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [.]

B0Token: ., B0_LastThreeLetters: ., transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

87- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [ ]

S0Token: ., S0_LastThreeLetters: ., StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

88- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

