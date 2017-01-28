## Sentence No. 408 - 
Keletą metų stypčiojusi vietoje , Prancūzijos automobilių rinka , kuri yra antra pagal dydį Europoje po Vokietijos , 2015 m . šovė į viršų .
### Existing MWEs: 
1- **stypčiojusi vietoje** (ID)
2- **šovė į viršų** (ID)



0- &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Keletą, metų, stypčiojusi ,.. ]

B0Token: Keletą, B0_LastThreeLetters: tą, B0_LastTwoLetters: ą, B1Token: metų, B1_LastThreeLetters: tų, B1_LastTwoLetters: ų, 

1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Keletą]   B= [metų, stypčiojusi, vietoje ,.. ]

B0Token: metų, B0_LastThreeLetters: tų, B0_LastTwoLetters: ų, B1Token: stypčiojusi, B1_LastThreeLetters: usi, B1_LastTwoLetters: si, S0B0Distance: 1, S0B0Token: Keletą_metų, S0B1Token: Keletą_stypčiojusi, S0B2Token: Keletą_vietoje, S0Token: Keletą, S0_LastThreeLetters: tą, S0_LastTwoLetters: ą, 

2- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [metų, stypčiojusi, vietoje ,.. ]

B0Token: metų, B0_LastThreeLetters: tų, B0_LastTwoLetters: ų, B1Token: stypčiojusi, B1_LastThreeLetters: usi, B1_LastTwoLetters: si, TransHistory1: 0, 

3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [metų]   B= [stypčiojusi, vietoje, , ,.. ]

B0Token: stypčiojusi, B0_LastThreeLetters: usi, B0_LastTwoLetters: si, B1Token: vietoje, B1_LastThreeLetters: oje, B1_LastTwoLetters: je, S0B0Distance: 1, S0B0Token: metų_stypčiojusi, S0B1Token: metų_vietoje, S0B2Token: metų_,, S0Token: metų, S0_LastThreeLetters: tų, S0_LastTwoLetters: ų, TransHistory1: 2, TransHistory2: 20, 

4- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [stypčiojusi, vietoje, , ,.. ]

B0Token: stypčiojusi, B0_LastThreeLetters: usi, B0_LastTwoLetters: si, B1Token: vietoje, B1_LastThreeLetters: oje, B1_LastTwoLetters: je, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [stypčiojusi]   B= [vietoje, ,, Prancūzijos ,.. ]

B0Token: vietoje, B0_LastThreeLetters: oje, B0_LastTwoLetters: je, B1Token: ,, B1_LastThreeLetters: ,, B1_LastTwoLetters: ,, S0B0Distance: 1, S0B0Token: stypčiojusi_vietoje, S0B1Token: stypčiojusi_,, S0B2Token: stypčiojusi_Prancūzijos, S0Token: stypčiojusi, S0_LastThreeLetters: usi, S0_LastTwoLetters: si, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

6- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [stypčiojusi, vietoje]   B= [,, Prancūzijos, automobilių ,.. ]

B0Token: ,, B0_LastThreeLetters: ,, B0_LastTwoLetters: ,, B1Token: Prancūzijos, B1_LastThreeLetters: jos, B1_LastTwoLetters: os, S0B0Distance: 1, S0B0Token: vietoje_,, S0B1Token: vietoje_Prancūzijos, S0B2Token: vietoje_automobilių, S0S1Distance: 1, S0Token: vietoje, S0_LastThreeLetters: oje, S0_LastTwoLetters: je, S1B0Token: stypčiojusi_,, S1S0B0Token: stypčiojusi_vietoje_,, S1S0Token: stypčiojusi_vietoje, S1Token: stypčiojusi, S1_LastThreeLetters: usi, S1_LastTwoLetters: si, StackLengthIs: 2, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

7- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[stypčiojusi, vietoje]]   B= [,, Prancūzijos, automobilių ,.. ]

B0Token: ,, B0_LastThreeLetters: ,, B0_LastTwoLetters: ,, B1Token: Prancūzijos, B1_LastThreeLetters: jos, B1_LastTwoLetters: os, S0B0Distance: 1, S0B0Token: stypčiojusi_vietoje_,, S0B1Token: stypčiojusi_vietoje_Prancūzijos, S0B2Token: stypčiojusi_vietoje_automobilių, S0Token: stypčiojusi_vietoje, TransHistory1: 0, TransHistory2: 00, TransHistory3: 002, 

8- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, Prancūzijos, automobilių ,.. ]

B0Token: ,, B0_LastThreeLetters: ,, B0_LastTwoLetters: ,, B1Token: Prancūzijos, B1_LastThreeLetters: jos, B1_LastTwoLetters: os, TransHistory1: 1, TransHistory2: 10, TransHistory3: 100, 

9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [Prancūzijos, automobilių, rinka ,.. ]

B0Token: Prancūzijos, B0_LastThreeLetters: jos, B0_LastTwoLetters: os, B1Token: automobilių, B1_LastThreeLetters: ių, B1_LastTwoLetters: ų, S0B0Distance: 1, S0B0Token: ,_Prancūzijos, S0B1Token: ,_automobilių, S0B2Token: ,_rinka, S0Token: ,, S0_LastThreeLetters: ,, S0_LastTwoLetters: ,, TransHistory1: 2, TransHistory2: 21, TransHistory3: 210, 

10- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Prancūzijos, automobilių, rinka ,.. ]

B0Token: Prancūzijos, B0_LastThreeLetters: jos, B0_LastTwoLetters: os, B1Token: automobilių, B1_LastThreeLetters: ių, B1_LastTwoLetters: ų, TransHistory1: 0, TransHistory2: 02, TransHistory3: 021, 

11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Prancūzijos]   B= [automobilių, rinka, , ,.. ]

B0Token: automobilių, B0_LastThreeLetters: ių, B0_LastTwoLetters: ų, B1Token: rinka, B1_LastThreeLetters: nka, B1_LastTwoLetters: ka, S0B0Distance: 1, S0B0Token: Prancūzijos_automobilių, S0B1Token: Prancūzijos_rinka, S0B2Token: Prancūzijos_,, S0Token: Prancūzijos, S0_LastThreeLetters: jos, S0_LastTwoLetters: os, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

12- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [automobilių, rinka, , ,.. ]

B0Token: automobilių, B0_LastThreeLetters: ių, B0_LastTwoLetters: ų, B1Token: rinka, B1_LastThreeLetters: nka, B1_LastTwoLetters: ka, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [automobilių]   B= [rinka, ,, kuri ,.. ]

B0Token: rinka, B0_LastThreeLetters: nka, B0_LastTwoLetters: ka, B1Token: ,, B1_LastThreeLetters: ,, B1_LastTwoLetters: ,, S0B0Distance: 1, S0B0Token: automobilių_rinka, S0B1Token: automobilių_,, S0B2Token: automobilių_kuri, S0Token: automobilių, S0_LastThreeLetters: ių, S0_LastTwoLetters: ų, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

14- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [rinka, ,, kuri ,.. ]

B0Token: rinka, B0_LastThreeLetters: nka, B0_LastTwoLetters: ka, B1Token: ,, B1_LastThreeLetters: ,, B1_LastTwoLetters: ,, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [rinka]   B= [,, kuri, yra ,.. ]

B0Token: ,, B0_LastThreeLetters: ,, B0_LastTwoLetters: ,, B1Token: kuri, B1_LastThreeLetters: uri, B1_LastTwoLetters: ri, S0B0Distance: 1, S0B0Token: rinka_,, S0B1Token: rinka_kuri, S0B2Token: rinka_yra, S0Token: rinka, S0_LastThreeLetters: nka, S0_LastTwoLetters: ka, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

16- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, kuri, yra ,.. ]

B0Token: ,, B0_LastThreeLetters: ,, B0_LastTwoLetters: ,, B1Token: kuri, B1_LastThreeLetters: uri, B1_LastTwoLetters: ri, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [kuri, yra, antra ,.. ]

B0Token: kuri, B0_LastThreeLetters: uri, B0_LastTwoLetters: ri, B1Token: yra, B1_LastThreeLetters: yra, B1_LastTwoLetters: ra, S0B0Distance: 1, S0B0Token: ,_kuri, S0B1Token: ,_yra, S0B2Token: ,_antra, S0Token: ,, S0_LastThreeLetters: ,, S0_LastTwoLetters: ,, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

18- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [kuri, yra, antra ,.. ]

B0Token: kuri, B0_LastThreeLetters: uri, B0_LastTwoLetters: ri, B1Token: yra, B1_LastThreeLetters: yra, B1_LastTwoLetters: ra, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [kuri]   B= [yra, antra, pagal ,.. ]

B0Token: yra, B0_LastThreeLetters: yra, B0_LastTwoLetters: ra, B1Token: antra, B1_LastThreeLetters: tra, B1_LastTwoLetters: ra, S0B0Distance: 1, S0B0Token: kuri_yra, S0B1Token: kuri_antra, S0B2Token: kuri_pagal, S0Token: kuri, S0_LastThreeLetters: uri, S0_LastTwoLetters: ri, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

20- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [yra, antra, pagal ,.. ]

B0Token: yra, B0_LastThreeLetters: yra, B0_LastTwoLetters: ra, B1Token: antra, B1_LastThreeLetters: tra, B1_LastTwoLetters: ra, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [yra]   B= [antra, pagal, dydį ,.. ]

B0Token: antra, B0_LastThreeLetters: tra, B0_LastTwoLetters: ra, B1Token: pagal, B1_LastThreeLetters: gal, B1_LastTwoLetters: al, S0B0Distance: 1, S0B0Token: yra_antra, S0B1Token: yra_pagal, S0B2Token: yra_dydį, S0Token: yra, S0_LastThreeLetters: yra, S0_LastTwoLetters: ra, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

22- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [antra, pagal, dydį ,.. ]

B0Token: antra, B0_LastThreeLetters: tra, B0_LastTwoLetters: ra, B1Token: pagal, B1_LastThreeLetters: gal, B1_LastTwoLetters: al, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

23- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [antra]   B= [pagal, dydį, Europoje ,.. ]

B0Token: pagal, B0_LastThreeLetters: gal, B0_LastTwoLetters: al, B1Token: dydį, B1_LastThreeLetters: dį, B1_LastTwoLetters: į, S0B0Distance: 1, S0B0Token: antra_pagal, S0B1Token: antra_dydį, S0B2Token: antra_Europoje, S0Token: antra, S0_LastThreeLetters: tra, S0_LastTwoLetters: ra, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

24- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [pagal, dydį, Europoje ,.. ]

B0Token: pagal, B0_LastThreeLetters: gal, B0_LastTwoLetters: al, B1Token: dydį, B1_LastThreeLetters: dį, B1_LastTwoLetters: į, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

25- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [pagal]   B= [dydį, Europoje, po ,.. ]

B0Token: dydį, B0_LastThreeLetters: dį, B0_LastTwoLetters: į, B1Token: Europoje, B1_LastThreeLetters: oje, B1_LastTwoLetters: je, S0B0Distance: 1, S0B0Token: pagal_dydį, S0B1Token: pagal_Europoje, S0B2Token: pagal_po, S0Token: pagal, S0_LastThreeLetters: gal, S0_LastTwoLetters: al, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

26- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [dydį, Europoje, po ,.. ]

B0Token: dydį, B0_LastThreeLetters: dį, B0_LastTwoLetters: į, B1Token: Europoje, B1_LastThreeLetters: oje, B1_LastTwoLetters: je, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

27- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [dydį]   B= [Europoje, po, Vokietijos ,.. ]

