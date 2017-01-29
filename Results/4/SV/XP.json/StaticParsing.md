## Sentence No. 67 - 
parkeringsplatserna ska vara trygga , av god kvalitet , ha väderskydd och det ska finnas möjligheter att låsa in eller fast cykeln . 
### Existing MWEs: 
1- **finnas möjligheter** (LVC)
2- **låsa in** (VPC)
3- **låsa fast** (VPC), Interleaving 



0- &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [parkeringsplatserna, ska, vara ,.. ]

B0Lemma: Parkeringsplats, B0POS: NN|UTR|PLU|DEF|NOM, B0Token: parkeringsplatserna, B1Lemma: skola, B1POS: VB|PRS|AKT, B1Token: ska, 

1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [parkeringsplatserna]   B= [ska, vara, trygga ,.. ]

B0Lemma: skola, B0POS: VB|PRS|AKT, B0Token: ska, B1IsInLexic: true, B1Lemma: vara, B1POS: VB|INF|AKT, B1Token: vara, Parkeringsplats_isGouvernedBy_trygg: true, Parkeringsplats_isGouvernedBy_trygg_nsubj: true, S0B0Distance: 1, S0B0Lemma: Parkeringsplats_skola, S0B0LemmaPOS: Parkeringsplats_VB|PRS|AKT, S0B0POS: NN|UTR|PLU|DEF|NOM_VB|PRS|AKT, S0B0POSLemma: NN|UTR|PLU|DEF|NOM_skola, S0B0Token: parkeringsplatserna_ska, S0B1Lemma: Parkeringsplats_vara, S0B1LemmaPOS: Parkeringsplats_VB|INF|AKT, S0B1POS: NN|UTR|PLU|DEF|NOM_VB|INF|AKT, S0B1POSLemma: NN|UTR|PLU|DEF|NOM_vara, S0B1Token: parkeringsplatserna_vara, S0B2Lemma: Parkeringsplats_trygg, S0B2LemmaPOS: Parkeringsplats_VB|INF|AKT, S0B2POS: NN|UTR|PLU|DEF|NOM_VB|INF|AKT, S0B2POSLemma: NN|UTR|PLU|DEF|NOM_trygg, S0B2Token: parkeringsplatserna_trygga, S0Lemma: Parkeringsplats, S0POS: NN|UTR|PLU|DEF|NOM, S0Token: parkeringsplatserna, 

2- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ska, vara, trygga ,.. ]

B0Lemma: skola, B0POS: VB|PRS|AKT, B0Token: ska, B1IsInLexic: true, B1Lemma: vara, B1POS: VB|INF|AKT, B1Token: vara, TransHistory1: 0, 

3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ska]   B= [vara, trygga, , ,.. ]

B0IsInLexic: true, B0Lemma: vara, B0POS: VB|INF|AKT, B0Token: vara, B1Lemma: trygg, B1POS: VB|INF|AKT, B1Token: trygga, S0B0Distance: 1, S0B0Lemma: skola_vara, S0B0LemmaPOS: skola_VB|INF|AKT, S0B0POS: VB|PRS|AKT_VB|INF|AKT, S0B0POSLemma: VB|PRS|AKT_vara, S0B0Token: ska_vara, S0B1Lemma: skola_trygg, S0B1LemmaPOS: skola_VB|INF|AKT, S0B1POS: VB|PRS|AKT_VB|INF|AKT, S0B1POSLemma: VB|PRS|AKT_trygg, S0B1Token: ska_trygga, S0B2Lemma: skola_,, S0B2LemmaPOS: skola_MID, S0B2POS: VB|PRS|AKT_MID, S0B2POSLemma: VB|PRS|AKT_,, S0B2Token: ska_,, S0Lemma: skola, S0POS: VB|PRS|AKT, S0Token: ska, TransHistory1: 2, TransHistory2: 20, skola_isGouvernedBy_trygg: true, skola_isGouvernedBy_trygg_aux: true, 

4- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [vara, trygga, , ,.. ]

B0IsInLexic: true, B0Lemma: vara, B0POS: VB|INF|AKT, B0Token: vara, B1Lemma: trygg, B1POS: VB|INF|AKT, B1Token: trygga, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [vara]   B= [trygga, ,, av ,.. ]

B0Lemma: trygg, B0POS: VB|INF|AKT, B0Token: trygga, B1Lemma: ,, B1POS: MID, B1Token: ,, S0B0Distance: 1, S0B0Lemma: vara_trygg, S0B0LemmaPOS: vara_VB|INF|AKT, S0B0POS: VB|INF|AKT_VB|INF|AKT, S0B0POSLemma: VB|INF|AKT_trygg, S0B0Token: vara_trygga, S0B1Lemma: vara_,, S0B1LemmaPOS: vara_MID, S0B1POS: VB|INF|AKT_MID, S0B1POSLemma: VB|INF|AKT_,, S0B1Token: vara_,, S0B2Lemma: vara_av, S0B2LemmaPOS: vara_PP, S0B2POS: VB|INF|AKT_PP, S0B2POSLemma: VB|INF|AKT_av, S0B2Token: vara_av, S0IsInLexic: true, S0Lemma: vara, S0POS: VB|INF|AKT, S0Token: vara, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, vara_isGouvernedBy_trygg: true, vara_isGouvernedBy_trygg_aux: true, 

6- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [trygga, ,, av ,.. ]

B0Lemma: trygg, B0POS: VB|INF|AKT, B0Token: trygga, B1Lemma: ,, B1POS: MID, B1Token: ,, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [trygga]   B= [,, av, god ,.. ]

B0Lemma: ,, B0POS: MID, B0Token: ,, B1IsInLexic: true, B1Lemma: av, B1POS: PP, B1Token: av, S0B0Distance: 1, S0B0Lemma: trygg_,, S0B0LemmaPOS: trygg_MID, S0B0POS: VB|INF|AKT_MID, S0B0POSLemma: VB|INF|AKT_,, S0B0Token: trygga_,, S0B1Lemma: trygg_av, S0B1LemmaPOS: trygg_PP, S0B1POS: VB|INF|AKT_PP, S0B1POSLemma: VB|INF|AKT_av, S0B1Token: trygga_av, S0B2Lemma: trygg_god, S0B2LemmaPOS: trygg_JJ|POS|UTR|SIN|IND|NOM, S0B2POS: VB|INF|AKT_JJ|POS|UTR|SIN|IND|NOM, S0B2POSLemma: VB|INF|AKT_god, S0B2Token: trygga_god, S0Lemma: trygg, S0POS: VB|INF|AKT, S0Token: trygga, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

8- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, av, god ,.. ]

B0Lemma: ,, B0POS: MID, B0Token: ,, B1IsInLexic: true, B1Lemma: av, B1POS: PP, B1Token: av, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [av, god, kvalitet ,.. ]

B0IsInLexic: true, B0Lemma: av, B0POS: PP, B0Token: av, B1Lemma: god, B1POS: JJ|POS|UTR|SIN|IND|NOM, B1Token: god, S0B0Distance: 1, S0B0Lemma: ,_av, S0B0LemmaPOS: ,_PP, S0B0POS: MID_PP, S0B0POSLemma: MID_av, S0B0Token: ,_av, S0B1Lemma: ,_god, S0B1LemmaPOS: ,_JJ|POS|UTR|SIN|IND|NOM, S0B1POS: MID_JJ|POS|UTR|SIN|IND|NOM, S0B1POSLemma: MID_god, S0B1Token: ,_god, S0B2Lemma: ,_kvalitet, S0B2LemmaPOS: ,_NN|UTR|SIN|IND|NOM, S0B2POS: MID_NN|UTR|SIN|IND|NOM, S0B2POSLemma: MID_kvalitet, S0B2Token: ,_kvalitet, S0Lemma: ,, S0POS: MID, S0Token: ,, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

10- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [av, god, kvalitet ,.. ]

B0IsInLexic: true, B0Lemma: av, B0POS: PP, B0Token: av, B1Lemma: god, B1POS: JJ|POS|UTR|SIN|IND|NOM, B1Token: god, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [av]   B= [god, kvalitet, , ,.. ]

B0Lemma: god, B0POS: JJ|POS|UTR|SIN|IND|NOM, B0Token: god, B1Lemma: kvalitet, B1POS: NN|UTR|SIN|IND|NOM, B1Token: kvalitet, S0B0Distance: 1, S0B0Lemma: av_god, S0B0LemmaPOS: av_JJ|POS|UTR|SIN|IND|NOM, S0B0POS: PP_JJ|POS|UTR|SIN|IND|NOM, S0B0POSLemma: PP_god, S0B0Token: av_god, S0B1Lemma: av_kvalitet, S0B1LemmaPOS: av_NN|UTR|SIN|IND|NOM, S0B1POS: PP_NN|UTR|SIN|IND|NOM, S0B1POSLemma: PP_kvalitet, S0B1Token: av_kvalitet, S0B2Lemma: av_,, S0B2LemmaPOS: av_MID, S0B2POS: PP_MID, S0B2POSLemma: PP_,, S0B2Token: av_,, S0IsInLexic: true, S0Lemma: av, S0POS: PP, S0Token: av, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, av_isGouvernedBy_kvalitet: true, av_isGouvernedBy_kvalitet_case: true, 

12- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [god, kvalitet, , ,.. ]

B0Lemma: god, B0POS: JJ|POS|UTR|SIN|IND|NOM, B0Token: god, B1Lemma: kvalitet, B1POS: NN|UTR|SIN|IND|NOM, B1Token: kvalitet, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [god]   B= [kvalitet, ,, ha ,.. ]

B0Lemma: kvalitet, B0POS: NN|UTR|SIN|IND|NOM, B0Token: kvalitet, B1Lemma: ,, B1POS: MID, B1Token: ,, S0B0Distance: 1, S0B0Lemma: god_kvalitet, S0B0LemmaPOS: god_NN|UTR|SIN|IND|NOM, S0B0POS: JJ|POS|UTR|SIN|IND|NOM_NN|UTR|SIN|IND|NOM, S0B0POSLemma: JJ|POS|UTR|SIN|IND|NOM_kvalitet, S0B0Token: god_kvalitet, S0B1Lemma: god_,, S0B1LemmaPOS: god_MID, S0B1POS: JJ|POS|UTR|SIN|IND|NOM_MID, S0B1POSLemma: JJ|POS|UTR|SIN|IND|NOM_,, S0B1Token: god_,, S0B2Lemma: god_ha, S0B2LemmaPOS: god_VB|INF|AKT, S0B2POS: JJ|POS|UTR|SIN|IND|NOM_VB|INF|AKT, S0B2POSLemma: JJ|POS|UTR|SIN|IND|NOM_ha, S0B2Token: god_ha, S0Lemma: god, S0POS: JJ|POS|UTR|SIN|IND|NOM, S0Token: god, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, god_isGouvernedBy_kvalitet: true, god_isGouvernedBy_kvalitet_amod: true, 

14- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [kvalitet, ,, ha ,.. ]

B0Lemma: kvalitet, B0POS: NN|UTR|SIN|IND|NOM, B0Token: kvalitet, B1Lemma: ,, B1POS: MID, B1Token: ,, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [kvalitet]   B= [,, ha, väderskydd ,.. ]

B0Lemma: ,, B0POS: MID, B0Token: ,, B1IsInLexic: true, B1Lemma: ha, B1POS: VB|INF|AKT, B1Token: ha, S0B0Distance: 1, S0B0Lemma: kvalitet_,, S0B0LemmaPOS: kvalitet_MID, S0B0POS: NN|UTR|SIN|IND|NOM_MID, S0B0POSLemma: NN|UTR|SIN|IND|NOM_,, S0B0Token: kvalitet_,, S0B1Lemma: kvalitet_ha, S0B1LemmaPOS: kvalitet_VB|INF|AKT, S0B1POS: NN|UTR|SIN|IND|NOM_VB|INF|AKT, S0B1POSLemma: NN|UTR|SIN|IND|NOM_ha, S0B1Token: kvalitet_ha, S0B2Lemma: kvalitet_väderskydd, S0B2LemmaPOS: kvalitet_NN|NEU|SIN|IND|NOM, S0B2POS: NN|UTR|SIN|IND|NOM_NN|NEU|SIN|IND|NOM, S0B2POSLemma: NN|UTR|SIN|IND|NOM_väderskydd, S0B2Token: kvalitet_väderskydd, S0Lemma: kvalitet, S0POS: NN|UTR|SIN|IND|NOM, S0Token: kvalitet, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, hasRighDep_punct: true, kvalitet_,_hasRighDep_punct: true, kvalitet_hasRighDep_punct: true, kvalitet_isGouvernedBy_ha: true, kvalitet_isGouvernedBy_ha_nmod: true, 

16- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, ha, väderskydd ,.. ]

B0Lemma: ,, B0POS: MID, B0Token: ,, B1IsInLexic: true, B1Lemma: ha, B1POS: VB|INF|AKT, B1Token: ha, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [ha, väderskydd, och ,.. ]

B0IsInLexic: true, B0Lemma: ha, B0POS: VB|INF|AKT, B0Token: ha, B1Lemma: väderskydd, B1POS: NN|NEU|SIN|IND|NOM, B1Token: väderskydd, S0B0Distance: 1, S0B0Lemma: ,_ha, S0B0LemmaPOS: ,_VB|INF|AKT, S0B0POS: MID_VB|INF|AKT, S0B0POSLemma: MID_ha, S0B0Token: ,_ha, S0B1Lemma: ,_väderskydd, S0B1LemmaPOS: ,_NN|NEU|SIN|IND|NOM, S0B1POS: MID_NN|NEU|SIN|IND|NOM, S0B1POSLemma: MID_väderskydd, S0B1Token: ,_väderskydd, S0B2Lemma: ,_och, S0B2LemmaPOS: ,_KN, S0B2POS: MID_KN, S0B2POSLemma: MID_och, S0B2Token: ,_och, S0Lemma: ,, S0POS: MID, S0Token: ,, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

18- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ha, väderskydd, och ,.. ]

B0IsInLexic: true, B0Lemma: ha, B0POS: VB|INF|AKT, B0Token: ha, B1Lemma: väderskydd, B1POS: NN|NEU|SIN|IND|NOM, B1Token: väderskydd, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ha]   B= [väderskydd, och, det ,.. ]

B0Lemma: väderskydd, B0POS: NN|NEU|SIN|IND|NOM, B0Token: väderskydd, B1Lemma: och, B1POS: KN, B1Token: och, S0B0Distance: 1, S0B0Lemma: ha_väderskydd, S0B0LemmaPOS: ha_NN|NEU|SIN|IND|NOM, S0B0POS: VB|INF|AKT_NN|NEU|SIN|IND|NOM, S0B0POSLemma: VB|INF|AKT_väderskydd, S0B0Token: ha_väderskydd, S0B1Lemma: ha_och, S0B1LemmaPOS: ha_KN, S0B1POS: VB|INF|AKT_KN, S0B1POSLemma: VB|INF|AKT_och, S0B1Token: ha_och, S0B2Lemma: ha_den, S0B2LemmaPOS: ha_PN|NEU|SIN|DEF|SUB/OBJ, S0B2POS: VB|INF|AKT_PN|NEU|SIN|DEF|SUB/OBJ, S0B2POSLemma: VB|INF|AKT_den, S0B2Token: ha_det, S0IsInLexic: true, S0Lemma: ha, S0POS: VB|INF|AKT, S0Token: ha, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, ha_hasRighDep_dobj: true, ha_väderskydd_hasRighDep_dobj: true, hasRighDep_dobj: true, 

20- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [väderskydd, och, det ,.. ]

B0Lemma: väderskydd, B0POS: NN|NEU|SIN|IND|NOM, B0Token: väderskydd, B1Lemma: och, B1POS: KN, B1Token: och, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [väderskydd]   B= [och, det, ska ,.. ]

B0Lemma: och, B0POS: KN, B0Token: och, B1Lemma: den, B1POS: PN|NEU|SIN|DEF|SUB/OBJ, B1Token: det, S0B0Distance: 1, S0B0Lemma: väderskydd_och, S0B0LemmaPOS: väderskydd_KN, S0B0POS: NN|NEU|SIN|IND|NOM_KN, S0B0POSLemma: NN|NEU|SIN|IND|NOM_och, S0B0Token: väderskydd_och, S0B1Lemma: väderskydd_den, S0B1LemmaPOS: väderskydd_PN|NEU|SIN|DEF|SUB/OBJ, S0B1POS: NN|NEU|SIN|IND|NOM_PN|NEU|SIN|DEF|SUB/OBJ, S0B1POSLemma: NN|NEU|SIN|IND|NOM_den, S0B1Token: väderskydd_det, S0B2Lemma: väderskydd_skola, S0B2LemmaPOS: väderskydd_VB|PRS|AKT, S0B2POS: NN|NEU|SIN|IND|NOM_VB|PRS|AKT, S0B2POSLemma: NN|NEU|SIN|IND|NOM_skola, S0B2Token: väderskydd_ska, S0Lemma: väderskydd, S0POS: NN|NEU|SIN|IND|NOM, S0Token: väderskydd, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

22- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [och, det, ska ,.. ]

B0Lemma: och, B0POS: KN, B0Token: och, B1Lemma: den, B1POS: PN|NEU|SIN|DEF|SUB/OBJ, B1Token: det, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

23- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [och]   B= [det, ska, finnas ,.. ]

B0Lemma: den, B0POS: PN|NEU|SIN|DEF|SUB/OBJ, B0Token: det, B1Lemma: skola, B1POS: VB|PRS|AKT, B1Token: ska, S0B0Distance: 1, S0B0Lemma: och_den, S0B0LemmaPOS: och_PN|NEU|SIN|DEF|SUB/OBJ, S0B0POS: KN_PN|NEU|SIN|DEF|SUB/OBJ, S0B0POSLemma: KN_den, S0B0Token: och_det, S0B1Lemma: och_skola, S0B1LemmaPOS: och_VB|PRS|AKT, S0B1POS: KN_VB|PRS|AKT, S0B1POSLemma: KN_skola, S0B1Token: och_ska, S0B2Lemma: och_finnas, S0B2LemmaPOS: och_VB|INF|SFO, S0B2POS: KN_VB|INF|SFO, S0B2POSLemma: KN_finnas, S0B2Token: och_finnas, S0Lemma: och, S0POS: KN, S0Token: och, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

24- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [det, ska, finnas ,.. ]

B0Lemma: den, B0POS: PN|NEU|SIN|DEF|SUB/OBJ, B0Token: det, B1Lemma: skola, B1POS: VB|PRS|AKT, B1Token: ska, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

25- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [det]   B= [ska, finnas, möjligheter ,.. ]

B0Lemma: skola, B0POS: VB|PRS|AKT, B0Token: ska, B1IsInLexic: true, B1Lemma: finnas, B1POS: VB|INF|SFO, B1Token: finnas, S0B0Distance: 1, S0B0Lemma: den_skola, S0B0LemmaPOS: den_VB|PRS|AKT, S0B0POS: PN|NEU|SIN|DEF|SUB/OBJ_VB|PRS|AKT, S0B0POSLemma: PN|NEU|SIN|DEF|SUB/OBJ_skola, S0B0Token: det_ska, S0B1Lemma: den_finnas, S0B1LemmaPOS: den_VB|INF|SFO, S0B1POS: PN|NEU|SIN|DEF|SUB/OBJ_VB|INF|SFO, S0B1POSLemma: PN|NEU|SIN|DEF|SUB/OBJ_finnas, S0B1Token: det_finnas, S0B2Lemma: den_möjlighet, S0B2LemmaPOS: den_NN|UTR|PLU|IND|NOM, S0B2POS: PN|NEU|SIN|DEF|SUB/OBJ_NN|UTR|PLU|IND|NOM, S0B2POSLemma: PN|NEU|SIN|DEF|SUB/OBJ_möjlighet, S0B2Token: det_möjligheter, S0Lemma: den, S0POS: PN|NEU|SIN|DEF|SUB/OBJ, S0Token: det, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, den_isGouvernedBy_finnas: true, den_isGouvernedBy_finnas_expl: true, 

26- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ska, finnas, möjligheter ,.. ]

B0Lemma: skola, B0POS: VB|PRS|AKT, B0Token: ska, B1IsInLexic: true, B1Lemma: finnas, B1POS: VB|INF|SFO, B1Token: finnas, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

27- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ska]   B= [finnas, möjligheter, att ,.. ]

B0IsInLexic: true, B0Lemma: finnas, B0POS: VB|INF|SFO, B0Token: finnas, B1IsInLexic: true, B1Lemma: möjlighet, B1POS: NN|UTR|PLU|IND|NOM, B1Token: möjligheter, S0B0Distance: 1, S0B0Lemma: skola_finnas, S0B0LemmaPOS: skola_VB|INF|SFO, S0B0POS: VB|PRS|AKT_VB|INF|SFO, S0B0POSLemma: VB|PRS|AKT_finnas, S0B0Token: ska_finnas, S0B1Lemma: skola_möjlighet, S0B1LemmaPOS: skola_NN|UTR|PLU|IND|NOM, S0B1POS: VB|PRS|AKT_NN|UTR|PLU|IND|NOM, S0B1POSLemma: VB|PRS|AKT_möjlighet, S0B1Token: ska_möjligheter, S0B2Lemma: skola_att, S0B2LemmaPOS: skola_IE, S0B2POS: VB|PRS|AKT_IE, S0B2POSLemma: VB|PRS|AKT_att, S0B2Token: ska_att, S0Lemma: skola, S0POS: VB|PRS|AKT, S0Token: ska, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, skola_isGouvernedBy_finnas: true, skola_isGouvernedBy_finnas_aux: true, 

28- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [finnas, möjligheter, att ,.. ]

B0IsInLexic: true, B0Lemma: finnas, B0POS: VB|INF|SFO, B0Token: finnas, B1IsInLexic: true, B1Lemma: möjlighet, B1POS: NN|UTR|PLU|IND|NOM, B1Token: möjligheter, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

29- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [finnas]   B= [möjligheter, att, låsa ,.. ]

B0IsInLexic: true, B0Lemma: möjlighet, B0POS: NN|UTR|PLU|IND|NOM, B0Token: möjligheter, B1Lemma: att, B1POS: IE, B1Token: att, S0B0Distance: 1, S0B0Lemma: finnas_möjlighet, S0B0LemmaPOS: finnas_NN|UTR|PLU|IND|NOM, S0B0POS: VB|INF|SFO_NN|UTR|PLU|IND|NOM, S0B0POSLemma: VB|INF|SFO_möjlighet, S0B0Token: finnas_möjligheter, S0B1Lemma: finnas_att, S0B1LemmaPOS: finnas_IE, S0B1POS: VB|INF|SFO_IE, S0B1POSLemma: VB|INF|SFO_att, S0B1Token: finnas_att, S0B2Lemma: finnas_låsa, S0B2LemmaPOS: finnas_VB|INF|AKT, S0B2POS: VB|INF|SFO_VB|INF|AKT, S0B2POSLemma: VB|INF|SFO_låsa, S0B2Token: finnas_låsa, S0IsInLexic: true, S0Lemma: finnas, S0POS: VB|INF|SFO, S0Token: finnas, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, finnas_hasRighDep_nsubj: true, finnas_möjlighet_hasRighDep_nsubj: true, hasRighDep_nsubj: true, 

30- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [finnas, möjligheter]   B= [att, låsa, in ,.. ]

B0Lemma: att, B0POS: IE, B0Token: att, B1IsInLexic: true, B1Lemma: låsa, B1POS: VB|INF|AKT, B1Token: låsa, S0B0Distance: 1, S0B0Lemma: möjlighet_att, S0B0LemmaPOS: möjlighet_IE, S0B0POS: NN|UTR|PLU|IND|NOM_IE, S0B0POSLemma: NN|UTR|PLU|IND|NOM_att, S0B0Token: möjligheter_att, S0B1Lemma: möjlighet_låsa, S0B1LemmaPOS: möjlighet_VB|INF|AKT, S0B1POS: NN|UTR|PLU|IND|NOM_VB|INF|AKT, S0B1POSLemma: NN|UTR|PLU|IND|NOM_låsa, S0B1Token: möjligheter_låsa, S0B2Lemma: möjlighet_in, S0B2LemmaPOS: möjlighet_PL, S0B2POS: NN|UTR|PLU|IND|NOM_PL, S0B2POSLemma: NN|UTR|PLU|IND|NOM_in, S0B2Token: möjligheter_in, S0IsInLexic: true, S0Lemma: möjlighet, S0POS: NN|UTR|PLU|IND|NOM, S0S1Distance: 1, S0Token: möjligheter, S1B0Lemma: finnas_att, S1B0LemmaPOS: finnas_IE, S1B0POS: VB|INF|SFO_IE, S1B0POSLemma: VB|INF|SFO_att, S1B0Token: finnas_att, S1IsInLexic: true, S1Lemma: finnas, S1POS: VB|INF|SFO, S1S0B0Lemma: finnas_möjlighet_att, S1S0B0LemmaPOS: finnas_NN|UTR|PLU|IND|NOM_IE, S1S0B0POS: VB|INF|SFO_NN|UTR|PLU|IND|NOM_IE, S1S0B0POSLemma: VB|INF|SFO_NN|UTR|PLU|IND|NOM_att, S1S0B0Token: finnas_möjligheter_att, S1S0Lemma: finnas_möjlighet, S1S0LemmaPOS: finnas_NN|UTR|PLU|IND|NOM, S1S0POS: VB|INF|SFO_NN|UTR|PLU|IND|NOM, S1S0POSLemma: VB|INF|SFO_möjlighet, S1S0Token: finnas_möjligheter, S1Token: finnas, StackLengthIs: 2, SyntaxicRelation: +nsubj, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, hasRighDep_acl: true, möjlighet_hasRighDep_acl: true, möjlighet_låsa_hasRighDep_acl: true, 

31- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[finnas, möjligheter]]   B= [att, låsa, in ,.. ]

