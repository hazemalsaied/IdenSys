## Sentence No. 67 - 
Parkeringsplatserna ska vara trygga , av god kvalitet , ha väderskydd och det ska finnas möjligheter att låsa in eller fast cykeln . 
### Existing MWEs: 
1- **finnas möjligheter** (LVC)
2- **låsa in** (VPC)
3- **låsa fast** (VPC), Interleaving 



0- &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Parkeringsplatserna, ska, vara ,.. ]

B0Lemma: Parkeringsplats, B0POS: NOUN, B0Token: Parkeringsplatserna, B1Lemma: skola, B1POS: AUX, B1Token: ska, 

1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Parkeringsplatserna]   B= [ska, vara, trygga ,.. ]

B0Lemma: skola, B0POS: AUX, B0Token: ska, B1Lemma: vara, B1POS: AUX, B1Token: vara, Parkeringsplats_isGouvernedBy_trygg: true, Parkeringsplats_isGouvernedBy_trygg_nsubj: true, S0B0Distance: 1, S0B0Lemma: Parkeringsplats_skola, S0B0LemmaPOS: Parkeringsplats_AUX, S0B0POS: NOUN_AUX, S0B0POSLemma: NOUN_skola, S0B0Token: Parkeringsplatserna_ska, S0B1Lemma: Parkeringsplats_vara, S0B1LemmaPOS: Parkeringsplats_AUX, S0B1POS: NOUN_AUX, S0B1POSLemma: NOUN_vara, S0B1Token: Parkeringsplatserna_vara, S0Lemma: Parkeringsplats, S0POS: NOUN, S0Token: Parkeringsplatserna, 

2- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ska, vara, trygga ,.. ]

B0Lemma: skola, B0POS: AUX, B0Token: ska, B1Lemma: vara, B1POS: AUX, B1Token: vara, transitionHistoryLength1: 0, 

3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ska]   B= [vara, trygga, , ,.. ]

B0Lemma: vara, B0POS: AUX, B0Token: vara, B1Lemma: trygg, B1POS: VERB, B1Token: trygga, S0B0Distance: 1, S0B0Lemma: skola_vara, S0B0LemmaPOS: skola_AUX, S0B0POS: AUX_AUX, S0B0POSLemma: AUX_vara, S0B0Token: ska_vara, S0B1Lemma: skola_trygg, S0B1LemmaPOS: skola_VERB, S0B1POS: AUX_VERB, S0B1POSLemma: AUX_trygg, S0B1Token: ska_trygga, S0Lemma: skola, S0POS: AUX, S0Token: ska, skola_isGouvernedBy_trygg: true, skola_isGouvernedBy_trygg_aux: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, 

4- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [vara, trygga, , ,.. ]

B0Lemma: vara, B0POS: AUX, B0Token: vara, B1Lemma: trygg, B1POS: VERB, B1Token: trygga, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [vara]   B= [trygga, ,, av ,.. ]

B0Lemma: trygg, B0POS: VERB, B0Token: trygga, B1Lemma: ,, B1POS: PUNCT, B1Token: ,, S0B0Distance: 1, S0B0Lemma: vara_trygg, S0B0LemmaPOS: vara_VERB, S0B0POS: AUX_VERB, S0B0POSLemma: AUX_trygg, S0B0Token: vara_trygga, S0B1Lemma: vara_,, S0B1LemmaPOS: vara_PUNCT, S0B1POS: AUX_PUNCT, S0B1POSLemma: AUX_,, S0B1Token: vara_,, S0Lemma: vara, S0POS: AUX, S0Token: vara, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, vara_isGouvernedBy_trygg: true, vara_isGouvernedBy_trygg_aux: true, 

6- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [trygga, ,, av ,.. ]

B0Lemma: trygg, B0POS: VERB, B0Token: trygga, B1Lemma: ,, B1POS: PUNCT, B1Token: ,, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [trygga]   B= [,, av, god ,.. ]

B0Lemma: ,, B0POS: PUNCT, B0Token: ,, B1Lemma: av, B1POS: ADP, B1Token: av, S0B0Distance: 1, S0B0Lemma: trygg_,, S0B0LemmaPOS: trygg_PUNCT, S0B0POS: VERB_PUNCT, S0B0POSLemma: VERB_,, S0B0Token: trygga_,, S0B1Lemma: trygg_av, S0B1LemmaPOS: trygg_ADP, S0B1POS: VERB_ADP, S0B1POSLemma: VERB_av, S0B1Token: trygga_av, S0Lemma: trygg, S0POS: VERB, S0Token: trygga, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

8- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, av, god ,.. ]

B0Lemma: ,, B0POS: PUNCT, B0Token: ,, B1Lemma: av, B1POS: ADP, B1Token: av, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [av, god, kvalitet ,.. ]

B0Lemma: av, B0POS: ADP, B0Token: av, B1Lemma: god, B1POS: ADJ, B1Token: god, S0B0Distance: 1, S0B0Lemma: ,_av, S0B0LemmaPOS: ,_ADP, S0B0POS: PUNCT_ADP, S0B0POSLemma: PUNCT_av, S0B0Token: ,_av, S0B1Lemma: ,_god, S0B1LemmaPOS: ,_ADJ, S0B1POS: PUNCT_ADJ, S0B1POSLemma: PUNCT_god, S0B1Token: ,_god, S0Lemma: ,, S0POS: PUNCT, S0Token: ,, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

10- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [av, god, kvalitet ,.. ]

B0Lemma: av, B0POS: ADP, B0Token: av, B1Lemma: god, B1POS: ADJ, B1Token: god, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [av]   B= [god, kvalitet, , ,.. ]

B0Lemma: god, B0POS: ADJ, B0Token: god, B1Lemma: kvalitet, B1POS: NOUN, B1Token: kvalitet, S0B0Distance: 1, S0B0Lemma: av_god, S0B0LemmaPOS: av_ADJ, S0B0POS: ADP_ADJ, S0B0POSLemma: ADP_god, S0B0Token: av_god, S0B1Lemma: av_kvalitet, S0B1LemmaPOS: av_NOUN, S0B1POS: ADP_NOUN, S0B1POSLemma: ADP_kvalitet, S0B1Token: av_kvalitet, S0Lemma: av, S0POS: ADP, S0Token: av, av_isGouvernedBy_kvalitet: true, av_isGouvernedBy_kvalitet_case: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

12- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [god, kvalitet, , ,.. ]

B0Lemma: god, B0POS: ADJ, B0Token: god, B1Lemma: kvalitet, B1POS: NOUN, B1Token: kvalitet, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [god]   B= [kvalitet, ,, ha ,.. ]

B0Lemma: kvalitet, B0POS: NOUN, B0Token: kvalitet, B1Lemma: ,, B1POS: PUNCT, B1Token: ,, S0B0Distance: 1, S0B0Lemma: god_kvalitet, S0B0LemmaPOS: god_NOUN, S0B0POS: ADJ_NOUN, S0B0POSLemma: ADJ_kvalitet, S0B0Token: god_kvalitet, S0B1Lemma: god_,, S0B1LemmaPOS: god_PUNCT, S0B1POS: ADJ_PUNCT, S0B1POSLemma: ADJ_,, S0B1Token: god_,, S0Lemma: god, S0POS: ADJ, S0Token: god, god_isGouvernedBy_kvalitet: true, god_isGouvernedBy_kvalitet_amod: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

14- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [kvalitet, ,, ha ,.. ]

B0Lemma: kvalitet, B0POS: NOUN, B0Token: kvalitet, B1Lemma: ,, B1POS: PUNCT, B1Token: ,, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [kvalitet]   B= [,, ha, väderskydd ,.. ]

B0Lemma: ,, B0POS: PUNCT, B0Token: ,, B1Lemma: ha, B1POS: VERB, B1Token: ha, S0B0Distance: 1, S0B0Lemma: kvalitet_,, S0B0LemmaPOS: kvalitet_PUNCT, S0B0POS: NOUN_PUNCT, S0B0POSLemma: NOUN_,, S0B0Token: kvalitet_,, S0B1Lemma: kvalitet_ha, S0B1LemmaPOS: kvalitet_VERB, S0B1POS: NOUN_VERB, S0B1POSLemma: NOUN_ha, S0B1Token: kvalitet_ha, S0Lemma: kvalitet, S0POS: NOUN, S0Token: kvalitet, hasRighDep_punct: true, kvalitet_,_hasRighDep_punct: true, kvalitet_hasRighDep_punct: true, kvalitet_isGouvernedBy_ha: true, kvalitet_isGouvernedBy_ha_nmod: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

16- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, ha, väderskydd ,.. ]

B0Lemma: ,, B0POS: PUNCT, B0Token: ,, B1Lemma: ha, B1POS: VERB, B1Token: ha, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [ha, väderskydd, och ,.. ]

B0Lemma: ha, B0POS: VERB, B0Token: ha, B1Lemma: väderskydd, B1POS: NOUN, B1Token: väderskydd, S0B0Distance: 1, S0B0Lemma: ,_ha, S0B0LemmaPOS: ,_VERB, S0B0POS: PUNCT_VERB, S0B0POSLemma: PUNCT_ha, S0B0Token: ,_ha, S0B1Lemma: ,_väderskydd, S0B1LemmaPOS: ,_NOUN, S0B1POS: PUNCT_NOUN, S0B1POSLemma: PUNCT_väderskydd, S0B1Token: ,_väderskydd, S0Lemma: ,, S0POS: PUNCT, S0Token: ,, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

18- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ha, väderskydd, och ,.. ]

B0Lemma: ha, B0POS: VERB, B0Token: ha, B1Lemma: väderskydd, B1POS: NOUN, B1Token: väderskydd, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ha]   B= [väderskydd, och, det ,.. ]

B0Lemma: väderskydd, B0POS: NOUN, B0Token: väderskydd, B1Lemma: och, B1POS: CONJ, B1Token: och, S0B0Distance: 1, S0B0Lemma: ha_väderskydd, S0B0LemmaPOS: ha_NOUN, S0B0POS: VERB_NOUN, S0B0POSLemma: VERB_väderskydd, S0B0Token: ha_väderskydd, S0B1Lemma: ha_och, S0B1LemmaPOS: ha_CONJ, S0B1POS: VERB_CONJ, S0B1POSLemma: VERB_och, S0B1Token: ha_och, S0Lemma: ha, S0POS: VERB, S0Token: ha, ha_hasRighDep_dobj: true, ha_väderskydd_hasRighDep_dobj: true, hasRighDep_dobj: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

20- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [väderskydd, och, det ,.. ]

B0Lemma: väderskydd, B0POS: NOUN, B0Token: väderskydd, B1Lemma: och, B1POS: CONJ, B1Token: och, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [väderskydd]   B= [och, det, ska ,.. ]

B0Lemma: och, B0POS: CONJ, B0Token: och, B1Lemma: den, B1POS: PRON, B1Token: det, S0B0Distance: 1, S0B0Lemma: väderskydd_och, S0B0LemmaPOS: väderskydd_CONJ, S0B0POS: NOUN_CONJ, S0B0POSLemma: NOUN_och, S0B0Token: väderskydd_och, S0B1Lemma: väderskydd_den, S0B1LemmaPOS: väderskydd_PRON, S0B1POS: NOUN_PRON, S0B1POSLemma: NOUN_den, S0B1Token: väderskydd_det, S0Lemma: väderskydd, S0POS: NOUN, S0Token: väderskydd, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

22- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [och, det, ska ,.. ]

B0Lemma: och, B0POS: CONJ, B0Token: och, B1Lemma: den, B1POS: PRON, B1Token: det, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

23- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [och]   B= [det, ska, finnas ,.. ]

B0Lemma: den, B0POS: PRON, B0Token: det, B1Lemma: skola, B1POS: AUX, B1Token: ska, S0B0Distance: 1, S0B0Lemma: och_den, S0B0LemmaPOS: och_PRON, S0B0POS: CONJ_PRON, S0B0POSLemma: CONJ_den, S0B0Token: och_det, S0B1Lemma: och_skola, S0B1LemmaPOS: och_AUX, S0B1POS: CONJ_AUX, S0B1POSLemma: CONJ_skola, S0B1Token: och_ska, S0Lemma: och, S0POS: CONJ, S0Token: och, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

24- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [det, ska, finnas ,.. ]

B0Lemma: den, B0POS: PRON, B0Token: det, B1Lemma: skola, B1POS: AUX, B1Token: ska, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

25- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [det]   B= [ska, finnas, möjligheter ,.. ]

B0Lemma: skola, B0POS: AUX, B0Token: ska, B1Lemma: finnas, B1POS: VERB, B1Token: finnas, S0B0Distance: 1, S0B0Lemma: den_skola, S0B0LemmaPOS: den_AUX, S0B0POS: PRON_AUX, S0B0POSLemma: PRON_skola, S0B0Token: det_ska, S0B1Lemma: den_finnas, S0B1LemmaPOS: den_VERB, S0B1POS: PRON_VERB, S0B1POSLemma: PRON_finnas, S0B1Token: det_finnas, S0Lemma: den, S0POS: PRON, S0Token: det, den_isGouvernedBy_finnas: true, den_isGouvernedBy_finnas_expl: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

26- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ska, finnas, möjligheter ,.. ]

B0Lemma: skola, B0POS: AUX, B0Token: ska, B1Lemma: finnas, B1POS: VERB, B1Token: finnas, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

27- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ska]   B= [finnas, möjligheter, att ,.. ]

B0Lemma: finnas, B0POS: VERB, B0Token: finnas, B1Lemma: möjlighet, B1POS: NOUN, B1Token: möjligheter, S0B0Distance: 1, S0B0Lemma: skola_finnas, S0B0LemmaPOS: skola_VERB, S0B0POS: AUX_VERB, S0B0POSLemma: AUX_finnas, S0B0Token: ska_finnas, S0B1Lemma: skola_möjlighet, S0B1LemmaPOS: skola_NOUN, S0B1POS: AUX_NOUN, S0B1POSLemma: AUX_möjlighet, S0B1Token: ska_möjligheter, S0Lemma: skola, S0POS: AUX, S0Token: ska, skola_isGouvernedBy_finnas: true, skola_isGouvernedBy_finnas_aux: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

28- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [finnas, möjligheter, att ,.. ]

B0Lemma: finnas, B0POS: VERB, B0Token: finnas, B1Lemma: möjlighet, B1POS: NOUN, B1Token: möjligheter, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

29- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [finnas]   B= [möjligheter, att, låsa ,.. ]

B0Lemma: möjlighet, B0POS: NOUN, B0Token: möjligheter, B1Lemma: att, B1POS: PART, B1Token: att, S0B0Distance: 1, S0B0Lemma: finnas_möjlighet, S0B0LemmaPOS: finnas_NOUN, S0B0POS: VERB_NOUN, S0B0POSLemma: VERB_möjlighet, S0B0Token: finnas_möjligheter, S0B1Lemma: finnas_att, S0B1LemmaPOS: finnas_PART, S0B1POS: VERB_PART, S0B1POSLemma: VERB_att, S0B1Token: finnas_att, S0Lemma: finnas, S0POS: VERB, S0Token: finnas, finnas_hasRighDep_nsubj: true, finnas_möjlighet_hasRighDep_nsubj: true, hasRighDep_nsubj: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

30- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [finnas, möjligheter]   B= [att, låsa, in ,.. ]

B0Lemma: att, B0POS: PART, B0Token: att, B1Lemma: låsa, B1POS: VERB, B1Token: låsa, S0B0Distance: 1, S0B0Lemma: möjlighet_att, S0B0LemmaPOS: möjlighet_PART, S0B0POS: NOUN_PART, S0B0POSLemma: NOUN_att, S0B0Token: möjligheter_att, S0B1Lemma: möjlighet_låsa, S0B1LemmaPOS: möjlighet_VERB, S0B1POS: NOUN_VERB, S0B1POSLemma: NOUN_låsa, S0B1Token: möjligheter_låsa, S0Lemma: möjlighet, S0POS: NOUN, S0Token: möjligheter, S1B0Lemma: finnas_att, S1B0LemmaPOS: finnas_PART, S1B0POS: VERB_PART, S1B0POSLemma: VERB_att, S1B0Token: finnas_att, S1Lemma: finnas, S1POS: VERB, S1S0Lemma: finnas_möjlighet, S1S0LemmaPOS: finnas_NOUN, S1S0POS: VERB_NOUN, S1S0POSLemma: VERB_möjlighet, S1S0Token: finnas_möjligheter, S1Token: finnas, SyntaxicRelation: +nsubj, hasRighDep_acl: true, möjlighet_hasRighDep_acl: true, möjlighet_låsa_hasRighDep_acl: true, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

31- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[finnas, möjligheter]]   B= [att, låsa, in ,.. ]