B0Token: Europoje, B0_LastThreeLetters: oje, B0_LastTwoLetters: je, B1Token: po, B1_LastThreeLetters: po, B1_LastTwoLetters: po, S0B0Distance: 1, S0B0Token: dydį_Europoje, S0B1Token: dydį_po, S0B2Token: dydį_Vokietijos, S0Token: dydį, S0_LastThreeLetters: dį, S0_LastTwoLetters: į, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

28- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Europoje, po, Vokietijos ,.. ]

B0Token: Europoje, B0_LastThreeLetters: oje, B0_LastTwoLetters: je, B1Token: po, B1_LastThreeLetters: po, B1_LastTwoLetters: po, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

29- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Europoje]   B= [po, Vokietijos, , ,.. ]

B0Token: po, B0_LastThreeLetters: po, B0_LastTwoLetters: po, B1Token: Vokietijos, B1_LastThreeLetters: jos, B1_LastTwoLetters: os, S0B0Distance: 1, S0B0Token: Europoje_po, S0B1Token: Europoje_Vokietijos, S0B2Token: Europoje_,, S0Token: Europoje, S0_LastThreeLetters: oje, S0_LastTwoLetters: je, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

30- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [po, Vokietijos, , ,.. ]

B0Token: po, B0_LastThreeLetters: po, B0_LastTwoLetters: po, B1Token: Vokietijos, B1_LastThreeLetters: jos, B1_LastTwoLetters: os, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

31- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [po]   B= [Vokietijos, ,, 2015 ,.. ]

B0Token: Vokietijos, B0_LastThreeLetters: jos, B0_LastTwoLetters: os, B1Token: ,, B1_LastThreeLetters: ,, B1_LastTwoLetters: ,, S0B0Distance: 1, S0B0Token: po_Vokietijos, S0B1Token: po_,, S0B2Token: po_2015, S0Token: po, S0_LastThreeLetters: po, S0_LastTwoLetters: po, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

32- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Vokietijos, ,, 2015 ,.. ]

B0Token: Vokietijos, B0_LastThreeLetters: jos, B0_LastTwoLetters: os, B1Token: ,, B1_LastThreeLetters: ,, B1_LastTwoLetters: ,, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

33- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Vokietijos]   B= [,, 2015, m ,.. ]

B0Token: ,, B0_LastThreeLetters: ,, B0_LastTwoLetters: ,, B1Token: 2015, B1_LastThreeLetters: 015, B1_LastTwoLetters: 15, S0B0Distance: 1, S0B0Token: Vokietijos_,, S0B1Token: Vokietijos_2015, S0B2Token: Vokietijos_m, S0Token: Vokietijos, S0_LastThreeLetters: jos, S0_LastTwoLetters: os, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

34- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, 2015, m ,.. ]

B0Token: ,, B0_LastThreeLetters: ,, B0_LastTwoLetters: ,, B1Token: 2015, B1_LastThreeLetters: 015, B1_LastTwoLetters: 15, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

35- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [2015, m, . ,.. ]

B0Token: 2015, B0_LastThreeLetters: 015, B0_LastTwoLetters: 15, B1Token: m, B1_LastThreeLetters: m, B1_LastTwoLetters: m, S0B0Distance: 1, S0B0Token: ,_2015, S0B1Token: ,_m, S0B2Token: ,_., S0Token: ,, S0_LastThreeLetters: ,, S0_LastTwoLetters: ,, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

36- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [2015, m, . ,.. ]

B0Token: 2015, B0_LastThreeLetters: 015, B0_LastTwoLetters: 15, B1Token: m, B1_LastThreeLetters: m, B1_LastTwoLetters: m, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

37- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [2015]   B= [m, ., šovė ,.. ]

B0Token: m, B0_LastThreeLetters: m, B0_LastTwoLetters: m, B1Token: ., B1_LastThreeLetters: ., B1_LastTwoLetters: ., S0B0Distance: 1, S0B0Token: 2015_m, S0B1Token: 2015_., S0B2Token: 2015_šovė, S0Token: 2015, S0_LastThreeLetters: 015, S0_LastTwoLetters: 15, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

38- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [m, ., šovė ,.. ]

B0Token: m, B0_LastThreeLetters: m, B0_LastTwoLetters: m, B1Token: ., B1_LastThreeLetters: ., B1_LastTwoLetters: ., TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

39- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [m]   B= [., šovė, į ,.. ]

B0Token: ., B0_LastThreeLetters: ., B0_LastTwoLetters: ., B1Token: šovė, B1_LastThreeLetters: vė, B1_LastTwoLetters: ė, S0B0Distance: 1, S0B0Token: m_., S0B1Token: m_šovė, S0B2Token: m_į, S0Token: m, S0_LastThreeLetters: m, S0_LastTwoLetters: m, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

40- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [., šovė, į ,.. ]

B0Token: ., B0_LastThreeLetters: ., B0_LastTwoLetters: ., B1Token: šovė, B1_LastThreeLetters: vė, B1_LastTwoLetters: ė, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

41- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [šovė, į, viršų ,.. ]

B0Token: šovė, B0_LastThreeLetters: vė, B0_LastTwoLetters: ė, B1Token: į, B1_LastThreeLetters: į, B1_LastTwoLetters: į, S0B0Distance: 1, S0B0Token: ._šovė, S0B1Token: ._į, S0B2Token: ._viršų, S0Token: ., S0_LastThreeLetters: ., S0_LastTwoLetters: ., TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

42- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [šovė, į, viršų ,.. ]

B0Token: šovė, B0_LastThreeLetters: vė, B0_LastTwoLetters: ė, B1Token: į, B1_LastThreeLetters: į, B1_LastTwoLetters: į, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

43- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [šovė]   B= [į, viršų, . ,.. ]

B0Token: į, B0_LastThreeLetters: į, B0_LastTwoLetters: į, B1Token: viršų, B1_LastThreeLetters: �ų, B1_LastTwoLetters: ų, S0B0Distance: 1, S0B0Token: šovė_į, S0B1Token: šovė_viršų, S0B2Token: šovė_., S0Token: šovė, S0_LastThreeLetters: vė, S0_LastTwoLetters: ė, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

44- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [šovė, į]   B= [viršų, . ,.. ]

B0Token: viršų, B0_LastThreeLetters: �ų, B0_LastTwoLetters: ų, B1Token: ., B1_LastThreeLetters: ., B1_LastTwoLetters: ., S0B0Distance: 1, S0B0Token: į_viršų, S0B1Token: į_., S0S1Distance: 1, S0Token: į, S0_LastThreeLetters: į, S0_LastTwoLetters: į, S1B0Token: šovė_viršų, S1S0B0Token: šovė_į_viršų, S1S0Token: šovė_į, S1Token: šovė, S1_LastThreeLetters: vė, S1_LastTwoLetters: ė, StackLengthIs: 2, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

45- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [šovė, į, viršų]   B= [.]

B0Token: ., B0_LastThreeLetters: ., B0_LastTwoLetters: ., S0B0Distance: 1, S0B0Token: viršų_., S0S1Distance: 1, S0Token: viršų, S0_LastThreeLetters: �ų, S0_LastTwoLetters: ų, S1B0Token: į_., S1S0B0Token: į_viršų_., S1S0Token: į_viršų, S1Token: į, S1_LastThreeLetters: į, S1_LastTwoLetters: į, StackLengthIs: 3, TransHistory1: 0, TransHistory2: 00, TransHistory3: 002, 

46- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [šovė, [į, viršų]]   B= [.]

B0Token: ., B0_LastThreeLetters: ., B0_LastTwoLetters: ., S0B0Distance: 1, S0B0Token: į_viršų_., S0Token: į_viršų, S1B0Token: šovė_., S1S0B0Token: šovė_į_viršų_., S1S0Token: šovė_į_viršų, S1Token: šovė, S1_LastThreeLetters: vė, S1_LastTwoLetters: ė, StackLengthIs: 2, TransHistory1: 0, TransHistory2: 00, TransHistory3: 000, 

47- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[šovė, [į, viršų]]]   B= [.]

B0Token: ., B0_LastThreeLetters: ., B0_LastTwoLetters: ., S0B0Distance: 1, S0B0Token: šovė_į_viršų_., S0Token: šovė_į_viršų, TransHistory1: 1, TransHistory2: 10, TransHistory3: 100, 

48- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [.]

B0Token: ., B0_LastThreeLetters: ., B0_LastTwoLetters: ., TransHistory1: 1, TransHistory2: 11, TransHistory3: 110, 

49- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [ ]

S0Token: ., S0_LastThreeLetters: ., S0_LastTwoLetters: ., TransHistory1: 2, TransHistory2: 21, TransHistory3: 211, 

50- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

## Sentence No. 1048 - 
Darome prielaidą , kad užsakovas gali priimti sprendimą ir nenaudoti šio korpuso tam , kad nugesintų gandų bangą ir numalšintų ažiotažą , kilusį tarp dalies gyventojų . “
### Existing MWEs: 
1- **priimti sprendimą** (LVC)
2- **nugesintų bangą** (ID)



0- &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Darome, prielaidą, , ,.. ]

B0Token: Darome, B0_LastThreeLetters: ome, B0_LastTwoLetters: me, B1Token: prielaidą, B1_LastThreeLetters: dą, B1_LastTwoLetters: ą, 

1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Darome]   B= [prielaidą, ,, kad ,.. ]

B0Token: prielaidą, B0_LastThreeLetters: dą, B0_LastTwoLetters: ą, B1Token: ,, B1_LastThreeLetters: ,, B1_LastTwoLetters: ,, S0B0Distance: 1, S0B0Token: Darome_prielaidą, S0B1Token: Darome_,, S0B2Token: Darome_kad, S0Token: Darome, S0_LastThreeLetters: ome, S0_LastTwoLetters: me, 

2- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [prielaidą, ,, kad ,.. ]

B0Token: prielaidą, B0_LastThreeLetters: dą, B0_LastTwoLetters: ą, B1Token: ,, B1_LastThreeLetters: ,, B1_LastTwoLetters: ,, TransHistory1: 0, 

3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [prielaidą]   B= [,, kad, užsakovas ,.. ]

B0Token: ,, B0_LastThreeLetters: ,, B0_LastTwoLetters: ,, B1Token: kad, B1_LastThreeLetters: kad, B1_LastTwoLetters: ad, S0B0Distance: 1, S0B0Token: prielaidą_,, S0B1Token: prielaidą_kad, S0B2Token: prielaidą_užsakovas, S0Token: prielaidą, S0_LastThreeLetters: dą, S0_LastTwoLetters: ą, TransHistory1: 2, TransHistory2: 20, 

4- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, kad, užsakovas ,.. ]

B0Token: ,, B0_LastThreeLetters: ,, B0_LastTwoLetters: ,, B1Token: kad, B1_LastThreeLetters: kad, B1_LastTwoLetters: ad, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [kad, užsakovas, gali ,.. ]

B0Token: kad, B0_LastThreeLetters: kad, B0_LastTwoLetters: ad, B1Token: užsakovas, B1_LastThreeLetters: vas, B1_LastTwoLetters: as, S0B0Distance: 1, S0B0Token: ,_kad, S0B1Token: ,_užsakovas, S0B2Token: ,_gali, S0Token: ,, S0_LastThreeLetters: ,, S0_LastTwoLetters: ,, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

6- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [kad, užsakovas, gali ,.. ]

B0Token: kad, B0_LastThreeLetters: kad, B0_LastTwoLetters: ad, B1Token: užsakovas, B1_LastThreeLetters: vas, B1_LastTwoLetters: as, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [kad]   B= [užsakovas, gali, priimti ,.. ]

