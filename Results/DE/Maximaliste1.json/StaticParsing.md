## Sentence No. 429 - 
Da die alte Mauer den Erddruck von der äußeren Ringmauer genommen hat , geht man inzwischen davon aus , dass das dauerhafte Eindringen von Wasser und Frostsprengungen zum schlechten Zustand der Mauer und damit zum Einsturz geführt hatten . 
### Existing MWEs: 
1- **geht aus** (VPC)
2- **geht davon aus** (ID), Interleaving 



0- &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Da, die, alte ,.. ]

B0Lemma: da, B0POS: SCONJ, B0Token: Da, B1Lemma: der, B1POS: DET, B1Token: die, 

1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Da]   B= [die, alte, Mauer ,.. ]

B0Lemma: der, B0POS: DET, B0Token: die, B1Lemma: alt, B1POS: ADJ, B1Token: alte, S0B0Distance: 1, S0B0Lemma: da_der, S0B0LemmaPOS: da_DET, S0B0POS: SCONJ_DET, S0B0POSLemma: SCONJ_der, S0B0Token: Da_die, S0B1Lemma: da_alt, S0B1LemmaPOS: da_ADJ, S0B1POS: SCONJ_ADJ, S0B1POSLemma: SCONJ_alt, S0B1Token: Da_alte, S0B2Lemma: da_Mauer, S0B2LemmaPOS: da_NOUN, S0B2POS: SCONJ_NOUN, S0B2POSLemma: SCONJ_Mauer, S0B2Token: Da_Mauer, S0Lemma: da, S0POS: SCONJ, S0Token: Da, StackLength: 1, da_isGouvernedBy_nehmen: true, da_isGouvernedBy_nehmen_mark: true, 

2- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [die, alte, Mauer ,.. ]

B0Lemma: der, B0POS: DET, B0Token: die, B1Lemma: alt, B1POS: ADJ, B1Token: alte, transitionHistoryLength1: 0, 

3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [die]   B= [alte, Mauer, den ,.. ]

B0Lemma: alt, B0POS: ADJ, B0Token: alte, B1Lemma: Mauer, B1POS: NOUN, B1Token: Mauer, S0B0Distance: 1, S0B0Lemma: der_alt, S0B0LemmaPOS: der_ADJ, S0B0POS: DET_ADJ, S0B0POSLemma: DET_alt, S0B0Token: die_alte, S0B1Lemma: der_Mauer, S0B1LemmaPOS: der_NOUN, S0B1POS: DET_NOUN, S0B1POSLemma: DET_Mauer, S0B1Token: die_Mauer, S0B2Lemma: der_der, S0B2LemmaPOS: der_DET, S0B2POS: DET_DET, S0B2POSLemma: DET_der, S0B2Token: die_den, S0Lemma: der, S0POS: DET, S0Token: die, StackLength: 1, der_isGouvernedBy_Mauer: true, der_isGouvernedBy_Mauer_det: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, 

4- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [alte, Mauer, den ,.. ]

B0Lemma: alt, B0POS: ADJ, B0Token: alte, B1Lemma: Mauer, B1POS: NOUN, B1Token: Mauer, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [alte]   B= [Mauer, den, Erddruck ,.. ]

B0Lemma: Mauer, B0POS: NOUN, B0Token: Mauer, B1Lemma: der, B1POS: DET, B1Token: den, S0B0Distance: 1, S0B0Lemma: alt_Mauer, S0B0LemmaPOS: alt_NOUN, S0B0POS: ADJ_NOUN, S0B0POSLemma: ADJ_Mauer, S0B0Token: alte_Mauer, S0B1Lemma: alt_der, S0B1LemmaPOS: alt_DET, S0B1POS: ADJ_DET, S0B1POSLemma: ADJ_der, S0B1Token: alte_den, S0B2Lemma: alt_Erddruck, S0B2LemmaPOS: alt_NOUN, S0B2POS: ADJ_NOUN, S0B2POSLemma: ADJ_Erddruck, S0B2Token: alte_Erddruck, S0Lemma: alt, S0POS: ADJ, S0Token: alte, StackLength: 1, alt_isGouvernedBy_Mauer: true, alt_isGouvernedBy_Mauer_amod: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

6- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Mauer, den, Erddruck ,.. ]

B0Lemma: Mauer, B0POS: NOUN, B0Token: Mauer, B1Lemma: der, B1POS: DET, B1Token: den, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Mauer]   B= [den, Erddruck, von ,.. ]

B0Lemma: der, B0POS: DET, B0Token: den, B1Lemma: Erddruck, B1POS: NOUN, B1Token: Erddruck, Mauer_isGouvernedBy_nehmen: true, Mauer_isGouvernedBy_nehmen_nsubj: true, S0B0Distance: 1, S0B0Lemma: Mauer_der, S0B0LemmaPOS: Mauer_DET, S0B0POS: NOUN_DET, S0B0POSLemma: NOUN_der, S0B0Token: Mauer_den, S0B1Lemma: Mauer_Erddruck, S0B1LemmaPOS: Mauer_NOUN, S0B1POS: NOUN_NOUN, S0B1POSLemma: NOUN_Erddruck, S0B1Token: Mauer_Erddruck, S0B2Lemma: Mauer_von, S0B2LemmaPOS: Mauer_ADP, S0B2POS: NOUN_ADP, S0B2POSLemma: NOUN_von, S0B2Token: Mauer_von, S0Lemma: Mauer, S0POS: NOUN, S0Token: Mauer, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

8- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [den, Erddruck, von ,.. ]

B0Lemma: der, B0POS: DET, B0Token: den, B1Lemma: Erddruck, B1POS: NOUN, B1Token: Erddruck, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [den]   B= [Erddruck, von, der ,.. ]

B0Lemma: Erddruck, B0POS: NOUN, B0Token: Erddruck, B1Lemma: von, B1POS: ADP, B1Token: von, S0B0Distance: 1, S0B0Lemma: der_Erddruck, S0B0LemmaPOS: der_NOUN, S0B0POS: DET_NOUN, S0B0POSLemma: DET_Erddruck, S0B0Token: den_Erddruck, S0B1Lemma: der_von, S0B1LemmaPOS: der_ADP, S0B1POS: DET_ADP, S0B1POSLemma: DET_von, S0B1Token: den_von, S0B2Lemma: der_der, S0B2LemmaPOS: der_DET, S0B2POS: DET_DET, S0B2POSLemma: DET_der, S0B2Token: den_der, S0Lemma: der, S0POS: DET, S0Token: den, StackLength: 1, der_isGouvernedBy_Erddruck: true, der_isGouvernedBy_Erddruck_det: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

10- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Erddruck, von, der ,.. ]

B0Lemma: Erddruck, B0POS: NOUN, B0Token: Erddruck, B1Lemma: von, B1POS: ADP, B1Token: von, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Erddruck]   B= [von, der, äußeren ,.. ]

B0Lemma: von, B0POS: ADP, B0Token: von, B1Lemma: der, B1POS: DET, B1Token: der, Erddruck_isGouvernedBy_nehmen: true, Erddruck_isGouvernedBy_nehmen_dobj: true, S0B0Distance: 1, S0B0Lemma: Erddruck_von, S0B0LemmaPOS: Erddruck_ADP, S0B0POS: NOUN_ADP, S0B0POSLemma: NOUN_von, S0B0Token: Erddruck_von, S0B1Lemma: Erddruck_der, S0B1LemmaPOS: Erddruck_DET, S0B1POS: NOUN_DET, S0B1POSLemma: NOUN_der, S0B1Token: Erddruck_der, S0B2Lemma: Erddruck_äußer, S0B2LemmaPOS: Erddruck_ADJ, S0B2POS: NOUN_ADJ, S0B2POSLemma: NOUN_äußer, S0B2Token: Erddruck_äußeren, S0Lemma: Erddruck, S0POS: NOUN, S0Token: Erddruck, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

12- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [von, der, äußeren ,.. ]

B0Lemma: von, B0POS: ADP, B0Token: von, B1Lemma: der, B1POS: DET, B1Token: der, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [von]   B= [der, äußeren, Ringmauer ,.. ]

B0Lemma: der, B0POS: DET, B0Token: der, B1Lemma: äußer, B1POS: ADJ, B1Token: äußeren, S0B0Distance: 1, S0B0Lemma: von_der, S0B0LemmaPOS: von_DET, S0B0POS: ADP_DET, S0B0POSLemma: ADP_der, S0B0Token: von_der, S0B1Lemma: von_äußer, S0B1LemmaPOS: von_ADJ, S0B1POS: ADP_ADJ, S0B1POSLemma: ADP_äußer, S0B1Token: von_äußeren, S0B2Lemma: von_Ringmauer, S0B2LemmaPOS: von_NOUN, S0B2POS: ADP_NOUN, S0B2POSLemma: ADP_Ringmauer, S0B2Token: von_Ringmauer, S0Lemma: von, S0POS: ADP, S0Token: von, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, von_isGouvernedBy_Ringmauer: true, von_isGouvernedBy_Ringmauer_case: true, 

14- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [der, äußeren, Ringmauer ,.. ]

B0Lemma: der, B0POS: DET, B0Token: der, B1Lemma: äußer, B1POS: ADJ, B1Token: äußeren, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [der]   B= [äußeren, Ringmauer, genommen ,.. ]

B0Lemma: äußer, B0POS: ADJ, B0Token: äußeren, B1Lemma: Ringmauer, B1POS: NOUN, B1Token: Ringmauer, S0B0Distance: 1, S0B0Lemma: der_äußer, S0B0LemmaPOS: der_ADJ, S0B0POS: DET_ADJ, S0B0POSLemma: DET_äußer, S0B0Token: der_äußeren, S0B1Lemma: der_Ringmauer, S0B1LemmaPOS: der_NOUN, S0B1POS: DET_NOUN, S0B1POSLemma: DET_Ringmauer, S0B1Token: der_Ringmauer, S0B2Lemma: der_nehmen, S0B2LemmaPOS: der_VERB, S0B2POS: DET_VERB, S0B2POSLemma: DET_nehmen, S0B2Token: der_genommen, S0Lemma: der, S0POS: DET, S0Token: der, StackLength: 1, der_isGouvernedBy_Ringmauer: true, der_isGouvernedBy_Ringmauer_det: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

16- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [äußeren, Ringmauer, genommen ,.. ]

B0Lemma: äußer, B0POS: ADJ, B0Token: äußeren, B1Lemma: Ringmauer, B1POS: NOUN, B1Token: Ringmauer, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [äußeren]   B= [Ringmauer, genommen, hat ,.. ]

B0Lemma: Ringmauer, B0POS: NOUN, B0Token: Ringmauer, B1Lemma: nehmen, B1POS: VERB, B1Token: genommen, S0B0Distance: 1, S0B0Lemma: äußer_Ringmauer, S0B0LemmaPOS: äußer_NOUN, S0B0POS: ADJ_NOUN, S0B0POSLemma: ADJ_Ringmauer, S0B0Token: äußeren_Ringmauer, S0B1Lemma: äußer_nehmen, S0B1LemmaPOS: äußer_VERB, S0B1POS: ADJ_VERB, S0B1POSLemma: ADJ_nehmen, S0B1Token: äußeren_genommen, S0B2Lemma: äußer_haben, S0B2LemmaPOS: äußer_AUX, S0B2POS: ADJ_AUX, S0B2POSLemma: ADJ_haben, S0B2Token: äußeren_hat, S0Lemma: äußer, S0POS: ADJ, S0Token: äußeren, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, äußer_isGouvernedBy_Ringmauer: true, äußer_isGouvernedBy_Ringmauer_amod: true, 

18- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Ringmauer, genommen, hat ,.. ]

B0Lemma: Ringmauer, B0POS: NOUN, B0Token: Ringmauer, B1Lemma: nehmen, B1POS: VERB, B1Token: genommen, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Ringmauer]   B= [genommen, hat, , ,.. ]

B0Lemma: nehmen, B0POS: VERB, B0Token: genommen, B1Lemma: haben, B1POS: AUX, B1Token: hat, Ringmauer_isGouvernedBy_nehmen: true, Ringmauer_isGouvernedBy_nehmen_nsubj: true, S0B0Distance: 1, S0B0Lemma: Ringmauer_nehmen, S0B0LemmaPOS: Ringmauer_VERB, S0B0POS: NOUN_VERB, S0B0POSLemma: NOUN_nehmen, S0B0Token: Ringmauer_genommen, S0B1Lemma: Ringmauer_haben, S0B1LemmaPOS: Ringmauer_AUX, S0B1POS: NOUN_AUX, S0B1POSLemma: NOUN_haben, S0B1Token: Ringmauer_hat, S0B2Lemma: Ringmauer_,, S0B2LemmaPOS: Ringmauer_PUNCT, S0B2POS: NOUN_PUNCT, S0B2POSLemma: NOUN_,, S0B2Token: Ringmauer_,, S0Lemma: Ringmauer, S0POS: NOUN, S0Token: Ringmauer, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

20- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [genommen, hat, , ,.. ]

B0Lemma: nehmen, B0POS: VERB, B0Token: genommen, B1Lemma: haben, B1POS: AUX, B1Token: hat, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [genommen]   B= [hat, ,, geht ,.. ]

B0Lemma: haben, B0POS: AUX, B0Token: hat, B1Lemma: ,, B1POS: PUNCT, B1Token: ,, S0B0Distance: 1, S0B0Lemma: nehmen_haben, S0B0LemmaPOS: nehmen_AUX, S0B0POS: VERB_AUX, S0B0POSLemma: VERB_haben, S0B0Token: genommen_hat, S0B1Lemma: nehmen_,, S0B1LemmaPOS: nehmen_PUNCT, S0B1POS: VERB_PUNCT, S0B1POSLemma: VERB_,, S0B1Token: genommen_,, S0B2Lemma: nehmen_gehen, S0B2LemmaPOS: nehmen_VERB, S0B2POS: VERB_VERB, S0B2POSLemma: VERB_gehen, S0B2Token: genommen_geht, S0Lemma: nehmen, S0POS: VERB, S0Token: genommen, StackLength: 1, hasRighDep_aux: true, nehmen_haben_hasRighDep_aux: true, nehmen_hasRighDep_aux: true, nehmen_isGouvernedBy_gehen: true, nehmen_isGouvernedBy_gehen_advcl: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

22- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [hat, ,, geht ,.. ]

B0Lemma: haben, B0POS: AUX, B0Token: hat, B1Lemma: ,, B1POS: PUNCT, B1Token: ,, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

23- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [hat]   B= [,, geht, man ,.. ]

B0Lemma: ,, B0POS: PUNCT, B0Token: ,, B1Lemma: gehen, B1POS: VERB, B1Token: geht, S0B0Distance: 1, S0B0Lemma: haben_,, S0B0LemmaPOS: haben_PUNCT, S0B0POS: AUX_PUNCT, S0B0POSLemma: AUX_,, S0B0Token: hat_,, S0B1Lemma: haben_gehen, S0B1LemmaPOS: haben_VERB, S0B1POS: AUX_VERB, S0B1POSLemma: AUX_gehen, S0B1Token: hat_geht, S0B2Lemma: haben_man, S0B2LemmaPOS: haben_PRON, S0B2POS: AUX_PRON, S0B2POSLemma: AUX_man, S0B2Token: hat_man, S0Lemma: haben, S0POS: AUX, S0Token: hat, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

24- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, geht, man ,.. ]

B0Lemma: ,, B0POS: PUNCT, B0Token: ,, B1Lemma: gehen, B1POS: VERB, B1Token: geht, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

25- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [geht, man, inzwischen ,.. ]

,_isGouvernedBy_gehen: true, ,_isGouvernedBy_gehen_punct: true, B0Lemma: gehen, B0POS: VERB, B0Token: geht, B1Lemma: man, B1POS: PRON, B1Token: man, S0B0Distance: 1, S0B0Lemma: ,_gehen, S0B0LemmaPOS: ,_VERB, S0B0POS: PUNCT_VERB, S0B0POSLemma: PUNCT_gehen, S0B0Token: ,_geht, S0B1Lemma: ,_man, S0B1LemmaPOS: ,_PRON, S0B1POS: PUNCT_PRON, S0B1POSLemma: PUNCT_man, S0B1Token: ,_man, S0B2Lemma: ,_inzwischen, S0B2LemmaPOS: ,_ADV, S0B2POS: PUNCT_ADV, S0B2POSLemma: PUNCT_inzwischen, S0B2Token: ,_inzwischen, S0Lemma: ,, S0POS: PUNCT, S0Token: ,, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

26- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [geht, man, inzwischen ,.. ]

B0Lemma: gehen, B0POS: VERB, B0Token: geht, B1Lemma: man, B1POS: PRON, B1Token: man, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

27- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [geht]   B= [man, inzwischen, davon ,.. ]

B0Lemma: man, B0POS: PRON, B0Token: man, B1Lemma: inzwischen, B1POS: ADV, B1Token: inzwischen, S0B0Distance: 1, S0B0Lemma: gehen_man, S0B0LemmaPOS: gehen_PRON, S0B0POS: VERB_PRON, S0B0POSLemma: VERB_man, S0B0Token: geht_man, S0B1Lemma: gehen_inzwischen, S0B1LemmaPOS: gehen_ADV, S0B1POS: VERB_ADV, S0B1POSLemma: VERB_inzwischen, S0B1Token: geht_inzwischen, S0B2Lemma: gehen_davon, S0B2LemmaPOS: gehen_PRON, S0B2POS: VERB_PRON, S0B2POSLemma: VERB_davon, S0B2Token: geht_davon, S0Lemma: gehen, S0POS: VERB, S0Token: geht, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

28- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [geht, man]   B= [inzwischen, davon, aus ,.. ]

B0Lemma: inzwischen, B0POS: ADV, B0Token: inzwischen, B1Lemma: davon, B1POS: PRON, B1Token: davon, S0B0Distance: 1, S0B0Lemma: man_inzwischen, S0B0LemmaPOS: man_ADV, S0B0POS: PRON_ADV, S0B0POSLemma: PRON_inzwischen, S0B0Token: man_inzwischen, S0B1Lemma: man_davon, S0B1LemmaPOS: man_PRON, S0B1POS: PRON_PRON, S0B1POSLemma: PRON_davon, S0B1Token: man_davon, S0B2Lemma: man_aus, S0B2LemmaPOS: man_ADP, S0B2POS: PRON_ADP, S0B2POSLemma: PRON_aus, S0B2Token: man_aus, S0Lemma: man, S0POS: PRON, S0S1Distance: 1, S0Token: man, S1B0Lemma: gehen_inzwischen, S1B0LemmaPOS: gehen_ADV, S1B0POS: VERB_ADV, S1B0POSLemma: VERB_inzwischen, S1B0Token: geht_inzwischen, S1Lemma: gehen, S1POS: VERB, S1S0B0Lemma: gehen_man_inzwischen, S1S0B0LemmaPOS: gehen_PRON_ADV, S1S0B0POS: VERB_PRON_ADV, S1S0B0POSLemma: VERB_PRON_inzwischen, S1S0B0Token: geht_man_inzwischen, S1S0Lemma: gehen_man, S1S0LemmaPOS: gehen_PRON, S1S0POS: VERB_PRON, S1S0POSLemma: VERB_man, S1S0Token: geht_man, S1Token: geht, StackLength: 2, SyntaxicRelation: +nsubj, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

29- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [geht]   B= [inzwischen, davon, aus ,.. ]

B0Lemma: inzwischen, B0POS: ADV, B0Token: inzwischen, B1Lemma: davon, B1POS: PRON, B1Token: davon, S0B0Distance: 2, S0B0Lemma: gehen_inzwischen, S0B0LemmaPOS: gehen_ADV, S0B0POS: VERB_ADV, S0B0POSLemma: VERB_inzwischen, S0B0Token: geht_inzwischen, S0B1Lemma: gehen_davon, S0B1LemmaPOS: gehen_PRON, S0B1POS: VERB_PRON, S0B1POSLemma: VERB_davon, S0B1Token: geht_davon, S0B2Lemma: gehen_aus, S0B2LemmaPOS: gehen_ADP, S0B2POS: VERB_ADP, S0B2POSLemma: VERB_aus, S0B2Token: geht_aus, S0Lemma: gehen, S0POS: VERB, S0Token: geht, StackLength: 1, transitionHistoryLength1: 0, transitionHistoryLength2: 00, transitionHistoryLength3: 002, 

30- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [geht, inzwischen]   B= [davon, aus, , ,.. ]

B0Lemma: davon, B0POS: PRON, B0Token: davon, B1Lemma: aus, B1POS: ADP, B1Token: aus, S0B0Distance: 1, S0B0Lemma: inzwischen_davon, S0B0LemmaPOS: inzwischen_PRON, S0B0POS: ADV_PRON, S0B0POSLemma: ADV_davon, S0B0Token: inzwischen_davon, S0B1Lemma: inzwischen_aus, S0B1LemmaPOS: inzwischen_ADP, S0B1POS: ADV_ADP, S0B1POSLemma: ADV_aus, S0B1Token: inzwischen_aus, S0B2Lemma: inzwischen_,, S0B2LemmaPOS: inzwischen_PUNCT, S0B2POS: ADV_PUNCT, S0B2POSLemma: ADV_,, S0B2Token: inzwischen_,, S0Lemma: inzwischen, S0POS: ADV, S0S1Distance: 2, S0Token: inzwischen, S1B0Lemma: gehen_davon, S1B0LemmaPOS: gehen_PRON, S1B0POS: VERB_PRON, S1B0POSLemma: VERB_davon, S1B0Token: geht_davon, S1Lemma: gehen, S1POS: VERB, S1S0B0Lemma: gehen_inzwischen_davon, S1S0B0LemmaPOS: gehen_ADV_PRON, S1S0B0POS: VERB_ADV_PRON, S1S0B0POSLemma: VERB_ADV_davon, S1S0B0Token: geht_inzwischen_davon, S1S0Lemma: gehen_inzwischen, S1S0LemmaPOS: gehen_ADV, S1S0POS: VERB_ADV, S1S0POSLemma: VERB_inzwischen, S1S0Token: geht_inzwischen, S1Token: geht, StackLength: 2, SyntaxicRelation: +advmod, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 200, 

31- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [geht]   B= [davon, aus, , ,.. ]

B0Lemma: davon, B0POS: PRON, B0Token: davon, B1Lemma: aus, B1POS: ADP, B1Token: aus, S0B0Distance: 3, S0B0Lemma: gehen_davon, S0B0LemmaPOS: gehen_PRON, S0B0POS: VERB_PRON, S0B0POSLemma: VERB_davon, S0B0Token: geht_davon, S0B1Lemma: gehen_aus, S0B1LemmaPOS: gehen_ADP, S0B1POS: VERB_ADP, S0B1POSLemma: VERB_aus, S0B1Token: geht_aus, S0B2Lemma: gehen_,, S0B2LemmaPOS: gehen_PUNCT, S0B2POS: VERB_PUNCT, S0B2POSLemma: VERB_,, S0B2Token: geht_,, S0Lemma: gehen, S0POS: VERB, S0Token: geht, StackLength: 1, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

32- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [geht, davon]   B= [aus, ,, dass ,.. ]

B0Lemma: aus, B0POS: ADP, B0Token: aus, B1Lemma: ,, B1POS: PUNCT, B1Token: ,, S0B0Distance: 1, S0B0Lemma: davon_aus, S0B0LemmaPOS: davon_ADP, S0B0POS: PRON_ADP, S0B0POSLemma: PRON_aus, S0B0Token: davon_aus, S0B1Lemma: davon_,, S0B1LemmaPOS: davon_PUNCT, S0B1POS: PRON_PUNCT, S0B1POSLemma: PRON_,, S0B1Token: davon_,, S0B2Lemma: davon_dass, S0B2LemmaPOS: davon_SCONJ, S0B2POS: PRON_SCONJ, S0B2POSLemma: PRON_dass, S0B2Token: davon_dass, S0Lemma: davon, S0POS: PRON, S0S1Distance: 3, S0Token: davon, S1B0Lemma: gehen_aus, S1B0LemmaPOS: gehen_ADP, S1B0POS: VERB_ADP, S1B0POSLemma: VERB_aus, S1B0Token: geht_aus, S1Lemma: gehen, S1POS: VERB, S1S0B0Lemma: gehen_davon_aus, S1S0B0LemmaPOS: gehen_PRON_ADP, S1S0B0POS: VERB_PRON_ADP, S1S0B0POSLemma: VERB_PRON_aus, S1S0B0Token: geht_davon_aus, S1S0Lemma: gehen_davon, S1S0LemmaPOS: gehen_PRON, S1S0POS: VERB_PRON, S1S0POSLemma: VERB_davon, S1S0Token: geht_davon, S1Token: geht, StackLength: 2, SyntaxicRelation: +dep, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

33- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [geht]   B= [aus, ,, dass ,.. ]

B0Lemma: aus, B0POS: ADP, B0Token: aus, B1Lemma: ,, B1POS: PUNCT, B1Token: ,, S0B0Distance: 4, S0B0Lemma: gehen_aus, S0B0LemmaPOS: gehen_ADP, S0B0POS: VERB_ADP, S0B0POSLemma: VERB_aus, S0B0Token: geht_aus, S0B1Lemma: gehen_,, S0B1LemmaPOS: gehen_PUNCT, S0B1POS: VERB_PUNCT, S0B1POSLemma: VERB_,, S0B1Token: geht_,, S0B2Lemma: gehen_dass, S0B2LemmaPOS: gehen_SCONJ, S0B2POS: VERB_SCONJ, S0B2POSLemma: VERB_dass, S0B2Token: geht_dass, S0Lemma: gehen, S0POS: VERB, S0Token: geht, StackLength: 1, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

34- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [geht, aus]   B= [,, dass, das ,.. ]

B0Lemma: ,, B0POS: PUNCT, B0Token: ,, B1Lemma: dass, B1POS: SCONJ, B1Token: dass, S0B0Distance: 1, S0B0Lemma: aus_,, S0B0LemmaPOS: aus_PUNCT, S0B0POS: ADP_PUNCT, S0B0POSLemma: ADP_,, S0B0Token: aus_,, S0B1Lemma: aus_dass, S0B1LemmaPOS: aus_SCONJ, S0B1POS: ADP_SCONJ, S0B1POSLemma: ADP_dass, S0B1Token: aus_dass, S0B2Lemma: aus_der, S0B2LemmaPOS: aus_DET, S0B2POS: ADP_DET, S0B2POSLemma: ADP_der, S0B2Token: aus_das, S0Lemma: aus, S0POS: ADP, S0S1Distance: 4, S0Token: aus, S1B0Lemma: gehen_,, S1B0LemmaPOS: gehen_PUNCT, S1B0POS: VERB_PUNCT, S1B0POSLemma: VERB_,, S1B0Token: geht_,, S1Lemma: gehen, S1POS: VERB, S1S0B0Lemma: gehen_aus_,, S1S0B0LemmaPOS: gehen_ADP_PUNCT, S1S0B0POS: VERB_ADP_PUNCT, S1S0B0POSLemma: VERB_ADP_,, S1S0B0Token: geht_aus_,, S1S0Lemma: gehen_aus, S1S0LemmaPOS: gehen_ADP, S1S0POS: VERB_ADP, S1S0POSLemma: VERB_aus, S1S0Token: geht_aus, S1Token: geht, StackLength: 2, SyntaxicRelation: +compound:prt, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

35- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[geht, aus]]   B= [,, dass, das ,.. ]