B0Lemma: att, B0POS: PART, B0Token: att, B1Lemma: låsa, B1POS: VERB, B1Token: låsa, S0B0Distance: 1, S0B0Lemma: finnas_möjlighet_att, S0B0LemmaPOS: finnas_möjlighet_PART, S0B0POS: VERB_NOUN_PART, S0B0POSLemma: VERB_NOUN_att, S0B0Token: finnas_möjligheter_att, S0B1Lemma: finnas_möjlighet_låsa, S0B1LemmaPOS: finnas_möjlighet_VERB, S0B1POS: VERB_NOUN_VERB, S0B1POSLemma: VERB_NOUN_låsa, S0B1Token: finnas_möjligheter_låsa, S0Lemma: finnas_möjlighet, S0POS: VERB_NOUN, S0Token: finnas_möjligheter, transitionHistoryLength1: 0, transitionHistoryLength2: 00, transitionHistoryLength3: 002, 

32- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [att, låsa, in ,.. ]

B0Lemma: att, B0POS: PART, B0Token: att, B1Lemma: låsa, B1POS: VERB, B1Token: låsa, transitionHistoryLength1: 1, transitionHistoryLength2: 10, transitionHistoryLength3: 100, 

33- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [att]   B= [låsa, in, eller ,.. ]

B0Lemma: låsa, B0POS: VERB, B0Token: låsa, B1Lemma: in, B1POS: ADV, B1Token: in, S0B0Distance: 1, S0B0Lemma: att_låsa, S0B0LemmaPOS: att_VERB, S0B0POS: PART_VERB, S0B0POSLemma: PART_låsa, S0B0Token: att_låsa, S0B1Lemma: att_in, S0B1LemmaPOS: att_ADV, S0B1POS: PART_ADV, S0B1POSLemma: PART_in, S0B1Token: att_in, S0Lemma: att, S0POS: PART, S0Token: att, att_isGouvernedBy_låsa: true, att_isGouvernedBy_låsa_mark: true, transitionHistoryLength1: 2, transitionHistoryLength2: 21, transitionHistoryLength3: 210, 

34- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [låsa, in, eller ,.. ]

B0Lemma: låsa, B0POS: VERB, B0Token: låsa, B1Lemma: in, B1POS: ADV, B1Token: in, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 021, 

35- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [låsa]   B= [in, eller, fast ,.. ]

B0Lemma: in, B0POS: ADV, B0Token: in, B1Lemma: eller, B1POS: CONJ, B1Token: eller, S0B0Distance: 1, S0B0Lemma: låsa_in, S0B0LemmaPOS: låsa_ADV, S0B0POS: VERB_ADV, S0B0POSLemma: VERB_in, S0B0Token: låsa_in, S0B1Lemma: låsa_eller, S0B1LemmaPOS: låsa_CONJ, S0B1POS: VERB_CONJ, S0B1POSLemma: VERB_eller, S0B1Token: låsa_eller, S0Lemma: låsa, S0POS: VERB, S0Token: låsa, hasRighDep_cc: true, hasRighDep_compound:prt: true, hasRighDep_conj: true, låsa_cykeln_hasRighDep_conj: true, låsa_eller_hasRighDep_cc: true, låsa_hasRighDep_cc: true, låsa_hasRighDep_compound:prt: true, låsa_hasRighDep_conj: true, låsa_in_hasRighDep_compound:prt: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

36- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [låsa, in]   B= [eller, fast, cykeln ,.. ]

B0Lemma: eller, B0POS: CONJ, B0Token: eller, B1Lemma: fast, B1POS: ADV, B1Token: fast, S0B0Distance: 1, S0B0Lemma: in_eller, S0B0LemmaPOS: in_CONJ, S0B0POS: ADV_CONJ, S0B0POSLemma: ADV_eller, S0B0Token: in_eller, S0B1Lemma: in_fast, S0B1LemmaPOS: in_ADV, S0B1POS: ADV_ADV, S0B1POSLemma: ADV_fast, S0B1Token: in_fast, S0Lemma: in, S0POS: ADV, S0Token: in, S1B0Lemma: låsa_eller, S1B0LemmaPOS: låsa_CONJ, S1B0POS: VERB_CONJ, S1B0POSLemma: VERB_eller, S1B0Token: låsa_eller, S1Lemma: låsa, S1POS: VERB, S1S0Lemma: låsa_in, S1S0LemmaPOS: låsa_ADV, S1S0POS: VERB_ADV, S1S0POSLemma: VERB_in, S1S0Token: låsa_in, S1Token: låsa, SyntaxicRelation: +compound:prt, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

37- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[låsa, in]]   B= [eller, fast, cykeln ,.. ]

B0Lemma: eller, B0POS: CONJ, B0Token: eller, B1Lemma: fast, B1POS: ADV, B1Token: fast, S0B0Distance: 1, S0B0Lemma: låsa_in_eller, S0B0LemmaPOS: låsa_in_CONJ, S0B0POS: VERB_ADV_CONJ, S0B0POSLemma: VERB_ADV_eller, S0B0Token: låsa_in_eller, S0B1Lemma: låsa_in_fast, S0B1LemmaPOS: låsa_in_ADV, S0B1POS: VERB_ADV_ADV, S0B1POSLemma: VERB_ADV_fast, S0B1Token: låsa_in_fast, S0Lemma: låsa_in, S0POS: VERB_ADV, S0Token: låsa_in, transitionHistoryLength1: 0, transitionHistoryLength2: 00, transitionHistoryLength3: 002, 

38- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [eller, fast, cykeln ,.. ]

B0Lemma: eller, B0POS: CONJ, B0Token: eller, B1Lemma: fast, B1POS: ADV, B1Token: fast, transitionHistoryLength1: 1, transitionHistoryLength2: 10, transitionHistoryLength3: 100, 

39- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [eller]   B= [fast, cykeln, . ,.. ]

B0Lemma: fast, B0POS: ADV, B0Token: fast, B1Lemma: cykeln, B1POS: NOUN, B1Token: cykeln, S0B0Distance: 1, S0B0Lemma: eller_fast, S0B0LemmaPOS: eller_ADV, S0B0POS: CONJ_ADV, S0B0POSLemma: CONJ_fast, S0B0Token: eller_fast, S0B1Lemma: eller_cykeln, S0B1LemmaPOS: eller_NOUN, S0B1POS: CONJ_NOUN, S0B1POSLemma: CONJ_cykeln, S0B1Token: eller_cykeln, S0Lemma: eller, S0POS: CONJ, S0Token: eller, transitionHistoryLength1: 2, transitionHistoryLength2: 21, transitionHistoryLength3: 210, 

40- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [fast, cykeln, . ,.. ]

B0Lemma: fast, B0POS: ADV, B0Token: fast, B1Lemma: cykeln, B1POS: NOUN, B1Token: cykeln, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 021, 

41- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [fast]   B= [cykeln, . ,.. ]

B0Lemma: cykeln, B0POS: NOUN, B0Token: cykeln, B1Lemma: ., B1POS: PUNCT, B1Token: ., S0B0Distance: 1, S0B0Lemma: fast_cykeln, S0B0LemmaPOS: fast_NOUN, S0B0POS: ADV_NOUN, S0B0POSLemma: ADV_cykeln, S0B0Token: fast_cykeln, S0B1Lemma: fast_., S0B1LemmaPOS: fast_PUNCT, S0B1POS: ADV_PUNCT, S0B1POSLemma: ADV_., S0B1Token: fast_., S0Lemma: fast, S0POS: ADV, S0Token: fast, fast_isGouvernedBy_cykeln: true, fast_isGouvernedBy_cykeln_advmod: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

42- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [cykeln, . ,.. ]

B0Lemma: cykeln, B0POS: NOUN, B0Token: cykeln, B1Lemma: ., B1POS: PUNCT, B1Token: ., transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

43- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [cykeln]   B= [.]

B0Lemma: ., B0POS: PUNCT, B0Token: ., S0B0Distance: 1, S0B0Lemma: cykeln_., S0B0LemmaPOS: cykeln_PUNCT, S0B0POS: NOUN_PUNCT, S0B0POSLemma: NOUN_., S0B0Token: cykeln_., S0Lemma: cykeln, S0POS: NOUN, S0Token: cykeln, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

44- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [.]

B0Lemma: ., B0POS: PUNCT, B0Token: ., transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

45- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [ ]

S0Lemma: ., S0POS: PUNCT, S0Token: ., transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

46- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

## Sentence No. 12 - 
Det går inte att komma igång med appen utan att först skapa ett konto och lägga till bilen i datorn . 
### Existing MWEs: 
1- **komma igång** (VPC)
2- **lägga till** (VPC)



0- &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Det, går, inte ,.. ]

B0Lemma: den, B0POS: PRON, B0Token: Det, B1Lemma: gå, B1POS: VERB, B1Token: går, 

1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Det]   B= [går, inte, att ,.. ]

B0Lemma: gå, B0POS: VERB, B0Token: går, B1Lemma: inte, B1POS: ADV, B1Token: inte, S0B0Distance: 1, S0B0Lemma: den_gå, S0B0LemmaPOS: den_VERB, S0B0POS: PRON_VERB, S0B0POSLemma: PRON_gå, S0B0Token: Det_går, S0B1Lemma: den_inte, S0B1LemmaPOS: den_ADV, S0B1POS: PRON_ADV, S0B1POSLemma: PRON_inte, S0B1Token: Det_inte, S0Lemma: den, S0POS: PRON, S0Token: Det, den_isGouvernedBy_gå: true, den_isGouvernedBy_gå_expl: true, 

2- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [går, inte, att ,.. ]

B0Lemma: gå, B0POS: VERB, B0Token: går, B1Lemma: inte, B1POS: ADV, B1Token: inte, transitionHistoryLength1: 0, 

3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [går]   B= [inte, att, komma ,.. ]

B0Lemma: inte, B0POS: ADV, B0Token: inte, B1Lemma: att, B1POS: PART, B1Token: att, S0B0Distance: 1, S0B0Lemma: gå_inte, S0B0LemmaPOS: gå_ADV, S0B0POS: VERB_ADV, S0B0POSLemma: VERB_inte, S0B0Token: går_inte, S0B1Lemma: gå_att, S0B1LemmaPOS: gå_PART, S0B1POS: VERB_PART, S0B1POSLemma: VERB_att, S0B1Token: går_att, S0Lemma: gå, S0POS: VERB, S0Token: går, transitionHistoryLength1: 2, transitionHistoryLength2: 20, 

4- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [inte, att, komma ,.. ]

B0Lemma: inte, B0POS: ADV, B0Token: inte, B1Lemma: att, B1POS: PART, B1Token: att, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [inte]   B= [att, komma, igång ,.. ]

B0Lemma: att, B0POS: PART, B0Token: att, B1Lemma: komma, B1POS: VERB, B1Token: komma, S0B0Distance: 1, S0B0Lemma: inte_att, S0B0LemmaPOS: inte_PART, S0B0POS: ADV_PART, S0B0POSLemma: ADV_att, S0B0Token: inte_att, S0B1Lemma: inte_komma, S0B1LemmaPOS: inte_VERB, S0B1POS: ADV_VERB, S0B1POSLemma: ADV_komma, S0B1Token: inte_komma, S0Lemma: inte, S0POS: ADV, S0Token: inte, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

6- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [att, komma, igång ,.. ]

B0Lemma: att, B0POS: PART, B0Token: att, B1Lemma: komma, B1POS: VERB, B1Token: komma, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [att]   B= [komma, igång, med ,.. ]

B0Lemma: komma, B0POS: VERB, B0Token: komma, B1Lemma: igång, B1POS: ADV, B1Token: igång, S0B0Distance: 1, S0B0Lemma: att_komma, S0B0LemmaPOS: att_VERB, S0B0POS: PART_VERB, S0B0POSLemma: PART_komma, S0B0Token: att_komma, S0B1Lemma: att_igång, S0B1LemmaPOS: att_ADV, S0B1POS: PART_ADV, S0B1POSLemma: PART_igång, S0B1Token: att_igång, S0Lemma: att, S0POS: PART, S0Token: att, att_isGouvernedBy_komma: true, att_isGouvernedBy_komma_mark: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

8- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [komma, igång, med ,.. ]

B0Lemma: komma, B0POS: VERB, B0Token: komma, B1Lemma: igång, B1POS: ADV, B1Token: igång, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [komma]   B= [igång, med, appen ,.. ]

B0Lemma: igång, B0POS: ADV, B0Token: igång, B1Lemma: med, B1POS: ADP, B1Token: med, S0B0Distance: 1, S0B0Lemma: komma_igång, S0B0LemmaPOS: komma_ADV, S0B0POS: VERB_ADV, S0B0POSLemma: VERB_igång, S0B0Token: komma_igång, S0B1Lemma: komma_med, S0B1LemmaPOS: komma_ADP, S0B1POS: VERB_ADP, S0B1POSLemma: VERB_med, S0B1Token: komma_med, S0Lemma: komma, S0POS: VERB, S0Token: komma, hasRighDep_advcl: true, hasRighDep_compound:prt: true, hasRighDep_nmod: true, komma_app_hasRighDep_nmod: true, komma_hasRighDep_advcl: true, komma_hasRighDep_compound:prt: true, komma_hasRighDep_nmod: true, komma_igång_hasRighDep_compound:prt: true, komma_skapa_hasRighDep_advcl: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

10- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [komma, igång]   B= [med, appen, utan ,.. ]

B0Lemma: med, B0POS: ADP, B0Token: med, B1Lemma: app, B1POS: NOUN, B1Token: appen, S0B0Distance: 1, S0B0Lemma: igång_med, S0B0LemmaPOS: igång_ADP, S0B0POS: ADV_ADP, S0B0POSLemma: ADV_med, S0B0Token: igång_med, S0B1Lemma: igång_app, S0B1LemmaPOS: igång_NOUN, S0B1POS: ADV_NOUN, S0B1POSLemma: ADV_app, S0B1Token: igång_appen, S0Lemma: igång, S0POS: ADV, S0Token: igång, S1B0Lemma: komma_med, S1B0LemmaPOS: komma_ADP, S1B0POS: VERB_ADP, S1B0POSLemma: VERB_med, S1B0Token: komma_med, S1Lemma: komma, S1POS: VERB, S1S0Lemma: komma_igång, S1S0LemmaPOS: komma_ADV, S1S0POS: VERB_ADV, S1S0POSLemma: VERB_igång, S1S0Token: komma_igång, S1Token: komma, SyntaxicRelation: +compound:prt, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

11- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[komma, igång]]   B= [med, appen, utan ,.. ]

B0Lemma: med, B0POS: ADP, B0Token: med, B1Lemma: app, B1POS: NOUN, B1Token: appen, S0B0Distance: 1, S0B0Lemma: komma_igång_med, S0B0LemmaPOS: komma_igång_ADP, S0B0POS: VERB_ADV_ADP, S0B0POSLemma: VERB_ADV_med, S0B0Token: komma_igång_med, S0B1Lemma: komma_igång_app, S0B1LemmaPOS: komma_igång_NOUN, S0B1POS: VERB_ADV_NOUN, S0B1POSLemma: VERB_ADV_app, S0B1Token: komma_igång_appen, S0Lemma: komma_igång, S0POS: VERB_ADV, S0Token: komma_igång, transitionHistoryLength1: 0, transitionHistoryLength2: 00, transitionHistoryLength3: 002, 

12- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [med, appen, utan ,.. ]

B0Lemma: med, B0POS: ADP, B0Token: med, B1Lemma: app, B1POS: NOUN, B1Token: appen, transitionHistoryLength1: 1, transitionHistoryLength2: 10, transitionHistoryLength3: 100, 

13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [med]   B= [appen, utan, att ,.. ]

B0Lemma: app, B0POS: NOUN, B0Token: appen, B1Lemma: utan, B1POS: ADP, B1Token: utan, S0B0Distance: 1, S0B0Lemma: med_app, S0B0LemmaPOS: med_NOUN, S0B0POS: ADP_NOUN, S0B0POSLemma: ADP_app, S0B0Token: med_appen, S0B1Lemma: med_utan, S0B1LemmaPOS: med_ADP, S0B1POS: ADP_ADP, S0B1POSLemma: ADP_utan, S0B1Token: med_utan, S0Lemma: med, S0POS: ADP, S0Token: med, med_isGouvernedBy_app: true, med_isGouvernedBy_app_case: true, transitionHistoryLength1: 2, transitionHistoryLength2: 21, transitionHistoryLength3: 210, 

14- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [appen, utan, att ,.. ]

B0Lemma: app, B0POS: NOUN, B0Token: appen, B1Lemma: utan, B1POS: ADP, B1Token: utan, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 021, 

15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [appen]   B= [utan, att, först ,.. ]

B0Lemma: utan, B0POS: ADP, B0Token: utan, B1Lemma: att, B1POS: PART, B1Token: att, S0B0Distance: 1, S0B0Lemma: app_utan, S0B0LemmaPOS: app_ADP, S0B0POS: NOUN_ADP, S0B0POSLemma: NOUN_utan, S0B0Token: appen_utan, S0B1Lemma: app_att, S0B1LemmaPOS: app_PART, S0B1POS: NOUN_PART, S0B1POSLemma: NOUN_att, S0B1Token: appen_att, S0Lemma: app, S0POS: NOUN, S0Token: appen, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

16- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [utan, att, först ,.. ]