B0Lemma: att, B0POS: IE, B0Token: att, B1IsInLexic: true, B1Lemma: låsa, B1POS: VB|INF|AKT, B1Token: låsa, S0B0Distance: 1, S0B0Lemma: finnas_möjlighet_att, S0B0LemmaPOS: finnas_möjlighet_IE, S0B0POS: VB|INF|SFO_NN|UTR|PLU|IND|NOM_IE, S0B0POSLemma: VB|INF|SFO_NN|UTR|PLU|IND|NOM_att, S0B0Token: finnas_möjligheter_att, S0B1Lemma: finnas_möjlighet_låsa, S0B1LemmaPOS: finnas_möjlighet_VB|INF|AKT, S0B1POS: VB|INF|SFO_NN|UTR|PLU|IND|NOM_VB|INF|AKT, S0B1POSLemma: VB|INF|SFO_NN|UTR|PLU|IND|NOM_låsa, S0B1Token: finnas_möjligheter_låsa, S0B2Lemma: finnas_möjlighet_in, S0B2LemmaPOS: finnas_möjlighet_PL, S0B2POS: VB|INF|SFO_NN|UTR|PLU|IND|NOM_PL, S0B2POSLemma: VB|INF|SFO_NN|UTR|PLU|IND|NOM_in, S0B2Token: finnas_möjligheter_in, S0Lemma: finnas_möjlighet, S0POS: VB|INF|SFO_NN|UTR|PLU|IND|NOM, S0Token: finnas_möjligheter, TransHistory1: 0, TransHistory2: 00, TransHistory3: 002, 

32- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [att, låsa, in ,.. ]

B0Lemma: att, B0POS: IE, B0Token: att, B1IsInLexic: true, B1Lemma: låsa, B1POS: VB|INF|AKT, B1Token: låsa, TransHistory1: 1, TransHistory2: 10, TransHistory3: 100, 

33- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [att]   B= [låsa, in, eller ,.. ]

B0IsInLexic: true, B0Lemma: låsa, B0POS: VB|INF|AKT, B0Token: låsa, B1IsInLexic: true, B1Lemma: in, B1POS: PL, B1Token: in, S0B0Distance: 1, S0B0Lemma: att_låsa, S0B0LemmaPOS: att_VB|INF|AKT, S0B0POS: IE_VB|INF|AKT, S0B0POSLemma: IE_låsa, S0B0Token: att_låsa, S0B1Lemma: att_in, S0B1LemmaPOS: att_PL, S0B1POS: IE_PL, S0B1POSLemma: IE_in, S0B1Token: att_in, S0B2Lemma: att_eller, S0B2LemmaPOS: att_KN, S0B2POS: IE_KN, S0B2POSLemma: IE_eller, S0B2Token: att_eller, S0Lemma: att, S0POS: IE, S0Token: att, TransHistory1: 2, TransHistory2: 21, TransHistory3: 210, att_isGouvernedBy_låsa: true, att_isGouvernedBy_låsa_mark: true, 

34- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [låsa, in, eller ,.. ]

B0IsInLexic: true, B0Lemma: låsa, B0POS: VB|INF|AKT, B0Token: låsa, B1IsInLexic: true, B1Lemma: in, B1POS: PL, B1Token: in, TransHistory1: 0, TransHistory2: 02, TransHistory3: 021, 

35- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [låsa]   B= [in, eller, fast ,.. ]

B0IsInLexic: true, B0Lemma: in, B0POS: PL, B0Token: in, B1Lemma: eller, B1POS: KN, B1Token: eller, S0B0Distance: 1, S0B0Lemma: låsa_in, S0B0LemmaPOS: låsa_PL, S0B0POS: VB|INF|AKT_PL, S0B0POSLemma: VB|INF|AKT_in, S0B0Token: låsa_in, S0B1Lemma: låsa_eller, S0B1LemmaPOS: låsa_KN, S0B1POS: VB|INF|AKT_KN, S0B1POSLemma: VB|INF|AKT_eller, S0B1Token: låsa_eller, S0B2Lemma: låsa_fast, S0B2LemmaPOS: låsa_AB|POS, S0B2POS: VB|INF|AKT_AB|POS, S0B2POSLemma: VB|INF|AKT_fast, S0B2Token: låsa_fast, S0IsInLexic: true, S0Lemma: låsa, S0POS: VB|INF|AKT, S0Token: låsa, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, hasRighDep_cc: true, hasRighDep_compound:prt: true, hasRighDep_conj: true, låsa_cykeln_hasRighDep_conj: true, låsa_eller_hasRighDep_cc: true, låsa_hasRighDep_cc: true, låsa_hasRighDep_compound:prt: true, låsa_hasRighDep_conj: true, låsa_in_hasRighDep_compound:prt: true, 

36- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [låsa, in]   B= [eller, fast, cykeln ,.. ]

B0Lemma: eller, B0POS: KN, B0Token: eller, B1IsInLexic: true, B1Lemma: fast, B1POS: AB|POS, B1Token: fast, S0B0Distance: 1, S0B0Lemma: in_eller, S0B0LemmaPOS: in_KN, S0B0POS: PL_KN, S0B0POSLemma: PL_eller, S0B0Token: in_eller, S0B1Lemma: in_fast, S0B1LemmaPOS: in_AB|POS, S0B1POS: PL_AB|POS, S0B1POSLemma: PL_fast, S0B1Token: in_fast, S0B2Lemma: in_cykeln, S0B2LemmaPOS: in_NN|UTR|SIN|DEF|NOM, S0B2POS: PL_NN|UTR|SIN|DEF|NOM, S0B2POSLemma: PL_cykeln, S0B2Token: in_cykeln, S0IsInLexic: true, S0Lemma: in, S0POS: PL, S0S1Distance: 1, S0Token: in, S1B0Lemma: låsa_eller, S1B0LemmaPOS: låsa_KN, S1B0POS: VB|INF|AKT_KN, S1B0POSLemma: VB|INF|AKT_eller, S1B0Token: låsa_eller, S1IsInLexic: true, S1Lemma: låsa, S1POS: VB|INF|AKT, S1S0B0Lemma: låsa_in_eller, S1S0B0LemmaPOS: låsa_PL_KN, S1S0B0POS: VB|INF|AKT_PL_KN, S1S0B0POSLemma: VB|INF|AKT_PL_eller, S1S0B0Token: låsa_in_eller, S1S0Lemma: låsa_in, S1S0LemmaPOS: låsa_PL, S1S0POS: VB|INF|AKT_PL, S1S0POSLemma: VB|INF|AKT_in, S1S0Token: låsa_in, S1Token: låsa, StackLengthIs: 2, SyntaxicRelation: +compound:prt, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

37- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[låsa, in]]   B= [eller, fast, cykeln ,.. ]

B0Lemma: eller, B0POS: KN, B0Token: eller, B1IsInLexic: true, B1Lemma: fast, B1POS: AB|POS, B1Token: fast, S0B0Distance: 1, S0B0Lemma: låsa_in_eller, S0B0LemmaPOS: låsa_in_KN, S0B0POS: VB|INF|AKT_PL_KN, S0B0POSLemma: VB|INF|AKT_PL_eller, S0B0Token: låsa_in_eller, S0B1Lemma: låsa_in_fast, S0B1LemmaPOS: låsa_in_AB|POS, S0B1POS: VB|INF|AKT_PL_AB|POS, S0B1POSLemma: VB|INF|AKT_PL_fast, S0B1Token: låsa_in_fast, S0B2Lemma: låsa_in_cykeln, S0B2LemmaPOS: låsa_in_NN|UTR|SIN|DEF|NOM, S0B2POS: VB|INF|AKT_PL_NN|UTR|SIN|DEF|NOM, S0B2POSLemma: VB|INF|AKT_PL_cykeln, S0B2Token: låsa_in_cykeln, S0Lemma: låsa_in, S0POS: VB|INF|AKT_PL, S0Token: låsa_in, TransHistory1: 0, TransHistory2: 00, TransHistory3: 002, 

38- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [eller, fast, cykeln ,.. ]

B0Lemma: eller, B0POS: KN, B0Token: eller, B1IsInLexic: true, B1Lemma: fast, B1POS: AB|POS, B1Token: fast, TransHistory1: 1, TransHistory2: 10, TransHistory3: 100, 

39- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [eller]   B= [fast, cykeln, . ,.. ]

B0IsInLexic: true, B0Lemma: fast, B0POS: AB|POS, B0Token: fast, B1Lemma: cykeln, B1POS: NN|UTR|SIN|DEF|NOM, B1Token: cykeln, S0B0Distance: 1, S0B0Lemma: eller_fast, S0B0LemmaPOS: eller_AB|POS, S0B0POS: KN_AB|POS, S0B0POSLemma: KN_fast, S0B0Token: eller_fast, S0B1Lemma: eller_cykeln, S0B1LemmaPOS: eller_NN|UTR|SIN|DEF|NOM, S0B1POS: KN_NN|UTR|SIN|DEF|NOM, S0B1POSLemma: KN_cykeln, S0B1Token: eller_cykeln, S0B2Lemma: eller_., S0B2LemmaPOS: eller_MAD, S0B2POS: KN_MAD, S0B2POSLemma: KN_., S0B2Token: eller_., S0Lemma: eller, S0POS: KN, S0Token: eller, TransHistory1: 2, TransHistory2: 21, TransHistory3: 210, 

40- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [fast, cykeln, . ,.. ]

B0IsInLexic: true, B0Lemma: fast, B0POS: AB|POS, B0Token: fast, B1Lemma: cykeln, B1POS: NN|UTR|SIN|DEF|NOM, B1Token: cykeln, TransHistory1: 0, TransHistory2: 02, TransHistory3: 021, 

41- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [fast]   B= [cykeln, . ,.. ]

B0Lemma: cykeln, B0POS: NN|UTR|SIN|DEF|NOM, B0Token: cykeln, B1Lemma: ., B1POS: MAD, B1Token: ., S0B0Distance: 1, S0B0Lemma: fast_cykeln, S0B0LemmaPOS: fast_NN|UTR|SIN|DEF|NOM, S0B0POS: AB|POS_NN|UTR|SIN|DEF|NOM, S0B0POSLemma: AB|POS_cykeln, S0B0Token: fast_cykeln, S0B1Lemma: fast_., S0B1LemmaPOS: fast_MAD, S0B1POS: AB|POS_MAD, S0B1POSLemma: AB|POS_., S0B1Token: fast_., S0IsInLexic: true, S0Lemma: fast, S0POS: AB|POS, S0Token: fast, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, fast_isGouvernedBy_cykeln: true, fast_isGouvernedBy_cykeln_advmod: true, 

42- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [cykeln, . ,.. ]

B0Lemma: cykeln, B0POS: NN|UTR|SIN|DEF|NOM, B0Token: cykeln, B1Lemma: ., B1POS: MAD, B1Token: ., TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

43- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [cykeln]   B= [.]

B0Lemma: ., B0POS: MAD, B0Token: ., S0B0Distance: 1, S0B0Lemma: cykeln_., S0B0LemmaPOS: cykeln_MAD, S0B0POS: NN|UTR|SIN|DEF|NOM_MAD, S0B0POSLemma: NN|UTR|SIN|DEF|NOM_., S0B0Token: cykeln_., S0Lemma: cykeln, S0POS: NN|UTR|SIN|DEF|NOM, S0Token: cykeln, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

44- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [.]

B0Lemma: ., B0POS: MAD, B0Token: ., TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

45- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [ ]

S0Lemma: ., S0POS: MAD, S0Token: ., TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

46- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

## Sentence No. 12 - 
det går inte att komma igång med appen utan att först skapa ett konto och lägga till bilen i datorn . 
### Existing MWEs: 
1- **komma igång** (VPC)
2- **lägga till** (VPC)



0- &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [det, går, inte ,.. ]

B0Lemma: den, B0POS: PN|NEU|SIN|DEF|SUB/OBJ, B0Token: det, B1IsInLexic: true, B1Lemma: gå, B1POS: VB|PRS|AKT, B1Token: går, 

1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [det]   B= [går, inte, att ,.. ]

B0IsInLexic: true, B0Lemma: gå, B0POS: VB|PRS|AKT, B0Token: går, B1Lemma: inte, B1POS: AB, B1Token: inte, S0B0Distance: 1, S0B0Lemma: den_gå, S0B0LemmaPOS: den_VB|PRS|AKT, S0B0POS: PN|NEU|SIN|DEF|SUB/OBJ_VB|PRS|AKT, S0B0POSLemma: PN|NEU|SIN|DEF|SUB/OBJ_gå, S0B0Token: det_går, S0B1Lemma: den_inte, S0B1LemmaPOS: den_AB, S0B1POS: PN|NEU|SIN|DEF|SUB/OBJ_AB, S0B1POSLemma: PN|NEU|SIN|DEF|SUB/OBJ_inte, S0B1Token: det_inte, S0B2Lemma: den_att, S0B2LemmaPOS: den_IE, S0B2POS: PN|NEU|SIN|DEF|SUB/OBJ_IE, S0B2POSLemma: PN|NEU|SIN|DEF|SUB/OBJ_att, S0B2Token: det_att, S0Lemma: den, S0POS: PN|NEU|SIN|DEF|SUB/OBJ, S0Token: det, den_isGouvernedBy_gå: true, den_isGouvernedBy_gå_expl: true, 

2- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [går, inte, att ,.. ]

B0IsInLexic: true, B0Lemma: gå, B0POS: VB|PRS|AKT, B0Token: går, B1Lemma: inte, B1POS: AB, B1Token: inte, TransHistory1: 0, 

3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [går]   B= [inte, att, komma ,.. ]

B0Lemma: inte, B0POS: AB, B0Token: inte, B1Lemma: att, B1POS: IE, B1Token: att, S0B0Distance: 1, S0B0Lemma: gå_inte, S0B0LemmaPOS: gå_AB, S0B0POS: VB|PRS|AKT_AB, S0B0POSLemma: VB|PRS|AKT_inte, S0B0Token: går_inte, S0B1Lemma: gå_att, S0B1LemmaPOS: gå_IE, S0B1POS: VB|PRS|AKT_IE, S0B1POSLemma: VB|PRS|AKT_att, S0B1Token: går_att, S0B2Lemma: gå_komma, S0B2LemmaPOS: gå_VB|INF|AKT, S0B2POS: VB|PRS|AKT_VB|INF|AKT, S0B2POSLemma: VB|PRS|AKT_komma, S0B2Token: går_komma, S0IsInLexic: true, S0Lemma: gå, S0POS: VB|PRS|AKT, S0Token: går, TransHistory1: 2, TransHistory2: 20, 

4- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [inte, att, komma ,.. ]

B0Lemma: inte, B0POS: AB, B0Token: inte, B1Lemma: att, B1POS: IE, B1Token: att, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [inte]   B= [att, komma, igång ,.. ]

B0Lemma: att, B0POS: IE, B0Token: att, B1IsInLexic: true, B1Lemma: komma, B1POS: VB|INF|AKT, B1Token: komma, S0B0Distance: 1, S0B0Lemma: inte_att, S0B0LemmaPOS: inte_IE, S0B0POS: AB_IE, S0B0POSLemma: AB_att, S0B0Token: inte_att, S0B1Lemma: inte_komma, S0B1LemmaPOS: inte_VB|INF|AKT, S0B1POS: AB_VB|INF|AKT, S0B1POSLemma: AB_komma, S0B1Token: inte_komma, S0B2Lemma: inte_igång, S0B2LemmaPOS: inte_PL, S0B2POS: AB_PL, S0B2POSLemma: AB_igång, S0B2Token: inte_igång, S0Lemma: inte, S0POS: AB, S0Token: inte, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

6- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [att, komma, igång ,.. ]

B0Lemma: att, B0POS: IE, B0Token: att, B1IsInLexic: true, B1Lemma: komma, B1POS: VB|INF|AKT, B1Token: komma, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [att]   B= [komma, igång, med ,.. ]

B0IsInLexic: true, B0Lemma: komma, B0POS: VB|INF|AKT, B0Token: komma, B1IsInLexic: true, B1Lemma: igång, B1POS: PL, B1Token: igång, S0B0Distance: 1, S0B0Lemma: att_komma, S0B0LemmaPOS: att_VB|INF|AKT, S0B0POS: IE_VB|INF|AKT, S0B0POSLemma: IE_komma, S0B0Token: att_komma, S0B1Lemma: att_igång, S0B1LemmaPOS: att_PL, S0B1POS: IE_PL, S0B1POSLemma: IE_igång, S0B1Token: att_igång, S0B2Lemma: att_med, S0B2LemmaPOS: att_PP, S0B2POS: IE_PP, S0B2POSLemma: IE_med, S0B2Token: att_med, S0Lemma: att, S0POS: IE, S0Token: att, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, att_isGouvernedBy_komma: true, att_isGouvernedBy_komma_mark: true, 

8- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [komma, igång, med ,.. ]

B0IsInLexic: true, B0Lemma: komma, B0POS: VB|INF|AKT, B0Token: komma, B1IsInLexic: true, B1Lemma: igång, B1POS: PL, B1Token: igång, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [komma]   B= [igång, med, appen ,.. ]

B0IsInLexic: true, B0Lemma: igång, B0POS: PL, B0Token: igång, B1IsInLexic: true, B1Lemma: med, B1POS: PP, B1Token: med, S0B0Distance: 1, S0B0Lemma: komma_igång, S0B0LemmaPOS: komma_PL, S0B0POS: VB|INF|AKT_PL, S0B0POSLemma: VB|INF|AKT_igång, S0B0Token: komma_igång, S0B1Lemma: komma_med, S0B1LemmaPOS: komma_PP, S0B1POS: VB|INF|AKT_PP, S0B1POSLemma: VB|INF|AKT_med, S0B1Token: komma_med, S0B2Lemma: komma_app, S0B2LemmaPOS: komma_NN|UTR|SIN|DEF|NOM, S0B2POS: VB|INF|AKT_NN|UTR|SIN|DEF|NOM, S0B2POSLemma: VB|INF|AKT_app, S0B2Token: komma_appen, S0IsInLexic: true, S0Lemma: komma, S0POS: VB|INF|AKT, S0Token: komma, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, hasRighDep_advcl: true, hasRighDep_compound:prt: true, hasRighDep_nmod: true, komma_app_hasRighDep_nmod: true, komma_hasRighDep_advcl: true, komma_hasRighDep_compound:prt: true, komma_hasRighDep_nmod: true, komma_igång_hasRighDep_compound:prt: true, komma_skapa_hasRighDep_advcl: true, 

10- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [komma, igång]   B= [med, appen, utan ,.. ]

B0IsInLexic: true, B0Lemma: med, B0POS: PP, B0Token: med, B1Lemma: app, B1POS: NN|UTR|SIN|DEF|NOM, B1Token: appen, S0B0Distance: 1, S0B0Lemma: igång_med, S0B0LemmaPOS: igång_PP, S0B0POS: PL_PP, S0B0POSLemma: PL_med, S0B0Token: igång_med, S0B1Lemma: igång_app, S0B1LemmaPOS: igång_NN|UTR|SIN|DEF|NOM, S0B1POS: PL_NN|UTR|SIN|DEF|NOM, S0B1POSLemma: PL_app, S0B1Token: igång_appen, S0B2Lemma: igång_utan, S0B2LemmaPOS: igång_PP, S0B2POS: PL_PP, S0B2POSLemma: PL_utan, S0B2Token: igång_utan, S0IsInLexic: true, S0Lemma: igång, S0POS: PL, S0S1Distance: 1, S0Token: igång, S1B0Lemma: komma_med, S1B0LemmaPOS: komma_PP, S1B0POS: VB|INF|AKT_PP, S1B0POSLemma: VB|INF|AKT_med, S1B0Token: komma_med, S1IsInLexic: true, S1Lemma: komma, S1POS: VB|INF|AKT, S1S0B0Lemma: komma_igång_med, S1S0B0LemmaPOS: komma_PL_PP, S1S0B0POS: VB|INF|AKT_PL_PP, S1S0B0POSLemma: VB|INF|AKT_PL_med, S1S0B0Token: komma_igång_med, S1S0Lemma: komma_igång, S1S0LemmaPOS: komma_PL, S1S0POS: VB|INF|AKT_PL, S1S0POSLemma: VB|INF|AKT_igång, S1S0Token: komma_igång, S1Token: komma, StackLengthIs: 2, SyntaxicRelation: +compound:prt, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

11- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[komma, igång]]   B= [med, appen, utan ,.. ]

B0IsInLexic: true, B0Lemma: med, B0POS: PP, B0Token: med, B1Lemma: app, B1POS: NN|UTR|SIN|DEF|NOM, B1Token: appen, S0B0Distance: 1, S0B0Lemma: komma_igång_med, S0B0LemmaPOS: komma_igång_PP, S0B0POS: VB|INF|AKT_PL_PP, S0B0POSLemma: VB|INF|AKT_PL_med, S0B0Token: komma_igång_med, S0B1Lemma: komma_igång_app, S0B1LemmaPOS: komma_igång_NN|UTR|SIN|DEF|NOM, S0B1POS: VB|INF|AKT_PL_NN|UTR|SIN|DEF|NOM, S0B1POSLemma: VB|INF|AKT_PL_app, S0B1Token: komma_igång_appen, S0B2Lemma: komma_igång_utan, S0B2LemmaPOS: komma_igång_PP, S0B2POS: VB|INF|AKT_PL_PP, S0B2POSLemma: VB|INF|AKT_PL_utan, S0B2Token: komma_igång_utan, S0Lemma: komma_igång, S0POS: VB|INF|AKT_PL, S0Token: komma_igång, TransHistory1: 0, TransHistory2: 00, TransHistory3: 002, 

12- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [med, appen, utan ,.. ]

B0IsInLexic: true, B0Lemma: med, B0POS: PP, B0Token: med, B1Lemma: app, B1POS: NN|UTR|SIN|DEF|NOM, B1Token: appen, TransHistory1: 1, TransHistory2: 10, TransHistory3: 100, 

13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [med]   B= [appen, utan, att ,.. ]

B0Lemma: app, B0POS: NN|UTR|SIN|DEF|NOM, B0Token: appen, B1Lemma: utan, B1POS: PP, B1Token: utan, S0B0Distance: 1, S0B0Lemma: med_app, S0B0LemmaPOS: med_NN|UTR|SIN|DEF|NOM, S0B0POS: PP_NN|UTR|SIN|DEF|NOM, S0B0POSLemma: PP_app, S0B0Token: med_appen, S0B1Lemma: med_utan, S0B1LemmaPOS: med_PP, S0B1POS: PP_PP, S0B1POSLemma: PP_utan, S0B1Token: med_utan, S0B2Lemma: med_att, S0B2LemmaPOS: med_IE, S0B2POS: PP_IE, S0B2POSLemma: PP_att, S0B2Token: med_att, S0IsInLexic: true, S0Lemma: med, S0POS: PP, S0Token: med, TransHistory1: 2, TransHistory2: 21, TransHistory3: 210, med_isGouvernedBy_app: true, med_isGouvernedBy_app_case: true, 

14- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [appen, utan, att ,.. ]

B0Lemma: app, B0POS: NN|UTR|SIN|DEF|NOM, B0Token: appen, B1Lemma: utan, B1POS: PP, B1Token: utan, TransHistory1: 0, TransHistory2: 02, TransHistory3: 021, 

15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [appen]   B= [utan, att, först ,.. ]

B0Lemma: utan, B0POS: PP, B0Token: utan, B1Lemma: att, B1POS: IE, B1Token: att, S0B0Distance: 1, S0B0Lemma: app_utan, S0B0LemmaPOS: app_PP, S0B0POS: NN|UTR|SIN|DEF|NOM_PP, S0B0POSLemma: NN|UTR|SIN|DEF|NOM_utan, S0B0Token: appen_utan, S0B1Lemma: app_att, S0B1LemmaPOS: app_IE, S0B1POS: NN|UTR|SIN|DEF|NOM_IE, S0B1POSLemma: NN|UTR|SIN|DEF|NOM_att, S0B1Token: appen_att, S0B2Lemma: app_först, S0B2LemmaPOS: app_AB, S0B2POS: NN|UTR|SIN|DEF|NOM_AB, S0B2POSLemma: NN|UTR|SIN|DEF|NOM_först, S0B2Token: appen_först, S0Lemma: app, S0POS: NN|UTR|SIN|DEF|NOM, S0Token: appen, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

16- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [utan, att, först ,.. ]

B0Lemma: utan, B0POS: PP, B0Token: utan, B1Lemma: att, B1POS: IE, B1Token: att, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [utan]   B= [att, först, skapa ,.. ]

B0Lemma: att, B0POS: IE, B0Token: att, B1Lemma: först, B1POS: AB, B1Token: först, S0B0Distance: 1, S0B0Lemma: utan_att, S0B0LemmaPOS: utan_IE, S0B0POS: PP_IE, S0B0POSLemma: PP_att, S0B0Token: utan_att, S0B1Lemma: utan_först, S0B1LemmaPOS: utan_AB, S0B1POS: PP_AB, S0B1POSLemma: PP_först, S0B1Token: utan_först, S0B2Lemma: utan_skapa, S0B2LemmaPOS: utan_VB|INF|AKT, S0B2POS: PP_VB|INF|AKT, S0B2POSLemma: PP_skapa, S0B2Token: utan_skapa, S0Lemma: utan, S0POS: PP, S0Token: utan, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, utan_isGouvernedBy_skapa: true, utan_isGouvernedBy_skapa_case: true, 

18- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [att, först, skapa ,.. ]

B0Lemma: att, B0POS: IE, B0Token: att, B1Lemma: först, B1POS: AB, B1Token: först, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [att]   B= [först, skapa, ett ,.. ]

B0Lemma: först, B0POS: AB, B0Token: först, B1IsInLexic: true, B1Lemma: skapa, B1POS: VB|INF|AKT, B1Token: skapa, S0B0Distance: 1, S0B0Lemma: att_först, S0B0LemmaPOS: att_AB, S0B0POS: IE_AB, S0B0POSLemma: IE_först, S0B0Token: att_först, S0B1Lemma: att_skapa, S0B1LemmaPOS: att_VB|INF|AKT, S0B1POS: IE_VB|INF|AKT, S0B1POSLemma: IE_skapa, S0B1Token: att_skapa, S0B2Lemma: att_en, S0B2LemmaPOS: att_DT|NEU|SIN|IND, S0B2POS: IE_DT|NEU|SIN|IND, S0B2POSLemma: IE_en, S0B2Token: att_ett, S0Lemma: att, S0POS: IE, S0Token: att, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, att_isGouvernedBy_skapa: true, att_isGouvernedBy_skapa_mark: true, 

20- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [först, skapa, ett ,.. ]

B0Lemma: först, B0POS: AB, B0Token: först, B1IsInLexic: true, B1Lemma: skapa, B1POS: VB|INF|AKT, B1Token: skapa, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [först]   B= [skapa, ett, konto ,.. ]

B0IsInLexic: true, B0Lemma: skapa, B0POS: VB|INF|AKT, B0Token: skapa, B1IsInLexic: true, B1Lemma: en, B1POS: DT|NEU|SIN|IND, B1Token: ett, S0B0Distance: 1, S0B0Lemma: först_skapa, S0B0LemmaPOS: först_VB|INF|AKT, S0B0POS: AB_VB|INF|AKT, S0B0POSLemma: AB_skapa, S0B0Token: först_skapa, S0B1Lemma: först_en, S0B1LemmaPOS: först_DT|NEU|SIN|IND, S0B1POS: AB_DT|NEU|SIN|IND, S0B1POSLemma: AB_en, S0B1Token: först_ett, S0B2Lemma: först_konto, S0B2LemmaPOS: först_NN|NEU|SIN|IND|NOM, S0B2POS: AB_NN|NEU|SIN|IND|NOM, S0B2POSLemma: AB_konto, S0B2Token: först_konto, S0Lemma: först, S0POS: AB, S0Token: först, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, först_isGouvernedBy_skapa: true, först_isGouvernedBy_skapa_advmod: true, 

22- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [skapa, ett, konto ,.. ]

B0IsInLexic: true, B0Lemma: skapa, B0POS: VB|INF|AKT, B0Token: skapa, B1IsInLexic: true, B1Lemma: en, B1POS: DT|NEU|SIN|IND, B1Token: ett, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

23- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [skapa]   B= [ett, konto, och ,.. ]

B0IsInLexic: true, B0Lemma: en, B0POS: DT|NEU|SIN|IND, B0Token: ett, B1Lemma: konto, B1POS: NN|NEU|SIN|IND|NOM, B1Token: konto, S0B0Distance: 1, S0B0Lemma: skapa_en, S0B0LemmaPOS: skapa_DT|NEU|SIN|IND, S0B0POS: VB|INF|AKT_DT|NEU|SIN|IND, S0B0POSLemma: VB|INF|AKT_en, S0B0Token: skapa_ett, S0B1Lemma: skapa_konto, S0B1LemmaPOS: skapa_NN|NEU|SIN|IND|NOM, S0B1POS: VB|INF|AKT_NN|NEU|SIN|IND|NOM, S0B1POSLemma: VB|INF|AKT_konto, S0B1Token: skapa_konto, S0B2Lemma: skapa_och, S0B2LemmaPOS: skapa_KN, S0B2POS: VB|INF|AKT_KN, S0B2POSLemma: VB|INF|AKT_och, S0B2Token: skapa_och, S0IsInLexic: true, S0Lemma: skapa, S0POS: VB|INF|AKT, S0Token: skapa, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, hasRighDep_cc: true, hasRighDep_conj: true, hasRighDep_dobj: true, hasRighDep_nmod: true, skapa_bil_hasRighDep_nmod: true, skapa_dator_hasRighDep_nmod: true, skapa_hasRighDep_cc: true, skapa_hasRighDep_conj: true, skapa_hasRighDep_dobj: true, skapa_hasRighDep_nmod: true, skapa_konto_hasRighDep_dobj: true, skapa_lägga_hasRighDep_conj: true, skapa_och_hasRighDep_cc: true, 

24- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ett, konto, och ,.. ]

B0IsInLexic: true, B0Lemma: en, B0POS: DT|NEU|SIN|IND, B0Token: ett, B1Lemma: konto, B1POS: NN|NEU|SIN|IND|NOM, B1Token: konto, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

25- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ett]   B= [konto, och, lägga ,.. ]

B0Lemma: konto, B0POS: NN|NEU|SIN|IND|NOM, B0Token: konto, B1Lemma: och, B1POS: KN, B1Token: och, S0B0Distance: 1, S0B0Lemma: en_konto, S0B0LemmaPOS: en_NN|NEU|SIN|IND|NOM, S0B0POS: DT|NEU|SIN|IND_NN|NEU|SIN|IND|NOM, S0B0POSLemma: DT|NEU|SIN|IND_konto, S0B0Token: ett_konto, S0B1Lemma: en_och, S0B1LemmaPOS: en_KN, S0B1POS: DT|NEU|SIN|IND_KN, S0B1POSLemma: DT|NEU|SIN|IND_och, S0B1Token: ett_och, S0B2Lemma: en_lägga, S0B2LemmaPOS: en_VB|INF|AKT, S0B2POS: DT|NEU|SIN|IND_VB|INF|AKT, S0B2POSLemma: DT|NEU|SIN|IND_lägga, S0B2Token: ett_lägga, S0IsInLexic: true, S0Lemma: en, S0POS: DT|NEU|SIN|IND, S0Token: ett, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, en_isGouvernedBy_konto: true, en_isGouvernedBy_konto_det: true, 

26- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [konto, och, lägga ,.. ]

B0Lemma: konto, B0POS: NN|NEU|SIN|IND|NOM, B0Token: konto, B1Lemma: och, B1POS: KN, B1Token: och, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

27- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [konto]   B= [och, lägga, till ,.. ]

B0Lemma: och, B0POS: KN, B0Token: och, B1IsInLexic: true, B1Lemma: lägga, B1POS: VB|INF|AKT, B1Token: lägga, S0B0Distance: 1, S0B0Lemma: konto_och, S0B0LemmaPOS: konto_KN, S0B0POS: NN|NEU|SIN|IND|NOM_KN, S0B0POSLemma: NN|NEU|SIN|IND|NOM_och, S0B0Token: konto_och, S0B1Lemma: konto_lägga, S0B1LemmaPOS: konto_VB|INF|AKT, S0B1POS: NN|NEU|SIN|IND|NOM_VB|INF|AKT, S0B1POSLemma: NN|NEU|SIN|IND|NOM_lägga, S0B1Token: konto_lägga, S0B2Lemma: konto_till, S0B2LemmaPOS: konto_PP, S0B2POS: NN|NEU|SIN|IND|NOM_PP, S0B2POSLemma: NN|NEU|SIN|IND|NOM_till, S0B2Token: konto_till, S0Lemma: konto, S0POS: NN|NEU|SIN|IND|NOM, S0Token: konto, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

28- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [och, lägga, till ,.. ]

B0Lemma: och, B0POS: KN, B0Token: och, B1IsInLexic: true, B1Lemma: lägga, B1POS: VB|INF|AKT, B1Token: lägga, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

29- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [och]   B= [lägga, till, bilen ,.. ]

B0IsInLexic: true, B0Lemma: lägga, B0POS: VB|INF|AKT, B0Token: lägga, B1IsInLexic: true, B1Lemma: till, B1POS: PP, B1Token: till, S0B0Distance: 1, S0B0Lemma: och_lägga, S0B0LemmaPOS: och_VB|INF|AKT, S0B0POS: KN_VB|INF|AKT, S0B0POSLemma: KN_lägga, S0B0Token: och_lägga, S0B1Lemma: och_till, S0B1LemmaPOS: och_PP, S0B1POS: KN_PP, S0B1POSLemma: KN_till, S0B1Token: och_till, S0B2Lemma: och_bil, S0B2LemmaPOS: och_NN|UTR|SIN|DEF|NOM, S0B2POS: KN_NN|UTR|SIN|DEF|NOM, S0B2POSLemma: KN_bil, S0B2Token: och_bilen, S0Lemma: och, S0POS: KN, S0Token: och, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

30- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [lägga, till, bilen ,.. ]

B0IsInLexic: true, B0Lemma: lägga, B0POS: VB|INF|AKT, B0Token: lägga, B1IsInLexic: true, B1Lemma: till, B1POS: PP, B1Token: till, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

31- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [lägga]   B= [till, bilen, i ,.. ]

B0IsInLexic: true, B0Lemma: till, B0POS: PP, B0Token: till, B1Lemma: bil, B1POS: NN|UTR|SIN|DEF|NOM, B1Token: bilen, S0B0Distance: 1, S0B0Lemma: lägga_till, S0B0LemmaPOS: lägga_PP, S0B0POS: VB|INF|AKT_PP, S0B0POSLemma: VB|INF|AKT_till, S0B0Token: lägga_till, S0B1Lemma: lägga_bil, S0B1LemmaPOS: lägga_NN|UTR|SIN|DEF|NOM, S0B1POS: VB|INF|AKT_NN|UTR|SIN|DEF|NOM, S0B1POSLemma: VB|INF|AKT_bil, S0B1Token: lägga_bilen, S0B2Lemma: lägga_i, S0B2LemmaPOS: lägga_PP, S0B2POS: VB|INF|AKT_PP, S0B2POSLemma: VB|INF|AKT_i, S0B2Token: lägga_i, S0IsInLexic: true, S0Lemma: lägga, S0POS: VB|INF|AKT, S0Token: lägga, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

32- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [lägga, till]   B= [bilen, i, datorn ,.. ]

B0Lemma: bil, B0POS: NN|UTR|SIN|DEF|NOM, B0Token: bilen, B1IsInLexic: true, B1Lemma: i, B1POS: PP, B1Token: i, S0B0Distance: 1, S0B0Lemma: till_bil, S0B0LemmaPOS: till_NN|UTR|SIN|DEF|NOM, S0B0POS: PP_NN|UTR|SIN|DEF|NOM, S0B0POSLemma: PP_bil, S0B0Token: till_bilen, S0B1Lemma: till_i, S0B1LemmaPOS: till_PP, S0B1POS: PP_PP, S0B1POSLemma: PP_i, S0B1Token: till_i, S0B2Lemma: till_dator, S0B2LemmaPOS: till_NN|UTR|SIN|DEF|NOM, S0B2POS: PP_NN|UTR|SIN|DEF|NOM, S0B2POSLemma: PP_dator, S0B2Token: till_datorn, S0IsInLexic: true, S0Lemma: till, S0POS: PP, S0S1Distance: 1, S0Token: till, S1B0Lemma: lägga_bil, S1B0LemmaPOS: lägga_NN|UTR|SIN|DEF|NOM, S1B0POS: VB|INF|AKT_NN|UTR|SIN|DEF|NOM, S1B0POSLemma: VB|INF|AKT_bil, S1B0Token: lägga_bilen, S1IsInLexic: true, S1Lemma: lägga, S1POS: VB|INF|AKT, S1S0B0Lemma: lägga_till_bil, S1S0B0LemmaPOS: lägga_PP_NN|UTR|SIN|DEF|NOM, S1S0B0POS: VB|INF|AKT_PP_NN|UTR|SIN|DEF|NOM, S1S0B0POSLemma: VB|INF|AKT_PP_bil, S1S0B0Token: lägga_till_bilen, S1S0Lemma: lägga_till, S1S0LemmaPOS: lägga_PP, S1S0POS: VB|INF|AKT_PP, S1S0POSLemma: VB|INF|AKT_till, S1S0Token: lägga_till, S1Token: lägga, StackLengthIs: 2, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, till_isGouvernedBy_bil: true, till_isGouvernedBy_bil_case: true, 

33- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[lägga, till]]   B= [bilen, i, datorn ,.. ]

B0Lemma: bil, B0POS: NN|UTR|SIN|DEF|NOM, B0Token: bilen, B1IsInLexic: true, B1Lemma: i, B1POS: PP, B1Token: i, S0B0Distance: 1, S0B0Lemma: lägga_till_bil, S0B0LemmaPOS: lägga_till_NN|UTR|SIN|DEF|NOM, S0B0POS: VB|INF|AKT_PP_NN|UTR|SIN|DEF|NOM, S0B0POSLemma: VB|INF|AKT_PP_bil, S0B0Token: lägga_till_bilen, S0B1Lemma: lägga_till_i, S0B1LemmaPOS: lägga_till_PP, S0B1POS: VB|INF|AKT_PP_PP, S0B1POSLemma: VB|INF|AKT_PP_i, S0B1Token: lägga_till_i, S0B2Lemma: lägga_till_dator, S0B2LemmaPOS: lägga_till_NN|UTR|SIN|DEF|NOM, S0B2POS: VB|INF|AKT_PP_NN|UTR|SIN|DEF|NOM, S0B2POSLemma: VB|INF|AKT_PP_dator, S0B2Token: lägga_till_datorn, S0Lemma: lägga_till, S0POS: VB|INF|AKT_PP, S0Token: lägga_till, TransHistory1: 0, TransHistory2: 00, TransHistory3: 002, 

34- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [bilen, i, datorn ,.. ]

B0Lemma: bil, B0POS: NN|UTR|SIN|DEF|NOM, B0Token: bilen, B1IsInLexic: true, B1Lemma: i, B1POS: PP, B1Token: i, TransHistory1: 1, TransHistory2: 10, TransHistory3: 100, 

35- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [bilen]   B= [i, datorn, . ,.. ]

B0IsInLexic: true, B0Lemma: i, B0POS: PP, B0Token: i, B1Lemma: dator, B1POS: NN|UTR|SIN|DEF|NOM, B1Token: datorn, S0B0Distance: 1, S0B0Lemma: bil_i, S0B0LemmaPOS: bil_PP, S0B0POS: NN|UTR|SIN|DEF|NOM_PP, S0B0POSLemma: NN|UTR|SIN|DEF|NOM_i, S0B0Token: bilen_i, S0B1Lemma: bil_dator, S0B1LemmaPOS: bil_NN|UTR|SIN|DEF|NOM, S0B1POS: NN|UTR|SIN|DEF|NOM_NN|UTR|SIN|DEF|NOM, S0B1POSLemma: NN|UTR|SIN|DEF|NOM_dator, S0B1Token: bilen_datorn, S0B2Lemma: bil_., S0B2LemmaPOS: bil_MAD, S0B2POS: NN|UTR|SIN|DEF|NOM_MAD, S0B2POSLemma: NN|UTR|SIN|DEF|NOM_., S0B2Token: bilen_., S0Lemma: bil, S0POS: NN|UTR|SIN|DEF|NOM, S0Token: bilen, TransHistory1: 2, TransHistory2: 21, TransHistory3: 210, 

36- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [i, datorn, . ,.. ]

B0IsInLexic: true, B0Lemma: i, B0POS: PP, B0Token: i, B1Lemma: dator, B1POS: NN|UTR|SIN|DEF|NOM, B1Token: datorn, TransHistory1: 0, TransHistory2: 02, TransHistory3: 021, 

37- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [i]   B= [datorn, . ,.. ]

B0Lemma: dator, B0POS: NN|UTR|SIN|DEF|NOM, B0Token: datorn, B1Lemma: ., B1POS: MAD, B1Token: ., S0B0Distance: 1, S0B0Lemma: i_dator, S0B0LemmaPOS: i_NN|UTR|SIN|DEF|NOM, S0B0POS: PP_NN|UTR|SIN|DEF|NOM, S0B0POSLemma: PP_dator, S0B0Token: i_datorn, S0B1Lemma: i_., S0B1LemmaPOS: i_MAD, S0B1POS: PP_MAD, S0B1POSLemma: PP_., S0B1Token: i_., S0IsInLexic: true, S0Lemma: i, S0POS: PP, S0Token: i, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, i_isGouvernedBy_dator: true, i_isGouvernedBy_dator_case: true, 

38- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [datorn, . ,.. ]

B0Lemma: dator, B0POS: NN|UTR|SIN|DEF|NOM, B0Token: datorn, B1Lemma: ., B1POS: MAD, B1Token: ., TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

39- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [datorn]   B= [.]

B0Lemma: ., B0POS: MAD, B0Token: ., S0B0Distance: 1, S0B0Lemma: dator_., S0B0LemmaPOS: dator_MAD, S0B0POS: NN|UTR|SIN|DEF|NOM_MAD, S0B0POSLemma: NN|UTR|SIN|DEF|NOM_., S0B0Token: datorn_., S0Lemma: dator, S0POS: NN|UTR|SIN|DEF|NOM, S0Token: datorn, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

40- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [.]

B0Lemma: ., B0POS: MAD, B0Token: ., TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

41- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [ ]

S0Lemma: ., S0POS: MAD, S0Token: ., TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

42- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

## Sentence No. 22 - 
mats grauers och anderz larqvist , ordförande och klubbdirektör , säger sig inte ha tagit ett slutgiltigt beslut . 
### Existing MWEs: 
1- **säger sig** (IReflV)
2- **tagit beslut** (LVC)



0- &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [mats, grauers, och ,.. ]

B0Lemma: Mas, B0POS: PM|GEN, B0Token: mats, B1Lemma: Grau, B1POS: PM|NOM, B1Token: grauers, 

1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [mats]   B= [grauers, och, anderz ,.. ]

B0Lemma: Grau, B0POS: PM|NOM, B0Token: grauers, B1Lemma: och, B1POS: KN, B1Token: och, Mas_isGouvernedBy_Grau: true, Mas_isGouvernedBy_Grau_nmod:poss: true, S0B0Distance: 1, S0B0Lemma: Mas_Grau, S0B0LemmaPOS: Mas_PM|NOM, S0B0POS: PM|GEN_PM|NOM, S0B0POSLemma: PM|GEN_Grau, S0B0Token: mats_grauers, S0B1Lemma: Mas_och, S0B1LemmaPOS: Mas_KN, S0B1POS: PM|GEN_KN, S0B1POSLemma: PM|GEN_och, S0B1Token: mats_och, S0B2Lemma: Mas_Anderz, S0B2LemmaPOS: Mas_PM|NOM, S0B2POS: PM|GEN_PM|NOM, S0B2POSLemma: PM|GEN_Anderz, S0B2Token: mats_anderz, S0Lemma: Mas, S0POS: PM|GEN, S0Token: mats, 

2- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [grauers, och, anderz ,.. ]

B0Lemma: Grau, B0POS: PM|NOM, B0Token: grauers, B1Lemma: och, B1POS: KN, B1Token: och, TransHistory1: 0, 

3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [grauers]   B= [och, anderz, larqvist ,.. ]

B0Lemma: och, B0POS: KN, B0Token: och, B1Lemma: Anderz, B1POS: PM|NOM, B1Token: anderz, Grau_,_hasRighDep_punct: true, Grau_Anderz_hasRighDep_conj: true, Grau_hasRighDep_cc: true, Grau_hasRighDep_conj: true, Grau_hasRighDep_punct: true, Grau_isGouvernedBy_säga: true, Grau_isGouvernedBy_säga_nsubj: true, Grau_klubbdirektör_hasRighDep_conj: true, Grau_och_hasRighDep_cc: true, Grau_ordförande_hasRighDep_conj: true, S0B0Distance: 1, S0B0Lemma: Grau_och, S0B0LemmaPOS: Grau_KN, S0B0POS: PM|NOM_KN, S0B0POSLemma: PM|NOM_och, S0B0Token: grauers_och, S0B1Lemma: Grau_Anderz, S0B1LemmaPOS: Grau_PM|NOM, S0B1POS: PM|NOM_PM|NOM, S0B1POSLemma: PM|NOM_Anderz, S0B1Token: grauers_anderz, S0B2Lemma: Grau_Larqvist, S0B2LemmaPOS: Grau_PM|NOM, S0B2POS: PM|NOM_PM|NOM, S0B2POSLemma: PM|NOM_Larqvist, S0B2Token: grauers_larqvist, S0Lemma: Grau, S0POS: PM|NOM, S0Token: grauers, TransHistory1: 2, TransHistory2: 20, hasRighDep_cc: true, hasRighDep_conj: true, hasRighDep_punct: true, 

4- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [och, anderz, larqvist ,.. ]

B0Lemma: och, B0POS: KN, B0Token: och, B1Lemma: Anderz, B1POS: PM|NOM, B1Token: anderz, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [och]   B= [anderz, larqvist, , ,.. ]

B0Lemma: Anderz, B0POS: PM|NOM, B0Token: anderz, B1Lemma: Larqvist, B1POS: PM|NOM, B1Token: larqvist, S0B0Distance: 1, S0B0Lemma: och_Anderz, S0B0LemmaPOS: och_PM|NOM, S0B0POS: KN_PM|NOM, S0B0POSLemma: KN_Anderz, S0B0Token: och_anderz, S0B1Lemma: och_Larqvist, S0B1LemmaPOS: och_PM|NOM, S0B1POS: KN_PM|NOM, S0B1POSLemma: KN_Larqvist, S0B1Token: och_larqvist, S0B2Lemma: och_,, S0B2LemmaPOS: och_MID, S0B2POS: KN_MID, S0B2POSLemma: KN_,, S0B2Token: och_,, S0Lemma: och, S0POS: KN, S0Token: och, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

6- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [anderz, larqvist, , ,.. ]

B0Lemma: Anderz, B0POS: PM|NOM, B0Token: anderz, B1Lemma: Larqvist, B1POS: PM|NOM, B1Token: larqvist, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [anderz]   B= [larqvist, ,, ordförande ,.. ]

Anderz_Larqvist_hasRighDep_name: true, Anderz_hasRighDep_name: true, B0Lemma: Larqvist, B0POS: PM|NOM, B0Token: larqvist, B1Lemma: ,, B1POS: MID, B1Token: ,, S0B0Distance: 1, S0B0Lemma: Anderz_Larqvist, S0B0LemmaPOS: Anderz_PM|NOM, S0B0POS: PM|NOM_PM|NOM, S0B0POSLemma: PM|NOM_Larqvist, S0B0Token: anderz_larqvist, S0B1Lemma: Anderz_,, S0B1LemmaPOS: Anderz_MID, S0B1POS: PM|NOM_MID, S0B1POSLemma: PM|NOM_,, S0B1Token: anderz_,, S0B2Lemma: Anderz_ordförande, S0B2LemmaPOS: Anderz_NN|NEU|SIN|IND|NOM, S0B2POS: PM|NOM_NN|NEU|SIN|IND|NOM, S0B2POSLemma: PM|NOM_ordförande, S0B2Token: anderz_ordförande, S0Lemma: Anderz, S0POS: PM|NOM, S0Token: anderz, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, hasRighDep_name: true, 

8- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [larqvist, ,, ordförande ,.. ]

B0Lemma: Larqvist, B0POS: PM|NOM, B0Token: larqvist, B1Lemma: ,, B1POS: MID, B1Token: ,, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [larqvist]   B= [,, ordförande, och ,.. ]

B0Lemma: ,, B0POS: MID, B0Token: ,, B1Lemma: ordförande, B1POS: NN|NEU|SIN|IND|NOM, B1Token: ordförande, S0B0Distance: 1, S0B0Lemma: Larqvist_,, S0B0LemmaPOS: Larqvist_MID, S0B0POS: PM|NOM_MID, S0B0POSLemma: PM|NOM_,, S0B0Token: larqvist_,, S0B1Lemma: Larqvist_ordförande, S0B1LemmaPOS: Larqvist_NN|NEU|SIN|IND|NOM, S0B1POS: PM|NOM_NN|NEU|SIN|IND|NOM, S0B1POSLemma: PM|NOM_ordförande, S0B1Token: larqvist_ordförande, S0B2Lemma: Larqvist_och, S0B2LemmaPOS: Larqvist_KN, S0B2POS: PM|NOM_KN, S0B2POSLemma: PM|NOM_och, S0B2Token: larqvist_och, S0Lemma: Larqvist, S0POS: PM|NOM, S0Token: larqvist, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

10- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, ordförande, och ,.. ]

B0Lemma: ,, B0POS: MID, B0Token: ,, B1Lemma: ordförande, B1POS: NN|NEU|SIN|IND|NOM, B1Token: ordförande, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [ordförande, och, klubbdirektör ,.. ]

B0Lemma: ordförande, B0POS: NN|NEU|SIN|IND|NOM, B0Token: ordförande, B1Lemma: och, B1POS: KN, B1Token: och, S0B0Distance: 1, S0B0Lemma: ,_ordförande, S0B0LemmaPOS: ,_NN|NEU|SIN|IND|NOM, S0B0POS: MID_NN|NEU|SIN|IND|NOM, S0B0POSLemma: MID_ordförande, S0B0Token: ,_ordförande, S0B1Lemma: ,_och, S0B1LemmaPOS: ,_KN, S0B1POS: MID_KN, S0B1POSLemma: MID_och, S0B1Token: ,_och, S0B2Lemma: ,_klubbdirektör, S0B2LemmaPOS: ,_NN|UTR|SIN|IND|NOM, S0B2POS: MID_NN|UTR|SIN|IND|NOM, S0B2POSLemma: MID_klubbdirektör, S0B2Token: ,_klubbdirektör, S0Lemma: ,, S0POS: MID, S0Token: ,, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

12- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ordförande, och, klubbdirektör ,.. ]

B0Lemma: ordförande, B0POS: NN|NEU|SIN|IND|NOM, B0Token: ordförande, B1Lemma: och, B1POS: KN, B1Token: och, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ordförande]   B= [och, klubbdirektör, , ,.. ]

B0Lemma: och, B0POS: KN, B0Token: och, B1Lemma: klubbdirektör, B1POS: NN|UTR|SIN|IND|NOM, B1Token: klubbdirektör, S0B0Distance: 1, S0B0Lemma: ordförande_och, S0B0LemmaPOS: ordförande_KN, S0B0POS: NN|NEU|SIN|IND|NOM_KN, S0B0POSLemma: NN|NEU|SIN|IND|NOM_och, S0B0Token: ordförande_och, S0B1Lemma: ordförande_klubbdirektör, S0B1LemmaPOS: ordförande_NN|UTR|SIN|IND|NOM, S0B1POS: NN|NEU|SIN|IND|NOM_NN|UTR|SIN|IND|NOM, S0B1POSLemma: NN|NEU|SIN|IND|NOM_klubbdirektör, S0B1Token: ordförande_klubbdirektör, S0B2Lemma: ordförande_,, S0B2LemmaPOS: ordförande_MID, S0B2POS: NN|NEU|SIN|IND|NOM_MID, S0B2POSLemma: NN|NEU|SIN|IND|NOM_,, S0B2Token: ordförande_,, S0Lemma: ordförande, S0POS: NN|NEU|SIN|IND|NOM, S0Token: ordförande, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

14- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [och, klubbdirektör, , ,.. ]

B0Lemma: och, B0POS: KN, B0Token: och, B1Lemma: klubbdirektör, B1POS: NN|UTR|SIN|IND|NOM, B1Token: klubbdirektör, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [och]   B= [klubbdirektör, ,, säger ,.. ]

B0Lemma: klubbdirektör, B0POS: NN|UTR|SIN|IND|NOM, B0Token: klubbdirektör, B1Lemma: ,, B1POS: MID, B1Token: ,, S0B0Distance: 1, S0B0Lemma: och_klubbdirektör, S0B0LemmaPOS: och_NN|UTR|SIN|IND|NOM, S0B0POS: KN_NN|UTR|SIN|IND|NOM, S0B0POSLemma: KN_klubbdirektör, S0B0Token: och_klubbdirektör, S0B1Lemma: och_,, S0B1LemmaPOS: och_MID, S0B1POS: KN_MID, S0B1POSLemma: KN_,, S0B1Token: och_,, S0B2Lemma: och_säga, S0B2LemmaPOS: och_VB|PRS|AKT, S0B2POS: KN_VB|PRS|AKT, S0B2POSLemma: KN_säga, S0B2Token: och_säger, S0Lemma: och, S0POS: KN, S0Token: och, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

16- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [klubbdirektör, ,, säger ,.. ]

B0Lemma: klubbdirektör, B0POS: NN|UTR|SIN|IND|NOM, B0Token: klubbdirektör, B1Lemma: ,, B1POS: MID, B1Token: ,, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [klubbdirektör]   B= [,, säger, sig ,.. ]

B0Lemma: ,, B0POS: MID, B0Token: ,, B1IsInLexic: true, B1Lemma: säga, B1POS: VB|PRS|AKT, B1Token: säger, S0B0Distance: 1, S0B0Lemma: klubbdirektör_,, S0B0LemmaPOS: klubbdirektör_MID, S0B0POS: NN|UTR|SIN|IND|NOM_MID, S0B0POSLemma: NN|UTR|SIN|IND|NOM_,, S0B0Token: klubbdirektör_,, S0B1Lemma: klubbdirektör_säga, S0B1LemmaPOS: klubbdirektör_VB|PRS|AKT, S0B1POS: NN|UTR|SIN|IND|NOM_VB|PRS|AKT, S0B1POSLemma: NN|UTR|SIN|IND|NOM_säga, S0B1Token: klubbdirektör_säger, S0B2Lemma: klubbdirektör_sig, S0B2LemmaPOS: klubbdirektör_PN|UTR/NEU|SIN/PLU|DEF|OBJ, S0B2POS: NN|UTR|SIN|IND|NOM_PN|UTR/NEU|SIN/PLU|DEF|OBJ, S0B2POSLemma: NN|UTR|SIN|IND|NOM_sig, S0B2Token: klubbdirektör_sig, S0Lemma: klubbdirektör, S0POS: NN|UTR|SIN|IND|NOM, S0Token: klubbdirektör, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

18- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, säger, sig ,.. ]

B0Lemma: ,, B0POS: MID, B0Token: ,, B1IsInLexic: true, B1Lemma: säga, B1POS: VB|PRS|AKT, B1Token: säger, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [säger, sig, inte ,.. ]

B0IsInLexic: true, B0Lemma: säga, B0POS: VB|PRS|AKT, B0Token: säger, B1IsInLexic: true, B1Lemma: sig, B1POS: PN|UTR/NEU|SIN/PLU|DEF|OBJ, B1Token: sig, S0B0Distance: 1, S0B0Lemma: ,_säga, S0B0LemmaPOS: ,_VB|PRS|AKT, S0B0POS: MID_VB|PRS|AKT, S0B0POSLemma: MID_säga, S0B0Token: ,_säger, S0B1Lemma: ,_sig, S0B1LemmaPOS: ,_PN|UTR/NEU|SIN/PLU|DEF|OBJ, S0B1POS: MID_PN|UTR/NEU|SIN/PLU|DEF|OBJ, S0B1POSLemma: MID_sig, S0B1Token: ,_sig, S0B2Lemma: ,_inte, S0B2LemmaPOS: ,_AB, S0B2POS: MID_AB, S0B2POSLemma: MID_inte, S0B2Token: ,_inte, S0Lemma: ,, S0POS: MID, S0Token: ,, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

20- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [säger, sig, inte ,.. ]

B0IsInLexic: true, B0Lemma: säga, B0POS: VB|PRS|AKT, B0Token: säger, B1IsInLexic: true, B1Lemma: sig, B1POS: PN|UTR/NEU|SIN/PLU|DEF|OBJ, B1Token: sig, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [säger]   B= [sig, inte, ha ,.. ]

B0IsInLexic: true, B0Lemma: sig, B0POS: PN|UTR/NEU|SIN/PLU|DEF|OBJ, B0Token: sig, B1Lemma: inte, B1POS: AB, B1Token: inte, S0B0Distance: 1, S0B0Lemma: säga_sig, S0B0LemmaPOS: säga_PN|UTR/NEU|SIN/PLU|DEF|OBJ, S0B0POS: VB|PRS|AKT_PN|UTR/NEU|SIN/PLU|DEF|OBJ, S0B0POSLemma: VB|PRS|AKT_sig, S0B0Token: säger_sig, S0B1Lemma: säga_inte, S0B1LemmaPOS: säga_AB, S0B1POS: VB|PRS|AKT_AB, S0B1POSLemma: VB|PRS|AKT_inte, S0B1Token: säger_inte, S0B2Lemma: säga_ha, S0B2LemmaPOS: säga_VB|INF|AKT, S0B2POS: VB|PRS|AKT_VB|INF|AKT, S0B2POSLemma: VB|PRS|AKT_ha, S0B2Token: säger_ha, S0IsInLexic: true, S0Lemma: säga, S0POS: VB|PRS|AKT, S0Token: säger, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

22- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [säger, sig]   B= [inte, ha, tagit ,.. ]

B0Lemma: inte, B0POS: AB, B0Token: inte, B1IsInLexic: true, B1Lemma: ha, B1POS: VB|INF|AKT, B1Token: ha, S0B0Distance: 1, S0B0Lemma: sig_inte, S0B0LemmaPOS: sig_AB, S0B0POS: PN|UTR/NEU|SIN/PLU|DEF|OBJ_AB, S0B0POSLemma: PN|UTR/NEU|SIN/PLU|DEF|OBJ_inte, S0B0Token: sig_inte, S0B1Lemma: sig_ha, S0B1LemmaPOS: sig_VB|INF|AKT, S0B1POS: PN|UTR/NEU|SIN/PLU|DEF|OBJ_VB|INF|AKT, S0B1POSLemma: PN|UTR/NEU|SIN/PLU|DEF|OBJ_ha, S0B1Token: sig_ha, S0B2Lemma: sig_ta, S0B2LemmaPOS: sig_VB|SUP|AKT, S0B2POS: PN|UTR/NEU|SIN/PLU|DEF|OBJ_VB|SUP|AKT, S0B2POSLemma: PN|UTR/NEU|SIN/PLU|DEF|OBJ_ta, S0B2Token: sig_tagit, S0IsInLexic: true, S0Lemma: sig, S0POS: PN|UTR/NEU|SIN/PLU|DEF|OBJ, S0S1Distance: 1, S0Token: sig, S1B0Lemma: säga_inte, S1B0LemmaPOS: säga_AB, S1B0POS: VB|PRS|AKT_AB, S1B0POSLemma: VB|PRS|AKT_inte, S1B0Token: säger_inte, S1IsInLexic: true, S1Lemma: säga, S1POS: VB|PRS|AKT, S1S0B0Lemma: säga_sig_inte, S1S0B0LemmaPOS: säga_PN|UTR/NEU|SIN/PLU|DEF|OBJ_AB, S1S0B0POS: VB|PRS|AKT_PN|UTR/NEU|SIN/PLU|DEF|OBJ_AB, S1S0B0POSLemma: VB|PRS|AKT_PN|UTR/NEU|SIN/PLU|DEF|OBJ_inte, S1S0B0Token: säger_sig_inte, S1S0Lemma: säga_sig, S1S0LemmaPOS: säga_PN|UTR/NEU|SIN/PLU|DEF|OBJ, S1S0POS: VB|PRS|AKT_PN|UTR/NEU|SIN/PLU|DEF|OBJ, S1S0POSLemma: VB|PRS|AKT_sig, S1S0Token: säger_sig, S1Token: säger, StackLengthIs: 2, SyntaxicRelation: +dobj, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

23- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[säger, sig]]   B= [inte, ha, tagit ,.. ]

B0Lemma: inte, B0POS: AB, B0Token: inte, B1IsInLexic: true, B1Lemma: ha, B1POS: VB|INF|AKT, B1Token: ha, S0B0Distance: 1, S0B0Lemma: säga_sig_inte, S0B0LemmaPOS: säga_sig_AB, S0B0POS: VB|PRS|AKT_PN|UTR/NEU|SIN/PLU|DEF|OBJ_AB, S0B0POSLemma: VB|PRS|AKT_PN|UTR/NEU|SIN/PLU|DEF|OBJ_inte, S0B0Token: säger_sig_inte, S0B1Lemma: säga_sig_ha, S0B1LemmaPOS: säga_sig_VB|INF|AKT, S0B1POS: VB|PRS|AKT_PN|UTR/NEU|SIN/PLU|DEF|OBJ_VB|INF|AKT, S0B1POSLemma: VB|PRS|AKT_PN|UTR/NEU|SIN/PLU|DEF|OBJ_ha, S0B1Token: säger_sig_ha, S0B2Lemma: säga_sig_ta, S0B2LemmaPOS: säga_sig_VB|SUP|AKT, S0B2POS: VB|PRS|AKT_PN|UTR/NEU|SIN/PLU|DEF|OBJ_VB|SUP|AKT, S0B2POSLemma: VB|PRS|AKT_PN|UTR/NEU|SIN/PLU|DEF|OBJ_ta, S0B2Token: säger_sig_tagit, S0Lemma: säga_sig, S0POS: VB|PRS|AKT_PN|UTR/NEU|SIN/PLU|DEF|OBJ, S0Token: säger_sig, TransHistory1: 0, TransHistory2: 00, TransHistory3: 002, 

24- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [inte, ha, tagit ,.. ]

B0Lemma: inte, B0POS: AB, B0Token: inte, B1IsInLexic: true, B1Lemma: ha, B1POS: VB|INF|AKT, B1Token: ha, TransHistory1: 1, TransHistory2: 10, TransHistory3: 100, 

25- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [inte]   B= [ha, tagit, ett ,.. ]

B0IsInLexic: true, B0Lemma: ha, B0POS: VB|INF|AKT, B0Token: ha, B1IsInLexic: true, B1Lemma: ta, B1POS: VB|SUP|AKT, B1Token: tagit, S0B0Distance: 1, S0B0Lemma: inte_ha, S0B0LemmaPOS: inte_VB|INF|AKT, S0B0POS: AB_VB|INF|AKT, S0B0POSLemma: AB_ha, S0B0Token: inte_ha, S0B1Lemma: inte_ta, S0B1LemmaPOS: inte_VB|SUP|AKT, S0B1POS: AB_VB|SUP|AKT, S0B1POSLemma: AB_ta, S0B1Token: inte_tagit, S0B2Lemma: inte_en, S0B2LemmaPOS: inte_DT|NEU|SIN|IND, S0B2POS: AB_DT|NEU|SIN|IND, S0B2POSLemma: AB_en, S0B2Token: inte_ett, S0Lemma: inte, S0POS: AB, S0Token: inte, TransHistory1: 2, TransHistory2: 21, TransHistory3: 210, 

26- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ha, tagit, ett ,.. ]

B0IsInLexic: true, B0Lemma: ha, B0POS: VB|INF|AKT, B0Token: ha, B1IsInLexic: true, B1Lemma: ta, B1POS: VB|SUP|AKT, B1Token: tagit, TransHistory1: 0, TransHistory2: 02, TransHistory3: 021, 

27- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ha]   B= [tagit, ett, slutgiltigt ,.. ]

B0IsInLexic: true, B0Lemma: ta, B0POS: VB|SUP|AKT, B0Token: tagit, B1IsInLexic: true, B1Lemma: en, B1POS: DT|NEU|SIN|IND, B1Token: ett, S0B0Distance: 1, S0B0Lemma: ha_ta, S0B0LemmaPOS: ha_VB|SUP|AKT, S0B0POS: VB|INF|AKT_VB|SUP|AKT, S0B0POSLemma: VB|INF|AKT_ta, S0B0Token: ha_tagit, S0B1Lemma: ha_en, S0B1LemmaPOS: ha_DT|NEU|SIN|IND, S0B1POS: VB|INF|AKT_DT|NEU|SIN|IND, S0B1POSLemma: VB|INF|AKT_en, S0B1Token: ha_ett, S0B2Lemma: ha_slutgiltig, S0B2LemmaPOS: ha_JJ|POS|NEU|SIN|IND|NOM, S0B2POS: VB|INF|AKT_JJ|POS|NEU|SIN|IND|NOM, S0B2POSLemma: VB|INF|AKT_slutgiltig, S0B2Token: ha_slutgiltigt, S0IsInLexic: true, S0Lemma: ha, S0POS: VB|INF|AKT, S0Token: ha, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, ha_isGouvernedBy_ta: true, ha_isGouvernedBy_ta_aux: true, 

28- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [tagit, ett, slutgiltigt ,.. ]

B0IsInLexic: true, B0Lemma: ta, B0POS: VB|SUP|AKT, B0Token: tagit, B1IsInLexic: true, B1Lemma: en, B1POS: DT|NEU|SIN|IND, B1Token: ett, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

29- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [tagit]   B= [ett, slutgiltigt, beslut ,.. ]

B0IsInLexic: true, B0Lemma: en, B0POS: DT|NEU|SIN|IND, B0Token: ett, B1Lemma: slutgiltig, B1POS: JJ|POS|NEU|SIN|IND|NOM, B1Token: slutgiltigt, S0B0Distance: 1, S0B0Lemma: ta_en, S0B0LemmaPOS: ta_DT|NEU|SIN|IND, S0B0POS: VB|SUP|AKT_DT|NEU|SIN|IND, S0B0POSLemma: VB|SUP|AKT_en, S0B0Token: tagit_ett, S0B1Lemma: ta_slutgiltig, S0B1LemmaPOS: ta_JJ|POS|NEU|SIN|IND|NOM, S0B1POS: VB|SUP|AKT_JJ|POS|NEU|SIN|IND|NOM, S0B1POSLemma: VB|SUP|AKT_slutgiltig, S0B1Token: tagit_slutgiltigt, S0B2Lemma: ta_beslut, S0B2LemmaPOS: ta_NN|NEU|SIN|IND|NOM, S0B2POS: VB|SUP|AKT_NN|NEU|SIN|IND|NOM, S0B2POSLemma: VB|SUP|AKT_beslut, S0B2Token: tagit_beslut, S0IsInLexic: true, S0Lemma: ta, S0POS: VB|SUP|AKT, S0Token: tagit, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, hasRighDep_dobj: true, ta_beslut_hasRighDep_dobj: true, ta_hasRighDep_dobj: true, 

30- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [tagit, ett]   B= [slutgiltigt, beslut, . ,.. ]

B0Lemma: slutgiltig, B0POS: JJ|POS|NEU|SIN|IND|NOM, B0Token: slutgiltigt, B1IsInLexic: true, B1Lemma: beslut, B1POS: NN|NEU|SIN|IND|NOM, B1Token: beslut, S0B0Distance: 1, S0B0Lemma: en_slutgiltig, S0B0LemmaPOS: en_JJ|POS|NEU|SIN|IND|NOM, S0B0POS: DT|NEU|SIN|IND_JJ|POS|NEU|SIN|IND|NOM, S0B0POSLemma: DT|NEU|SIN|IND_slutgiltig, S0B0Token: ett_slutgiltigt, S0B1Lemma: en_beslut, S0B1LemmaPOS: en_NN|NEU|SIN|IND|NOM, S0B1POS: DT|NEU|SIN|IND_NN|NEU|SIN|IND|NOM, S0B1POSLemma: DT|NEU|SIN|IND_beslut, S0B1Token: ett_beslut, S0B2Lemma: en_., S0B2LemmaPOS: en_MAD, S0B2POS: DT|NEU|SIN|IND_MAD, S0B2POSLemma: DT|NEU|SIN|IND_., S0B2Token: ett_., S0IsInLexic: true, S0Lemma: en, S0POS: DT|NEU|SIN|IND, S0S1Distance: 1, S0Token: ett, S1B0Lemma: ta_slutgiltig, S1B0LemmaPOS: ta_JJ|POS|NEU|SIN|IND|NOM, S1B0POS: VB|SUP|AKT_JJ|POS|NEU|SIN|IND|NOM, S1B0POSLemma: VB|SUP|AKT_slutgiltig, S1B0Token: tagit_slutgiltigt, S1IsInLexic: true, S1Lemma: ta, S1POS: VB|SUP|AKT, S1S0B0Lemma: ta_en_slutgiltig, S1S0B0LemmaPOS: ta_DT|NEU|SIN|IND_JJ|POS|NEU|SIN|IND|NOM, S1S0B0POS: VB|SUP|AKT_DT|NEU|SIN|IND_JJ|POS|NEU|SIN|IND|NOM, S1S0B0POSLemma: VB|SUP|AKT_DT|NEU|SIN|IND_slutgiltig, S1S0B0Token: tagit_ett_slutgiltigt, S1S0Lemma: ta_en, S1S0LemmaPOS: ta_DT|NEU|SIN|IND, S1S0POS: VB|SUP|AKT_DT|NEU|SIN|IND, S1S0POSLemma: VB|SUP|AKT_en, S1S0Token: tagit_ett, S1Token: tagit, StackLengthIs: 2, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, en_isGouvernedBy_beslut: true, en_isGouvernedBy_beslut_det: true, 

31- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [tagit]   B= [slutgiltigt, beslut, . ,.. ]

B0Lemma: slutgiltig, B0POS: JJ|POS|NEU|SIN|IND|NOM, B0Token: slutgiltigt, B1IsInLexic: true, B1Lemma: beslut, B1POS: NN|NEU|SIN|IND|NOM, B1Token: beslut, S0B0Distance: 2, S0B0Lemma: ta_slutgiltig, S0B0LemmaPOS: ta_JJ|POS|NEU|SIN|IND|NOM, S0B0POS: VB|SUP|AKT_JJ|POS|NEU|SIN|IND|NOM, S0B0POSLemma: VB|SUP|AKT_slutgiltig, S0B0Token: tagit_slutgiltigt, S0B1Lemma: ta_beslut, S0B1LemmaPOS: ta_NN|NEU|SIN|IND|NOM, S0B1POS: VB|SUP|AKT_NN|NEU|SIN|IND|NOM, S0B1POSLemma: VB|SUP|AKT_beslut, S0B1Token: tagit_beslut, S0B2Lemma: ta_., S0B2LemmaPOS: ta_MAD, S0B2POS: VB|SUP|AKT_MAD, S0B2POSLemma: VB|SUP|AKT_., S0B2Token: tagit_., S0IsInLexic: true, S0Lemma: ta, S0POS: VB|SUP|AKT, S0Token: tagit, TransHistory1: 0, TransHistory2: 00, TransHistory3: 002, hasRighDep_dobj: true, ta_beslut_hasRighDep_dobj: true, ta_hasRighDep_dobj: true, 

32- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [tagit, slutgiltigt]   B= [beslut, . ,.. ]

B0IsInLexic: true, B0Lemma: beslut, B0POS: NN|NEU|SIN|IND|NOM, B0Token: beslut, B1Lemma: ., B1POS: MAD, B1Token: ., S0B0Distance: 1, S0B0Lemma: slutgiltig_beslut, S0B0LemmaPOS: slutgiltig_NN|NEU|SIN|IND|NOM, S0B0POS: JJ|POS|NEU|SIN|IND|NOM_NN|NEU|SIN|IND|NOM, S0B0POSLemma: JJ|POS|NEU|SIN|IND|NOM_beslut, S0B0Token: slutgiltigt_beslut, S0B1Lemma: slutgiltig_., S0B1LemmaPOS: slutgiltig_MAD, S0B1POS: JJ|POS|NEU|SIN|IND|NOM_MAD, S0B1POSLemma: JJ|POS|NEU|SIN|IND|NOM_., S0B1Token: slutgiltigt_., S0Lemma: slutgiltig, S0POS: JJ|POS|NEU|SIN|IND|NOM, S0S1Distance: 2, S0Token: slutgiltigt, S1B0Lemma: ta_beslut, S1B0LemmaPOS: ta_NN|NEU|SIN|IND|NOM, S1B0POS: VB|SUP|AKT_NN|NEU|SIN|IND|NOM, S1B0POSLemma: VB|SUP|AKT_beslut, S1B0Token: tagit_beslut, S1IsInLexic: true, S1Lemma: ta, S1POS: VB|SUP|AKT, S1S0B0Lemma: ta_slutgiltig_beslut, S1S0B0LemmaPOS: ta_JJ|POS|NEU|SIN|IND|NOM_NN|NEU|SIN|IND|NOM, S1S0B0POS: VB|SUP|AKT_JJ|POS|NEU|SIN|IND|NOM_NN|NEU|SIN|IND|NOM, S1S0B0POSLemma: VB|SUP|AKT_JJ|POS|NEU|SIN|IND|NOM_beslut, S1S0B0Token: tagit_slutgiltigt_beslut, S1S0Lemma: ta_slutgiltig, S1S0LemmaPOS: ta_JJ|POS|NEU|SIN|IND|NOM, S1S0POS: VB|SUP|AKT_JJ|POS|NEU|SIN|IND|NOM, S1S0POSLemma: VB|SUP|AKT_slutgiltig, S1S0Token: tagit_slutgiltigt, S1Token: tagit, StackLengthIs: 2, TransHistory1: 2, TransHistory2: 20, TransHistory3: 200, slutgiltig_isGouvernedBy_beslut: true, slutgiltig_isGouvernedBy_beslut_amod: true, 

33- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [tagit]   B= [beslut, . ,.. ]

B0IsInLexic: true, B0Lemma: beslut, B0POS: NN|NEU|SIN|IND|NOM, B0Token: beslut, B1Lemma: ., B1POS: MAD, B1Token: ., S0B0Distance: 3, S0B0Lemma: ta_beslut, S0B0LemmaPOS: ta_NN|NEU|SIN|IND|NOM, S0B0POS: VB|SUP|AKT_NN|NEU|SIN|IND|NOM, S0B0POSLemma: VB|SUP|AKT_beslut, S0B0Token: tagit_beslut, S0B1Lemma: ta_., S0B1LemmaPOS: ta_MAD, S0B1POS: VB|SUP|AKT_MAD, S0B1POSLemma: VB|SUP|AKT_., S0B1Token: tagit_., S0IsInLexic: true, S0Lemma: ta, S0POS: VB|SUP|AKT, S0Token: tagit, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, hasRighDep_dobj: true, ta_beslut_hasRighDep_dobj: true, ta_hasRighDep_dobj: true, 

34- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [tagit, beslut]   B= [.]

B0Lemma: ., B0POS: MAD, B0Token: ., S0B0Distance: 1, S0B0Lemma: beslut_., S0B0LemmaPOS: beslut_MAD, S0B0POS: NN|NEU|SIN|IND|NOM_MAD, S0B0POSLemma: NN|NEU|SIN|IND|NOM_., S0B0Token: beslut_., S0IsInLexic: true, S0Lemma: beslut, S0POS: NN|NEU|SIN|IND|NOM, S0S1Distance: 3, S0Token: beslut, S1B0Lemma: ta_., S1B0LemmaPOS: ta_MAD, S1B0POS: VB|SUP|AKT_MAD, S1B0POSLemma: VB|SUP|AKT_., S1B0Token: tagit_., S1IsInLexic: true, S1Lemma: ta, S1POS: VB|SUP|AKT, S1S0B0Lemma: ta_beslut_., S1S0B0LemmaPOS: ta_NN|NEU|SIN|IND|NOM_MAD, S1S0B0POS: VB|SUP|AKT_NN|NEU|SIN|IND|NOM_MAD, S1S0B0POSLemma: VB|SUP|AKT_NN|NEU|SIN|IND|NOM_., S1S0B0Token: tagit_beslut_., S1S0Lemma: ta_beslut, S1S0LemmaPOS: ta_NN|NEU|SIN|IND|NOM, S1S0POS: VB|SUP|AKT_NN|NEU|SIN|IND|NOM, S1S0POSLemma: VB|SUP|AKT_beslut, S1S0Token: tagit_beslut, S1Token: tagit, StackLengthIs: 2, SyntaxicRelation: +dobj, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

35- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[tagit, beslut]]   B= [.]

B0Lemma: ., B0POS: MAD, B0Token: ., S0B0Distance: 1, S0B0Lemma: ta_beslut_., S0B0LemmaPOS: ta_beslut_MAD, S0B0POS: VB|SUP|AKT_NN|NEU|SIN|IND|NOM_MAD, S0B0POSLemma: VB|SUP|AKT_NN|NEU|SIN|IND|NOM_., S0B0Token: tagit_beslut_., S0Lemma: ta_beslut, S0POS: VB|SUP|AKT_NN|NEU|SIN|IND|NOM, S0Token: tagit_beslut, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

36- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [.]

B0Lemma: ., B0POS: MAD, B0Token: ., TransHistory1: 1, TransHistory2: 10, TransHistory3: 102, 

37- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [ ]