B0Token: užsakovas, B0_LastThreeLetters: vas, B0_LastTwoLetters: as, B1Token: gali, B1_LastThreeLetters: ali, B1_LastTwoLetters: li, S0B0Distance: 1, S0B0Token: kad_užsakovas, S0B1Token: kad_gali, S0B2Token: kad_priimti, S0Token: kad, S0_LastThreeLetters: kad, S0_LastTwoLetters: ad, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

8- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [užsakovas, gali, priimti ,.. ]

B0Token: užsakovas, B0_LastThreeLetters: vas, B0_LastTwoLetters: as, B1Token: gali, B1_LastThreeLetters: ali, B1_LastTwoLetters: li, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [užsakovas]   B= [gali, priimti, sprendimą ,.. ]

B0Token: gali, B0_LastThreeLetters: ali, B0_LastTwoLetters: li, B1Token: priimti, B1_LastThreeLetters: mti, B1_LastTwoLetters: ti, S0B0Distance: 1, S0B0Token: užsakovas_gali, S0B1Token: užsakovas_priimti, S0B2Token: užsakovas_sprendimą, S0Token: užsakovas, S0_LastThreeLetters: vas, S0_LastTwoLetters: as, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

10- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [gali, priimti, sprendimą ,.. ]

B0Token: gali, B0_LastThreeLetters: ali, B0_LastTwoLetters: li, B1Token: priimti, B1_LastThreeLetters: mti, B1_LastTwoLetters: ti, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [gali]   B= [priimti, sprendimą, ir ,.. ]

B0Token: priimti, B0_LastThreeLetters: mti, B0_LastTwoLetters: ti, B1Token: sprendimą, B1_LastThreeLetters: mą, B1_LastTwoLetters: ą, S0B0Distance: 1, S0B0Token: gali_priimti, S0B1Token: gali_sprendimą, S0B2Token: gali_ir, S0Token: gali, S0_LastThreeLetters: ali, S0_LastTwoLetters: li, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

12- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [priimti, sprendimą, ir ,.. ]

B0Token: priimti, B0_LastThreeLetters: mti, B0_LastTwoLetters: ti, B1Token: sprendimą, B1_LastThreeLetters: mą, B1_LastTwoLetters: ą, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [priimti]   B= [sprendimą, ir, nenaudoti ,.. ]

B0Token: sprendimą, B0_LastThreeLetters: mą, B0_LastTwoLetters: ą, B1Token: ir, B1_LastThreeLetters: ir, B1_LastTwoLetters: ir, S0B0Distance: 1, S0B0Token: priimti_sprendimą, S0B1Token: priimti_ir, S0B2Token: priimti_nenaudoti, S0Token: priimti, S0_LastThreeLetters: mti, S0_LastTwoLetters: ti, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

14- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [priimti, sprendimą]   B= [ir, nenaudoti, šio ,.. ]

B0Token: ir, B0_LastThreeLetters: ir, B0_LastTwoLetters: ir, B1Token: nenaudoti, B1_LastThreeLetters: oti, B1_LastTwoLetters: ti, S0B0Distance: 1, S0B0Token: sprendimą_ir, S0B1Token: sprendimą_nenaudoti, S0B2Token: sprendimą_šio, S0S1Distance: 1, S0Token: sprendimą, S0_LastThreeLetters: mą, S0_LastTwoLetters: ą, S1B0Token: priimti_ir, S1S0B0Token: priimti_sprendimą_ir, S1S0Token: priimti_sprendimą, S1Token: priimti, S1_LastThreeLetters: mti, S1_LastTwoLetters: ti, StackLengthIs: 2, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

15- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[priimti, sprendimą]]   B= [ir, nenaudoti, šio ,.. ]

B0Token: ir, B0_LastThreeLetters: ir, B0_LastTwoLetters: ir, B1Token: nenaudoti, B1_LastThreeLetters: oti, B1_LastTwoLetters: ti, S0B0Distance: 1, S0B0Token: priimti_sprendimą_ir, S0B1Token: priimti_sprendimą_nenaudoti, S0B2Token: priimti_sprendimą_šio, S0Token: priimti_sprendimą, TransHistory1: 0, TransHistory2: 00, TransHistory3: 002, 

16- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ir, nenaudoti, šio ,.. ]

B0Token: ir, B0_LastThreeLetters: ir, B0_LastTwoLetters: ir, B1Token: nenaudoti, B1_LastThreeLetters: oti, B1_LastTwoLetters: ti, TransHistory1: 1, TransHistory2: 10, TransHistory3: 100, 

17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ir]   B= [nenaudoti, šio, korpuso ,.. ]

B0Token: nenaudoti, B0_LastThreeLetters: oti, B0_LastTwoLetters: ti, B1Token: šio, B1_LastThreeLetters: �io, B1_LastTwoLetters: io, S0B0Distance: 1, S0B0Token: ir_nenaudoti, S0B1Token: ir_šio, S0B2Token: ir_korpuso, S0Token: ir, S0_LastThreeLetters: ir, S0_LastTwoLetters: ir, TransHistory1: 2, TransHistory2: 21, TransHistory3: 210, 

18- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [nenaudoti, šio, korpuso ,.. ]

B0Token: nenaudoti, B0_LastThreeLetters: oti, B0_LastTwoLetters: ti, B1Token: šio, B1_LastThreeLetters: �io, B1_LastTwoLetters: io, TransHistory1: 0, TransHistory2: 02, TransHistory3: 021, 

19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [nenaudoti]   B= [šio, korpuso, tam ,.. ]

B0Token: šio, B0_LastThreeLetters: �io, B0_LastTwoLetters: io, B1Token: korpuso, B1_LastThreeLetters: uso, B1_LastTwoLetters: so, S0B0Distance: 1, S0B0Token: nenaudoti_šio, S0B1Token: nenaudoti_korpuso, S0B2Token: nenaudoti_tam, S0Token: nenaudoti, S0_LastThreeLetters: oti, S0_LastTwoLetters: ti, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

20- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [šio, korpuso, tam ,.. ]

B0Token: šio, B0_LastThreeLetters: �io, B0_LastTwoLetters: io, B1Token: korpuso, B1_LastThreeLetters: uso, B1_LastTwoLetters: so, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [šio]   B= [korpuso, tam, , ,.. ]

B0Token: korpuso, B0_LastThreeLetters: uso, B0_LastTwoLetters: so, B1Token: tam, B1_LastThreeLetters: tam, B1_LastTwoLetters: am, S0B0Distance: 1, S0B0Token: šio_korpuso, S0B1Token: šio_tam, S0B2Token: šio_,, S0Token: šio, S0_LastThreeLetters: �io, S0_LastTwoLetters: io, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

22- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [korpuso, tam, , ,.. ]

B0Token: korpuso, B0_LastThreeLetters: uso, B0_LastTwoLetters: so, B1Token: tam, B1_LastThreeLetters: tam, B1_LastTwoLetters: am, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

23- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [korpuso]   B= [tam, ,, kad ,.. ]

B0Token: tam, B0_LastThreeLetters: tam, B0_LastTwoLetters: am, B1Token: ,, B1_LastThreeLetters: ,, B1_LastTwoLetters: ,, S0B0Distance: 1, S0B0Token: korpuso_tam, S0B1Token: korpuso_,, S0B2Token: korpuso_kad, S0Token: korpuso, S0_LastThreeLetters: uso, S0_LastTwoLetters: so, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

24- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [tam, ,, kad ,.. ]

B0Token: tam, B0_LastThreeLetters: tam, B0_LastTwoLetters: am, B1Token: ,, B1_LastThreeLetters: ,, B1_LastTwoLetters: ,, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

25- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [tam]   B= [,, kad, nugesintų ,.. ]

B0Token: ,, B0_LastThreeLetters: ,, B0_LastTwoLetters: ,, B1Token: kad, B1_LastThreeLetters: kad, B1_LastTwoLetters: ad, S0B0Distance: 1, S0B0Token: tam_,, S0B1Token: tam_kad, S0B2Token: tam_nugesintų, S0Token: tam, S0_LastThreeLetters: tam, S0_LastTwoLetters: am, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

26- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, kad, nugesintų ,.. ]

B0Token: ,, B0_LastThreeLetters: ,, B0_LastTwoLetters: ,, B1Token: kad, B1_LastThreeLetters: kad, B1_LastTwoLetters: ad, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

27- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [kad, nugesintų, gandų ,.. ]

B0Token: kad, B0_LastThreeLetters: kad, B0_LastTwoLetters: ad, B1Token: nugesintų, B1_LastThreeLetters: tų, B1_LastTwoLetters: ų, S0B0Distance: 1, S0B0Token: ,_kad, S0B1Token: ,_nugesintų, S0B2Token: ,_gandų, S0Token: ,, S0_LastThreeLetters: ,, S0_LastTwoLetters: ,, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

28- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [kad, nugesintų, gandų ,.. ]

B0Token: kad, B0_LastThreeLetters: kad, B0_LastTwoLetters: ad, B1Token: nugesintų, B1_LastThreeLetters: tų, B1_LastTwoLetters: ų, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

29- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [kad]   B= [nugesintų, gandų, bangą ,.. ]

B0Token: nugesintų, B0_LastThreeLetters: tų, B0_LastTwoLetters: ų, B1Token: gandų, B1_LastThreeLetters: dų, B1_LastTwoLetters: ų, S0B0Distance: 1, S0B0Token: kad_nugesintų, S0B1Token: kad_gandų, S0B2Token: kad_bangą, S0Token: kad, S0_LastThreeLetters: kad, S0_LastTwoLetters: ad, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

30- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [nugesintų, gandų, bangą ,.. ]

B0Token: nugesintų, B0_LastThreeLetters: tų, B0_LastTwoLetters: ų, B1Token: gandų, B1_LastThreeLetters: dų, B1_LastTwoLetters: ų, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

31- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [nugesintų]   B= [gandų, bangą, ir ,.. ]

B0Token: gandų, B0_LastThreeLetters: dų, B0_LastTwoLetters: ų, B1Token: bangą, B1_LastThreeLetters: gą, B1_LastTwoLetters: ą, S0B0Distance: 1, S0B0Token: nugesintų_gandų, S0B1Token: nugesintų_bangą, S0B2Token: nugesintų_ir, S0Token: nugesintų, S0_LastThreeLetters: tų, S0_LastTwoLetters: ų, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

32- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [nugesintų, gandų]   B= [bangą, ir, numalšintų ,.. ]

B0Token: bangą, B0_LastThreeLetters: gą, B0_LastTwoLetters: ą, B1Token: ir, B1_LastThreeLetters: ir, B1_LastTwoLetters: ir, S0B0Distance: 1, S0B0Token: gandų_bangą, S0B1Token: gandų_ir, S0B2Token: gandų_numalšintų, S0S1Distance: 1, S0Token: gandų, S0_LastThreeLetters: dų, S0_LastTwoLetters: ų, S1B0Token: nugesintų_bangą, S1S0B0Token: nugesintų_gandų_bangą, S1S0Token: nugesintų_gandų, S1Token: nugesintų, S1_LastThreeLetters: tų, S1_LastTwoLetters: ų, StackLengthIs: 2, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

33- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [nugesintų]   B= [bangą, ir, numalšintų ,.. ]

B0Token: bangą, B0_LastThreeLetters: gą, B0_LastTwoLetters: ą, B1Token: ir, B1_LastThreeLetters: ir, B1_LastTwoLetters: ir, S0B0Distance: 2, S0B0Token: nugesintų_bangą, S0B1Token: nugesintų_ir, S0B2Token: nugesintų_numalšintų, S0Token: nugesintų, S0_LastThreeLetters: tų, S0_LastTwoLetters: ų, TransHistory1: 0, TransHistory2: 00, TransHistory3: 002, 

34- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [nugesintų, bangą]   B= [ir, numalšintų, ažiotažą ,.. ]

B0Token: ir, B0_LastThreeLetters: ir, B0_LastTwoLetters: ir, B1Token: numalšintų, B1_LastThreeLetters: tų, B1_LastTwoLetters: ų, S0B0Distance: 1, S0B0Token: bangą_ir, S0B1Token: bangą_numalšintų, S0B2Token: bangą_ažiotažą, S0S1Distance: 2, S0Token: bangą, S0_LastThreeLetters: gą, S0_LastTwoLetters: ą, S1B0Token: nugesintų_ir, S1S0B0Token: nugesintų_bangą_ir, S1S0Token: nugesintų_bangą, S1Token: nugesintų, S1_LastThreeLetters: tų, S1_LastTwoLetters: ų, StackLengthIs: 2, TransHistory1: 2, TransHistory2: 20, TransHistory3: 200, 

35- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[nugesintų, bangą]]   B= [ir, numalšintų, ažiotažą ,.. ]

B0Token: ir, B0_LastThreeLetters: ir, B0_LastTwoLetters: ir, B1Token: numalšintų, B1_LastThreeLetters: tų, B1_LastTwoLetters: ų, S0B0Distance: 1, S0B0Token: nugesintų_bangą_ir, S0B1Token: nugesintų_bangą_numalšintų, S0B2Token: nugesintų_bangą_ažiotažą, S0Token: nugesintų_bangą, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

36- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ir, numalšintų, ažiotažą ,.. ]

B0Token: ir, B0_LastThreeLetters: ir, B0_LastTwoLetters: ir, B1Token: numalšintų, B1_LastThreeLetters: tų, B1_LastTwoLetters: ų, TransHistory1: 1, TransHistory2: 10, TransHistory3: 102, 

37- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ir]   B= [numalšintų, ažiotažą, , ,.. ]

B0Token: numalšintų, B0_LastThreeLetters: tų, B0_LastTwoLetters: ų, B1Token: ažiotažą, B1_LastThreeLetters: �ą, B1_LastTwoLetters: ą, S0B0Distance: 1, S0B0Token: ir_numalšintų, S0B1Token: ir_ažiotažą, S0B2Token: ir_,, S0Token: ir, S0_LastThreeLetters: ir, S0_LastTwoLetters: ir, TransHistory1: 2, TransHistory2: 21, TransHistory3: 210, 

38- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [numalšintų, ažiotažą, , ,.. ]

B0Token: numalšintų, B0_LastThreeLetters: tų, B0_LastTwoLetters: ų, B1Token: ažiotažą, B1_LastThreeLetters: �ą, B1_LastTwoLetters: ą, TransHistory1: 0, TransHistory2: 02, TransHistory3: 021, 

39- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [numalšintų]   B= [ažiotažą, ,, kilusį ,.. ]

B0Token: ažiotažą, B0_LastThreeLetters: �ą, B0_LastTwoLetters: ą, B1Token: ,, B1_LastThreeLetters: ,, B1_LastTwoLetters: ,, S0B0Distance: 1, S0B0Token: numalšintų_ažiotažą, S0B1Token: numalšintų_,, S0B2Token: numalšintų_kilusį, S0Token: numalšintų, S0_LastThreeLetters: tų, S0_LastTwoLetters: ų, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

40- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ažiotažą, ,, kilusį ,.. ]

B0Token: ažiotažą, B0_LastThreeLetters: �ą, B0_LastTwoLetters: ą, B1Token: ,, B1_LastThreeLetters: ,, B1_LastTwoLetters: ,, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

41- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ažiotažą]   B= [,, kilusį, tarp ,.. ]

B0Token: ,, B0_LastThreeLetters: ,, B0_LastTwoLetters: ,, B1Token: kilusį, B1_LastThreeLetters: sį, B1_LastTwoLetters: į, S0B0Distance: 1, S0B0Token: ažiotažą_,, S0B1Token: ažiotažą_kilusį, S0B2Token: ažiotažą_tarp, S0Token: ažiotažą, S0_LastThreeLetters: �ą, S0_LastTwoLetters: ą, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

42- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, kilusį, tarp ,.. ]

B0Token: ,, B0_LastThreeLetters: ,, B0_LastTwoLetters: ,, B1Token: kilusį, B1_LastThreeLetters: sį, B1_LastTwoLetters: į, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

43- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [kilusį, tarp, dalies ,.. ]

B0Token: kilusį, B0_LastThreeLetters: sį, B0_LastTwoLetters: į, B1Token: tarp, B1_LastThreeLetters: arp, B1_LastTwoLetters: rp, S0B0Distance: 1, S0B0Token: ,_kilusį, S0B1Token: ,_tarp, S0B2Token: ,_dalies, S0Token: ,, S0_LastThreeLetters: ,, S0_LastTwoLetters: ,, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

44- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [kilusį, tarp, dalies ,.. ]

B0Token: kilusį, B0_LastThreeLetters: sį, B0_LastTwoLetters: į, B1Token: tarp, B1_LastThreeLetters: arp, B1_LastTwoLetters: rp, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

45- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [kilusį]   B= [tarp, dalies, gyventojų ,.. ]

B0Token: tarp, B0_LastThreeLetters: arp, B0_LastTwoLetters: rp, B1Token: dalies, B1_LastThreeLetters: ies, B1_LastTwoLetters: es, S0B0Distance: 1, S0B0Token: kilusį_tarp, S0B1Token: kilusį_dalies, S0B2Token: kilusį_gyventojų, S0Token: kilusį, S0_LastThreeLetters: sį, S0_LastTwoLetters: į, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

46- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [tarp, dalies, gyventojų ,.. ]

B0Token: tarp, B0_LastThreeLetters: arp, B0_LastTwoLetters: rp, B1Token: dalies, B1_LastThreeLetters: ies, B1_LastTwoLetters: es, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

47- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [tarp]   B= [dalies, gyventojų, . ,.. ]

B0Token: dalies, B0_LastThreeLetters: ies, B0_LastTwoLetters: es, B1Token: gyventojų, B1_LastThreeLetters: jų, B1_LastTwoLetters: ų, S0B0Distance: 1, S0B0Token: tarp_dalies, S0B1Token: tarp_gyventojų, S0B2Token: tarp_., S0Token: tarp, S0_LastThreeLetters: arp, S0_LastTwoLetters: rp, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

48- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [dalies, gyventojų, . ,.. ]

B0Token: dalies, B0_LastThreeLetters: ies, B0_LastTwoLetters: es, B1Token: gyventojų, B1_LastThreeLetters: jų, B1_LastTwoLetters: ų, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

49- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [dalies]   B= [gyventojų, ., “ ,.. ]

B0Token: gyventojų, B0_LastThreeLetters: jų, B0_LastTwoLetters: ų, B1Token: ., B1_LastThreeLetters: ., B1_LastTwoLetters: ., S0B0Distance: 1, S0B0Token: dalies_gyventojų, S0B1Token: dalies_., S0B2Token: dalies_“, S0Token: dalies, S0_LastThreeLetters: ies, S0_LastTwoLetters: es, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

50- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [gyventojų, ., “ ,.. ]

B0Token: gyventojų, B0_LastThreeLetters: jų, B0_LastTwoLetters: ų, B1Token: ., B1_LastThreeLetters: ., B1_LastTwoLetters: ., TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

51- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [gyventojų]   B= [., “ ,.. ]

B0Token: ., B0_LastThreeLetters: ., B0_LastTwoLetters: ., B1Token: “, B1_LastThreeLetters: “, B1_LastTwoLetters: ��, S0B0Distance: 1, S0B0Token: gyventojų_., S0B1Token: gyventojų_“, S0Token: gyventojų, S0_LastThreeLetters: jų, S0_LastTwoLetters: ų, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

52- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [., “ ,.. ]

B0Token: ., B0_LastThreeLetters: ., B0_LastTwoLetters: ., B1Token: “, B1_LastThreeLetters: “, B1_LastTwoLetters: ��, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

53- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [“]

B0Token: “, B0_LastThreeLetters: “, B0_LastTwoLetters: ��, S0B0Distance: 1, S0B0Token: ._“, S0Token: ., S0_LastThreeLetters: ., S0_LastTwoLetters: ., TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

54- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [“]

B0Token: “, B0_LastThreeLetters: “, B0_LastTwoLetters: ��, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

55- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [“]   B= [ ]

S0Token: “, S0_LastThreeLetters: “, S0_LastTwoLetters: ��, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

56- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

## Sentence No. 1469 - 
Pasak A . Gališanskytės , D . Štraupaitė yra išreiškusi norą duoti parodymus , naudojasi šia teise , tačiau atvykti duoti parodymų turi ne kada nori , o kada kviečiama .
### Existing MWEs: 
1- **duoti parodymus** (LVC)
2- **duoti parodymų** (LVC)



0- &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Pasak, A, . ,.. ]

B0Token: Pasak, B0_LastThreeLetters: sak, B0_LastTwoLetters: ak, B1Token: A, B1_LastThreeLetters: A, B1_LastTwoLetters: A, 

1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Pasak]   B= [A, ., Gališanskytės ,.. ]

B0Token: A, B0_LastThreeLetters: A, B0_LastTwoLetters: A, B1Token: ., B1_LastThreeLetters: ., B1_LastTwoLetters: ., S0B0Distance: 1, S0B0Token: Pasak_A, S0B1Token: Pasak_., S0B2Token: Pasak_Gališanskytės, S0Token: Pasak, S0_LastThreeLetters: sak, S0_LastTwoLetters: ak, 

2- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [A, ., Gališanskytės ,.. ]

B0Token: A, B0_LastThreeLetters: A, B0_LastTwoLetters: A, B1Token: ., B1_LastThreeLetters: ., B1_LastTwoLetters: ., TransHistory1: 0, 

3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [A]   B= [., Gališanskytės, , ,.. ]

B0Token: ., B0_LastThreeLetters: ., B0_LastTwoLetters: ., B1Token: Gališanskytės, B1_LastThreeLetters: ės, B1_LastTwoLetters: �s, S0B0Distance: 1, S0B0Token: A_., S0B1Token: A_Gališanskytės, S0B2Token: A_,, S0Token: A, S0_LastThreeLetters: A, S0_LastTwoLetters: A, TransHistory1: 2, TransHistory2: 20, 

4- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [., Gališanskytės, , ,.. ]

B0Token: ., B0_LastThreeLetters: ., B0_LastTwoLetters: ., B1Token: Gališanskytės, B1_LastThreeLetters: ės, B1_LastTwoLetters: �s, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [Gališanskytės, ,, D ,.. ]

B0Token: Gališanskytės, B0_LastThreeLetters: ės, B0_LastTwoLetters: �s, B1Token: ,, B1_LastThreeLetters: ,, B1_LastTwoLetters: ,, S0B0Distance: 1, S0B0Token: ._Gališanskytės, S0B1Token: ._,, S0B2Token: ._D, S0Token: ., S0_LastThreeLetters: ., S0_LastTwoLetters: ., TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

6- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Gališanskytės, ,, D ,.. ]

B0Token: Gališanskytės, B0_LastThreeLetters: ės, B0_LastTwoLetters: �s, B1Token: ,, B1_LastThreeLetters: ,, B1_LastTwoLetters: ,, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Gališanskytės]   B= [,, D, . ,.. ]