B0Lemma: utan, B0POS: ADP, B0Token: utan, B1Lemma: att, B1POS: PART, B1Token: att, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [utan]   B= [att, först, skapa ,.. ]

B0Lemma: att, B0POS: PART, B0Token: att, B1Lemma: först, B1POS: ADV, B1Token: först, S0B0Distance: 1, S0B0Lemma: utan_att, S0B0LemmaPOS: utan_PART, S0B0POS: ADP_PART, S0B0POSLemma: ADP_att, S0B0Token: utan_att, S0B1Lemma: utan_först, S0B1LemmaPOS: utan_ADV, S0B1POS: ADP_ADV, S0B1POSLemma: ADP_först, S0B1Token: utan_först, S0Lemma: utan, S0POS: ADP, S0Token: utan, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, utan_isGouvernedBy_skapa: true, utan_isGouvernedBy_skapa_case: true, 

18- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [att, först, skapa ,.. ]

B0Lemma: att, B0POS: PART, B0Token: att, B1Lemma: först, B1POS: ADV, B1Token: först, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [att]   B= [först, skapa, ett ,.. ]

B0Lemma: först, B0POS: ADV, B0Token: först, B1Lemma: skapa, B1POS: VERB, B1Token: skapa, S0B0Distance: 1, S0B0Lemma: att_först, S0B0LemmaPOS: att_ADV, S0B0POS: PART_ADV, S0B0POSLemma: PART_först, S0B0Token: att_först, S0B1Lemma: att_skapa, S0B1LemmaPOS: att_VERB, S0B1POS: PART_VERB, S0B1POSLemma: PART_skapa, S0B1Token: att_skapa, S0Lemma: att, S0POS: PART, S0Token: att, att_isGouvernedBy_skapa: true, att_isGouvernedBy_skapa_mark: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

20- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [först, skapa, ett ,.. ]

B0Lemma: först, B0POS: ADV, B0Token: först, B1Lemma: skapa, B1POS: VERB, B1Token: skapa, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [först]   B= [skapa, ett, konto ,.. ]

B0Lemma: skapa, B0POS: VERB, B0Token: skapa, B1Lemma: en, B1POS: DET, B1Token: ett, S0B0Distance: 1, S0B0Lemma: först_skapa, S0B0LemmaPOS: först_VERB, S0B0POS: ADV_VERB, S0B0POSLemma: ADV_skapa, S0B0Token: först_skapa, S0B1Lemma: först_en, S0B1LemmaPOS: först_DET, S0B1POS: ADV_DET, S0B1POSLemma: ADV_en, S0B1Token: först_ett, S0Lemma: först, S0POS: ADV, S0Token: först, först_isGouvernedBy_skapa: true, först_isGouvernedBy_skapa_advmod: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

22- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [skapa, ett, konto ,.. ]

B0Lemma: skapa, B0POS: VERB, B0Token: skapa, B1Lemma: en, B1POS: DET, B1Token: ett, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

23- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [skapa]   B= [ett, konto, och ,.. ]

B0Lemma: en, B0POS: DET, B0Token: ett, B1Lemma: konto, B1POS: NOUN, B1Token: konto, S0B0Distance: 1, S0B0Lemma: skapa_en, S0B0LemmaPOS: skapa_DET, S0B0POS: VERB_DET, S0B0POSLemma: VERB_en, S0B0Token: skapa_ett, S0B1Lemma: skapa_konto, S0B1LemmaPOS: skapa_NOUN, S0B1POS: VERB_NOUN, S0B1POSLemma: VERB_konto, S0B1Token: skapa_konto, S0Lemma: skapa, S0POS: VERB, S0Token: skapa, hasRighDep_cc: true, hasRighDep_conj: true, hasRighDep_dobj: true, hasRighDep_nmod: true, skapa_bil_hasRighDep_nmod: true, skapa_dator_hasRighDep_nmod: true, skapa_hasRighDep_cc: true, skapa_hasRighDep_conj: true, skapa_hasRighDep_dobj: true, skapa_hasRighDep_nmod: true, skapa_konto_hasRighDep_dobj: true, skapa_lägga_hasRighDep_conj: true, skapa_och_hasRighDep_cc: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

24- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ett, konto, och ,.. ]

B0Lemma: en, B0POS: DET, B0Token: ett, B1Lemma: konto, B1POS: NOUN, B1Token: konto, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

25- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ett]   B= [konto, och, lägga ,.. ]

B0Lemma: konto, B0POS: NOUN, B0Token: konto, B1Lemma: och, B1POS: CONJ, B1Token: och, S0B0Distance: 1, S0B0Lemma: en_konto, S0B0LemmaPOS: en_NOUN, S0B0POS: DET_NOUN, S0B0POSLemma: DET_konto, S0B0Token: ett_konto, S0B1Lemma: en_och, S0B1LemmaPOS: en_CONJ, S0B1POS: DET_CONJ, S0B1POSLemma: DET_och, S0B1Token: ett_och, S0Lemma: en, S0POS: DET, S0Token: ett, en_isGouvernedBy_konto: true, en_isGouvernedBy_konto_det: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

26- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [konto, och, lägga ,.. ]

B0Lemma: konto, B0POS: NOUN, B0Token: konto, B1Lemma: och, B1POS: CONJ, B1Token: och, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

27- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [konto]   B= [och, lägga, till ,.. ]

B0Lemma: och, B0POS: CONJ, B0Token: och, B1Lemma: lägga, B1POS: VERB, B1Token: lägga, S0B0Distance: 1, S0B0Lemma: konto_och, S0B0LemmaPOS: konto_CONJ, S0B0POS: NOUN_CONJ, S0B0POSLemma: NOUN_och, S0B0Token: konto_och, S0B1Lemma: konto_lägga, S0B1LemmaPOS: konto_VERB, S0B1POS: NOUN_VERB, S0B1POSLemma: NOUN_lägga, S0B1Token: konto_lägga, S0Lemma: konto, S0POS: NOUN, S0Token: konto, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

28- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [och, lägga, till ,.. ]

B0Lemma: och, B0POS: CONJ, B0Token: och, B1Lemma: lägga, B1POS: VERB, B1Token: lägga, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

29- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [och]   B= [lägga, till, bilen ,.. ]

B0Lemma: lägga, B0POS: VERB, B0Token: lägga, B1Lemma: till, B1POS: ADP, B1Token: till, S0B0Distance: 1, S0B0Lemma: och_lägga, S0B0LemmaPOS: och_VERB, S0B0POS: CONJ_VERB, S0B0POSLemma: CONJ_lägga, S0B0Token: och_lägga, S0B1Lemma: och_till, S0B1LemmaPOS: och_ADP, S0B1POS: CONJ_ADP, S0B1POSLemma: CONJ_till, S0B1Token: och_till, S0Lemma: och, S0POS: CONJ, S0Token: och, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

30- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [lägga, till, bilen ,.. ]

B0Lemma: lägga, B0POS: VERB, B0Token: lägga, B1Lemma: till, B1POS: ADP, B1Token: till, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

31- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [lägga]   B= [till, bilen, i ,.. ]

B0Lemma: till, B0POS: ADP, B0Token: till, B1Lemma: bil, B1POS: NOUN, B1Token: bilen, S0B0Distance: 1, S0B0Lemma: lägga_till, S0B0LemmaPOS: lägga_ADP, S0B0POS: VERB_ADP, S0B0POSLemma: VERB_till, S0B0Token: lägga_till, S0B1Lemma: lägga_bil, S0B1LemmaPOS: lägga_NOUN, S0B1POS: VERB_NOUN, S0B1POSLemma: VERB_bil, S0B1Token: lägga_bilen, S0Lemma: lägga, S0POS: VERB, S0Token: lägga, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

32- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [lägga, till]   B= [bilen, i, datorn ,.. ]

B0Lemma: bil, B0POS: NOUN, B0Token: bilen, B1Lemma: i, B1POS: ADP, B1Token: i, S0B0Distance: 1, S0B0Lemma: till_bil, S0B0LemmaPOS: till_NOUN, S0B0POS: ADP_NOUN, S0B0POSLemma: ADP_bil, S0B0Token: till_bilen, S0B1Lemma: till_i, S0B1LemmaPOS: till_ADP, S0B1POS: ADP_ADP, S0B1POSLemma: ADP_i, S0B1Token: till_i, S0Lemma: till, S0POS: ADP, S0Token: till, S1B0Lemma: lägga_bil, S1B0LemmaPOS: lägga_NOUN, S1B0POS: VERB_NOUN, S1B0POSLemma: VERB_bil, S1B0Token: lägga_bilen, S1Lemma: lägga, S1POS: VERB, S1S0Lemma: lägga_till, S1S0LemmaPOS: lägga_ADP, S1S0POS: VERB_ADP, S1S0POSLemma: VERB_till, S1S0Token: lägga_till, S1Token: lägga, till_isGouvernedBy_bil: true, till_isGouvernedBy_bil_case: true, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

33- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[lägga, till]]   B= [bilen, i, datorn ,.. ]

B0Lemma: bil, B0POS: NOUN, B0Token: bilen, B1Lemma: i, B1POS: ADP, B1Token: i, S0B0Distance: 1, S0B0Lemma: lägga_till_bil, S0B0LemmaPOS: lägga_till_NOUN, S0B0POS: VERB_ADP_NOUN, S0B0POSLemma: VERB_ADP_bil, S0B0Token: lägga_till_bilen, S0B1Lemma: lägga_till_i, S0B1LemmaPOS: lägga_till_ADP, S0B1POS: VERB_ADP_ADP, S0B1POSLemma: VERB_ADP_i, S0B1Token: lägga_till_i, S0Lemma: lägga_till, S0POS: VERB_ADP, S0Token: lägga_till, transitionHistoryLength1: 0, transitionHistoryLength2: 00, transitionHistoryLength3: 002, 

34- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [bilen, i, datorn ,.. ]

B0Lemma: bil, B0POS: NOUN, B0Token: bilen, B1Lemma: i, B1POS: ADP, B1Token: i, transitionHistoryLength1: 1, transitionHistoryLength2: 10, transitionHistoryLength3: 100, 

35- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [bilen]   B= [i, datorn, . ,.. ]

B0Lemma: i, B0POS: ADP, B0Token: i, B1Lemma: dator, B1POS: NOUN, B1Token: datorn, S0B0Distance: 1, S0B0Lemma: bil_i, S0B0LemmaPOS: bil_ADP, S0B0POS: NOUN_ADP, S0B0POSLemma: NOUN_i, S0B0Token: bilen_i, S0B1Lemma: bil_dator, S0B1LemmaPOS: bil_NOUN, S0B1POS: NOUN_NOUN, S0B1POSLemma: NOUN_dator, S0B1Token: bilen_datorn, S0Lemma: bil, S0POS: NOUN, S0Token: bilen, transitionHistoryLength1: 2, transitionHistoryLength2: 21, transitionHistoryLength3: 210, 

36- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [i, datorn, . ,.. ]

B0Lemma: i, B0POS: ADP, B0Token: i, B1Lemma: dator, B1POS: NOUN, B1Token: datorn, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 021, 

37- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [i]   B= [datorn, . ,.. ]

B0Lemma: dator, B0POS: NOUN, B0Token: datorn, B1Lemma: ., B1POS: PUNCT, B1Token: ., S0B0Distance: 1, S0B0Lemma: i_dator, S0B0LemmaPOS: i_NOUN, S0B0POS: ADP_NOUN, S0B0POSLemma: ADP_dator, S0B0Token: i_datorn, S0B1Lemma: i_., S0B1LemmaPOS: i_PUNCT, S0B1POS: ADP_PUNCT, S0B1POSLemma: ADP_., S0B1Token: i_., S0Lemma: i, S0POS: ADP, S0Token: i, i_isGouvernedBy_dator: true, i_isGouvernedBy_dator_case: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

38- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [datorn, . ,.. ]

B0Lemma: dator, B0POS: NOUN, B0Token: datorn, B1Lemma: ., B1POS: PUNCT, B1Token: ., transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

39- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [datorn]   B= [.]

B0Lemma: ., B0POS: PUNCT, B0Token: ., S0B0Distance: 1, S0B0Lemma: dator_., S0B0LemmaPOS: dator_PUNCT, S0B0POS: NOUN_PUNCT, S0B0POSLemma: NOUN_., S0B0Token: datorn_., S0Lemma: dator, S0POS: NOUN, S0Token: datorn, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

40- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [.]

B0Lemma: ., B0POS: PUNCT, B0Token: ., transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

41- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [ ]

S0Lemma: ., S0POS: PUNCT, S0Token: ., transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

42- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

## Sentence No. 22 - 
Mats Grauers och Anderz Larqvist , ordförande och klubbdirektör , säger sig inte ha tagit ett slutgiltigt beslut . 
### Existing MWEs: 
1- **säger sig** (IReflV)
2- **tagit beslut** (LVC)



0- &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Mats, Grauers, och ,.. ]

B0Lemma: Mas, B0POS: PROPN, B0Token: Mats, B1Lemma: Grau, B1POS: PROPN, B1Token: Grauers, 

1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Mats]   B= [Grauers, och, Anderz ,.. ]

B0Lemma: Grau, B0POS: PROPN, B0Token: Grauers, B1Lemma: och, B1POS: CONJ, B1Token: och, Mas_isGouvernedBy_Grau: true, Mas_isGouvernedBy_Grau_nmod:poss: true, S0B0Distance: 1, S0B0Lemma: Mas_Grau, S0B0LemmaPOS: Mas_PROPN, S0B0POS: PROPN_PROPN, S0B0POSLemma: PROPN_Grau, S0B0Token: Mats_Grauers, S0B1Lemma: Mas_och, S0B1LemmaPOS: Mas_CONJ, S0B1POS: PROPN_CONJ, S0B1POSLemma: PROPN_och, S0B1Token: Mats_och, S0Lemma: Mas, S0POS: PROPN, S0Token: Mats, 

2- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Grauers, och, Anderz ,.. ]

B0Lemma: Grau, B0POS: PROPN, B0Token: Grauers, B1Lemma: och, B1POS: CONJ, B1Token: och, transitionHistoryLength1: 0, 

3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Grauers]   B= [och, Anderz, Larqvist ,.. ]

B0Lemma: och, B0POS: CONJ, B0Token: och, B1Lemma: Anderz, B1POS: PROPN, B1Token: Anderz, Grau_,_hasRighDep_punct: true, Grau_Anderz_hasRighDep_conj: true, Grau_hasRighDep_cc: true, Grau_hasRighDep_conj: true, Grau_hasRighDep_punct: true, Grau_isGouvernedBy_säga: true, Grau_isGouvernedBy_säga_nsubj: true, Grau_klubbdirektör_hasRighDep_conj: true, Grau_och_hasRighDep_cc: true, Grau_ordförande_hasRighDep_conj: true, S0B0Distance: 1, S0B0Lemma: Grau_och, S0B0LemmaPOS: Grau_CONJ, S0B0POS: PROPN_CONJ, S0B0POSLemma: PROPN_och, S0B0Token: Grauers_och, S0B1Lemma: Grau_Anderz, S0B1LemmaPOS: Grau_PROPN, S0B1POS: PROPN_PROPN, S0B1POSLemma: PROPN_Anderz, S0B1Token: Grauers_Anderz, S0Lemma: Grau, S0POS: PROPN, S0Token: Grauers, hasRighDep_cc: true, hasRighDep_conj: true, hasRighDep_punct: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, 

4- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [och, Anderz, Larqvist ,.. ]

B0Lemma: och, B0POS: CONJ, B0Token: och, B1Lemma: Anderz, B1POS: PROPN, B1Token: Anderz, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [och]   B= [Anderz, Larqvist, , ,.. ]

B0Lemma: Anderz, B0POS: PROPN, B0Token: Anderz, B1Lemma: Larqvist, B1POS: PROPN, B1Token: Larqvist, S0B0Distance: 1, S0B0Lemma: och_Anderz, S0B0LemmaPOS: och_PROPN, S0B0POS: CONJ_PROPN, S0B0POSLemma: CONJ_Anderz, S0B0Token: och_Anderz, S0B1Lemma: och_Larqvist, S0B1LemmaPOS: och_PROPN, S0B1POS: CONJ_PROPN, S0B1POSLemma: CONJ_Larqvist, S0B1Token: och_Larqvist, S0Lemma: och, S0POS: CONJ, S0Token: och, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

6- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Anderz, Larqvist, , ,.. ]

B0Lemma: Anderz, B0POS: PROPN, B0Token: Anderz, B1Lemma: Larqvist, B1POS: PROPN, B1Token: Larqvist, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Anderz]   B= [Larqvist, ,, ordförande ,.. ]