S0Lemma: ., S0POS: MAD, S0Token: ., TransHistory1: 2, TransHistory2: 21, TransHistory3: 210, 

38- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

## Sentence No. 34 - 
exempelvis erbjöd sig ryssland , som ofta bromsat västmakternas planer på militära ingripanden , i går att hjälpa till med att transportera franska soldater till mali . 
### Existing MWEs: 
1- **erbjöd sig** (IReflV)
2- **hjälpa till** (VPC)



0- &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [exempelvis, erbjöd, sig ,.. ]

B0Lemma: exempelvis, B0POS: AB, B0Token: exempelvis, B1IsInLexic: true, B1Lemma: erbjuda, B1POS: VB|PRT|AKT, B1Token: erbjöd, 

1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [exempelvis]   B= [erbjöd, sig, ryssland ,.. ]

B0IsInLexic: true, B0Lemma: erbjuda, B0POS: VB|PRT|AKT, B0Token: erbjöd, B1IsInLexic: true, B1Lemma: sig, B1POS: PN|UTR/NEU|SIN/PLU|DEF|OBJ, B1Token: sig, S0B0Distance: 1, S0B0Lemma: exempelvis_erbjuda, S0B0LemmaPOS: exempelvis_VB|PRT|AKT, S0B0POS: AB_VB|PRT|AKT, S0B0POSLemma: AB_erbjuda, S0B0Token: exempelvis_erbjöd, S0B1Lemma: exempelvis_sig, S0B1LemmaPOS: exempelvis_PN|UTR/NEU|SIN/PLU|DEF|OBJ, S0B1POS: AB_PN|UTR/NEU|SIN/PLU|DEF|OBJ, S0B1POSLemma: AB_sig, S0B1Token: exempelvis_sig, S0B2Lemma: exempelvis_Ryssland, S0B2LemmaPOS: exempelvis_PM|NOM, S0B2POS: AB_PM|NOM, S0B2POSLemma: AB_Ryssland, S0B2Token: exempelvis_ryssland, S0Lemma: exempelvis, S0POS: AB, S0Token: exempelvis, exempelvis_isGouvernedBy_erbjuda: true, exempelvis_isGouvernedBy_erbjuda_advmod: true, 

2- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [erbjöd, sig, ryssland ,.. ]

B0IsInLexic: true, B0Lemma: erbjuda, B0POS: VB|PRT|AKT, B0Token: erbjöd, B1IsInLexic: true, B1Lemma: sig, B1POS: PN|UTR/NEU|SIN/PLU|DEF|OBJ, B1Token: sig, TransHistory1: 0, 

3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [erbjöd]   B= [sig, ryssland, , ,.. ]

B0IsInLexic: true, B0Lemma: sig, B0POS: PN|UTR/NEU|SIN/PLU|DEF|OBJ, B0Token: sig, B1Lemma: Ryssland, B1POS: PM|NOM, B1Token: ryssland, S0B0Distance: 1, S0B0Lemma: erbjuda_sig, S0B0LemmaPOS: erbjuda_PN|UTR/NEU|SIN/PLU|DEF|OBJ, S0B0POS: VB|PRT|AKT_PN|UTR/NEU|SIN/PLU|DEF|OBJ, S0B0POSLemma: VB|PRT|AKT_sig, S0B0Token: erbjöd_sig, S0B1Lemma: erbjuda_Ryssland, S0B1LemmaPOS: erbjuda_PM|NOM, S0B1POS: VB|PRT|AKT_PM|NOM, S0B1POSLemma: VB|PRT|AKT_Ryssland, S0B1Token: erbjöd_ryssland, S0B2Lemma: erbjuda_,, S0B2LemmaPOS: erbjuda_MID, S0B2POS: VB|PRT|AKT_MID, S0B2POSLemma: VB|PRT|AKT_,, S0B2Token: erbjöd_,, S0IsInLexic: true, S0Lemma: erbjuda, S0POS: VB|PRT|AKT, S0Token: erbjöd, TransHistory1: 2, TransHistory2: 20, 

4- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [erbjöd, sig]   B= [ryssland, ,, som ,.. ]

B0Lemma: Ryssland, B0POS: PM|NOM, B0Token: ryssland, B1Lemma: ,, B1POS: MID, B1Token: ,, S0B0Distance: 1, S0B0Lemma: sig_Ryssland, S0B0LemmaPOS: sig_PM|NOM, S0B0POS: PN|UTR/NEU|SIN/PLU|DEF|OBJ_PM|NOM, S0B0POSLemma: PN|UTR/NEU|SIN/PLU|DEF|OBJ_Ryssland, S0B0Token: sig_ryssland, S0B1Lemma: sig_,, S0B1LemmaPOS: sig_MID, S0B1POS: PN|UTR/NEU|SIN/PLU|DEF|OBJ_MID, S0B1POSLemma: PN|UTR/NEU|SIN/PLU|DEF|OBJ_,, S0B1Token: sig_,, S0B2Lemma: sig_som, S0B2LemmaPOS: sig_HP|-|-|-, S0B2POS: PN|UTR/NEU|SIN/PLU|DEF|OBJ_HP|-|-|-, S0B2POSLemma: PN|UTR/NEU|SIN/PLU|DEF|OBJ_som, S0B2Token: sig_som, S0IsInLexic: true, S0Lemma: sig, S0POS: PN|UTR/NEU|SIN/PLU|DEF|OBJ, S0S1Distance: 1, S0Token: sig, S1B0Lemma: erbjuda_Ryssland, S1B0LemmaPOS: erbjuda_PM|NOM, S1B0POS: VB|PRT|AKT_PM|NOM, S1B0POSLemma: VB|PRT|AKT_Ryssland, S1B0Token: erbjöd_ryssland, S1IsInLexic: true, S1Lemma: erbjuda, S1POS: VB|PRT|AKT, S1S0B0Lemma: erbjuda_sig_Ryssland, S1S0B0LemmaPOS: erbjuda_PN|UTR/NEU|SIN/PLU|DEF|OBJ_PM|NOM, S1S0B0POS: VB|PRT|AKT_PN|UTR/NEU|SIN/PLU|DEF|OBJ_PM|NOM, S1S0B0POSLemma: VB|PRT|AKT_PN|UTR/NEU|SIN/PLU|DEF|OBJ_Ryssland, S1S0B0Token: erbjöd_sig_ryssland, S1S0Lemma: erbjuda_sig, S1S0LemmaPOS: erbjuda_PN|UTR/NEU|SIN/PLU|DEF|OBJ, S1S0POS: VB|PRT|AKT_PN|UTR/NEU|SIN/PLU|DEF|OBJ, S1S0POSLemma: VB|PRT|AKT_sig, S1S0Token: erbjöd_sig, S1Token: erbjöd, StackLengthIs: 2, SyntaxicRelation: +dobj, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

5- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[erbjöd, sig]]   B= [ryssland, ,, som ,.. ]

B0Lemma: Ryssland, B0POS: PM|NOM, B0Token: ryssland, B1Lemma: ,, B1POS: MID, B1Token: ,, S0B0Distance: 1, S0B0Lemma: erbjuda_sig_Ryssland, S0B0LemmaPOS: erbjuda_sig_PM|NOM, S0B0POS: VB|PRT|AKT_PN|UTR/NEU|SIN/PLU|DEF|OBJ_PM|NOM, S0B0POSLemma: VB|PRT|AKT_PN|UTR/NEU|SIN/PLU|DEF|OBJ_Ryssland, S0B0Token: erbjöd_sig_ryssland, S0B1Lemma: erbjuda_sig_,, S0B1LemmaPOS: erbjuda_sig_MID, S0B1POS: VB|PRT|AKT_PN|UTR/NEU|SIN/PLU|DEF|OBJ_MID, S0B1POSLemma: VB|PRT|AKT_PN|UTR/NEU|SIN/PLU|DEF|OBJ_,, S0B1Token: erbjöd_sig_,, S0B2Lemma: erbjuda_sig_som, S0B2LemmaPOS: erbjuda_sig_HP|-|-|-, S0B2POS: VB|PRT|AKT_PN|UTR/NEU|SIN/PLU|DEF|OBJ_HP|-|-|-, S0B2POSLemma: VB|PRT|AKT_PN|UTR/NEU|SIN/PLU|DEF|OBJ_som, S0B2Token: erbjöd_sig_som, S0Lemma: erbjuda_sig, S0POS: VB|PRT|AKT_PN|UTR/NEU|SIN/PLU|DEF|OBJ, S0Token: erbjöd_sig, TransHistory1: 0, TransHistory2: 00, TransHistory3: 002, 

6- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ryssland, ,, som ,.. ]

B0Lemma: Ryssland, B0POS: PM|NOM, B0Token: ryssland, B1Lemma: ,, B1POS: MID, B1Token: ,, TransHistory1: 1, TransHistory2: 10, TransHistory3: 100, 

7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ryssland]   B= [,, som, ofta ,.. ]

B0Lemma: ,, B0POS: MID, B0Token: ,, B1Lemma: som, B1POS: HP|-|-|-, B1Token: som, Ryssland_,_hasRighDep_punct: true, Ryssland_bromsa_hasRighDep_acl:relcl: true, Ryssland_hasRighDep_acl:relcl: true, Ryssland_hasRighDep_punct: true, S0B0Distance: 1, S0B0Lemma: Ryssland_,, S0B0LemmaPOS: Ryssland_MID, S0B0POS: PM|NOM_MID, S0B0POSLemma: PM|NOM_,, S0B0Token: ryssland_,, S0B1Lemma: Ryssland_som, S0B1LemmaPOS: Ryssland_HP|-|-|-, S0B1POS: PM|NOM_HP|-|-|-, S0B1POSLemma: PM|NOM_som, S0B1Token: ryssland_som, S0B2Lemma: Ryssland_ofta, S0B2LemmaPOS: Ryssland_AB|POS, S0B2POS: PM|NOM_AB|POS, S0B2POSLemma: PM|NOM_ofta, S0B2Token: ryssland_ofta, S0Lemma: Ryssland, S0POS: PM|NOM, S0Token: ryssland, TransHistory1: 2, TransHistory2: 21, TransHistory3: 210, hasRighDep_acl:relcl: true, hasRighDep_punct: true, 

8- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, som, ofta ,.. ]

B0Lemma: ,, B0POS: MID, B0Token: ,, B1Lemma: som, B1POS: HP|-|-|-, B1Token: som, TransHistory1: 0, TransHistory2: 02, TransHistory3: 021, 

9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [som, ofta, bromsat ,.. ]

B0Lemma: som, B0POS: HP|-|-|-, B0Token: som, B1Lemma: ofta, B1POS: AB|POS, B1Token: ofta, S0B0Distance: 1, S0B0Lemma: ,_som, S0B0LemmaPOS: ,_HP|-|-|-, S0B0POS: MID_HP|-|-|-, S0B0POSLemma: MID_som, S0B0Token: ,_som, S0B1Lemma: ,_ofta, S0B1LemmaPOS: ,_AB|POS, S0B1POS: MID_AB|POS, S0B1POSLemma: MID_ofta, S0B1Token: ,_ofta, S0B2Lemma: ,_bromsa, S0B2LemmaPOS: ,_VB|SUP|AKT, S0B2POS: MID_VB|SUP|AKT, S0B2POSLemma: MID_bromsa, S0B2Token: ,_bromsat, S0Lemma: ,, S0POS: MID, S0Token: ,, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

10- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [som, ofta, bromsat ,.. ]

B0Lemma: som, B0POS: HP|-|-|-, B0Token: som, B1Lemma: ofta, B1POS: AB|POS, B1Token: ofta, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [som]   B= [ofta, bromsat, västmakternas ,.. ]

B0Lemma: ofta, B0POS: AB|POS, B0Token: ofta, B1Lemma: bromsa, B1POS: VB|SUP|AKT, B1Token: bromsat, S0B0Distance: 1, S0B0Lemma: som_ofta, S0B0LemmaPOS: som_AB|POS, S0B0POS: HP|-|-|-_AB|POS, S0B0POSLemma: HP|-|-|-_ofta, S0B0Token: som_ofta, S0B1Lemma: som_bromsa, S0B1LemmaPOS: som_VB|SUP|AKT, S0B1POS: HP|-|-|-_VB|SUP|AKT, S0B1POSLemma: HP|-|-|-_bromsa, S0B1Token: som_bromsat, S0B2Lemma: som_västmakt, S0B2LemmaPOS: som_NN|UTR|PLU|DEF|GEN, S0B2POS: HP|-|-|-_NN|UTR|PLU|DEF|GEN, S0B2POSLemma: HP|-|-|-_västmakt, S0B2Token: som_västmakternas, S0Lemma: som, S0POS: HP|-|-|-, S0Token: som, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, som_isGouvernedBy_bromsa: true, som_isGouvernedBy_bromsa_nsubj: true, 

12- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ofta, bromsat, västmakternas ,.. ]

B0Lemma: ofta, B0POS: AB|POS, B0Token: ofta, B1Lemma: bromsa, B1POS: VB|SUP|AKT, B1Token: bromsat, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ofta]   B= [bromsat, västmakternas, planer ,.. ]

B0Lemma: bromsa, B0POS: VB|SUP|AKT, B0Token: bromsat, B1Lemma: västmakt, B1POS: NN|UTR|PLU|DEF|GEN, B1Token: västmakternas, S0B0Distance: 1, S0B0Lemma: ofta_bromsa, S0B0LemmaPOS: ofta_VB|SUP|AKT, S0B0POS: AB|POS_VB|SUP|AKT, S0B0POSLemma: AB|POS_bromsa, S0B0Token: ofta_bromsat, S0B1Lemma: ofta_västmakt, S0B1LemmaPOS: ofta_NN|UTR|PLU|DEF|GEN, S0B1POS: AB|POS_NN|UTR|PLU|DEF|GEN, S0B1POSLemma: AB|POS_västmakt, S0B1Token: ofta_västmakternas, S0B2Lemma: ofta_plana, S0B2LemmaPOS: ofta_NN|UTR|PLU|IND|NOM, S0B2POS: AB|POS_NN|UTR|PLU|IND|NOM, S0B2POSLemma: AB|POS_plana, S0B2Token: ofta_planer, S0Lemma: ofta, S0POS: AB|POS, S0Token: ofta, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, ofta_isGouvernedBy_bromsa: true, ofta_isGouvernedBy_bromsa_advmod: true, 

14- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [bromsat, västmakternas, planer ,.. ]

B0Lemma: bromsa, B0POS: VB|SUP|AKT, B0Token: bromsat, B1Lemma: västmakt, B1POS: NN|UTR|PLU|DEF|GEN, B1Token: västmakternas, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [bromsat]   B= [västmakternas, planer, på ,.. ]

B0Lemma: västmakt, B0POS: NN|UTR|PLU|DEF|GEN, B0Token: västmakternas, B1Lemma: plana, B1POS: NN|UTR|PLU|IND|NOM, B1Token: planer, S0B0Distance: 1, S0B0Lemma: bromsa_västmakt, S0B0LemmaPOS: bromsa_NN|UTR|PLU|DEF|GEN, S0B0POS: VB|SUP|AKT_NN|UTR|PLU|DEF|GEN, S0B0POSLemma: VB|SUP|AKT_västmakt, S0B0Token: bromsat_västmakternas, S0B1Lemma: bromsa_plana, S0B1LemmaPOS: bromsa_NN|UTR|PLU|IND|NOM, S0B1POS: VB|SUP|AKT_NN|UTR|PLU|IND|NOM, S0B1POSLemma: VB|SUP|AKT_plana, S0B1Token: bromsat_planer, S0B2Lemma: bromsa_på, S0B2LemmaPOS: bromsa_PP, S0B2POS: VB|SUP|AKT_PP, S0B2POSLemma: VB|SUP|AKT_på, S0B2Token: bromsat_på, S0Lemma: bromsa, S0POS: VB|SUP|AKT, S0Token: bromsat, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, bromsa_hasRighDep_dobj: true, bromsa_plana_hasRighDep_dobj: true, hasRighDep_dobj: true, 

16- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [västmakternas, planer, på ,.. ]

B0Lemma: västmakt, B0POS: NN|UTR|PLU|DEF|GEN, B0Token: västmakternas, B1Lemma: plana, B1POS: NN|UTR|PLU|IND|NOM, B1Token: planer, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [västmakternas]   B= [planer, på, militära ,.. ]

B0Lemma: plana, B0POS: NN|UTR|PLU|IND|NOM, B0Token: planer, B1IsInLexic: true, B1Lemma: på, B1POS: PP, B1Token: på, S0B0Distance: 1, S0B0Lemma: västmakt_plana, S0B0LemmaPOS: västmakt_NN|UTR|PLU|IND|NOM, S0B0POS: NN|UTR|PLU|DEF|GEN_NN|UTR|PLU|IND|NOM, S0B0POSLemma: NN|UTR|PLU|DEF|GEN_plana, S0B0Token: västmakternas_planer, S0B1Lemma: västmakt_på, S0B1LemmaPOS: västmakt_PP, S0B1POS: NN|UTR|PLU|DEF|GEN_PP, S0B1POSLemma: NN|UTR|PLU|DEF|GEN_på, S0B1Token: västmakternas_på, S0B2Lemma: västmakt_militär, S0B2LemmaPOS: västmakt_JJ|POS|UTR/NEU|PLU|IND/DEF|NOM, S0B2POS: NN|UTR|PLU|DEF|GEN_JJ|POS|UTR/NEU|PLU|IND/DEF|NOM, S0B2POSLemma: NN|UTR|PLU|DEF|GEN_militär, S0B2Token: västmakternas_militära, S0Lemma: västmakt, S0POS: NN|UTR|PLU|DEF|GEN, S0Token: västmakternas, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, västmakt_isGouvernedBy_plana: true, västmakt_isGouvernedBy_plana_nmod:poss: true, 

18- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [planer, på, militära ,.. ]

B0Lemma: plana, B0POS: NN|UTR|PLU|IND|NOM, B0Token: planer, B1IsInLexic: true, B1Lemma: på, B1POS: PP, B1Token: på, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [planer]   B= [på, militära, ingripanden ,.. ]

B0IsInLexic: true, B0Lemma: på, B0POS: PP, B0Token: på, B1Lemma: militär, B1POS: JJ|POS|UTR/NEU|PLU|IND/DEF|NOM, B1Token: militära, S0B0Distance: 1, S0B0Lemma: plana_på, S0B0LemmaPOS: plana_PP, S0B0POS: NN|UTR|PLU|IND|NOM_PP, S0B0POSLemma: NN|UTR|PLU|IND|NOM_på, S0B0Token: planer_på, S0B1Lemma: plana_militär, S0B1LemmaPOS: plana_JJ|POS|UTR/NEU|PLU|IND/DEF|NOM, S0B1POS: NN|UTR|PLU|IND|NOM_JJ|POS|UTR/NEU|PLU|IND/DEF|NOM, S0B1POSLemma: NN|UTR|PLU|IND|NOM_militär, S0B1Token: planer_militära, S0B2Lemma: plana_ingripande, S0B2LemmaPOS: plana_NN|NEU|PLU|IND|NOM, S0B2POS: NN|UTR|PLU|IND|NOM_NN|NEU|PLU|IND|NOM, S0B2POSLemma: NN|UTR|PLU|IND|NOM_ingripande, S0B2Token: planer_ingripanden, S0Lemma: plana, S0POS: NN|UTR|PLU|IND|NOM, S0Token: planer, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, hasRighDep_nmod: true, plana_hasRighDep_nmod: true, plana_ingripande_hasRighDep_nmod: true, 

20- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [på, militära, ingripanden ,.. ]

B0IsInLexic: true, B0Lemma: på, B0POS: PP, B0Token: på, B1Lemma: militär, B1POS: JJ|POS|UTR/NEU|PLU|IND/DEF|NOM, B1Token: militära, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [på]   B= [militära, ingripanden, , ,.. ]

B0Lemma: militär, B0POS: JJ|POS|UTR/NEU|PLU|IND/DEF|NOM, B0Token: militära, B1Lemma: ingripande, B1POS: NN|NEU|PLU|IND|NOM, B1Token: ingripanden, S0B0Distance: 1, S0B0Lemma: på_militär, S0B0LemmaPOS: på_JJ|POS|UTR/NEU|PLU|IND/DEF|NOM, S0B0POS: PP_JJ|POS|UTR/NEU|PLU|IND/DEF|NOM, S0B0POSLemma: PP_militär, S0B0Token: på_militära, S0B1Lemma: på_ingripande, S0B1LemmaPOS: på_NN|NEU|PLU|IND|NOM, S0B1POS: PP_NN|NEU|PLU|IND|NOM, S0B1POSLemma: PP_ingripande, S0B1Token: på_ingripanden, S0B2Lemma: på_,, S0B2LemmaPOS: på_MID, S0B2POS: PP_MID, S0B2POSLemma: PP_,, S0B2Token: på_,, S0IsInLexic: true, S0Lemma: på, S0POS: PP, S0Token: på, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, på_isGouvernedBy_ingripande: true, på_isGouvernedBy_ingripande_case: true, 

22- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [militära, ingripanden, , ,.. ]

B0Lemma: militär, B0POS: JJ|POS|UTR/NEU|PLU|IND/DEF|NOM, B0Token: militära, B1Lemma: ingripande, B1POS: NN|NEU|PLU|IND|NOM, B1Token: ingripanden, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

23- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [militära]   B= [ingripanden, ,, i ,.. ]

B0Lemma: ingripande, B0POS: NN|NEU|PLU|IND|NOM, B0Token: ingripanden, B1Lemma: ,, B1POS: MID, B1Token: ,, S0B0Distance: 1, S0B0Lemma: militär_ingripande, S0B0LemmaPOS: militär_NN|NEU|PLU|IND|NOM, S0B0POS: JJ|POS|UTR/NEU|PLU|IND/DEF|NOM_NN|NEU|PLU|IND|NOM, S0B0POSLemma: JJ|POS|UTR/NEU|PLU|IND/DEF|NOM_ingripande, S0B0Token: militära_ingripanden, S0B1Lemma: militär_,, S0B1LemmaPOS: militär_MID, S0B1POS: JJ|POS|UTR/NEU|PLU|IND/DEF|NOM_MID, S0B1POSLemma: JJ|POS|UTR/NEU|PLU|IND/DEF|NOM_,, S0B1Token: militära_,, S0B2Lemma: militär_i, S0B2LemmaPOS: militär_PP, S0B2POS: JJ|POS|UTR/NEU|PLU|IND/DEF|NOM_PP, S0B2POSLemma: JJ|POS|UTR/NEU|PLU|IND/DEF|NOM_i, S0B2Token: militära_i, S0Lemma: militär, S0POS: JJ|POS|UTR/NEU|PLU|IND/DEF|NOM, S0Token: militära, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, militär_isGouvernedBy_ingripande: true, militär_isGouvernedBy_ingripande_amod: true, 

24- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ingripanden, ,, i ,.. ]

B0Lemma: ingripande, B0POS: NN|NEU|PLU|IND|NOM, B0Token: ingripanden, B1Lemma: ,, B1POS: MID, B1Token: ,, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

25- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ingripanden]   B= [,, i, går ,.. ]

B0Lemma: ,, B0POS: MID, B0Token: ,, B1IsInLexic: true, B1Lemma: i, B1POS: PP, B1Token: i, S0B0Distance: 1, S0B0Lemma: ingripande_,, S0B0LemmaPOS: ingripande_MID, S0B0POS: NN|NEU|PLU|IND|NOM_MID, S0B0POSLemma: NN|NEU|PLU|IND|NOM_,, S0B0Token: ingripanden_,, S0B1Lemma: ingripande_i, S0B1LemmaPOS: ingripande_PP, S0B1POS: NN|NEU|PLU|IND|NOM_PP, S0B1POSLemma: NN|NEU|PLU|IND|NOM_i, S0B1Token: ingripanden_i, S0B2Lemma: ingripande_gå, S0B2LemmaPOS: ingripande_VB|PRS|AKT, S0B2POS: NN|NEU|PLU|IND|NOM_VB|PRS|AKT, S0B2POSLemma: NN|NEU|PLU|IND|NOM_gå, S0B2Token: ingripanden_går, S0Lemma: ingripande, S0POS: NN|NEU|PLU|IND|NOM, S0Token: ingripanden, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

26- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, i, går ,.. ]

B0Lemma: ,, B0POS: MID, B0Token: ,, B1IsInLexic: true, B1Lemma: i, B1POS: PP, B1Token: i, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

27- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [i, går, att ,.. ]

B0IsInLexic: true, B0Lemma: i, B0POS: PP, B0Token: i, B1IsInLexic: true, B1Lemma: gå, B1POS: VB|PRS|AKT, B1Token: går, S0B0Distance: 1, S0B0Lemma: ,_i, S0B0LemmaPOS: ,_PP, S0B0POS: MID_PP, S0B0POSLemma: MID_i, S0B0Token: ,_i, S0B1Lemma: ,_gå, S0B1LemmaPOS: ,_VB|PRS|AKT, S0B1POS: MID_VB|PRS|AKT, S0B1POSLemma: MID_gå, S0B1Token: ,_går, S0B2Lemma: ,_att, S0B2LemmaPOS: ,_IE, S0B2POS: MID_IE, S0B2POSLemma: MID_att, S0B2Token: ,_att, S0Lemma: ,, S0POS: MID, S0Token: ,, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

28- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [i, går, att ,.. ]

B0IsInLexic: true, B0Lemma: i, B0POS: PP, B0Token: i, B1IsInLexic: true, B1Lemma: gå, B1POS: VB|PRS|AKT, B1Token: går, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

29- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [i]   B= [går, att, hjälpa ,.. ]