B0Lemma: ,, B0POS: PUNCT, B0Token: ,, B1Lemma: dass, B1POS: SCONJ, B1Token: dass, S0B0Distance: 1, S0B0Lemma: gehen_aus_,, S0B0LemmaPOS: gehen_aus_PUNCT, S0B0POS: VERB_ADP_PUNCT, S0B0POSLemma: VERB_ADP_,, S0B0Token: geht_aus_,, S0B1Lemma: gehen_aus_dass, S0B1LemmaPOS: gehen_aus_SCONJ, S0B1POS: VERB_ADP_SCONJ, S0B1POSLemma: VERB_ADP_dass, S0B1Token: geht_aus_dass, S0B2Lemma: gehen_aus_der, S0B2LemmaPOS: gehen_aus_DET, S0B2POS: VERB_ADP_DET, S0B2POSLemma: VERB_ADP_der, S0B2Token: geht_aus_das, S0Lemma: gehen_aus, S0POS: VERB_ADP, S0Token: geht_aus, StackLength: 1, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

36- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, dass, das ,.. ]

B0Lemma: ,, B0POS: PUNCT, B0Token: ,, B1Lemma: dass, B1POS: SCONJ, B1Token: dass, transitionHistoryLength1: 1, transitionHistoryLength2: 10, transitionHistoryLength3: 102, 

37- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [dass, das, dauerhafte ,.. ]

B0Lemma: dass, B0POS: SCONJ, B0Token: dass, B1Lemma: der, B1POS: DET, B1Token: das, S0B0Distance: 1, S0B0Lemma: ,_dass, S0B0LemmaPOS: ,_SCONJ, S0B0POS: PUNCT_SCONJ, S0B0POSLemma: PUNCT_dass, S0B0Token: ,_dass, S0B1Lemma: ,_der, S0B1LemmaPOS: ,_DET, S0B1POS: PUNCT_DET, S0B1POSLemma: PUNCT_der, S0B1Token: ,_das, S0B2Lemma: ,_dauerhaft, S0B2LemmaPOS: ,_ADJ, S0B2POS: PUNCT_ADJ, S0B2POSLemma: PUNCT_dauerhaft, S0B2Token: ,_dauerhafte, S0Lemma: ,, S0POS: PUNCT, S0Token: ,, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 21, transitionHistoryLength3: 210, 

38- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [dass, das, dauerhafte ,.. ]

B0Lemma: dass, B0POS: SCONJ, B0Token: dass, B1Lemma: der, B1POS: DET, B1Token: das, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 021, 

39- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [dass]   B= [das, dauerhafte, Eindringen ,.. ]

B0Lemma: der, B0POS: DET, B0Token: das, B1Lemma: dauerhaft, B1POS: ADJ, B1Token: dauerhafte, S0B0Distance: 1, S0B0Lemma: dass_der, S0B0LemmaPOS: dass_DET, S0B0POS: SCONJ_DET, S0B0POSLemma: SCONJ_der, S0B0Token: dass_das, S0B1Lemma: dass_dauerhaft, S0B1LemmaPOS: dass_ADJ, S0B1POS: SCONJ_ADJ, S0B1POSLemma: SCONJ_dauerhaft, S0B1Token: dass_dauerhafte, S0B2Lemma: dass_Eindringen, S0B2LemmaPOS: dass_NOUN, S0B2POS: SCONJ_NOUN, S0B2POSLemma: SCONJ_Eindringen, S0B2Token: dass_Eindringen, S0Lemma: dass, S0POS: SCONJ, S0Token: dass, StackLength: 1, dass_isGouvernedBy_geführen: true, dass_isGouvernedBy_geführen_mark: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

40- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [das, dauerhafte, Eindringen ,.. ]

B0Lemma: der, B0POS: DET, B0Token: das, B1Lemma: dauerhaft, B1POS: ADJ, B1Token: dauerhafte, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

41- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [das]   B= [dauerhafte, Eindringen, von ,.. ]

B0Lemma: dauerhaft, B0POS: ADJ, B0Token: dauerhafte, B1Lemma: Eindringen, B1POS: NOUN, B1Token: Eindringen, S0B0Distance: 1, S0B0Lemma: der_dauerhaft, S0B0LemmaPOS: der_ADJ, S0B0POS: DET_ADJ, S0B0POSLemma: DET_dauerhaft, S0B0Token: das_dauerhafte, S0B1Lemma: der_Eindringen, S0B1LemmaPOS: der_NOUN, S0B1POS: DET_NOUN, S0B1POSLemma: DET_Eindringen, S0B1Token: das_Eindringen, S0B2Lemma: der_von, S0B2LemmaPOS: der_ADP, S0B2POS: DET_ADP, S0B2POSLemma: DET_von, S0B2Token: das_von, S0Lemma: der, S0POS: DET, S0Token: das, StackLength: 1, der_isGouvernedBy_Eindringen: true, der_isGouvernedBy_Eindringen_det: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

42- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [dauerhafte, Eindringen, von ,.. ]

B0Lemma: dauerhaft, B0POS: ADJ, B0Token: dauerhafte, B1Lemma: Eindringen, B1POS: NOUN, B1Token: Eindringen, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

43- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [dauerhafte]   B= [Eindringen, von, Wasser ,.. ]

B0Lemma: Eindringen, B0POS: NOUN, B0Token: Eindringen, B1Lemma: von, B1POS: ADP, B1Token: von, S0B0Distance: 1, S0B0Lemma: dauerhaft_Eindringen, S0B0LemmaPOS: dauerhaft_NOUN, S0B0POS: ADJ_NOUN, S0B0POSLemma: ADJ_Eindringen, S0B0Token: dauerhafte_Eindringen, S0B1Lemma: dauerhaft_von, S0B1LemmaPOS: dauerhaft_ADP, S0B1POS: ADJ_ADP, S0B1POSLemma: ADJ_von, S0B1Token: dauerhafte_von, S0B2Lemma: dauerhaft_Wasser, S0B2LemmaPOS: dauerhaft_NOUN, S0B2POS: ADJ_NOUN, S0B2POSLemma: ADJ_Wasser, S0B2Token: dauerhafte_Wasser, S0Lemma: dauerhaft, S0POS: ADJ, S0Token: dauerhafte, StackLength: 1, dauerhaft_isGouvernedBy_Eindringen: true, dauerhaft_isGouvernedBy_Eindringen_amod: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

44- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Eindringen, von, Wasser ,.. ]

B0Lemma: Eindringen, B0POS: NOUN, B0Token: Eindringen, B1Lemma: von, B1POS: ADP, B1Token: von, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

45- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Eindringen]   B= [von, Wasser, und ,.. ]

B0Lemma: von, B0POS: ADP, B0Token: von, B1Lemma: Wasser, B1POS: NOUN, B1Token: Wasser, Eindringen_Wasser_hasRighDep_nmod: true, Eindringen_hasRighDep_nmod: true, Eindringen_isGouvernedBy_geführen: true, Eindringen_isGouvernedBy_geführen_dobj: true, S0B0Distance: 1, S0B0Lemma: Eindringen_von, S0B0LemmaPOS: Eindringen_ADP, S0B0POS: NOUN_ADP, S0B0POSLemma: NOUN_von, S0B0Token: Eindringen_von, S0B1Lemma: Eindringen_Wasser, S0B1LemmaPOS: Eindringen_NOUN, S0B1POS: NOUN_NOUN, S0B1POSLemma: NOUN_Wasser, S0B1Token: Eindringen_Wasser, S0B2Lemma: Eindringen_und, S0B2LemmaPOS: Eindringen_CONJ, S0B2POS: NOUN_CONJ, S0B2POSLemma: NOUN_und, S0B2Token: Eindringen_und, S0Lemma: Eindringen, S0POS: NOUN, S0Token: Eindringen, StackLength: 1, hasRighDep_nmod: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

46- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [von, Wasser, und ,.. ]

B0Lemma: von, B0POS: ADP, B0Token: von, B1Lemma: Wasser, B1POS: NOUN, B1Token: Wasser, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

47- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [von]   B= [Wasser, und, Frostsprengungen ,.. ]

B0Lemma: Wasser, B0POS: NOUN, B0Token: Wasser, B1Lemma: und, B1POS: CONJ, B1Token: und, S0B0Distance: 1, S0B0Lemma: von_Wasser, S0B0LemmaPOS: von_NOUN, S0B0POS: ADP_NOUN, S0B0POSLemma: ADP_Wasser, S0B0Token: von_Wasser, S0B1Lemma: von_und, S0B1LemmaPOS: von_CONJ, S0B1POS: ADP_CONJ, S0B1POSLemma: ADP_und, S0B1Token: von_und, S0B2Lemma: von_Frostsprengung, S0B2LemmaPOS: von_NOUN, S0B2POS: ADP_NOUN, S0B2POSLemma: ADP_Frostsprengung, S0B2Token: von_Frostsprengungen, S0Lemma: von, S0POS: ADP, S0Token: von, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, von_isGouvernedBy_Wasser: true, von_isGouvernedBy_Wasser_case: true, 

48- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Wasser, und, Frostsprengungen ,.. ]

B0Lemma: Wasser, B0POS: NOUN, B0Token: Wasser, B1Lemma: und, B1POS: CONJ, B1Token: und, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

49- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Wasser]   B= [und, Frostsprengungen, zum ,.. ]

B0Lemma: und, B0POS: CONJ, B0Token: und, B1Lemma: Frostsprengung, B1POS: NOUN, B1Token: Frostsprengungen, S0B0Distance: 1, S0B0Lemma: Wasser_und, S0B0LemmaPOS: Wasser_CONJ, S0B0POS: NOUN_CONJ, S0B0POSLemma: NOUN_und, S0B0Token: Wasser_und, S0B1Lemma: Wasser_Frostsprengung, S0B1LemmaPOS: Wasser_NOUN, S0B1POS: NOUN_NOUN, S0B1POSLemma: NOUN_Frostsprengung, S0B1Token: Wasser_Frostsprengungen, S0B2Lemma: Wasser_zu+der, S0B2LemmaPOS: Wasser_ADP, S0B2POS: NOUN_ADP, S0B2POSLemma: NOUN_zu+der, S0B2Token: Wasser_zum, S0Lemma: Wasser, S0POS: NOUN, S0Token: Wasser, StackLength: 1, Wasser_Frostsprengung_hasRighDep_conj: true, Wasser_hasRighDep_cc: true, Wasser_hasRighDep_conj: true, Wasser_und_hasRighDep_cc: true, hasRighDep_cc: true, hasRighDep_conj: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

50- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [und, Frostsprengungen, zum ,.. ]

B0Lemma: und, B0POS: CONJ, B0Token: und, B1Lemma: Frostsprengung, B1POS: NOUN, B1Token: Frostsprengungen, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

51- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [und]   B= [Frostsprengungen, zum, schlechten ,.. ]

B0Lemma: Frostsprengung, B0POS: NOUN, B0Token: Frostsprengungen, B1Lemma: zu+der, B1POS: ADP, B1Token: zum, S0B0Distance: 1, S0B0Lemma: und_Frostsprengung, S0B0LemmaPOS: und_NOUN, S0B0POS: CONJ_NOUN, S0B0POSLemma: CONJ_Frostsprengung, S0B0Token: und_Frostsprengungen, S0B1Lemma: und_zu+der, S0B1LemmaPOS: und_ADP, S0B1POS: CONJ_ADP, S0B1POSLemma: CONJ_zu+der, S0B1Token: und_zum, S0B2Lemma: und_schlecht, S0B2LemmaPOS: und_ADJ, S0B2POS: CONJ_ADJ, S0B2POSLemma: CONJ_schlecht, S0B2Token: und_schlechten, S0Lemma: und, S0POS: CONJ, S0Token: und, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

52- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Frostsprengungen, zum, schlechten ,.. ]

B0Lemma: Frostsprengung, B0POS: NOUN, B0Token: Frostsprengungen, B1Lemma: zu+der, B1POS: ADP, B1Token: zum, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

53- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Frostsprengungen]   B= [zum, schlechten, Zustand ,.. ]

B0Lemma: zu+der, B0POS: ADP, B0Token: zum, B1Lemma: schlecht, B1POS: ADJ, B1Token: schlechten, S0B0Distance: 1, S0B0Lemma: Frostsprengung_zu+der, S0B0LemmaPOS: Frostsprengung_ADP, S0B0POS: NOUN_ADP, S0B0POSLemma: NOUN_zu+der, S0B0Token: Frostsprengungen_zum, S0B1Lemma: Frostsprengung_schlecht, S0B1LemmaPOS: Frostsprengung_ADJ, S0B1POS: NOUN_ADJ, S0B1POSLemma: NOUN_schlecht, S0B1Token: Frostsprengungen_schlechten, S0B2Lemma: Frostsprengung_Zustand, S0B2LemmaPOS: Frostsprengung_NOUN, S0B2POS: NOUN_NOUN, S0B2POSLemma: NOUN_Zustand, S0B2Token: Frostsprengungen_Zustand, S0Lemma: Frostsprengung, S0POS: NOUN, S0Token: Frostsprengungen, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

54- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [zum, schlechten, Zustand ,.. ]

B0Lemma: zu+der, B0POS: ADP, B0Token: zum, B1Lemma: schlecht, B1POS: ADJ, B1Token: schlechten, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

55- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [zum]   B= [schlechten, Zustand, der ,.. ]

B0Lemma: schlecht, B0POS: ADJ, B0Token: schlechten, B1Lemma: Zustand, B1POS: NOUN, B1Token: Zustand, S0B0Distance: 1, S0B0Lemma: zu+der_schlecht, S0B0LemmaPOS: zu+der_ADJ, S0B0POS: ADP_ADJ, S0B0POSLemma: ADP_schlecht, S0B0Token: zum_schlechten, S0B1Lemma: zu+der_Zustand, S0B1LemmaPOS: zu+der_NOUN, S0B1POS: ADP_NOUN, S0B1POSLemma: ADP_Zustand, S0B1Token: zum_Zustand, S0B2Lemma: zu+der_der, S0B2LemmaPOS: zu+der_DET, S0B2POS: ADP_DET, S0B2POSLemma: ADP_der, S0B2Token: zum_der, S0Lemma: zu+der, S0POS: ADP, S0Token: zum, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, zu+der_isGouvernedBy_Zustand: true, zu+der_isGouvernedBy_Zustand_case: true, 

56- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [schlechten, Zustand, der ,.. ]

B0Lemma: schlecht, B0POS: ADJ, B0Token: schlechten, B1Lemma: Zustand, B1POS: NOUN, B1Token: Zustand, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

57- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [schlechten]   B= [Zustand, der, Mauer ,.. ]

B0Lemma: Zustand, B0POS: NOUN, B0Token: Zustand, B1Lemma: der, B1POS: DET, B1Token: der, S0B0Distance: 1, S0B0Lemma: schlecht_Zustand, S0B0LemmaPOS: schlecht_NOUN, S0B0POS: ADJ_NOUN, S0B0POSLemma: ADJ_Zustand, S0B0Token: schlechten_Zustand, S0B1Lemma: schlecht_der, S0B1LemmaPOS: schlecht_DET, S0B1POS: ADJ_DET, S0B1POSLemma: ADJ_der, S0B1Token: schlechten_der, S0B2Lemma: schlecht_Mauer, S0B2LemmaPOS: schlecht_NOUN, S0B2POS: ADJ_NOUN, S0B2POSLemma: ADJ_Mauer, S0B2Token: schlechten_Mauer, S0Lemma: schlecht, S0POS: ADJ, S0Token: schlechten, StackLength: 1, schlecht_isGouvernedBy_Zustand: true, schlecht_isGouvernedBy_Zustand_amod: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

58- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Zustand, der, Mauer ,.. ]

B0Lemma: Zustand, B0POS: NOUN, B0Token: Zustand, B1Lemma: der, B1POS: DET, B1Token: der, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

59- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Zustand]   B= [der, Mauer, und ,.. ]

B0Lemma: der, B0POS: DET, B0Token: der, B1Lemma: Mauer, B1POS: NOUN, B1Token: Mauer, S0B0Distance: 1, S0B0Lemma: Zustand_der, S0B0LemmaPOS: Zustand_DET, S0B0POS: NOUN_DET, S0B0POSLemma: NOUN_der, S0B0Token: Zustand_der, S0B1Lemma: Zustand_Mauer, S0B1LemmaPOS: Zustand_NOUN, S0B1POS: NOUN_NOUN, S0B1POSLemma: NOUN_Mauer, S0B1Token: Zustand_Mauer, S0B2Lemma: Zustand_und, S0B2LemmaPOS: Zustand_CONJ, S0B2POS: NOUN_CONJ, S0B2POSLemma: NOUN_und, S0B2Token: Zustand_und, S0Lemma: Zustand, S0POS: NOUN, S0Token: Zustand, StackLength: 1, Zustand_Mauer_hasRighDep_nmod: true, Zustand_hasRighDep_cc: true, Zustand_hasRighDep_nmod: true, Zustand_isGouvernedBy_geführen: true, Zustand_isGouvernedBy_geführen_nmod: true, Zustand_und_hasRighDep_cc: true, hasRighDep_cc: true, hasRighDep_nmod: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

60- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [der, Mauer, und ,.. ]

B0Lemma: der, B0POS: DET, B0Token: der, B1Lemma: Mauer, B1POS: NOUN, B1Token: Mauer, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

61- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [der]   B= [Mauer, und, damit ,.. ]

B0Lemma: Mauer, B0POS: NOUN, B0Token: Mauer, B1Lemma: und, B1POS: CONJ, B1Token: und, S0B0Distance: 1, S0B0Lemma: der_Mauer, S0B0LemmaPOS: der_NOUN, S0B0POS: DET_NOUN, S0B0POSLemma: DET_Mauer, S0B0Token: der_Mauer, S0B1Lemma: der_und, S0B1LemmaPOS: der_CONJ, S0B1POS: DET_CONJ, S0B1POSLemma: DET_und, S0B1Token: der_und, S0B2Lemma: der_damit, S0B2LemmaPOS: der_ADV, S0B2POS: DET_ADV, S0B2POSLemma: DET_damit, S0B2Token: der_damit, S0Lemma: der, S0POS: DET, S0Token: der, StackLength: 1, der_isGouvernedBy_Mauer: true, der_isGouvernedBy_Mauer_det: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

62- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Mauer, und, damit ,.. ]

B0Lemma: Mauer, B0POS: NOUN, B0Token: Mauer, B1Lemma: und, B1POS: CONJ, B1Token: und, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

63- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Mauer]   B= [und, damit, zum ,.. ]

B0Lemma: und, B0POS: CONJ, B0Token: und, B1Lemma: damit, B1POS: ADV, B1Token: damit, S0B0Distance: 1, S0B0Lemma: Mauer_und, S0B0LemmaPOS: Mauer_CONJ, S0B0POS: NOUN_CONJ, S0B0POSLemma: NOUN_und, S0B0Token: Mauer_und, S0B1Lemma: Mauer_damit, S0B1LemmaPOS: Mauer_ADV, S0B1POS: NOUN_ADV, S0B1POSLemma: NOUN_damit, S0B1Token: Mauer_damit, S0B2Lemma: Mauer_zu+der, S0B2LemmaPOS: Mauer_ADP, S0B2POS: NOUN_ADP, S0B2POSLemma: NOUN_zu+der, S0B2Token: Mauer_zum, S0Lemma: Mauer, S0POS: NOUN, S0Token: Mauer, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

64- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [und, damit, zum ,.. ]

B0Lemma: und, B0POS: CONJ, B0Token: und, B1Lemma: damit, B1POS: ADV, B1Token: damit, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

65- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [und]   B= [damit, zum, Einsturz ,.. ]

B0Lemma: damit, B0POS: ADV, B0Token: damit, B1Lemma: zu+der, B1POS: ADP, B1Token: zum, S0B0Distance: 1, S0B0Lemma: und_damit, S0B0LemmaPOS: und_ADV, S0B0POS: CONJ_ADV, S0B0POSLemma: CONJ_damit, S0B0Token: und_damit, S0B1Lemma: und_zu+der, S0B1LemmaPOS: und_ADP, S0B1POS: CONJ_ADP, S0B1POSLemma: CONJ_zu+der, S0B1Token: und_zum, S0B2Lemma: und_Einsturz, S0B2LemmaPOS: und_NOUN, S0B2POS: CONJ_NOUN, S0B2POSLemma: CONJ_Einsturz, S0B2Token: und_Einsturz, S0Lemma: und, S0POS: CONJ, S0Token: und, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

66- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [damit, zum, Einsturz ,.. ]

B0Lemma: damit, B0POS: ADV, B0Token: damit, B1Lemma: zu+der, B1POS: ADP, B1Token: zum, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

67- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [damit]   B= [zum, Einsturz, geführt ,.. ]

B0Lemma: zu+der, B0POS: ADP, B0Token: zum, B1Lemma: Einsturz, B1POS: NOUN, B1Token: Einsturz, S0B0Distance: 1, S0B0Lemma: damit_zu+der, S0B0LemmaPOS: damit_ADP, S0B0POS: ADV_ADP, S0B0POSLemma: ADV_zu+der, S0B0Token: damit_zum, S0B1Lemma: damit_Einsturz, S0B1LemmaPOS: damit_NOUN, S0B1POS: ADV_NOUN, S0B1POSLemma: ADV_Einsturz, S0B1Token: damit_Einsturz, S0B2Lemma: damit_geführen, S0B2LemmaPOS: damit_VERB, S0B2POS: ADV_VERB, S0B2POSLemma: ADV_geführen, S0B2Token: damit_geführt, S0Lemma: damit, S0POS: ADV, S0Token: damit, StackLength: 1, damit_isGouvernedBy_geführen: true, damit_isGouvernedBy_geführen_advmod: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

68- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [zum, Einsturz, geführt ,.. ]

B0Lemma: zu+der, B0POS: ADP, B0Token: zum, B1Lemma: Einsturz, B1POS: NOUN, B1Token: Einsturz, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

69- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [zum]   B= [Einsturz, geführt, hatten ,.. ]

B0Lemma: Einsturz, B0POS: NOUN, B0Token: Einsturz, B1Lemma: geführen, B1POS: VERB, B1Token: geführt, S0B0Distance: 1, S0B0Lemma: zu+der_Einsturz, S0B0LemmaPOS: zu+der_NOUN, S0B0POS: ADP_NOUN, S0B0POSLemma: ADP_Einsturz, S0B0Token: zum_Einsturz, S0B1Lemma: zu+der_geführen, S0B1LemmaPOS: zu+der_VERB, S0B1POS: ADP_VERB, S0B1POSLemma: ADP_geführen, S0B1Token: zum_geführt, S0B2Lemma: zu+der_haben, S0B2LemmaPOS: zu+der_AUX, S0B2POS: ADP_AUX, S0B2POSLemma: ADP_haben, S0B2Token: zum_hatten, S0Lemma: zu+der, S0POS: ADP, S0Token: zum, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, zu+der_isGouvernedBy_Einsturz: true, zu+der_isGouvernedBy_Einsturz_case: true, 

70- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Einsturz, geführt, hatten ,.. ]

B0Lemma: Einsturz, B0POS: NOUN, B0Token: Einsturz, B1Lemma: geführen, B1POS: VERB, B1Token: geführt, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

71- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Einsturz]   B= [geführt, hatten, . ,.. ]

B0Lemma: geführen, B0POS: VERB, B0Token: geführt, B1Lemma: haben, B1POS: AUX, B1Token: hatten, Einsturz_isGouvernedBy_geführen: true, Einsturz_isGouvernedBy_geführen_nmod: true, S0B0Distance: 1, S0B0Lemma: Einsturz_geführen, S0B0LemmaPOS: Einsturz_VERB, S0B0POS: NOUN_VERB, S0B0POSLemma: NOUN_geführen, S0B0Token: Einsturz_geführt, S0B1Lemma: Einsturz_haben, S0B1LemmaPOS: Einsturz_AUX, S0B1POS: NOUN_AUX, S0B1POSLemma: NOUN_haben, S0B1Token: Einsturz_hatten, S0B2Lemma: Einsturz_., S0B2LemmaPOS: Einsturz_PUNCT, S0B2POS: NOUN_PUNCT, S0B2POSLemma: NOUN_., S0B2Token: Einsturz_., S0Lemma: Einsturz, S0POS: NOUN, S0Token: Einsturz, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

72- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [geführt, hatten, . ,.. ]

B0Lemma: geführen, B0POS: VERB, B0Token: geführt, B1Lemma: haben, B1POS: AUX, B1Token: hatten, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

73- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [geführt]   B= [hatten, . ,.. ]

B0Lemma: haben, B0POS: AUX, B0Token: hatten, B1Lemma: ., B1POS: PUNCT, B1Token: ., S0B0Distance: 1, S0B0Lemma: geführen_haben, S0B0LemmaPOS: geführen_AUX, S0B0POS: VERB_AUX, S0B0POSLemma: VERB_haben, S0B0Token: geführt_hatten, S0B1Lemma: geführen_., S0B1LemmaPOS: geführen_PUNCT, S0B1POS: VERB_PUNCT, S0B1POSLemma: VERB_., S0B1Token: geführt_., S0Lemma: geführen, S0POS: VERB, S0Token: geführt, StackLength: 1, geführen_haben_hasRighDep_aux: true, geführen_hasRighDep_aux: true, hasRighDep_aux: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

74- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [hatten, . ,.. ]

B0Lemma: haben, B0POS: AUX, B0Token: hatten, B1Lemma: ., B1POS: PUNCT, B1Token: ., transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

75- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [hatten]   B= [.]

B0Lemma: ., B0POS: PUNCT, B0Token: ., S0B0Distance: 1, S0B0Lemma: haben_., S0B0LemmaPOS: haben_PUNCT, S0B0POS: AUX_PUNCT, S0B0POSLemma: AUX_., S0B0Token: hatten_., S0Lemma: haben, S0POS: AUX, S0Token: hatten, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

76- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [.]

B0Lemma: ., B0POS: PUNCT, B0Token: ., transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

77- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [ ]

S0Lemma: ., S0POS: PUNCT, S0Token: ., StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

78- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

## Sentence No. 438 - 
Rolf Simon , Hülshoff , Dammann gingen dagegen leer aus . 
### Existing MWEs: 
1- **gingen aus** (VPC)
2- **gingen leer aus** (ID), Interleaving 



0- &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Rolf, Simon, , ,.. ]

B0Lemma: Rolf, B0POS: PROPN, B0Token: Rolf, B1Lemma: Simon, B1POS: PROPN, B1Token: Simon, 

1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Rolf]   B= [Simon, ,, Hülshoff ,.. ]

B0Lemma: Simon, B0POS: PROPN, B0Token: Simon, B1Lemma: ,, B1POS: PUNCT, B1Token: ,, Rolf_isGouvernedBy_Simon: true, Rolf_isGouvernedBy_Simon_name: true, S0B0Distance: 1, S0B0Lemma: Rolf_Simon, S0B0LemmaPOS: Rolf_PROPN, S0B0POS: PROPN_PROPN, S0B0POSLemma: PROPN_Simon, S0B0Token: Rolf_Simon, S0B1Lemma: Rolf_,, S0B1LemmaPOS: Rolf_PUNCT, S0B1POS: PROPN_PUNCT, S0B1POSLemma: PROPN_,, S0B1Token: Rolf_,, S0B2Lemma: Rolf_Hülshoff, S0B2LemmaPOS: Rolf_PROPN, S0B2POS: PROPN_PROPN, S0B2POSLemma: PROPN_Hülshoff, S0B2Token: Rolf_Hülshoff, S0Lemma: Rolf, S0POS: PROPN, S0Token: Rolf, StackLength: 1, 

2- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Simon, ,, Hülshoff ,.. ]

B0Lemma: Simon, B0POS: PROPN, B0Token: Simon, B1Lemma: ,, B1POS: PUNCT, B1Token: ,, transitionHistoryLength1: 0, 

3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Simon]   B= [,, Hülshoff, , ,.. ]

B0Lemma: ,, B0POS: PUNCT, B0Token: ,, B1Lemma: Hülshoff, B1POS: PROPN, B1Token: Hülshoff, S0B0Distance: 1, S0B0Lemma: Simon_,, S0B0LemmaPOS: Simon_PUNCT, S0B0POS: PROPN_PUNCT, S0B0POSLemma: PROPN_,, S0B0Token: Simon_,, S0B1Lemma: Simon_Hülshoff, S0B1LemmaPOS: Simon_PROPN, S0B1POS: PROPN_PROPN, S0B1POSLemma: PROPN_Hülshoff, S0B1Token: Simon_Hülshoff, S0B2Lemma: Simon_,, S0B2LemmaPOS: Simon_PUNCT, S0B2POS: PROPN_PUNCT, S0B2POSLemma: PROPN_,, S0B2Token: Simon_,, S0Lemma: Simon, S0POS: PROPN, S0Token: Simon, Simon_,_hasRighDep_punct: true, Simon_Dammann_hasRighDep_appos: true, Simon_Hülshoff_hasRighDep_conj: true, Simon_hasRighDep_appos: true, Simon_hasRighDep_conj: true, Simon_hasRighDep_punct: true, Simon_isGouvernedBy_gehen: true, Simon_isGouvernedBy_gehen_nsubj: true, StackLength: 1, hasRighDep_appos: true, hasRighDep_conj: true, hasRighDep_punct: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, 

4- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, Hülshoff, , ,.. ]

B0Lemma: ,, B0POS: PUNCT, B0Token: ,, B1Lemma: Hülshoff, B1POS: PROPN, B1Token: Hülshoff, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [Hülshoff, ,, Dammann ,.. ]

B0Lemma: Hülshoff, B0POS: PROPN, B0Token: Hülshoff, B1Lemma: ,, B1POS: PUNCT, B1Token: ,, S0B0Distance: 1, S0B0Lemma: ,_Hülshoff, S0B0LemmaPOS: ,_PROPN, S0B0POS: PUNCT_PROPN, S0B0POSLemma: PUNCT_Hülshoff, S0B0Token: ,_Hülshoff, S0B1Lemma: ,_,, S0B1LemmaPOS: ,_PUNCT, S0B1POS: PUNCT_PUNCT, S0B1POSLemma: PUNCT_,, S0B1Token: ,_,, S0B2Lemma: ,_Dammann, S0B2LemmaPOS: ,_PROPN, S0B2POS: PUNCT_PROPN, S0B2POSLemma: PUNCT_Dammann, S0B2Token: ,_Dammann, S0Lemma: ,, S0POS: PUNCT, S0Token: ,, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

6- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Hülshoff, ,, Dammann ,.. ]

B0Lemma: Hülshoff, B0POS: PROPN, B0Token: Hülshoff, B1Lemma: ,, B1POS: PUNCT, B1Token: ,, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Hülshoff]   B= [,, Dammann, gingen ,.. ]

B0Lemma: ,, B0POS: PUNCT, B0Token: ,, B1Lemma: Dammann, B1POS: PROPN, B1Token: Dammann, S0B0Distance: 1, S0B0Lemma: Hülshoff_,, S0B0LemmaPOS: Hülshoff_PUNCT, S0B0POS: PROPN_PUNCT, S0B0POSLemma: PROPN_,, S0B0Token: Hülshoff_,, S0B1Lemma: Hülshoff_Dammann, S0B1LemmaPOS: Hülshoff_PROPN, S0B1POS: PROPN_PROPN, S0B1POSLemma: PROPN_Dammann, S0B1Token: Hülshoff_Dammann, S0B2Lemma: Hülshoff_gehen, S0B2LemmaPOS: Hülshoff_VERB, S0B2POS: PROPN_VERB, S0B2POSLemma: PROPN_gehen, S0B2Token: Hülshoff_gingen, S0Lemma: Hülshoff, S0POS: PROPN, S0Token: Hülshoff, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

8- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, Dammann, gingen ,.. ]

B0Lemma: ,, B0POS: PUNCT, B0Token: ,, B1Lemma: Dammann, B1POS: PROPN, B1Token: Dammann, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [Dammann, gingen, dagegen ,.. ]

B0Lemma: Dammann, B0POS: PROPN, B0Token: Dammann, B1Lemma: gehen, B1POS: VERB, B1Token: gingen, S0B0Distance: 1, S0B0Lemma: ,_Dammann, S0B0LemmaPOS: ,_PROPN, S0B0POS: PUNCT_PROPN, S0B0POSLemma: PUNCT_Dammann, S0B0Token: ,_Dammann, S0B1Lemma: ,_gehen, S0B1LemmaPOS: ,_VERB, S0B1POS: PUNCT_VERB, S0B1POSLemma: PUNCT_gehen, S0B1Token: ,_gingen, S0B2Lemma: ,_dagegen, S0B2LemmaPOS: ,_ADV, S0B2POS: PUNCT_ADV, S0B2POSLemma: PUNCT_dagegen, S0B2Token: ,_dagegen, S0Lemma: ,, S0POS: PUNCT, S0Token: ,, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

10- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Dammann, gingen, dagegen ,.. ]

B0Lemma: Dammann, B0POS: PROPN, B0Token: Dammann, B1Lemma: gehen, B1POS: VERB, B1Token: gingen, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Dammann]   B= [gingen, dagegen, leer ,.. ]

B0Lemma: gehen, B0POS: VERB, B0Token: gingen, B1Lemma: dagegen, B1POS: ADV, B1Token: dagegen, S0B0Distance: 1, S0B0Lemma: Dammann_gehen, S0B0LemmaPOS: Dammann_VERB, S0B0POS: PROPN_VERB, S0B0POSLemma: PROPN_gehen, S0B0Token: Dammann_gingen, S0B1Lemma: Dammann_dagegen, S0B1LemmaPOS: Dammann_ADV, S0B1POS: PROPN_ADV, S0B1POSLemma: PROPN_dagegen, S0B1Token: Dammann_dagegen, S0B2Lemma: Dammann_leer, S0B2LemmaPOS: Dammann_ADJ, S0B2POS: PROPN_ADJ, S0B2POSLemma: PROPN_leer, S0B2Token: Dammann_leer, S0Lemma: Dammann, S0POS: PROPN, S0Token: Dammann, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

12- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [gingen, dagegen, leer ,.. ]

B0Lemma: gehen, B0POS: VERB, B0Token: gingen, B1Lemma: dagegen, B1POS: ADV, B1Token: dagegen, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [gingen]   B= [dagegen, leer, aus ,.. ]

B0Lemma: dagegen, B0POS: ADV, B0Token: dagegen, B1Lemma: leer, B1POS: ADJ, B1Token: leer, S0B0Distance: 1, S0B0Lemma: gehen_dagegen, S0B0LemmaPOS: gehen_ADV, S0B0POS: VERB_ADV, S0B0POSLemma: VERB_dagegen, S0B0Token: gingen_dagegen, S0B1Lemma: gehen_leer, S0B1LemmaPOS: gehen_ADJ, S0B1POS: VERB_ADJ, S0B1POSLemma: VERB_leer, S0B1Token: gingen_leer, S0B2Lemma: gehen_aus, S0B2LemmaPOS: gehen_ADP, S0B2POS: VERB_ADP, S0B2POSLemma: VERB_aus, S0B2Token: gingen_aus, S0Lemma: gehen, S0POS: VERB, S0Token: gingen, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

14- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [gingen, dagegen]   B= [leer, aus, . ,.. ]

B0Lemma: leer, B0POS: ADJ, B0Token: leer, B1Lemma: aus, B1POS: ADP, B1Token: aus, S0B0Distance: 1, S0B0Lemma: dagegen_leer, S0B0LemmaPOS: dagegen_ADJ, S0B0POS: ADV_ADJ, S0B0POSLemma: ADV_leer, S0B0Token: dagegen_leer, S0B1Lemma: dagegen_aus, S0B1LemmaPOS: dagegen_ADP, S0B1POS: ADV_ADP, S0B1POSLemma: ADV_aus, S0B1Token: dagegen_aus, S0B2Lemma: dagegen_., S0B2LemmaPOS: dagegen_PUNCT, S0B2POS: ADV_PUNCT, S0B2POSLemma: ADV_., S0B2Token: dagegen_., S0Lemma: dagegen, S0POS: ADV, S0S1Distance: 1, S0Token: dagegen, S1B0Lemma: gehen_leer, S1B0LemmaPOS: gehen_ADJ, S1B0POS: VERB_ADJ, S1B0POSLemma: VERB_leer, S1B0Token: gingen_leer, S1Lemma: gehen, S1POS: VERB, S1S0B0Lemma: gehen_dagegen_leer, S1S0B0LemmaPOS: gehen_ADV_ADJ, S1S0B0POS: VERB_ADV_ADJ, S1S0B0POSLemma: VERB_ADV_leer, S1S0B0Token: gingen_dagegen_leer, S1S0Lemma: gehen_dagegen, S1S0LemmaPOS: gehen_ADV, S1S0POS: VERB_ADV, S1S0POSLemma: VERB_dagegen, S1S0Token: gingen_dagegen, S1Token: gingen, StackLength: 2, SyntaxicRelation: +advmod, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

15- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [gingen]   B= [leer, aus, . ,.. ]

B0Lemma: leer, B0POS: ADJ, B0Token: leer, B1Lemma: aus, B1POS: ADP, B1Token: aus, S0B0Distance: 2, S0B0Lemma: gehen_leer, S0B0LemmaPOS: gehen_ADJ, S0B0POS: VERB_ADJ, S0B0POSLemma: VERB_leer, S0B0Token: gingen_leer, S0B1Lemma: gehen_aus, S0B1LemmaPOS: gehen_ADP, S0B1POS: VERB_ADP, S0B1POSLemma: VERB_aus, S0B1Token: gingen_aus, S0B2Lemma: gehen_., S0B2LemmaPOS: gehen_PUNCT, S0B2POS: VERB_PUNCT, S0B2POSLemma: VERB_., S0B2Token: gingen_., S0Lemma: gehen, S0POS: VERB, S0Token: gingen, StackLength: 1, transitionHistoryLength1: 0, transitionHistoryLength2: 00, transitionHistoryLength3: 002, 

16- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [gingen, leer]   B= [aus, . ,.. ]

B0Lemma: aus, B0POS: ADP, B0Token: aus, B1Lemma: ., B1POS: PUNCT, B1Token: ., S0B0Distance: 1, S0B0Lemma: leer_aus, S0B0LemmaPOS: leer_ADP, S0B0POS: ADJ_ADP, S0B0POSLemma: ADJ_aus, S0B0Token: leer_aus, S0B1Lemma: leer_., S0B1LemmaPOS: leer_PUNCT, S0B1POS: ADJ_PUNCT, S0B1POSLemma: ADJ_., S0B1Token: leer_., S0Lemma: leer, S0POS: ADJ, S0S1Distance: 2, S0Token: leer, S1B0Lemma: gehen_aus, S1B0LemmaPOS: gehen_ADP, S1B0POS: VERB_ADP, S1B0POSLemma: VERB_aus, S1B0Token: gingen_aus, S1Lemma: gehen, S1POS: VERB, S1S0B0Lemma: gehen_leer_aus, S1S0B0LemmaPOS: gehen_ADJ_ADP, S1S0B0POS: VERB_ADJ_ADP, S1S0B0POSLemma: VERB_ADJ_aus, S1S0B0Token: gingen_leer_aus, S1S0Lemma: gehen_leer, S1S0LemmaPOS: gehen_ADJ, S1S0POS: VERB_ADJ, S1S0POSLemma: VERB_leer, S1S0Token: gingen_leer, S1Token: gingen, StackLength: 2, SyntaxicRelation: +advmod, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 200, 

17- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [gingen]   B= [aus, . ,.. ]

B0Lemma: aus, B0POS: ADP, B0Token: aus, B1Lemma: ., B1POS: PUNCT, B1Token: ., S0B0Distance: 3, S0B0Lemma: gehen_aus, S0B0LemmaPOS: gehen_ADP, S0B0POS: VERB_ADP, S0B0POSLemma: VERB_aus, S0B0Token: gingen_aus, S0B1Lemma: gehen_., S0B1LemmaPOS: gehen_PUNCT, S0B1POS: VERB_PUNCT, S0B1POSLemma: VERB_., S0B1Token: gingen_., S0Lemma: gehen, S0POS: VERB, S0Token: gingen, StackLength: 1, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

18- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [gingen, aus]   B= [.]

B0Lemma: ., B0POS: PUNCT, B0Token: ., S0B0Distance: 1, S0B0Lemma: aus_., S0B0LemmaPOS: aus_PUNCT, S0B0POS: ADP_PUNCT, S0B0POSLemma: ADP_., S0B0Token: aus_., S0Lemma: aus, S0POS: ADP, S0S1Distance: 3, S0Token: aus, S1B0Lemma: gehen_., S1B0LemmaPOS: gehen_PUNCT, S1B0POS: VERB_PUNCT, S1B0POSLemma: VERB_., S1B0Token: gingen_., S1Lemma: gehen, S1POS: VERB, S1S0B0Lemma: gehen_aus_., S1S0B0LemmaPOS: gehen_ADP_PUNCT, S1S0B0POS: VERB_ADP_PUNCT, S1S0B0POSLemma: VERB_ADP_., S1S0B0Token: gingen_aus_., S1S0Lemma: gehen_aus, S1S0LemmaPOS: gehen_ADP, S1S0POS: VERB_ADP, S1S0POSLemma: VERB_aus, S1S0Token: gingen_aus, S1Token: gingen, StackLength: 2, SyntaxicRelation: +compound:prt, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

19- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[gingen, aus]]   B= [.]

B0Lemma: ., B0POS: PUNCT, B0Token: ., S0B0Distance: 1, S0B0Lemma: gehen_aus_., S0B0LemmaPOS: gehen_aus_PUNCT, S0B0POS: VERB_ADP_PUNCT, S0B0POSLemma: VERB_ADP_., S0B0Token: gingen_aus_., S0Lemma: gehen_aus, S0POS: VERB_ADP, S0Token: gingen_aus, StackLength: 1, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

20- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [.]

B0Lemma: ., B0POS: PUNCT, B0Token: ., transitionHistoryLength1: 1, transitionHistoryLength2: 10, transitionHistoryLength3: 102, 

21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [ ]

S0Lemma: ., S0POS: PUNCT, S0Token: ., StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 21, transitionHistoryLength3: 210, 

22- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

## Sentence No. 469 - 
Einig sind sie sich im großen Dialog über den GV , vulgo Geschlechtsverkehr : Die Liebe habe mit ihm so viel zu tun wie der Mond mit den Gedichten , die auf ihn abgesondert werden . 
### Existing MWEs: 
1- **habe zu tun** (ID)
2- **abgesondert** (VPC)



0- &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Einig, sind, sie ,.. ]

B0Lemma: einig, B0POS: ADJ, B0Token: Einig, B1Lemma: sein, B1POS: VERB, B1Token: sind, 

1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Einig]   B= [sind, sie, sich ,.. ]

B0Lemma: sein, B0POS: VERB, B0Token: sind, B1Lemma: sie, B1POS: PRON, B1Token: sie, S0B0Distance: 1, S0B0Lemma: einig_sein, S0B0LemmaPOS: einig_VERB, S0B0POS: ADJ_VERB, S0B0POSLemma: ADJ_sein, S0B0Token: Einig_sind, S0B1Lemma: einig_sie, S0B1LemmaPOS: einig_PRON, S0B1POS: ADJ_PRON, S0B1POSLemma: ADJ_sie, S0B1Token: Einig_sie, S0B2Lemma: einig_er|es|sie, S0B2LemmaPOS: einig_PRON, S0B2POS: ADJ_PRON, S0B2POSLemma: ADJ_er|es|sie, S0B2Token: Einig_sich, S0Lemma: einig, S0POS: ADJ, S0Token: Einig, StackLength: 1, 

2- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [sind, sie, sich ,.. ]

B0Lemma: sein, B0POS: VERB, B0Token: sind, B1Lemma: sie, B1POS: PRON, B1Token: sie, transitionHistoryLength1: 0, 

3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [sind]   B= [sie, sich, im ,.. ]

B0Lemma: sie, B0POS: PRON, B0Token: sie, B1Lemma: er|es|sie, B1POS: PRON, B1Token: sich, S0B0Distance: 1, S0B0Lemma: sein_sie, S0B0LemmaPOS: sein_PRON, S0B0POS: VERB_PRON, S0B0POSLemma: VERB_sie, S0B0Token: sind_sie, S0B1Lemma: sein_er|es|sie, S0B1LemmaPOS: sein_PRON, S0B1POS: VERB_PRON, S0B1POSLemma: VERB_er|es|sie, S0B1Token: sind_sich, S0B2Lemma: sein_in+der, S0B2LemmaPOS: sein_ADP, S0B2POS: VERB_ADP, S0B2POSLemma: VERB_in+der, S0B2Token: sind_im, S0Lemma: sein, S0POS: VERB, S0Token: sind, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, 

4- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [sie, sich, im ,.. ]

B0Lemma: sie, B0POS: PRON, B0Token: sie, B1Lemma: er|es|sie, B1POS: PRON, B1Token: sich, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [sie]   B= [sich, im, großen ,.. ]

B0Lemma: er|es|sie, B0POS: PRON, B0Token: sich, B1Lemma: in+der, B1POS: ADP, B1Token: im, S0B0Distance: 1, S0B0Lemma: sie_er|es|sie, S0B0LemmaPOS: sie_PRON, S0B0POS: PRON_PRON, S0B0POSLemma: PRON_er|es|sie, S0B0Token: sie_sich, S0B1Lemma: sie_in+der, S0B1LemmaPOS: sie_ADP, S0B1POS: PRON_ADP, S0B1POSLemma: PRON_in+der, S0B1Token: sie_im, S0B2Lemma: sie_groß, S0B2LemmaPOS: sie_ADJ, S0B2POS: PRON_ADJ, S0B2POSLemma: PRON_groß, S0B2Token: sie_großen, S0Lemma: sie, S0POS: PRON, S0Token: sie, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

6- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [sich, im, großen ,.. ]

B0Lemma: er|es|sie, B0POS: PRON, B0Token: sich, B1Lemma: in+der, B1POS: ADP, B1Token: im, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [sich]   B= [im, großen, Dialog ,.. ]

B0Lemma: in+der, B0POS: ADP, B0Token: im, B1Lemma: groß, B1POS: ADJ, B1Token: großen, S0B0Distance: 1, S0B0Lemma: er|es|sie_in+der, S0B0LemmaPOS: er|es|sie_ADP, S0B0POS: PRON_ADP, S0B0POSLemma: PRON_in+der, S0B0Token: sich_im, S0B1Lemma: er|es|sie_groß, S0B1LemmaPOS: er|es|sie_ADJ, S0B1POS: PRON_ADJ, S0B1POSLemma: PRON_groß, S0B1Token: sich_großen, S0B2Lemma: er|es|sie_Dialog, S0B2LemmaPOS: er|es|sie_NOUN, S0B2POS: PRON_NOUN, S0B2POSLemma: PRON_Dialog, S0B2Token: sich_Dialog, S0Lemma: er|es|sie, S0POS: PRON, S0Token: sich, StackLength: 1, er|es|sie_Dialog_hasRighDep_nmod: true, er|es|sie_hasRighDep_nmod: true, er|es|sie_isGouvernedBy_tun: true, er|es|sie_isGouvernedBy_tun_dobj: true, hasRighDep_nmod: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

8- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [im, großen, Dialog ,.. ]

B0Lemma: in+der, B0POS: ADP, B0Token: im, B1Lemma: groß, B1POS: ADJ, B1Token: großen, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [im]   B= [großen, Dialog, über ,.. ]

B0Lemma: groß, B0POS: ADJ, B0Token: großen, B1Lemma: Dialog, B1POS: NOUN, B1Token: Dialog, S0B0Distance: 1, S0B0Lemma: in+der_groß, S0B0LemmaPOS: in+der_ADJ, S0B0POS: ADP_ADJ, S0B0POSLemma: ADP_groß, S0B0Token: im_großen, S0B1Lemma: in+der_Dialog, S0B1LemmaPOS: in+der_NOUN, S0B1POS: ADP_NOUN, S0B1POSLemma: ADP_Dialog, S0B1Token: im_Dialog, S0B2Lemma: in+der_über, S0B2LemmaPOS: in+der_ADP, S0B2POS: ADP_ADP, S0B2POSLemma: ADP_über, S0B2Token: im_über, S0Lemma: in+der, S0POS: ADP, S0Token: im, StackLength: 1, in+der_isGouvernedBy_Dialog: true, in+der_isGouvernedBy_Dialog_case: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

10- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [großen, Dialog, über ,.. ]

B0Lemma: groß, B0POS: ADJ, B0Token: großen, B1Lemma: Dialog, B1POS: NOUN, B1Token: Dialog, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [großen]   B= [Dialog, über, den ,.. ]

B0Lemma: Dialog, B0POS: NOUN, B0Token: Dialog, B1Lemma: über, B1POS: ADP, B1Token: über, S0B0Distance: 1, S0B0Lemma: groß_Dialog, S0B0LemmaPOS: groß_NOUN, S0B0POS: ADJ_NOUN, S0B0POSLemma: ADJ_Dialog, S0B0Token: großen_Dialog, S0B1Lemma: groß_über, S0B1LemmaPOS: groß_ADP, S0B1POS: ADJ_ADP, S0B1POSLemma: ADJ_über, S0B1Token: großen_über, S0B2Lemma: groß_der, S0B2LemmaPOS: groß_DET, S0B2POS: ADJ_DET, S0B2POSLemma: ADJ_der, S0B2Token: großen_den, S0Lemma: groß, S0POS: ADJ, S0Token: großen, StackLength: 1, groß_isGouvernedBy_Dialog: true, groß_isGouvernedBy_Dialog_amod: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

12- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Dialog, über, den ,.. ]

B0Lemma: Dialog, B0POS: NOUN, B0Token: Dialog, B1Lemma: über, B1POS: ADP, B1Token: über, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Dialog]   B= [über, den, GV ,.. ]

B0Lemma: über, B0POS: ADP, B0Token: über, B1Lemma: der, B1POS: DET, B1Token: den, Dialog_GV_hasRighDep_nmod: true, Dialog_Lieb_hasRighDep_conj: true, Dialog_hasRighDep_conj: true, Dialog_hasRighDep_nmod: true, S0B0Distance: 1, S0B0Lemma: Dialog_über, S0B0LemmaPOS: Dialog_ADP, S0B0POS: NOUN_ADP, S0B0POSLemma: NOUN_über, S0B0Token: Dialog_über, S0B1Lemma: Dialog_der, S0B1LemmaPOS: Dialog_DET, S0B1POS: NOUN_DET, S0B1POSLemma: NOUN_der, S0B1Token: Dialog_den, S0B2Lemma: Dialog_GV, S0B2LemmaPOS: Dialog_PROPN, S0B2POS: NOUN_PROPN, S0B2POSLemma: NOUN_GV, S0B2Token: Dialog_GV, S0Lemma: Dialog, S0POS: NOUN, S0Token: Dialog, StackLength: 1, hasRighDep_conj: true, hasRighDep_nmod: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

14- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [über, den, GV ,.. ]

B0Lemma: über, B0POS: ADP, B0Token: über, B1Lemma: der, B1POS: DET, B1Token: den, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [über]   B= [den, GV, , ,.. ]

B0Lemma: der, B0POS: DET, B0Token: den, B1Lemma: GV, B1POS: PROPN, B1Token: GV, S0B0Distance: 1, S0B0Lemma: über_der, S0B0LemmaPOS: über_DET, S0B0POS: ADP_DET, S0B0POSLemma: ADP_der, S0B0Token: über_den, S0B1Lemma: über_GV, S0B1LemmaPOS: über_PROPN, S0B1POS: ADP_PROPN, S0B1POSLemma: ADP_GV, S0B1Token: über_GV, S0B2Lemma: über_,, S0B2LemmaPOS: über_PUNCT, S0B2POS: ADP_PUNCT, S0B2POSLemma: ADP_,, S0B2Token: über_,, S0Lemma: über, S0POS: ADP, S0Token: über, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, über_isGouvernedBy_GV: true, über_isGouvernedBy_GV_case: true, 

16- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [den, GV, , ,.. ]

B0Lemma: der, B0POS: DET, B0Token: den, B1Lemma: GV, B1POS: PROPN, B1Token: GV, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [den]   B= [GV, ,, vulgo ,.. ]

B0Lemma: GV, B0POS: PROPN, B0Token: GV, B1Lemma: ,, B1POS: PUNCT, B1Token: ,, S0B0Distance: 1, S0B0Lemma: der_GV, S0B0LemmaPOS: der_PROPN, S0B0POS: DET_PROPN, S0B0POSLemma: DET_GV, S0B0Token: den_GV, S0B1Lemma: der_,, S0B1LemmaPOS: der_PUNCT, S0B1POS: DET_PUNCT, S0B1POSLemma: DET_,, S0B1Token: den_,, S0B2Lemma: der_vulgo, S0B2LemmaPOS: der_PROPN, S0B2POS: DET_PROPN, S0B2POSLemma: DET_vulgo, S0B2Token: den_vulgo, S0Lemma: der, S0POS: DET, S0Token: den, StackLength: 1, der_isGouvernedBy_GV: true, der_isGouvernedBy_GV_det: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

18- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [GV, ,, vulgo ,.. ]

B0Lemma: GV, B0POS: PROPN, B0Token: GV, B1Lemma: ,, B1POS: PUNCT, B1Token: ,, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [GV]   B= [,, vulgo, Geschlechtsverkehr ,.. ]

B0Lemma: ,, B0POS: PUNCT, B0Token: ,, B1Lemma: vulgo, B1POS: PROPN, B1Token: vulgo, GV_,_hasRighDep_punct: true, GV_:_hasRighDep_punct: true, GV_Geschlechtsverkehr_hasRighDep_appos: true, GV_hasRighDep_appos: true, GV_hasRighDep_name: true, GV_hasRighDep_punct: true, GV_vulgo_hasRighDep_name: true, S0B0Distance: 1, S0B0Lemma: GV_,, S0B0LemmaPOS: GV_PUNCT, S0B0POS: PROPN_PUNCT, S0B0POSLemma: PROPN_,, S0B0Token: GV_,, S0B1Lemma: GV_vulgo, S0B1LemmaPOS: GV_PROPN, S0B1POS: PROPN_PROPN, S0B1POSLemma: PROPN_vulgo, S0B1Token: GV_vulgo, S0B2Lemma: GV_Geschlechtsverkehr, S0B2LemmaPOS: GV_PROPN, S0B2POS: PROPN_PROPN, S0B2POSLemma: PROPN_Geschlechtsverkehr, S0B2Token: GV_Geschlechtsverkehr, S0Lemma: GV, S0POS: PROPN, S0Token: GV, StackLength: 1, hasRighDep_appos: true, hasRighDep_name: true, hasRighDep_punct: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

20- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, vulgo, Geschlechtsverkehr ,.. ]

B0Lemma: ,, B0POS: PUNCT, B0Token: ,, B1Lemma: vulgo, B1POS: PROPN, B1Token: vulgo, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [vulgo, Geschlechtsverkehr, : ,.. ]

B0Lemma: vulgo, B0POS: PROPN, B0Token: vulgo, B1Lemma: Geschlechtsverkehr, B1POS: PROPN, B1Token: Geschlechtsverkehr, S0B0Distance: 1, S0B0Lemma: ,_vulgo, S0B0LemmaPOS: ,_PROPN, S0B0POS: PUNCT_PROPN, S0B0POSLemma: PUNCT_vulgo, S0B0Token: ,_vulgo, S0B1Lemma: ,_Geschlechtsverkehr, S0B1LemmaPOS: ,_PROPN, S0B1POS: PUNCT_PROPN, S0B1POSLemma: PUNCT_Geschlechtsverkehr, S0B1Token: ,_Geschlechtsverkehr, S0B2Lemma: ,_:, S0B2LemmaPOS: ,_PUNCT, S0B2POS: PUNCT_PUNCT, S0B2POSLemma: PUNCT_:, S0B2Token: ,_:, S0Lemma: ,, S0POS: PUNCT, S0Token: ,, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

22- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [vulgo, Geschlechtsverkehr, : ,.. ]

B0Lemma: vulgo, B0POS: PROPN, B0Token: vulgo, B1Lemma: Geschlechtsverkehr, B1POS: PROPN, B1Token: Geschlechtsverkehr, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

23- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [vulgo]   B= [Geschlechtsverkehr, :, Die ,.. ]

B0Lemma: Geschlechtsverkehr, B0POS: PROPN, B0Token: Geschlechtsverkehr, B1Lemma: :, B1POS: PUNCT, B1Token: :, S0B0Distance: 1, S0B0Lemma: vulgo_Geschlechtsverkehr, S0B0LemmaPOS: vulgo_PROPN, S0B0POS: PROPN_PROPN, S0B0POSLemma: PROPN_Geschlechtsverkehr, S0B0Token: vulgo_Geschlechtsverkehr, S0B1Lemma: vulgo_:, S0B1LemmaPOS: vulgo_PUNCT, S0B1POS: PROPN_PUNCT, S0B1POSLemma: PROPN_:, S0B1Token: vulgo_:, S0B2Lemma: vulgo_der, S0B2LemmaPOS: vulgo_DET, S0B2POS: PROPN_DET, S0B2POSLemma: PROPN_der, S0B2Token: vulgo_Die, S0Lemma: vulgo, S0POS: PROPN, S0Token: vulgo, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

24- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Geschlechtsverkehr, :, Die ,.. ]

B0Lemma: Geschlechtsverkehr, B0POS: PROPN, B0Token: Geschlechtsverkehr, B1Lemma: :, B1POS: PUNCT, B1Token: :, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

25- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Geschlechtsverkehr]   B= [:, Die, Liebe ,.. ]

B0Lemma: :, B0POS: PUNCT, B0Token: :, B1Lemma: der, B1POS: DET, B1Token: Die, S0B0Distance: 1, S0B0Lemma: Geschlechtsverkehr_:, S0B0LemmaPOS: Geschlechtsverkehr_PUNCT, S0B0POS: PROPN_PUNCT, S0B0POSLemma: PROPN_:, S0B0Token: Geschlechtsverkehr_:, S0B1Lemma: Geschlechtsverkehr_der, S0B1LemmaPOS: Geschlechtsverkehr_DET, S0B1POS: PROPN_DET, S0B1POSLemma: PROPN_der, S0B1Token: Geschlechtsverkehr_Die, S0B2Lemma: Geschlechtsverkehr_Lieb, S0B2LemmaPOS: Geschlechtsverkehr_NOUN, S0B2POS: PROPN_NOUN, S0B2POSLemma: PROPN_Lieb, S0B2Token: Geschlechtsverkehr_Liebe, S0Lemma: Geschlechtsverkehr, S0POS: PROPN, S0Token: Geschlechtsverkehr, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

26- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [:, Die, Liebe ,.. ]

B0Lemma: :, B0POS: PUNCT, B0Token: :, B1Lemma: der, B1POS: DET, B1Token: Die, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

27- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [:]   B= [Die, Liebe, habe ,.. ]

B0Lemma: der, B0POS: DET, B0Token: Die, B1Lemma: Lieb, B1POS: NOUN, B1Token: Liebe, S0B0Distance: 1, S0B0Lemma: :_der, S0B0LemmaPOS: :_DET, S0B0POS: PUNCT_DET, S0B0POSLemma: PUNCT_der, S0B0Token: :_Die, S0B1Lemma: :_Lieb, S0B1LemmaPOS: :_NOUN, S0B1POS: PUNCT_NOUN, S0B1POSLemma: PUNCT_Lieb, S0B1Token: :_Liebe, S0B2Lemma: :_haben, S0B2LemmaPOS: :_AUX, S0B2POS: PUNCT_AUX, S0B2POSLemma: PUNCT_haben, S0B2Token: :_habe, S0Lemma: :, S0POS: PUNCT, S0Token: :, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

28- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Die, Liebe, habe ,.. ]

B0Lemma: der, B0POS: DET, B0Token: Die, B1Lemma: Lieb, B1POS: NOUN, B1Token: Liebe, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

29- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Die]   B= [Liebe, habe, mit ,.. ]

B0Lemma: Lieb, B0POS: NOUN, B0Token: Liebe, B1Lemma: haben, B1POS: AUX, B1Token: habe, S0B0Distance: 1, S0B0Lemma: der_Lieb, S0B0LemmaPOS: der_NOUN, S0B0POS: DET_NOUN, S0B0POSLemma: DET_Lieb, S0B0Token: Die_Liebe, S0B1Lemma: der_haben, S0B1LemmaPOS: der_AUX, S0B1POS: DET_AUX, S0B1POSLemma: DET_haben, S0B1Token: Die_habe, S0B2Lemma: der_mit, S0B2LemmaPOS: der_ADP, S0B2POS: DET_ADP, S0B2POSLemma: DET_mit, S0B2Token: Die_mit, S0Lemma: der, S0POS: DET, S0Token: Die, StackLength: 1, der_isGouvernedBy_Lieb: true, der_isGouvernedBy_Lieb_det: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

30- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Liebe, habe, mit ,.. ]

B0Lemma: Lieb, B0POS: NOUN, B0Token: Liebe, B1Lemma: haben, B1POS: AUX, B1Token: habe, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

31- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Liebe]   B= [habe, mit, ihm ,.. ]

B0Lemma: haben, B0POS: AUX, B0Token: habe, B1Lemma: mit, B1POS: ADP, B1Token: mit, S0B0Distance: 1, S0B0Lemma: Lieb_haben, S0B0LemmaPOS: Lieb_AUX, S0B0POS: NOUN_AUX, S0B0POSLemma: NOUN_haben, S0B0Token: Liebe_habe, S0B1Lemma: Lieb_mit, S0B1LemmaPOS: Lieb_ADP, S0B1POS: NOUN_ADP, S0B1POSLemma: NOUN_mit, S0B1Token: Liebe_mit, S0B2Lemma: Lieb_er, S0B2LemmaPOS: Lieb_PRON, S0B2POS: NOUN_PRON, S0B2POSLemma: NOUN_er, S0B2Token: Liebe_ihm, S0Lemma: Lieb, S0POS: NOUN, S0Token: Liebe, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

32- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [habe, mit, ihm ,.. ]

B0Lemma: haben, B0POS: AUX, B0Token: habe, B1Lemma: mit, B1POS: ADP, B1Token: mit, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

33- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [habe]   B= [mit, ihm, so ,.. ]

B0Lemma: mit, B0POS: ADP, B0Token: mit, B1Lemma: er, B1POS: PRON, B1Token: ihm, S0B0Distance: 1, S0B0Lemma: haben_mit, S0B0LemmaPOS: haben_ADP, S0B0POS: AUX_ADP, S0B0POSLemma: AUX_mit, S0B0Token: habe_mit, S0B1Lemma: haben_er, S0B1LemmaPOS: haben_PRON, S0B1POS: AUX_PRON, S0B1POSLemma: AUX_er, S0B1Token: habe_ihm, S0B2Lemma: haben_so, S0B2LemmaPOS: haben_ADV, S0B2POS: AUX_ADV, S0B2POSLemma: AUX_so, S0B2Token: habe_so, S0Lemma: haben, S0POS: AUX, S0Token: habe, StackLength: 1, haben_isGouvernedBy_tun: true, haben_isGouvernedBy_tun_aux: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

34- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [habe, mit]   B= [ihm, so, viel ,.. ]

B0Lemma: er, B0POS: PRON, B0Token: ihm, B1Lemma: so, B1POS: ADV, B1Token: so, S0B0Distance: 1, S0B0Lemma: mit_er, S0B0LemmaPOS: mit_PRON, S0B0POS: ADP_PRON, S0B0POSLemma: ADP_er, S0B0Token: mit_ihm, S0B1Lemma: mit_so, S0B1LemmaPOS: mit_ADV, S0B1POS: ADP_ADV, S0B1POSLemma: ADP_so, S0B1Token: mit_so, S0B2Lemma: mit_viel, S0B2LemmaPOS: mit_ADV, S0B2POS: ADP_ADV, S0B2POSLemma: ADP_viel, S0B2Token: mit_viel, S0Lemma: mit, S0POS: ADP, S0S1Distance: 1, S0Token: mit, S1B0Lemma: haben_er, S1B0LemmaPOS: haben_PRON, S1B0POS: AUX_PRON, S1B0POSLemma: AUX_er, S1B0Token: habe_ihm, S1Lemma: haben, S1POS: AUX, S1S0B0Lemma: haben_mit_er, S1S0B0LemmaPOS: haben_ADP_PRON, S1S0B0POS: AUX_ADP_PRON, S1S0B0POSLemma: AUX_ADP_er, S1S0B0Token: habe_mit_ihm, S1S0Lemma: haben_mit, S1S0LemmaPOS: haben_ADP, S1S0POS: AUX_ADP, S1S0POSLemma: AUX_mit, S1S0Token: habe_mit, S1Token: habe, StackLength: 2, mit_isGouvernedBy_er: true, mit_isGouvernedBy_er_case: true, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

35- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [habe]   B= [ihm, so, viel ,.. ]

B0Lemma: er, B0POS: PRON, B0Token: ihm, B1Lemma: so, B1POS: ADV, B1Token: so, S0B0Distance: 2, S0B0Lemma: haben_er, S0B0LemmaPOS: haben_PRON, S0B0POS: AUX_PRON, S0B0POSLemma: AUX_er, S0B0Token: habe_ihm, S0B1Lemma: haben_so, S0B1LemmaPOS: haben_ADV, S0B1POS: AUX_ADV, S0B1POSLemma: AUX_so, S0B1Token: habe_so, S0B2Lemma: haben_viel, S0B2LemmaPOS: haben_ADV, S0B2POS: AUX_ADV, S0B2POSLemma: AUX_viel, S0B2Token: habe_viel, S0Lemma: haben, S0POS: AUX, S0Token: habe, StackLength: 1, haben_isGouvernedBy_tun: true, haben_isGouvernedBy_tun_aux: true, transitionHistoryLength1: 0, transitionHistoryLength2: 00, transitionHistoryLength3: 002, 

36- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [habe, ihm]   B= [so, viel, zu ,.. ]

B0Lemma: so, B0POS: ADV, B0Token: so, B1Lemma: viel, B1POS: ADV, B1Token: viel, S0B0Distance: 1, S0B0Lemma: er_so, S0B0LemmaPOS: er_ADV, S0B0POS: PRON_ADV, S0B0POSLemma: PRON_so, S0B0Token: ihm_so, S0B1Lemma: er_viel, S0B1LemmaPOS: er_ADV, S0B1POS: PRON_ADV, S0B1POSLemma: PRON_viel, S0B1Token: ihm_viel, S0B2Lemma: er_zu, S0B2LemmaPOS: er_ADV, S0B2POS: PRON_ADV, S0B2POSLemma: PRON_zu, S0B2Token: ihm_zu, S0Lemma: er, S0POS: PRON, S0S1Distance: 2, S0Token: ihm, S1B0Lemma: haben_so, S1B0LemmaPOS: haben_ADV, S1B0POS: AUX_ADV, S1B0POSLemma: AUX_so, S1B0Token: habe_so, S1Lemma: haben, S1POS: AUX, S1S0B0Lemma: haben_er_so, S1S0B0LemmaPOS: haben_PRON_ADV, S1S0B0POS: AUX_PRON_ADV, S1S0B0POSLemma: AUX_PRON_so, S1S0B0Token: habe_ihm_so, S1S0Lemma: haben_er, S1S0LemmaPOS: haben_PRON, S1S0POS: AUX_PRON, S1S0POSLemma: AUX_er, S1S0Token: habe_ihm, S1Token: habe, StackLength: 2, er_isGouvernedBy_tun: true, er_isGouvernedBy_tun_nmod: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 200, 

37- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [habe]   B= [so, viel, zu ,.. ]

B0Lemma: so, B0POS: ADV, B0Token: so, B1Lemma: viel, B1POS: ADV, B1Token: viel, S0B0Distance: 3, S0B0Lemma: haben_so, S0B0LemmaPOS: haben_ADV, S0B0POS: AUX_ADV, S0B0POSLemma: AUX_so, S0B0Token: habe_so, S0B1Lemma: haben_viel, S0B1LemmaPOS: haben_ADV, S0B1POS: AUX_ADV, S0B1POSLemma: AUX_viel, S0B1Token: habe_viel, S0B2Lemma: haben_zu, S0B2LemmaPOS: haben_ADV, S0B2POS: AUX_ADV, S0B2POSLemma: AUX_zu, S0B2Token: habe_zu, S0Lemma: haben, S0POS: AUX, S0Token: habe, StackLength: 1, haben_isGouvernedBy_tun: true, haben_isGouvernedBy_tun_aux: true, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

38- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [habe, so]   B= [viel, zu, tun ,.. ]

B0Lemma: viel, B0POS: ADV, B0Token: viel, B1Lemma: zu, B1POS: ADV, B1Token: zu, S0B0Distance: 1, S0B0Lemma: so_viel, S0B0LemmaPOS: so_ADV, S0B0POS: ADV_ADV, S0B0POSLemma: ADV_viel, S0B0Token: so_viel, S0B1Lemma: so_zu, S0B1LemmaPOS: so_ADV, S0B1POS: ADV_ADV, S0B1POSLemma: ADV_zu, S0B1Token: so_zu, S0B2Lemma: so_tun, S0B2LemmaPOS: so_ADJ, S0B2POS: ADV_ADJ, S0B2POSLemma: ADV_tun, S0B2Token: so_tun, S0Lemma: so, S0POS: ADV, S0S1Distance: 3, S0Token: so, S1B0Lemma: haben_viel, S1B0LemmaPOS: haben_ADV, S1B0POS: AUX_ADV, S1B0POSLemma: AUX_viel, S1B0Token: habe_viel, S1Lemma: haben, S1POS: AUX, S1S0B0Lemma: haben_so_viel, S1S0B0LemmaPOS: haben_ADV_ADV, S1S0B0POS: AUX_ADV_ADV, S1S0B0POSLemma: AUX_ADV_viel, S1S0B0Token: habe_so_viel, S1S0Lemma: haben_so, S1S0LemmaPOS: haben_ADV, S1S0POS: AUX_ADV, S1S0POSLemma: AUX_so, S1S0Token: habe_so, S1Token: habe, StackLength: 2, so_isGouvernedBy_tun: true, so_isGouvernedBy_tun_advmod: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

39- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [habe]   B= [viel, zu, tun ,.. ]

B0Lemma: viel, B0POS: ADV, B0Token: viel, B1Lemma: zu, B1POS: ADV, B1Token: zu, S0B0Distance: 4, S0B0Lemma: haben_viel, S0B0LemmaPOS: haben_ADV, S0B0POS: AUX_ADV, S0B0POSLemma: AUX_viel, S0B0Token: habe_viel, S0B1Lemma: haben_zu, S0B1LemmaPOS: haben_ADV, S0B1POS: AUX_ADV, S0B1POSLemma: AUX_zu, S0B1Token: habe_zu, S0B2Lemma: haben_tun, S0B2LemmaPOS: haben_ADJ, S0B2POS: AUX_ADJ, S0B2POSLemma: AUX_tun, S0B2Token: habe_tun, S0Lemma: haben, S0POS: AUX, S0Token: habe, StackLength: 1, haben_isGouvernedBy_tun: true, haben_isGouvernedBy_tun_aux: true, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

40- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [habe, viel]   B= [zu, tun, wie ,.. ]

B0Lemma: zu, B0POS: ADV, B0Token: zu, B1Lemma: tun, B1POS: ADJ, B1Token: tun, S0B0Distance: 1, S0B0Lemma: viel_zu, S0B0LemmaPOS: viel_ADV, S0B0POS: ADV_ADV, S0B0POSLemma: ADV_zu, S0B0Token: viel_zu, S0B1Lemma: viel_tun, S0B1LemmaPOS: viel_ADJ, S0B1POS: ADV_ADJ, S0B1POSLemma: ADV_tun, S0B1Token: viel_tun, S0B2Lemma: viel_wie, S0B2LemmaPOS: viel_ADP, S0B2POS: ADV_ADP, S0B2POSLemma: ADV_wie, S0B2Token: viel_wie, S0Lemma: viel, S0POS: ADV, S0S1Distance: 4, S0Token: viel, S1B0Lemma: haben_zu, S1B0LemmaPOS: haben_ADV, S1B0POS: AUX_ADV, S1B0POSLemma: AUX_zu, S1B0Token: habe_zu, S1Lemma: haben, S1POS: AUX, S1S0B0Lemma: haben_viel_zu, S1S0B0LemmaPOS: haben_ADV_ADV, S1S0B0POS: AUX_ADV_ADV, S1S0B0POSLemma: AUX_ADV_zu, S1S0B0Token: habe_viel_zu, S1S0Lemma: haben_viel, S1S0LemmaPOS: haben_ADV, S1S0POS: AUX_ADV, S1S0POSLemma: AUX_viel, S1S0Token: habe_viel, S1Token: habe, StackLength: 2, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, viel_isGouvernedBy_tun: true, viel_isGouvernedBy_tun_advmod: true, 

41- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [habe]   B= [zu, tun, wie ,.. ]

B0Lemma: zu, B0POS: ADV, B0Token: zu, B1Lemma: tun, B1POS: ADJ, B1Token: tun, S0B0Distance: 5, S0B0Lemma: haben_zu, S0B0LemmaPOS: haben_ADV, S0B0POS: AUX_ADV, S0B0POSLemma: AUX_zu, S0B0Token: habe_zu, S0B1Lemma: haben_tun, S0B1LemmaPOS: haben_ADJ, S0B1POS: AUX_ADJ, S0B1POSLemma: AUX_tun, S0B1Token: habe_tun, S0B2Lemma: haben_wie, S0B2LemmaPOS: haben_ADP, S0B2POS: AUX_ADP, S0B2POSLemma: AUX_wie, S0B2Token: habe_wie, S0Lemma: haben, S0POS: AUX, S0Token: habe, StackLength: 1, haben_isGouvernedBy_tun: true, haben_isGouvernedBy_tun_aux: true, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

42- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [habe, zu]   B= [tun, wie, der ,.. ]

B0Lemma: tun, B0POS: ADJ, B0Token: tun, B1Lemma: wie, B1POS: ADP, B1Token: wie, S0B0Distance: 1, S0B0Lemma: zu_tun, S0B0LemmaPOS: zu_ADJ, S0B0POS: ADV_ADJ, S0B0POSLemma: ADV_tun, S0B0Token: zu_tun, S0B1Lemma: zu_wie, S0B1LemmaPOS: zu_ADP, S0B1POS: ADV_ADP, S0B1POSLemma: ADV_wie, S0B1Token: zu_wie, S0B2Lemma: zu_der, S0B2LemmaPOS: zu_DET, S0B2POS: ADV_DET, S0B2POSLemma: ADV_der, S0B2Token: zu_der, S0Lemma: zu, S0POS: ADV, S0S1Distance: 5, S0Token: zu, S1B0Lemma: haben_tun, S1B0LemmaPOS: haben_ADJ, S1B0POS: AUX_ADJ, S1B0POSLemma: AUX_tun, S1B0Token: habe_tun, S1Lemma: haben, S1POS: AUX, S1S0B0Lemma: haben_zu_tun, S1S0B0LemmaPOS: haben_ADV_ADJ, S1S0B0POS: AUX_ADV_ADJ, S1S0B0POSLemma: AUX_ADV_tun, S1S0B0Token: habe_zu_tun, S1S0Lemma: haben_zu, S1S0LemmaPOS: haben_ADV, S1S0POS: AUX_ADV, S1S0POSLemma: AUX_zu, S1S0Token: habe_zu, S1Token: habe, StackLength: 2, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, zu_isGouvernedBy_tun: true, zu_isGouvernedBy_tun_advmod: true, 

43- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [habe, zu, tun]   B= [wie, der, Mond ,.. ]

B0Lemma: wie, B0POS: ADP, B0Token: wie, B1Lemma: der, B1POS: DET, B1Token: der, S0B0Distance: 1, S0B0Lemma: tun_wie, S0B0LemmaPOS: tun_ADP, S0B0POS: ADJ_ADP, S0B0POSLemma: ADJ_wie, S0B0Token: tun_wie, S0B1Lemma: tun_der, S0B1LemmaPOS: tun_DET, S0B1POS: ADJ_DET, S0B1POSLemma: ADJ_der, S0B1Token: tun_der, S0B2Lemma: tun_Mond, S0B2LemmaPOS: tun_PROPN, S0B2POS: ADJ_PROPN, S0B2POSLemma: ADJ_Mond, S0B2Token: tun_Mond, S0Lemma: tun, S0POS: ADJ, S0S1Distance: 1, S0Token: tun, S1B0Lemma: zu_wie, S1B0LemmaPOS: zu_ADP, S1B0POS: ADV_ADP, S1B0POSLemma: ADV_wie, S1B0Token: zu_wie, S1Lemma: zu, S1POS: ADV, S1S0B0Lemma: zu_tun_wie, S1S0B0LemmaPOS: zu_ADJ_ADP, S1S0B0POS: ADV_ADJ_ADP, S1S0B0POSLemma: ADV_ADJ_wie, S1S0B0Token: zu_tun_wie, S1S0Lemma: zu_tun, S1S0LemmaPOS: zu_ADJ, S1S0POS: ADV_ADJ, S1S0POSLemma: ADV_tun, S1S0Token: zu_tun, S1Token: zu, StackLength: 3, SyntaxicRelation: -advmod, hasRighDep_nmod: true, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, tun_Gedicht_hasRighDep_nmod: true, tun_Mond_hasRighDep_nmod: true, tun_hasRighDep_nmod: true, 

44- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [habe, [zu, tun]]   B= [wie, der, Mond ,.. ]

B0Lemma: wie, B0POS: ADP, B0Token: wie, B1Lemma: der, B1POS: DET, B1Token: der, S0B0Distance: 1, S0B0Lemma: zu_tun_wie, S0B0LemmaPOS: zu_tun_ADP, S0B0POS: ADV_ADJ_ADP, S0B0POSLemma: ADV_ADJ_wie, S0B0Token: zu_tun_wie, S0B1Lemma: zu_tun_der, S0B1LemmaPOS: zu_tun_DET, S0B1POS: ADV_ADJ_DET, S0B1POSLemma: ADV_ADJ_der, S0B1Token: zu_tun_der, S0B2Lemma: zu_tun_Mond, S0B2LemmaPOS: zu_tun_PROPN, S0B2POS: ADV_ADJ_PROPN, S0B2POSLemma: ADV_ADJ_Mond, S0B2Token: zu_tun_Mond, S0Lemma: zu_tun, S0POS: ADV_ADJ, S0Token: zu_tun, S1B0Lemma: haben_wie, S1B0LemmaPOS: haben_ADP, S1B0POS: AUX_ADP, S1B0POSLemma: AUX_wie, S1B0Token: habe_wie, S1Lemma: haben, S1POS: AUX, S1S0B0Lemma: haben_zu_tun_wie, S1S0B0LemmaPOS: haben_ADV_ADJ_ADP, S1S0B0POS: AUX_ADV_ADJ_ADP, S1S0B0POSLemma: AUX_ADV_ADJ_wie, S1S0B0Token: habe_zu_tun_wie, S1S0Lemma: haben_zu_tun, S1S0LemmaPOS: haben_ADV_ADJ, S1S0POS: AUX_ADV_ADJ, S1S0POSLemma: AUX_zu_tun, S1S0Token: habe_zu_tun, S1Token: habe, StackLength: 2, transitionHistoryLength1: 0, transitionHistoryLength2: 00, transitionHistoryLength3: 002, 

45- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[habe, [zu, tun]]]   B= [wie, der, Mond ,.. ]

B0Lemma: wie, B0POS: ADP, B0Token: wie, B1Lemma: der, B1POS: DET, B1Token: der, S0B0Distance: 1, S0B0Lemma: haben_zu_tun_wie, S0B0LemmaPOS: haben_zu_tun_ADP, S0B0POS: AUX_ADV_ADJ_ADP, S0B0POSLemma: AUX_ADV_ADJ_wie, S0B0Token: habe_zu_tun_wie, S0B1Lemma: haben_zu_tun_der, S0B1LemmaPOS: haben_zu_tun_DET, S0B1POS: AUX_ADV_ADJ_DET, S0B1POSLemma: AUX_ADV_ADJ_der, S0B1Token: habe_zu_tun_der, S0B2Lemma: haben_zu_tun_Mond, S0B2LemmaPOS: haben_zu_tun_PROPN, S0B2POS: AUX_ADV_ADJ_PROPN, S0B2POSLemma: AUX_ADV_ADJ_Mond, S0B2Token: habe_zu_tun_Mond, S0Lemma: haben_zu_tun, S0POS: AUX_ADV_ADJ, S0Token: habe_zu_tun, StackLength: 1, transitionHistoryLength1: 1, transitionHistoryLength2: 10, transitionHistoryLength3: 100, 

46- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [wie, der, Mond ,.. ]

B0Lemma: wie, B0POS: ADP, B0Token: wie, B1Lemma: der, B1POS: DET, B1Token: der, transitionHistoryLength1: 1, transitionHistoryLength2: 11, transitionHistoryLength3: 110, 

47- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [wie]   B= [der, Mond, mit ,.. ]

B0Lemma: der, B0POS: DET, B0Token: der, B1Lemma: Mond, B1POS: PROPN, B1Token: Mond, S0B0Distance: 1, S0B0Lemma: wie_der, S0B0LemmaPOS: wie_DET, S0B0POS: ADP_DET, S0B0POSLemma: ADP_der, S0B0Token: wie_der, S0B1Lemma: wie_Mond, S0B1LemmaPOS: wie_PROPN, S0B1POS: ADP_PROPN, S0B1POSLemma: ADP_Mond, S0B1Token: wie_Mond, S0B2Lemma: wie_mit, S0B2LemmaPOS: wie_ADP, S0B2POS: ADP_ADP, S0B2POSLemma: ADP_mit, S0B2Token: wie_mit, S0Lemma: wie, S0POS: ADP, S0Token: wie, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 21, transitionHistoryLength3: 211, wie_isGouvernedBy_Mond: true, wie_isGouvernedBy_Mond_case: true, 

48- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [der, Mond, mit ,.. ]

B0Lemma: der, B0POS: DET, B0Token: der, B1Lemma: Mond, B1POS: PROPN, B1Token: Mond, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 021, 

49- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [der]   B= [Mond, mit, den ,.. ]

B0Lemma: Mond, B0POS: PROPN, B0Token: Mond, B1Lemma: mit, B1POS: ADP, B1Token: mit, S0B0Distance: 1, S0B0Lemma: der_Mond, S0B0LemmaPOS: der_PROPN, S0B0POS: DET_PROPN, S0B0POSLemma: DET_Mond, S0B0Token: der_Mond, S0B1Lemma: der_mit, S0B1LemmaPOS: der_ADP, S0B1POS: DET_ADP, S0B1POSLemma: DET_mit, S0B1Token: der_mit, S0B2Lemma: der_der, S0B2LemmaPOS: der_DET, S0B2POS: DET_DET, S0B2POSLemma: DET_der, S0B2Token: der_den, S0Lemma: der, S0POS: DET, S0Token: der, StackLength: 1, der_isGouvernedBy_Mond: true, der_isGouvernedBy_Mond_det: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

50- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Mond, mit, den ,.. ]

B0Lemma: Mond, B0POS: PROPN, B0Token: Mond, B1Lemma: mit, B1POS: ADP, B1Token: mit, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

51- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Mond]   B= [mit, den, Gedichten ,.. ]

B0Lemma: mit, B0POS: ADP, B0Token: mit, B1Lemma: der, B1POS: DET, B1Token: den, S0B0Distance: 1, S0B0Lemma: Mond_mit, S0B0LemmaPOS: Mond_ADP, S0B0POS: PROPN_ADP, S0B0POSLemma: PROPN_mit, S0B0Token: Mond_mit, S0B1Lemma: Mond_der, S0B1LemmaPOS: Mond_DET, S0B1POS: PROPN_DET, S0B1POSLemma: PROPN_der, S0B1Token: Mond_den, S0B2Lemma: Mond_Gedicht, S0B2LemmaPOS: Mond_NOUN, S0B2POS: PROPN_NOUN, S0B2POSLemma: PROPN_Gedicht, S0B2Token: Mond_Gedichten, S0Lemma: Mond, S0POS: PROPN, S0Token: Mond, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

52- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [mit, den, Gedichten ,.. ]

B0Lemma: mit, B0POS: ADP, B0Token: mit, B1Lemma: der, B1POS: DET, B1Token: den, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

53- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [mit]   B= [den, Gedichten, , ,.. ]

B0Lemma: der, B0POS: DET, B0Token: den, B1Lemma: Gedicht, B1POS: NOUN, B1Token: Gedichten, S0B0Distance: 1, S0B0Lemma: mit_der, S0B0LemmaPOS: mit_DET, S0B0POS: ADP_DET, S0B0POSLemma: ADP_der, S0B0Token: mit_den, S0B1Lemma: mit_Gedicht, S0B1LemmaPOS: mit_NOUN, S0B1POS: ADP_NOUN, S0B1POSLemma: ADP_Gedicht, S0B1Token: mit_Gedichten, S0B2Lemma: mit_,, S0B2LemmaPOS: mit_PUNCT, S0B2POS: ADP_PUNCT, S0B2POSLemma: ADP_,, S0B2Token: mit_,, S0Lemma: mit, S0POS: ADP, S0Token: mit, StackLength: 1, mit_isGouvernedBy_Gedicht: true, mit_isGouvernedBy_Gedicht_case: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

54- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [den, Gedichten, , ,.. ]

B0Lemma: der, B0POS: DET, B0Token: den, B1Lemma: Gedicht, B1POS: NOUN, B1Token: Gedichten, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

55- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [den]   B= [Gedichten, ,, die ,.. ]

B0Lemma: Gedicht, B0POS: NOUN, B0Token: Gedichten, B1Lemma: ,, B1POS: PUNCT, B1Token: ,, S0B0Distance: 1, S0B0Lemma: der_Gedicht, S0B0LemmaPOS: der_NOUN, S0B0POS: DET_NOUN, S0B0POSLemma: DET_Gedicht, S0B0Token: den_Gedichten, S0B1Lemma: der_,, S0B1LemmaPOS: der_PUNCT, S0B1POS: DET_PUNCT, S0B1POSLemma: DET_,, S0B1Token: den_,, S0B2Lemma: der_der, S0B2LemmaPOS: der_PRON, S0B2POS: DET_PRON, S0B2POSLemma: DET_der, S0B2Token: den_die, S0Lemma: der, S0POS: DET, S0Token: den, StackLength: 1, der_isGouvernedBy_Gedicht: true, der_isGouvernedBy_Gedicht_det: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

56- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Gedichten, ,, die ,.. ]

B0Lemma: Gedicht, B0POS: NOUN, B0Token: Gedichten, B1Lemma: ,, B1POS: PUNCT, B1Token: ,, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

57- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Gedichten]   B= [,, die, auf ,.. ]

B0Lemma: ,, B0POS: PUNCT, B0Token: ,, B1Lemma: der, B1POS: PRON, B1Token: die, Gedicht_,_hasRighDep_punct: true, Gedicht_abgesondern_hasRighDep_acl: true, Gedicht_hasRighDep_acl: true, Gedicht_hasRighDep_punct: true, S0B0Distance: 1, S0B0Lemma: Gedicht_,, S0B0LemmaPOS: Gedicht_PUNCT, S0B0POS: NOUN_PUNCT, S0B0POSLemma: NOUN_,, S0B0Token: Gedichten_,, S0B1Lemma: Gedicht_der, S0B1LemmaPOS: Gedicht_PRON, S0B1POS: NOUN_PRON, S0B1POSLemma: NOUN_der, S0B1Token: Gedichten_die, S0B2Lemma: Gedicht_auf, S0B2LemmaPOS: Gedicht_ADP, S0B2POS: NOUN_ADP, S0B2POSLemma: NOUN_auf, S0B2Token: Gedichten_auf, S0Lemma: Gedicht, S0POS: NOUN, S0Token: Gedichten, StackLength: 1, hasRighDep_acl: true, hasRighDep_punct: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

58- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, die, auf ,.. ]

B0Lemma: ,, B0POS: PUNCT, B0Token: ,, B1Lemma: der, B1POS: PRON, B1Token: die, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

59- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [die, auf, ihn ,.. ]

B0Lemma: der, B0POS: PRON, B0Token: die, B1Lemma: auf, B1POS: ADP, B1Token: auf, S0B0Distance: 1, S0B0Lemma: ,_der, S0B0LemmaPOS: ,_PRON, S0B0POS: PUNCT_PRON, S0B0POSLemma: PUNCT_der, S0B0Token: ,_die, S0B1Lemma: ,_auf, S0B1LemmaPOS: ,_ADP, S0B1POS: PUNCT_ADP, S0B1POSLemma: PUNCT_auf, S0B1Token: ,_auf, S0B2Lemma: ,_er, S0B2LemmaPOS: ,_PRON, S0B2POS: PUNCT_PRON, S0B2POSLemma: PUNCT_er, S0B2Token: ,_ihn, S0Lemma: ,, S0POS: PUNCT, S0Token: ,, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

60- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [die, auf, ihn ,.. ]

B0Lemma: der, B0POS: PRON, B0Token: die, B1Lemma: auf, B1POS: ADP, B1Token: auf, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

61- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [die]   B= [auf, ihn, abgesondert ,.. ]

B0Lemma: auf, B0POS: ADP, B0Token: auf, B1Lemma: er, B1POS: PRON, B1Token: ihn, S0B0Distance: 1, S0B0Lemma: der_auf, S0B0LemmaPOS: der_ADP, S0B0POS: PRON_ADP, S0B0POSLemma: PRON_auf, S0B0Token: die_auf, S0B1Lemma: der_er, S0B1LemmaPOS: der_PRON, S0B1POS: PRON_PRON, S0B1POSLemma: PRON_er, S0B1Token: die_ihn, S0B2Lemma: der_abgesondern, S0B2LemmaPOS: der_VERB, S0B2POS: PRON_VERB, S0B2POSLemma: PRON_abgesondern, S0B2Token: die_abgesondert, S0Lemma: der, S0POS: PRON, S0Token: die, StackLength: 1, der_isGouvernedBy_abgesondern: true, der_isGouvernedBy_abgesondern_nsubjpass: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

62- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [auf, ihn, abgesondert ,.. ]

B0Lemma: auf, B0POS: ADP, B0Token: auf, B1Lemma: er, B1POS: PRON, B1Token: ihn, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

63- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [auf]   B= [ihn, abgesondert, werden ,.. ]

B0Lemma: er, B0POS: PRON, B0Token: ihn, B1Lemma: abgesondern, B1POS: VERB, B1Token: abgesondert, S0B0Distance: 1, S0B0Lemma: auf_er, S0B0LemmaPOS: auf_PRON, S0B0POS: ADP_PRON, S0B0POSLemma: ADP_er, S0B0Token: auf_ihn, S0B1Lemma: auf_abgesondern, S0B1LemmaPOS: auf_VERB, S0B1POS: ADP_VERB, S0B1POSLemma: ADP_abgesondern, S0B1Token: auf_abgesondert, S0B2Lemma: auf_werden, S0B2LemmaPOS: auf_AUX, S0B2POS: ADP_AUX, S0B2POSLemma: ADP_werden, S0B2Token: auf_werden, S0Lemma: auf, S0POS: ADP, S0Token: auf, StackLength: 1, auf_isGouvernedBy_er: true, auf_isGouvernedBy_er_case: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

64- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ihn, abgesondert, werden ,.. ]

B0Lemma: er, B0POS: PRON, B0Token: ihn, B1Lemma: abgesondern, B1POS: VERB, B1Token: abgesondert, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

65- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ihn]   B= [abgesondert, werden, . ,.. ]

B0Lemma: abgesondern, B0POS: VERB, B0Token: abgesondert, B1Lemma: werden, B1POS: AUX, B1Token: werden, S0B0Distance: 1, S0B0Lemma: er_abgesondern, S0B0LemmaPOS: er_VERB, S0B0POS: PRON_VERB, S0B0POSLemma: PRON_abgesondern, S0B0Token: ihn_abgesondert, S0B1Lemma: er_werden, S0B1LemmaPOS: er_AUX, S0B1POS: PRON_AUX, S0B1POSLemma: PRON_werden, S0B1Token: ihn_werden, S0B2Lemma: er_., S0B2LemmaPOS: er_PUNCT, S0B2POS: PRON_PUNCT, S0B2POSLemma: PRON_., S0B2Token: ihn_., S0Lemma: er, S0POS: PRON, S0Token: ihn, StackLength: 1, er_isGouvernedBy_abgesondern: true, er_isGouvernedBy_abgesondern_nmod: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

66- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [abgesondert, werden, . ,.. ]

B0Lemma: abgesondern, B0POS: VERB, B0Token: abgesondert, B1Lemma: werden, B1POS: AUX, B1Token: werden, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

67- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [abgesondert]   B= [werden, . ,.. ]

B0Lemma: werden, B0POS: AUX, B0Token: werden, B1Lemma: ., B1POS: PUNCT, B1Token: ., S0B0Distance: 1, S0B0Lemma: abgesondern_werden, S0B0LemmaPOS: abgesondern_AUX, S0B0POS: VERB_AUX, S0B0POSLemma: VERB_werden, S0B0Token: abgesondert_werden, S0B1Lemma: abgesondern_., S0B1LemmaPOS: abgesondern_PUNCT, S0B1POS: VERB_PUNCT, S0B1POSLemma: VERB_., S0B1Token: abgesondert_., S0Lemma: abgesondern, S0POS: VERB, S0Token: abgesondert, StackLength: 1, abgesondern_hasRighDep_auxpass: true, abgesondern_werden_hasRighDep_auxpass: true, hasRighDep_auxpass: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

68- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [abgesondert, werden]   B= [.]

B0Lemma: ., B0POS: PUNCT, B0Token: ., S0B0Distance: 1, S0B0Lemma: werden_., S0B0LemmaPOS: werden_PUNCT, S0B0POS: AUX_PUNCT, S0B0POSLemma: AUX_., S0B0Token: werden_., S0Lemma: werden, S0POS: AUX, S0S1Distance: 1, S0Token: werden, S1B0Lemma: abgesondern_., S1B0LemmaPOS: abgesondern_PUNCT, S1B0POS: VERB_PUNCT, S1B0POSLemma: VERB_., S1B0Token: abgesondert_., S1Lemma: abgesondern, S1POS: VERB, S1S0B0Lemma: abgesondern_werden_., S1S0B0LemmaPOS: abgesondern_AUX_PUNCT, S1S0B0POS: VERB_AUX_PUNCT, S1S0B0POSLemma: VERB_AUX_., S1S0B0Token: abgesondert_werden_., S1S0Lemma: abgesondern_werden, S1S0LemmaPOS: abgesondern_AUX, S1S0POS: VERB_AUX, S1S0POSLemma: VERB_werden, S1S0Token: abgesondert_werden, S1Token: abgesondert, StackLength: 2, SyntaxicRelation: +auxpass, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

69- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [abgesondert]   B= [.]

B0Lemma: ., B0POS: PUNCT, B0Token: ., S0B0Distance: 2, S0B0Lemma: abgesondern_., S0B0LemmaPOS: abgesondern_PUNCT, S0B0POS: VERB_PUNCT, S0B0POSLemma: VERB_., S0B0Token: abgesondert_., S0Lemma: abgesondern, S0POS: VERB, S0Token: abgesondert, StackLength: 1, transitionHistoryLength1: 0, transitionHistoryLength2: 00, transitionHistoryLength3: 002, 

70- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [abgesondert, .]   B= [ ]

S0Lemma: ., S0POS: PUNCT, S0S1Distance: 2, S0Token: ., S1Lemma: abgesondern, S1POS: VERB, S1S0Lemma: abgesondern_., S1S0LemmaPOS: abgesondern_PUNCT, S1S0POS: VERB_PUNCT, S1S0POSLemma: VERB_., S1S0Token: abgesondert_., S1Token: abgesondert, StackLength: 2, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 200, 

71- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [abgesondert]   B= [ ]

S0Lemma: abgesondern, S0POS: VERB, S0Token: abgesondert, StackLength: 1, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

72- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

## Sentence No. 506 - 
Fall Jonny K. : Hauptverdächtigter stellt sich der Polizei Möchten Sehbehinderte und Blinde ihre Kreuzchen im Wahllokal machen , so bringen diese eigene Schablonen mit . 
### Existing MWEs: 
1- **stellt sich** (IReflV)
2- **Kreuzchen machen** (ID)



0- &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Fall, Jonny, K. ,.. ]

B0Lemma: Fall, B0POS: NOUN, B0Token: Fall, B1Lemma: Jonny, B1POS: PROPN, B1Token: Jonny, 

1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Fall]   B= [Jonny, K., : ,.. ]

B0Lemma: Jonny, B0POS: PROPN, B0Token: Jonny, B1Lemma: K., B1POS: PROPN, B1Token: K., Fall_Hauptverdächtigte_hasRighDep_appos: true, Fall_hasRighDep_appos: true, Fall_isGouvernedBy_stellen: true, Fall_isGouvernedBy_stellen_nsubj: true, S0B0Distance: 1, S0B0Lemma: Fall_Jonny, S0B0LemmaPOS: Fall_PROPN, S0B0POS: NOUN_PROPN, S0B0POSLemma: NOUN_Jonny, S0B0Token: Fall_Jonny, S0B1Lemma: Fall_K., S0B1LemmaPOS: Fall_PROPN, S0B1POS: NOUN_PROPN, S0B1POSLemma: NOUN_K., S0B1Token: Fall_K., S0B2Lemma: Fall_:, S0B2LemmaPOS: Fall_PUNCT, S0B2POS: NOUN_PUNCT, S0B2POSLemma: NOUN_:, S0B2Token: Fall_:, S0Lemma: Fall, S0POS: NOUN, S0Token: Fall, StackLength: 1, hasRighDep_appos: true, 

2- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Jonny, K., : ,.. ]

B0Lemma: Jonny, B0POS: PROPN, B0Token: Jonny, B1Lemma: K., B1POS: PROPN, B1Token: K., transitionHistoryLength1: 0, 

3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Jonny]   B= [K., :, Hauptverdächtigter ,.. ]

B0Lemma: K., B0POS: PROPN, B0Token: K., B1Lemma: :, B1POS: PUNCT, B1Token: :, Jonny_isGouvernedBy_K.: true, Jonny_isGouvernedBy_K._name: true, S0B0Distance: 1, S0B0Lemma: Jonny_K., S0B0LemmaPOS: Jonny_PROPN, S0B0POS: PROPN_PROPN, S0B0POSLemma: PROPN_K., S0B0Token: Jonny_K., S0B1Lemma: Jonny_:, S0B1LemmaPOS: Jonny_PUNCT, S0B1POS: PROPN_PUNCT, S0B1POSLemma: PROPN_:, S0B1Token: Jonny_:, S0B2Lemma: Jonny_Hauptverdächtigte, S0B2LemmaPOS: Jonny_NOUN, S0B2POS: PROPN_NOUN, S0B2POSLemma: PROPN_Hauptverdächtigte, S0B2Token: Jonny_Hauptverdächtigter, S0Lemma: Jonny, S0POS: PROPN, S0Token: Jonny, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, 

4- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [K., :, Hauptverdächtigter ,.. ]

B0Lemma: K., B0POS: PROPN, B0Token: K., B1Lemma: :, B1POS: PUNCT, B1Token: :, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [K.]   B= [:, Hauptverdächtigter, stellt ,.. ]

B0Lemma: :, B0POS: PUNCT, B0Token: :, B1Lemma: Hauptverdächtigte, B1POS: NOUN, B1Token: Hauptverdächtigter, K._isGouvernedBy_Hauptverdächtigte: true, K._isGouvernedBy_Hauptverdächtigte_nmod: true, S0B0Distance: 1, S0B0Lemma: K._:, S0B0LemmaPOS: K._PUNCT, S0B0POS: PROPN_PUNCT, S0B0POSLemma: PROPN_:, S0B0Token: K._:, S0B1Lemma: K._Hauptverdächtigte, S0B1LemmaPOS: K._NOUN, S0B1POS: PROPN_NOUN, S0B1POSLemma: PROPN_Hauptverdächtigte, S0B1Token: K._Hauptverdächtigter, S0B2Lemma: K._stellen, S0B2LemmaPOS: K._VERB, S0B2POS: PROPN_VERB, S0B2POSLemma: PROPN_stellen, S0B2Token: K._stellt, S0Lemma: K., S0POS: PROPN, S0Token: K., StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

6- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [:, Hauptverdächtigter, stellt ,.. ]

B0Lemma: :, B0POS: PUNCT, B0Token: :, B1Lemma: Hauptverdächtigte, B1POS: NOUN, B1Token: Hauptverdächtigter, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [:]   B= [Hauptverdächtigter, stellt, sich ,.. ]

:_isGouvernedBy_Hauptverdächtigte: true, :_isGouvernedBy_Hauptverdächtigte_punct: true, B0Lemma: Hauptverdächtigte, B0POS: NOUN, B0Token: Hauptverdächtigter, B1Lemma: stellen, B1POS: VERB, B1Token: stellt, S0B0Distance: 1, S0B0Lemma: :_Hauptverdächtigte, S0B0LemmaPOS: :_NOUN, S0B0POS: PUNCT_NOUN, S0B0POSLemma: PUNCT_Hauptverdächtigte, S0B0Token: :_Hauptverdächtigter, S0B1Lemma: :_stellen, S0B1LemmaPOS: :_VERB, S0B1POS: PUNCT_VERB, S0B1POSLemma: PUNCT_stellen, S0B1Token: :_stellt, S0B2Lemma: :_er|es|sie, S0B2LemmaPOS: :_PRON, S0B2POS: PUNCT_PRON, S0B2POSLemma: PUNCT_er|es|sie, S0B2Token: :_sich, S0Lemma: :, S0POS: PUNCT, S0Token: :, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

8- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Hauptverdächtigter, stellt, sich ,.. ]

B0Lemma: Hauptverdächtigte, B0POS: NOUN, B0Token: Hauptverdächtigter, B1Lemma: stellen, B1POS: VERB, B1Token: stellt, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Hauptverdächtigter]   B= [stellt, sich, der ,.. ]

B0Lemma: stellen, B0POS: VERB, B0Token: stellt, B1Lemma: er|es|sie, B1POS: PRON, B1Token: sich, S0B0Distance: 1, S0B0Lemma: Hauptverdächtigte_stellen, S0B0LemmaPOS: Hauptverdächtigte_VERB, S0B0POS: NOUN_VERB, S0B0POSLemma: NOUN_stellen, S0B0Token: Hauptverdächtigter_stellt, S0B1Lemma: Hauptverdächtigte_er|es|sie, S0B1LemmaPOS: Hauptverdächtigte_PRON, S0B1POS: NOUN_PRON, S0B1POSLemma: NOUN_er|es|sie, S0B1Token: Hauptverdächtigter_sich, S0B2Lemma: Hauptverdächtigte_der, S0B2LemmaPOS: Hauptverdächtigte_DET, S0B2POS: NOUN_DET, S0B2POSLemma: NOUN_der, S0B2Token: Hauptverdächtigter_der, S0Lemma: Hauptverdächtigte, S0POS: NOUN, S0Token: Hauptverdächtigter, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

10- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [stellt, sich, der ,.. ]

B0Lemma: stellen, B0POS: VERB, B0Token: stellt, B1Lemma: er|es|sie, B1POS: PRON, B1Token: sich, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [stellt]   B= [sich, der, Polizei ,.. ]

B0Lemma: er|es|sie, B0POS: PRON, B0Token: sich, B1Lemma: der, B1POS: DET, B1Token: der, S0B0Distance: 1, S0B0Lemma: stellen_er|es|sie, S0B0LemmaPOS: stellen_PRON, S0B0POS: VERB_PRON, S0B0POSLemma: VERB_er|es|sie, S0B0Token: stellt_sich, S0B1Lemma: stellen_der, S0B1LemmaPOS: stellen_DET, S0B1POS: VERB_DET, S0B1POSLemma: VERB_der, S0B1Token: stellt_der, S0B2Lemma: stellen_Polizei, S0B2LemmaPOS: stellen_NOUN, S0B2POS: VERB_NOUN, S0B2POSLemma: VERB_Polizei, S0B2Token: stellt_Polizei, S0Lemma: stellen, S0POS: VERB, S0Token: stellt, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

12- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [stellt, sich]   B= [der, Polizei, Möchten ,.. ]

B0Lemma: der, B0POS: DET, B0Token: der, B1Lemma: Polizei, B1POS: NOUN, B1Token: Polizei, S0B0Distance: 1, S0B0Lemma: er|es|sie_der, S0B0LemmaPOS: er|es|sie_DET, S0B0POS: PRON_DET, S0B0POSLemma: PRON_der, S0B0Token: sich_der, S0B1Lemma: er|es|sie_Polizei, S0B1LemmaPOS: er|es|sie_NOUN, S0B1POS: PRON_NOUN, S0B1POSLemma: PRON_Polizei, S0B1Token: sich_Polizei, S0B2Lemma: er|es|sie_mögen, S0B2LemmaPOS: er|es|sie_AUX, S0B2POS: PRON_AUX, S0B2POSLemma: PRON_mögen, S0B2Token: sich_Möchten, S0Lemma: er|es|sie, S0POS: PRON, S0S1Distance: 1, S0Token: sich, S1B0Lemma: stellen_der, S1B0LemmaPOS: stellen_DET, S1B0POS: VERB_DET, S1B0POSLemma: VERB_der, S1B0Token: stellt_der, S1Lemma: stellen, S1POS: VERB, S1S0B0Lemma: stellen_er|es|sie_der, S1S0B0LemmaPOS: stellen_PRON_DET, S1S0B0POS: VERB_PRON_DET, S1S0B0POSLemma: VERB_PRON_der, S1S0B0Token: stellt_sich_der, S1S0Lemma: stellen_er|es|sie, S1S0LemmaPOS: stellen_PRON, S1S0POS: VERB_PRON, S1S0POSLemma: VERB_er|es|sie, S1S0Token: stellt_sich, S1Token: stellt, StackLength: 2, SyntaxicRelation: +dobj, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

13- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[stellt, sich]]   B= [der, Polizei, Möchten ,.. ]

B0Lemma: der, B0POS: DET, B0Token: der, B1Lemma: Polizei, B1POS: NOUN, B1Token: Polizei, S0B0Distance: 1, S0B0Lemma: stellen_er|es|sie_der, S0B0LemmaPOS: stellen_er|es|sie_DET, S0B0POS: VERB_PRON_DET, S0B0POSLemma: VERB_PRON_der, S0B0Token: stellt_sich_der, S0B1Lemma: stellen_er|es|sie_Polizei, S0B1LemmaPOS: stellen_er|es|sie_NOUN, S0B1POS: VERB_PRON_NOUN, S0B1POSLemma: VERB_PRON_Polizei, S0B1Token: stellt_sich_Polizei, S0B2Lemma: stellen_er|es|sie_mögen, S0B2LemmaPOS: stellen_er|es|sie_AUX, S0B2POS: VERB_PRON_AUX, S0B2POSLemma: VERB_PRON_mögen, S0B2Token: stellt_sich_Möchten, S0Lemma: stellen_er|es|sie, S0POS: VERB_PRON, S0Token: stellt_sich, StackLength: 1, transitionHistoryLength1: 0, transitionHistoryLength2: 00, transitionHistoryLength3: 002, 

14- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [der, Polizei, Möchten ,.. ]

B0Lemma: der, B0POS: DET, B0Token: der, B1Lemma: Polizei, B1POS: NOUN, B1Token: Polizei, transitionHistoryLength1: 1, transitionHistoryLength2: 10, transitionHistoryLength3: 100, 

15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [der]   B= [Polizei, Möchten, Sehbehinderte ,.. ]

B0Lemma: Polizei, B0POS: NOUN, B0Token: Polizei, B1Lemma: mögen, B1POS: AUX, B1Token: Möchten, S0B0Distance: 1, S0B0Lemma: der_Polizei, S0B0LemmaPOS: der_NOUN, S0B0POS: DET_NOUN, S0B0POSLemma: DET_Polizei, S0B0Token: der_Polizei, S0B1Lemma: der_mögen, S0B1LemmaPOS: der_AUX, S0B1POS: DET_AUX, S0B1POSLemma: DET_mögen, S0B1Token: der_Möchten, S0B2Lemma: der_sehbehinderte, S0B2LemmaPOS: der_NOUN, S0B2POS: DET_NOUN, S0B2POSLemma: DET_sehbehinderte, S0B2Token: der_Sehbehinderte, S0Lemma: der, S0POS: DET, S0Token: der, StackLength: 1, der_isGouvernedBy_Polizei: true, der_isGouvernedBy_Polizei_det: true, transitionHistoryLength1: 2, transitionHistoryLength2: 21, transitionHistoryLength3: 210, 

16- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Polizei, Möchten, Sehbehinderte ,.. ]

B0Lemma: Polizei, B0POS: NOUN, B0Token: Polizei, B1Lemma: mögen, B1POS: AUX, B1Token: Möchten, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 021, 

17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Polizei]   B= [Möchten, Sehbehinderte, und ,.. ]