Anderz_Larqvist_hasRighDep_name: true, Anderz_hasRighDep_name: true, B0Lemma: Larqvist, B0POS: PROPN, B0Token: Larqvist, B1Lemma: ,, B1POS: PUNCT, B1Token: ,, S0B0Distance: 1, S0B0Lemma: Anderz_Larqvist, S0B0LemmaPOS: Anderz_PROPN, S0B0POS: PROPN_PROPN, S0B0POSLemma: PROPN_Larqvist, S0B0Token: Anderz_Larqvist, S0B1Lemma: Anderz_,, S0B1LemmaPOS: Anderz_PUNCT, S0B1POS: PROPN_PUNCT, S0B1POSLemma: PROPN_,, S0B1Token: Anderz_,, S0Lemma: Anderz, S0POS: PROPN, S0Token: Anderz, hasRighDep_name: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

8- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Larqvist, ,, ordförande ,.. ]

B0Lemma: Larqvist, B0POS: PROPN, B0Token: Larqvist, B1Lemma: ,, B1POS: PUNCT, B1Token: ,, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Larqvist]   B= [,, ordförande, och ,.. ]

B0Lemma: ,, B0POS: PUNCT, B0Token: ,, B1Lemma: ordförande, B1POS: NOUN, B1Token: ordförande, S0B0Distance: 1, S0B0Lemma: Larqvist_,, S0B0LemmaPOS: Larqvist_PUNCT, S0B0POS: PROPN_PUNCT, S0B0POSLemma: PROPN_,, S0B0Token: Larqvist_,, S0B1Lemma: Larqvist_ordförande, S0B1LemmaPOS: Larqvist_NOUN, S0B1POS: PROPN_NOUN, S0B1POSLemma: PROPN_ordförande, S0B1Token: Larqvist_ordförande, S0Lemma: Larqvist, S0POS: PROPN, S0Token: Larqvist, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

10- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, ordförande, och ,.. ]

B0Lemma: ,, B0POS: PUNCT, B0Token: ,, B1Lemma: ordförande, B1POS: NOUN, B1Token: ordförande, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [ordförande, och, klubbdirektör ,.. ]

B0Lemma: ordförande, B0POS: NOUN, B0Token: ordförande, B1Lemma: och, B1POS: CONJ, B1Token: och, S0B0Distance: 1, S0B0Lemma: ,_ordförande, S0B0LemmaPOS: ,_NOUN, S0B0POS: PUNCT_NOUN, S0B0POSLemma: PUNCT_ordförande, S0B0Token: ,_ordförande, S0B1Lemma: ,_och, S0B1LemmaPOS: ,_CONJ, S0B1POS: PUNCT_CONJ, S0B1POSLemma: PUNCT_och, S0B1Token: ,_och, S0Lemma: ,, S0POS: PUNCT, S0Token: ,, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

12- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ordförande, och, klubbdirektör ,.. ]

B0Lemma: ordförande, B0POS: NOUN, B0Token: ordförande, B1Lemma: och, B1POS: CONJ, B1Token: och, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ordförande]   B= [och, klubbdirektör, , ,.. ]

B0Lemma: och, B0POS: CONJ, B0Token: och, B1Lemma: klubbdirektör, B1POS: NOUN, B1Token: klubbdirektör, S0B0Distance: 1, S0B0Lemma: ordförande_och, S0B0LemmaPOS: ordförande_CONJ, S0B0POS: NOUN_CONJ, S0B0POSLemma: NOUN_och, S0B0Token: ordförande_och, S0B1Lemma: ordförande_klubbdirektör, S0B1LemmaPOS: ordförande_NOUN, S0B1POS: NOUN_NOUN, S0B1POSLemma: NOUN_klubbdirektör, S0B1Token: ordförande_klubbdirektör, S0Lemma: ordförande, S0POS: NOUN, S0Token: ordförande, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

14- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [och, klubbdirektör, , ,.. ]

B0Lemma: och, B0POS: CONJ, B0Token: och, B1Lemma: klubbdirektör, B1POS: NOUN, B1Token: klubbdirektör, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [och]   B= [klubbdirektör, ,, säger ,.. ]

B0Lemma: klubbdirektör, B0POS: NOUN, B0Token: klubbdirektör, B1Lemma: ,, B1POS: PUNCT, B1Token: ,, S0B0Distance: 1, S0B0Lemma: och_klubbdirektör, S0B0LemmaPOS: och_NOUN, S0B0POS: CONJ_NOUN, S0B0POSLemma: CONJ_klubbdirektör, S0B0Token: och_klubbdirektör, S0B1Lemma: och_,, S0B1LemmaPOS: och_PUNCT, S0B1POS: CONJ_PUNCT, S0B1POSLemma: CONJ_,, S0B1Token: och_,, S0Lemma: och, S0POS: CONJ, S0Token: och, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

16- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [klubbdirektör, ,, säger ,.. ]

B0Lemma: klubbdirektör, B0POS: NOUN, B0Token: klubbdirektör, B1Lemma: ,, B1POS: PUNCT, B1Token: ,, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [klubbdirektör]   B= [,, säger, sig ,.. ]

B0Lemma: ,, B0POS: PUNCT, B0Token: ,, B1Lemma: säga, B1POS: VERB, B1Token: säger, S0B0Distance: 1, S0B0Lemma: klubbdirektör_,, S0B0LemmaPOS: klubbdirektör_PUNCT, S0B0POS: NOUN_PUNCT, S0B0POSLemma: NOUN_,, S0B0Token: klubbdirektör_,, S0B1Lemma: klubbdirektör_säga, S0B1LemmaPOS: klubbdirektör_VERB, S0B1POS: NOUN_VERB, S0B1POSLemma: NOUN_säga, S0B1Token: klubbdirektör_säger, S0Lemma: klubbdirektör, S0POS: NOUN, S0Token: klubbdirektör, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

18- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, säger, sig ,.. ]

B0Lemma: ,, B0POS: PUNCT, B0Token: ,, B1Lemma: säga, B1POS: VERB, B1Token: säger, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [säger, sig, inte ,.. ]

B0Lemma: säga, B0POS: VERB, B0Token: säger, B1Lemma: sig, B1POS: PRON, B1Token: sig, S0B0Distance: 1, S0B0Lemma: ,_säga, S0B0LemmaPOS: ,_VERB, S0B0POS: PUNCT_VERB, S0B0POSLemma: PUNCT_säga, S0B0Token: ,_säger, S0B1Lemma: ,_sig, S0B1LemmaPOS: ,_PRON, S0B1POS: PUNCT_PRON, S0B1POSLemma: PUNCT_sig, S0B1Token: ,_sig, S0Lemma: ,, S0POS: PUNCT, S0Token: ,, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

20- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [säger, sig, inte ,.. ]

B0Lemma: säga, B0POS: VERB, B0Token: säger, B1Lemma: sig, B1POS: PRON, B1Token: sig, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [säger]   B= [sig, inte, ha ,.. ]

B0Lemma: sig, B0POS: PRON, B0Token: sig, B1Lemma: inte, B1POS: ADV, B1Token: inte, S0B0Distance: 1, S0B0Lemma: säga_sig, S0B0LemmaPOS: säga_PRON, S0B0POS: VERB_PRON, S0B0POSLemma: VERB_sig, S0B0Token: säger_sig, S0B1Lemma: säga_inte, S0B1LemmaPOS: säga_ADV, S0B1POS: VERB_ADV, S0B1POSLemma: VERB_inte, S0B1Token: säger_inte, S0Lemma: säga, S0POS: VERB, S0Token: säger, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

22- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [säger, sig]   B= [inte, ha, tagit ,.. ]

B0Lemma: inte, B0POS: ADV, B0Token: inte, B1Lemma: ha, B1POS: AUX, B1Token: ha, S0B0Distance: 1, S0B0Lemma: sig_inte, S0B0LemmaPOS: sig_ADV, S0B0POS: PRON_ADV, S0B0POSLemma: PRON_inte, S0B0Token: sig_inte, S0B1Lemma: sig_ha, S0B1LemmaPOS: sig_AUX, S0B1POS: PRON_AUX, S0B1POSLemma: PRON_ha, S0B1Token: sig_ha, S0Lemma: sig, S0POS: PRON, S0Token: sig, S1B0Lemma: säga_inte, S1B0LemmaPOS: säga_ADV, S1B0POS: VERB_ADV, S1B0POSLemma: VERB_inte, S1B0Token: säger_inte, S1Lemma: säga, S1POS: VERB, S1S0Lemma: säga_sig, S1S0LemmaPOS: säga_PRON, S1S0POS: VERB_PRON, S1S0POSLemma: VERB_sig, S1S0Token: säger_sig, S1Token: säger, SyntaxicRelation: +dobj, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

23- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[säger, sig]]   B= [inte, ha, tagit ,.. ]

B0Lemma: inte, B0POS: ADV, B0Token: inte, B1Lemma: ha, B1POS: AUX, B1Token: ha, S0B0Distance: 1, S0B0Lemma: säga_sig_inte, S0B0LemmaPOS: säga_sig_ADV, S0B0POS: VERB_PRON_ADV, S0B0POSLemma: VERB_PRON_inte, S0B0Token: säger_sig_inte, S0B1Lemma: säga_sig_ha, S0B1LemmaPOS: säga_sig_AUX, S0B1POS: VERB_PRON_AUX, S0B1POSLemma: VERB_PRON_ha, S0B1Token: säger_sig_ha, S0Lemma: säga_sig, S0POS: VERB_PRON, S0Token: säger_sig, transitionHistoryLength1: 0, transitionHistoryLength2: 00, transitionHistoryLength3: 002, 

24- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [inte, ha, tagit ,.. ]

B0Lemma: inte, B0POS: ADV, B0Token: inte, B1Lemma: ha, B1POS: AUX, B1Token: ha, transitionHistoryLength1: 1, transitionHistoryLength2: 10, transitionHistoryLength3: 100, 

25- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [inte]   B= [ha, tagit, ett ,.. ]

B0Lemma: ha, B0POS: AUX, B0Token: ha, B1Lemma: ta, B1POS: VERB, B1Token: tagit, S0B0Distance: 1, S0B0Lemma: inte_ha, S0B0LemmaPOS: inte_AUX, S0B0POS: ADV_AUX, S0B0POSLemma: ADV_ha, S0B0Token: inte_ha, S0B1Lemma: inte_ta, S0B1LemmaPOS: inte_VERB, S0B1POS: ADV_VERB, S0B1POSLemma: ADV_ta, S0B1Token: inte_tagit, S0Lemma: inte, S0POS: ADV, S0Token: inte, transitionHistoryLength1: 2, transitionHistoryLength2: 21, transitionHistoryLength3: 210, 

26- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ha, tagit, ett ,.. ]

B0Lemma: ha, B0POS: AUX, B0Token: ha, B1Lemma: ta, B1POS: VERB, B1Token: tagit, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 021, 

27- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ha]   B= [tagit, ett, slutgiltigt ,.. ]

B0Lemma: ta, B0POS: VERB, B0Token: tagit, B1Lemma: en, B1POS: DET, B1Token: ett, S0B0Distance: 1, S0B0Lemma: ha_ta, S0B0LemmaPOS: ha_VERB, S0B0POS: AUX_VERB, S0B0POSLemma: AUX_ta, S0B0Token: ha_tagit, S0B1Lemma: ha_en, S0B1LemmaPOS: ha_DET, S0B1POS: AUX_DET, S0B1POSLemma: AUX_en, S0B1Token: ha_ett, S0Lemma: ha, S0POS: AUX, S0Token: ha, ha_isGouvernedBy_ta: true, ha_isGouvernedBy_ta_aux: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

28- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [tagit, ett, slutgiltigt ,.. ]

B0Lemma: ta, B0POS: VERB, B0Token: tagit, B1Lemma: en, B1POS: DET, B1Token: ett, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

29- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [tagit]   B= [ett, slutgiltigt, beslut ,.. ]

B0Lemma: en, B0POS: DET, B0Token: ett, B1Lemma: slutgiltig, B1POS: ADJ, B1Token: slutgiltigt, S0B0Distance: 1, S0B0Lemma: ta_en, S0B0LemmaPOS: ta_DET, S0B0POS: VERB_DET, S0B0POSLemma: VERB_en, S0B0Token: tagit_ett, S0B1Lemma: ta_slutgiltig, S0B1LemmaPOS: ta_ADJ, S0B1POS: VERB_ADJ, S0B1POSLemma: VERB_slutgiltig, S0B1Token: tagit_slutgiltigt, S0Lemma: ta, S0POS: VERB, S0Token: tagit, hasRighDep_dobj: true, ta_beslut_hasRighDep_dobj: true, ta_hasRighDep_dobj: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

30- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [tagit, ett]   B= [slutgiltigt, beslut, . ,.. ]

B0Lemma: slutgiltig, B0POS: ADJ, B0Token: slutgiltigt, B1Lemma: beslut, B1POS: NOUN, B1Token: beslut, S0B0Distance: 1, S0B0Lemma: en_slutgiltig, S0B0LemmaPOS: en_ADJ, S0B0POS: DET_ADJ, S0B0POSLemma: DET_slutgiltig, S0B0Token: ett_slutgiltigt, S0B1Lemma: en_beslut, S0B1LemmaPOS: en_NOUN, S0B1POS: DET_NOUN, S0B1POSLemma: DET_beslut, S0B1Token: ett_beslut, S0Lemma: en, S0POS: DET, S0Token: ett, S1B0Lemma: ta_slutgiltig, S1B0LemmaPOS: ta_ADJ, S1B0POS: VERB_ADJ, S1B0POSLemma: VERB_slutgiltig, S1B0Token: tagit_slutgiltigt, S1Lemma: ta, S1POS: VERB, S1S0Lemma: ta_en, S1S0LemmaPOS: ta_DET, S1S0POS: VERB_DET, S1S0POSLemma: VERB_en, S1S0Token: tagit_ett, S1Token: tagit, en_isGouvernedBy_beslut: true, en_isGouvernedBy_beslut_det: true, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

31- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [tagit]   B= [slutgiltigt, beslut, . ,.. ]

B0Lemma: slutgiltig, B0POS: ADJ, B0Token: slutgiltigt, B1Lemma: beslut, B1POS: NOUN, B1Token: beslut, S0B0Distance: 2, S0B0Lemma: ta_slutgiltig, S0B0LemmaPOS: ta_ADJ, S0B0POS: VERB_ADJ, S0B0POSLemma: VERB_slutgiltig, S0B0Token: tagit_slutgiltigt, S0B1Lemma: ta_beslut, S0B1LemmaPOS: ta_NOUN, S0B1POS: VERB_NOUN, S0B1POSLemma: VERB_beslut, S0B1Token: tagit_beslut, S0Lemma: ta, S0POS: VERB, S0Token: tagit, hasRighDep_dobj: true, ta_beslut_hasRighDep_dobj: true, ta_hasRighDep_dobj: true, transitionHistoryLength1: 0, transitionHistoryLength2: 00, transitionHistoryLength3: 002, 

32- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [tagit, slutgiltigt]   B= [beslut, . ,.. ]

B0Lemma: beslut, B0POS: NOUN, B0Token: beslut, B1Lemma: ., B1POS: PUNCT, B1Token: ., S0B0Distance: 1, S0B0Lemma: slutgiltig_beslut, S0B0LemmaPOS: slutgiltig_NOUN, S0B0POS: ADJ_NOUN, S0B0POSLemma: ADJ_beslut, S0B0Token: slutgiltigt_beslut, S0B1Lemma: slutgiltig_., S0B1LemmaPOS: slutgiltig_PUNCT, S0B1POS: ADJ_PUNCT, S0B1POSLemma: ADJ_., S0B1Token: slutgiltigt_., S0Lemma: slutgiltig, S0POS: ADJ, S0Token: slutgiltigt, S1B0Lemma: ta_beslut, S1B0LemmaPOS: ta_NOUN, S1B0POS: VERB_NOUN, S1B0POSLemma: VERB_beslut, S1B0Token: tagit_beslut, S1Lemma: ta, S1POS: VERB, S1S0Lemma: ta_slutgiltig, S1S0LemmaPOS: ta_ADJ, S1S0POS: VERB_ADJ, S1S0POSLemma: VERB_slutgiltig, S1S0Token: tagit_slutgiltigt, S1Token: tagit, slutgiltig_isGouvernedBy_beslut: true, slutgiltig_isGouvernedBy_beslut_amod: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 200, 

33- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [tagit]   B= [beslut, . ,.. ]

B0Lemma: beslut, B0POS: NOUN, B0Token: beslut, B1Lemma: ., B1POS: PUNCT, B1Token: ., S0B0Distance: 3, S0B0Lemma: ta_beslut, S0B0LemmaPOS: ta_NOUN, S0B0POS: VERB_NOUN, S0B0POSLemma: VERB_beslut, S0B0Token: tagit_beslut, S0B1Lemma: ta_., S0B1LemmaPOS: ta_PUNCT, S0B1POS: VERB_PUNCT, S0B1POSLemma: VERB_., S0B1Token: tagit_., S0Lemma: ta, S0POS: VERB, S0Token: tagit, hasRighDep_dobj: true, ta_beslut_hasRighDep_dobj: true, ta_hasRighDep_dobj: true, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

34- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [tagit, beslut]   B= [.]