B0Token: ,, B0_LastThreeLetters: ,, B0_LastTwoLetters: ,, B1Token: D, B1_LastThreeLetters: D, B1_LastTwoLetters: D, S0B0Distance: 1, S0B0Token: Gališanskytės_,, S0B1Token: Gališanskytės_D, S0B2Token: Gališanskytės_., S0Token: Gališanskytės, S0_LastThreeLetters: ės, S0_LastTwoLetters: �s, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

8- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, D, . ,.. ]

B0Token: ,, B0_LastThreeLetters: ,, B0_LastTwoLetters: ,, B1Token: D, B1_LastThreeLetters: D, B1_LastTwoLetters: D, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [D, ., Štraupaitė ,.. ]

B0Token: D, B0_LastThreeLetters: D, B0_LastTwoLetters: D, B1Token: ., B1_LastThreeLetters: ., B1_LastTwoLetters: ., S0B0Distance: 1, S0B0Token: ,_D, S0B1Token: ,_., S0B2Token: ,_Štraupaitė, S0Token: ,, S0_LastThreeLetters: ,, S0_LastTwoLetters: ,, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

10- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [D, ., Štraupaitė ,.. ]

B0Token: D, B0_LastThreeLetters: D, B0_LastTwoLetters: D, B1Token: ., B1_LastThreeLetters: ., B1_LastTwoLetters: ., TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [D]   B= [., Štraupaitė, yra ,.. ]

B0Token: ., B0_LastThreeLetters: ., B0_LastTwoLetters: ., B1Token: Štraupaitė, B1_LastThreeLetters: tė, B1_LastTwoLetters: ė, S0B0Distance: 1, S0B0Token: D_., S0B1Token: D_Štraupaitė, S0B2Token: D_yra, S0Token: D, S0_LastThreeLetters: D, S0_LastTwoLetters: D, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

12- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [., Štraupaitė, yra ,.. ]

B0Token: ., B0_LastThreeLetters: ., B0_LastTwoLetters: ., B1Token: Štraupaitė, B1_LastThreeLetters: tė, B1_LastTwoLetters: ė, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [Štraupaitė, yra, išreiškusi ,.. ]

B0Token: Štraupaitė, B0_LastThreeLetters: tė, B0_LastTwoLetters: ė, B1Token: yra, B1_LastThreeLetters: yra, B1_LastTwoLetters: ra, S0B0Distance: 1, S0B0Token: ._Štraupaitė, S0B1Token: ._yra, S0B2Token: ._išreiškusi, S0Token: ., S0_LastThreeLetters: ., S0_LastTwoLetters: ., TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

14- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Štraupaitė, yra, išreiškusi ,.. ]

B0Token: Štraupaitė, B0_LastThreeLetters: tė, B0_LastTwoLetters: ė, B1Token: yra, B1_LastThreeLetters: yra, B1_LastTwoLetters: ra, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Štraupaitė]   B= [yra, išreiškusi, norą ,.. ]

B0Token: yra, B0_LastThreeLetters: yra, B0_LastTwoLetters: ra, B1Token: išreiškusi, B1_LastThreeLetters: usi, B1_LastTwoLetters: si, S0B0Distance: 1, S0B0Token: Štraupaitė_yra, S0B1Token: Štraupaitė_išreiškusi, S0B2Token: Štraupaitė_norą, S0Token: Štraupaitė, S0_LastThreeLetters: tė, S0_LastTwoLetters: ė, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

16- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [yra, išreiškusi, norą ,.. ]

B0Token: yra, B0_LastThreeLetters: yra, B0_LastTwoLetters: ra, B1Token: išreiškusi, B1_LastThreeLetters: usi, B1_LastTwoLetters: si, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [yra]   B= [išreiškusi, norą, duoti ,.. ]

B0Token: išreiškusi, B0_LastThreeLetters: usi, B0_LastTwoLetters: si, B1Token: norą, B1_LastThreeLetters: rą, B1_LastTwoLetters: ą, S0B0Distance: 1, S0B0Token: yra_išreiškusi, S0B1Token: yra_norą, S0B2Token: yra_duoti, S0Token: yra, S0_LastThreeLetters: yra, S0_LastTwoLetters: ra, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

18- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [išreiškusi, norą, duoti ,.. ]

B0Token: išreiškusi, B0_LastThreeLetters: usi, B0_LastTwoLetters: si, B1Token: norą, B1_LastThreeLetters: rą, B1_LastTwoLetters: ą, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [išreiškusi]   B= [norą, duoti, parodymus ,.. ]

B0Token: norą, B0_LastThreeLetters: rą, B0_LastTwoLetters: ą, B1Token: duoti, B1_LastThreeLetters: oti, B1_LastTwoLetters: ti, S0B0Distance: 1, S0B0Token: išreiškusi_norą, S0B1Token: išreiškusi_duoti, S0B2Token: išreiškusi_parodymus, S0Token: išreiškusi, S0_LastThreeLetters: usi, S0_LastTwoLetters: si, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

20- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [norą, duoti, parodymus ,.. ]

B0Token: norą, B0_LastThreeLetters: rą, B0_LastTwoLetters: ą, B1Token: duoti, B1_LastThreeLetters: oti, B1_LastTwoLetters: ti, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [norą]   B= [duoti, parodymus, , ,.. ]

B0Token: duoti, B0_LastThreeLetters: oti, B0_LastTwoLetters: ti, B1Token: parodymus, B1_LastThreeLetters: mus, B1_LastTwoLetters: us, S0B0Distance: 1, S0B0Token: norą_duoti, S0B1Token: norą_parodymus, S0B2Token: norą_,, S0Token: norą, S0_LastThreeLetters: rą, S0_LastTwoLetters: ą, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

22- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [duoti, parodymus, , ,.. ]

B0Token: duoti, B0_LastThreeLetters: oti, B0_LastTwoLetters: ti, B1Token: parodymus, B1_LastThreeLetters: mus, B1_LastTwoLetters: us, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

23- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [duoti]   B= [parodymus, ,, naudojasi ,.. ]

B0Token: parodymus, B0_LastThreeLetters: mus, B0_LastTwoLetters: us, B1Token: ,, B1_LastThreeLetters: ,, B1_LastTwoLetters: ,, S0B0Distance: 1, S0B0Token: duoti_parodymus, S0B1Token: duoti_,, S0B2Token: duoti_naudojasi, S0Token: duoti, S0_LastThreeLetters: oti, S0_LastTwoLetters: ti, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

24- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [duoti, parodymus]   B= [,, naudojasi, šia ,.. ]

B0Token: ,, B0_LastThreeLetters: ,, B0_LastTwoLetters: ,, B1Token: naudojasi, B1_LastThreeLetters: asi, B1_LastTwoLetters: si, S0B0Distance: 1, S0B0Token: parodymus_,, S0B1Token: parodymus_naudojasi, S0B2Token: parodymus_šia, S0S1Distance: 1, S0Token: parodymus, S0_LastThreeLetters: mus, S0_LastTwoLetters: us, S1B0Token: duoti_,, S1S0B0Token: duoti_parodymus_,, S1S0Token: duoti_parodymus, S1Token: duoti, S1_LastThreeLetters: oti, S1_LastTwoLetters: ti, StackLengthIs: 2, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

25- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[duoti, parodymus]]   B= [,, naudojasi, šia ,.. ]

B0Token: ,, B0_LastThreeLetters: ,, B0_LastTwoLetters: ,, B1Token: naudojasi, B1_LastThreeLetters: asi, B1_LastTwoLetters: si, S0B0Distance: 1, S0B0Token: duoti_parodymus_,, S0B1Token: duoti_parodymus_naudojasi, S0B2Token: duoti_parodymus_šia, S0Token: duoti_parodymus, TransHistory1: 0, TransHistory2: 00, TransHistory3: 002, 

26- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, naudojasi, šia ,.. ]

B0Token: ,, B0_LastThreeLetters: ,, B0_LastTwoLetters: ,, B1Token: naudojasi, B1_LastThreeLetters: asi, B1_LastTwoLetters: si, TransHistory1: 1, TransHistory2: 10, TransHistory3: 100, 

27- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [naudojasi, šia, teise ,.. ]

B0Token: naudojasi, B0_LastThreeLetters: asi, B0_LastTwoLetters: si, B1Token: šia, B1_LastThreeLetters: �ia, B1_LastTwoLetters: ia, S0B0Distance: 1, S0B0Token: ,_naudojasi, S0B1Token: ,_šia, S0B2Token: ,_teise, S0Token: ,, S0_LastThreeLetters: ,, S0_LastTwoLetters: ,, TransHistory1: 2, TransHistory2: 21, TransHistory3: 210, 

28- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [naudojasi, šia, teise ,.. ]

B0Token: naudojasi, B0_LastThreeLetters: asi, B0_LastTwoLetters: si, B1Token: šia, B1_LastThreeLetters: �ia, B1_LastTwoLetters: ia, TransHistory1: 0, TransHistory2: 02, TransHistory3: 021, 

29- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [naudojasi]   B= [šia, teise, , ,.. ]

B0Token: šia, B0_LastThreeLetters: �ia, B0_LastTwoLetters: ia, B1Token: teise, B1_LastThreeLetters: ise, B1_LastTwoLetters: se, S0B0Distance: 1, S0B0Token: naudojasi_šia, S0B1Token: naudojasi_teise, S0B2Token: naudojasi_,, S0Token: naudojasi, S0_LastThreeLetters: asi, S0_LastTwoLetters: si, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

30- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [šia, teise, , ,.. ]

B0Token: šia, B0_LastThreeLetters: �ia, B0_LastTwoLetters: ia, B1Token: teise, B1_LastThreeLetters: ise, B1_LastTwoLetters: se, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

31- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [šia]   B= [teise, ,, tačiau ,.. ]

B0Token: teise, B0_LastThreeLetters: ise, B0_LastTwoLetters: se, B1Token: ,, B1_LastThreeLetters: ,, B1_LastTwoLetters: ,, S0B0Distance: 1, S0B0Token: šia_teise, S0B1Token: šia_,, S0B2Token: šia_tačiau, S0Token: šia, S0_LastThreeLetters: �ia, S0_LastTwoLetters: ia, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

32- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [teise, ,, tačiau ,.. ]

B0Token: teise, B0_LastThreeLetters: ise, B0_LastTwoLetters: se, B1Token: ,, B1_LastThreeLetters: ,, B1_LastTwoLetters: ,, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

33- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [teise]   B= [,, tačiau, atvykti ,.. ]

B0Token: ,, B0_LastThreeLetters: ,, B0_LastTwoLetters: ,, B1Token: tačiau, B1_LastThreeLetters: iau, B1_LastTwoLetters: au, S0B0Distance: 1, S0B0Token: teise_,, S0B1Token: teise_tačiau, S0B2Token: teise_atvykti, S0Token: teise, S0_LastThreeLetters: ise, S0_LastTwoLetters: se, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

34- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, tačiau, atvykti ,.. ]

B0Token: ,, B0_LastThreeLetters: ,, B0_LastTwoLetters: ,, B1Token: tačiau, B1_LastThreeLetters: iau, B1_LastTwoLetters: au, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

35- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [tačiau, atvykti, duoti ,.. ]

B0Token: tačiau, B0_LastThreeLetters: iau, B0_LastTwoLetters: au, B1Token: atvykti, B1_LastThreeLetters: kti, B1_LastTwoLetters: ti, S0B0Distance: 1, S0B0Token: ,_tačiau, S0B1Token: ,_atvykti, S0B2Token: ,_duoti, S0Token: ,, S0_LastThreeLetters: ,, S0_LastTwoLetters: ,, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

36- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [tačiau, atvykti, duoti ,.. ]

B0Token: tačiau, B0_LastThreeLetters: iau, B0_LastTwoLetters: au, B1Token: atvykti, B1_LastThreeLetters: kti, B1_LastTwoLetters: ti, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

37- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [tačiau]   B= [atvykti, duoti, parodymų ,.. ]

B0Token: atvykti, B0_LastThreeLetters: kti, B0_LastTwoLetters: ti, B1Token: duoti, B1_LastThreeLetters: oti, B1_LastTwoLetters: ti, S0B0Distance: 1, S0B0Token: tačiau_atvykti, S0B1Token: tačiau_duoti, S0B2Token: tačiau_parodymų, S0Token: tačiau, S0_LastThreeLetters: iau, S0_LastTwoLetters: au, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

38- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [atvykti, duoti, parodymų ,.. ]

B0Token: atvykti, B0_LastThreeLetters: kti, B0_LastTwoLetters: ti, B1Token: duoti, B1_LastThreeLetters: oti, B1_LastTwoLetters: ti, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

39- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [atvykti]   B= [duoti, parodymų, turi ,.. ]

B0Token: duoti, B0_LastThreeLetters: oti, B0_LastTwoLetters: ti, B1Token: parodymų, B1_LastThreeLetters: mų, B1_LastTwoLetters: ų, S0B0Distance: 1, S0B0Token: atvykti_duoti, S0B1Token: atvykti_parodymų, S0B2Token: atvykti_turi, S0Token: atvykti, S0_LastThreeLetters: kti, S0_LastTwoLetters: ti, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

40- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [duoti, parodymų, turi ,.. ]

B0Token: duoti, B0_LastThreeLetters: oti, B0_LastTwoLetters: ti, B1Token: parodymų, B1_LastThreeLetters: mų, B1_LastTwoLetters: ų, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

41- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [duoti]   B= [parodymų, turi, ne ,.. ]

B0Token: parodymų, B0_LastThreeLetters: mų, B0_LastTwoLetters: ų, B1Token: turi, B1_LastThreeLetters: uri, B1_LastTwoLetters: ri, S0B0Distance: 1, S0B0Token: duoti_parodymų, S0B1Token: duoti_turi, S0B2Token: duoti_ne, S0Token: duoti, S0_LastThreeLetters: oti, S0_LastTwoLetters: ti, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

42- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [duoti, parodymų]   B= [turi, ne, kada ,.. ]

B0Token: turi, B0_LastThreeLetters: uri, B0_LastTwoLetters: ri, B1Token: ne, B1_LastThreeLetters: ne, B1_LastTwoLetters: ne, S0B0Distance: 1, S0B0Token: parodymų_turi, S0B1Token: parodymų_ne, S0B2Token: parodymų_kada, S0S1Distance: 1, S0Token: parodymų, S0_LastThreeLetters: mų, S0_LastTwoLetters: ų, S1B0Token: duoti_turi, S1S0B0Token: duoti_parodymų_turi, S1S0Token: duoti_parodymų, S1Token: duoti, S1_LastThreeLetters: oti, S1_LastTwoLetters: ti, StackLengthIs: 2, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

43- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[duoti, parodymų]]   B= [turi, ne, kada ,.. ]

B0Token: turi, B0_LastThreeLetters: uri, B0_LastTwoLetters: ri, B1Token: ne, B1_LastThreeLetters: ne, B1_LastTwoLetters: ne, S0B0Distance: 1, S0B0Token: duoti_parodymų_turi, S0B1Token: duoti_parodymų_ne, S0B2Token: duoti_parodymų_kada, S0Token: duoti_parodymų, TransHistory1: 0, TransHistory2: 00, TransHistory3: 002, 

44- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [turi, ne, kada ,.. ]

B0Token: turi, B0_LastThreeLetters: uri, B0_LastTwoLetters: ri, B1Token: ne, B1_LastThreeLetters: ne, B1_LastTwoLetters: ne, TransHistory1: 1, TransHistory2: 10, TransHistory3: 100, 

45- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [turi]   B= [ne, kada, nori ,.. ]

B0Token: ne, B0_LastThreeLetters: ne, B0_LastTwoLetters: ne, B1Token: kada, B1_LastThreeLetters: ada, B1_LastTwoLetters: da, S0B0Distance: 1, S0B0Token: turi_ne, S0B1Token: turi_kada, S0B2Token: turi_nori, S0Token: turi, S0_LastThreeLetters: uri, S0_LastTwoLetters: ri, TransHistory1: 2, TransHistory2: 21, TransHistory3: 210, 

46- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ne, kada, nori ,.. ]

B0Token: ne, B0_LastThreeLetters: ne, B0_LastTwoLetters: ne, B1Token: kada, B1_LastThreeLetters: ada, B1_LastTwoLetters: da, TransHistory1: 0, TransHistory2: 02, TransHistory3: 021, 

47- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ne]   B= [kada, nori, , ,.. ]

B0Token: kada, B0_LastThreeLetters: ada, B0_LastTwoLetters: da, B1Token: nori, B1_LastThreeLetters: ori, B1_LastTwoLetters: ri, S0B0Distance: 1, S0B0Token: ne_kada, S0B1Token: ne_nori, S0B2Token: ne_,, S0Token: ne, S0_LastThreeLetters: ne, S0_LastTwoLetters: ne, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

48- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [kada, nori, , ,.. ]

B0Token: kada, B0_LastThreeLetters: ada, B0_LastTwoLetters: da, B1Token: nori, B1_LastThreeLetters: ori, B1_LastTwoLetters: ri, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

49- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [kada]   B= [nori, ,, o ,.. ]

B0Token: nori, B0_LastThreeLetters: ori, B0_LastTwoLetters: ri, B1Token: ,, B1_LastThreeLetters: ,, B1_LastTwoLetters: ,, S0B0Distance: 1, S0B0Token: kada_nori, S0B1Token: kada_,, S0B2Token: kada_o, S0Token: kada, S0_LastThreeLetters: ada, S0_LastTwoLetters: da, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

50- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [nori, ,, o ,.. ]

B0Token: nori, B0_LastThreeLetters: ori, B0_LastTwoLetters: ri, B1Token: ,, B1_LastThreeLetters: ,, B1_LastTwoLetters: ,, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

51- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [nori]   B= [,, o, kada ,.. ]

B0Token: ,, B0_LastThreeLetters: ,, B0_LastTwoLetters: ,, B1Token: o, B1_LastThreeLetters: o, B1_LastTwoLetters: o, S0B0Distance: 1, S0B0Token: nori_,, S0B1Token: nori_o, S0B2Token: nori_kada, S0Token: nori, S0_LastThreeLetters: ori, S0_LastTwoLetters: ri, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

52- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, o, kada ,.. ]

B0Token: ,, B0_LastThreeLetters: ,, B0_LastTwoLetters: ,, B1Token: o, B1_LastThreeLetters: o, B1_LastTwoLetters: o, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

53- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [o, kada, kviečiama ,.. ]

B0Token: o, B0_LastThreeLetters: o, B0_LastTwoLetters: o, B1Token: kada, B1_LastThreeLetters: ada, B1_LastTwoLetters: da, S0B0Distance: 1, S0B0Token: ,_o, S0B1Token: ,_kada, S0B2Token: ,_kviečiama, S0Token: ,, S0_LastThreeLetters: ,, S0_LastTwoLetters: ,, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

54- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [o, kada, kviečiama ,.. ]

B0Token: o, B0_LastThreeLetters: o, B0_LastTwoLetters: o, B1Token: kada, B1_LastThreeLetters: ada, B1_LastTwoLetters: da, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

55- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [o]   B= [kada, kviečiama, . ,.. ]

B0Token: kada, B0_LastThreeLetters: ada, B0_LastTwoLetters: da, B1Token: kviečiama, B1_LastThreeLetters: ama, B1_LastTwoLetters: ma, S0B0Distance: 1, S0B0Token: o_kada, S0B1Token: o_kviečiama, S0B2Token: o_., S0Token: o, S0_LastThreeLetters: o, S0_LastTwoLetters: o, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

56- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [kada, kviečiama, . ,.. ]

B0Token: kada, B0_LastThreeLetters: ada, B0_LastTwoLetters: da, B1Token: kviečiama, B1_LastThreeLetters: ama, B1_LastTwoLetters: ma, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

57- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [kada]   B= [kviečiama, . ,.. ]

B0Token: kviečiama, B0_LastThreeLetters: ama, B0_LastTwoLetters: ma, B1Token: ., B1_LastThreeLetters: ., B1_LastTwoLetters: ., S0B0Distance: 1, S0B0Token: kada_kviečiama, S0B1Token: kada_., S0Token: kada, S0_LastThreeLetters: ada, S0_LastTwoLetters: da, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

58- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [kviečiama, . ,.. ]

B0Token: kviečiama, B0_LastThreeLetters: ama, B0_LastTwoLetters: ma, B1Token: ., B1_LastThreeLetters: ., B1_LastTwoLetters: ., TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

59- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [kviečiama]   B= [.]

B0Token: ., B0_LastThreeLetters: ., B0_LastTwoLetters: ., S0B0Distance: 1, S0B0Token: kviečiama_., S0Token: kviečiama, S0_LastThreeLetters: ama, S0_LastTwoLetters: ma, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

60- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [.]

B0Token: ., B0_LastThreeLetters: ., B0_LastTwoLetters: ., TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

61- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [ ]

S0Token: ., S0_LastThreeLetters: ., S0_LastTwoLetters: ., TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

62- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

## Sentence No. 5337 - 
Pradėjusi didelio masto saugumo tarnybų pertvarkymą , Turkija siekė padidinti civilių institucijų įtaką , taip pat sustiprinti prezidento galias vykdyti priežiūrą , kad būtų užkirstas bet kokia galimybė įvykdyti perversmą .
### Existing MWEs: 
1- **vykdyti priežiūrą** (LVC)
2- **įvykdyti perversmą** (LVC)



0- &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Pradėjusi, didelio, masto ,.. ]

B0Token: Pradėjusi, B0_LastThreeLetters: usi, B0_LastTwoLetters: si, B1Token: didelio, B1_LastThreeLetters: lio, B1_LastTwoLetters: io, 

1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Pradėjusi]   B= [didelio, masto, saugumo ,.. ]

B0Token: didelio, B0_LastThreeLetters: lio, B0_LastTwoLetters: io, B1Token: masto, B1_LastThreeLetters: sto, B1_LastTwoLetters: to, S0B0Distance: 1, S0B0Token: Pradėjusi_didelio, S0B1Token: Pradėjusi_masto, S0B2Token: Pradėjusi_saugumo, S0Token: Pradėjusi, S0_LastThreeLetters: usi, S0_LastTwoLetters: si, 

2- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [didelio, masto, saugumo ,.. ]

B0Token: didelio, B0_LastThreeLetters: lio, B0_LastTwoLetters: io, B1Token: masto, B1_LastThreeLetters: sto, B1_LastTwoLetters: to, TransHistory1: 0, 

3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [didelio]   B= [masto, saugumo, tarnybų ,.. ]

B0Token: masto, B0_LastThreeLetters: sto, B0_LastTwoLetters: to, B1Token: saugumo, B1_LastThreeLetters: umo, B1_LastTwoLetters: mo, S0B0Distance: 1, S0B0Token: didelio_masto, S0B1Token: didelio_saugumo, S0B2Token: didelio_tarnybų, S0Token: didelio, S0_LastThreeLetters: lio, S0_LastTwoLetters: io, TransHistory1: 2, TransHistory2: 20, 

4- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [masto, saugumo, tarnybų ,.. ]

B0Token: masto, B0_LastThreeLetters: sto, B0_LastTwoLetters: to, B1Token: saugumo, B1_LastThreeLetters: umo, B1_LastTwoLetters: mo, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [masto]   B= [saugumo, tarnybų, pertvarkymą ,.. ]

B0Token: saugumo, B0_LastThreeLetters: umo, B0_LastTwoLetters: mo, B1Token: tarnybų, B1_LastThreeLetters: bų, B1_LastTwoLetters: ų, S0B0Distance: 1, S0B0Token: masto_saugumo, S0B1Token: masto_tarnybų, S0B2Token: masto_pertvarkymą, S0Token: masto, S0_LastThreeLetters: sto, S0_LastTwoLetters: to, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

6- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [saugumo, tarnybų, pertvarkymą ,.. ]

B0Token: saugumo, B0_LastThreeLetters: umo, B0_LastTwoLetters: mo, B1Token: tarnybų, B1_LastThreeLetters: bų, B1_LastTwoLetters: ų, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [saugumo]   B= [tarnybų, pertvarkymą, , ,.. ]

B0Token: tarnybų, B0_LastThreeLetters: bų, B0_LastTwoLetters: ų, B1Token: pertvarkymą, B1_LastThreeLetters: mą, B1_LastTwoLetters: ą, S0B0Distance: 1, S0B0Token: saugumo_tarnybų, S0B1Token: saugumo_pertvarkymą, S0B2Token: saugumo_,, S0Token: saugumo, S0_LastThreeLetters: umo, S0_LastTwoLetters: mo, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

8- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [tarnybų, pertvarkymą, , ,.. ]

B0Token: tarnybų, B0_LastThreeLetters: bų, B0_LastTwoLetters: ų, B1Token: pertvarkymą, B1_LastThreeLetters: mą, B1_LastTwoLetters: ą, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [tarnybų]   B= [pertvarkymą, ,, Turkija ,.. ]

B0Token: pertvarkymą, B0_LastThreeLetters: mą, B0_LastTwoLetters: ą, B1Token: ,, B1_LastThreeLetters: ,, B1_LastTwoLetters: ,, S0B0Distance: 1, S0B0Token: tarnybų_pertvarkymą, S0B1Token: tarnybų_,, S0B2Token: tarnybų_Turkija, S0Token: tarnybų, S0_LastThreeLetters: bų, S0_LastTwoLetters: ų, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

10- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [pertvarkymą, ,, Turkija ,.. ]

B0Token: pertvarkymą, B0_LastThreeLetters: mą, B0_LastTwoLetters: ą, B1Token: ,, B1_LastThreeLetters: ,, B1_LastTwoLetters: ,, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [pertvarkymą]   B= [,, Turkija, siekė ,.. ]

B0Token: ,, B0_LastThreeLetters: ,, B0_LastTwoLetters: ,, B1Token: Turkija, B1_LastThreeLetters: ija, B1_LastTwoLetters: ja, S0B0Distance: 1, S0B0Token: pertvarkymą_,, S0B1Token: pertvarkymą_Turkija, S0B2Token: pertvarkymą_siekė, S0Token: pertvarkymą, S0_LastThreeLetters: mą, S0_LastTwoLetters: ą, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

12- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, Turkija, siekė ,.. ]

B0Token: ,, B0_LastThreeLetters: ,, B0_LastTwoLetters: ,, B1Token: Turkija, B1_LastThreeLetters: ija, B1_LastTwoLetters: ja, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [Turkija, siekė, padidinti ,.. ]

B0Token: Turkija, B0_LastThreeLetters: ija, B0_LastTwoLetters: ja, B1Token: siekė, B1_LastThreeLetters: kė, B1_LastTwoLetters: ė, S0B0Distance: 1, S0B0Token: ,_Turkija, S0B1Token: ,_siekė, S0B2Token: ,_padidinti, S0Token: ,, S0_LastThreeLetters: ,, S0_LastTwoLetters: ,, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

14- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Turkija, siekė, padidinti ,.. ]

B0Token: Turkija, B0_LastThreeLetters: ija, B0_LastTwoLetters: ja, B1Token: siekė, B1_LastThreeLetters: kė, B1_LastTwoLetters: ė, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Turkija]   B= [siekė, padidinti, civilių ,.. ]

B0Token: siekė, B0_LastThreeLetters: kė, B0_LastTwoLetters: ė, B1Token: padidinti, B1_LastThreeLetters: nti, B1_LastTwoLetters: ti, S0B0Distance: 1, S0B0Token: Turkija_siekė, S0B1Token: Turkija_padidinti, S0B2Token: Turkija_civilių, S0Token: Turkija, S0_LastThreeLetters: ija, S0_LastTwoLetters: ja, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

16- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [siekė, padidinti, civilių ,.. ]

B0Token: siekė, B0_LastThreeLetters: kė, B0_LastTwoLetters: ė, B1Token: padidinti, B1_LastThreeLetters: nti, B1_LastTwoLetters: ti, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [siekė]   B= [padidinti, civilių, institucijų ,.. ]

B0Token: padidinti, B0_LastThreeLetters: nti, B0_LastTwoLetters: ti, B1Token: civilių, B1_LastThreeLetters: ių, B1_LastTwoLetters: ų, S0B0Distance: 1, S0B0Token: siekė_padidinti, S0B1Token: siekė_civilių, S0B2Token: siekė_institucijų, S0Token: siekė, S0_LastThreeLetters: kė, S0_LastTwoLetters: ė, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

18- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [padidinti, civilių, institucijų ,.. ]

B0Token: padidinti, B0_LastThreeLetters: nti, B0_LastTwoLetters: ti, B1Token: civilių, B1_LastThreeLetters: ių, B1_LastTwoLetters: ų, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [padidinti]   B= [civilių, institucijų, įtaką ,.. ]

B0Token: civilių, B0_LastThreeLetters: ių, B0_LastTwoLetters: ų, B1Token: institucijų, B1_LastThreeLetters: jų, B1_LastTwoLetters: ų, S0B0Distance: 1, S0B0Token: padidinti_civilių, S0B1Token: padidinti_institucijų, S0B2Token: padidinti_įtaką, S0Token: padidinti, S0_LastThreeLetters: nti, S0_LastTwoLetters: ti, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

20- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [civilių, institucijų, įtaką ,.. ]

B0Token: civilių, B0_LastThreeLetters: ių, B0_LastTwoLetters: ų, B1Token: institucijų, B1_LastThreeLetters: jų, B1_LastTwoLetters: ų, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [civilių]   B= [institucijų, įtaką, , ,.. ]

B0Token: institucijų, B0_LastThreeLetters: jų, B0_LastTwoLetters: ų, B1Token: įtaką, B1_LastThreeLetters: ką, B1_LastTwoLetters: ą, S0B0Distance: 1, S0B0Token: civilių_institucijų, S0B1Token: civilių_įtaką, S0B2Token: civilių_,, S0Token: civilių, S0_LastThreeLetters: ių, S0_LastTwoLetters: ų, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

22- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [institucijų, įtaką, , ,.. ]

B0Token: institucijų, B0_LastThreeLetters: jų, B0_LastTwoLetters: ų, B1Token: įtaką, B1_LastThreeLetters: ką, B1_LastTwoLetters: ą, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

23- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [institucijų]   B= [įtaką, ,, taip ,.. ]

B0Token: įtaką, B0_LastThreeLetters: ką, B0_LastTwoLetters: ą, B1Token: ,, B1_LastThreeLetters: ,, B1_LastTwoLetters: ,, S0B0Distance: 1, S0B0Token: institucijų_įtaką, S0B1Token: institucijų_,, S0B2Token: institucijų_taip, S0Token: institucijų, S0_LastThreeLetters: jų, S0_LastTwoLetters: ų, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

24- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [įtaką, ,, taip ,.. ]

B0Token: įtaką, B0_LastThreeLetters: ką, B0_LastTwoLetters: ą, B1Token: ,, B1_LastThreeLetters: ,, B1_LastTwoLetters: ,, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

25- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [įtaką]   B= [,, taip, pat ,.. ]

B0Token: ,, B0_LastThreeLetters: ,, B0_LastTwoLetters: ,, B1Token: taip, B1_LastThreeLetters: aip, B1_LastTwoLetters: ip, S0B0Distance: 1, S0B0Token: įtaką_,, S0B1Token: įtaką_taip, S0B2Token: įtaką_pat, S0Token: įtaką, S0_LastThreeLetters: ką, S0_LastTwoLetters: ą, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

26- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, taip, pat ,.. ]

B0Token: ,, B0_LastThreeLetters: ,, B0_LastTwoLetters: ,, B1Token: taip, B1_LastThreeLetters: aip, B1_LastTwoLetters: ip, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

27- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [taip, pat, sustiprinti ,.. ]

B0Token: taip, B0_LastThreeLetters: aip, B0_LastTwoLetters: ip, B1Token: pat, B1_LastThreeLetters: pat, B1_LastTwoLetters: at, S0B0Distance: 1, S0B0Token: ,_taip, S0B1Token: ,_pat, S0B2Token: ,_sustiprinti, S0Token: ,, S0_LastThreeLetters: ,, S0_LastTwoLetters: ,, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

28- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [taip, pat, sustiprinti ,.. ]

B0Token: taip, B0_LastThreeLetters: aip, B0_LastTwoLetters: ip, B1Token: pat, B1_LastThreeLetters: pat, B1_LastTwoLetters: at, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

29- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [taip]   B= [pat, sustiprinti, prezidento ,.. ]

B0Token: pat, B0_LastThreeLetters: pat, B0_LastTwoLetters: at, B1Token: sustiprinti, B1_LastThreeLetters: nti, B1_LastTwoLetters: ti, S0B0Distance: 1, S0B0Token: taip_pat, S0B1Token: taip_sustiprinti, S0B2Token: taip_prezidento, S0Token: taip, S0_LastThreeLetters: aip, S0_LastTwoLetters: ip, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

30- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [pat, sustiprinti, prezidento ,.. ]

B0Token: pat, B0_LastThreeLetters: pat, B0_LastTwoLetters: at, B1Token: sustiprinti, B1_LastThreeLetters: nti, B1_LastTwoLetters: ti, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

31- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [pat]   B= [sustiprinti, prezidento, galias ,.. ]

B0Token: sustiprinti, B0_LastThreeLetters: nti, B0_LastTwoLetters: ti, B1Token: prezidento, B1_LastThreeLetters: nto, B1_LastTwoLetters: to, S0B0Distance: 1, S0B0Token: pat_sustiprinti, S0B1Token: pat_prezidento, S0B2Token: pat_galias, S0Token: pat, S0_LastThreeLetters: pat, S0_LastTwoLetters: at, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

32- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [sustiprinti, prezidento, galias ,.. ]

B0Token: sustiprinti, B0_LastThreeLetters: nti, B0_LastTwoLetters: ti, B1Token: prezidento, B1_LastThreeLetters: nto, B1_LastTwoLetters: to, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

33- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [sustiprinti]   B= [prezidento, galias, vykdyti ,.. ]

B0Token: prezidento, B0_LastThreeLetters: nto, B0_LastTwoLetters: to, B1Token: galias, B1_LastThreeLetters: ias, B1_LastTwoLetters: as, S0B0Distance: 1, S0B0Token: sustiprinti_prezidento, S0B1Token: sustiprinti_galias, S0B2Token: sustiprinti_vykdyti, S0Token: sustiprinti, S0_LastThreeLetters: nti, S0_LastTwoLetters: ti, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

34- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [prezidento, galias, vykdyti ,.. ]

B0Token: prezidento, B0_LastThreeLetters: nto, B0_LastTwoLetters: to, B1Token: galias, B1_LastThreeLetters: ias, B1_LastTwoLetters: as, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

35- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [prezidento]   B= [galias, vykdyti, priežiūrą ,.. ]

B0Token: galias, B0_LastThreeLetters: ias, B0_LastTwoLetters: as, B1Token: vykdyti, B1_LastThreeLetters: yti, B1_LastTwoLetters: ti, S0B0Distance: 1, S0B0Token: prezidento_galias, S0B1Token: prezidento_vykdyti, S0B2Token: prezidento_priežiūrą, S0Token: prezidento, S0_LastThreeLetters: nto, S0_LastTwoLetters: to, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

36- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [galias, vykdyti, priežiūrą ,.. ]

B0Token: galias, B0_LastThreeLetters: ias, B0_LastTwoLetters: as, B1Token: vykdyti, B1_LastThreeLetters: yti, B1_LastTwoLetters: ti, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

37- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [galias]   B= [vykdyti, priežiūrą, , ,.. ]

B0Token: vykdyti, B0_LastThreeLetters: yti, B0_LastTwoLetters: ti, B1Token: priežiūrą, B1_LastThreeLetters: rą, B1_LastTwoLetters: ą, S0B0Distance: 1, S0B0Token: galias_vykdyti, S0B1Token: galias_priežiūrą, S0B2Token: galias_,, S0Token: galias, S0_LastThreeLetters: ias, S0_LastTwoLetters: as, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

38- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [vykdyti, priežiūrą, , ,.. ]

B0Token: vykdyti, B0_LastThreeLetters: yti, B0_LastTwoLetters: ti, B1Token: priežiūrą, B1_LastThreeLetters: rą, B1_LastTwoLetters: ą, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

39- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [vykdyti]   B= [priežiūrą, ,, kad ,.. ]

B0Token: priežiūrą, B0_LastThreeLetters: rą, B0_LastTwoLetters: ą, B1Token: ,, B1_LastThreeLetters: ,, B1_LastTwoLetters: ,, S0B0Distance: 1, S0B0Token: vykdyti_priežiūrą, S0B1Token: vykdyti_,, S0B2Token: vykdyti_kad, S0Token: vykdyti, S0_LastThreeLetters: yti, S0_LastTwoLetters: ti, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

40- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [vykdyti, priežiūrą]   B= [,, kad, būtų ,.. ]

B0Token: ,, B0_LastThreeLetters: ,, B0_LastTwoLetters: ,, B1Token: kad, B1_LastThreeLetters: kad, B1_LastTwoLetters: ad, S0B0Distance: 1, S0B0Token: priežiūrą_,, S0B1Token: priežiūrą_kad, S0B2Token: priežiūrą_būtų, S0S1Distance: 1, S0Token: priežiūrą, S0_LastThreeLetters: rą, S0_LastTwoLetters: ą, S1B0Token: vykdyti_,, S1S0B0Token: vykdyti_priežiūrą_,, S1S0Token: vykdyti_priežiūrą, S1Token: vykdyti, S1_LastThreeLetters: yti, S1_LastTwoLetters: ti, StackLengthIs: 2, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

41- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[vykdyti, priežiūrą]]   B= [,, kad, būtų ,.. ]

B0Token: ,, B0_LastThreeLetters: ,, B0_LastTwoLetters: ,, B1Token: kad, B1_LastThreeLetters: kad, B1_LastTwoLetters: ad, S0B0Distance: 1, S0B0Token: vykdyti_priežiūrą_,, S0B1Token: vykdyti_priežiūrą_kad, S0B2Token: vykdyti_priežiūrą_būtų, S0Token: vykdyti_priežiūrą, TransHistory1: 0, TransHistory2: 00, TransHistory3: 002, 

42- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, kad, būtų ,.. ]

B0Token: ,, B0_LastThreeLetters: ,, B0_LastTwoLetters: ,, B1Token: kad, B1_LastThreeLetters: kad, B1_LastTwoLetters: ad, TransHistory1: 1, TransHistory2: 10, TransHistory3: 100, 

43- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [kad, būtų, užkirstas ,.. ]

B0Token: kad, B0_LastThreeLetters: kad, B0_LastTwoLetters: ad, B1Token: būtų, B1_LastThreeLetters: tų, B1_LastTwoLetters: ų, S0B0Distance: 1, S0B0Token: ,_kad, S0B1Token: ,_būtų, S0B2Token: ,_užkirstas, S0Token: ,, S0_LastThreeLetters: ,, S0_LastTwoLetters: ,, TransHistory1: 2, TransHistory2: 21, TransHistory3: 210, 

44- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [kad, būtų, užkirstas ,.. ]

B0Token: kad, B0_LastThreeLetters: kad, B0_LastTwoLetters: ad, B1Token: būtų, B1_LastThreeLetters: tų, B1_LastTwoLetters: ų, TransHistory1: 0, TransHistory2: 02, TransHistory3: 021, 

45- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [kad]   B= [būtų, užkirstas, bet ,.. ]

B0Token: būtų, B0_LastThreeLetters: tų, B0_LastTwoLetters: ų, B1Token: užkirstas, B1_LastThreeLetters: tas, B1_LastTwoLetters: as, S0B0Distance: 1, S0B0Token: kad_būtų, S0B1Token: kad_užkirstas, S0B2Token: kad_bet, S0Token: kad, S0_LastThreeLetters: kad, S0_LastTwoLetters: ad, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

46- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [būtų, užkirstas, bet ,.. ]

B0Token: būtų, B0_LastThreeLetters: tų, B0_LastTwoLetters: ų, B1Token: užkirstas, B1_LastThreeLetters: tas, B1_LastTwoLetters: as, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

47- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [būtų]   B= [užkirstas, bet, kokia ,.. ]

B0Token: užkirstas, B0_LastThreeLetters: tas, B0_LastTwoLetters: as, B1Token: bet, B1_LastThreeLetters: bet, B1_LastTwoLetters: et, S0B0Distance: 1, S0B0Token: būtų_užkirstas, S0B1Token: būtų_bet, S0B2Token: būtų_kokia, S0Token: būtų, S0_LastThreeLetters: tų, S0_LastTwoLetters: ų, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

48- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [užkirstas, bet, kokia ,.. ]

B0Token: užkirstas, B0_LastThreeLetters: tas, B0_LastTwoLetters: as, B1Token: bet, B1_LastThreeLetters: bet, B1_LastTwoLetters: et, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

49- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [užkirstas]   B= [bet, kokia, galimybė ,.. ]

B0Token: bet, B0_LastThreeLetters: bet, B0_LastTwoLetters: et, B1Token: kokia, B1_LastThreeLetters: kia, B1_LastTwoLetters: ia, S0B0Distance: 1, S0B0Token: užkirstas_bet, S0B1Token: užkirstas_kokia, S0B2Token: užkirstas_galimybė, S0Token: užkirstas, S0_LastThreeLetters: tas, S0_LastTwoLetters: as, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

50- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [bet, kokia, galimybė ,.. ]

B0Token: bet, B0_LastThreeLetters: bet, B0_LastTwoLetters: et, B1Token: kokia, B1_LastThreeLetters: kia, B1_LastTwoLetters: ia, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

51- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [bet]   B= [kokia, galimybė, įvykdyti ,.. ]

B0Token: kokia, B0_LastThreeLetters: kia, B0_LastTwoLetters: ia, B1Token: galimybė, B1_LastThreeLetters: bė, B1_LastTwoLetters: ė, S0B0Distance: 1, S0B0Token: bet_kokia, S0B1Token: bet_galimybė, S0B2Token: bet_įvykdyti, S0Token: bet, S0_LastThreeLetters: bet, S0_LastTwoLetters: et, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

52- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [kokia, galimybė, įvykdyti ,.. ]

B0Token: kokia, B0_LastThreeLetters: kia, B0_LastTwoLetters: ia, B1Token: galimybė, B1_LastThreeLetters: bė, B1_LastTwoLetters: ė, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

53- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [kokia]   B= [galimybė, įvykdyti, perversmą ,.. ]

B0Token: galimybė, B0_LastThreeLetters: bė, B0_LastTwoLetters: ė, B1Token: įvykdyti, B1_LastThreeLetters: yti, B1_LastTwoLetters: ti, S0B0Distance: 1, S0B0Token: kokia_galimybė, S0B1Token: kokia_įvykdyti, S0B2Token: kokia_perversmą, S0Token: kokia, S0_LastThreeLetters: kia, S0_LastTwoLetters: ia, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

54- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [galimybė, įvykdyti, perversmą ,.. ]

B0Token: galimybė, B0_LastThreeLetters: bė, B0_LastTwoLetters: ė, B1Token: įvykdyti, B1_LastThreeLetters: yti, B1_LastTwoLetters: ti, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

55- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [galimybė]   B= [įvykdyti, perversmą, . ,.. ]

B0Token: įvykdyti, B0_LastThreeLetters: yti, B0_LastTwoLetters: ti, B1Token: perversmą, B1_LastThreeLetters: mą, B1_LastTwoLetters: ą, S0B0Distance: 1, S0B0Token: galimybė_įvykdyti, S0B1Token: galimybė_perversmą, S0B2Token: galimybė_., S0Token: galimybė, S0_LastThreeLetters: bė, S0_LastTwoLetters: ė, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

56- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [įvykdyti, perversmą, . ,.. ]

B0Token: įvykdyti, B0_LastThreeLetters: yti, B0_LastTwoLetters: ti, B1Token: perversmą, B1_LastThreeLetters: mą, B1_LastTwoLetters: ą, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

57- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [įvykdyti]   B= [perversmą, . ,.. ]

B0Token: perversmą, B0_LastThreeLetters: mą, B0_LastTwoLetters: ą, B1Token: ., B1_LastThreeLetters: ., B1_LastTwoLetters: ., S0B0Distance: 1, S0B0Token: įvykdyti_perversmą, S0B1Token: įvykdyti_., S0Token: įvykdyti, S0_LastThreeLetters: yti, S0_LastTwoLetters: ti, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

58- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [įvykdyti, perversmą]   B= [.]

B0Token: ., B0_LastThreeLetters: ., B0_LastTwoLetters: ., S0B0Distance: 1, S0B0Token: perversmą_., S0S1Distance: 1, S0Token: perversmą, S0_LastThreeLetters: mą, S0_LastTwoLetters: ą, S1B0Token: įvykdyti_., S1S0B0Token: įvykdyti_perversmą_., S1S0Token: įvykdyti_perversmą, S1Token: įvykdyti, S1_LastThreeLetters: yti, S1_LastTwoLetters: ti, StackLengthIs: 2, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

59- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[įvykdyti, perversmą]]   B= [.]

B0Token: ., B0_LastThreeLetters: ., B0_LastTwoLetters: ., S0B0Distance: 1, S0B0Token: įvykdyti_perversmą_., S0Token: įvykdyti_perversmą, TransHistory1: 0, TransHistory2: 00, TransHistory3: 002, 

60- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [.]

B0Token: ., B0_LastThreeLetters: ., B0_LastTwoLetters: ., TransHistory1: 1, TransHistory2: 10, TransHistory3: 100, 

61- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [ ]

S0Token: ., S0_LastThreeLetters: ., S0_LastTwoLetters: ., TransHistory1: 2, TransHistory2: 21, TransHistory3: 210, 

62- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