B0Lemma: mögen, B0POS: AUX, B0Token: Möchten, B1Lemma: sehbehinderte, B1POS: NOUN, B1Token: Sehbehinderte, Polizei_hasRighDep_appos: true, Polizei_sehbehinderte_hasRighDep_appos: true, S0B0Distance: 1, S0B0Lemma: Polizei_mögen, S0B0LemmaPOS: Polizei_AUX, S0B0POS: NOUN_AUX, S0B0POSLemma: NOUN_mögen, S0B0Token: Polizei_Möchten, S0B1Lemma: Polizei_sehbehinderte, S0B1LemmaPOS: Polizei_NOUN, S0B1POS: NOUN_NOUN, S0B1POSLemma: NOUN_sehbehinderte, S0B1Token: Polizei_Sehbehinderte, S0B2Lemma: Polizei_und, S0B2LemmaPOS: Polizei_CONJ, S0B2POS: NOUN_CONJ, S0B2POSLemma: NOUN_und, S0B2Token: Polizei_und, S0Lemma: Polizei, S0POS: NOUN, S0Token: Polizei, StackLength: 1, hasRighDep_appos: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

18- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Möchten, Sehbehinderte, und ,.. ]

B0Lemma: mögen, B0POS: AUX, B0Token: Möchten, B1Lemma: sehbehinderte, B1POS: NOUN, B1Token: Sehbehinderte, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Möchten]   B= [Sehbehinderte, und, Blinde ,.. ]

B0Lemma: sehbehinderte, B0POS: NOUN, B0Token: Sehbehinderte, B1Lemma: und, B1POS: CONJ, B1Token: und, S0B0Distance: 1, S0B0Lemma: mögen_sehbehinderte, S0B0LemmaPOS: mögen_NOUN, S0B0POS: AUX_NOUN, S0B0POSLemma: AUX_sehbehinderte, S0B0Token: Möchten_Sehbehinderte, S0B1Lemma: mögen_und, S0B1LemmaPOS: mögen_CONJ, S0B1POS: AUX_CONJ, S0B1POSLemma: AUX_und, S0B1Token: Möchten_und, S0B2Lemma: mögen_Blinde, S0B2LemmaPOS: mögen_NOUN, S0B2POS: AUX_NOUN, S0B2POSLemma: AUX_Blinde, S0B2Token: Möchten_Blinde, S0Lemma: mögen, S0POS: AUX, S0Token: Möchten, StackLength: 1, mögen_isGouvernedBy_sehbehinderte: true, mögen_isGouvernedBy_sehbehinderte_aux: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

20- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Sehbehinderte, und, Blinde ,.. ]

B0Lemma: sehbehinderte, B0POS: NOUN, B0Token: Sehbehinderte, B1Lemma: und, B1POS: CONJ, B1Token: und, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Sehbehinderte]   B= [und, Blinde, ihre ,.. ]

B0Lemma: und, B0POS: CONJ, B0Token: und, B1Lemma: Blinde, B1POS: NOUN, B1Token: Blinde, S0B0Distance: 1, S0B0Lemma: sehbehinderte_und, S0B0LemmaPOS: sehbehinderte_CONJ, S0B0POS: NOUN_CONJ, S0B0POSLemma: NOUN_und, S0B0Token: Sehbehinderte_und, S0B1Lemma: sehbehinderte_Blinde, S0B1LemmaPOS: sehbehinderte_NOUN, S0B1POS: NOUN_NOUN, S0B1POSLemma: NOUN_Blinde, S0B1Token: Sehbehinderte_Blinde, S0B2Lemma: sehbehinderte_ihr, S0B2LemmaPOS: sehbehinderte_DET, S0B2POS: NOUN_DET, S0B2POSLemma: NOUN_ihr, S0B2Token: Sehbehinderte_ihre, S0Lemma: sehbehinderte, S0POS: NOUN, S0Token: Sehbehinderte, StackLength: 1, hasRighDep_cc: true, hasRighDep_conj: true, sehbehinderte_Blinde_hasRighDep_conj: true, sehbehinderte_hasRighDep_cc: true, sehbehinderte_hasRighDep_conj: true, sehbehinderte_und_hasRighDep_cc: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

22- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [und, Blinde, ihre ,.. ]

B0Lemma: und, B0POS: CONJ, B0Token: und, B1Lemma: Blinde, B1POS: NOUN, B1Token: Blinde, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

23- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [und]   B= [Blinde, ihre, Kreuzchen ,.. ]

B0Lemma: Blinde, B0POS: NOUN, B0Token: Blinde, B1Lemma: ihr, B1POS: DET, B1Token: ihre, S0B0Distance: 1, S0B0Lemma: und_Blinde, S0B0LemmaPOS: und_NOUN, S0B0POS: CONJ_NOUN, S0B0POSLemma: CONJ_Blinde, S0B0Token: und_Blinde, S0B1Lemma: und_ihr, S0B1LemmaPOS: und_DET, S0B1POS: CONJ_DET, S0B1POSLemma: CONJ_ihr, S0B1Token: und_ihre, S0B2Lemma: und_Kreuzchen, S0B2LemmaPOS: und_NOUN, S0B2POS: CONJ_NOUN, S0B2POSLemma: CONJ_Kreuzchen, S0B2Token: und_Kreuzchen, S0Lemma: und, S0POS: CONJ, S0Token: und, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

24- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Blinde, ihre, Kreuzchen ,.. ]

B0Lemma: Blinde, B0POS: NOUN, B0Token: Blinde, B1Lemma: ihr, B1POS: DET, B1Token: ihre, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

25- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Blinde]   B= [ihre, Kreuzchen, im ,.. ]

B0Lemma: ihr, B0POS: DET, B0Token: ihre, B1Lemma: Kreuzchen, B1POS: NOUN, B1Token: Kreuzchen, S0B0Distance: 1, S0B0Lemma: Blinde_ihr, S0B0LemmaPOS: Blinde_DET, S0B0POS: NOUN_DET, S0B0POSLemma: NOUN_ihr, S0B0Token: Blinde_ihre, S0B1Lemma: Blinde_Kreuzchen, S0B1LemmaPOS: Blinde_NOUN, S0B1POS: NOUN_NOUN, S0B1POSLemma: NOUN_Kreuzchen, S0B1Token: Blinde_Kreuzchen, S0B2Lemma: Blinde_in+der, S0B2LemmaPOS: Blinde_ADP, S0B2POS: NOUN_ADP, S0B2POSLemma: NOUN_in+der, S0B2Token: Blinde_im, S0Lemma: Blinde, S0POS: NOUN, S0Token: Blinde, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

26- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ihre, Kreuzchen, im ,.. ]

B0Lemma: ihr, B0POS: DET, B0Token: ihre, B1Lemma: Kreuzchen, B1POS: NOUN, B1Token: Kreuzchen, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

27- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ihre]   B= [Kreuzchen, im, Wahllokal ,.. ]

B0Lemma: Kreuzchen, B0POS: NOUN, B0Token: Kreuzchen, B1Lemma: in+der, B1POS: ADP, B1Token: im, S0B0Distance: 1, S0B0Lemma: ihr_Kreuzchen, S0B0LemmaPOS: ihr_NOUN, S0B0POS: DET_NOUN, S0B0POSLemma: DET_Kreuzchen, S0B0Token: ihre_Kreuzchen, S0B1Lemma: ihr_in+der, S0B1LemmaPOS: ihr_ADP, S0B1POS: DET_ADP, S0B1POSLemma: DET_in+der, S0B1Token: ihre_im, S0B2Lemma: ihr_Wahllokal, S0B2LemmaPOS: ihr_NOUN, S0B2POS: DET_NOUN, S0B2POSLemma: DET_Wahllokal, S0B2Token: ihre_Wahllokal, S0Lemma: ihr, S0POS: DET, S0Token: ihre, StackLength: 1, ihr_isGouvernedBy_Kreuzchen: true, ihr_isGouvernedBy_Kreuzchen_det:poss: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

28- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Kreuzchen, im, Wahllokal ,.. ]

B0Lemma: Kreuzchen, B0POS: NOUN, B0Token: Kreuzchen, B1Lemma: in+der, B1POS: ADP, B1Token: im, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

29- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Kreuzchen]   B= [im, Wahllokal, machen ,.. ]

B0Lemma: in+der, B0POS: ADP, B0Token: im, B1Lemma: Wahllokal, B1POS: NOUN, B1Token: Wahllokal, Kreuzchen_isGouvernedBy_machen: true, Kreuzchen_isGouvernedBy_machen_conj: true, S0B0Distance: 1, S0B0Lemma: Kreuzchen_in+der, S0B0LemmaPOS: Kreuzchen_ADP, S0B0POS: NOUN_ADP, S0B0POSLemma: NOUN_in+der, S0B0Token: Kreuzchen_im, S0B1Lemma: Kreuzchen_Wahllokal, S0B1LemmaPOS: Kreuzchen_NOUN, S0B1POS: NOUN_NOUN, S0B1POSLemma: NOUN_Wahllokal, S0B1Token: Kreuzchen_Wahllokal, S0B2Lemma: Kreuzchen_machen, S0B2LemmaPOS: Kreuzchen_VERB, S0B2POS: NOUN_VERB, S0B2POSLemma: NOUN_machen, S0B2Token: Kreuzchen_machen, S0Lemma: Kreuzchen, S0POS: NOUN, S0Token: Kreuzchen, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

30- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Kreuzchen, im]   B= [Wahllokal, machen, , ,.. ]

B0Lemma: Wahllokal, B0POS: NOUN, B0Token: Wahllokal, B1Lemma: machen, B1POS: VERB, B1Token: machen, S0B0Distance: 1, S0B0Lemma: in+der_Wahllokal, S0B0LemmaPOS: in+der_NOUN, S0B0POS: ADP_NOUN, S0B0POSLemma: ADP_Wahllokal, S0B0Token: im_Wahllokal, S0B1Lemma: in+der_machen, S0B1LemmaPOS: in+der_VERB, S0B1POS: ADP_VERB, S0B1POSLemma: ADP_machen, S0B1Token: im_machen, S0B2Lemma: in+der_,, S0B2LemmaPOS: in+der_PUNCT, S0B2POS: ADP_PUNCT, S0B2POSLemma: ADP_,, S0B2Token: im_,, S0Lemma: in+der, S0POS: ADP, S0S1Distance: 1, S0Token: im, S1B0Lemma: Kreuzchen_Wahllokal, S1B0LemmaPOS: Kreuzchen_NOUN, S1B0POS: NOUN_NOUN, S1B0POSLemma: NOUN_Wahllokal, S1B0Token: Kreuzchen_Wahllokal, S1Lemma: Kreuzchen, S1POS: NOUN, S1S0B0Lemma: Kreuzchen_in+der_Wahllokal, S1S0B0LemmaPOS: Kreuzchen_ADP_NOUN, S1S0B0POS: NOUN_ADP_NOUN, S1S0B0POSLemma: NOUN_ADP_Wahllokal, S1S0B0Token: Kreuzchen_im_Wahllokal, S1S0Lemma: Kreuzchen_in+der, S1S0LemmaPOS: Kreuzchen_ADP, S1S0POS: NOUN_ADP, S1S0POSLemma: NOUN_in+der, S1S0Token: Kreuzchen_im, S1Token: Kreuzchen, StackLength: 2, in+der_isGouvernedBy_Wahllokal: true, in+der_isGouvernedBy_Wahllokal_case: true, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

31- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Kreuzchen]   B= [Wahllokal, machen, , ,.. ]

B0Lemma: Wahllokal, B0POS: NOUN, B0Token: Wahllokal, B1Lemma: machen, B1POS: VERB, B1Token: machen, Kreuzchen_isGouvernedBy_machen: true, Kreuzchen_isGouvernedBy_machen_conj: true, S0B0Distance: 2, S0B0Lemma: Kreuzchen_Wahllokal, S0B0LemmaPOS: Kreuzchen_NOUN, S0B0POS: NOUN_NOUN, S0B0POSLemma: NOUN_Wahllokal, S0B0Token: Kreuzchen_Wahllokal, S0B1Lemma: Kreuzchen_machen, S0B1LemmaPOS: Kreuzchen_VERB, S0B1POS: NOUN_VERB, S0B1POSLemma: NOUN_machen, S0B1Token: Kreuzchen_machen, S0B2Lemma: Kreuzchen_,, S0B2LemmaPOS: Kreuzchen_PUNCT, S0B2POS: NOUN_PUNCT, S0B2POSLemma: NOUN_,, S0B2Token: Kreuzchen_,, S0Lemma: Kreuzchen, S0POS: NOUN, S0Token: Kreuzchen, StackLength: 1, transitionHistoryLength1: 0, transitionHistoryLength2: 00, transitionHistoryLength3: 002, 

32- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Kreuzchen, Wahllokal]   B= [machen, ,, so ,.. ]

B0Lemma: machen, B0POS: VERB, B0Token: machen, B1Lemma: ,, B1POS: PUNCT, B1Token: ,, S0B0Distance: 1, S0B0Lemma: Wahllokal_machen, S0B0LemmaPOS: Wahllokal_VERB, S0B0POS: NOUN_VERB, S0B0POSLemma: NOUN_machen, S0B0Token: Wahllokal_machen, S0B1Lemma: Wahllokal_,, S0B1LemmaPOS: Wahllokal_PUNCT, S0B1POS: NOUN_PUNCT, S0B1POSLemma: NOUN_,, S0B1Token: Wahllokal_,, S0B2Lemma: Wahllokal_so, S0B2LemmaPOS: Wahllokal_ADV, S0B2POS: NOUN_ADV, S0B2POSLemma: NOUN_so, S0B2Token: Wahllokal_so, S0Lemma: Wahllokal, S0POS: NOUN, S0S1Distance: 2, S0Token: Wahllokal, S1B0Lemma: Kreuzchen_machen, S1B0LemmaPOS: Kreuzchen_VERB, S1B0POS: NOUN_VERB, S1B0POSLemma: NOUN_machen, S1B0Token: Kreuzchen_machen, S1Lemma: Kreuzchen, S1POS: NOUN, S1S0B0Lemma: Kreuzchen_Wahllokal_machen, S1S0B0LemmaPOS: Kreuzchen_NOUN_VERB, S1S0B0POS: NOUN_NOUN_VERB, S1S0B0POSLemma: NOUN_NOUN_machen, S1S0B0Token: Kreuzchen_Wahllokal_machen, S1S0Lemma: Kreuzchen_Wahllokal, S1S0LemmaPOS: Kreuzchen_NOUN, S1S0POS: NOUN_NOUN, S1S0POSLemma: NOUN_Wahllokal, S1S0Token: Kreuzchen_Wahllokal, S1Token: Kreuzchen, StackLength: 2, Wahllokal_isGouvernedBy_machen: true, Wahllokal_isGouvernedBy_machen_nmod: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 200, 

33- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Kreuzchen]   B= [machen, ,, so ,.. ]

B0Lemma: machen, B0POS: VERB, B0Token: machen, B1Lemma: ,, B1POS: PUNCT, B1Token: ,, Kreuzchen_isGouvernedBy_machen: true, Kreuzchen_isGouvernedBy_machen_conj: true, S0B0Distance: 3, S0B0Lemma: Kreuzchen_machen, S0B0LemmaPOS: Kreuzchen_VERB, S0B0POS: NOUN_VERB, S0B0POSLemma: NOUN_machen, S0B0Token: Kreuzchen_machen, S0B1Lemma: Kreuzchen_,, S0B1LemmaPOS: Kreuzchen_PUNCT, S0B1POS: NOUN_PUNCT, S0B1POSLemma: NOUN_,, S0B1Token: Kreuzchen_,, S0B2Lemma: Kreuzchen_so, S0B2LemmaPOS: Kreuzchen_ADV, S0B2POS: NOUN_ADV, S0B2POSLemma: NOUN_so, S0B2Token: Kreuzchen_so, S0Lemma: Kreuzchen, S0POS: NOUN, S0Token: Kreuzchen, StackLength: 1, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

34- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Kreuzchen, machen]   B= [,, so, bringen ,.. ]

B0Lemma: ,, B0POS: PUNCT, B0Token: ,, B1Lemma: so, B1POS: ADV, B1Token: so, S0B0Distance: 1, S0B0Lemma: machen_,, S0B0LemmaPOS: machen_PUNCT, S0B0POS: VERB_PUNCT, S0B0POSLemma: VERB_,, S0B0Token: machen_,, S0B1Lemma: machen_so, S0B1LemmaPOS: machen_ADV, S0B1POS: VERB_ADV, S0B1POSLemma: VERB_so, S0B1Token: machen_so, S0B2Lemma: machen_bringen, S0B2LemmaPOS: machen_VERB, S0B2POS: VERB_VERB, S0B2POSLemma: VERB_bringen, S0B2Token: machen_bringen, S0Lemma: machen, S0POS: VERB, S0S1Distance: 3, S0Token: machen, S1B0Lemma: Kreuzchen_,, S1B0LemmaPOS: Kreuzchen_PUNCT, S1B0POS: NOUN_PUNCT, S1B0POSLemma: NOUN_,, S1B0Token: Kreuzchen_,, S1Lemma: Kreuzchen, S1POS: NOUN, S1S0B0Lemma: Kreuzchen_machen_,, S1S0B0LemmaPOS: Kreuzchen_VERB_PUNCT, S1S0B0POS: NOUN_VERB_PUNCT, S1S0B0POSLemma: NOUN_VERB_,, S1S0B0Token: Kreuzchen_machen_,, S1S0Lemma: Kreuzchen_machen, S1S0LemmaPOS: Kreuzchen_VERB, S1S0POS: NOUN_VERB, S1S0POSLemma: NOUN_machen, S1S0Token: Kreuzchen_machen, S1Token: Kreuzchen, StackLength: 2, SyntaxicRelation: -conj, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

35- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[Kreuzchen, machen]]   B= [,, so, bringen ,.. ]

B0Lemma: ,, B0POS: PUNCT, B0Token: ,, B1Lemma: so, B1POS: ADV, B1Token: so, S0B0Distance: 1, S0B0Lemma: Kreuzchen_machen_,, S0B0LemmaPOS: Kreuzchen_machen_PUNCT, S0B0POS: NOUN_VERB_PUNCT, S0B0POSLemma: NOUN_VERB_,, S0B0Token: Kreuzchen_machen_,, S0B1Lemma: Kreuzchen_machen_so, S0B1LemmaPOS: Kreuzchen_machen_ADV, S0B1POS: NOUN_VERB_ADV, S0B1POSLemma: NOUN_VERB_so, S0B1Token: Kreuzchen_machen_so, S0B2Lemma: Kreuzchen_machen_bringen, S0B2LemmaPOS: Kreuzchen_machen_VERB, S0B2POS: NOUN_VERB_VERB, S0B2POSLemma: NOUN_VERB_bringen, S0B2Token: Kreuzchen_machen_bringen, S0Lemma: Kreuzchen_machen, S0POS: NOUN_VERB, S0Token: Kreuzchen_machen, StackLength: 1, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

36- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, so, bringen ,.. ]

B0Lemma: ,, B0POS: PUNCT, B0Token: ,, B1Lemma: so, B1POS: ADV, B1Token: so, transitionHistoryLength1: 1, transitionHistoryLength2: 10, transitionHistoryLength3: 102, 

37- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [so, bringen, diese ,.. ]

B0Lemma: so, B0POS: ADV, B0Token: so, B1Lemma: bringen, B1POS: VERB, B1Token: bringen, S0B0Distance: 1, S0B0Lemma: ,_so, S0B0LemmaPOS: ,_ADV, S0B0POS: PUNCT_ADV, S0B0POSLemma: PUNCT_so, S0B0Token: ,_so, S0B1Lemma: ,_bringen, S0B1LemmaPOS: ,_VERB, S0B1POS: PUNCT_VERB, S0B1POSLemma: PUNCT_bringen, S0B1Token: ,_bringen, S0B2Lemma: ,_dies, S0B2LemmaPOS: ,_PRON, S0B2POS: PUNCT_PRON, S0B2POSLemma: PUNCT_dies, S0B2Token: ,_diese, S0Lemma: ,, S0POS: PUNCT, S0Token: ,, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 21, transitionHistoryLength3: 210, 

38- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [so, bringen, diese ,.. ]

B0Lemma: so, B0POS: ADV, B0Token: so, B1Lemma: bringen, B1POS: VERB, B1Token: bringen, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 021, 

39- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [so]   B= [bringen, diese, eigene ,.. ]

B0Lemma: bringen, B0POS: VERB, B0Token: bringen, B1Lemma: dies, B1POS: PRON, B1Token: diese, S0B0Distance: 1, S0B0Lemma: so_bringen, S0B0LemmaPOS: so_VERB, S0B0POS: ADV_VERB, S0B0POSLemma: ADV_bringen, S0B0Token: so_bringen, S0B1Lemma: so_dies, S0B1LemmaPOS: so_PRON, S0B1POS: ADV_PRON, S0B1POSLemma: ADV_dies, S0B1Token: so_diese, S0B2Lemma: so_eigen, S0B2LemmaPOS: so_ADJ, S0B2POS: ADV_ADJ, S0B2POSLemma: ADV_eigen, S0B2Token: so_eigene, S0Lemma: so, S0POS: ADV, S0Token: so, StackLength: 1, so_isGouvernedBy_bringen: true, so_isGouvernedBy_bringen_advmod: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

40- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [bringen, diese, eigene ,.. ]

B0Lemma: bringen, B0POS: VERB, B0Token: bringen, B1Lemma: dies, B1POS: PRON, B1Token: diese, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

41- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [bringen]   B= [diese, eigene, Schablonen ,.. ]

B0Lemma: dies, B0POS: PRON, B0Token: diese, B1Lemma: eigen, B1POS: ADJ, B1Token: eigene, S0B0Distance: 1, S0B0Lemma: bringen_dies, S0B0LemmaPOS: bringen_PRON, S0B0POS: VERB_PRON, S0B0POSLemma: VERB_dies, S0B0Token: bringen_diese, S0B1Lemma: bringen_eigen, S0B1LemmaPOS: bringen_ADJ, S0B1POS: VERB_ADJ, S0B1POSLemma: VERB_eigen, S0B1Token: bringen_eigene, S0B2Lemma: bringen_Schablon, S0B2LemmaPOS: bringen_NOUN, S0B2POS: VERB_NOUN, S0B2POSLemma: VERB_Schablon, S0B2Token: bringen_Schablonen, S0Lemma: bringen, S0POS: VERB, S0Token: bringen, StackLength: 1, bringen_Schablon_hasRighDep_nmod: true, bringen_hasRighDep_compound:prt: true, bringen_hasRighDep_nmod: true, bringen_mit_hasRighDep_compound:prt: true, hasRighDep_compound:prt: true, hasRighDep_nmod: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

42- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [diese, eigene, Schablonen ,.. ]

B0Lemma: dies, B0POS: PRON, B0Token: diese, B1Lemma: eigen, B1POS: ADJ, B1Token: eigene, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

43- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [diese]   B= [eigene, Schablonen, mit ,.. ]

B0Lemma: eigen, B0POS: ADJ, B0Token: eigene, B1Lemma: Schablon, B1POS: NOUN, B1Token: Schablonen, S0B0Distance: 1, S0B0Lemma: dies_eigen, S0B0LemmaPOS: dies_ADJ, S0B0POS: PRON_ADJ, S0B0POSLemma: PRON_eigen, S0B0Token: diese_eigene, S0B1Lemma: dies_Schablon, S0B1LemmaPOS: dies_NOUN, S0B1POS: PRON_NOUN, S0B1POSLemma: PRON_Schablon, S0B1Token: diese_Schablonen, S0B2Lemma: dies_mit, S0B2LemmaPOS: dies_ADP, S0B2POS: PRON_ADP, S0B2POSLemma: PRON_mit, S0B2Token: diese_mit, S0Lemma: dies, S0POS: PRON, S0Token: diese, StackLength: 1, dies_isGouvernedBy_Schablon: true, dies_isGouvernedBy_Schablon_nsubj: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

44- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [eigene, Schablonen, mit ,.. ]

B0Lemma: eigen, B0POS: ADJ, B0Token: eigene, B1Lemma: Schablon, B1POS: NOUN, B1Token: Schablonen, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

45- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [eigene]   B= [Schablonen, mit, . ,.. ]

B0Lemma: Schablon, B0POS: NOUN, B0Token: Schablonen, B1Lemma: mit, B1POS: ADP, B1Token: mit, S0B0Distance: 1, S0B0Lemma: eigen_Schablon, S0B0LemmaPOS: eigen_NOUN, S0B0POS: ADJ_NOUN, S0B0POSLemma: ADJ_Schablon, S0B0Token: eigene_Schablonen, S0B1Lemma: eigen_mit, S0B1LemmaPOS: eigen_ADP, S0B1POS: ADJ_ADP, S0B1POSLemma: ADJ_mit, S0B1Token: eigene_mit, S0B2Lemma: eigen_., S0B2LemmaPOS: eigen_PUNCT, S0B2POS: ADJ_PUNCT, S0B2POSLemma: ADJ_., S0B2Token: eigene_., S0Lemma: eigen, S0POS: ADJ, S0Token: eigene, StackLength: 1, eigen_isGouvernedBy_Schablon: true, eigen_isGouvernedBy_Schablon_amod: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

46- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Schablonen, mit, . ,.. ]

B0Lemma: Schablon, B0POS: NOUN, B0Token: Schablonen, B1Lemma: mit, B1POS: ADP, B1Token: mit, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

47- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Schablonen]   B= [mit, . ,.. ]

B0Lemma: mit, B0POS: ADP, B0Token: mit, B1Lemma: ., B1POS: PUNCT, B1Token: ., S0B0Distance: 1, S0B0Lemma: Schablon_mit, S0B0LemmaPOS: Schablon_ADP, S0B0POS: NOUN_ADP, S0B0POSLemma: NOUN_mit, S0B0Token: Schablonen_mit, S0B1Lemma: Schablon_., S0B1LemmaPOS: Schablon_PUNCT, S0B1POS: NOUN_PUNCT, S0B1POSLemma: NOUN_., S0B1Token: Schablonen_., S0Lemma: Schablon, S0POS: NOUN, S0Token: Schablonen, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

48- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [mit, . ,.. ]

B0Lemma: mit, B0POS: ADP, B0Token: mit, B1Lemma: ., B1POS: PUNCT, B1Token: ., transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

49- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [mit]   B= [.]

B0Lemma: ., B0POS: PUNCT, B0Token: ., S0B0Distance: 1, S0B0Lemma: mit_., S0B0LemmaPOS: mit_PUNCT, S0B0POS: ADP_PUNCT, S0B0POSLemma: ADP_., S0B0Token: mit_., S0Lemma: mit, S0POS: ADP, S0Token: mit, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

50- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [.]

B0Lemma: ., B0POS: PUNCT, B0Token: ., transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

51- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [ ]

S0Lemma: ., S0POS: PUNCT, S0Token: ., StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

52- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

## Sentence No. 542 - 
Wenn die Zumbastunden im Studio stattfänden und sie nebenan im Büro sitze , dann sei immer irgendetwas von ihr in Bewegung . 
### Existing MWEs: 
1- **stattfänden** (ID)
2- **sei in Bewegung** (ID)



0- &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Wenn, die, Zumbastunden ,.. ]

B0Lemma: wenn, B0POS: SCONJ, B0Token: Wenn, B1Lemma: der, B1POS: DET, B1Token: die, 

1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Wenn]   B= [die, Zumbastunden, im ,.. ]