B0Lemma: ., B0POS: PUNCT, B0Token: ., S0B0Distance: 1, S0B0Lemma: beslut_., S0B0LemmaPOS: beslut_PUNCT, S0B0POS: NOUN_PUNCT, S0B0POSLemma: NOUN_., S0B0Token: beslut_., S0Lemma: beslut, S0POS: NOUN, S0Token: beslut, S1B0Lemma: ta_., S1B0LemmaPOS: ta_PUNCT, S1B0POS: VERB_PUNCT, S1B0POSLemma: VERB_., S1B0Token: tagit_., S1Lemma: ta, S1POS: VERB, S1S0Lemma: ta_beslut, S1S0LemmaPOS: ta_NOUN, S1S0POS: VERB_NOUN, S1S0POSLemma: VERB_beslut, S1S0Token: tagit_beslut, S1Token: tagit, SyntaxicRelation: +dobj, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

35- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[tagit, beslut]]   B= [.]

B0Lemma: ., B0POS: PUNCT, B0Token: ., S0B0Distance: 1, S0B0Lemma: ta_beslut_., S0B0LemmaPOS: ta_beslut_PUNCT, S0B0POS: VERB_NOUN_PUNCT, S0B0POSLemma: VERB_NOUN_., S0B0Token: tagit_beslut_., S0Lemma: ta_beslut, S0POS: VERB_NOUN, S0Token: tagit_beslut, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

36- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [.]

B0Lemma: ., B0POS: PUNCT, B0Token: ., transitionHistoryLength1: 1, transitionHistoryLength2: 10, transitionHistoryLength3: 102, 

37- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [ ]

S0Lemma: ., S0POS: PUNCT, S0Token: ., transitionHistoryLength1: 2, transitionHistoryLength2: 21, transitionHistoryLength3: 210, 

38- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

## Sentence No. 34 - 
Exempelvis erbjöd sig Ryssland , som ofta bromsat västmakternas planer på militära ingripanden , i går att hjälpa till med att transportera franska soldater till Mali . 
### Existing MWEs: 
1- **erbjöd sig** (IReflV)
2- **hjälpa till** (VPC)



0- &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Exempelvis, erbjöd, sig ,.. ]

B0Lemma: exempelvis, B0POS: ADV, B0Token: Exempelvis, B1Lemma: erbjuda, B1POS: VERB, B1Token: erbjöd, 

1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Exempelvis]   B= [erbjöd, sig, Ryssland ,.. ]

B0Lemma: erbjuda, B0POS: VERB, B0Token: erbjöd, B1Lemma: sig, B1POS: PRON, B1Token: sig, S0B0Distance: 1, S0B0Lemma: exempelvis_erbjuda, S0B0LemmaPOS: exempelvis_VERB, S0B0POS: ADV_VERB, S0B0POSLemma: ADV_erbjuda, S0B0Token: Exempelvis_erbjöd, S0B1Lemma: exempelvis_sig, S0B1LemmaPOS: exempelvis_PRON, S0B1POS: ADV_PRON, S0B1POSLemma: ADV_sig, S0B1Token: Exempelvis_sig, S0Lemma: exempelvis, S0POS: ADV, S0Token: Exempelvis, exempelvis_isGouvernedBy_erbjuda: true, exempelvis_isGouvernedBy_erbjuda_advmod: true, 

2- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [erbjöd, sig, Ryssland ,.. ]

B0Lemma: erbjuda, B0POS: VERB, B0Token: erbjöd, B1Lemma: sig, B1POS: PRON, B1Token: sig, transitionHistoryLength1: 0, 

3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [erbjöd]   B= [sig, Ryssland, , ,.. ]

B0Lemma: sig, B0POS: PRON, B0Token: sig, B1Lemma: Ryssland, B1POS: PROPN, B1Token: Ryssland, S0B0Distance: 1, S0B0Lemma: erbjuda_sig, S0B0LemmaPOS: erbjuda_PRON, S0B0POS: VERB_PRON, S0B0POSLemma: VERB_sig, S0B0Token: erbjöd_sig, S0B1Lemma: erbjuda_Ryssland, S0B1LemmaPOS: erbjuda_PROPN, S0B1POS: VERB_PROPN, S0B1POSLemma: VERB_Ryssland, S0B1Token: erbjöd_Ryssland, S0Lemma: erbjuda, S0POS: VERB, S0Token: erbjöd, transitionHistoryLength1: 2, transitionHistoryLength2: 20, 

4- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [erbjöd, sig]   B= [Ryssland, ,, som ,.. ]

B0Lemma: Ryssland, B0POS: PROPN, B0Token: Ryssland, B1Lemma: ,, B1POS: PUNCT, B1Token: ,, S0B0Distance: 1, S0B0Lemma: sig_Ryssland, S0B0LemmaPOS: sig_PROPN, S0B0POS: PRON_PROPN, S0B0POSLemma: PRON_Ryssland, S0B0Token: sig_Ryssland, S0B1Lemma: sig_,, S0B1LemmaPOS: sig_PUNCT, S0B1POS: PRON_PUNCT, S0B1POSLemma: PRON_,, S0B1Token: sig_,, S0Lemma: sig, S0POS: PRON, S0Token: sig, S1B0Lemma: erbjuda_Ryssland, S1B0LemmaPOS: erbjuda_PROPN, S1B0POS: VERB_PROPN, S1B0POSLemma: VERB_Ryssland, S1B0Token: erbjöd_Ryssland, S1Lemma: erbjuda, S1POS: VERB, S1S0Lemma: erbjuda_sig, S1S0LemmaPOS: erbjuda_PRON, S1S0POS: VERB_PRON, S1S0POSLemma: VERB_sig, S1S0Token: erbjöd_sig, S1Token: erbjöd, SyntaxicRelation: +dobj, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

5- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[erbjöd, sig]]   B= [Ryssland, ,, som ,.. ]

B0Lemma: Ryssland, B0POS: PROPN, B0Token: Ryssland, B1Lemma: ,, B1POS: PUNCT, B1Token: ,, S0B0Distance: 1, S0B0Lemma: erbjuda_sig_Ryssland, S0B0LemmaPOS: erbjuda_sig_PROPN, S0B0POS: VERB_PRON_PROPN, S0B0POSLemma: VERB_PRON_Ryssland, S0B0Token: erbjöd_sig_Ryssland, S0B1Lemma: erbjuda_sig_,, S0B1LemmaPOS: erbjuda_sig_PUNCT, S0B1POS: VERB_PRON_PUNCT, S0B1POSLemma: VERB_PRON_,, S0B1Token: erbjöd_sig_,, S0Lemma: erbjuda_sig, S0POS: VERB_PRON, S0Token: erbjöd_sig, transitionHistoryLength1: 0, transitionHistoryLength2: 00, transitionHistoryLength3: 002, 

6- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Ryssland, ,, som ,.. ]

B0Lemma: Ryssland, B0POS: PROPN, B0Token: Ryssland, B1Lemma: ,, B1POS: PUNCT, B1Token: ,, transitionHistoryLength1: 1, transitionHistoryLength2: 10, transitionHistoryLength3: 100, 

7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Ryssland]   B= [,, som, ofta ,.. ]

B0Lemma: ,, B0POS: PUNCT, B0Token: ,, B1Lemma: som, B1POS: PRON, B1Token: som, Ryssland_,_hasRighDep_punct: true, Ryssland_bromsa_hasRighDep_acl:relcl: true, Ryssland_hasRighDep_acl:relcl: true, Ryssland_hasRighDep_punct: true, S0B0Distance: 1, S0B0Lemma: Ryssland_,, S0B0LemmaPOS: Ryssland_PUNCT, S0B0POS: PROPN_PUNCT, S0B0POSLemma: PROPN_,, S0B0Token: Ryssland_,, S0B1Lemma: Ryssland_som, S0B1LemmaPOS: Ryssland_PRON, S0B1POS: PROPN_PRON, S0B1POSLemma: PROPN_som, S0B1Token: Ryssland_som, S0Lemma: Ryssland, S0POS: PROPN, S0Token: Ryssland, hasRighDep_acl:relcl: true, hasRighDep_punct: true, transitionHistoryLength1: 2, transitionHistoryLength2: 21, transitionHistoryLength3: 210, 

8- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, som, ofta ,.. ]

B0Lemma: ,, B0POS: PUNCT, B0Token: ,, B1Lemma: som, B1POS: PRON, B1Token: som, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 021, 

9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [som, ofta, bromsat ,.. ]

B0Lemma: som, B0POS: PRON, B0Token: som, B1Lemma: ofta, B1POS: ADV, B1Token: ofta, S0B0Distance: 1, S0B0Lemma: ,_som, S0B0LemmaPOS: ,_PRON, S0B0POS: PUNCT_PRON, S0B0POSLemma: PUNCT_som, S0B0Token: ,_som, S0B1Lemma: ,_ofta, S0B1LemmaPOS: ,_ADV, S0B1POS: PUNCT_ADV, S0B1POSLemma: PUNCT_ofta, S0B1Token: ,_ofta, S0Lemma: ,, S0POS: PUNCT, S0Token: ,, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

10- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [som, ofta, bromsat ,.. ]

B0Lemma: som, B0POS: PRON, B0Token: som, B1Lemma: ofta, B1POS: ADV, B1Token: ofta, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [som]   B= [ofta, bromsat, västmakternas ,.. ]

B0Lemma: ofta, B0POS: ADV, B0Token: ofta, B1Lemma: bromsa, B1POS: VERB, B1Token: bromsat, S0B0Distance: 1, S0B0Lemma: som_ofta, S0B0LemmaPOS: som_ADV, S0B0POS: PRON_ADV, S0B0POSLemma: PRON_ofta, S0B0Token: som_ofta, S0B1Lemma: som_bromsa, S0B1LemmaPOS: som_VERB, S0B1POS: PRON_VERB, S0B1POSLemma: PRON_bromsa, S0B1Token: som_bromsat, S0Lemma: som, S0POS: PRON, S0Token: som, som_isGouvernedBy_bromsa: true, som_isGouvernedBy_bromsa_nsubj: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

12- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ofta, bromsat, västmakternas ,.. ]

B0Lemma: ofta, B0POS: ADV, B0Token: ofta, B1Lemma: bromsa, B1POS: VERB, B1Token: bromsat, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ofta]   B= [bromsat, västmakternas, planer ,.. ]

B0Lemma: bromsa, B0POS: VERB, B0Token: bromsat, B1Lemma: västmakt, B1POS: NOUN, B1Token: västmakternas, S0B0Distance: 1, S0B0Lemma: ofta_bromsa, S0B0LemmaPOS: ofta_VERB, S0B0POS: ADV_VERB, S0B0POSLemma: ADV_bromsa, S0B0Token: ofta_bromsat, S0B1Lemma: ofta_västmakt, S0B1LemmaPOS: ofta_NOUN, S0B1POS: ADV_NOUN, S0B1POSLemma: ADV_västmakt, S0B1Token: ofta_västmakternas, S0Lemma: ofta, S0POS: ADV, S0Token: ofta, ofta_isGouvernedBy_bromsa: true, ofta_isGouvernedBy_bromsa_advmod: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

14- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [bromsat, västmakternas, planer ,.. ]

B0Lemma: bromsa, B0POS: VERB, B0Token: bromsat, B1Lemma: västmakt, B1POS: NOUN, B1Token: västmakternas, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [bromsat]   B= [västmakternas, planer, på ,.. ]

B0Lemma: västmakt, B0POS: NOUN, B0Token: västmakternas, B1Lemma: plana, B1POS: NOUN, B1Token: planer, S0B0Distance: 1, S0B0Lemma: bromsa_västmakt, S0B0LemmaPOS: bromsa_NOUN, S0B0POS: VERB_NOUN, S0B0POSLemma: VERB_västmakt, S0B0Token: bromsat_västmakternas, S0B1Lemma: bromsa_plana, S0B1LemmaPOS: bromsa_NOUN, S0B1POS: VERB_NOUN, S0B1POSLemma: VERB_plana, S0B1Token: bromsat_planer, S0Lemma: bromsa, S0POS: VERB, S0Token: bromsat, bromsa_hasRighDep_dobj: true, bromsa_plana_hasRighDep_dobj: true, hasRighDep_dobj: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

16- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [västmakternas, planer, på ,.. ]

B0Lemma: västmakt, B0POS: NOUN, B0Token: västmakternas, B1Lemma: plana, B1POS: NOUN, B1Token: planer, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [västmakternas]   B= [planer, på, militära ,.. ]

B0Lemma: plana, B0POS: NOUN, B0Token: planer, B1Lemma: på, B1POS: ADP, B1Token: på, S0B0Distance: 1, S0B0Lemma: västmakt_plana, S0B0LemmaPOS: västmakt_NOUN, S0B0POS: NOUN_NOUN, S0B0POSLemma: NOUN_plana, S0B0Token: västmakternas_planer, S0B1Lemma: västmakt_på, S0B1LemmaPOS: västmakt_ADP, S0B1POS: NOUN_ADP, S0B1POSLemma: NOUN_på, S0B1Token: västmakternas_på, S0Lemma: västmakt, S0POS: NOUN, S0Token: västmakternas, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, västmakt_isGouvernedBy_plana: true, västmakt_isGouvernedBy_plana_nmod:poss: true, 

18- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [planer, på, militära ,.. ]

B0Lemma: plana, B0POS: NOUN, B0Token: planer, B1Lemma: på, B1POS: ADP, B1Token: på, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [planer]   B= [på, militära, ingripanden ,.. ]

B0Lemma: på, B0POS: ADP, B0Token: på, B1Lemma: militär, B1POS: ADJ, B1Token: militära, S0B0Distance: 1, S0B0Lemma: plana_på, S0B0LemmaPOS: plana_ADP, S0B0POS: NOUN_ADP, S0B0POSLemma: NOUN_på, S0B0Token: planer_på, S0B1Lemma: plana_militär, S0B1LemmaPOS: plana_ADJ, S0B1POS: NOUN_ADJ, S0B1POSLemma: NOUN_militär, S0B1Token: planer_militära, S0Lemma: plana, S0POS: NOUN, S0Token: planer, hasRighDep_nmod: true, plana_hasRighDep_nmod: true, plana_ingripande_hasRighDep_nmod: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

20- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [på, militära, ingripanden ,.. ]

B0Lemma: på, B0POS: ADP, B0Token: på, B1Lemma: militär, B1POS: ADJ, B1Token: militära, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [på]   B= [militära, ingripanden, , ,.. ]

B0Lemma: militär, B0POS: ADJ, B0Token: militära, B1Lemma: ingripande, B1POS: NOUN, B1Token: ingripanden, S0B0Distance: 1, S0B0Lemma: på_militär, S0B0LemmaPOS: på_ADJ, S0B0POS: ADP_ADJ, S0B0POSLemma: ADP_militär, S0B0Token: på_militära, S0B1Lemma: på_ingripande, S0B1LemmaPOS: på_NOUN, S0B1POS: ADP_NOUN, S0B1POSLemma: ADP_ingripande, S0B1Token: på_ingripanden, S0Lemma: på, S0POS: ADP, S0Token: på, på_isGouvernedBy_ingripande: true, på_isGouvernedBy_ingripande_case: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

22- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [militära, ingripanden, , ,.. ]

B0Lemma: militär, B0POS: ADJ, B0Token: militära, B1Lemma: ingripande, B1POS: NOUN, B1Token: ingripanden, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

23- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [militära]   B= [ingripanden, ,, i ,.. ]

B0Lemma: ingripande, B0POS: NOUN, B0Token: ingripanden, B1Lemma: ,, B1POS: PUNCT, B1Token: ,, S0B0Distance: 1, S0B0Lemma: militär_ingripande, S0B0LemmaPOS: militär_NOUN, S0B0POS: ADJ_NOUN, S0B0POSLemma: ADJ_ingripande, S0B0Token: militära_ingripanden, S0B1Lemma: militär_,, S0B1LemmaPOS: militär_PUNCT, S0B1POS: ADJ_PUNCT, S0B1POSLemma: ADJ_,, S0B1Token: militära_,, S0Lemma: militär, S0POS: ADJ, S0Token: militära, militär_isGouvernedBy_ingripande: true, militär_isGouvernedBy_ingripande_amod: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

24- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ingripanden, ,, i ,.. ]

B0Lemma: ingripande, B0POS: NOUN, B0Token: ingripanden, B1Lemma: ,, B1POS: PUNCT, B1Token: ,, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

25- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ingripanden]   B= [,, i, går ,.. ]

B0Lemma: ,, B0POS: PUNCT, B0Token: ,, B1Lemma: i, B1POS: ADP, B1Token: i, S0B0Distance: 1, S0B0Lemma: ingripande_,, S0B0LemmaPOS: ingripande_PUNCT, S0B0POS: NOUN_PUNCT, S0B0POSLemma: NOUN_,, S0B0Token: ingripanden_,, S0B1Lemma: ingripande_i, S0B1LemmaPOS: ingripande_ADP, S0B1POS: NOUN_ADP, S0B1POSLemma: NOUN_i, S0B1Token: ingripanden_i, S0Lemma: ingripande, S0POS: NOUN, S0Token: ingripanden, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

26- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, i, går ,.. ]