B0IsInLexic: true, B0Lemma: gå, B0POS: VB|PRS|AKT, B0Token: går, B1Lemma: att, B1POS: IE, B1Token: att, S0B0Distance: 1, S0B0Lemma: i_gå, S0B0LemmaPOS: i_VB|PRS|AKT, S0B0POS: PP_VB|PRS|AKT, S0B0POSLemma: PP_gå, S0B0Token: i_går, S0B1Lemma: i_att, S0B1LemmaPOS: i_IE, S0B1POS: PP_IE, S0B1POSLemma: PP_att, S0B1Token: i_att, S0B2Lemma: i_hjälpa, S0B2LemmaPOS: i_VB|INF|AKT, S0B2POS: PP_VB|INF|AKT, S0B2POSLemma: PP_hjälpa, S0B2Token: i_hjälpa, S0IsInLexic: true, S0Lemma: i, S0POS: PP, S0Token: i, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, i_isGouvernedBy_gå: true, i_isGouvernedBy_gå_case: true, 

30- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [går, att, hjälpa ,.. ]

B0IsInLexic: true, B0Lemma: gå, B0POS: VB|PRS|AKT, B0Token: går, B1Lemma: att, B1POS: IE, B1Token: att, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

31- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [går]   B= [att, hjälpa, till ,.. ]

B0Lemma: att, B0POS: IE, B0Token: att, B1IsInLexic: true, B1Lemma: hjälpa, B1POS: VB|INF|AKT, B1Token: hjälpa, S0B0Distance: 1, S0B0Lemma: gå_att, S0B0LemmaPOS: gå_IE, S0B0POS: VB|PRS|AKT_IE, S0B0POSLemma: VB|PRS|AKT_att, S0B0Token: går_att, S0B1Lemma: gå_hjälpa, S0B1LemmaPOS: gå_VB|INF|AKT, S0B1POS: VB|PRS|AKT_VB|INF|AKT, S0B1POSLemma: VB|PRS|AKT_hjälpa, S0B1Token: går_hjälpa, S0B2Lemma: gå_till, S0B2LemmaPOS: gå_PL, S0B2POS: VB|PRS|AKT_PL, S0B2POSLemma: VB|PRS|AKT_till, S0B2Token: går_till, S0IsInLexic: true, S0Lemma: gå, S0POS: VB|PRS|AKT, S0Token: går, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, gå_hasRighDep_xcomp: true, gå_hjälpa_hasRighDep_xcomp: true, hasRighDep_xcomp: true, 

32- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [att, hjälpa, till ,.. ]

B0Lemma: att, B0POS: IE, B0Token: att, B1IsInLexic: true, B1Lemma: hjälpa, B1POS: VB|INF|AKT, B1Token: hjälpa, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

33- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [att]   B= [hjälpa, till, med ,.. ]

B0IsInLexic: true, B0Lemma: hjälpa, B0POS: VB|INF|AKT, B0Token: hjälpa, B1IsInLexic: true, B1Lemma: till, B1POS: PL, B1Token: till, S0B0Distance: 1, S0B0Lemma: att_hjälpa, S0B0LemmaPOS: att_VB|INF|AKT, S0B0POS: IE_VB|INF|AKT, S0B0POSLemma: IE_hjälpa, S0B0Token: att_hjälpa, S0B1Lemma: att_till, S0B1LemmaPOS: att_PL, S0B1POS: IE_PL, S0B1POSLemma: IE_till, S0B1Token: att_till, S0B2Lemma: att_med, S0B2LemmaPOS: att_PP, S0B2POS: IE_PP, S0B2POSLemma: IE_med, S0B2Token: att_med, S0Lemma: att, S0POS: IE, S0Token: att, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, att_isGouvernedBy_hjälpa: true, att_isGouvernedBy_hjälpa_mark: true, 

34- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [hjälpa, till, med ,.. ]

B0IsInLexic: true, B0Lemma: hjälpa, B0POS: VB|INF|AKT, B0Token: hjälpa, B1IsInLexic: true, B1Lemma: till, B1POS: PL, B1Token: till, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

35- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [hjälpa]   B= [till, med, att ,.. ]

B0IsInLexic: true, B0Lemma: till, B0POS: PL, B0Token: till, B1IsInLexic: true, B1Lemma: med, B1POS: PP, B1Token: med, S0B0Distance: 1, S0B0Lemma: hjälpa_till, S0B0LemmaPOS: hjälpa_PL, S0B0POS: VB|INF|AKT_PL, S0B0POSLemma: VB|INF|AKT_till, S0B0Token: hjälpa_till, S0B1Lemma: hjälpa_med, S0B1LemmaPOS: hjälpa_PP, S0B1POS: VB|INF|AKT_PP, S0B1POSLemma: VB|INF|AKT_med, S0B1Token: hjälpa_med, S0B2Lemma: hjälpa_att, S0B2LemmaPOS: hjälpa_IE, S0B2POS: VB|INF|AKT_IE, S0B2POSLemma: VB|INF|AKT_att, S0B2Token: hjälpa_att, S0IsInLexic: true, S0Lemma: hjälpa, S0POS: VB|INF|AKT, S0Token: hjälpa, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, hasRighDep_advcl: true, hasRighDep_compound:prt: true, hjälpa_hasRighDep_advcl: true, hjälpa_hasRighDep_compound:prt: true, hjälpa_till_hasRighDep_compound:prt: true, hjälpa_transportera_hasRighDep_advcl: true, 

36- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [hjälpa, till]   B= [med, att, transportera ,.. ]

B0IsInLexic: true, B0Lemma: med, B0POS: PP, B0Token: med, B1Lemma: att, B1POS: IE, B1Token: att, S0B0Distance: 1, S0B0Lemma: till_med, S0B0LemmaPOS: till_PP, S0B0POS: PL_PP, S0B0POSLemma: PL_med, S0B0Token: till_med, S0B1Lemma: till_att, S0B1LemmaPOS: till_IE, S0B1POS: PL_IE, S0B1POSLemma: PL_att, S0B1Token: till_att, S0B2Lemma: till_transportera, S0B2LemmaPOS: till_VB|INF|AKT, S0B2POS: PL_VB|INF|AKT, S0B2POSLemma: PL_transportera, S0B2Token: till_transportera, S0IsInLexic: true, S0Lemma: till, S0POS: PL, S0S1Distance: 1, S0Token: till, S1B0Lemma: hjälpa_med, S1B0LemmaPOS: hjälpa_PP, S1B0POS: VB|INF|AKT_PP, S1B0POSLemma: VB|INF|AKT_med, S1B0Token: hjälpa_med, S1IsInLexic: true, S1Lemma: hjälpa, S1POS: VB|INF|AKT, S1S0B0Lemma: hjälpa_till_med, S1S0B0LemmaPOS: hjälpa_PL_PP, S1S0B0POS: VB|INF|AKT_PL_PP, S1S0B0POSLemma: VB|INF|AKT_PL_med, S1S0B0Token: hjälpa_till_med, S1S0Lemma: hjälpa_till, S1S0LemmaPOS: hjälpa_PL, S1S0POS: VB|INF|AKT_PL, S1S0POSLemma: VB|INF|AKT_till, S1S0Token: hjälpa_till, S1Token: hjälpa, StackLengthIs: 2, SyntaxicRelation: +compound:prt, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

37- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[hjälpa, till]]   B= [med, att, transportera ,.. ]

B0IsInLexic: true, B0Lemma: med, B0POS: PP, B0Token: med, B1Lemma: att, B1POS: IE, B1Token: att, S0B0Distance: 1, S0B0Lemma: hjälpa_till_med, S0B0LemmaPOS: hjälpa_till_PP, S0B0POS: VB|INF|AKT_PL_PP, S0B0POSLemma: VB|INF|AKT_PL_med, S0B0Token: hjälpa_till_med, S0B1Lemma: hjälpa_till_att, S0B1LemmaPOS: hjälpa_till_IE, S0B1POS: VB|INF|AKT_PL_IE, S0B1POSLemma: VB|INF|AKT_PL_att, S0B1Token: hjälpa_till_att, S0B2Lemma: hjälpa_till_transportera, S0B2LemmaPOS: hjälpa_till_VB|INF|AKT, S0B2POS: VB|INF|AKT_PL_VB|INF|AKT, S0B2POSLemma: VB|INF|AKT_PL_transportera, S0B2Token: hjälpa_till_transportera, S0Lemma: hjälpa_till, S0POS: VB|INF|AKT_PL, S0Token: hjälpa_till, TransHistory1: 0, TransHistory2: 00, TransHistory3: 002, 

38- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [med, att, transportera ,.. ]

B0IsInLexic: true, B0Lemma: med, B0POS: PP, B0Token: med, B1Lemma: att, B1POS: IE, B1Token: att, TransHistory1: 1, TransHistory2: 10, TransHistory3: 100, 

39- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [med]   B= [att, transportera, franska ,.. ]

B0Lemma: att, B0POS: IE, B0Token: att, B1Lemma: transportera, B1POS: VB|INF|AKT, B1Token: transportera, S0B0Distance: 1, S0B0Lemma: med_att, S0B0LemmaPOS: med_IE, S0B0POS: PP_IE, S0B0POSLemma: PP_att, S0B0Token: med_att, S0B1Lemma: med_transportera, S0B1LemmaPOS: med_VB|INF|AKT, S0B1POS: PP_VB|INF|AKT, S0B1POSLemma: PP_transportera, S0B1Token: med_transportera, S0B2Lemma: med_fransk, S0B2LemmaPOS: med_JJ|POS|UTR/NEU|PLU|IND/DEF|NOM, S0B2POS: PP_JJ|POS|UTR/NEU|PLU|IND/DEF|NOM, S0B2POSLemma: PP_fransk, S0B2Token: med_franska, S0IsInLexic: true, S0Lemma: med, S0POS: PP, S0Token: med, TransHistory1: 2, TransHistory2: 21, TransHistory3: 210, med_isGouvernedBy_transportera: true, med_isGouvernedBy_transportera_case: true, 

40- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [att, transportera, franska ,.. ]

B0Lemma: att, B0POS: IE, B0Token: att, B1Lemma: transportera, B1POS: VB|INF|AKT, B1Token: transportera, TransHistory1: 0, TransHistory2: 02, TransHistory3: 021, 

41- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [att]   B= [transportera, franska, soldater ,.. ]

B0Lemma: transportera, B0POS: VB|INF|AKT, B0Token: transportera, B1Lemma: fransk, B1POS: JJ|POS|UTR/NEU|PLU|IND/DEF|NOM, B1Token: franska, S0B0Distance: 1, S0B0Lemma: att_transportera, S0B0LemmaPOS: att_VB|INF|AKT, S0B0POS: IE_VB|INF|AKT, S0B0POSLemma: IE_transportera, S0B0Token: att_transportera, S0B1Lemma: att_fransk, S0B1LemmaPOS: att_JJ|POS|UTR/NEU|PLU|IND/DEF|NOM, S0B1POS: IE_JJ|POS|UTR/NEU|PLU|IND/DEF|NOM, S0B1POSLemma: IE_fransk, S0B1Token: att_franska, S0B2Lemma: att_soldat, S0B2LemmaPOS: att_NN|UTR|PLU|IND|NOM, S0B2POS: IE_NN|UTR|PLU|IND|NOM, S0B2POSLemma: IE_soldat, S0B2Token: att_soldater, S0Lemma: att, S0POS: IE, S0Token: att, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, att_isGouvernedBy_transportera: true, att_isGouvernedBy_transportera_mark: true, 

42- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [transportera, franska, soldater ,.. ]

B0Lemma: transportera, B0POS: VB|INF|AKT, B0Token: transportera, B1Lemma: fransk, B1POS: JJ|POS|UTR/NEU|PLU|IND/DEF|NOM, B1Token: franska, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

43- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [transportera]   B= [franska, soldater, till ,.. ]

B0Lemma: fransk, B0POS: JJ|POS|UTR/NEU|PLU|IND/DEF|NOM, B0Token: franska, B1Lemma: soldat, B1POS: NN|UTR|PLU|IND|NOM, B1Token: soldater, S0B0Distance: 1, S0B0Lemma: transportera_fransk, S0B0LemmaPOS: transportera_JJ|POS|UTR/NEU|PLU|IND/DEF|NOM, S0B0POS: VB|INF|AKT_JJ|POS|UTR/NEU|PLU|IND/DEF|NOM, S0B0POSLemma: VB|INF|AKT_fransk, S0B0Token: transportera_franska, S0B1Lemma: transportera_soldat, S0B1LemmaPOS: transportera_NN|UTR|PLU|IND|NOM, S0B1POS: VB|INF|AKT_NN|UTR|PLU|IND|NOM, S0B1POSLemma: VB|INF|AKT_soldat, S0B1Token: transportera_soldater, S0B2Lemma: transportera_till, S0B2LemmaPOS: transportera_PP, S0B2POS: VB|INF|AKT_PP, S0B2POSLemma: VB|INF|AKT_till, S0B2Token: transportera_till, S0Lemma: transportera, S0POS: VB|INF|AKT, S0Token: transportera, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, hasRighDep_dobj: true, hasRighDep_nmod: true, transportera_Malus_hasRighDep_nmod: true, transportera_hasRighDep_dobj: true, transportera_hasRighDep_nmod: true, transportera_soldat_hasRighDep_dobj: true, 

44- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [franska, soldater, till ,.. ]

B0Lemma: fransk, B0POS: JJ|POS|UTR/NEU|PLU|IND/DEF|NOM, B0Token: franska, B1Lemma: soldat, B1POS: NN|UTR|PLU|IND|NOM, B1Token: soldater, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

45- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [franska]   B= [soldater, till, mali ,.. ]

B0Lemma: soldat, B0POS: NN|UTR|PLU|IND|NOM, B0Token: soldater, B1IsInLexic: true, B1Lemma: till, B1POS: PP, B1Token: till, S0B0Distance: 1, S0B0Lemma: fransk_soldat, S0B0LemmaPOS: fransk_NN|UTR|PLU|IND|NOM, S0B0POS: JJ|POS|UTR/NEU|PLU|IND/DEF|NOM_NN|UTR|PLU|IND|NOM, S0B0POSLemma: JJ|POS|UTR/NEU|PLU|IND/DEF|NOM_soldat, S0B0Token: franska_soldater, S0B1Lemma: fransk_till, S0B1LemmaPOS: fransk_PP, S0B1POS: JJ|POS|UTR/NEU|PLU|IND/DEF|NOM_PP, S0B1POSLemma: JJ|POS|UTR/NEU|PLU|IND/DEF|NOM_till, S0B1Token: franska_till, S0B2Lemma: fransk_Malus, S0B2LemmaPOS: fransk_PM|NOM, S0B2POS: JJ|POS|UTR/NEU|PLU|IND/DEF|NOM_PM|NOM, S0B2POSLemma: JJ|POS|UTR/NEU|PLU|IND/DEF|NOM_Malus, S0B2Token: franska_mali, S0Lemma: fransk, S0POS: JJ|POS|UTR/NEU|PLU|IND/DEF|NOM, S0Token: franska, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, fransk_isGouvernedBy_soldat: true, fransk_isGouvernedBy_soldat_amod: true, 

46- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [soldater, till, mali ,.. ]

B0Lemma: soldat, B0POS: NN|UTR|PLU|IND|NOM, B0Token: soldater, B1IsInLexic: true, B1Lemma: till, B1POS: PP, B1Token: till, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

47- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [soldater]   B= [till, mali, . ,.. ]

B0IsInLexic: true, B0Lemma: till, B0POS: PP, B0Token: till, B1Lemma: Malus, B1POS: PM|NOM, B1Token: mali, S0B0Distance: 1, S0B0Lemma: soldat_till, S0B0LemmaPOS: soldat_PP, S0B0POS: NN|UTR|PLU|IND|NOM_PP, S0B0POSLemma: NN|UTR|PLU|IND|NOM_till, S0B0Token: soldater_till, S0B1Lemma: soldat_Malus, S0B1LemmaPOS: soldat_PM|NOM, S0B1POS: NN|UTR|PLU|IND|NOM_PM|NOM, S0B1POSLemma: NN|UTR|PLU|IND|NOM_Malus, S0B1Token: soldater_mali, S0B2Lemma: soldat_., S0B2LemmaPOS: soldat_MAD, S0B2POS: NN|UTR|PLU|IND|NOM_MAD, S0B2POSLemma: NN|UTR|PLU|IND|NOM_., S0B2Token: soldater_., S0Lemma: soldat, S0POS: NN|UTR|PLU|IND|NOM, S0Token: soldater, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

48- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [till, mali, . ,.. ]

B0IsInLexic: true, B0Lemma: till, B0POS: PP, B0Token: till, B1Lemma: Malus, B1POS: PM|NOM, B1Token: mali, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

49- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [till]   B= [mali, . ,.. ]

B0Lemma: Malus, B0POS: PM|NOM, B0Token: mali, B1Lemma: ., B1POS: MAD, B1Token: ., S0B0Distance: 1, S0B0Lemma: till_Malus, S0B0LemmaPOS: till_PM|NOM, S0B0POS: PP_PM|NOM, S0B0POSLemma: PP_Malus, S0B0Token: till_mali, S0B1Lemma: till_., S0B1LemmaPOS: till_MAD, S0B1POS: PP_MAD, S0B1POSLemma: PP_., S0B1Token: till_., S0IsInLexic: true, S0Lemma: till, S0POS: PP, S0Token: till, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, till_isGouvernedBy_Malus: true, till_isGouvernedBy_Malus_case: true, 

50- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [mali, . ,.. ]

B0Lemma: Malus, B0POS: PM|NOM, B0Token: mali, B1Lemma: ., B1POS: MAD, B1Token: ., TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

51- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [mali]   B= [.]

B0Lemma: ., B0POS: MAD, B0Token: ., S0B0Distance: 1, S0B0Lemma: Malus_., S0B0LemmaPOS: Malus_MAD, S0B0POS: PM|NOM_MAD, S0B0POSLemma: PM|NOM_., S0B0Token: mali_., S0Lemma: Malus, S0POS: PM|NOM, S0Token: mali, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

52- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [.]

B0Lemma: ., B0POS: MAD, B0Token: ., TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

53- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [ ]

S0Lemma: ., S0POS: MAD, S0Token: ., TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

54- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

## Sentence No. 61 - 
det avspeglar sig också i den säsongsbetonade menyn som vi borrade oss ner i medan vi smååt av den goda brödkorgen med malt- , surdegs- och knäckebröd , och ett rört smör därtill . 
### Existing MWEs: 
1- **avspeglar sig** (IReflV)
2- **borrade oss ner** (ID)



0- &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [det, avspeglar, sig ,.. ]

B0Lemma: den, B0POS: PN|NEU|SIN|DEF|SUB/OBJ, B0Token: det, B1IsInLexic: true, B1Lemma: avspegla, B1POS: VB|PRS|AKT, B1Token: avspeglar, 

1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [det]   B= [avspeglar, sig, också ,.. ]

B0IsInLexic: true, B0Lemma: avspegla, B0POS: VB|PRS|AKT, B0Token: avspeglar, B1IsInLexic: true, B1Lemma: sig, B1POS: PN|UTR/NEU|SIN/PLU|DEF|OBJ, B1Token: sig, S0B0Distance: 1, S0B0Lemma: den_avspegla, S0B0LemmaPOS: den_VB|PRS|AKT, S0B0POS: PN|NEU|SIN|DEF|SUB/OBJ_VB|PRS|AKT, S0B0POSLemma: PN|NEU|SIN|DEF|SUB/OBJ_avspegla, S0B0Token: det_avspeglar, S0B1Lemma: den_sig, S0B1LemmaPOS: den_PN|UTR/NEU|SIN/PLU|DEF|OBJ, S0B1POS: PN|NEU|SIN|DEF|SUB/OBJ_PN|UTR/NEU|SIN/PLU|DEF|OBJ, S0B1POSLemma: PN|NEU|SIN|DEF|SUB/OBJ_sig, S0B1Token: det_sig, S0B2Lemma: den_också, S0B2LemmaPOS: den_AB, S0B2POS: PN|NEU|SIN|DEF|SUB/OBJ_AB, S0B2POSLemma: PN|NEU|SIN|DEF|SUB/OBJ_också, S0B2Token: det_också, S0Lemma: den, S0POS: PN|NEU|SIN|DEF|SUB/OBJ, S0Token: det, den_isGouvernedBy_avspegla: true, den_isGouvernedBy_avspegla_nsubj: true, 

2- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [avspeglar, sig, också ,.. ]

B0IsInLexic: true, B0Lemma: avspegla, B0POS: VB|PRS|AKT, B0Token: avspeglar, B1IsInLexic: true, B1Lemma: sig, B1POS: PN|UTR/NEU|SIN/PLU|DEF|OBJ, B1Token: sig, TransHistory1: 0, 

3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [avspeglar]   B= [sig, också, i ,.. ]

B0IsInLexic: true, B0Lemma: sig, B0POS: PN|UTR/NEU|SIN/PLU|DEF|OBJ, B0Token: sig, B1Lemma: också, B1POS: AB, B1Token: också, S0B0Distance: 1, S0B0Lemma: avspegla_sig, S0B0LemmaPOS: avspegla_PN|UTR/NEU|SIN/PLU|DEF|OBJ, S0B0POS: VB|PRS|AKT_PN|UTR/NEU|SIN/PLU|DEF|OBJ, S0B0POSLemma: VB|PRS|AKT_sig, S0B0Token: avspeglar_sig, S0B1Lemma: avspegla_också, S0B1LemmaPOS: avspegla_AB, S0B1POS: VB|PRS|AKT_AB, S0B1POSLemma: VB|PRS|AKT_också, S0B1Token: avspeglar_också, S0B2Lemma: avspegla_i, S0B2LemmaPOS: avspegla_PP, S0B2POS: VB|PRS|AKT_PP, S0B2POSLemma: VB|PRS|AKT_i, S0B2Token: avspeglar_i, S0IsInLexic: true, S0Lemma: avspegla, S0POS: VB|PRS|AKT, S0Token: avspeglar, TransHistory1: 2, TransHistory2: 20, 

4- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [avspeglar, sig]   B= [också, i, den ,.. ]

B0Lemma: också, B0POS: AB, B0Token: också, B1IsInLexic: true, B1Lemma: i, B1POS: PP, B1Token: i, S0B0Distance: 1, S0B0Lemma: sig_också, S0B0LemmaPOS: sig_AB, S0B0POS: PN|UTR/NEU|SIN/PLU|DEF|OBJ_AB, S0B0POSLemma: PN|UTR/NEU|SIN/PLU|DEF|OBJ_också, S0B0Token: sig_också, S0B1Lemma: sig_i, S0B1LemmaPOS: sig_PP, S0B1POS: PN|UTR/NEU|SIN/PLU|DEF|OBJ_PP, S0B1POSLemma: PN|UTR/NEU|SIN/PLU|DEF|OBJ_i, S0B1Token: sig_i, S0B2Lemma: sig_en, S0B2LemmaPOS: sig_DT|UTR|SIN|DEF, S0B2POS: PN|UTR/NEU|SIN/PLU|DEF|OBJ_DT|UTR|SIN|DEF, S0B2POSLemma: PN|UTR/NEU|SIN/PLU|DEF|OBJ_en, S0B2Token: sig_den, S0IsInLexic: true, S0Lemma: sig, S0POS: PN|UTR/NEU|SIN/PLU|DEF|OBJ, S0S1Distance: 1, S0Token: sig, S1B0Lemma: avspegla_också, S1B0LemmaPOS: avspegla_AB, S1B0POS: VB|PRS|AKT_AB, S1B0POSLemma: VB|PRS|AKT_också, S1B0Token: avspeglar_också, S1IsInLexic: true, S1Lemma: avspegla, S1POS: VB|PRS|AKT, S1S0B0Lemma: avspegla_sig_också, S1S0B0LemmaPOS: avspegla_PN|UTR/NEU|SIN/PLU|DEF|OBJ_AB, S1S0B0POS: VB|PRS|AKT_PN|UTR/NEU|SIN/PLU|DEF|OBJ_AB, S1S0B0POSLemma: VB|PRS|AKT_PN|UTR/NEU|SIN/PLU|DEF|OBJ_också, S1S0B0Token: avspeglar_sig_också, S1S0Lemma: avspegla_sig, S1S0LemmaPOS: avspegla_PN|UTR/NEU|SIN/PLU|DEF|OBJ, S1S0POS: VB|PRS|AKT_PN|UTR/NEU|SIN/PLU|DEF|OBJ, S1S0POSLemma: VB|PRS|AKT_sig, S1S0Token: avspeglar_sig, S1Token: avspeglar, StackLengthIs: 2, SyntaxicRelation: +dobj, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

5- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[avspeglar, sig]]   B= [också, i, den ,.. ]

B0Lemma: också, B0POS: AB, B0Token: också, B1IsInLexic: true, B1Lemma: i, B1POS: PP, B1Token: i, S0B0Distance: 1, S0B0Lemma: avspegla_sig_också, S0B0LemmaPOS: avspegla_sig_AB, S0B0POS: VB|PRS|AKT_PN|UTR/NEU|SIN/PLU|DEF|OBJ_AB, S0B0POSLemma: VB|PRS|AKT_PN|UTR/NEU|SIN/PLU|DEF|OBJ_också, S0B0Token: avspeglar_sig_också, S0B1Lemma: avspegla_sig_i, S0B1LemmaPOS: avspegla_sig_PP, S0B1POS: VB|PRS|AKT_PN|UTR/NEU|SIN/PLU|DEF|OBJ_PP, S0B1POSLemma: VB|PRS|AKT_PN|UTR/NEU|SIN/PLU|DEF|OBJ_i, S0B1Token: avspeglar_sig_i, S0B2Lemma: avspegla_sig_en, S0B2LemmaPOS: avspegla_sig_DT|UTR|SIN|DEF, S0B2POS: VB|PRS|AKT_PN|UTR/NEU|SIN/PLU|DEF|OBJ_DT|UTR|SIN|DEF, S0B2POSLemma: VB|PRS|AKT_PN|UTR/NEU|SIN/PLU|DEF|OBJ_en, S0B2Token: avspeglar_sig_den, S0Lemma: avspegla_sig, S0POS: VB|PRS|AKT_PN|UTR/NEU|SIN/PLU|DEF|OBJ, S0Token: avspeglar_sig, TransHistory1: 0, TransHistory2: 00, TransHistory3: 002, 

6- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [också, i, den ,.. ]