B0Lemma: der, B0POS: DET, B0Token: die, B1Lemma: Zumbastunde, B1POS: NOUN, B1Token: Zumbastunden, S0B0Distance: 1, S0B0Lemma: wenn_der, S0B0LemmaPOS: wenn_DET, S0B0POS: SCONJ_DET, S0B0POSLemma: SCONJ_der, S0B0Token: Wenn_die, S0B1Lemma: wenn_Zumbastunde, S0B1LemmaPOS: wenn_NOUN, S0B1POS: SCONJ_NOUN, S0B1POSLemma: SCONJ_Zumbastunde, S0B1Token: Wenn_Zumbastunden, S0B2Lemma: wenn_in+der, S0B2LemmaPOS: wenn_ADP, S0B2POS: SCONJ_ADP, S0B2POSLemma: SCONJ_in+der, S0B2Token: Wenn_im, S0Lemma: wenn, S0POS: SCONJ, S0Token: Wenn, StackLength: 1, wenn_isGouvernedBy_stattfinden: true, wenn_isGouvernedBy_stattfinden_mark: true, 

2- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [die, Zumbastunden, im ,.. ]

B0Lemma: der, B0POS: DET, B0Token: die, B1Lemma: Zumbastunde, B1POS: NOUN, B1Token: Zumbastunden, transitionHistoryLength1: 0, 

3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [die]   B= [Zumbastunden, im, Studio ,.. ]

B0Lemma: Zumbastunde, B0POS: NOUN, B0Token: Zumbastunden, B1Lemma: in+der, B1POS: ADP, B1Token: im, S0B0Distance: 1, S0B0Lemma: der_Zumbastunde, S0B0LemmaPOS: der_NOUN, S0B0POS: DET_NOUN, S0B0POSLemma: DET_Zumbastunde, S0B0Token: die_Zumbastunden, S0B1Lemma: der_in+der, S0B1LemmaPOS: der_ADP, S0B1POS: DET_ADP, S0B1POSLemma: DET_in+der, S0B1Token: die_im, S0B2Lemma: der_Studio, S0B2LemmaPOS: der_NOUN, S0B2POS: DET_NOUN, S0B2POSLemma: DET_Studio, S0B2Token: die_Studio, S0Lemma: der, S0POS: DET, S0Token: die, StackLength: 1, der_isGouvernedBy_Zumbastunde: true, der_isGouvernedBy_Zumbastunde_det: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, 

4- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Zumbastunden, im, Studio ,.. ]

B0Lemma: Zumbastunde, B0POS: NOUN, B0Token: Zumbastunden, B1Lemma: in+der, B1POS: ADP, B1Token: im, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Zumbastunden]   B= [im, Studio, stattfänden ,.. ]

B0Lemma: in+der, B0POS: ADP, B0Token: im, B1Lemma: Studio, B1POS: NOUN, B1Token: Studio, S0B0Distance: 1, S0B0Lemma: Zumbastunde_in+der, S0B0LemmaPOS: Zumbastunde_ADP, S0B0POS: NOUN_ADP, S0B0POSLemma: NOUN_in+der, S0B0Token: Zumbastunden_im, S0B1Lemma: Zumbastunde_Studio, S0B1LemmaPOS: Zumbastunde_NOUN, S0B1POS: NOUN_NOUN, S0B1POSLemma: NOUN_Studio, S0B1Token: Zumbastunden_Studio, S0B2Lemma: Zumbastunde_stattfinden, S0B2LemmaPOS: Zumbastunde_VERB, S0B2POS: NOUN_VERB, S0B2POSLemma: NOUN_stattfinden, S0B2Token: Zumbastunden_stattfänden, S0Lemma: Zumbastunde, S0POS: NOUN, S0Token: Zumbastunden, StackLength: 1, Zumbastunde_Studio_hasRighDep_nmod: true, Zumbastunde_hasRighDep_nmod: true, Zumbastunde_isGouvernedBy_stattfinden: true, Zumbastunde_isGouvernedBy_stattfinden_nmod: true, hasRighDep_nmod: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

6- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [im, Studio, stattfänden ,.. ]

B0Lemma: in+der, B0POS: ADP, B0Token: im, B1Lemma: Studio, B1POS: NOUN, B1Token: Studio, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [im]   B= [Studio, stattfänden, und ,.. ]

B0Lemma: Studio, B0POS: NOUN, B0Token: Studio, B1Lemma: stattfinden, B1POS: VERB, B1Token: stattfänden, S0B0Distance: 1, S0B0Lemma: in+der_Studio, S0B0LemmaPOS: in+der_NOUN, S0B0POS: ADP_NOUN, S0B0POSLemma: ADP_Studio, S0B0Token: im_Studio, S0B1Lemma: in+der_stattfinden, S0B1LemmaPOS: in+der_VERB, S0B1POS: ADP_VERB, S0B1POSLemma: ADP_stattfinden, S0B1Token: im_stattfänden, S0B2Lemma: in+der_und, S0B2LemmaPOS: in+der_CONJ, S0B2POS: ADP_CONJ, S0B2POSLemma: ADP_und, S0B2Token: im_und, S0Lemma: in+der, S0POS: ADP, S0Token: im, StackLength: 1, in+der_isGouvernedBy_Studio: true, in+der_isGouvernedBy_Studio_case: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

8- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Studio, stattfänden, und ,.. ]

B0Lemma: Studio, B0POS: NOUN, B0Token: Studio, B1Lemma: stattfinden, B1POS: VERB, B1Token: stattfänden, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Studio]   B= [stattfänden, und, sie ,.. ]

B0Lemma: stattfinden, B0POS: VERB, B0Token: stattfänden, B1Lemma: und, B1POS: CONJ, B1Token: und, S0B0Distance: 1, S0B0Lemma: Studio_stattfinden, S0B0LemmaPOS: Studio_VERB, S0B0POS: NOUN_VERB, S0B0POSLemma: NOUN_stattfinden, S0B0Token: Studio_stattfänden, S0B1Lemma: Studio_und, S0B1LemmaPOS: Studio_CONJ, S0B1POS: NOUN_CONJ, S0B1POSLemma: NOUN_und, S0B1Token: Studio_und, S0B2Lemma: Studio_sie, S0B2LemmaPOS: Studio_PRON, S0B2POS: NOUN_PRON, S0B2POSLemma: NOUN_sie, S0B2Token: Studio_sie, S0Lemma: Studio, S0POS: NOUN, S0Token: Studio, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

10- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [stattfänden, und, sie ,.. ]

B0Lemma: stattfinden, B0POS: VERB, B0Token: stattfänden, B1Lemma: und, B1POS: CONJ, B1Token: und, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [stattfänden]   B= [und, sie, nebenan ,.. ]

B0Lemma: und, B0POS: CONJ, B0Token: und, B1Lemma: sie, B1POS: PRON, B1Token: sie, S0B0Distance: 1, S0B0Lemma: stattfinden_und, S0B0LemmaPOS: stattfinden_CONJ, S0B0POS: VERB_CONJ, S0B0POSLemma: VERB_und, S0B0Token: stattfänden_und, S0B1Lemma: stattfinden_sie, S0B1LemmaPOS: stattfinden_PRON, S0B1POS: VERB_PRON, S0B1POSLemma: VERB_sie, S0B1Token: stattfänden_sie, S0B2Lemma: stattfinden_nebenan, S0B2LemmaPOS: stattfinden_ADV, S0B2POS: VERB_ADV, S0B2POSLemma: VERB_nebenan, S0B2Token: stattfänden_nebenan, S0Lemma: stattfinden, S0POS: VERB, S0Token: stattfänden, StackLength: 1, hasRighDep_cc: true, hasRighDep_conj: true, hasRighDep_punct: true, stattfinden_,_hasRighDep_punct: true, stattfinden_hasRighDep_cc: true, stattfinden_hasRighDep_conj: true, stattfinden_hasRighDep_punct: true, stattfinden_isGouvernedBy_irgendetwas: true, stattfinden_isGouvernedBy_irgendetwas_advcl: true, stattfinden_sitz_hasRighDep_conj: true, stattfinden_und_hasRighDep_cc: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

12- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [stattfänden, und]   B= [sie, nebenan, im ,.. ]

B0Lemma: sie, B0POS: PRON, B0Token: sie, B1Lemma: nebenan, B1POS: ADV, B1Token: nebenan, S0B0Distance: 1, S0B0Lemma: und_sie, S0B0LemmaPOS: und_PRON, S0B0POS: CONJ_PRON, S0B0POSLemma: CONJ_sie, S0B0Token: und_sie, S0B1Lemma: und_nebenan, S0B1LemmaPOS: und_ADV, S0B1POS: CONJ_ADV, S0B1POSLemma: CONJ_nebenan, S0B1Token: und_nebenan, S0B2Lemma: und_in+der, S0B2LemmaPOS: und_ADP, S0B2POS: CONJ_ADP, S0B2POSLemma: CONJ_in+der, S0B2Token: und_im, S0Lemma: und, S0POS: CONJ, S0S1Distance: 1, S0Token: und, S1B0Lemma: stattfinden_sie, S1B0LemmaPOS: stattfinden_PRON, S1B0POS: VERB_PRON, S1B0POSLemma: VERB_sie, S1B0Token: stattfänden_sie, S1Lemma: stattfinden, S1POS: VERB, S1S0B0Lemma: stattfinden_und_sie, S1S0B0LemmaPOS: stattfinden_CONJ_PRON, S1S0B0POS: VERB_CONJ_PRON, S1S0B0POSLemma: VERB_CONJ_sie, S1S0B0Token: stattfänden_und_sie, S1S0Lemma: stattfinden_und, S1S0LemmaPOS: stattfinden_CONJ, S1S0POS: VERB_CONJ, S1S0POSLemma: VERB_und, S1S0Token: stattfänden_und, S1Token: stattfänden, StackLength: 2, SyntaxicRelation: +cc, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

13- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [stattfänden]   B= [sie, nebenan, im ,.. ]

B0Lemma: sie, B0POS: PRON, B0Token: sie, B1Lemma: nebenan, B1POS: ADV, B1Token: nebenan, S0B0Distance: 2, S0B0Lemma: stattfinden_sie, S0B0LemmaPOS: stattfinden_PRON, S0B0POS: VERB_PRON, S0B0POSLemma: VERB_sie, S0B0Token: stattfänden_sie, S0B1Lemma: stattfinden_nebenan, S0B1LemmaPOS: stattfinden_ADV, S0B1POS: VERB_ADV, S0B1POSLemma: VERB_nebenan, S0B1Token: stattfänden_nebenan, S0B2Lemma: stattfinden_in+der, S0B2LemmaPOS: stattfinden_ADP, S0B2POS: VERB_ADP, S0B2POSLemma: VERB_in+der, S0B2Token: stattfänden_im, S0Lemma: stattfinden, S0POS: VERB, S0Token: stattfänden, StackLength: 1, hasRighDep_conj: true, hasRighDep_punct: true, stattfinden_,_hasRighDep_punct: true, stattfinden_hasRighDep_conj: true, stattfinden_hasRighDep_punct: true, stattfinden_isGouvernedBy_irgendetwas: true, stattfinden_isGouvernedBy_irgendetwas_advcl: true, stattfinden_sitz_hasRighDep_conj: true, transitionHistoryLength1: 0, transitionHistoryLength2: 00, transitionHistoryLength3: 002, 

14- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [stattfänden, sie]   B= [nebenan, im, Büro ,.. ]

B0Lemma: nebenan, B0POS: ADV, B0Token: nebenan, B1Lemma: in+der, B1POS: ADP, B1Token: im, S0B0Distance: 1, S0B0Lemma: sie_nebenan, S0B0LemmaPOS: sie_ADV, S0B0POS: PRON_ADV, S0B0POSLemma: PRON_nebenan, S0B0Token: sie_nebenan, S0B1Lemma: sie_in+der, S0B1LemmaPOS: sie_ADP, S0B1POS: PRON_ADP, S0B1POSLemma: PRON_in+der, S0B1Token: sie_im, S0B2Lemma: sie_Büro, S0B2LemmaPOS: sie_NOUN, S0B2POS: PRON_NOUN, S0B2POSLemma: PRON_Büro, S0B2Token: sie_Büro, S0Lemma: sie, S0POS: PRON, S0S1Distance: 2, S0Token: sie, S1B0Lemma: stattfinden_nebenan, S1B0LemmaPOS: stattfinden_ADV, S1B0POS: VERB_ADV, S1B0POSLemma: VERB_nebenan, S1B0Token: stattfänden_nebenan, S1Lemma: stattfinden, S1POS: VERB, S1S0B0Lemma: stattfinden_sie_nebenan, S1S0B0LemmaPOS: stattfinden_PRON_ADV, S1S0B0POS: VERB_PRON_ADV, S1S0B0POSLemma: VERB_PRON_nebenan, S1S0B0Token: stattfänden_sie_nebenan, S1S0Lemma: stattfinden_sie, S1S0LemmaPOS: stattfinden_PRON, S1S0POS: VERB_PRON, S1S0POSLemma: VERB_sie, S1S0Token: stattfänden_sie, S1Token: stattfänden, StackLength: 2, sie_isGouvernedBy_sitz: true, sie_isGouvernedBy_sitz_nsubj: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 200, 

15- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [stattfänden]   B= [nebenan, im, Büro ,.. ]

B0Lemma: nebenan, B0POS: ADV, B0Token: nebenan, B1Lemma: in+der, B1POS: ADP, B1Token: im, S0B0Distance: 3, S0B0Lemma: stattfinden_nebenan, S0B0LemmaPOS: stattfinden_ADV, S0B0POS: VERB_ADV, S0B0POSLemma: VERB_nebenan, S0B0Token: stattfänden_nebenan, S0B1Lemma: stattfinden_in+der, S0B1LemmaPOS: stattfinden_ADP, S0B1POS: VERB_ADP, S0B1POSLemma: VERB_in+der, S0B1Token: stattfänden_im, S0B2Lemma: stattfinden_Büro, S0B2LemmaPOS: stattfinden_NOUN, S0B2POS: VERB_NOUN, S0B2POSLemma: VERB_Büro, S0B2Token: stattfänden_Büro, S0Lemma: stattfinden, S0POS: VERB, S0Token: stattfänden, StackLength: 1, hasRighDep_conj: true, hasRighDep_punct: true, stattfinden_,_hasRighDep_punct: true, stattfinden_hasRighDep_conj: true, stattfinden_hasRighDep_punct: true, stattfinden_isGouvernedBy_irgendetwas: true, stattfinden_isGouvernedBy_irgendetwas_advcl: true, stattfinden_sitz_hasRighDep_conj: true, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

16- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [stattfänden, nebenan]   B= [im, Büro, sitze ,.. ]

B0Lemma: in+der, B0POS: ADP, B0Token: im, B1Lemma: Büro, B1POS: NOUN, B1Token: Büro, S0B0Distance: 1, S0B0Lemma: nebenan_in+der, S0B0LemmaPOS: nebenan_ADP, S0B0POS: ADV_ADP, S0B0POSLemma: ADV_in+der, S0B0Token: nebenan_im, S0B1Lemma: nebenan_Büro, S0B1LemmaPOS: nebenan_NOUN, S0B1POS: ADV_NOUN, S0B1POSLemma: ADV_Büro, S0B1Token: nebenan_Büro, S0B2Lemma: nebenan_sitz, S0B2LemmaPOS: nebenan_ADJ, S0B2POS: ADV_ADJ, S0B2POSLemma: ADV_sitz, S0B2Token: nebenan_sitze, S0Lemma: nebenan, S0POS: ADV, S0S1Distance: 3, S0Token: nebenan, S1B0Lemma: stattfinden_in+der, S1B0LemmaPOS: stattfinden_ADP, S1B0POS: VERB_ADP, S1B0POSLemma: VERB_in+der, S1B0Token: stattfänden_im, S1Lemma: stattfinden, S1POS: VERB, S1S0B0Lemma: stattfinden_nebenan_in+der, S1S0B0LemmaPOS: stattfinden_ADV_ADP, S1S0B0POS: VERB_ADV_ADP, S1S0B0POSLemma: VERB_ADV_in+der, S1S0B0Token: stattfänden_nebenan_im, S1S0Lemma: stattfinden_nebenan, S1S0LemmaPOS: stattfinden_ADV, S1S0POS: VERB_ADV, S1S0POSLemma: VERB_nebenan, S1S0Token: stattfänden_nebenan, S1Token: stattfänden, StackLength: 2, nebenan_isGouvernedBy_sitz: true, nebenan_isGouvernedBy_sitz_advmod: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

17- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [stattfänden]   B= [im, Büro, sitze ,.. ]

B0Lemma: in+der, B0POS: ADP, B0Token: im, B1Lemma: Büro, B1POS: NOUN, B1Token: Büro, S0B0Distance: 4, S0B0Lemma: stattfinden_in+der, S0B0LemmaPOS: stattfinden_ADP, S0B0POS: VERB_ADP, S0B0POSLemma: VERB_in+der, S0B0Token: stattfänden_im, S0B1Lemma: stattfinden_Büro, S0B1LemmaPOS: stattfinden_NOUN, S0B1POS: VERB_NOUN, S0B1POSLemma: VERB_Büro, S0B1Token: stattfänden_Büro, S0B2Lemma: stattfinden_sitz, S0B2LemmaPOS: stattfinden_ADJ, S0B2POS: VERB_ADJ, S0B2POSLemma: VERB_sitz, S0B2Token: stattfänden_sitze, S0Lemma: stattfinden, S0POS: VERB, S0Token: stattfänden, StackLength: 1, hasRighDep_conj: true, hasRighDep_punct: true, stattfinden_,_hasRighDep_punct: true, stattfinden_hasRighDep_conj: true, stattfinden_hasRighDep_punct: true, stattfinden_isGouvernedBy_irgendetwas: true, stattfinden_isGouvernedBy_irgendetwas_advcl: true, stattfinden_sitz_hasRighDep_conj: true, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

18- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [stattfänden, im]   B= [Büro, sitze, , ,.. ]

B0Lemma: Büro, B0POS: NOUN, B0Token: Büro, B1Lemma: sitz, B1POS: ADJ, B1Token: sitze, S0B0Distance: 1, S0B0Lemma: in+der_Büro, S0B0LemmaPOS: in+der_NOUN, S0B0POS: ADP_NOUN, S0B0POSLemma: ADP_Büro, S0B0Token: im_Büro, S0B1Lemma: in+der_sitz, S0B1LemmaPOS: in+der_ADJ, S0B1POS: ADP_ADJ, S0B1POSLemma: ADP_sitz, S0B1Token: im_sitze, S0B2Lemma: in+der_,, S0B2LemmaPOS: in+der_PUNCT, S0B2POS: ADP_PUNCT, S0B2POSLemma: ADP_,, S0B2Token: im_,, S0Lemma: in+der, S0POS: ADP, S0S1Distance: 4, S0Token: im, S1B0Lemma: stattfinden_Büro, S1B0LemmaPOS: stattfinden_NOUN, S1B0POS: VERB_NOUN, S1B0POSLemma: VERB_Büro, S1B0Token: stattfänden_Büro, S1Lemma: stattfinden, S1POS: VERB, S1S0B0Lemma: stattfinden_in+der_Büro, S1S0B0LemmaPOS: stattfinden_ADP_NOUN, S1S0B0POS: VERB_ADP_NOUN, S1S0B0POSLemma: VERB_ADP_Büro, S1S0B0Token: stattfänden_im_Büro, S1S0Lemma: stattfinden_in+der, S1S0LemmaPOS: stattfinden_ADP, S1S0POS: VERB_ADP, S1S0POSLemma: VERB_in+der, S1S0Token: stattfänden_im, S1Token: stattfänden, StackLength: 2, in+der_isGouvernedBy_Büro: true, in+der_isGouvernedBy_Büro_case: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

19- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [stattfänden]   B= [Büro, sitze, , ,.. ]

B0Lemma: Büro, B0POS: NOUN, B0Token: Büro, B1Lemma: sitz, B1POS: ADJ, B1Token: sitze, S0B0Distance: 5, S0B0Lemma: stattfinden_Büro, S0B0LemmaPOS: stattfinden_NOUN, S0B0POS: VERB_NOUN, S0B0POSLemma: VERB_Büro, S0B0Token: stattfänden_Büro, S0B1Lemma: stattfinden_sitz, S0B1LemmaPOS: stattfinden_ADJ, S0B1POS: VERB_ADJ, S0B1POSLemma: VERB_sitz, S0B1Token: stattfänden_sitze, S0B2Lemma: stattfinden_,, S0B2LemmaPOS: stattfinden_PUNCT, S0B2POS: VERB_PUNCT, S0B2POSLemma: VERB_,, S0B2Token: stattfänden_,, S0Lemma: stattfinden, S0POS: VERB, S0Token: stattfänden, StackLength: 1, hasRighDep_conj: true, hasRighDep_punct: true, stattfinden_,_hasRighDep_punct: true, stattfinden_hasRighDep_conj: true, stattfinden_hasRighDep_punct: true, stattfinden_isGouvernedBy_irgendetwas: true, stattfinden_isGouvernedBy_irgendetwas_advcl: true, stattfinden_sitz_hasRighDep_conj: true, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

20- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [stattfänden, Büro]   B= [sitze, ,, dann ,.. ]

B0Lemma: sitz, B0POS: ADJ, B0Token: sitze, B1Lemma: ,, B1POS: PUNCT, B1Token: ,, Büro_isGouvernedBy_sitz: true, Büro_isGouvernedBy_sitz_nmod: true, S0B0Distance: 1, S0B0Lemma: Büro_sitz, S0B0LemmaPOS: Büro_ADJ, S0B0POS: NOUN_ADJ, S0B0POSLemma: NOUN_sitz, S0B0Token: Büro_sitze, S0B1Lemma: Büro_,, S0B1LemmaPOS: Büro_PUNCT, S0B1POS: NOUN_PUNCT, S0B1POSLemma: NOUN_,, S0B1Token: Büro_,, S0B2Lemma: Büro_dann, S0B2LemmaPOS: Büro_ADV, S0B2POS: NOUN_ADV, S0B2POSLemma: NOUN_dann, S0B2Token: Büro_dann, S0Lemma: Büro, S0POS: NOUN, S0S1Distance: 5, S0Token: Büro, S1B0Lemma: stattfinden_sitz, S1B0LemmaPOS: stattfinden_ADJ, S1B0POS: VERB_ADJ, S1B0POSLemma: VERB_sitz, S1B0Token: stattfänden_sitze, S1Lemma: stattfinden, S1POS: VERB, S1S0B0Lemma: stattfinden_Büro_sitz, S1S0B0LemmaPOS: stattfinden_NOUN_ADJ, S1S0B0POS: VERB_NOUN_ADJ, S1S0B0POSLemma: VERB_NOUN_sitz, S1S0B0Token: stattfänden_Büro_sitze, S1S0Lemma: stattfinden_Büro, S1S0LemmaPOS: stattfinden_NOUN, S1S0POS: VERB_NOUN, S1S0POSLemma: VERB_Büro, S1S0Token: stattfänden_Büro, S1Token: stattfänden, StackLength: 2, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

21- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [stattfänden]   B= [sitze, ,, dann ,.. ]

B0Lemma: sitz, B0POS: ADJ, B0Token: sitze, B1Lemma: ,, B1POS: PUNCT, B1Token: ,, S0B0Distance: 6, S0B0Lemma: stattfinden_sitz, S0B0LemmaPOS: stattfinden_ADJ, S0B0POS: VERB_ADJ, S0B0POSLemma: VERB_sitz, S0B0Token: stattfänden_sitze, S0B1Lemma: stattfinden_,, S0B1LemmaPOS: stattfinden_PUNCT, S0B1POS: VERB_PUNCT, S0B1POSLemma: VERB_,, S0B1Token: stattfänden_,, S0B2Lemma: stattfinden_dann, S0B2LemmaPOS: stattfinden_ADV, S0B2POS: VERB_ADV, S0B2POSLemma: VERB_dann, S0B2Token: stattfänden_dann, S0Lemma: stattfinden, S0POS: VERB, S0Token: stattfänden, StackLength: 1, hasRighDep_conj: true, hasRighDep_punct: true, stattfinden_,_hasRighDep_punct: true, stattfinden_hasRighDep_conj: true, stattfinden_hasRighDep_punct: true, stattfinden_isGouvernedBy_irgendetwas: true, stattfinden_isGouvernedBy_irgendetwas_advcl: true, stattfinden_sitz_hasRighDep_conj: true, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

22- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [stattfänden, sitze]   B= [,, dann, sei ,.. ]

B0Lemma: ,, B0POS: PUNCT, B0Token: ,, B1Lemma: dann, B1POS: ADV, B1Token: dann, S0B0Distance: 1, S0B0Lemma: sitz_,, S0B0LemmaPOS: sitz_PUNCT, S0B0POS: ADJ_PUNCT, S0B0POSLemma: ADJ_,, S0B0Token: sitze_,, S0B1Lemma: sitz_dann, S0B1LemmaPOS: sitz_ADV, S0B1POS: ADJ_ADV, S0B1POSLemma: ADJ_dann, S0B1Token: sitze_dann, S0B2Lemma: sitz_sein, S0B2LemmaPOS: sitz_VERB, S0B2POS: ADJ_VERB, S0B2POSLemma: ADJ_sein, S0B2Token: sitze_sei, S0Lemma: sitz, S0POS: ADJ, S0S1Distance: 6, S0Token: sitze, S1B0Lemma: stattfinden_,, S1B0LemmaPOS: stattfinden_PUNCT, S1B0POS: VERB_PUNCT, S1B0POSLemma: VERB_,, S1B0Token: stattfänden_,, S1Lemma: stattfinden, S1POS: VERB, S1S0B0Lemma: stattfinden_sitz_,, S1S0B0LemmaPOS: stattfinden_ADJ_PUNCT, S1S0B0POS: VERB_ADJ_PUNCT, S1S0B0POSLemma: VERB_ADJ_,, S1S0B0Token: stattfänden_sitze_,, S1S0Lemma: stattfinden_sitz, S1S0LemmaPOS: stattfinden_ADJ, S1S0POS: VERB_ADJ, S1S0POSLemma: VERB_sitz, S1S0Token: stattfänden_sitze, S1Token: stattfänden, StackLength: 2, SyntaxicRelation: +conj, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

23- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [stattfänden]   B= [,, dann, sei ,.. ]

B0Lemma: ,, B0POS: PUNCT, B0Token: ,, B1Lemma: dann, B1POS: ADV, B1Token: dann, S0B0Distance: 7, S0B0Lemma: stattfinden_,, S0B0LemmaPOS: stattfinden_PUNCT, S0B0POS: VERB_PUNCT, S0B0POSLemma: VERB_,, S0B0Token: stattfänden_,, S0B1Lemma: stattfinden_dann, S0B1LemmaPOS: stattfinden_ADV, S0B1POS: VERB_ADV, S0B1POSLemma: VERB_dann, S0B1Token: stattfänden_dann, S0B2Lemma: stattfinden_sein, S0B2LemmaPOS: stattfinden_VERB, S0B2POS: VERB_VERB, S0B2POSLemma: VERB_sein, S0B2Token: stattfänden_sei, S0Lemma: stattfinden, S0POS: VERB, S0Token: stattfänden, StackLength: 1, hasRighDep_punct: true, stattfinden_,_hasRighDep_punct: true, stattfinden_hasRighDep_punct: true, stattfinden_isGouvernedBy_irgendetwas: true, stattfinden_isGouvernedBy_irgendetwas_advcl: true, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

24- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [stattfänden, ,]   B= [dann, sei, immer ,.. ]

B0Lemma: dann, B0POS: ADV, B0Token: dann, B1Lemma: sein, B1POS: VERB, B1Token: sei, S0B0Distance: 1, S0B0Lemma: ,_dann, S0B0LemmaPOS: ,_ADV, S0B0POS: PUNCT_ADV, S0B0POSLemma: PUNCT_dann, S0B0Token: ,_dann, S0B1Lemma: ,_sein, S0B1LemmaPOS: ,_VERB, S0B1POS: PUNCT_VERB, S0B1POSLemma: PUNCT_sein, S0B1Token: ,_sei, S0B2Lemma: ,_immer, S0B2LemmaPOS: ,_ADV, S0B2POS: PUNCT_ADV, S0B2POSLemma: PUNCT_immer, S0B2Token: ,_immer, S0Lemma: ,, S0POS: PUNCT, S0S1Distance: 7, S0Token: ,, S1B0Lemma: stattfinden_dann, S1B0LemmaPOS: stattfinden_ADV, S1B0POS: VERB_ADV, S1B0POSLemma: VERB_dann, S1B0Token: stattfänden_dann, S1Lemma: stattfinden, S1POS: VERB, S1S0B0Lemma: stattfinden_,_dann, S1S0B0LemmaPOS: stattfinden_PUNCT_ADV, S1S0B0POS: VERB_PUNCT_ADV, S1S0B0POSLemma: VERB_PUNCT_dann, S1S0B0Token: stattfänden_,_dann, S1S0Lemma: stattfinden_,, S1S0LemmaPOS: stattfinden_PUNCT, S1S0POS: VERB_PUNCT, S1S0POSLemma: VERB_,, S1S0Token: stattfänden_,, S1Token: stattfänden, StackLength: 2, SyntaxicRelation: +punct, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

25- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [stattfänden]   B= [dann, sei, immer ,.. ]

B0Lemma: dann, B0POS: ADV, B0Token: dann, B1Lemma: sein, B1POS: VERB, B1Token: sei, S0B0Distance: 8, S0B0Lemma: stattfinden_dann, S0B0LemmaPOS: stattfinden_ADV, S0B0POS: VERB_ADV, S0B0POSLemma: VERB_dann, S0B0Token: stattfänden_dann, S0B1Lemma: stattfinden_sein, S0B1LemmaPOS: stattfinden_VERB, S0B1POS: VERB_VERB, S0B1POSLemma: VERB_sein, S0B1Token: stattfänden_sei, S0B2Lemma: stattfinden_immer, S0B2LemmaPOS: stattfinden_ADV, S0B2POS: VERB_ADV, S0B2POSLemma: VERB_immer, S0B2Token: stattfänden_immer, S0Lemma: stattfinden, S0POS: VERB, S0Token: stattfänden, StackLength: 1, stattfinden_isGouvernedBy_irgendetwas: true, stattfinden_isGouvernedBy_irgendetwas_advcl: true, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

26- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [stattfänden, dann]   B= [sei, immer, irgendetwas ,.. ]

B0Lemma: sein, B0POS: VERB, B0Token: sei, B1Lemma: immer, B1POS: ADV, B1Token: immer, S0B0Distance: 1, S0B0Lemma: dann_sein, S0B0LemmaPOS: dann_VERB, S0B0POS: ADV_VERB, S0B0POSLemma: ADV_sein, S0B0Token: dann_sei, S0B1Lemma: dann_immer, S0B1LemmaPOS: dann_ADV, S0B1POS: ADV_ADV, S0B1POSLemma: ADV_immer, S0B1Token: dann_immer, S0B2Lemma: dann_irgendetwas, S0B2LemmaPOS: dann_PRON, S0B2POS: ADV_PRON, S0B2POSLemma: ADV_irgendetwas, S0B2Token: dann_irgendetwas, S0Lemma: dann, S0POS: ADV, S0S1Distance: 8, S0Token: dann, S1B0Lemma: stattfinden_sein, S1B0LemmaPOS: stattfinden_VERB, S1B0POS: VERB_VERB, S1B0POSLemma: VERB_sein, S1B0Token: stattfänden_sei, S1Lemma: stattfinden, S1POS: VERB, S1S0B0Lemma: stattfinden_dann_sein, S1S0B0LemmaPOS: stattfinden_ADV_VERB, S1S0B0POS: VERB_ADV_VERB, S1S0B0POSLemma: VERB_ADV_sein, S1S0B0Token: stattfänden_dann_sei, S1S0Lemma: stattfinden_dann, S1S0LemmaPOS: stattfinden_ADV, S1S0POS: VERB_ADV, S1S0POSLemma: VERB_dann, S1S0Token: stattfänden_dann, S1Token: stattfänden, StackLength: 2, dann_hasRighDep_cop: true, dann_isGouvernedBy_irgendetwas: true, dann_isGouvernedBy_irgendetwas_advmod: true, dann_sein_hasRighDep_cop: true, hasRighDep_cop: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

27- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [stattfänden]   B= [sei, immer, irgendetwas ,.. ]

B0Lemma: sein, B0POS: VERB, B0Token: sei, B1Lemma: immer, B1POS: ADV, B1Token: immer, S0B0Distance: 9, S0B0Lemma: stattfinden_sein, S0B0LemmaPOS: stattfinden_VERB, S0B0POS: VERB_VERB, S0B0POSLemma: VERB_sein, S0B0Token: stattfänden_sei, S0B1Lemma: stattfinden_immer, S0B1LemmaPOS: stattfinden_ADV, S0B1POS: VERB_ADV, S0B1POSLemma: VERB_immer, S0B1Token: stattfänden_immer, S0B2Lemma: stattfinden_irgendetwas, S0B2LemmaPOS: stattfinden_PRON, S0B2POS: VERB_PRON, S0B2POSLemma: VERB_irgendetwas, S0B2Token: stattfänden_irgendetwas, S0Lemma: stattfinden, S0POS: VERB, S0Token: stattfänden, StackLength: 1, stattfinden_isGouvernedBy_irgendetwas: true, stattfinden_isGouvernedBy_irgendetwas_advcl: true, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

28- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [stattfänden, sei]   B= [immer, irgendetwas, von ,.. ]

B0Lemma: immer, B0POS: ADV, B0Token: immer, B1Lemma: irgendetwas, B1POS: PRON, B1Token: irgendetwas, S0B0Distance: 1, S0B0Lemma: sein_immer, S0B0LemmaPOS: sein_ADV, S0B0POS: VERB_ADV, S0B0POSLemma: VERB_immer, S0B0Token: sei_immer, S0B1Lemma: sein_irgendetwas, S0B1LemmaPOS: sein_PRON, S0B1POS: VERB_PRON, S0B1POSLemma: VERB_irgendetwas, S0B1Token: sei_irgendetwas, S0B2Lemma: sein_von, S0B2LemmaPOS: sein_ADP, S0B2POS: VERB_ADP, S0B2POSLemma: VERB_von, S0B2Token: sei_von, S0Lemma: sein, S0POS: VERB, S0S1Distance: 9, S0Token: sei, S1B0Lemma: stattfinden_immer, S1B0LemmaPOS: stattfinden_ADV, S1B0POS: VERB_ADV, S1B0POSLemma: VERB_immer, S1B0Token: stattfänden_immer, S1Lemma: stattfinden, S1POS: VERB, S1S0B0Lemma: stattfinden_sein_immer, S1S0B0LemmaPOS: stattfinden_VERB_ADV, S1S0B0POS: VERB_VERB_ADV, S1S0B0POSLemma: VERB_VERB_immer, S1S0B0Token: stattfänden_sei_immer, S1S0Lemma: stattfinden_sein, S1S0LemmaPOS: stattfinden_VERB, S1S0POS: VERB_VERB, S1S0POSLemma: VERB_sein, S1S0Token: stattfänden_sei, S1Token: stattfänden, StackLength: 2, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

29- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [stattfänden, sei, immer]   B= [irgendetwas, von, ihr ,.. ]

B0Lemma: irgendetwas, B0POS: PRON, B0Token: irgendetwas, B1Lemma: von, B1POS: ADP, B1Token: von, S0B0Distance: 1, S0B0Lemma: immer_irgendetwas, S0B0LemmaPOS: immer_PRON, S0B0POS: ADV_PRON, S0B0POSLemma: ADV_irgendetwas, S0B0Token: immer_irgendetwas, S0B1Lemma: immer_von, S0B1LemmaPOS: immer_ADP, S0B1POS: ADV_ADP, S0B1POSLemma: ADV_von, S0B1Token: immer_von, S0B2Lemma: immer_ihr, S0B2LemmaPOS: immer_PRON, S0B2POS: ADV_PRON, S0B2POSLemma: ADV_ihr, S0B2Token: immer_ihr, S0Lemma: immer, S0POS: ADV, S0S1Distance: 1, S0Token: immer, S1B0Lemma: sein_irgendetwas, S1B0LemmaPOS: sein_PRON, S1B0POS: VERB_PRON, S1B0POSLemma: VERB_irgendetwas, S1B0Token: sei_irgendetwas, S1Lemma: sein, S1POS: VERB, S1S0B0Lemma: sein_immer_irgendetwas, S1S0B0LemmaPOS: sein_ADV_PRON, S1S0B0POS: VERB_ADV_PRON, S1S0B0POSLemma: VERB_ADV_irgendetwas, S1S0B0Token: sei_immer_irgendetwas, S1S0Lemma: sein_immer, S1S0LemmaPOS: sein_ADV, S1S0POS: VERB_ADV, S1S0POSLemma: VERB_immer, S1S0Token: sei_immer, S1Token: sei, StackLength: 3, immer_isGouvernedBy_irgendetwas: true, immer_isGouvernedBy_irgendetwas_advmod: true, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

30- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [stattfänden, sei]   B= [irgendetwas, von, ihr ,.. ]

B0Lemma: irgendetwas, B0POS: PRON, B0Token: irgendetwas, B1Lemma: von, B1POS: ADP, B1Token: von, S0B0Distance: 2, S0B0Lemma: sein_irgendetwas, S0B0LemmaPOS: sein_PRON, S0B0POS: VERB_PRON, S0B0POSLemma: VERB_irgendetwas, S0B0Token: sei_irgendetwas, S0B1Lemma: sein_von, S0B1LemmaPOS: sein_ADP, S0B1POS: VERB_ADP, S0B1POSLemma: VERB_von, S0B1Token: sei_von, S0B2Lemma: sein_ihr, S0B2LemmaPOS: sein_PRON, S0B2POS: VERB_PRON, S0B2POSLemma: VERB_ihr, S0B2Token: sei_ihr, S0Lemma: sein, S0POS: VERB, S0S1Distance: 9, S0Token: sei, S1B0Lemma: stattfinden_irgendetwas, S1B0LemmaPOS: stattfinden_PRON, S1B0POS: VERB_PRON, S1B0POSLemma: VERB_irgendetwas, S1B0Token: stattfänden_irgendetwas, S1Lemma: stattfinden, S1POS: VERB, S1S0B0Lemma: stattfinden_sein_irgendetwas, S1S0B0LemmaPOS: stattfinden_VERB_PRON, S1S0B0POS: VERB_VERB_PRON, S1S0B0POSLemma: VERB_VERB_irgendetwas, S1S0B0Token: stattfänden_sei_irgendetwas, S1S0Lemma: stattfinden_sein, S1S0LemmaPOS: stattfinden_VERB, S1S0POS: VERB_VERB, S1S0POSLemma: VERB_sein, S1S0Token: stattfänden_sei, S1Token: stattfänden, StackLength: 2, transitionHistoryLength1: 0, transitionHistoryLength2: 00, transitionHistoryLength3: 002, 

31- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [stattfänden, sei, irgendetwas]   B= [von, ihr, in ,.. ]

B0Lemma: von, B0POS: ADP, B0Token: von, B1Lemma: ihr, B1POS: PRON, B1Token: ihr, S0B0Distance: 1, S0B0Lemma: irgendetwas_von, S0B0LemmaPOS: irgendetwas_ADP, S0B0POS: PRON_ADP, S0B0POSLemma: PRON_von, S0B0Token: irgendetwas_von, S0B1Lemma: irgendetwas_ihr, S0B1LemmaPOS: irgendetwas_PRON, S0B1POS: PRON_PRON, S0B1POSLemma: PRON_ihr, S0B1Token: irgendetwas_ihr, S0B2Lemma: irgendetwas_in, S0B2LemmaPOS: irgendetwas_ADP, S0B2POS: PRON_ADP, S0B2POSLemma: PRON_in, S0B2Token: irgendetwas_in, S0Lemma: irgendetwas, S0POS: PRON, S0S1Distance: 2, S0Token: irgendetwas, S1B0Lemma: sein_von, S1B0LemmaPOS: sein_ADP, S1B0POS: VERB_ADP, S1B0POSLemma: VERB_von, S1B0Token: sei_von, S1Lemma: sein, S1POS: VERB, S1S0B0Lemma: sein_irgendetwas_von, S1S0B0LemmaPOS: sein_PRON_ADP, S1S0B0POS: VERB_PRON_ADP, S1S0B0POSLemma: VERB_PRON_von, S1S0B0Token: sei_irgendetwas_von, S1S0Lemma: sein_irgendetwas, S1S0LemmaPOS: sein_PRON, S1S0POS: VERB_PRON, S1S0POSLemma: VERB_irgendetwas, S1S0Token: sei_irgendetwas, S1Token: sei, StackLength: 3, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 200, 

32- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [stattfänden, sei]   B= [von, ihr, in ,.. ]

B0Lemma: von, B0POS: ADP, B0Token: von, B1Lemma: ihr, B1POS: PRON, B1Token: ihr, S0B0Distance: 3, S0B0Lemma: sein_von, S0B0LemmaPOS: sein_ADP, S0B0POS: VERB_ADP, S0B0POSLemma: VERB_von, S0B0Token: sei_von, S0B1Lemma: sein_ihr, S0B1LemmaPOS: sein_PRON, S0B1POS: VERB_PRON, S0B1POSLemma: VERB_ihr, S0B1Token: sei_ihr, S0B2Lemma: sein_in, S0B2LemmaPOS: sein_ADP, S0B2POS: VERB_ADP, S0B2POSLemma: VERB_in, S0B2Token: sei_in, S0Lemma: sein, S0POS: VERB, S0S1Distance: 9, S0Token: sei, S1B0Lemma: stattfinden_von, S1B0LemmaPOS: stattfinden_ADP, S1B0POS: VERB_ADP, S1B0POSLemma: VERB_von, S1B0Token: stattfänden_von, S1Lemma: stattfinden, S1POS: VERB, S1S0B0Lemma: stattfinden_sein_von, S1S0B0LemmaPOS: stattfinden_VERB_ADP, S1S0B0POS: VERB_VERB_ADP, S1S0B0POSLemma: VERB_VERB_von, S1S0B0Token: stattfänden_sei_von, S1S0Lemma: stattfinden_sein, S1S0LemmaPOS: stattfinden_VERB, S1S0POS: VERB_VERB, S1S0POSLemma: VERB_sein, S1S0Token: stattfänden_sei, S1Token: stattfänden, StackLength: 2, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

33- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [stattfänden, sei, von]   B= [ihr, in, Bewegung ,.. ]

B0Lemma: ihr, B0POS: PRON, B0Token: ihr, B1Lemma: in, B1POS: ADP, B1Token: in, S0B0Distance: 1, S0B0Lemma: von_ihr, S0B0LemmaPOS: von_PRON, S0B0POS: ADP_PRON, S0B0POSLemma: ADP_ihr, S0B0Token: von_ihr, S0B1Lemma: von_in, S0B1LemmaPOS: von_ADP, S0B1POS: ADP_ADP, S0B1POSLemma: ADP_in, S0B1Token: von_in, S0B2Lemma: von_Bewegung, S0B2LemmaPOS: von_NOUN, S0B2POS: ADP_NOUN, S0B2POSLemma: ADP_Bewegung, S0B2Token: von_Bewegung, S0Lemma: von, S0POS: ADP, S0S1Distance: 3, S0Token: von, S1B0Lemma: sein_ihr, S1B0LemmaPOS: sein_PRON, S1B0POS: VERB_PRON, S1B0POSLemma: VERB_ihr, S1B0Token: sei_ihr, S1Lemma: sein, S1POS: VERB, S1S0B0Lemma: sein_von_ihr, S1S0B0LemmaPOS: sein_ADP_PRON, S1S0B0POS: VERB_ADP_PRON, S1S0B0POSLemma: VERB_ADP_ihr, S1S0B0Token: sei_von_ihr, S1S0Lemma: sein_von, S1S0LemmaPOS: sein_ADP, S1S0POS: VERB_ADP, S1S0POSLemma: VERB_von, S1S0Token: sei_von, S1Token: sei, StackLength: 3, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, von_isGouvernedBy_ihr: true, von_isGouvernedBy_ihr_case: true, 

34- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [stattfänden, sei]   B= [ihr, in, Bewegung ,.. ]

B0Lemma: ihr, B0POS: PRON, B0Token: ihr, B1Lemma: in, B1POS: ADP, B1Token: in, S0B0Distance: 4, S0B0Lemma: sein_ihr, S0B0LemmaPOS: sein_PRON, S0B0POS: VERB_PRON, S0B0POSLemma: VERB_ihr, S0B0Token: sei_ihr, S0B1Lemma: sein_in, S0B1LemmaPOS: sein_ADP, S0B1POS: VERB_ADP, S0B1POSLemma: VERB_in, S0B1Token: sei_in, S0B2Lemma: sein_Bewegung, S0B2LemmaPOS: sein_NOUN, S0B2POS: VERB_NOUN, S0B2POSLemma: VERB_Bewegung, S0B2Token: sei_Bewegung, S0Lemma: sein, S0POS: VERB, S0S1Distance: 9, S0Token: sei, S1B0Lemma: stattfinden_ihr, S1B0LemmaPOS: stattfinden_PRON, S1B0POS: VERB_PRON, S1B0POSLemma: VERB_ihr, S1B0Token: stattfänden_ihr, S1Lemma: stattfinden, S1POS: VERB, S1S0B0Lemma: stattfinden_sein_ihr, S1S0B0LemmaPOS: stattfinden_VERB_PRON, S1S0B0POS: VERB_VERB_PRON, S1S0B0POSLemma: VERB_VERB_ihr, S1S0B0Token: stattfänden_sei_ihr, S1S0Lemma: stattfinden_sein, S1S0LemmaPOS: stattfinden_VERB, S1S0POS: VERB_VERB, S1S0POSLemma: VERB_sein, S1S0Token: stattfänden_sei, S1Token: stattfänden, StackLength: 2, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

35- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [stattfänden, sei, ihr]   B= [in, Bewegung, . ,.. ]

B0Lemma: in, B0POS: ADP, B0Token: in, B1Lemma: Bewegung, B1POS: NOUN, B1Token: Bewegung, S0B0Distance: 1, S0B0Lemma: ihr_in, S0B0LemmaPOS: ihr_ADP, S0B0POS: PRON_ADP, S0B0POSLemma: PRON_in, S0B0Token: ihr_in, S0B1Lemma: ihr_Bewegung, S0B1LemmaPOS: ihr_NOUN, S0B1POS: PRON_NOUN, S0B1POSLemma: PRON_Bewegung, S0B1Token: ihr_Bewegung, S0B2Lemma: ihr_., S0B2LemmaPOS: ihr_PUNCT, S0B2POS: PRON_PUNCT, S0B2POSLemma: PRON_., S0B2Token: ihr_., S0Lemma: ihr, S0POS: PRON, S0S1Distance: 4, S0Token: ihr, S1B0Lemma: sein_in, S1B0LemmaPOS: sein_ADP, S1B0POS: VERB_ADP, S1B0POSLemma: VERB_in, S1B0Token: sei_in, S1Lemma: sein, S1POS: VERB, S1S0B0Lemma: sein_ihr_in, S1S0B0LemmaPOS: sein_PRON_ADP, S1S0B0POS: VERB_PRON_ADP, S1S0B0POSLemma: VERB_PRON_in, S1S0B0Token: sei_ihr_in, S1S0Lemma: sein_ihr, S1S0LemmaPOS: sein_PRON, S1S0POS: VERB_PRON, S1S0POSLemma: VERB_ihr, S1S0Token: sei_ihr, S1Token: sei, StackLength: 3, ihr_isGouvernedBy_Bewegung: true, ihr_isGouvernedBy_Bewegung_nmod: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

36- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [stattfänden, sei]   B= [in, Bewegung, . ,.. ]

B0Lemma: in, B0POS: ADP, B0Token: in, B1Lemma: Bewegung, B1POS: NOUN, B1Token: Bewegung, S0B0Distance: 5, S0B0Lemma: sein_in, S0B0LemmaPOS: sein_ADP, S0B0POS: VERB_ADP, S0B0POSLemma: VERB_in, S0B0Token: sei_in, S0B1Lemma: sein_Bewegung, S0B1LemmaPOS: sein_NOUN, S0B1POS: VERB_NOUN, S0B1POSLemma: VERB_Bewegung, S0B1Token: sei_Bewegung, S0B2Lemma: sein_., S0B2LemmaPOS: sein_PUNCT, S0B2POS: VERB_PUNCT, S0B2POSLemma: VERB_., S0B2Token: sei_., S0Lemma: sein, S0POS: VERB, S0S1Distance: 9, S0Token: sei, S1B0Lemma: stattfinden_in, S1B0LemmaPOS: stattfinden_ADP, S1B0POS: VERB_ADP, S1B0POSLemma: VERB_in, S1B0Token: stattfänden_in, S1Lemma: stattfinden, S1POS: VERB, S1S0B0Lemma: stattfinden_sein_in, S1S0B0LemmaPOS: stattfinden_VERB_ADP, S1S0B0POS: VERB_VERB_ADP, S1S0B0POSLemma: VERB_VERB_in, S1S0B0Token: stattfänden_sei_in, S1S0Lemma: stattfinden_sein, S1S0LemmaPOS: stattfinden_VERB, S1S0POS: VERB_VERB, S1S0POSLemma: VERB_sein, S1S0Token: stattfänden_sei, S1Token: stattfänden, StackLength: 2, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

37- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [stattfänden, sei, in]   B= [Bewegung, . ,.. ]

B0Lemma: Bewegung, B0POS: NOUN, B0Token: Bewegung, B1Lemma: ., B1POS: PUNCT, B1Token: ., S0B0Distance: 1, S0B0Lemma: in_Bewegung, S0B0LemmaPOS: in_NOUN, S0B0POS: ADP_NOUN, S0B0POSLemma: ADP_Bewegung, S0B0Token: in_Bewegung, S0B1Lemma: in_., S0B1LemmaPOS: in_PUNCT, S0B1POS: ADP_PUNCT, S0B1POSLemma: ADP_., S0B1Token: in_., S0Lemma: in, S0POS: ADP, S0S1Distance: 5, S0Token: in, S1B0Lemma: sein_Bewegung, S1B0LemmaPOS: sein_NOUN, S1B0POS: VERB_NOUN, S1B0POSLemma: VERB_Bewegung, S1B0Token: sei_Bewegung, S1Lemma: sein, S1POS: VERB, S1S0B0Lemma: sein_in_Bewegung, S1S0B0LemmaPOS: sein_ADP_NOUN, S1S0B0POS: VERB_ADP_NOUN, S1S0B0POSLemma: VERB_ADP_Bewegung, S1S0B0Token: sei_in_Bewegung, S1S0Lemma: sein_in, S1S0LemmaPOS: sein_ADP, S1S0POS: VERB_ADP, S1S0POSLemma: VERB_in, S1S0Token: sei_in, S1Token: sei, StackLength: 3, in_isGouvernedBy_Bewegung: true, in_isGouvernedBy_Bewegung_case: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

38- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [stattfänden, sei, in, Bewegung]   B= [.]

B0Lemma: ., B0POS: PUNCT, B0Token: ., S0B0Distance: 1, S0B0Lemma: Bewegung_., S0B0LemmaPOS: Bewegung_PUNCT, S0B0POS: NOUN_PUNCT, S0B0POSLemma: NOUN_., S0B0Token: Bewegung_., S0Lemma: Bewegung, S0POS: NOUN, S0S1Distance: 1, S0Token: Bewegung, S1B0Lemma: in_., S1B0LemmaPOS: in_PUNCT, S1B0POS: ADP_PUNCT, S1B0POSLemma: ADP_., S1B0Token: in_., S1Lemma: in, S1POS: ADP, S1S0B0Lemma: in_Bewegung_., S1S0B0LemmaPOS: in_NOUN_PUNCT, S1S0B0POS: ADP_NOUN_PUNCT, S1S0B0POSLemma: ADP_NOUN_., S1S0B0Token: in_Bewegung_., S1S0Lemma: in_Bewegung, S1S0LemmaPOS: in_NOUN, S1S0POS: ADP_NOUN, S1S0POSLemma: ADP_Bewegung, S1S0Token: in_Bewegung, S1Token: in, StackLength: 4, SyntaxicRelation: -case, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

39- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [stattfänden, sei, in, Bewegung, .]   B= [ ]

S0Lemma: ., S0POS: PUNCT, S0S1Distance: 1, S0Token: ., S1Lemma: Bewegung, S1POS: NOUN, S1S0Lemma: Bewegung_., S1S0LemmaPOS: Bewegung_PUNCT, S1S0POS: NOUN_PUNCT, S1S0POSLemma: NOUN_., S1S0Token: Bewegung_., S1Token: Bewegung, StackLength: 5, transitionHistoryLength1: 0, transitionHistoryLength2: 00, transitionHistoryLength3: 002, 

40- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [stattfänden, sei, in, Bewegung]   B= [ ]

S0Lemma: Bewegung, S0POS: NOUN, S0S1Distance: 1, S0Token: Bewegung, S1Lemma: in, S1POS: ADP, S1S0Lemma: in_Bewegung, S1S0LemmaPOS: in_NOUN, S1S0POS: ADP_NOUN, S1S0POSLemma: ADP_Bewegung, S1S0Token: in_Bewegung, S1Token: in, StackLength: 4, SyntaxicRelation: -case, transitionHistoryLength1: 0, transitionHistoryLength2: 00, transitionHistoryLength3: 000, 

41- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [stattfänden, sei, in]   B= [ ]

S0Lemma: in, S0POS: ADP, S0S1Distance: 5, S0Token: in, S1Lemma: sein, S1POS: VERB, S1S0Lemma: sein_in, S1S0LemmaPOS: sein_ADP, S1S0POS: VERB_ADP, S1S0POSLemma: VERB_in, S1S0Token: sei_in, S1Token: sei, StackLength: 3, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 200, 

42- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [stattfänden, sei]   B= [ ]

S0Lemma: sein, S0POS: VERB, S0S1Distance: 9, S0Token: sei, S1Lemma: stattfinden, S1POS: VERB, S1S0Lemma: stattfinden_sein, S1S0LemmaPOS: stattfinden_VERB, S1S0POS: VERB_VERB, S1S0POSLemma: VERB_sein, S1S0Token: stattfänden_sei, S1Token: stattfänden, StackLength: 2, transitionHistoryLength1: 2, transitionHistoryLength2: 22, transitionHistoryLength3: 220, 

43- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [stattfänden]   B= [ ]

S0Lemma: stattfinden, S0POS: VERB, S0Token: stattfänden, StackLength: 1, transitionHistoryLength1: 2, transitionHistoryLength2: 22, transitionHistoryLength3: 222, 

44- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