B0Lemma: ,, B0POS: PUNCT, B0Token: ,, B1Lemma: i, B1POS: ADP, B1Token: i, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

27- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [i, går, att ,.. ]

B0Lemma: i, B0POS: ADP, B0Token: i, B1Lemma: gå, B1POS: VERB, B1Token: går, S0B0Distance: 1, S0B0Lemma: ,_i, S0B0LemmaPOS: ,_ADP, S0B0POS: PUNCT_ADP, S0B0POSLemma: PUNCT_i, S0B0Token: ,_i, S0B1Lemma: ,_gå, S0B1LemmaPOS: ,_VERB, S0B1POS: PUNCT_VERB, S0B1POSLemma: PUNCT_gå, S0B1Token: ,_går, S0Lemma: ,, S0POS: PUNCT, S0Token: ,, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

28- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [i, går, att ,.. ]

B0Lemma: i, B0POS: ADP, B0Token: i, B1Lemma: gå, B1POS: VERB, B1Token: går, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

29- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [i]   B= [går, att, hjälpa ,.. ]

B0Lemma: gå, B0POS: VERB, B0Token: går, B1Lemma: att, B1POS: PART, B1Token: att, S0B0Distance: 1, S0B0Lemma: i_gå, S0B0LemmaPOS: i_VERB, S0B0POS: ADP_VERB, S0B0POSLemma: ADP_gå, S0B0Token: i_går, S0B1Lemma: i_att, S0B1LemmaPOS: i_PART, S0B1POS: ADP_PART, S0B1POSLemma: ADP_att, S0B1Token: i_att, S0Lemma: i, S0POS: ADP, S0Token: i, i_isGouvernedBy_gå: true, i_isGouvernedBy_gå_case: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

30- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [går, att, hjälpa ,.. ]

B0Lemma: gå, B0POS: VERB, B0Token: går, B1Lemma: att, B1POS: PART, B1Token: att, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

31- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [går]   B= [att, hjälpa, till ,.. ]

B0Lemma: att, B0POS: PART, B0Token: att, B1Lemma: hjälpa, B1POS: VERB, B1Token: hjälpa, S0B0Distance: 1, S0B0Lemma: gå_att, S0B0LemmaPOS: gå_PART, S0B0POS: VERB_PART, S0B0POSLemma: VERB_att, S0B0Token: går_att, S0B1Lemma: gå_hjälpa, S0B1LemmaPOS: gå_VERB, S0B1POS: VERB_VERB, S0B1POSLemma: VERB_hjälpa, S0B1Token: går_hjälpa, S0Lemma: gå, S0POS: VERB, S0Token: går, gå_hasRighDep_xcomp: true, gå_hjälpa_hasRighDep_xcomp: true, hasRighDep_xcomp: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

32- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [att, hjälpa, till ,.. ]

B0Lemma: att, B0POS: PART, B0Token: att, B1Lemma: hjälpa, B1POS: VERB, B1Token: hjälpa, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

33- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [att]   B= [hjälpa, till, med ,.. ]

B0Lemma: hjälpa, B0POS: VERB, B0Token: hjälpa, B1Lemma: till, B1POS: ADP, B1Token: till, S0B0Distance: 1, S0B0Lemma: att_hjälpa, S0B0LemmaPOS: att_VERB, S0B0POS: PART_VERB, S0B0POSLemma: PART_hjälpa, S0B0Token: att_hjälpa, S0B1Lemma: att_till, S0B1LemmaPOS: att_ADP, S0B1POS: PART_ADP, S0B1POSLemma: PART_till, S0B1Token: att_till, S0Lemma: att, S0POS: PART, S0Token: att, att_isGouvernedBy_hjälpa: true, att_isGouvernedBy_hjälpa_mark: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

34- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [hjälpa, till, med ,.. ]

B0Lemma: hjälpa, B0POS: VERB, B0Token: hjälpa, B1Lemma: till, B1POS: ADP, B1Token: till, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

35- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [hjälpa]   B= [till, med, att ,.. ]

B0Lemma: till, B0POS: ADP, B0Token: till, B1Lemma: med, B1POS: ADP, B1Token: med, S0B0Distance: 1, S0B0Lemma: hjälpa_till, S0B0LemmaPOS: hjälpa_ADP, S0B0POS: VERB_ADP, S0B0POSLemma: VERB_till, S0B0Token: hjälpa_till, S0B1Lemma: hjälpa_med, S0B1LemmaPOS: hjälpa_ADP, S0B1POS: VERB_ADP, S0B1POSLemma: VERB_med, S0B1Token: hjälpa_med, S0Lemma: hjälpa, S0POS: VERB, S0Token: hjälpa, hasRighDep_advcl: true, hasRighDep_compound:prt: true, hjälpa_hasRighDep_advcl: true, hjälpa_hasRighDep_compound:prt: true, hjälpa_till_hasRighDep_compound:prt: true, hjälpa_transportera_hasRighDep_advcl: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

36- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [hjälpa, till]   B= [med, att, transportera ,.. ]

B0Lemma: med, B0POS: ADP, B0Token: med, B1Lemma: att, B1POS: PART, B1Token: att, S0B0Distance: 1, S0B0Lemma: till_med, S0B0LemmaPOS: till_ADP, S0B0POS: ADP_ADP, S0B0POSLemma: ADP_med, S0B0Token: till_med, S0B1Lemma: till_att, S0B1LemmaPOS: till_PART, S0B1POS: ADP_PART, S0B1POSLemma: ADP_att, S0B1Token: till_att, S0Lemma: till, S0POS: ADP, S0Token: till, S1B0Lemma: hjälpa_med, S1B0LemmaPOS: hjälpa_ADP, S1B0POS: VERB_ADP, S1B0POSLemma: VERB_med, S1B0Token: hjälpa_med, S1Lemma: hjälpa, S1POS: VERB, S1S0Lemma: hjälpa_till, S1S0LemmaPOS: hjälpa_ADP, S1S0POS: VERB_ADP, S1S0POSLemma: VERB_till, S1S0Token: hjälpa_till, S1Token: hjälpa, SyntaxicRelation: +compound:prt, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

37- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[hjälpa, till]]   B= [med, att, transportera ,.. ]

B0Lemma: med, B0POS: ADP, B0Token: med, B1Lemma: att, B1POS: PART, B1Token: att, S0B0Distance: 1, S0B0Lemma: hjälpa_till_med, S0B0LemmaPOS: hjälpa_till_ADP, S0B0POS: VERB_ADP_ADP, S0B0POSLemma: VERB_ADP_med, S0B0Token: hjälpa_till_med, S0B1Lemma: hjälpa_till_att, S0B1LemmaPOS: hjälpa_till_PART, S0B1POS: VERB_ADP_PART, S0B1POSLemma: VERB_ADP_att, S0B1Token: hjälpa_till_att, S0Lemma: hjälpa_till, S0POS: VERB_ADP, S0Token: hjälpa_till, transitionHistoryLength1: 0, transitionHistoryLength2: 00, transitionHistoryLength3: 002, 

38- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [med, att, transportera ,.. ]

B0Lemma: med, B0POS: ADP, B0Token: med, B1Lemma: att, B1POS: PART, B1Token: att, transitionHistoryLength1: 1, transitionHistoryLength2: 10, transitionHistoryLength3: 100, 

39- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [med]   B= [att, transportera, franska ,.. ]

B0Lemma: att, B0POS: PART, B0Token: att, B1Lemma: transportera, B1POS: VERB, B1Token: transportera, S0B0Distance: 1, S0B0Lemma: med_att, S0B0LemmaPOS: med_PART, S0B0POS: ADP_PART, S0B0POSLemma: ADP_att, S0B0Token: med_att, S0B1Lemma: med_transportera, S0B1LemmaPOS: med_VERB, S0B1POS: ADP_VERB, S0B1POSLemma: ADP_transportera, S0B1Token: med_transportera, S0Lemma: med, S0POS: ADP, S0Token: med, med_isGouvernedBy_transportera: true, med_isGouvernedBy_transportera_case: true, transitionHistoryLength1: 2, transitionHistoryLength2: 21, transitionHistoryLength3: 210, 

40- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [att, transportera, franska ,.. ]

B0Lemma: att, B0POS: PART, B0Token: att, B1Lemma: transportera, B1POS: VERB, B1Token: transportera, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 021, 

41- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [att]   B= [transportera, franska, soldater ,.. ]

B0Lemma: transportera, B0POS: VERB, B0Token: transportera, B1Lemma: fransk, B1POS: ADJ, B1Token: franska, S0B0Distance: 1, S0B0Lemma: att_transportera, S0B0LemmaPOS: att_VERB, S0B0POS: PART_VERB, S0B0POSLemma: PART_transportera, S0B0Token: att_transportera, S0B1Lemma: att_fransk, S0B1LemmaPOS: att_ADJ, S0B1POS: PART_ADJ, S0B1POSLemma: PART_fransk, S0B1Token: att_franska, S0Lemma: att, S0POS: PART, S0Token: att, att_isGouvernedBy_transportera: true, att_isGouvernedBy_transportera_mark: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

42- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [transportera, franska, soldater ,.. ]

B0Lemma: transportera, B0POS: VERB, B0Token: transportera, B1Lemma: fransk, B1POS: ADJ, B1Token: franska, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

43- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [transportera]   B= [franska, soldater, till ,.. ]

B0Lemma: fransk, B0POS: ADJ, B0Token: franska, B1Lemma: soldat, B1POS: NOUN, B1Token: soldater, S0B0Distance: 1, S0B0Lemma: transportera_fransk, S0B0LemmaPOS: transportera_ADJ, S0B0POS: VERB_ADJ, S0B0POSLemma: VERB_fransk, S0B0Token: transportera_franska, S0B1Lemma: transportera_soldat, S0B1LemmaPOS: transportera_NOUN, S0B1POS: VERB_NOUN, S0B1POSLemma: VERB_soldat, S0B1Token: transportera_soldater, S0Lemma: transportera, S0POS: VERB, S0Token: transportera, hasRighDep_dobj: true, hasRighDep_nmod: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, transportera_Malus_hasRighDep_nmod: true, transportera_hasRighDep_dobj: true, transportera_hasRighDep_nmod: true, transportera_soldat_hasRighDep_dobj: true, 

44- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [franska, soldater, till ,.. ]

B0Lemma: fransk, B0POS: ADJ, B0Token: franska, B1Lemma: soldat, B1POS: NOUN, B1Token: soldater, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

45- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [franska]   B= [soldater, till, Mali ,.. ]

B0Lemma: soldat, B0POS: NOUN, B0Token: soldater, B1Lemma: till, B1POS: ADP, B1Token: till, S0B0Distance: 1, S0B0Lemma: fransk_soldat, S0B0LemmaPOS: fransk_NOUN, S0B0POS: ADJ_NOUN, S0B0POSLemma: ADJ_soldat, S0B0Token: franska_soldater, S0B1Lemma: fransk_till, S0B1LemmaPOS: fransk_ADP, S0B1POS: ADJ_ADP, S0B1POSLemma: ADJ_till, S0B1Token: franska_till, S0Lemma: fransk, S0POS: ADJ, S0Token: franska, fransk_isGouvernedBy_soldat: true, fransk_isGouvernedBy_soldat_amod: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

46- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [soldater, till, Mali ,.. ]

B0Lemma: soldat, B0POS: NOUN, B0Token: soldater, B1Lemma: till, B1POS: ADP, B1Token: till, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

47- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [soldater]   B= [till, Mali, . ,.. ]

B0Lemma: till, B0POS: ADP, B0Token: till, B1Lemma: Malus, B1POS: PROPN, B1Token: Mali, S0B0Distance: 1, S0B0Lemma: soldat_till, S0B0LemmaPOS: soldat_ADP, S0B0POS: NOUN_ADP, S0B0POSLemma: NOUN_till, S0B0Token: soldater_till, S0B1Lemma: soldat_Malus, S0B1LemmaPOS: soldat_PROPN, S0B1POS: NOUN_PROPN, S0B1POSLemma: NOUN_Malus, S0B1Token: soldater_Mali, S0Lemma: soldat, S0POS: NOUN, S0Token: soldater, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

48- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [till, Mali, . ,.. ]

B0Lemma: till, B0POS: ADP, B0Token: till, B1Lemma: Malus, B1POS: PROPN, B1Token: Mali, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

49- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [till]   B= [Mali, . ,.. ]

B0Lemma: Malus, B0POS: PROPN, B0Token: Mali, B1Lemma: ., B1POS: PUNCT, B1Token: ., S0B0Distance: 1, S0B0Lemma: till_Malus, S0B0LemmaPOS: till_PROPN, S0B0POS: ADP_PROPN, S0B0POSLemma: ADP_Malus, S0B0Token: till_Mali, S0B1Lemma: till_., S0B1LemmaPOS: till_PUNCT, S0B1POS: ADP_PUNCT, S0B1POSLemma: ADP_., S0B1Token: till_., S0Lemma: till, S0POS: ADP, S0Token: till, till_isGouvernedBy_Malus: true, till_isGouvernedBy_Malus_case: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

50- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Mali, . ,.. ]

B0Lemma: Malus, B0POS: PROPN, B0Token: Mali, B1Lemma: ., B1POS: PUNCT, B1Token: ., transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

51- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Mali]   B= [.]

B0Lemma: ., B0POS: PUNCT, B0Token: ., S0B0Distance: 1, S0B0Lemma: Malus_., S0B0LemmaPOS: Malus_PUNCT, S0B0POS: PROPN_PUNCT, S0B0POSLemma: PROPN_., S0B0Token: Mali_., S0Lemma: Malus, S0POS: PROPN, S0Token: Mali, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

52- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [.]

B0Lemma: ., B0POS: PUNCT, B0Token: ., transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

53- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [ ]

S0Lemma: ., S0POS: PUNCT, S0Token: ., transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

54- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

## Sentence No. 61 - 
Det avspeglar sig också i den säsongsbetonade menyn som vi borrade oss ner i medan vi smååt av den goda brödkorgen med malt- , surdegs- och knäckebröd , och ett rört smör därtill . 
### Existing MWEs: 
1- **avspeglar sig** (IReflV)
2- **borrade oss ner** (ID)



0- &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Det, avspeglar, sig ,.. ]

B0Lemma: den, B0POS: PRON, B0Token: Det, B1Lemma: avspegla, B1POS: VERB, B1Token: avspeglar, 

1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Det]   B= [avspeglar, sig, också ,.. ]

B0Lemma: avspegla, B0POS: VERB, B0Token: avspeglar, B1Lemma: sig, B1POS: PRON, B1Token: sig, S0B0Distance: 1, S0B0Lemma: den_avspegla, S0B0LemmaPOS: den_VERB, S0B0POS: PRON_VERB, S0B0POSLemma: PRON_avspegla, S0B0Token: Det_avspeglar, S0B1Lemma: den_sig, S0B1LemmaPOS: den_PRON, S0B1POS: PRON_PRON, S0B1POSLemma: PRON_sig, S0B1Token: Det_sig, S0Lemma: den, S0POS: PRON, S0Token: Det, den_isGouvernedBy_avspegla: true, den_isGouvernedBy_avspegla_nsubj: true, 

2- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [avspeglar, sig, också ,.. ]

B0Lemma: avspegla, B0POS: VERB, B0Token: avspeglar, B1Lemma: sig, B1POS: PRON, B1Token: sig, transitionHistoryLength1: 0, 

3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [avspeglar]   B= [sig, också, i ,.. ]

B0Lemma: sig, B0POS: PRON, B0Token: sig, B1Lemma: också, B1POS: ADV, B1Token: också, S0B0Distance: 1, S0B0Lemma: avspegla_sig, S0B0LemmaPOS: avspegla_PRON, S0B0POS: VERB_PRON, S0B0POSLemma: VERB_sig, S0B0Token: avspeglar_sig, S0B1Lemma: avspegla_också, S0B1LemmaPOS: avspegla_ADV, S0B1POS: VERB_ADV, S0B1POSLemma: VERB_också, S0B1Token: avspeglar_också, S0Lemma: avspegla, S0POS: VERB, S0Token: avspeglar, transitionHistoryLength1: 2, transitionHistoryLength2: 20, 

4- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [avspeglar, sig]   B= [också, i, den ,.. ]

B0Lemma: också, B0POS: ADV, B0Token: också, B1Lemma: i, B1POS: ADP, B1Token: i, S0B0Distance: 1, S0B0Lemma: sig_också, S0B0LemmaPOS: sig_ADV, S0B0POS: PRON_ADV, S0B0POSLemma: PRON_också, S0B0Token: sig_också, S0B1Lemma: sig_i, S0B1LemmaPOS: sig_ADP, S0B1POS: PRON_ADP, S0B1POSLemma: PRON_i, S0B1Token: sig_i, S0Lemma: sig, S0POS: PRON, S0Token: sig, S1B0Lemma: avspegla_också, S1B0LemmaPOS: avspegla_ADV, S1B0POS: VERB_ADV, S1B0POSLemma: VERB_också, S1B0Token: avspeglar_också, S1Lemma: avspegla, S1POS: VERB, S1S0Lemma: avspegla_sig, S1S0LemmaPOS: avspegla_PRON, S1S0POS: VERB_PRON, S1S0POSLemma: VERB_sig, S1S0Token: avspeglar_sig, S1Token: avspeglar, SyntaxicRelation: +dobj, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

5- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[avspeglar, sig]]   B= [också, i, den ,.. ]

B0Lemma: också, B0POS: ADV, B0Token: också, B1Lemma: i, B1POS: ADP, B1Token: i, S0B0Distance: 1, S0B0Lemma: avspegla_sig_också, S0B0LemmaPOS: avspegla_sig_ADV, S0B0POS: VERB_PRON_ADV, S0B0POSLemma: VERB_PRON_också, S0B0Token: avspeglar_sig_också, S0B1Lemma: avspegla_sig_i, S0B1LemmaPOS: avspegla_sig_ADP, S0B1POS: VERB_PRON_ADP, S0B1POSLemma: VERB_PRON_i, S0B1Token: avspeglar_sig_i, S0Lemma: avspegla_sig, S0POS: VERB_PRON, S0Token: avspeglar_sig, transitionHistoryLength1: 0, transitionHistoryLength2: 00, transitionHistoryLength3: 002, 

6- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [också, i, den ,.. ]

B0Lemma: också, B0POS: ADV, B0Token: också, B1Lemma: i, B1POS: ADP, B1Token: i, transitionHistoryLength1: 1, transitionHistoryLength2: 10, transitionHistoryLength3: 100, 

7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [också]   B= [i, den, säsongsbetonade ,.. ]

B0Lemma: i, B0POS: ADP, B0Token: i, B1Lemma: en, B1POS: DET, B1Token: den, S0B0Distance: 1, S0B0Lemma: också_i, S0B0LemmaPOS: också_ADP, S0B0POS: ADV_ADP, S0B0POSLemma: ADV_i, S0B0Token: också_i, S0B1Lemma: också_en, S0B1LemmaPOS: också_DET, S0B1POS: ADV_DET, S0B1POSLemma: ADV_en, S0B1Token: också_den, S0Lemma: också, S0POS: ADV, S0Token: också, transitionHistoryLength1: 2, transitionHistoryLength2: 21, transitionHistoryLength3: 210, 

8- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [i, den, säsongsbetonade ,.. ]

B0Lemma: i, B0POS: ADP, B0Token: i, B1Lemma: en, B1POS: DET, B1Token: den, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 021, 

9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [i]   B= [den, säsongsbetonade, menyn ,.. ]

B0Lemma: en, B0POS: DET, B0Token: den, B1Lemma: säsongsbetonad, B1POS: ADJ, B1Token: säsongsbetonade, S0B0Distance: 1, S0B0Lemma: i_en, S0B0LemmaPOS: i_DET, S0B0POS: ADP_DET, S0B0POSLemma: ADP_en, S0B0Token: i_den, S0B1Lemma: i_säsongsbetonad, S0B1LemmaPOS: i_ADJ, S0B1POS: ADP_ADJ, S0B1POSLemma: ADP_säsongsbetonad, S0B1Token: i_säsongsbetonade, S0Lemma: i, S0POS: ADP, S0Token: i, i_isGouvernedBy_menyn: true, i_isGouvernedBy_menyn_case: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

10- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [den, säsongsbetonade, menyn ,.. ]

B0Lemma: en, B0POS: DET, B0Token: den, B1Lemma: säsongsbetonad, B1POS: ADJ, B1Token: säsongsbetonade, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [den]   B= [säsongsbetonade, menyn, som ,.. ]

B0Lemma: säsongsbetonad, B0POS: ADJ, B0Token: säsongsbetonade, B1Lemma: menyn, B1POS: NOUN, B1Token: menyn, S0B0Distance: 1, S0B0Lemma: en_säsongsbetonad, S0B0LemmaPOS: en_ADJ, S0B0POS: DET_ADJ, S0B0POSLemma: DET_säsongsbetonad, S0B0Token: den_säsongsbetonade, S0B1Lemma: en_menyn, S0B1LemmaPOS: en_NOUN, S0B1POS: DET_NOUN, S0B1POSLemma: DET_menyn, S0B1Token: den_menyn, S0Lemma: en, S0POS: DET, S0Token: den, en_isGouvernedBy_menyn: true, en_isGouvernedBy_menyn_det: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

12- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [säsongsbetonade, menyn, som ,.. ]

B0Lemma: säsongsbetonad, B0POS: ADJ, B0Token: säsongsbetonade, B1Lemma: menyn, B1POS: NOUN, B1Token: menyn, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [säsongsbetonade]   B= [menyn, som, vi ,.. ]

B0Lemma: menyn, B0POS: NOUN, B0Token: menyn, B1Lemma: som, B1POS: PRON, B1Token: som, S0B0Distance: 1, S0B0Lemma: säsongsbetonad_menyn, S0B0LemmaPOS: säsongsbetonad_NOUN, S0B0POS: ADJ_NOUN, S0B0POSLemma: ADJ_menyn, S0B0Token: säsongsbetonade_menyn, S0B1Lemma: säsongsbetonad_som, S0B1LemmaPOS: säsongsbetonad_PRON, S0B1POS: ADJ_PRON, S0B1POSLemma: ADJ_som, S0B1Token: säsongsbetonade_som, S0Lemma: säsongsbetonad, S0POS: ADJ, S0Token: säsongsbetonade, säsongsbetonad_isGouvernedBy_menyn: true, säsongsbetonad_isGouvernedBy_menyn_amod: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

14- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [menyn, som, vi ,.. ]

B0Lemma: menyn, B0POS: NOUN, B0Token: menyn, B1Lemma: som, B1POS: PRON, B1Token: som, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [menyn]   B= [som, vi, borrade ,.. ]

B0Lemma: som, B0POS: PRON, B0Token: som, B1Lemma: vi, B1POS: PRON, B1Token: vi, S0B0Distance: 1, S0B0Lemma: menyn_som, S0B0LemmaPOS: menyn_PRON, S0B0POS: NOUN_PRON, S0B0POSLemma: NOUN_som, S0B0Token: menyn_som, S0B1Lemma: menyn_vi, S0B1LemmaPOS: menyn_PRON, S0B1POS: NOUN_PRON, S0B1POSLemma: NOUN_vi, S0B1Token: menyn_vi, S0Lemma: menyn, S0POS: NOUN, S0Token: menyn, hasRighDep_acl:relcl: true, menyn_borra_hasRighDep_acl:relcl: true, menyn_hasRighDep_acl:relcl: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

16- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [som, vi, borrade ,.. ]

B0Lemma: som, B0POS: PRON, B0Token: som, B1Lemma: vi, B1POS: PRON, B1Token: vi, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [som]   B= [vi, borrade, oss ,.. ]

B0Lemma: vi, B0POS: PRON, B0Token: vi, B1Lemma: borra, B1POS: VERB, B1Token: borrade, S0B0Distance: 1, S0B0Lemma: som_vi, S0B0LemmaPOS: som_PRON, S0B0POS: PRON_PRON, S0B0POSLemma: PRON_vi, S0B0Token: som_vi, S0B1Lemma: som_borra, S0B1LemmaPOS: som_VERB, S0B1POS: PRON_VERB, S0B1POSLemma: PRON_borra, S0B1Token: som_borrade, S0Lemma: som, S0POS: PRON, S0Token: som, som_isGouvernedBy_borra: true, som_isGouvernedBy_borra_dobj: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

18- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [vi, borrade, oss ,.. ]

B0Lemma: vi, B0POS: PRON, B0Token: vi, B1Lemma: borra, B1POS: VERB, B1Token: borrade, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [vi]   B= [borrade, oss, ner ,.. ]

B0Lemma: borra, B0POS: VERB, B0Token: borrade, B1Lemma: vi, B1POS: PRON, B1Token: oss, S0B0Distance: 1, S0B0Lemma: vi_borra, S0B0LemmaPOS: vi_VERB, S0B0POS: PRON_VERB, S0B0POSLemma: PRON_borra, S0B0Token: vi_borrade, S0B1Lemma: vi_vi, S0B1LemmaPOS: vi_PRON, S0B1POS: PRON_PRON, S0B1POSLemma: PRON_vi, S0B1Token: vi_oss, S0Lemma: vi, S0POS: PRON, S0Token: vi, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, vi_isGouvernedBy_borra: true, vi_isGouvernedBy_borra_nsubj: true, 

20- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [borrade, oss, ner ,.. ]

B0Lemma: borra, B0POS: VERB, B0Token: borrade, B1Lemma: vi, B1POS: PRON, B1Token: oss, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [borrade]   B= [oss, ner, i ,.. ]

B0Lemma: vi, B0POS: PRON, B0Token: oss, B1Lemma: ner, B1POS: ADV, B1Token: ner, S0B0Distance: 1, S0B0Lemma: borra_vi, S0B0LemmaPOS: borra_PRON, S0B0POS: VERB_PRON, S0B0POSLemma: VERB_vi, S0B0Token: borrade_oss, S0B1Lemma: borra_ner, S0B1LemmaPOS: borra_ADV, S0B1POS: VERB_ADV, S0B1POSLemma: VERB_ner, S0B1Token: borrade_ner, S0Lemma: borra, S0POS: VERB, S0Token: borrade, borra_hasRighDep_advcl: true, borra_hasRighDep_compound:prt: true, borra_hasRighDep_dobj: true, borra_ner_hasRighDep_compound:prt: true, borra_smååta_hasRighDep_advcl: true, borra_vi_hasRighDep_dobj: true, hasRighDep_advcl: true, hasRighDep_compound:prt: true, hasRighDep_dobj: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

22- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [borrade, oss]   B= [ner, i, medan ,.. ]

B0Lemma: ner, B0POS: ADV, B0Token: ner, B1Lemma: i, B1POS: ADP, B1Token: i, S0B0Distance: 1, S0B0Lemma: vi_ner, S0B0LemmaPOS: vi_ADV, S0B0POS: PRON_ADV, S0B0POSLemma: PRON_ner, S0B0Token: oss_ner, S0B1Lemma: vi_i, S0B1LemmaPOS: vi_ADP, S0B1POS: PRON_ADP, S0B1POSLemma: PRON_i, S0B1Token: oss_i, S0Lemma: vi, S0POS: PRON, S0Token: oss, S1B0Lemma: borra_ner, S1B0LemmaPOS: borra_ADV, S1B0POS: VERB_ADV, S1B0POSLemma: VERB_ner, S1B0Token: borrade_ner, S1Lemma: borra, S1POS: VERB, S1S0Lemma: borra_vi, S1S0LemmaPOS: borra_PRON, S1S0POS: VERB_PRON, S1S0POSLemma: VERB_vi, S1S0Token: borrade_oss, S1Token: borrade, SyntaxicRelation: +dobj, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

23- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [borrade, oss, ner]   B= [i, medan, vi ,.. ]

B0Lemma: i, B0POS: ADP, B0Token: i, B1Lemma: medan, B1POS: SCONJ, B1Token: medan, S0B0Distance: 1, S0B0Lemma: ner_i, S0B0LemmaPOS: ner_ADP, S0B0POS: ADV_ADP, S0B0POSLemma: ADV_i, S0B0Token: ner_i, S0B1Lemma: ner_medan, S0B1LemmaPOS: ner_SCONJ, S0B1POS: ADV_SCONJ, S0B1POSLemma: ADV_medan, S0B1Token: ner_medan, S0Lemma: ner, S0POS: ADV, S0Token: ner, S1B0Lemma: vi_i, S1B0LemmaPOS: vi_ADP, S1B0POS: PRON_ADP, S1B0POSLemma: PRON_i, S1B0Token: oss_i, S1Lemma: vi, S1POS: PRON, S1S0Lemma: vi_ner, S1S0LemmaPOS: vi_ADV, S1S0POS: PRON_ADV, S1S0POSLemma: PRON_ner, S1S0Token: oss_ner, S1Token: oss, transitionHistoryLength1: 0, transitionHistoryLength2: 00, transitionHistoryLength3: 002, 

24- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [borrade, [oss, ner]]   B= [i, medan, vi ,.. ]

B0Lemma: i, B0POS: ADP, B0Token: i, B1Lemma: medan, B1POS: SCONJ, B1Token: medan, S0B0Distance: 1, S0B0Lemma: vi_ner_i, S0B0LemmaPOS: vi_ner_ADP, S0B0POS: PRON_ADV_ADP, S0B0POSLemma: PRON_ADV_i, S0B0Token: oss_ner_i, S0B1Lemma: vi_ner_medan, S0B1LemmaPOS: vi_ner_SCONJ, S0B1POS: PRON_ADV_SCONJ, S0B1POSLemma: PRON_ADV_medan, S0B1Token: oss_ner_medan, S0Lemma: vi_ner, S0POS: PRON_ADV, S0Token: oss_ner, S1B0Lemma: borra_i, S1B0LemmaPOS: borra_ADP, S1B0POS: VERB_ADP, S1B0POSLemma: VERB_i, S1B0Token: borrade_i, S1Lemma: borra, S1POS: VERB, S1S0Lemma: borra_vi_ner, S1S0LemmaPOS: borra_PRON_ADV, S1S0POS: VERB_PRON_ADV, S1S0POSLemma: VERB_vi_ner, S1S0Token: borrade_oss_ner, S1Token: borrade, transitionHistoryLength1: 0, transitionHistoryLength2: 00, transitionHistoryLength3: 000, 

25- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[borrade, [oss, ner]]]   B= [i, medan, vi ,.. ]

B0Lemma: i, B0POS: ADP, B0Token: i, B1Lemma: medan, B1POS: SCONJ, B1Token: medan, S0B0Distance: 1, S0B0Lemma: borra_vi_ner_i, S0B0LemmaPOS: borra_vi_ner_ADP, S0B0POS: VERB_PRON_ADV_ADP, S0B0POSLemma: VERB_PRON_ADV_i, S0B0Token: borrade_oss_ner_i, S0B1Lemma: borra_vi_ner_medan, S0B1LemmaPOS: borra_vi_ner_SCONJ, S0B1POS: VERB_PRON_ADV_SCONJ, S0B1POSLemma: VERB_PRON_ADV_medan, S0B1Token: borrade_oss_ner_medan, S0Lemma: borra_vi_ner, S0POS: VERB_PRON_ADV, S0Token: borrade_oss_ner, transitionHistoryLength1: 1, transitionHistoryLength2: 10, transitionHistoryLength3: 100, 

26- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [i, medan, vi ,.. ]

B0Lemma: i, B0POS: ADP, B0Token: i, B1Lemma: medan, B1POS: SCONJ, B1Token: medan, transitionHistoryLength1: 1, transitionHistoryLength2: 11, transitionHistoryLength3: 110, 

27- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [i]   B= [medan, vi, smååt ,.. ]

B0Lemma: medan, B0POS: SCONJ, B0Token: medan, B1Lemma: vi, B1POS: PRON, B1Token: vi, S0B0Distance: 1, S0B0Lemma: i_medan, S0B0LemmaPOS: i_SCONJ, S0B0POS: ADP_SCONJ, S0B0POSLemma: ADP_medan, S0B0Token: i_medan, S0B1Lemma: i_vi, S0B1LemmaPOS: i_PRON, S0B1POS: ADP_PRON, S0B1POSLemma: ADP_vi, S0B1Token: i_vi, S0Lemma: i, S0POS: ADP, S0Token: i, i_isGouvernedBy_smååta: true, i_isGouvernedBy_smååta_case: true, transitionHistoryLength1: 2, transitionHistoryLength2: 21, transitionHistoryLength3: 211, 

28- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [medan, vi, smååt ,.. ]

B0Lemma: medan, B0POS: SCONJ, B0Token: medan, B1Lemma: vi, B1POS: PRON, B1Token: vi, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 021, 

29- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [medan]   B= [vi, smååt, av ,.. ]

B0Lemma: vi, B0POS: PRON, B0Token: vi, B1Lemma: smååta, B1POS: VERB, B1Token: smååt, S0B0Distance: 1, S0B0Lemma: medan_vi, S0B0LemmaPOS: medan_PRON, S0B0POS: SCONJ_PRON, S0B0POSLemma: SCONJ_vi, S0B0Token: medan_vi, S0B1Lemma: medan_smååta, S0B1LemmaPOS: medan_VERB, S0B1POS: SCONJ_VERB, S0B1POSLemma: SCONJ_smååta, S0B1Token: medan_smååt, S0Lemma: medan, S0POS: SCONJ, S0Token: medan, medan_isGouvernedBy_smååta: true, medan_isGouvernedBy_smååta_mark: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

30- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [vi, smååt, av ,.. ]

B0Lemma: vi, B0POS: PRON, B0Token: vi, B1Lemma: smååta, B1POS: VERB, B1Token: smååt, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

31- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [vi]   B= [smååt, av, den ,.. ]