B0Lemma: också, B0POS: AB, B0Token: också, B1IsInLexic: true, B1Lemma: i, B1POS: PP, B1Token: i, TransHistory1: 1, TransHistory2: 10, TransHistory3: 100, 

7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [också]   B= [i, den, säsongsbetonade ,.. ]

B0IsInLexic: true, B0Lemma: i, B0POS: PP, B0Token: i, B1IsInLexic: true, B1Lemma: en, B1POS: DT|UTR|SIN|DEF, B1Token: den, S0B0Distance: 1, S0B0Lemma: också_i, S0B0LemmaPOS: också_PP, S0B0POS: AB_PP, S0B0POSLemma: AB_i, S0B0Token: också_i, S0B1Lemma: också_en, S0B1LemmaPOS: också_DT|UTR|SIN|DEF, S0B1POS: AB_DT|UTR|SIN|DEF, S0B1POSLemma: AB_en, S0B1Token: också_den, S0B2Lemma: också_säsongsbetonad, S0B2LemmaPOS: också_JJ|POS|UTR/NEU|SIN|DEF|NOM, S0B2POS: AB_JJ|POS|UTR/NEU|SIN|DEF|NOM, S0B2POSLemma: AB_säsongsbetonad, S0B2Token: också_säsongsbetonade, S0Lemma: också, S0POS: AB, S0Token: också, TransHistory1: 2, TransHistory2: 21, TransHistory3: 210, 

8- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [i, den, säsongsbetonade ,.. ]

B0IsInLexic: true, B0Lemma: i, B0POS: PP, B0Token: i, B1IsInLexic: true, B1Lemma: en, B1POS: DT|UTR|SIN|DEF, B1Token: den, TransHistory1: 0, TransHistory2: 02, TransHistory3: 021, 

9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [i]   B= [den, säsongsbetonade, menyn ,.. ]

B0IsInLexic: true, B0Lemma: en, B0POS: DT|UTR|SIN|DEF, B0Token: den, B1Lemma: säsongsbetonad, B1POS: JJ|POS|UTR/NEU|SIN|DEF|NOM, B1Token: säsongsbetonade, S0B0Distance: 1, S0B0Lemma: i_en, S0B0LemmaPOS: i_DT|UTR|SIN|DEF, S0B0POS: PP_DT|UTR|SIN|DEF, S0B0POSLemma: PP_en, S0B0Token: i_den, S0B1Lemma: i_säsongsbetonad, S0B1LemmaPOS: i_JJ|POS|UTR/NEU|SIN|DEF|NOM, S0B1POS: PP_JJ|POS|UTR/NEU|SIN|DEF|NOM, S0B1POSLemma: PP_säsongsbetonad, S0B1Token: i_säsongsbetonade, S0B2Lemma: i_menyn, S0B2LemmaPOS: i_NN|UTR|SIN|DEF|NOM, S0B2POS: PP_NN|UTR|SIN|DEF|NOM, S0B2POSLemma: PP_menyn, S0B2Token: i_menyn, S0IsInLexic: true, S0Lemma: i, S0POS: PP, S0Token: i, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, i_isGouvernedBy_menyn: true, i_isGouvernedBy_menyn_case: true, 

10- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [den, säsongsbetonade, menyn ,.. ]

B0IsInLexic: true, B0Lemma: en, B0POS: DT|UTR|SIN|DEF, B0Token: den, B1Lemma: säsongsbetonad, B1POS: JJ|POS|UTR/NEU|SIN|DEF|NOM, B1Token: säsongsbetonade, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [den]   B= [säsongsbetonade, menyn, som ,.. ]

B0Lemma: säsongsbetonad, B0POS: JJ|POS|UTR/NEU|SIN|DEF|NOM, B0Token: säsongsbetonade, B1Lemma: menyn, B1POS: NN|UTR|SIN|DEF|NOM, B1Token: menyn, S0B0Distance: 1, S0B0Lemma: en_säsongsbetonad, S0B0LemmaPOS: en_JJ|POS|UTR/NEU|SIN|DEF|NOM, S0B0POS: DT|UTR|SIN|DEF_JJ|POS|UTR/NEU|SIN|DEF|NOM, S0B0POSLemma: DT|UTR|SIN|DEF_säsongsbetonad, S0B0Token: den_säsongsbetonade, S0B1Lemma: en_menyn, S0B1LemmaPOS: en_NN|UTR|SIN|DEF|NOM, S0B1POS: DT|UTR|SIN|DEF_NN|UTR|SIN|DEF|NOM, S0B1POSLemma: DT|UTR|SIN|DEF_menyn, S0B1Token: den_menyn, S0B2Lemma: en_som, S0B2LemmaPOS: en_HP|-|-|-, S0B2POS: DT|UTR|SIN|DEF_HP|-|-|-, S0B2POSLemma: DT|UTR|SIN|DEF_som, S0B2Token: den_som, S0IsInLexic: true, S0Lemma: en, S0POS: DT|UTR|SIN|DEF, S0Token: den, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, en_isGouvernedBy_menyn: true, en_isGouvernedBy_menyn_det: true, 

12- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [säsongsbetonade, menyn, som ,.. ]

B0Lemma: säsongsbetonad, B0POS: JJ|POS|UTR/NEU|SIN|DEF|NOM, B0Token: säsongsbetonade, B1Lemma: menyn, B1POS: NN|UTR|SIN|DEF|NOM, B1Token: menyn, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [säsongsbetonade]   B= [menyn, som, vi ,.. ]

B0Lemma: menyn, B0POS: NN|UTR|SIN|DEF|NOM, B0Token: menyn, B1Lemma: som, B1POS: HP|-|-|-, B1Token: som, S0B0Distance: 1, S0B0Lemma: säsongsbetonad_menyn, S0B0LemmaPOS: säsongsbetonad_NN|UTR|SIN|DEF|NOM, S0B0POS: JJ|POS|UTR/NEU|SIN|DEF|NOM_NN|UTR|SIN|DEF|NOM, S0B0POSLemma: JJ|POS|UTR/NEU|SIN|DEF|NOM_menyn, S0B0Token: säsongsbetonade_menyn, S0B1Lemma: säsongsbetonad_som, S0B1LemmaPOS: säsongsbetonad_HP|-|-|-, S0B1POS: JJ|POS|UTR/NEU|SIN|DEF|NOM_HP|-|-|-, S0B1POSLemma: JJ|POS|UTR/NEU|SIN|DEF|NOM_som, S0B1Token: säsongsbetonade_som, S0B2Lemma: säsongsbetonad_vi, S0B2LemmaPOS: säsongsbetonad_PN|UTR|PLU|DEF|SUB, S0B2POS: JJ|POS|UTR/NEU|SIN|DEF|NOM_PN|UTR|PLU|DEF|SUB, S0B2POSLemma: JJ|POS|UTR/NEU|SIN|DEF|NOM_vi, S0B2Token: säsongsbetonade_vi, S0Lemma: säsongsbetonad, S0POS: JJ|POS|UTR/NEU|SIN|DEF|NOM, S0Token: säsongsbetonade, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, säsongsbetonad_isGouvernedBy_menyn: true, säsongsbetonad_isGouvernedBy_menyn_amod: true, 

14- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [menyn, som, vi ,.. ]

B0Lemma: menyn, B0POS: NN|UTR|SIN|DEF|NOM, B0Token: menyn, B1Lemma: som, B1POS: HP|-|-|-, B1Token: som, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [menyn]   B= [som, vi, borrade ,.. ]

B0Lemma: som, B0POS: HP|-|-|-, B0Token: som, B1IsInLexic: true, B1Lemma: vi, B1POS: PN|UTR|PLU|DEF|SUB, B1Token: vi, S0B0Distance: 1, S0B0Lemma: menyn_som, S0B0LemmaPOS: menyn_HP|-|-|-, S0B0POS: NN|UTR|SIN|DEF|NOM_HP|-|-|-, S0B0POSLemma: NN|UTR|SIN|DEF|NOM_som, S0B0Token: menyn_som, S0B1Lemma: menyn_vi, S0B1LemmaPOS: menyn_PN|UTR|PLU|DEF|SUB, S0B1POS: NN|UTR|SIN|DEF|NOM_PN|UTR|PLU|DEF|SUB, S0B1POSLemma: NN|UTR|SIN|DEF|NOM_vi, S0B1Token: menyn_vi, S0B2Lemma: menyn_borra, S0B2LemmaPOS: menyn_VB|PRT|AKT, S0B2POS: NN|UTR|SIN|DEF|NOM_VB|PRT|AKT, S0B2POSLemma: NN|UTR|SIN|DEF|NOM_borra, S0B2Token: menyn_borrade, S0Lemma: menyn, S0POS: NN|UTR|SIN|DEF|NOM, S0Token: menyn, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, hasRighDep_acl:relcl: true, menyn_borra_hasRighDep_acl:relcl: true, menyn_hasRighDep_acl:relcl: true, 

16- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [som, vi, borrade ,.. ]

B0Lemma: som, B0POS: HP|-|-|-, B0Token: som, B1IsInLexic: true, B1Lemma: vi, B1POS: PN|UTR|PLU|DEF|SUB, B1Token: vi, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [som]   B= [vi, borrade, oss ,.. ]

B0IsInLexic: true, B0Lemma: vi, B0POS: PN|UTR|PLU|DEF|SUB, B0Token: vi, B1IsInLexic: true, B1Lemma: borra, B1POS: VB|PRT|AKT, B1Token: borrade, S0B0Distance: 1, S0B0Lemma: som_vi, S0B0LemmaPOS: som_PN|UTR|PLU|DEF|SUB, S0B0POS: HP|-|-|-_PN|UTR|PLU|DEF|SUB, S0B0POSLemma: HP|-|-|-_vi, S0B0Token: som_vi, S0B1Lemma: som_borra, S0B1LemmaPOS: som_VB|PRT|AKT, S0B1POS: HP|-|-|-_VB|PRT|AKT, S0B1POSLemma: HP|-|-|-_borra, S0B1Token: som_borrade, S0B2Lemma: som_vi, S0B2LemmaPOS: som_PN|UTR|PLU|DEF|OBJ, S0B2POS: HP|-|-|-_PN|UTR|PLU|DEF|OBJ, S0B2POSLemma: HP|-|-|-_vi, S0B2Token: som_oss, S0Lemma: som, S0POS: HP|-|-|-, S0Token: som, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, som_isGouvernedBy_borra: true, som_isGouvernedBy_borra_dobj: true, 

18- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [vi, borrade, oss ,.. ]

B0IsInLexic: true, B0Lemma: vi, B0POS: PN|UTR|PLU|DEF|SUB, B0Token: vi, B1IsInLexic: true, B1Lemma: borra, B1POS: VB|PRT|AKT, B1Token: borrade, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [vi]   B= [borrade, oss, ner ,.. ]

B0IsInLexic: true, B0Lemma: borra, B0POS: VB|PRT|AKT, B0Token: borrade, B1IsInLexic: true, B1Lemma: vi, B1POS: PN|UTR|PLU|DEF|OBJ, B1Token: oss, S0B0Distance: 1, S0B0Lemma: vi_borra, S0B0LemmaPOS: vi_VB|PRT|AKT, S0B0POS: PN|UTR|PLU|DEF|SUB_VB|PRT|AKT, S0B0POSLemma: PN|UTR|PLU|DEF|SUB_borra, S0B0Token: vi_borrade, S0B1Lemma: vi_vi, S0B1LemmaPOS: vi_PN|UTR|PLU|DEF|OBJ, S0B1POS: PN|UTR|PLU|DEF|SUB_PN|UTR|PLU|DEF|OBJ, S0B1POSLemma: PN|UTR|PLU|DEF|SUB_vi, S0B1Token: vi_oss, S0B2Lemma: vi_ner, S0B2LemmaPOS: vi_AB, S0B2POS: PN|UTR|PLU|DEF|SUB_AB, S0B2POSLemma: PN|UTR|PLU|DEF|SUB_ner, S0B2Token: vi_ner, S0IsInLexic: true, S0Lemma: vi, S0POS: PN|UTR|PLU|DEF|SUB, S0Token: vi, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, vi_isGouvernedBy_borra: true, vi_isGouvernedBy_borra_nsubj: true, 

20- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [borrade, oss, ner ,.. ]

B0IsInLexic: true, B0Lemma: borra, B0POS: VB|PRT|AKT, B0Token: borrade, B1IsInLexic: true, B1Lemma: vi, B1POS: PN|UTR|PLU|DEF|OBJ, B1Token: oss, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [borrade]   B= [oss, ner, i ,.. ]

B0IsInLexic: true, B0Lemma: vi, B0POS: PN|UTR|PLU|DEF|OBJ, B0Token: oss, B1IsInLexic: true, B1Lemma: ner, B1POS: AB, B1Token: ner, S0B0Distance: 1, S0B0Lemma: borra_vi, S0B0LemmaPOS: borra_PN|UTR|PLU|DEF|OBJ, S0B0POS: VB|PRT|AKT_PN|UTR|PLU|DEF|OBJ, S0B0POSLemma: VB|PRT|AKT_vi, S0B0Token: borrade_oss, S0B1Lemma: borra_ner, S0B1LemmaPOS: borra_AB, S0B1POS: VB|PRT|AKT_AB, S0B1POSLemma: VB|PRT|AKT_ner, S0B1Token: borrade_ner, S0B2Lemma: borra_i, S0B2LemmaPOS: borra_PP, S0B2POS: VB|PRT|AKT_PP, S0B2POSLemma: VB|PRT|AKT_i, S0B2Token: borrade_i, S0IsInLexic: true, S0Lemma: borra, S0POS: VB|PRT|AKT, S0Token: borrade, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, borra_hasRighDep_advcl: true, borra_hasRighDep_compound:prt: true, borra_hasRighDep_dobj: true, borra_ner_hasRighDep_compound:prt: true, borra_smååta_hasRighDep_advcl: true, borra_vi_hasRighDep_dobj: true, hasRighDep_advcl: true, hasRighDep_compound:prt: true, hasRighDep_dobj: true, 

22- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [borrade, oss]   B= [ner, i, medan ,.. ]

B0IsInLexic: true, B0Lemma: ner, B0POS: AB, B0Token: ner, B1IsInLexic: true, B1Lemma: i, B1POS: PP, B1Token: i, S0B0Distance: 1, S0B0Lemma: vi_ner, S0B0LemmaPOS: vi_AB, S0B0POS: PN|UTR|PLU|DEF|OBJ_AB, S0B0POSLemma: PN|UTR|PLU|DEF|OBJ_ner, S0B0Token: oss_ner, S0B1Lemma: vi_i, S0B1LemmaPOS: vi_PP, S0B1POS: PN|UTR|PLU|DEF|OBJ_PP, S0B1POSLemma: PN|UTR|PLU|DEF|OBJ_i, S0B1Token: oss_i, S0B2Lemma: vi_medan, S0B2LemmaPOS: vi_SN, S0B2POS: PN|UTR|PLU|DEF|OBJ_SN, S0B2POSLemma: PN|UTR|PLU|DEF|OBJ_medan, S0B2Token: oss_medan, S0IsInLexic: true, S0Lemma: vi, S0POS: PN|UTR|PLU|DEF|OBJ, S0S1Distance: 1, S0Token: oss, S1B0Lemma: borra_ner, S1B0LemmaPOS: borra_AB, S1B0POS: VB|PRT|AKT_AB, S1B0POSLemma: VB|PRT|AKT_ner, S1B0Token: borrade_ner, S1IsInLexic: true, S1Lemma: borra, S1POS: VB|PRT|AKT, S1S0B0Lemma: borra_vi_ner, S1S0B0LemmaPOS: borra_PN|UTR|PLU|DEF|OBJ_AB, S1S0B0POS: VB|PRT|AKT_PN|UTR|PLU|DEF|OBJ_AB, S1S0B0POSLemma: VB|PRT|AKT_PN|UTR|PLU|DEF|OBJ_ner, S1S0B0Token: borrade_oss_ner, S1S0Lemma: borra_vi, S1S0LemmaPOS: borra_PN|UTR|PLU|DEF|OBJ, S1S0POS: VB|PRT|AKT_PN|UTR|PLU|DEF|OBJ, S1S0POSLemma: VB|PRT|AKT_vi, S1S0Token: borrade_oss, S1Token: borrade, StackLengthIs: 2, SyntaxicRelation: +dobj, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

23- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [borrade, oss, ner]   B= [i, medan, vi ,.. ]

B0IsInLexic: true, B0Lemma: i, B0POS: PP, B0Token: i, B1Lemma: medan, B1POS: SN, B1Token: medan, S0B0Distance: 1, S0B0Lemma: ner_i, S0B0LemmaPOS: ner_PP, S0B0POS: AB_PP, S0B0POSLemma: AB_i, S0B0Token: ner_i, S0B1Lemma: ner_medan, S0B1LemmaPOS: ner_SN, S0B1POS: AB_SN, S0B1POSLemma: AB_medan, S0B1Token: ner_medan, S0B2Lemma: ner_vi, S0B2LemmaPOS: ner_PN|UTR|PLU|DEF|SUB, S0B2POS: AB_PN|UTR|PLU|DEF|SUB, S0B2POSLemma: AB_vi, S0B2Token: ner_vi, S0IsInLexic: true, S0Lemma: ner, S0POS: AB, S0S1Distance: 1, S0Token: ner, S1B0Lemma: vi_i, S1B0LemmaPOS: vi_PP, S1B0POS: PN|UTR|PLU|DEF|OBJ_PP, S1B0POSLemma: PN|UTR|PLU|DEF|OBJ_i, S1B0Token: oss_i, S1IsInLexic: true, S1Lemma: vi, S1POS: PN|UTR|PLU|DEF|OBJ, S1S0B0Lemma: vi_ner_i, S1S0B0LemmaPOS: vi_AB_PP, S1S0B0POS: PN|UTR|PLU|DEF|OBJ_AB_PP, S1S0B0POSLemma: PN|UTR|PLU|DEF|OBJ_AB_i, S1S0B0Token: oss_ner_i, S1S0Lemma: vi_ner, S1S0LemmaPOS: vi_AB, S1S0POS: PN|UTR|PLU|DEF|OBJ_AB, S1S0POSLemma: PN|UTR|PLU|DEF|OBJ_ner, S1S0Token: oss_ner, S1Token: oss, StackLengthIs: 3, TransHistory1: 0, TransHistory2: 00, TransHistory3: 002, 

24- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [borrade, [oss, ner]]   B= [i, medan, vi ,.. ]

B0IsInLexic: true, B0Lemma: i, B0POS: PP, B0Token: i, B1Lemma: medan, B1POS: SN, B1Token: medan, S0B0Distance: 1, S0B0Lemma: vi_ner_i, S0B0LemmaPOS: vi_ner_PP, S0B0POS: PN|UTR|PLU|DEF|OBJ_AB_PP, S0B0POSLemma: PN|UTR|PLU|DEF|OBJ_AB_i, S0B0Token: oss_ner_i, S0B1Lemma: vi_ner_medan, S0B1LemmaPOS: vi_ner_SN, S0B1POS: PN|UTR|PLU|DEF|OBJ_AB_SN, S0B1POSLemma: PN|UTR|PLU|DEF|OBJ_AB_medan, S0B1Token: oss_ner_medan, S0B2Lemma: vi_ner_vi, S0B2LemmaPOS: vi_ner_PN|UTR|PLU|DEF|SUB, S0B2POS: PN|UTR|PLU|DEF|OBJ_AB_PN|UTR|PLU|DEF|SUB, S0B2POSLemma: PN|UTR|PLU|DEF|OBJ_AB_vi, S0B2Token: oss_ner_vi, S0Lemma: vi_ner, S0POS: PN|UTR|PLU|DEF|OBJ_AB, S0Token: oss_ner, S1B0Lemma: borra_i, S1B0LemmaPOS: borra_PP, S1B0POS: VB|PRT|AKT_PP, S1B0POSLemma: VB|PRT|AKT_i, S1B0Token: borrade_i, S1IsInLexic: true, S1Lemma: borra, S1POS: VB|PRT|AKT, S1S0B0Lemma: borra_vi_ner_i, S1S0B0LemmaPOS: borra_PN|UTR|PLU|DEF|OBJ_AB_PP, S1S0B0POS: VB|PRT|AKT_PN|UTR|PLU|DEF|OBJ_AB_PP, S1S0B0POSLemma: VB|PRT|AKT_PN|UTR|PLU|DEF|OBJ_AB_i, S1S0B0Token: borrade_oss_ner_i, S1S0Lemma: borra_vi_ner, S1S0LemmaPOS: borra_PN|UTR|PLU|DEF|OBJ_AB, S1S0POS: VB|PRT|AKT_PN|UTR|PLU|DEF|OBJ_AB, S1S0POSLemma: VB|PRT|AKT_vi_ner, S1S0Token: borrade_oss_ner, S1Token: borrade, StackLengthIs: 2, TransHistory1: 0, TransHistory2: 00, TransHistory3: 000, 

25- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[borrade, [oss, ner]]]   B= [i, medan, vi ,.. ]

B0IsInLexic: true, B0Lemma: i, B0POS: PP, B0Token: i, B1Lemma: medan, B1POS: SN, B1Token: medan, S0B0Distance: 1, S0B0Lemma: borra_vi_ner_i, S0B0LemmaPOS: borra_vi_ner_PP, S0B0POS: VB|PRT|AKT_PN|UTR|PLU|DEF|OBJ_AB_PP, S0B0POSLemma: VB|PRT|AKT_PN|UTR|PLU|DEF|OBJ_AB_i, S0B0Token: borrade_oss_ner_i, S0B1Lemma: borra_vi_ner_medan, S0B1LemmaPOS: borra_vi_ner_SN, S0B1POS: VB|PRT|AKT_PN|UTR|PLU|DEF|OBJ_AB_SN, S0B1POSLemma: VB|PRT|AKT_PN|UTR|PLU|DEF|OBJ_AB_medan, S0B1Token: borrade_oss_ner_medan, S0B2Lemma: borra_vi_ner_vi, S0B2LemmaPOS: borra_vi_ner_PN|UTR|PLU|DEF|SUB, S0B2POS: VB|PRT|AKT_PN|UTR|PLU|DEF|OBJ_AB_PN|UTR|PLU|DEF|SUB, S0B2POSLemma: VB|PRT|AKT_PN|UTR|PLU|DEF|OBJ_AB_vi, S0B2Token: borrade_oss_ner_vi, S0Lemma: borra_vi_ner, S0POS: VB|PRT|AKT_PN|UTR|PLU|DEF|OBJ_AB, S0Token: borrade_oss_ner, TransHistory1: 1, TransHistory2: 10, TransHistory3: 100, 

26- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [i, medan, vi ,.. ]

B0IsInLexic: true, B0Lemma: i, B0POS: PP, B0Token: i, B1Lemma: medan, B1POS: SN, B1Token: medan, TransHistory1: 1, TransHistory2: 11, TransHistory3: 110, 

27- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [i]   B= [medan, vi, smååt ,.. ]

B0Lemma: medan, B0POS: SN, B0Token: medan, B1IsInLexic: true, B1Lemma: vi, B1POS: PN|UTR|PLU|DEF|SUB, B1Token: vi, S0B0Distance: 1, S0B0Lemma: i_medan, S0B0LemmaPOS: i_SN, S0B0POS: PP_SN, S0B0POSLemma: PP_medan, S0B0Token: i_medan, S0B1Lemma: i_vi, S0B1LemmaPOS: i_PN|UTR|PLU|DEF|SUB, S0B1POS: PP_PN|UTR|PLU|DEF|SUB, S0B1POSLemma: PP_vi, S0B1Token: i_vi, S0B2Lemma: i_smååta, S0B2LemmaPOS: i_VB|PRT|AKT, S0B2POS: PP_VB|PRT|AKT, S0B2POSLemma: PP_smååta, S0B2Token: i_smååt, S0IsInLexic: true, S0Lemma: i, S0POS: PP, S0Token: i, TransHistory1: 2, TransHistory2: 21, TransHistory3: 211, i_isGouvernedBy_smååta: true, i_isGouvernedBy_smååta_case: true, 

28- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [medan, vi, smååt ,.. ]

B0Lemma: medan, B0POS: SN, B0Token: medan, B1IsInLexic: true, B1Lemma: vi, B1POS: PN|UTR|PLU|DEF|SUB, B1Token: vi, TransHistory1: 0, TransHistory2: 02, TransHistory3: 021, 

29- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [medan]   B= [vi, smååt, av ,.. ]

B0IsInLexic: true, B0Lemma: vi, B0POS: PN|UTR|PLU|DEF|SUB, B0Token: vi, B1Lemma: smååta, B1POS: VB|PRT|AKT, B1Token: smååt, S0B0Distance: 1, S0B0Lemma: medan_vi, S0B0LemmaPOS: medan_PN|UTR|PLU|DEF|SUB, S0B0POS: SN_PN|UTR|PLU|DEF|SUB, S0B0POSLemma: SN_vi, S0B0Token: medan_vi, S0B1Lemma: medan_smååta, S0B1LemmaPOS: medan_VB|PRT|AKT, S0B1POS: SN_VB|PRT|AKT, S0B1POSLemma: SN_smååta, S0B1Token: medan_smååt, S0B2Lemma: medan_av, S0B2LemmaPOS: medan_PP, S0B2POS: SN_PP, S0B2POSLemma: SN_av, S0B2Token: medan_av, S0Lemma: medan, S0POS: SN, S0Token: medan, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, medan_isGouvernedBy_smååta: true, medan_isGouvernedBy_smååta_mark: true, 

30- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [vi, smååt, av ,.. ]

B0IsInLexic: true, B0Lemma: vi, B0POS: PN|UTR|PLU|DEF|SUB, B0Token: vi, B1Lemma: smååta, B1POS: VB|PRT|AKT, B1Token: smååt, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

31- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [vi]   B= [smååt, av, den ,.. ]