B0Lemma: smååta, B0POS: VERB, B0Token: smååt, B1Lemma: av, B1POS: ADP, B1Token: av, S0B0Distance: 1, S0B0Lemma: vi_smååta, S0B0LemmaPOS: vi_VERB, S0B0POS: PRON_VERB, S0B0POSLemma: PRON_smååta, S0B0Token: vi_smååt, S0B1Lemma: vi_av, S0B1LemmaPOS: vi_ADP, S0B1POS: PRON_ADP, S0B1POSLemma: PRON_av, S0B1Token: vi_av, S0Lemma: vi, S0POS: PRON, S0Token: vi, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, vi_isGouvernedBy_smååta: true, vi_isGouvernedBy_smååta_nsubj: true, 

32- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [smååt, av, den ,.. ]

B0Lemma: smååta, B0POS: VERB, B0Token: smååt, B1Lemma: av, B1POS: ADP, B1Token: av, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

33- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [smååt]   B= [av, den, goda ,.. ]

B0Lemma: av, B0POS: ADP, B0Token: av, B1Lemma: en, B1POS: DET, B1Token: den, S0B0Distance: 1, S0B0Lemma: smååta_av, S0B0LemmaPOS: smååta_ADP, S0B0POS: VERB_ADP, S0B0POSLemma: VERB_av, S0B0Token: smååt_av, S0B1Lemma: smååta_en, S0B1LemmaPOS: smååta_DET, S0B1POS: VERB_DET, S0B1POSLemma: VERB_en, S0B1Token: smååt_den, S0Lemma: smååta, S0POS: VERB, S0Token: smååt, hasRighDep_nmod: true, smååta_brödkorg_hasRighDep_nmod: true, smååta_hasRighDep_nmod: true, smååta_malta_hasRighDep_nmod: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

34- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [av, den, goda ,.. ]

B0Lemma: av, B0POS: ADP, B0Token: av, B1Lemma: en, B1POS: DET, B1Token: den, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

35- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [av]   B= [den, goda, brödkorgen ,.. ]

B0Lemma: en, B0POS: DET, B0Token: den, B1Lemma: god, B1POS: ADJ, B1Token: goda, S0B0Distance: 1, S0B0Lemma: av_en, S0B0LemmaPOS: av_DET, S0B0POS: ADP_DET, S0B0POSLemma: ADP_en, S0B0Token: av_den, S0B1Lemma: av_god, S0B1LemmaPOS: av_ADJ, S0B1POS: ADP_ADJ, S0B1POSLemma: ADP_god, S0B1Token: av_goda, S0Lemma: av, S0POS: ADP, S0Token: av, av_isGouvernedBy_brödkorg: true, av_isGouvernedBy_brödkorg_case: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

36- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [den, goda, brödkorgen ,.. ]

B0Lemma: en, B0POS: DET, B0Token: den, B1Lemma: god, B1POS: ADJ, B1Token: goda, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

37- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [den]   B= [goda, brödkorgen, med ,.. ]

B0Lemma: god, B0POS: ADJ, B0Token: goda, B1Lemma: brödkorg, B1POS: NOUN, B1Token: brödkorgen, S0B0Distance: 1, S0B0Lemma: en_god, S0B0LemmaPOS: en_ADJ, S0B0POS: DET_ADJ, S0B0POSLemma: DET_god, S0B0Token: den_goda, S0B1Lemma: en_brödkorg, S0B1LemmaPOS: en_NOUN, S0B1POS: DET_NOUN, S0B1POSLemma: DET_brödkorg, S0B1Token: den_brödkorgen, S0Lemma: en, S0POS: DET, S0Token: den, en_isGouvernedBy_brödkorg: true, en_isGouvernedBy_brödkorg_det: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

38- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [goda, brödkorgen, med ,.. ]

B0Lemma: god, B0POS: ADJ, B0Token: goda, B1Lemma: brödkorg, B1POS: NOUN, B1Token: brödkorgen, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

39- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [goda]   B= [brödkorgen, med, malt- ,.. ]

B0Lemma: brödkorg, B0POS: NOUN, B0Token: brödkorgen, B1Lemma: med, B1POS: ADP, B1Token: med, S0B0Distance: 1, S0B0Lemma: god_brödkorg, S0B0LemmaPOS: god_NOUN, S0B0POS: ADJ_NOUN, S0B0POSLemma: ADJ_brödkorg, S0B0Token: goda_brödkorgen, S0B1Lemma: god_med, S0B1LemmaPOS: god_ADP, S0B1POS: ADJ_ADP, S0B1POSLemma: ADJ_med, S0B1Token: goda_med, S0Lemma: god, S0POS: ADJ, S0Token: goda, god_isGouvernedBy_brödkorg: true, god_isGouvernedBy_brödkorg_amod: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

40- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [brödkorgen, med, malt- ,.. ]

B0Lemma: brödkorg, B0POS: NOUN, B0Token: brödkorgen, B1Lemma: med, B1POS: ADP, B1Token: med, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

41- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [brödkorgen]   B= [med, malt-, , ,.. ]

B0Lemma: med, B0POS: ADP, B0Token: med, B1Lemma: malta, B1POS: NOUN, B1Token: malt-, S0B0Distance: 1, S0B0Lemma: brödkorg_med, S0B0LemmaPOS: brödkorg_ADP, S0B0POS: NOUN_ADP, S0B0POSLemma: NOUN_med, S0B0Token: brödkorgen_med, S0B1Lemma: brödkorg_malta, S0B1LemmaPOS: brödkorg_NOUN, S0B1POS: NOUN_NOUN, S0B1POSLemma: NOUN_malta, S0B1Token: brödkorgen_malt-, S0Lemma: brödkorg, S0POS: NOUN, S0Token: brödkorgen, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

42- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [med, malt-, , ,.. ]

B0Lemma: med, B0POS: ADP, B0Token: med, B1Lemma: malta, B1POS: NOUN, B1Token: malt-, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

43- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [med]   B= [malt-, ,, surdegs- ,.. ]

B0Lemma: malta, B0POS: NOUN, B0Token: malt-, B1Lemma: ,, B1POS: PUNCT, B1Token: ,, S0B0Distance: 1, S0B0Lemma: med_malta, S0B0LemmaPOS: med_NOUN, S0B0POS: ADP_NOUN, S0B0POSLemma: ADP_malta, S0B0Token: med_malt-, S0B1Lemma: med_,, S0B1LemmaPOS: med_PUNCT, S0B1POS: ADP_PUNCT, S0B1POSLemma: ADP_,, S0B1Token: med_,, S0Lemma: med, S0POS: ADP, S0Token: med, med_isGouvernedBy_malta: true, med_isGouvernedBy_malta_case: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

44- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [malt-, ,, surdegs- ,.. ]

B0Lemma: malta, B0POS: NOUN, B0Token: malt-, B1Lemma: ,, B1POS: PUNCT, B1Token: ,, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

45- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [malt-]   B= [,, surdegs-, och ,.. ]

B0Lemma: ,, B0POS: PUNCT, B0Token: ,, B1Lemma: surdeg, B1POS: NOUN, B1Token: surdegs-, S0B0Distance: 1, S0B0Lemma: malta_,, S0B0LemmaPOS: malta_PUNCT, S0B0POS: NOUN_PUNCT, S0B0POSLemma: NOUN_,, S0B0Token: malt-_,, S0B1Lemma: malta_surdeg, S0B1LemmaPOS: malta_NOUN, S0B1POS: NOUN_NOUN, S0B1POSLemma: NOUN_surdeg, S0B1Token: malt-_surdegs-, S0Lemma: malta, S0POS: NOUN, S0Token: malt-, hasRighDep_cc: true, hasRighDep_conj: true, hasRighDep_punct: true, malta_,_hasRighDep_punct: true, malta_hasRighDep_cc: true, malta_hasRighDep_conj: true, malta_hasRighDep_punct: true, malta_knäckebröd_hasRighDep_conj: true, malta_och_hasRighDep_cc: true, malta_surdeg_hasRighDep_conj: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

46- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, surdegs-, och ,.. ]

B0Lemma: ,, B0POS: PUNCT, B0Token: ,, B1Lemma: surdeg, B1POS: NOUN, B1Token: surdegs-, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

47- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [surdegs-, och, knäckebröd ,.. ]

B0Lemma: surdeg, B0POS: NOUN, B0Token: surdegs-, B1Lemma: och, B1POS: CONJ, B1Token: och, S0B0Distance: 1, S0B0Lemma: ,_surdeg, S0B0LemmaPOS: ,_NOUN, S0B0POS: PUNCT_NOUN, S0B0POSLemma: PUNCT_surdeg, S0B0Token: ,_surdegs-, S0B1Lemma: ,_och, S0B1LemmaPOS: ,_CONJ, S0B1POS: PUNCT_CONJ, S0B1POSLemma: PUNCT_och, S0B1Token: ,_och, S0Lemma: ,, S0POS: PUNCT, S0Token: ,, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

48- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [surdegs-, och, knäckebröd ,.. ]

B0Lemma: surdeg, B0POS: NOUN, B0Token: surdegs-, B1Lemma: och, B1POS: CONJ, B1Token: och, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

49- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [surdegs-]   B= [och, knäckebröd, , ,.. ]

B0Lemma: och, B0POS: CONJ, B0Token: och, B1Lemma: knäckebröd, B1POS: NOUN, B1Token: knäckebröd, S0B0Distance: 1, S0B0Lemma: surdeg_och, S0B0LemmaPOS: surdeg_CONJ, S0B0POS: NOUN_CONJ, S0B0POSLemma: NOUN_och, S0B0Token: surdegs-_och, S0B1Lemma: surdeg_knäckebröd, S0B1LemmaPOS: surdeg_NOUN, S0B1POS: NOUN_NOUN, S0B1POSLemma: NOUN_knäckebröd, S0B1Token: surdegs-_knäckebröd, S0Lemma: surdeg, S0POS: NOUN, S0Token: surdegs-, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

50- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [och, knäckebröd, , ,.. ]

B0Lemma: och, B0POS: CONJ, B0Token: och, B1Lemma: knäckebröd, B1POS: NOUN, B1Token: knäckebröd, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

51- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [och]   B= [knäckebröd, ,, och ,.. ]

B0Lemma: knäckebröd, B0POS: NOUN, B0Token: knäckebröd, B1Lemma: ,, B1POS: PUNCT, B1Token: ,, S0B0Distance: 1, S0B0Lemma: och_knäckebröd, S0B0LemmaPOS: och_NOUN, S0B0POS: CONJ_NOUN, S0B0POSLemma: CONJ_knäckebröd, S0B0Token: och_knäckebröd, S0B1Lemma: och_,, S0B1LemmaPOS: och_PUNCT, S0B1POS: CONJ_PUNCT, S0B1POSLemma: CONJ_,, S0B1Token: och_,, S0Lemma: och, S0POS: CONJ, S0Token: och, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

52- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [knäckebröd, ,, och ,.. ]

B0Lemma: knäckebröd, B0POS: NOUN, B0Token: knäckebröd, B1Lemma: ,, B1POS: PUNCT, B1Token: ,, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

53- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [knäckebröd]   B= [,, och, ett ,.. ]

B0Lemma: ,, B0POS: PUNCT, B0Token: ,, B1Lemma: och, B1POS: CONJ, B1Token: och, S0B0Distance: 1, S0B0Lemma: knäckebröd_,, S0B0LemmaPOS: knäckebröd_PUNCT, S0B0POS: NOUN_PUNCT, S0B0POSLemma: NOUN_,, S0B0Token: knäckebröd_,, S0B1Lemma: knäckebröd_och, S0B1LemmaPOS: knäckebröd_CONJ, S0B1POS: NOUN_CONJ, S0B1POSLemma: NOUN_och, S0B1Token: knäckebröd_och, S0Lemma: knäckebröd, S0POS: NOUN, S0Token: knäckebröd, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

54- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, och, ett ,.. ]

B0Lemma: ,, B0POS: PUNCT, B0Token: ,, B1Lemma: och, B1POS: CONJ, B1Token: och, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

55- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [och, ett, rört ,.. ]

B0Lemma: och, B0POS: CONJ, B0Token: och, B1Lemma: en, B1POS: DET, B1Token: ett, S0B0Distance: 1, S0B0Lemma: ,_och, S0B0LemmaPOS: ,_CONJ, S0B0POS: PUNCT_CONJ, S0B0POSLemma: PUNCT_och, S0B0Token: ,_och, S0B1Lemma: ,_en, S0B1LemmaPOS: ,_DET, S0B1POS: PUNCT_DET, S0B1POSLemma: PUNCT_en, S0B1Token: ,_ett, S0Lemma: ,, S0POS: PUNCT, S0Token: ,, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

56- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [och, ett, rört ,.. ]

B0Lemma: och, B0POS: CONJ, B0Token: och, B1Lemma: en, B1POS: DET, B1Token: ett, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

57- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [och]   B= [ett, rört, smör ,.. ]

B0Lemma: en, B0POS: DET, B0Token: ett, B1Lemma: röra, B1POS: ADJ, B1Token: rört, S0B0Distance: 1, S0B0Lemma: och_en, S0B0LemmaPOS: och_DET, S0B0POS: CONJ_DET, S0B0POSLemma: CONJ_en, S0B0Token: och_ett, S0B1Lemma: och_röra, S0B1LemmaPOS: och_ADJ, S0B1POS: CONJ_ADJ, S0B1POSLemma: CONJ_röra, S0B1Token: och_rört, S0Lemma: och, S0POS: CONJ, S0Token: och, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

58- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ett, rört, smör ,.. ]

B0Lemma: en, B0POS: DET, B0Token: ett, B1Lemma: röra, B1POS: ADJ, B1Token: rört, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

59- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ett]   B= [rört, smör, därtill ,.. ]

B0Lemma: röra, B0POS: ADJ, B0Token: rört, B1Lemma: smör, B1POS: NOUN, B1Token: smör, S0B0Distance: 1, S0B0Lemma: en_röra, S0B0LemmaPOS: en_ADJ, S0B0POS: DET_ADJ, S0B0POSLemma: DET_röra, S0B0Token: ett_rört, S0B1Lemma: en_smör, S0B1LemmaPOS: en_NOUN, S0B1POS: DET_NOUN, S0B1POSLemma: DET_smör, S0B1Token: ett_smör, S0Lemma: en, S0POS: DET, S0Token: ett, en_isGouvernedBy_smör: true, en_isGouvernedBy_smör_det: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

60- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [rört, smör, därtill ,.. ]

B0Lemma: röra, B0POS: ADJ, B0Token: rört, B1Lemma: smör, B1POS: NOUN, B1Token: smör, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

61- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [rört]   B= [smör, därtill, . ,.. ]

B0Lemma: smör, B0POS: NOUN, B0Token: smör, B1Lemma: därtill, B1POS: ADV, B1Token: därtill, S0B0Distance: 1, S0B0Lemma: röra_smör, S0B0LemmaPOS: röra_NOUN, S0B0POS: ADJ_NOUN, S0B0POSLemma: ADJ_smör, S0B0Token: rört_smör, S0B1Lemma: röra_därtill, S0B1LemmaPOS: röra_ADV, S0B1POS: ADJ_ADV, S0B1POSLemma: ADJ_därtill, S0B1Token: rört_därtill, S0Lemma: röra, S0POS: ADJ, S0Token: rört, röra_isGouvernedBy_smör: true, röra_isGouvernedBy_smör_amod: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

62- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [smör, därtill, . ,.. ]

B0Lemma: smör, B0POS: NOUN, B0Token: smör, B1Lemma: därtill, B1POS: ADV, B1Token: därtill, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

63- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [smör]   B= [därtill, . ,.. ]

B0Lemma: därtill, B0POS: ADV, B0Token: därtill, B1Lemma: ., B1POS: PUNCT, B1Token: ., S0B0Distance: 1, S0B0Lemma: smör_därtill, S0B0LemmaPOS: smör_ADV, S0B0POS: NOUN_ADV, S0B0POSLemma: NOUN_därtill, S0B0Token: smör_därtill, S0B1Lemma: smör_., S0B1LemmaPOS: smör_PUNCT, S0B1POS: NOUN_PUNCT, S0B1POSLemma: NOUN_., S0B1Token: smör_., S0Lemma: smör, S0POS: NOUN, S0Token: smör, hasRighDep_advmod: true, smör_därtill_hasRighDep_advmod: true, smör_hasRighDep_advmod: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

64- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [därtill, . ,.. ]

B0Lemma: därtill, B0POS: ADV, B0Token: därtill, B1Lemma: ., B1POS: PUNCT, B1Token: ., transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

65- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [därtill]   B= [.]

B0Lemma: ., B0POS: PUNCT, B0Token: ., S0B0Distance: 1, S0B0Lemma: därtill_., S0B0LemmaPOS: därtill_PUNCT, S0B0POS: ADV_PUNCT, S0B0POSLemma: ADV_., S0B0Token: därtill_., S0Lemma: därtill, S0POS: ADV, S0Token: därtill, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

66- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [.]

B0Lemma: ., B0POS: PUNCT, B0Token: ., transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

67- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [ ]

S0Lemma: ., S0POS: PUNCT, S0Token: ., transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

68- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