B0Lemma: smååta, B0POS: VB|PRT|AKT, B0Token: smååt, B1IsInLexic: true, B1Lemma: av, B1POS: PP, B1Token: av, S0B0Distance: 1, S0B0Lemma: vi_smååta, S0B0LemmaPOS: vi_VB|PRT|AKT, S0B0POS: PN|UTR|PLU|DEF|SUB_VB|PRT|AKT, S0B0POSLemma: PN|UTR|PLU|DEF|SUB_smååta, S0B0Token: vi_smååt, S0B1Lemma: vi_av, S0B1LemmaPOS: vi_PP, S0B1POS: PN|UTR|PLU|DEF|SUB_PP, S0B1POSLemma: PN|UTR|PLU|DEF|SUB_av, S0B1Token: vi_av, S0B2Lemma: vi_en, S0B2LemmaPOS: vi_DT|UTR|SIN|DEF, S0B2POS: PN|UTR|PLU|DEF|SUB_DT|UTR|SIN|DEF, S0B2POSLemma: PN|UTR|PLU|DEF|SUB_en, S0B2Token: vi_den, S0IsInLexic: true, S0Lemma: vi, S0POS: PN|UTR|PLU|DEF|SUB, S0Token: vi, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, vi_isGouvernedBy_smååta: true, vi_isGouvernedBy_smååta_nsubj: true, 

32- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [smååt, av, den ,.. ]

B0Lemma: smååta, B0POS: VB|PRT|AKT, B0Token: smååt, B1IsInLexic: true, B1Lemma: av, B1POS: PP, B1Token: av, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

33- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [smååt]   B= [av, den, goda ,.. ]

B0IsInLexic: true, B0Lemma: av, B0POS: PP, B0Token: av, B1IsInLexic: true, B1Lemma: en, B1POS: DT|UTR|SIN|DEF, B1Token: den, S0B0Distance: 1, S0B0Lemma: smååta_av, S0B0LemmaPOS: smååta_PP, S0B0POS: VB|PRT|AKT_PP, S0B0POSLemma: VB|PRT|AKT_av, S0B0Token: smååt_av, S0B1Lemma: smååta_en, S0B1LemmaPOS: smååta_DT|UTR|SIN|DEF, S0B1POS: VB|PRT|AKT_DT|UTR|SIN|DEF, S0B1POSLemma: VB|PRT|AKT_en, S0B1Token: smååt_den, S0B2Lemma: smååta_god, S0B2LemmaPOS: smååta_JJ|POS|UTR/NEU|SIN|DEF|NOM, S0B2POS: VB|PRT|AKT_JJ|POS|UTR/NEU|SIN|DEF|NOM, S0B2POSLemma: VB|PRT|AKT_god, S0B2Token: smååt_goda, S0Lemma: smååta, S0POS: VB|PRT|AKT, S0Token: smååt, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, hasRighDep_nmod: true, smååta_brödkorg_hasRighDep_nmod: true, smååta_hasRighDep_nmod: true, smååta_malta_hasRighDep_nmod: true, 

34- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [av, den, goda ,.. ]

B0IsInLexic: true, B0Lemma: av, B0POS: PP, B0Token: av, B1IsInLexic: true, B1Lemma: en, B1POS: DT|UTR|SIN|DEF, B1Token: den, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

35- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [av]   B= [den, goda, brödkorgen ,.. ]

B0IsInLexic: true, B0Lemma: en, B0POS: DT|UTR|SIN|DEF, B0Token: den, B1Lemma: god, B1POS: JJ|POS|UTR/NEU|SIN|DEF|NOM, B1Token: goda, S0B0Distance: 1, S0B0Lemma: av_en, S0B0LemmaPOS: av_DT|UTR|SIN|DEF, S0B0POS: PP_DT|UTR|SIN|DEF, S0B0POSLemma: PP_en, S0B0Token: av_den, S0B1Lemma: av_god, S0B1LemmaPOS: av_JJ|POS|UTR/NEU|SIN|DEF|NOM, S0B1POS: PP_JJ|POS|UTR/NEU|SIN|DEF|NOM, S0B1POSLemma: PP_god, S0B1Token: av_goda, S0B2Lemma: av_brödkorg, S0B2LemmaPOS: av_NN|UTR|SIN|DEF|NOM, S0B2POS: PP_NN|UTR|SIN|DEF|NOM, S0B2POSLemma: PP_brödkorg, S0B2Token: av_brödkorgen, S0IsInLexic: true, S0Lemma: av, S0POS: PP, S0Token: av, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, av_isGouvernedBy_brödkorg: true, av_isGouvernedBy_brödkorg_case: true, 

36- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [den, goda, brödkorgen ,.. ]

B0IsInLexic: true, B0Lemma: en, B0POS: DT|UTR|SIN|DEF, B0Token: den, B1Lemma: god, B1POS: JJ|POS|UTR/NEU|SIN|DEF|NOM, B1Token: goda, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

37- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [den]   B= [goda, brödkorgen, med ,.. ]

B0Lemma: god, B0POS: JJ|POS|UTR/NEU|SIN|DEF|NOM, B0Token: goda, B1Lemma: brödkorg, B1POS: NN|UTR|SIN|DEF|NOM, B1Token: brödkorgen, S0B0Distance: 1, S0B0Lemma: en_god, S0B0LemmaPOS: en_JJ|POS|UTR/NEU|SIN|DEF|NOM, S0B0POS: DT|UTR|SIN|DEF_JJ|POS|UTR/NEU|SIN|DEF|NOM, S0B0POSLemma: DT|UTR|SIN|DEF_god, S0B0Token: den_goda, S0B1Lemma: en_brödkorg, S0B1LemmaPOS: en_NN|UTR|SIN|DEF|NOM, S0B1POS: DT|UTR|SIN|DEF_NN|UTR|SIN|DEF|NOM, S0B1POSLemma: DT|UTR|SIN|DEF_brödkorg, S0B1Token: den_brödkorgen, S0B2Lemma: en_med, S0B2LemmaPOS: en_PP, S0B2POS: DT|UTR|SIN|DEF_PP, S0B2POSLemma: DT|UTR|SIN|DEF_med, S0B2Token: den_med, S0IsInLexic: true, S0Lemma: en, S0POS: DT|UTR|SIN|DEF, S0Token: den, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, en_isGouvernedBy_brödkorg: true, en_isGouvernedBy_brödkorg_det: true, 

38- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [goda, brödkorgen, med ,.. ]

B0Lemma: god, B0POS: JJ|POS|UTR/NEU|SIN|DEF|NOM, B0Token: goda, B1Lemma: brödkorg, B1POS: NN|UTR|SIN|DEF|NOM, B1Token: brödkorgen, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

39- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [goda]   B= [brödkorgen, med, malt- ,.. ]

B0Lemma: brödkorg, B0POS: NN|UTR|SIN|DEF|NOM, B0Token: brödkorgen, B1IsInLexic: true, B1Lemma: med, B1POS: PP, B1Token: med, S0B0Distance: 1, S0B0Lemma: god_brödkorg, S0B0LemmaPOS: god_NN|UTR|SIN|DEF|NOM, S0B0POS: JJ|POS|UTR/NEU|SIN|DEF|NOM_NN|UTR|SIN|DEF|NOM, S0B0POSLemma: JJ|POS|UTR/NEU|SIN|DEF|NOM_brödkorg, S0B0Token: goda_brödkorgen, S0B1Lemma: god_med, S0B1LemmaPOS: god_PP, S0B1POS: JJ|POS|UTR/NEU|SIN|DEF|NOM_PP, S0B1POSLemma: JJ|POS|UTR/NEU|SIN|DEF|NOM_med, S0B1Token: goda_med, S0B2Lemma: god_malta, S0B2LemmaPOS: god_NN|UTR|SIN|IND|NOM, S0B2POS: JJ|POS|UTR/NEU|SIN|DEF|NOM_NN|UTR|SIN|IND|NOM, S0B2POSLemma: JJ|POS|UTR/NEU|SIN|DEF|NOM_malta, S0B2Token: goda_malt-, S0Lemma: god, S0POS: JJ|POS|UTR/NEU|SIN|DEF|NOM, S0Token: goda, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, god_isGouvernedBy_brödkorg: true, god_isGouvernedBy_brödkorg_amod: true, 

40- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [brödkorgen, med, malt- ,.. ]

B0Lemma: brödkorg, B0POS: NN|UTR|SIN|DEF|NOM, B0Token: brödkorgen, B1IsInLexic: true, B1Lemma: med, B1POS: PP, B1Token: med, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

41- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [brödkorgen]   B= [med, malt-, , ,.. ]

B0IsInLexic: true, B0Lemma: med, B0POS: PP, B0Token: med, B1Lemma: malta, B1POS: NN|UTR|SIN|IND|NOM, B1Token: malt-, S0B0Distance: 1, S0B0Lemma: brödkorg_med, S0B0LemmaPOS: brödkorg_PP, S0B0POS: NN|UTR|SIN|DEF|NOM_PP, S0B0POSLemma: NN|UTR|SIN|DEF|NOM_med, S0B0Token: brödkorgen_med, S0B1Lemma: brödkorg_malta, S0B1LemmaPOS: brödkorg_NN|UTR|SIN|IND|NOM, S0B1POS: NN|UTR|SIN|DEF|NOM_NN|UTR|SIN|IND|NOM, S0B1POSLemma: NN|UTR|SIN|DEF|NOM_malta, S0B1Token: brödkorgen_malt-, S0B2Lemma: brödkorg_,, S0B2LemmaPOS: brödkorg_MID, S0B2POS: NN|UTR|SIN|DEF|NOM_MID, S0B2POSLemma: NN|UTR|SIN|DEF|NOM_,, S0B2Token: brödkorgen_,, S0Lemma: brödkorg, S0POS: NN|UTR|SIN|DEF|NOM, S0Token: brödkorgen, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

42- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [med, malt-, , ,.. ]

B0IsInLexic: true, B0Lemma: med, B0POS: PP, B0Token: med, B1Lemma: malta, B1POS: NN|UTR|SIN|IND|NOM, B1Token: malt-, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

43- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [med]   B= [malt-, ,, surdegs- ,.. ]

B0Lemma: malta, B0POS: NN|UTR|SIN|IND|NOM, B0Token: malt-, B1Lemma: ,, B1POS: MID, B1Token: ,, S0B0Distance: 1, S0B0Lemma: med_malta, S0B0LemmaPOS: med_NN|UTR|SIN|IND|NOM, S0B0POS: PP_NN|UTR|SIN|IND|NOM, S0B0POSLemma: PP_malta, S0B0Token: med_malt-, S0B1Lemma: med_,, S0B1LemmaPOS: med_MID, S0B1POS: PP_MID, S0B1POSLemma: PP_,, S0B1Token: med_,, S0B2Lemma: med_surdeg, S0B2LemmaPOS: med_NN|UTR|SIN|IND|NOM, S0B2POS: PP_NN|UTR|SIN|IND|NOM, S0B2POSLemma: PP_surdeg, S0B2Token: med_surdegs-, S0IsInLexic: true, S0Lemma: med, S0POS: PP, S0Token: med, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, med_isGouvernedBy_malta: true, med_isGouvernedBy_malta_case: true, 

44- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [malt-, ,, surdegs- ,.. ]

B0Lemma: malta, B0POS: NN|UTR|SIN|IND|NOM, B0Token: malt-, B1Lemma: ,, B1POS: MID, B1Token: ,, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

45- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [malt-]   B= [,, surdegs-, och ,.. ]

B0Lemma: ,, B0POS: MID, B0Token: ,, B1Lemma: surdeg, B1POS: NN|UTR|SIN|IND|NOM, B1Token: surdegs-, S0B0Distance: 1, S0B0Lemma: malta_,, S0B0LemmaPOS: malta_MID, S0B0POS: NN|UTR|SIN|IND|NOM_MID, S0B0POSLemma: NN|UTR|SIN|IND|NOM_,, S0B0Token: malt-_,, S0B1Lemma: malta_surdeg, S0B1LemmaPOS: malta_NN|UTR|SIN|IND|NOM, S0B1POS: NN|UTR|SIN|IND|NOM_NN|UTR|SIN|IND|NOM, S0B1POSLemma: NN|UTR|SIN|IND|NOM_surdeg, S0B1Token: malt-_surdegs-, S0B2Lemma: malta_och, S0B2LemmaPOS: malta_KN, S0B2POS: NN|UTR|SIN|IND|NOM_KN, S0B2POSLemma: NN|UTR|SIN|IND|NOM_och, S0B2Token: malt-_och, S0Lemma: malta, S0POS: NN|UTR|SIN|IND|NOM, S0Token: malt-, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, hasRighDep_cc: true, hasRighDep_conj: true, hasRighDep_punct: true, malta_,_hasRighDep_punct: true, malta_hasRighDep_cc: true, malta_hasRighDep_conj: true, malta_hasRighDep_punct: true, malta_knäckebröd_hasRighDep_conj: true, malta_och_hasRighDep_cc: true, malta_surdeg_hasRighDep_conj: true, 

46- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, surdegs-, och ,.. ]

B0Lemma: ,, B0POS: MID, B0Token: ,, B1Lemma: surdeg, B1POS: NN|UTR|SIN|IND|NOM, B1Token: surdegs-, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

47- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [surdegs-, och, knäckebröd ,.. ]

B0Lemma: surdeg, B0POS: NN|UTR|SIN|IND|NOM, B0Token: surdegs-, B1Lemma: och, B1POS: KN, B1Token: och, S0B0Distance: 1, S0B0Lemma: ,_surdeg, S0B0LemmaPOS: ,_NN|UTR|SIN|IND|NOM, S0B0POS: MID_NN|UTR|SIN|IND|NOM, S0B0POSLemma: MID_surdeg, S0B0Token: ,_surdegs-, S0B1Lemma: ,_och, S0B1LemmaPOS: ,_KN, S0B1POS: MID_KN, S0B1POSLemma: MID_och, S0B1Token: ,_och, S0B2Lemma: ,_knäckebröd, S0B2LemmaPOS: ,_NN|UTR|SIN|IND|NOM, S0B2POS: MID_NN|UTR|SIN|IND|NOM, S0B2POSLemma: MID_knäckebröd, S0B2Token: ,_knäckebröd, S0Lemma: ,, S0POS: MID, S0Token: ,, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

48- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [surdegs-, och, knäckebröd ,.. ]

B0Lemma: surdeg, B0POS: NN|UTR|SIN|IND|NOM, B0Token: surdegs-, B1Lemma: och, B1POS: KN, B1Token: och, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

49- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [surdegs-]   B= [och, knäckebröd, , ,.. ]

B0Lemma: och, B0POS: KN, B0Token: och, B1Lemma: knäckebröd, B1POS: NN|UTR|SIN|IND|NOM, B1Token: knäckebröd, S0B0Distance: 1, S0B0Lemma: surdeg_och, S0B0LemmaPOS: surdeg_KN, S0B0POS: NN|UTR|SIN|IND|NOM_KN, S0B0POSLemma: NN|UTR|SIN|IND|NOM_och, S0B0Token: surdegs-_och, S0B1Lemma: surdeg_knäckebröd, S0B1LemmaPOS: surdeg_NN|UTR|SIN|IND|NOM, S0B1POS: NN|UTR|SIN|IND|NOM_NN|UTR|SIN|IND|NOM, S0B1POSLemma: NN|UTR|SIN|IND|NOM_knäckebröd, S0B1Token: surdegs-_knäckebröd, S0B2Lemma: surdeg_,, S0B2LemmaPOS: surdeg_MID, S0B2POS: NN|UTR|SIN|IND|NOM_MID, S0B2POSLemma: NN|UTR|SIN|IND|NOM_,, S0B2Token: surdegs-_,, S0Lemma: surdeg, S0POS: NN|UTR|SIN|IND|NOM, S0Token: surdegs-, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

50- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [och, knäckebröd, , ,.. ]

B0Lemma: och, B0POS: KN, B0Token: och, B1Lemma: knäckebröd, B1POS: NN|UTR|SIN|IND|NOM, B1Token: knäckebröd, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

51- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [och]   B= [knäckebröd, ,, och ,.. ]

B0Lemma: knäckebröd, B0POS: NN|UTR|SIN|IND|NOM, B0Token: knäckebröd, B1Lemma: ,, B1POS: MID, B1Token: ,, S0B0Distance: 1, S0B0Lemma: och_knäckebröd, S0B0LemmaPOS: och_NN|UTR|SIN|IND|NOM, S0B0POS: KN_NN|UTR|SIN|IND|NOM, S0B0POSLemma: KN_knäckebröd, S0B0Token: och_knäckebröd, S0B1Lemma: och_,, S0B1LemmaPOS: och_MID, S0B1POS: KN_MID, S0B1POSLemma: KN_,, S0B1Token: och_,, S0B2Lemma: och_och, S0B2LemmaPOS: och_KN, S0B2POS: KN_KN, S0B2POSLemma: KN_och, S0B2Token: och_och, S0Lemma: och, S0POS: KN, S0Token: och, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

52- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [knäckebröd, ,, och ,.. ]

B0Lemma: knäckebröd, B0POS: NN|UTR|SIN|IND|NOM, B0Token: knäckebröd, B1Lemma: ,, B1POS: MID, B1Token: ,, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

53- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [knäckebröd]   B= [,, och, ett ,.. ]

B0Lemma: ,, B0POS: MID, B0Token: ,, B1Lemma: och, B1POS: KN, B1Token: och, S0B0Distance: 1, S0B0Lemma: knäckebröd_,, S0B0LemmaPOS: knäckebröd_MID, S0B0POS: NN|UTR|SIN|IND|NOM_MID, S0B0POSLemma: NN|UTR|SIN|IND|NOM_,, S0B0Token: knäckebröd_,, S0B1Lemma: knäckebröd_och, S0B1LemmaPOS: knäckebröd_KN, S0B1POS: NN|UTR|SIN|IND|NOM_KN, S0B1POSLemma: NN|UTR|SIN|IND|NOM_och, S0B1Token: knäckebröd_och, S0B2Lemma: knäckebröd_en, S0B2LemmaPOS: knäckebröd_DT|NEU|SIN|IND, S0B2POS: NN|UTR|SIN|IND|NOM_DT|NEU|SIN|IND, S0B2POSLemma: NN|UTR|SIN|IND|NOM_en, S0B2Token: knäckebröd_ett, S0Lemma: knäckebröd, S0POS: NN|UTR|SIN|IND|NOM, S0Token: knäckebröd, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

54- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, och, ett ,.. ]

B0Lemma: ,, B0POS: MID, B0Token: ,, B1Lemma: och, B1POS: KN, B1Token: och, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

55- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [och, ett, rört ,.. ]

B0Lemma: och, B0POS: KN, B0Token: och, B1IsInLexic: true, B1Lemma: en, B1POS: DT|NEU|SIN|IND, B1Token: ett, S0B0Distance: 1, S0B0Lemma: ,_och, S0B0LemmaPOS: ,_KN, S0B0POS: MID_KN, S0B0POSLemma: MID_och, S0B0Token: ,_och, S0B1Lemma: ,_en, S0B1LemmaPOS: ,_DT|NEU|SIN|IND, S0B1POS: MID_DT|NEU|SIN|IND, S0B1POSLemma: MID_en, S0B1Token: ,_ett, S0B2Lemma: ,_röra, S0B2LemmaPOS: ,_JJ|POS|NEU|SIN|IND|NOM, S0B2POS: MID_JJ|POS|NEU|SIN|IND|NOM, S0B2POSLemma: MID_röra, S0B2Token: ,_rört, S0Lemma: ,, S0POS: MID, S0Token: ,, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

56- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [och, ett, rört ,.. ]

B0Lemma: och, B0POS: KN, B0Token: och, B1IsInLexic: true, B1Lemma: en, B1POS: DT|NEU|SIN|IND, B1Token: ett, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

57- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [och]   B= [ett, rört, smör ,.. ]

B0IsInLexic: true, B0Lemma: en, B0POS: DT|NEU|SIN|IND, B0Token: ett, B1IsInLexic: true, B1Lemma: röra, B1POS: JJ|POS|NEU|SIN|IND|NOM, B1Token: rört, S0B0Distance: 1, S0B0Lemma: och_en, S0B0LemmaPOS: och_DT|NEU|SIN|IND, S0B0POS: KN_DT|NEU|SIN|IND, S0B0POSLemma: KN_en, S0B0Token: och_ett, S0B1Lemma: och_röra, S0B1LemmaPOS: och_JJ|POS|NEU|SIN|IND|NOM, S0B1POS: KN_JJ|POS|NEU|SIN|IND|NOM, S0B1POSLemma: KN_röra, S0B1Token: och_rört, S0B2Lemma: och_smör, S0B2LemmaPOS: och_NN|NEU|SIN|IND|NOM, S0B2POS: KN_NN|NEU|SIN|IND|NOM, S0B2POSLemma: KN_smör, S0B2Token: och_smör, S0Lemma: och, S0POS: KN, S0Token: och, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

58- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ett, rört, smör ,.. ]

B0IsInLexic: true, B0Lemma: en, B0POS: DT|NEU|SIN|IND, B0Token: ett, B1IsInLexic: true, B1Lemma: röra, B1POS: JJ|POS|NEU|SIN|IND|NOM, B1Token: rört, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

59- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ett]   B= [rört, smör, därtill ,.. ]

B0IsInLexic: true, B0Lemma: röra, B0POS: JJ|POS|NEU|SIN|IND|NOM, B0Token: rört, B1Lemma: smör, B1POS: NN|NEU|SIN|IND|NOM, B1Token: smör, S0B0Distance: 1, S0B0Lemma: en_röra, S0B0LemmaPOS: en_JJ|POS|NEU|SIN|IND|NOM, S0B0POS: DT|NEU|SIN|IND_JJ|POS|NEU|SIN|IND|NOM, S0B0POSLemma: DT|NEU|SIN|IND_röra, S0B0Token: ett_rört, S0B1Lemma: en_smör, S0B1LemmaPOS: en_NN|NEU|SIN|IND|NOM, S0B1POS: DT|NEU|SIN|IND_NN|NEU|SIN|IND|NOM, S0B1POSLemma: DT|NEU|SIN|IND_smör, S0B1Token: ett_smör, S0B2Lemma: en_därtill, S0B2LemmaPOS: en_AB, S0B2POS: DT|NEU|SIN|IND_AB, S0B2POSLemma: DT|NEU|SIN|IND_därtill, S0B2Token: ett_därtill, S0IsInLexic: true, S0Lemma: en, S0POS: DT|NEU|SIN|IND, S0Token: ett, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, en_isGouvernedBy_smör: true, en_isGouvernedBy_smör_det: true, 

60- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [rört, smör, därtill ,.. ]

B0IsInLexic: true, B0Lemma: röra, B0POS: JJ|POS|NEU|SIN|IND|NOM, B0Token: rört, B1Lemma: smör, B1POS: NN|NEU|SIN|IND|NOM, B1Token: smör, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

61- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [rört]   B= [smör, därtill, . ,.. ]

B0Lemma: smör, B0POS: NN|NEU|SIN|IND|NOM, B0Token: smör, B1Lemma: därtill, B1POS: AB, B1Token: därtill, S0B0Distance: 1, S0B0Lemma: röra_smör, S0B0LemmaPOS: röra_NN|NEU|SIN|IND|NOM, S0B0POS: JJ|POS|NEU|SIN|IND|NOM_NN|NEU|SIN|IND|NOM, S0B0POSLemma: JJ|POS|NEU|SIN|IND|NOM_smör, S0B0Token: rört_smör, S0B1Lemma: röra_därtill, S0B1LemmaPOS: röra_AB, S0B1POS: JJ|POS|NEU|SIN|IND|NOM_AB, S0B1POSLemma: JJ|POS|NEU|SIN|IND|NOM_därtill, S0B1Token: rört_därtill, S0B2Lemma: röra_., S0B2LemmaPOS: röra_MAD, S0B2POS: JJ|POS|NEU|SIN|IND|NOM_MAD, S0B2POSLemma: JJ|POS|NEU|SIN|IND|NOM_., S0B2Token: rört_., S0IsInLexic: true, S0Lemma: röra, S0POS: JJ|POS|NEU|SIN|IND|NOM, S0Token: rört, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, röra_isGouvernedBy_smör: true, röra_isGouvernedBy_smör_amod: true, 

62- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [smör, därtill, . ,.. ]

B0Lemma: smör, B0POS: NN|NEU|SIN|IND|NOM, B0Token: smör, B1Lemma: därtill, B1POS: AB, B1Token: därtill, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

63- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [smör]   B= [därtill, . ,.. ]

B0Lemma: därtill, B0POS: AB, B0Token: därtill, B1Lemma: ., B1POS: MAD, B1Token: ., S0B0Distance: 1, S0B0Lemma: smör_därtill, S0B0LemmaPOS: smör_AB, S0B0POS: NN|NEU|SIN|IND|NOM_AB, S0B0POSLemma: NN|NEU|SIN|IND|NOM_därtill, S0B0Token: smör_därtill, S0B1Lemma: smör_., S0B1LemmaPOS: smör_MAD, S0B1POS: NN|NEU|SIN|IND|NOM_MAD, S0B1POSLemma: NN|NEU|SIN|IND|NOM_., S0B1Token: smör_., S0Lemma: smör, S0POS: NN|NEU|SIN|IND|NOM, S0Token: smör, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, hasRighDep_advmod: true, smör_därtill_hasRighDep_advmod: true, smör_hasRighDep_advmod: true, 

64- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [därtill, . ,.. ]

B0Lemma: därtill, B0POS: AB, B0Token: därtill, B1Lemma: ., B1POS: MAD, B1Token: ., TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

65- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [därtill]   B= [.]

B0Lemma: ., B0POS: MAD, B0Token: ., S0B0Distance: 1, S0B0Lemma: därtill_., S0B0LemmaPOS: därtill_MAD, S0B0POS: AB_MAD, S0B0POSLemma: AB_., S0B0Token: därtill_., S0Lemma: därtill, S0POS: AB, S0Token: därtill, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

66- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [.]

B0Lemma: ., B0POS: MAD, B0Token: ., TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

67- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [ ]

S0Lemma: ., S0POS: MAD, S0Token: ., TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

68- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

