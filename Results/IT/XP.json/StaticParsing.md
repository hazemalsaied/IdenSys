## Sentence No. 12776 - 
andavo pazzo dell' autore ; m' innamoravo fantasticamente di " lucile " del chateaubriand , come più tardi mi innamorai di " diana vernon " , una eroina di walter scott » . 
### Existing MWEs: 
1- **andavo pazzo** (ID)
2- **m' innamoravo** (IReflV)
3- **mi innamorai** (IReflV)



0- &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [andavo, pazzo, dell' ,.. ]

B0Lemma: andare, B0POS: V, B0Token: andavo, 

1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [andavo]   B= [pazzo, dell', autore ,.. ]

B0Lemma: pazzo, B0POS: S, B0Token: pazzo, S0B0Lemma: andare_pazzo, S0B0LemmaPOS: andare_S, S0B0POS: V_S, S0B0POSLemma: V_pazzo, S0B0Token: andavo_pazzo, S0B1Lemma: andare_di, S0B1LemmaPOS: andare_EA, S0B1POS: V_EA, S0B1POSLemma: V_di, S0B1Token: andavo_dell', S0Lemma: andare, S0POS: V, S0Token: andavo, 

2- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [andavo, pazzo]   B= [dell', autore, ; ,.. ]

B0Lemma: di, B0POS: EA, B0Token: dell', S0B0Lemma: pazzo_di, S0B0LemmaPOS: pazzo_EA, S0B0POS: S_EA, S0B0POSLemma: S_di, S0B0Token: pazzo_dell', S0B1Lemma: pazzo_autore, S0B1LemmaPOS: pazzo_S, S0B1POS: S_S, S0B1POSLemma: S_autore, S0B1Token: pazzo_autore, S0Lemma: pazzo, S0POS: S, S0S1Distance: 1, S0Token: pazzo, S1B0Lemma: andare_di, S1B0LemmaPOS: andare_EA, S1B0POS: V_EA, S1B0POSLemma: V_di, S1B0Token: andavo_dell', S1Lemma: andare, S1POS: V, S1S0Lemma: andare_pazzo, S1S0LemmaPOS: andare_S, S1S0POS: V_S, S1S0POSLemma: V_pazzo, S1S0Token: andavo_pazzo, S1Token: andavo, SyntaxicRelation: +subj, hasRighDep_comp: true, pazzo_di_hasRighDep_comp: true, pazzo_hasRighDep_comp: true, 

3- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[andavo, pazzo]]   B= [dell', autore, ; ,.. ]

B0Lemma: di, B0POS: EA, B0Token: dell', S0B0Lemma: andare_pazzo_di, S0B0LemmaPOS: andare_pazzo_EA, S0B0POS: V_S_EA, S0B0POSLemma: V_S_di, S0B0Token: andavo_pazzo_dell', S0B1Lemma: andare_pazzo_autore, S0B1LemmaPOS: andare_pazzo_S, S0B1POS: V_S_S, S0B1POSLemma: V_S_autore, S0B1Token: andavo_pazzo_autore, S0Lemma: andare_pazzo, S0POS: V_S, S0Token: andavo_pazzo, 

4- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [dell', autore, ; ,.. ]

B0Lemma: di, B0POS: EA, B0Token: dell', TransHistory3: 100, 

5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [dell']   B= [autore, ;, m' ,.. ]

B0Lemma: autore, B0POS: S, B0Token: autore, S0B0Lemma: di_autore, S0B0LemmaPOS: di_S, S0B0POS: EA_S, S0B0POSLemma: EA_autore, S0B0Token: dell'_autore, S0B1Lemma: di_;, S0B1LemmaPOS: di_FC, S0B1POS: EA_FC, S0B1POSLemma: EA_;, S0B1Token: dell'_;, S0Lemma: di, S0POS: EA, S0Token: dell', TransHistory3: 210, di_autore_hasRighDep_prep: true, di_hasRighDep_prep: true, hasRighDep_prep: true, 

6- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [autore, ;, m' ,.. ]

B0Lemma: autore, B0POS: S, B0Token: autore, TransHistory3: 021, 

7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [autore]   B= [;, m', innamoravo ,.. ]

B0Lemma: ;, B0POS: FC, B0Token: ;, S0B0Lemma: autore_;, S0B0LemmaPOS: autore_FC, S0B0POS: S_FC, S0B0POSLemma: S_;, S0B0Token: autore_;, S0B1Lemma: autore_m', S0B1LemmaPOS: autore_PC, S0B1POS: S_PC, S0B1POSLemma: S_m', S0B1Token: autore_m', S0Lemma: autore, S0POS: S, S0Token: autore, TransHistory3: 202, autore_;_hasRighDep_punc: true, autore_hasRighDep_punc: true, hasRighDep_punc: true, 

8- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [;, m', innamoravo ,.. ]

B0Lemma: ;, B0POS: FC, B0Token: ;, TransHistory3: 020, 

9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [;]   B= [m', innamoravo, fantasticamente ,.. ]

B0Lemma: m', B0POS: PC, B0Token: m', S0B0Lemma: ;_m', S0B0LemmaPOS: ;_PC, S0B0POS: FC_PC, S0B0POSLemma: FC_m', S0B0Token: ;_m', S0B1Lemma: ;_innamorare, S0B1LemmaPOS: ;_V, S0B1POS: FC_V, S0B1POSLemma: FC_innamorare, S0B1Token: ;_innamoravo, S0Lemma: ;, S0POS: FC, S0Token: ;, TransHistory3: 202, 

10- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [m', innamoravo, fantasticamente ,.. ]

B0Lemma: m', B0POS: PC, B0Token: m', TransHistory3: 020, 

11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [m']   B= [innamoravo, fantasticamente, di ,.. ]

B0Lemma: innamorare, B0POS: V, B0Token: innamoravo, S0B0Lemma: m'_innamorare, S0B0LemmaPOS: m'_V, S0B0POS: PC_V, S0B0POSLemma: PC_innamorare, S0B0Token: m'_innamoravo, S0B1Lemma: m'_fantasticamente, S0B1LemmaPOS: m'_B, S0B1POS: PC_B, S0B1POSLemma: PC_fantasticamente, S0B1Token: m'_fantasticamente, S0Lemma: m', S0POS: PC, S0Token: m', TransHistory3: 202, m'_isGouvernedBy_innamorare: true, m'_isGouvernedBy_innamorare_comp_ind: true, 

12- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [m', innamoravo]   B= [fantasticamente, di, " ,.. ]

B0Lemma: fantasticamente, B0POS: B, B0Token: fantasticamente, S0B0Lemma: innamorare_fantasticamente, S0B0LemmaPOS: innamorare_B, S0B0POS: V_B, S0B0POSLemma: V_fantasticamente, S0B0Token: innamoravo_fantasticamente, S0B1Lemma: innamorare_di, S0B1LemmaPOS: innamorare_E, S0B1POS: V_E, S0B1POSLemma: V_di, S0B1Token: innamoravo_di, S0Lemma: innamorare, S0POS: V, S0S1Distance: 1, S0Token: innamoravo, S1B0Lemma: m'_fantasticamente, S1B0LemmaPOS: m'_B, S1B0POS: PC_B, S1B0POSLemma: PC_fantasticamente, S1B0Token: m'_fantasticamente, S1Lemma: m', S1POS: PC, S1S0Lemma: m'_innamorare, S1S0LemmaPOS: m'_V, S1S0POS: PC_V, S1S0POSLemma: PC_innamorare, S1S0Token: m'_innamoravo, S1Token: m', SyntaxicRelation: -comp_ind, TransHistory3: 020, hasRighDep_comp: true, hasRighDep_mod: true, innamorare_di_hasRighDep_comp: true, innamorare_fantasticamente_hasRighDep_mod: true, innamorare_hasRighDep_comp: true, innamorare_hasRighDep_mod: true, 

13- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[m', innamoravo]]   B= [fantasticamente, di, " ,.. ]

B0Lemma: fantasticamente, B0POS: B, B0Token: fantasticamente, S0B0Lemma: m'_innamorare_fantasticamente, S0B0LemmaPOS: m'_innamorare_B, S0B0POS: PC_V_B, S0B0POSLemma: PC_V_fantasticamente, S0B0Token: m'_innamoravo_fantasticamente, S0B1Lemma: m'_innamorare_di, S0B1LemmaPOS: m'_innamorare_E, S0B1POS: PC_V_E, S0B1POSLemma: PC_V_di, S0B1Token: m'_innamoravo_di, S0Lemma: m'_innamorare, S0POS: PC_V, S0Token: m'_innamoravo, TransHistory3: 002, 

14- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [fantasticamente, di, " ,.. ]

B0Lemma: fantasticamente, B0POS: B, B0Token: fantasticamente, TransHistory3: 100, 

15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [fantasticamente]   B= [di, ", lucile ,.. ]

B0Lemma: di, B0POS: E, B0Token: di, S0B0Lemma: fantasticamente_di, S0B0LemmaPOS: fantasticamente_E, S0B0POS: B_E, S0B0POSLemma: B_di, S0B0Token: fantasticamente_di, S0B1Lemma: fantasticamente_", S0B1LemmaPOS: fantasticamente_FB, S0B1POS: B_FB, S0B1POSLemma: B_", S0B1Token: fantasticamente_", S0Lemma: fantasticamente, S0POS: B, S0Token: fantasticamente, TransHistory3: 210, 

16- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [di, ", lucile ,.. ]

B0Lemma: di, B0POS: E, B0Token: di, TransHistory3: 021, 

17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [di]   B= [", lucile, " ,.. ]

B0Lemma: ", B0POS: FB, B0Token: ", S0B0Lemma: di_", S0B0LemmaPOS: di_FB, S0B0POS: E_FB, S0B0POSLemma: E_", S0B0Token: di_", S0B1Lemma: di_Lucile, S0B1LemmaPOS: di_SP, S0B1POS: E_SP, S0B1POSLemma: E_Lucile, S0B1Token: di_lucile, S0Lemma: di, S0POS: E, S0Token: di, TransHistory3: 202, di_Lucile_hasRighDep_prep: true, di_hasRighDep_prep: true, hasRighDep_prep: true, 

18- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [", lucile, " ,.. ]

B0Lemma: ", B0POS: FB, B0Token: ", TransHistory3: 020, 

19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= ["]   B= [lucile, ", del ,.. ]

"_isGouvernedBy_Lucile: true, "_isGouvernedBy_Lucile_punc: true, B0Lemma: Lucile, B0POS: SP, B0Token: lucile, S0B0Lemma: "_Lucile, S0B0LemmaPOS: "_SP, S0B0POS: FB_SP, S0B0POSLemma: FB_Lucile, S0B0Token: "_lucile, S0B1Lemma: "_", S0B1LemmaPOS: "_FB, S0B1POS: FB_FB, S0B1POSLemma: FB_", S0B1Token: "_", S0Lemma: ", S0POS: FB, S0Token: ", TransHistory3: 202, 

20- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [lucile, ", del ,.. ]

B0Lemma: Lucile, B0POS: SP, B0Token: lucile, TransHistory3: 020, 

21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [lucile]   B= [", del, chateaubriand ,.. ]

B0Lemma: ", B0POS: FB, B0Token: ", Lucile_"_hasRighDep_punc: true, Lucile_di_hasRighDep_comp: true, Lucile_hasRighDep_comp: true, Lucile_hasRighDep_punc: true, S0B0Lemma: Lucile_", S0B0LemmaPOS: Lucile_FB, S0B0POS: SP_FB, S0B0POSLemma: SP_", S0B0Token: lucile_", S0B1Lemma: Lucile_di, S0B1LemmaPOS: Lucile_EA, S0B1POS: SP_EA, S0B1POSLemma: SP_di, S0B1Token: lucile_del, S0Lemma: Lucile, S0POS: SP, S0Token: lucile, TransHistory3: 202, hasRighDep_comp: true, hasRighDep_punc: true, 

22- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [", del, chateaubriand ,.. ]

B0Lemma: ", B0POS: FB, B0Token: ", TransHistory3: 020, 

23- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= ["]   B= [del, chateaubriand, , ,.. ]

B0Lemma: di, B0POS: EA, B0Token: del, S0B0Lemma: "_di, S0B0LemmaPOS: "_EA, S0B0POS: FB_EA, S0B0POSLemma: FB_di, S0B0Token: "_del, S0B1Lemma: "_Chateaubriand, S0B1LemmaPOS: "_SP, S0B1POS: FB_SP, S0B1POSLemma: FB_Chateaubriand, S0B1Token: "_chateaubriand, S0Lemma: ", S0POS: FB, S0Token: ", TransHistory3: 202, 

24- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [del, chateaubriand, , ,.. ]

B0Lemma: di, B0POS: EA, B0Token: del, TransHistory3: 020, 

25- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [del]   B= [chateaubriand, ,, come ,.. ]

B0Lemma: Chateaubriand, B0POS: SP, B0Token: chateaubriand, S0B0Lemma: di_Chateaubriand, S0B0LemmaPOS: di_SP, S0B0POS: EA_SP, S0B0POSLemma: EA_Chateaubriand, S0B0Token: del_chateaubriand, S0B1Lemma: di_,, S0B1LemmaPOS: di_FF, S0B1POS: EA_FF, S0B1POSLemma: EA_,, S0B1Token: del_,, S0Lemma: di, S0POS: EA, S0Token: del, TransHistory3: 202, di_Chateaubriand_hasRighDep_prep: true, di_hasRighDep_prep: true, hasRighDep_prep: true, 

26- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [chateaubriand, ,, come ,.. ]

B0Lemma: Chateaubriand, B0POS: SP, B0Token: chateaubriand, TransHistory3: 020, 

27- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [chateaubriand]   B= [,, come, più ,.. ]

B0Lemma: ,, B0POS: FF, B0Token: ,, Chateaubriand_hasRighDep_mod_rel: true, Chateaubriand_innamorare_hasRighDep_mod_rel: true, S0B0Lemma: Chateaubriand_,, S0B0LemmaPOS: Chateaubriand_FF, S0B0POS: SP_FF, S0B0POSLemma: SP_,, S0B0Token: chateaubriand_,, S0B1Lemma: Chateaubriand_come, S0B1LemmaPOS: Chateaubriand_B, S0B1POS: SP_B, S0B1POSLemma: SP_come, S0B1Token: chateaubriand_come, S0Lemma: Chateaubriand, S0POS: SP, S0Token: chateaubriand, TransHistory3: 202, hasRighDep_mod_rel: true, 

28- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, come, più ,.. ]

B0Lemma: ,, B0POS: FF, B0Token: ,, TransHistory3: 020, 

29- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [come, più, tardi ,.. ]

,_isGouvernedBy_tardi: true, ,_isGouvernedBy_tardi_punc: true, B0Lemma: come, B0POS: B, B0Token: come, S0B0Lemma: ,_come, S0B0LemmaPOS: ,_B, S0B0POS: FF_B, S0B0POSLemma: FF_come, S0B0Token: ,_come, S0B1Lemma: ,_più, S0B1LemmaPOS: ,_B, S0B1POS: FF_B, S0B1POSLemma: FF_più, S0B1Token: ,_più, S0Lemma: ,, S0POS: FF, S0Token: ,, TransHistory3: 202, 

30- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [come, più, tardi ,.. ]

B0Lemma: come, B0POS: B, B0Token: come, TransHistory3: 020, 

31- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [come]   B= [più, tardi, mi ,.. ]

B0Lemma: più, B0POS: B, B0Token: più, S0B0Lemma: come_più, S0B0LemmaPOS: come_B, S0B0POS: B_B, S0B0POSLemma: B_più, S0B0Token: come_più, S0B1Lemma: come_tardi, S0B1LemmaPOS: come_B, S0B1POS: B_B, S0B1POSLemma: B_tardi, S0B1Token: come_tardi, S0Lemma: come, S0POS: B, S0Token: come, TransHistory3: 202, come_isGouvernedBy_più: true, come_isGouvernedBy_più_mod: true, 

32- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [più, tardi, mi ,.. ]

B0Lemma: più, B0POS: B, B0Token: più, TransHistory3: 020, 

33- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [più]   B= [tardi, mi, innamorai ,.. ]

B0Lemma: tardi, B0POS: B, B0Token: tardi, S0B0Lemma: più_tardi, S0B0LemmaPOS: più_B, S0B0POS: B_B, S0B0POSLemma: B_tardi, S0B0Token: più_tardi, S0B1Lemma: più_mi, S0B1LemmaPOS: più_PC, S0B1POS: B_PC, S0B1POSLemma: B_mi, S0B1Token: più_mi, S0Lemma: più, S0POS: B, S0Token: più, TransHistory3: 202, più_isGouvernedBy_tardi: true, più_isGouvernedBy_tardi_mod: true, 

34- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [tardi, mi, innamorai ,.. ]

B0Lemma: tardi, B0POS: B, B0Token: tardi, TransHistory3: 020, 

35- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [tardi]   B= [mi, innamorai, di ,.. ]

B0Lemma: mi, B0POS: PC, B0Token: mi, S0B0Lemma: tardi_mi, S0B0LemmaPOS: tardi_PC, S0B0POS: B_PC, S0B0POSLemma: B_mi, S0B0Token: tardi_mi, S0B1Lemma: tardi_innamorare, S0B1LemmaPOS: tardi_V, S0B1POS: B_V, S0B1POSLemma: B_innamorare, S0B1Token: tardi_innamorai, S0Lemma: tardi, S0POS: B, S0Token: tardi, TransHistory3: 202, tardi_isGouvernedBy_innamorare: true, tardi_isGouvernedBy_innamorare_mod: true, 

36- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [mi, innamorai, di ,.. ]

B0Lemma: mi, B0POS: PC, B0Token: mi, TransHistory3: 020, 

37- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [mi]   B= [innamorai, di, " ,.. ]

B0Lemma: innamorare, B0POS: V, B0Token: innamorai, S0B0Lemma: mi_innamorare, S0B0LemmaPOS: mi_V, S0B0POS: PC_V, S0B0POSLemma: PC_innamorare, S0B0Token: mi_innamorai, S0B1Lemma: mi_di, S0B1LemmaPOS: mi_E, S0B1POS: PC_E, S0B1POSLemma: PC_di, S0B1Token: mi_di, S0Lemma: mi, S0POS: PC, S0Token: mi, TransHistory3: 202, mi_isGouvernedBy_innamorare: true, mi_isGouvernedBy_innamorare_comp_ind: true, 

38- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [mi, innamorai]   B= [di, ", diana ,.. ]

B0Lemma: di, B0POS: E, B0Token: di, S0B0Lemma: innamorare_di, S0B0LemmaPOS: innamorare_E, S0B0POS: V_E, S0B0POSLemma: V_di, S0B0Token: innamorai_di, S0B1Lemma: innamorare_", S0B1LemmaPOS: innamorare_FB, S0B1POS: V_FB, S0B1POSLemma: V_", S0B1Token: innamorai_", S0Lemma: innamorare, S0POS: V, S0S1Distance: 1, S0Token: innamorai, S1B0Lemma: mi_di, S1B0LemmaPOS: mi_E, S1B0POS: PC_E, S1B0POSLemma: PC_di, S1B0Token: mi_di, S1Lemma: mi, S1POS: PC, S1S0Lemma: mi_innamorare, S1S0LemmaPOS: mi_V, S1S0POS: PC_V, S1S0POSLemma: PC_innamorare, S1S0Token: mi_innamorai, S1Token: mi, SyntaxicRelation: -comp_ind, TransHistory3: 020, hasRighDep_comp: true, innamorare_di_hasRighDep_comp: true, innamorare_hasRighDep_comp: true, 

39- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[mi, innamorai]]   B= [di, ", diana ,.. ]

B0Lemma: di, B0POS: E, B0Token: di, S0B0Lemma: mi_innamorare_di, S0B0LemmaPOS: mi_innamorare_E, S0B0POS: PC_V_E, S0B0POSLemma: PC_V_di, S0B0Token: mi_innamorai_di, S0B1Lemma: mi_innamorare_", S0B1LemmaPOS: mi_innamorare_FB, S0B1POS: PC_V_FB, S0B1POSLemma: PC_V_", S0B1Token: mi_innamorai_", S0Lemma: mi_innamorare, S0POS: PC_V, S0Token: mi_innamorai, TransHistory3: 002, 

40- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [di, ", diana ,.. ]

B0Lemma: di, B0POS: E, B0Token: di, TransHistory3: 100, 

41- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [di]   B= [", diana, vernon ,.. ]

B0Lemma: ", B0POS: FB, B0Token: ", S0B0Lemma: di_", S0B0LemmaPOS: di_FB, S0B0POS: E_FB, S0B0POSLemma: E_", S0B0Token: di_", S0B1Lemma: di_Diana, S0B1LemmaPOS: di_SP, S0B1POS: E_SP, S0B1POSLemma: E_Diana, S0B1Token: di_diana, S0Lemma: di, S0POS: E, S0Token: di, TransHistory3: 210, di_Vernon_hasRighDep_prep: true, di_hasRighDep_prep: true, hasRighDep_prep: true, 

42- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [", diana, vernon ,.. ]

B0Lemma: ", B0POS: FB, B0Token: ", TransHistory3: 021, 

43- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= ["]   B= [diana, vernon, " ,.. ]

"_isGouvernedBy_Vernon: true, "_isGouvernedBy_Vernon_punc: true, B0Lemma: Diana, B0POS: SP, B0Token: diana, S0B0Lemma: "_Diana, S0B0LemmaPOS: "_SP, S0B0POS: FB_SP, S0B0POSLemma: FB_Diana, S0B0Token: "_diana, S0B1Lemma: "_Vernon, S0B1LemmaPOS: "_SP, S0B1POS: FB_SP, S0B1POSLemma: FB_Vernon, S0B1Token: "_vernon, S0Lemma: ", S0POS: FB, S0Token: ", TransHistory3: 202, 

44- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [diana, vernon, " ,.. ]

B0Lemma: Diana, B0POS: SP, B0Token: diana, TransHistory3: 020, 

45- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [diana]   B= [vernon, ", , ,.. ]

B0Lemma: Vernon, B0POS: SP, B0Token: vernon, Diana_isGouvernedBy_Vernon: true, Diana_isGouvernedBy_Vernon_mod: true, S0B0Lemma: Diana_Vernon, S0B0LemmaPOS: Diana_SP, S0B0POS: SP_SP, S0B0POSLemma: SP_Vernon, S0B0Token: diana_vernon, S0B1Lemma: Diana_", S0B1LemmaPOS: Diana_FB, S0B1POS: SP_FB, S0B1POSLemma: SP_", S0B1Token: diana_", S0Lemma: Diana, S0POS: SP, S0Token: diana, TransHistory3: 202, 

46- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [vernon, ", , ,.. ]

B0Lemma: Vernon, B0POS: SP, B0Token: vernon, TransHistory3: 020, 

47- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [vernon]   B= [", ,, una ,.. ]

B0Lemma: ", B0POS: FB, B0Token: ", S0B0Lemma: Vernon_", S0B0LemmaPOS: Vernon_FB, S0B0POS: SP_FB, S0B0POSLemma: SP_", S0B0Token: vernon_", S0B1Lemma: Vernon_,, S0B1LemmaPOS: Vernon_FF, S0B1POS: SP_FF, S0B1POSLemma: SP_,, S0B1Token: vernon_,, S0Lemma: Vernon, S0POS: SP, S0Token: vernon, TransHistory3: 202, Vernon_"_hasRighDep_punc: true, Vernon_eroina_hasRighDep_mod: true, Vernon_hasRighDep_mod: true, Vernon_hasRighDep_punc: true, hasRighDep_mod: true, hasRighDep_punc: true, 

48- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [", ,, una ,.. ]

B0Lemma: ", B0POS: FB, B0Token: ", TransHistory3: 020, 

49- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= ["]   B= [,, una, eroina ,.. ]

B0Lemma: ,, B0POS: FF, B0Token: ,, S0B0Lemma: "_,, S0B0LemmaPOS: "_FF, S0B0POS: FB_FF, S0B0POSLemma: FB_,, S0B0Token: "_,, S0B1Lemma: "_una, S0B1LemmaPOS: "_RI, S0B1POS: FB_RI, S0B1POSLemma: FB_una, S0B1Token: "_una, S0Lemma: ", S0POS: FB, S0Token: ", TransHistory3: 202, 

50- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, una, eroina ,.. ]

B0Lemma: ,, B0POS: FF, B0Token: ,, TransHistory3: 020, 

51- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [una, eroina, di ,.. ]

,_isGouvernedBy_eroina: true, ,_isGouvernedBy_eroina_punc: true, B0Lemma: una, B0POS: RI, B0Token: una, S0B0Lemma: ,_una, S0B0LemmaPOS: ,_RI, S0B0POS: FF_RI, S0B0POSLemma: FF_una, S0B0Token: ,_una, S0B1Lemma: ,_eroina, S0B1LemmaPOS: ,_S, S0B1POS: FF_S, S0B1POSLemma: FF_eroina, S0B1Token: ,_eroina, S0Lemma: ,, S0POS: FF, S0Token: ,, TransHistory3: 202, 

52- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [una, eroina, di ,.. ]

B0Lemma: una, B0POS: RI, B0Token: una, TransHistory3: 020, 

53- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [una]   B= [eroina, di, walter ,.. ]

B0Lemma: eroina, B0POS: S, B0Token: eroina, S0B0Lemma: una_eroina, S0B0LemmaPOS: una_S, S0B0POS: RI_S, S0B0POSLemma: RI_eroina, S0B0Token: una_eroina, S0B1Lemma: una_di, S0B1LemmaPOS: una_E, S0B1POS: RI_E, S0B1POSLemma: RI_di, S0B1Token: una_di, S0Lemma: una, S0POS: RI, S0Token: una, TransHistory3: 202, una_isGouvernedBy_eroina: true, una_isGouvernedBy_eroina_det: true, 

54- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [eroina, di, walter ,.. ]

B0Lemma: eroina, B0POS: S, B0Token: eroina, TransHistory3: 020, 

55- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [eroina]   B= [di, walter, scott ,.. ]

B0Lemma: di, B0POS: E, B0Token: di, S0B0Lemma: eroina_di, S0B0LemmaPOS: eroina_E, S0B0POS: S_E, S0B0POSLemma: S_di, S0B0Token: eroina_di, S0B1Lemma: eroina_Walter, S0B1LemmaPOS: eroina_SP, S0B1POS: S_SP, S0B1POSLemma: S_Walter, S0B1Token: eroina_walter, S0Lemma: eroina, S0POS: S, S0Token: eroina, TransHistory3: 202, eroina_di_hasRighDep_comp: true, eroina_hasRighDep_comp: true, eroina_hasRighDep_punc: true, eroina_»_hasRighDep_punc: true, hasRighDep_comp: true, hasRighDep_punc: true, 

56- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [di, walter, scott ,.. ]

B0Lemma: di, B0POS: E, B0Token: di, TransHistory3: 020, 

57- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [di]   B= [walter, scott, » ,.. ]

B0Lemma: Walter, B0POS: SP, B0Token: walter, S0B0Lemma: di_Walter, S0B0LemmaPOS: di_SP, S0B0POS: E_SP, S0B0POSLemma: E_Walter, S0B0Token: di_walter, S0B1Lemma: di_Scott, S0B1LemmaPOS: di_SP, S0B1POS: E_SP, S0B1POSLemma: E_Scott, S0B1Token: di_scott, S0Lemma: di, S0POS: E, S0Token: di, TransHistory3: 202, di_Scott_hasRighDep_prep: true, di_hasRighDep_prep: true, hasRighDep_prep: true, 

58- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [walter, scott, » ,.. ]

B0Lemma: Walter, B0POS: SP, B0Token: walter, TransHistory3: 020, 

59- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [walter]   B= [scott, », . ,.. ]

B0Lemma: Scott, B0POS: SP, B0Token: scott, S0B0Lemma: Walter_Scott, S0B0LemmaPOS: Walter_SP, S0B0POS: SP_SP, S0B0POSLemma: SP_Scott, S0B0Token: walter_scott, S0B1Lemma: Walter_», S0B1LemmaPOS: Walter_FB, S0B1POS: SP_FB, S0B1POSLemma: SP_», S0B1Token: walter_», S0Lemma: Walter, S0POS: SP, S0Token: walter, TransHistory3: 202, Walter_isGouvernedBy_Scott: true, Walter_isGouvernedBy_Scott_mod: true, 

60- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [scott, », . ,.. ]

B0Lemma: Scott, B0POS: SP, B0Token: scott, TransHistory3: 020, 

61- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [scott]   B= [», . ,.. ]

B0Lemma: », B0POS: FB, B0Token: », S0B0Lemma: Scott_», S0B0LemmaPOS: Scott_FB, S0B0POS: SP_FB, S0B0POSLemma: SP_», S0B0Token: scott_», S0B1Lemma: Scott_., S0B1LemmaPOS: Scott_FS, S0B1POS: SP_FS, S0B1POSLemma: SP_., S0B1Token: scott_., S0Lemma: Scott, S0POS: SP, S0Token: scott, TransHistory3: 202, 

62- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [», . ,.. ]

B0Lemma: », B0POS: FB, B0Token: », TransHistory3: 020, 

63- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [»]   B= [.]

B0Lemma: ., B0POS: FS, B0Token: ., S0B0Lemma: »_., S0B0LemmaPOS: »_FS, S0B0POS: FB_FS, S0B0POSLemma: FB_., S0B0Token: »_., S0Lemma: », S0POS: FB, S0Token: », TransHistory3: 202, 

64- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [.]

B0Lemma: ., B0POS: FS, B0Token: ., TransHistory3: 020, 

65- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [ ]

S0Lemma: ., S0POS: FS, S0Token: ., TransHistory3: 202, 

66- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

## Sentence No. 12791 - 
i due giovani si sposarono a vicenza il 31 luglio 1866 , poche settimane dopo che il veneto , a seguito della terza guerra di indipendenza , era entrato a far parte del regno d' italia . 
### Existing MWEs: 
1- **si sposarono** (IReflV)
3- **entrato a far parte** (ID)
2- **far parte** (LVC), Embedded



0- &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [i, due, giovani ,.. ]

B0Lemma: il, B0POS: RD, B0Token: i, 

1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [i]   B= [due, giovani, si ,.. ]

B0Lemma: due, B0POS: N, B0Token: due, S0B0Lemma: il_due, S0B0LemmaPOS: il_N, S0B0POS: RD_N, S0B0POSLemma: RD_due, S0B0Token: i_due, S0B1Lemma: il_giovane, S0B1LemmaPOS: il_A, S0B1POS: RD_A, S0B1POSLemma: RD_giovane, S0B1Token: i_giovani, S0Lemma: il, S0POS: RD, S0Token: i, il_isGouvernedBy_due: true, il_isGouvernedBy_due_det: true, 

2- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [due, giovani, si ,.. ]

B0Lemma: due, B0POS: N, B0Token: due, 

3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [due]   B= [giovani, si, sposarono ,.. ]

B0Lemma: giovane, B0POS: A, B0Token: giovani, S0B0Lemma: due_giovane, S0B0LemmaPOS: due_A, S0B0POS: N_A, S0B0POSLemma: N_giovane, S0B0Token: due_giovani, S0B1Lemma: due_si, S0B1LemmaPOS: due_PC, S0B1POS: N_PC, S0B1POSLemma: N_si, S0B1Token: due_si, S0Lemma: due, S0POS: N, S0Token: due, due_giovane_hasRighDep_mod: true, due_hasRighDep_mod: true, due_isGouvernedBy_sposare: true, due_isGouvernedBy_sposare_subj: true, hasRighDep_mod: true, 

4- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [giovani, si, sposarono ,.. ]

B0Lemma: giovane, B0POS: A, B0Token: giovani, TransHistory3: 020, 

5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [giovani]   B= [si, sposarono, a ,.. ]

B0Lemma: si, B0POS: PC, B0Token: si, S0B0Lemma: giovane_si, S0B0LemmaPOS: giovane_PC, S0B0POS: A_PC, S0B0POSLemma: A_si, S0B0Token: giovani_si, S0B1Lemma: giovane_sposare, S0B1LemmaPOS: giovane_V, S0B1POS: A_V, S0B1POSLemma: A_sposare, S0B1Token: giovani_sposarono, S0Lemma: giovane, S0POS: A, S0Token: giovani, TransHistory3: 202, 

6- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [si, sposarono, a ,.. ]

B0Lemma: si, B0POS: PC, B0Token: si, TransHistory3: 020, 

7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [si]   B= [sposarono, a, vicenza ,.. ]

B0Lemma: sposare, B0POS: V, B0Token: sposarono, S0B0Lemma: si_sposare, S0B0LemmaPOS: si_V, S0B0POS: PC_V, S0B0POSLemma: PC_sposare, S0B0Token: si_sposarono, S0B1Lemma: si_a, S0B1LemmaPOS: si_E, S0B1POS: PC_E, S0B1POSLemma: PC_a, S0B1Token: si_a, S0Lemma: si, S0POS: PC, S0Token: si, TransHistory3: 202, si_isGouvernedBy_sposare: true, si_isGouvernedBy_sposare_clit: true, 

8- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [si, sposarono]   B= [a, vicenza, il ,.. ]

B0Lemma: a, B0POS: E, B0Token: a, S0B0Lemma: sposare_a, S0B0LemmaPOS: sposare_E, S0B0POS: V_E, S0B0POSLemma: V_a, S0B0Token: sposarono_a, S0B1Lemma: sposare_Vicenza, S0B1LemmaPOS: sposare_SP, S0B1POS: V_SP, S0B1POSLemma: V_Vicenza, S0B1Token: sposarono_vicenza, S0Lemma: sposare, S0POS: V, S0S1Distance: 1, S0Token: sposarono, S1B0Lemma: si_a, S1B0LemmaPOS: si_E, S1B0POS: PC_E, S1B0POSLemma: PC_a, S1B0Token: si_a, S1Lemma: si, S1POS: PC, S1S0Lemma: si_sposare, S1S0LemmaPOS: si_V, S1S0POS: PC_V, S1S0POSLemma: PC_sposare, S1S0Token: si_sposarono, S1Token: si, TransHistory3: 020, 

9- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[si, sposarono]]   B= [a, vicenza, il ,.. ]

B0Lemma: a, B0POS: E, B0Token: a, S0B0Lemma: si_sposare_a, S0B0LemmaPOS: si_sposare_E, S0B0POS: PC_V_E, S0B0POSLemma: PC_V_a, S0B0Token: si_sposarono_a, S0B1Lemma: si_sposare_Vicenza, S0B1LemmaPOS: si_sposare_SP, S0B1POS: PC_V_SP, S0B1POSLemma: PC_V_Vicenza, S0B1Token: si_sposarono_vicenza, S0Lemma: si_sposare, S0POS: PC_V, S0Token: si_sposarono, TransHistory3: 002, 

10- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [a, vicenza, il ,.. ]

B0Lemma: a, B0POS: E, B0Token: a, TransHistory3: 100, 

11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [a]   B= [vicenza, il, 31 ,.. ]

B0Lemma: Vicenza, B0POS: SP, B0Token: vicenza, S0B0Lemma: a_Vicenza, S0B0LemmaPOS: a_SP, S0B0POS: E_SP, S0B0POSLemma: E_Vicenza, S0B0Token: a_vicenza, S0B1Lemma: a_il, S0B1LemmaPOS: a_RD, S0B1POS: E_RD, S0B1POSLemma: E_il, S0B1Token: a_il, S0Lemma: a, S0POS: E, S0Token: a, TransHistory3: 210, a_Vicenza_hasRighDep_prep: true, a_hasRighDep_prep: true, hasRighDep_prep: true, 

12- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [vicenza, il, 31 ,.. ]

B0Lemma: Vicenza, B0POS: SP, B0Token: vicenza, TransHistory3: 021, 

13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [vicenza]   B= [il, 31, luglio ,.. ]

B0Lemma: il, B0POS: RD, B0Token: il, S0B0Lemma: Vicenza_il, S0B0LemmaPOS: Vicenza_RD, S0B0POS: SP_RD, S0B0POSLemma: SP_il, S0B0Token: vicenza_il, S0B1Lemma: Vicenza_31, S0B1LemmaPOS: Vicenza_N, S0B1POS: SP_N, S0B1POSLemma: SP_31, S0B1Token: vicenza_31, S0Lemma: Vicenza, S0POS: SP, S0Token: vicenza, TransHistory3: 202, Vicenza_31_hasRighDep_mod: true, Vicenza_hasRighDep_mod: true, hasRighDep_mod: true, 

14- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [il, 31, luglio ,.. ]

B0Lemma: il, B0POS: RD, B0Token: il, TransHistory3: 020, 

15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [il]   B= [31, luglio, 1866 ,.. ]

B0Lemma: 31, B0POS: N, B0Token: 31, S0B0Lemma: il_31, S0B0LemmaPOS: il_N, S0B0POS: RD_N, S0B0POSLemma: RD_31, S0B0Token: il_31, S0B1Lemma: il_luglio, S0B1LemmaPOS: il_S, S0B1POS: RD_S, S0B1POSLemma: RD_luglio, S0B1Token: il_luglio, S0Lemma: il, S0POS: RD, S0Token: il, TransHistory3: 202, il_isGouvernedBy_31: true, il_isGouvernedBy_31_det: true, 

16- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [31, luglio, 1866 ,.. ]

B0Lemma: 31, B0POS: N, B0Token: 31, TransHistory3: 020, 

17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [31]   B= [luglio, 1866, , ,.. ]

31_,_hasRighDep_punc: true, 31_hasRighDep_mod: true, 31_hasRighDep_punc: true, 31_luglio_hasRighDep_mod: true, B0Lemma: luglio, B0POS: S, B0Token: luglio, S0B0Lemma: 31_luglio, S0B0LemmaPOS: 31_S, S0B0POS: N_S, S0B0POSLemma: N_luglio, S0B0Token: 31_luglio, S0B1Lemma: 31_1866, S0B1LemmaPOS: 31_N, S0B1POS: N_N, S0B1POSLemma: N_1866, S0B1Token: 31_1866, S0Lemma: 31, S0POS: N, S0Token: 31, TransHistory3: 202, hasRighDep_mod: true, hasRighDep_punc: true, 

18- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [luglio, 1866, , ,.. ]

B0Lemma: luglio, B0POS: S, B0Token: luglio, TransHistory3: 020, 

19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [luglio]   B= [1866, ,, poche ,.. ]

B0Lemma: 1866, B0POS: N, B0Token: 1866, S0B0Lemma: luglio_1866, S0B0LemmaPOS: luglio_N, S0B0POS: S_N, S0B0POSLemma: S_1866, S0B0Token: luglio_1866, S0B1Lemma: luglio_,, S0B1LemmaPOS: luglio_FF, S0B1POS: S_FF, S0B1POSLemma: S_,, S0B1Token: luglio_,, S0Lemma: luglio, S0POS: S, S0Token: luglio, TransHistory3: 202, hasRighDep_mod: true, luglio_1866_hasRighDep_mod: true, luglio_hasRighDep_mod: true, 

20- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [1866, ,, poche ,.. ]

B0Lemma: 1866, B0POS: N, B0Token: 1866, TransHistory3: 020, 

21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [1866]   B= [,, poche, settimane ,.. ]

B0Lemma: ,, B0POS: FF, B0Token: ,, S0B0Lemma: 1866_,, S0B0LemmaPOS: 1866_FF, S0B0POS: N_FF, S0B0POSLemma: N_,, S0B0Token: 1866_,, S0B1Lemma: 1866_poco, S0B1LemmaPOS: 1866_DI, S0B1POS: N_DI, S0B1POSLemma: N_poco, S0B1Token: 1866_poche, S0Lemma: 1866, S0POS: N, S0Token: 1866, TransHistory3: 202, 

22- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, poche, settimane ,.. ]

B0Lemma: ,, B0POS: FF, B0Token: ,, TransHistory3: 020, 

23- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [poche, settimane, dopo ,.. ]

B0Lemma: poco, B0POS: DI, B0Token: poche, S0B0Lemma: ,_poco, S0B0LemmaPOS: ,_DI, S0B0POS: FF_DI, S0B0POSLemma: FF_poco, S0B0Token: ,_poche, S0B1Lemma: ,_settimana, S0B1LemmaPOS: ,_S, S0B1POS: FF_S, S0B1POSLemma: FF_settimana, S0B1Token: ,_settimane, S0Lemma: ,, S0POS: FF, S0Token: ,, TransHistory3: 202, 

24- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [poche, settimane, dopo ,.. ]

B0Lemma: poco, B0POS: DI, B0Token: poche, TransHistory3: 020, 

25- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [poche]   B= [settimane, dopo, che ,.. ]

B0Lemma: settimana, B0POS: S, B0Token: settimane, S0B0Lemma: poco_settimana, S0B0LemmaPOS: poco_S, S0B0POS: DI_S, S0B0POSLemma: DI_settimana, S0B0Token: poche_settimane, S0B1Lemma: poco_dopo, S0B1LemmaPOS: poco_E, S0B1POS: DI_E, S0B1POSLemma: DI_dopo, S0B1Token: poche_dopo, S0Lemma: poco, S0POS: DI, S0Token: poche, TransHistory3: 202, poco_isGouvernedBy_settimana: true, poco_isGouvernedBy_settimana_mod: true, 

26- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [settimane, dopo, che ,.. ]

B0Lemma: settimana, B0POS: S, B0Token: settimane, TransHistory3: 020, 

27- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [settimane]   B= [dopo, che, il ,.. ]

B0Lemma: dopo, B0POS: E, B0Token: dopo, S0B0Lemma: settimana_dopo, S0B0LemmaPOS: settimana_E, S0B0POS: S_E, S0B0POSLemma: S_dopo, S0B0Token: settimane_dopo, S0B1Lemma: settimana_che, S0B1LemmaPOS: settimana_PR, S0B1POS: S_PR, S0B1POSLemma: S_che, S0B1Token: settimane_che, S0Lemma: settimana, S0POS: S, S0Token: settimane, TransHistory3: 202, hasRighDep_mod_rel: true, settimana_entrare_hasRighDep_mod_rel: true, settimana_hasRighDep_mod_rel: true, 

28- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [dopo, che, il ,.. ]

B0Lemma: dopo, B0POS: E, B0Token: dopo, TransHistory3: 020, 

29- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [dopo]   B= [che, il, veneto ,.. ]

B0Lemma: che, B0POS: PR, B0Token: che, S0B0Lemma: dopo_che, S0B0LemmaPOS: dopo_PR, S0B0POS: E_PR, S0B0POSLemma: E_che, S0B0Token: dopo_che, S0B1Lemma: dopo_il, S0B1LemmaPOS: dopo_RD, S0B1POS: E_RD, S0B1POSLemma: E_il, S0B1Token: dopo_il, S0Lemma: dopo, S0POS: E, S0Token: dopo, TransHistory3: 202, dopo_che_hasRighDep_prep: true, dopo_hasRighDep_prep: true, dopo_isGouvernedBy_entrare: true, dopo_isGouvernedBy_entrare_comp: true, hasRighDep_prep: true, 

30- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [che, il, veneto ,.. ]

B0Lemma: che, B0POS: PR, B0Token: che, TransHistory3: 020, 

31- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [che]   B= [il, veneto, , ,.. ]

B0Lemma: il, B0POS: RD, B0Token: il, S0B0Lemma: che_il, S0B0LemmaPOS: che_RD, S0B0POS: PR_RD, S0B0POSLemma: PR_il, S0B0Token: che_il, S0B1Lemma: che_Veneto, S0B1LemmaPOS: che_SP, S0B1POS: PR_SP, S0B1POSLemma: PR_Veneto, S0B1Token: che_veneto, S0Lemma: che, S0POS: PR, S0Token: che, TransHistory3: 202, 

32- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [il, veneto, , ,.. ]

B0Lemma: il, B0POS: RD, B0Token: il, TransHistory3: 020, 

33- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [il]   B= [veneto, ,, a ,.. ]

B0Lemma: Veneto, B0POS: SP, B0Token: veneto, S0B0Lemma: il_Veneto, S0B0LemmaPOS: il_SP, S0B0POS: RD_SP, S0B0POSLemma: RD_Veneto, S0B0Token: il_veneto, S0B1Lemma: il_,, S0B1LemmaPOS: il_FF, S0B1POS: RD_FF, S0B1POSLemma: RD_,, S0B1Token: il_,, S0Lemma: il, S0POS: RD, S0Token: il, TransHistory3: 202, il_isGouvernedBy_Veneto: true, il_isGouvernedBy_Veneto_det: true, 

34- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [veneto, ,, a ,.. ]

B0Lemma: Veneto, B0POS: SP, B0Token: veneto, TransHistory3: 020, 

35- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [veneto]   B= [,, a, seguito ,.. ]

B0Lemma: ,, B0POS: FF, B0Token: ,, S0B0Lemma: Veneto_,, S0B0LemmaPOS: Veneto_FF, S0B0POS: SP_FF, S0B0POSLemma: SP_,, S0B0Token: veneto_,, S0B1Lemma: Veneto_a, S0B1LemmaPOS: Veneto_E, S0B1POS: SP_E, S0B1POSLemma: SP_a, S0B1Token: veneto_a, S0Lemma: Veneto, S0POS: SP, S0Token: veneto, TransHistory3: 202, Veneto_isGouvernedBy_entrare: true, Veneto_isGouvernedBy_entrare_subj: true, 

36- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, a, seguito ,.. ]

B0Lemma: ,, B0POS: FF, B0Token: ,, TransHistory3: 020, 

37- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [a, seguito, della ,.. ]

,_isGouvernedBy_a: true, ,_isGouvernedBy_a_punc: true, B0Lemma: a, B0POS: E, B0Token: a, S0B0Lemma: ,_a, S0B0LemmaPOS: ,_E, S0B0POS: FF_E, S0B0POSLemma: FF_a, S0B0Token: ,_a, S0B1Lemma: ,_seguito, S0B1LemmaPOS: ,_S, S0B1POS: FF_S, S0B1POSLemma: FF_seguito, S0B1Token: ,_seguito, S0Lemma: ,, S0POS: FF, S0Token: ,, TransHistory3: 202, 

38- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [a, seguito, della ,.. ]

B0Lemma: a, B0POS: E, B0Token: a, TransHistory3: 020, 

39- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [a]   B= [seguito, della, terza ,.. ]

B0Lemma: seguito, B0POS: S, B0Token: seguito, S0B0Lemma: a_seguito, S0B0LemmaPOS: a_S, S0B0POS: E_S, S0B0POSLemma: E_seguito, S0B0Token: a_seguito, S0B1Lemma: a_di, S0B1LemmaPOS: a_EA, S0B1POS: E_EA, S0B1POSLemma: E_di, S0B1Token: a_della, S0Lemma: a, S0POS: E, S0Token: a, TransHistory3: 202, a_,_hasRighDep_punc: true, a_hasRighDep_prep: true, a_hasRighDep_punc: true, a_isGouvernedBy_entrare: true, a_isGouvernedBy_entrare_comp: true, a_seguito_hasRighDep_prep: true, hasRighDep_prep: true, hasRighDep_punc: true, 

40- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [seguito, della, terza ,.. ]

B0Lemma: seguito, B0POS: S, B0Token: seguito, TransHistory3: 020, 

41- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [seguito]   B= [della, terza, guerra ,.. ]

B0Lemma: di, B0POS: EA, B0Token: della, S0B0Lemma: seguito_di, S0B0LemmaPOS: seguito_EA, S0B0POS: S_EA, S0B0POSLemma: S_di, S0B0Token: seguito_della, S0B1Lemma: seguito_terzo, S0B1LemmaPOS: seguito_NO, S0B1POS: S_NO, S0B1POSLemma: S_terzo, S0B1Token: seguito_terza, S0Lemma: seguito, S0POS: S, S0Token: seguito, TransHistory3: 202, hasRighDep_comp: true, seguito_di_hasRighDep_comp: true, seguito_hasRighDep_comp: true, 

42- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [della, terza, guerra ,.. ]

B0Lemma: di, B0POS: EA, B0Token: della, TransHistory3: 020, 

43- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [della]   B= [terza, guerra, di ,.. ]

B0Lemma: terzo, B0POS: NO, B0Token: terza, S0B0Lemma: di_terzo, S0B0LemmaPOS: di_NO, S0B0POS: EA_NO, S0B0POSLemma: EA_terzo, S0B0Token: della_terza, S0B1Lemma: di_guerra, S0B1LemmaPOS: di_S, S0B1POS: EA_S, S0B1POSLemma: EA_guerra, S0B1Token: della_guerra, S0Lemma: di, S0POS: EA, S0Token: della, TransHistory3: 202, di_guerra_hasRighDep_prep: true, di_hasRighDep_prep: true, hasRighDep_prep: true, 

44- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [terza, guerra, di ,.. ]

B0Lemma: terzo, B0POS: NO, B0Token: terza, TransHistory3: 020, 

45- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [terza]   B= [guerra, di, indipendenza ,.. ]

B0Lemma: guerra, B0POS: S, B0Token: guerra, S0B0Lemma: terzo_guerra, S0B0LemmaPOS: terzo_S, S0B0POS: NO_S, S0B0POSLemma: NO_guerra, S0B0Token: terza_guerra, S0B1Lemma: terzo_di, S0B1LemmaPOS: terzo_E, S0B1POS: NO_E, S0B1POSLemma: NO_di, S0B1Token: terza_di, S0Lemma: terzo, S0POS: NO, S0Token: terza, TransHistory3: 202, terzo_isGouvernedBy_guerra: true, terzo_isGouvernedBy_guerra_mod: true, 

46- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [guerra, di, indipendenza ,.. ]

B0Lemma: guerra, B0POS: S, B0Token: guerra, TransHistory3: 020, 

47- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [guerra]   B= [di, indipendenza, , ,.. ]

B0Lemma: di, B0POS: E, B0Token: di, S0B0Lemma: guerra_di, S0B0LemmaPOS: guerra_E, S0B0POS: S_E, S0B0POSLemma: S_di, S0B0Token: guerra_di, S0B1Lemma: guerra_indipendenza, S0B1LemmaPOS: guerra_S, S0B1POS: S_S, S0B1POSLemma: S_indipendenza, S0B1Token: guerra_indipendenza, S0Lemma: guerra, S0POS: S, S0Token: guerra, TransHistory3: 202, guerra_di_hasRighDep_comp: true, guerra_hasRighDep_comp: true, hasRighDep_comp: true, 

48- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [di, indipendenza, , ,.. ]

B0Lemma: di, B0POS: E, B0Token: di, TransHistory3: 020, 

49- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [di]   B= [indipendenza, ,, era ,.. ]

B0Lemma: indipendenza, B0POS: S, B0Token: indipendenza, S0B0Lemma: di_indipendenza, S0B0LemmaPOS: di_S, S0B0POS: E_S, S0B0POSLemma: E_indipendenza, S0B0Token: di_indipendenza, S0B1Lemma: di_,, S0B1LemmaPOS: di_FF, S0B1POS: E_FF, S0B1POSLemma: E_,, S0B1Token: di_,, S0Lemma: di, S0POS: E, S0Token: di, TransHistory3: 202, di_hasRighDep_prep: true, di_indipendenza_hasRighDep_prep: true, hasRighDep_prep: true, 

50- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [indipendenza, ,, era ,.. ]

B0Lemma: indipendenza, B0POS: S, B0Token: indipendenza, TransHistory3: 020, 

51- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [indipendenza]   B= [,, era, entrato ,.. ]

B0Lemma: ,, B0POS: FF, B0Token: ,, S0B0Lemma: indipendenza_,, S0B0LemmaPOS: indipendenza_FF, S0B0POS: S_FF, S0B0POSLemma: S_,, S0B0Token: indipendenza_,, S0B1Lemma: indipendenza_essere, S0B1LemmaPOS: indipendenza_VA, S0B1POS: S_VA, S0B1POSLemma: S_essere, S0B1Token: indipendenza_era, S0Lemma: indipendenza, S0POS: S, S0Token: indipendenza, TransHistory3: 202, 

52- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, era, entrato ,.. ]

B0Lemma: ,, B0POS: FF, B0Token: ,, TransHistory3: 020, 

53- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [era, entrato, a ,.. ]

B0Lemma: essere, B0POS: VA, B0Token: era, S0B0Lemma: ,_essere, S0B0LemmaPOS: ,_VA, S0B0POS: FF_VA, S0B0POSLemma: FF_essere, S0B0Token: ,_era, S0B1Lemma: ,_entrare, S0B1LemmaPOS: ,_V, S0B1POS: FF_V, S0B1POSLemma: FF_entrare, S0B1Token: ,_entrato, S0Lemma: ,, S0POS: FF, S0Token: ,, TransHistory3: 202, 

54- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [era, entrato, a ,.. ]

B0Lemma: essere, B0POS: VA, B0Token: era, TransHistory3: 020, 

55- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [era]   B= [entrato, a, far ,.. ]

B0Lemma: entrare, B0POS: V, B0Token: entrato, S0B0Lemma: essere_entrare, S0B0LemmaPOS: essere_V, S0B0POS: VA_V, S0B0POSLemma: VA_entrare, S0B0Token: era_entrato, S0B1Lemma: essere_a, S0B1LemmaPOS: essere_E, S0B1POS: VA_E, S0B1POSLemma: VA_a, S0B1Token: era_a, S0Lemma: essere, S0POS: VA, S0Token: era, TransHistory3: 202, essere_isGouvernedBy_entrare: true, essere_isGouvernedBy_entrare_aux: true, 

56- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [entrato, a, far ,.. ]

B0Lemma: entrare, B0POS: V, B0Token: entrato, TransHistory3: 020, 

57- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [entrato]   B= [a, far, parte ,.. ]

B0Lemma: a, B0POS: E, B0Token: a, S0B0Lemma: entrare_a, S0B0LemmaPOS: entrare_E, S0B0POS: V_E, S0B0POSLemma: V_a, S0B0Token: entrato_a, S0B1Lemma: entrare_fare, S0B1LemmaPOS: entrare_V, S0B1POS: V_V, S0B1POSLemma: V_fare, S0B1Token: entrato_far, S0Lemma: entrare, S0POS: V, S0Token: entrato, TransHistory3: 202, entrare_a_hasRighDep_arg: true, entrare_hasRighDep_arg: true, hasRighDep_arg: true, 

58- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [entrato, a]   B= [far, parte, del ,.. ]

B0Lemma: fare, B0POS: V, B0Token: far, S0B0Lemma: a_fare, S0B0LemmaPOS: a_V, S0B0POS: E_V, S0B0POSLemma: E_fare, S0B0Token: a_far, S0B1Lemma: a_parte, S0B1LemmaPOS: a_S, S0B1POS: E_S, S0B1POSLemma: E_parte, S0B1Token: a_parte, S0Lemma: a, S0POS: E, S0S1Distance: 1, S0Token: a, S1B0Lemma: entrare_fare, S1B0LemmaPOS: entrare_V, S1B0POS: V_V, S1B0POSLemma: V_fare, S1B0Token: entrato_far, S1Lemma: entrare, S1POS: V, S1S0Lemma: entrare_a, S1S0LemmaPOS: entrare_E, S1S0POS: V_E, S1S0POSLemma: V_a, S1S0Token: entrato_a, S1Token: entrato, SyntaxicRelation: +arg, TransHistory3: 020, a_fare_hasRighDep_prep: true, a_hasRighDep_prep: true, hasRighDep_prep: true, 

59- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [entrato, a, far]   B= [parte, del, regno ,.. ]

B0Lemma: parte, B0POS: S, B0Token: parte, S0B0Lemma: fare_parte, S0B0LemmaPOS: fare_S, S0B0POS: V_S, S0B0POSLemma: V_parte, S0B0Token: far_parte, S0B1Lemma: fare_di, S0B1LemmaPOS: fare_EA, S0B1POS: V_EA, S0B1POSLemma: V_di, S0B1Token: far_del, S0Lemma: fare, S0POS: V, S0S1Distance: 1, S0Token: far, S1B0Lemma: a_parte, S1B0LemmaPOS: a_S, S1B0POS: E_S, S1B0POSLemma: E_parte, S1B0Token: a_parte, S1Lemma: a, S1POS: E, S1S0Lemma: a_fare, S1S0LemmaPOS: a_V, S1S0POS: E_V, S1S0POSLemma: E_fare, S1S0Token: a_far, S1Token: a, SyntaxicRelation: +prep, TransHistory3: 002, fare_hasRighDep_obj: true, fare_parte_hasRighDep_obj: true, hasRighDep_obj: true, 

60- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [entrato, a, far, parte]   B= [del, regno, d' ,.. ]

B0Lemma: di, B0POS: EA, B0Token: del, S0B0Lemma: parte_di, S0B0LemmaPOS: parte_EA, S0B0POS: S_EA, S0B0POSLemma: S_di, S0B0Token: parte_del, S0B1Lemma: parte_Regno, S0B1LemmaPOS: parte_SP, S0B1POS: S_SP, S0B1POSLemma: S_Regno, S0B1Token: parte_regno, S0Lemma: parte, S0POS: S, S0S1Distance: 1, S0Token: parte, S1B0Lemma: fare_di, S1B0LemmaPOS: fare_EA, S1B0POS: V_EA, S1B0POSLemma: V_di, S1B0Token: far_del, S1Lemma: fare, S1POS: V, S1S0Lemma: fare_parte, S1S0LemmaPOS: fare_S, S1S0POS: V_S, S1S0POSLemma: V_parte, S1S0Token: far_parte, S1Token: far, SyntaxicRelation: +obj, TransHistory3: 000, hasRighDep_comp: true, parte_di_hasRighDep_comp: true, parte_hasRighDep_comp: true, 

61- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [entrato, a, [far, parte]]   B= [del, regno, d' ,.. ]

B0Lemma: di, B0POS: EA, B0Token: del, S0B0Lemma: fare_parte_di, S0B0LemmaPOS: fare_parte_EA, S0B0POS: V_S_EA, S0B0POSLemma: V_S_di, S0B0Token: far_parte_del, S0B1Lemma: fare_parte_Regno, S0B1LemmaPOS: fare_parte_SP, S0B1POS: V_S_SP, S0B1POSLemma: V_S_Regno, S0B1Token: far_parte_regno, S0Lemma: fare_parte, S0POS: V_S, S0Token: far_parte, S1B0Lemma: a_di, S1B0LemmaPOS: a_EA, S1B0POS: E_EA, S1B0POSLemma: E_di, S1B0Token: a_del, S1Lemma: a, S1POS: E, S1S0Lemma: a_fare_parte, S1S0LemmaPOS: a_V_S, S1S0POS: E_V_S, S1S0POSLemma: E_fare_parte, S1S0Token: a_far_parte, S1Token: a, TransHistory3: 000, 

62- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [entrato, [a, [far, parte]]]   B= [del, regno, d' ,.. ]

B0Lemma: di, B0POS: EA, B0Token: del, S0B0Lemma: a_fare_parte_di, S0B0LemmaPOS: a_fare_parte_EA, S0B0POS: E_V_S_EA, S0B0POSLemma: E_V_S_di, S0B0Token: a_far_parte_del, S0B1Lemma: a_fare_parte_Regno, S0B1LemmaPOS: a_fare_parte_SP, S0B1POS: E_V_S_SP, S0B1POSLemma: E_V_S_Regno, S0B1Token: a_far_parte_regno, S0Lemma: a_fare_parte, S0POS: E_V_S, S0Token: a_far_parte, S1B0Lemma: entrare_di, S1B0LemmaPOS: entrare_EA, S1B0POS: V_EA, S1B0POSLemma: V_di, S1B0Token: entrato_del, S1Lemma: entrare, S1POS: V, S1S0Lemma: entrare_a_fare_parte, S1S0LemmaPOS: entrare_E_V_S, S1S0POS: V_E_V_S, S1S0POSLemma: V_a_fare_parte, S1S0Token: entrato_a_far_parte, S1Token: entrato, TransHistory3: 100, 

63- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[entrato, [a, [far, parte]]]]   B= [del, regno, d' ,.. ]

B0Lemma: di, B0POS: EA, B0Token: del, S0B0Lemma: entrare_a_fare_parte_di, S0B0LemmaPOS: entrare_a_fare_parte_EA, S0B0POS: V_E_V_S_EA, S0B0POSLemma: V_E_V_S_di, S0B0Token: entrato_a_far_parte_del, S0B1Lemma: entrare_a_fare_parte_Regno, S0B1LemmaPOS: entrare_a_fare_parte_SP, S0B1POS: V_E_V_S_SP, S0B1POSLemma: V_E_V_S_Regno, S0B1Token: entrato_a_far_parte_regno, S0Lemma: entrare_a_fare_parte, S0POS: V_E_V_S, S0Token: entrato_a_far_parte, TransHistory3: 110, 

64- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [del, regno, d' ,.. ]

B0Lemma: di, B0POS: EA, B0Token: del, TransHistory3: 111, 

65- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [del]   B= [regno, d', italia ,.. ]

B0Lemma: Regno, B0POS: SP, B0Token: regno, S0B0Lemma: di_Regno, S0B0LemmaPOS: di_SP, S0B0POS: EA_SP, S0B0POSLemma: EA_Regno, S0B0Token: del_regno, S0B1Lemma: di_d', S0B1LemmaPOS: di_E, S0B1POS: EA_E, S0B1POSLemma: EA_d', S0B1Token: del_d', S0Lemma: di, S0POS: EA, S0Token: del, TransHistory3: 211, di_Regno_hasRighDep_prep: true, di_hasRighDep_prep: true, hasRighDep_prep: true, 

66- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [regno, d', italia ,.. ]

B0Lemma: Regno, B0POS: SP, B0Token: regno, TransHistory3: 021, 

67- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [regno]   B= [d', italia, . ,.. ]

B0Lemma: d', B0POS: E, B0Token: d', Regno_d'_hasRighDep_comp_loc: true, Regno_hasRighDep_comp_loc: true, S0B0Lemma: Regno_d', S0B0LemmaPOS: Regno_E, S0B0POS: SP_E, S0B0POSLemma: SP_d', S0B0Token: regno_d', S0B1Lemma: Regno_Italia, S0B1LemmaPOS: Regno_SP, S0B1POS: SP_SP, S0B1POSLemma: SP_Italia, S0B1Token: regno_italia, S0Lemma: Regno, S0POS: SP, S0Token: regno, TransHistory3: 202, hasRighDep_comp_loc: true, 

68- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [d', italia, . ,.. ]

B0Lemma: d', B0POS: E, B0Token: d', TransHistory3: 020, 

69- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [d']   B= [italia, . ,.. ]

B0Lemma: Italia, B0POS: SP, B0Token: italia, S0B0Lemma: d'_Italia, S0B0LemmaPOS: d'_SP, S0B0POS: E_SP, S0B0POSLemma: E_Italia, S0B0Token: d'_italia, S0B1Lemma: d'_., S0B1LemmaPOS: d'_FS, S0B1POS: E_FS, S0B1POSLemma: E_., S0B1Token: d'_., S0Lemma: d', S0POS: E, S0Token: d', TransHistory3: 202, d'_Italia_hasRighDep_prep: true, d'_hasRighDep_prep: true, hasRighDep_prep: true, 

70- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [italia, . ,.. ]

B0Lemma: Italia, B0POS: SP, B0Token: italia, TransHistory3: 020, 

71- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [italia]   B= [.]

B0Lemma: ., B0POS: FS, B0Token: ., S0B0Lemma: Italia_., S0B0LemmaPOS: Italia_FS, S0B0POS: SP_FS, S0B0POSLemma: SP_., S0B0Token: italia_., S0Lemma: Italia, S0POS: SP, S0Token: italia, TransHistory3: 202, 

72- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [.]

B0Lemma: ., B0POS: FS, B0Token: ., TransHistory3: 020, 

73- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [ ]

S0Lemma: ., S0POS: FS, S0Token: ., TransHistory3: 202, 

74- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

## Sentence No. 15263 - 
in molti film di hitchcock si rivela l' ossessione del regista per una figura femminile tipica : si tratta di solito di una giovane donna alta e bionda , dai lineamenti sottili e dall' aspetto rassicurante , che quasi sempre si rivela un personaggio ambiguo e malvagio come , ad esempio , la melanie daniels de " gli uccelli " o la madeleine de " la donna che visse due volte " . 
### Existing MWEs: 
1- **si rivela** (IReflV)
2- **si tratta** (IReflV)
3- **si rivela** (IReflV)



0- &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [in, molti, film ,.. ]

B0Lemma: in, B0POS: E, B0Token: in, 

1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [in]   B= [molti, film, di ,.. ]

B0Lemma: molto, B0POS: DI, B0Token: molti, S0B0Lemma: in_molto, S0B0LemmaPOS: in_DI, S0B0POS: E_DI, S0B0POSLemma: E_molto, S0B0Token: in_molti, S0B1Lemma: in_film, S0B1LemmaPOS: in_S, S0B1POS: E_S, S0B1POSLemma: E_film, S0B1Token: in_film, S0Lemma: in, S0POS: E, S0Token: in, hasRighDep_prep: true, in_film_hasRighDep_prep: true, in_hasRighDep_prep: true, in_isGouvernedBy_rivelare: true, in_isGouvernedBy_rivelare_comp: true, 

2- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [molti, film, di ,.. ]

B0Lemma: molto, B0POS: DI, B0Token: molti, 

3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [molti]   B= [film, di, hitchcock ,.. ]

B0Lemma: film, B0POS: S, B0Token: film, S0B0Lemma: molto_film, S0B0LemmaPOS: molto_S, S0B0POS: DI_S, S0B0POSLemma: DI_film, S0B0Token: molti_film, S0B1Lemma: molto_di, S0B1LemmaPOS: molto_E, S0B1POS: DI_E, S0B1POSLemma: DI_di, S0B1Token: molti_di, S0Lemma: molto, S0POS: DI, S0Token: molti, molto_isGouvernedBy_film: true, molto_isGouvernedBy_film_mod: true, 

4- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [film, di, hitchcock ,.. ]

B0Lemma: film, B0POS: S, B0Token: film, TransHistory3: 020, 

5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [film]   B= [di, hitchcock, si ,.. ]

B0Lemma: di, B0POS: E, B0Token: di, S0B0Lemma: film_di, S0B0LemmaPOS: film_E, S0B0POS: S_E, S0B0POSLemma: S_di, S0B0Token: film_di, S0B1Lemma: film_Hitchcock, S0B1LemmaPOS: film_SP, S0B1POS: S_SP, S0B1POSLemma: S_Hitchcock, S0B1Token: film_hitchcock, S0Lemma: film, S0POS: S, S0Token: film, TransHistory3: 202, film_di_hasRighDep_comp: true, film_hasRighDep_comp: true, hasRighDep_comp: true, 

6- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [di, hitchcock, si ,.. ]

B0Lemma: di, B0POS: E, B0Token: di, TransHistory3: 020, 

7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [di]   B= [hitchcock, si, rivela ,.. ]

B0Lemma: Hitchcock, B0POS: SP, B0Token: hitchcock, S0B0Lemma: di_Hitchcock, S0B0LemmaPOS: di_SP, S0B0POS: E_SP, S0B0POSLemma: E_Hitchcock, S0B0Token: di_hitchcock, S0B1Lemma: di_si, S0B1LemmaPOS: di_PC, S0B1POS: E_PC, S0B1POSLemma: E_si, S0B1Token: di_si, S0Lemma: di, S0POS: E, S0Token: di, TransHistory3: 202, di_Hitchcock_hasRighDep_prep: true, di_hasRighDep_prep: true, hasRighDep_prep: true, 

8- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [hitchcock, si, rivela ,.. ]

B0Lemma: Hitchcock, B0POS: SP, B0Token: hitchcock, TransHistory3: 020, 

9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [hitchcock]   B= [si, rivela, l' ,.. ]

B0Lemma: si, B0POS: PC, B0Token: si, S0B0Lemma: Hitchcock_si, S0B0LemmaPOS: Hitchcock_PC, S0B0POS: SP_PC, S0B0POSLemma: SP_si, S0B0Token: hitchcock_si, S0B1Lemma: Hitchcock_rivelare, S0B1LemmaPOS: Hitchcock_V, S0B1POS: SP_V, S0B1POSLemma: SP_rivelare, S0B1Token: hitchcock_rivela, S0Lemma: Hitchcock, S0POS: SP, S0Token: hitchcock, TransHistory3: 202, 

10- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [si, rivela, l' ,.. ]

B0Lemma: si, B0POS: PC, B0Token: si, TransHistory3: 020, 

11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [si]   B= [rivela, l', ossessione ,.. ]

B0Lemma: rivelare, B0POS: V, B0Token: rivela, S0B0Lemma: si_rivelare, S0B0LemmaPOS: si_V, S0B0POS: PC_V, S0B0POSLemma: PC_rivelare, S0B0Token: si_rivela, S0B1Lemma: si_il, S0B1LemmaPOS: si_RD, S0B1POS: PC_RD, S0B1POSLemma: PC_il, S0B1Token: si_l', S0Lemma: si, S0POS: PC, S0Token: si, TransHistory3: 202, si_isGouvernedBy_rivelare: true, si_isGouvernedBy_rivelare_clit: true, 

12- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [si, rivela]   B= [l', ossessione, del ,.. ]

B0Lemma: il, B0POS: RD, B0Token: l', S0B0Lemma: rivelare_il, S0B0LemmaPOS: rivelare_RD, S0B0POS: V_RD, S0B0POSLemma: V_il, S0B0Token: rivela_l', S0B1Lemma: rivelare_ossessione, S0B1LemmaPOS: rivelare_S, S0B1POS: V_S, S0B1POSLemma: V_ossessione, S0B1Token: rivela_ossessione, S0Lemma: rivelare, S0POS: V, S0S1Distance: 1, S0Token: rivela, S1B0Lemma: si_il, S1B0LemmaPOS: si_RD, S1B0POS: PC_RD, S1B0POSLemma: PC_il, S1B0Token: si_l', S1Lemma: si, S1POS: PC, S1S0Lemma: si_rivelare, S1S0LemmaPOS: si_V, S1S0POS: PC_V, S1S0POSLemma: PC_rivelare, S1S0Token: si_rivela, S1Token: si, TransHistory3: 020, 

13- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[si, rivela]]   B= [l', ossessione, del ,.. ]

B0Lemma: il, B0POS: RD, B0Token: l', S0B0Lemma: si_rivelare_il, S0B0LemmaPOS: si_rivelare_RD, S0B0POS: PC_V_RD, S0B0POSLemma: PC_V_il, S0B0Token: si_rivela_l', S0B1Lemma: si_rivelare_ossessione, S0B1LemmaPOS: si_rivelare_S, S0B1POS: PC_V_S, S0B1POSLemma: PC_V_ossessione, S0B1Token: si_rivela_ossessione, S0Lemma: si_rivelare, S0POS: PC_V, S0Token: si_rivela, TransHistory3: 002, 

14- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [l', ossessione, del ,.. ]

B0Lemma: il, B0POS: RD, B0Token: l', TransHistory3: 100, 

15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [l']   B= [ossessione, del, regista ,.. ]

B0Lemma: ossessione, B0POS: S, B0Token: ossessione, S0B0Lemma: il_ossessione, S0B0LemmaPOS: il_S, S0B0POS: RD_S, S0B0POSLemma: RD_ossessione, S0B0Token: l'_ossessione, S0B1Lemma: il_di, S0B1LemmaPOS: il_EA, S0B1POS: RD_EA, S0B1POSLemma: RD_di, S0B1Token: l'_del, S0Lemma: il, S0POS: RD, S0Token: l', TransHistory3: 210, il_isGouvernedBy_ossessione: true, il_isGouvernedBy_ossessione_det: true, 

16- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ossessione, del, regista ,.. ]

B0Lemma: ossessione, B0POS: S, B0Token: ossessione, TransHistory3: 021, 

17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ossessione]   B= [del, regista, per ,.. ]

B0Lemma: di, B0POS: EA, B0Token: del, S0B0Lemma: ossessione_di, S0B0LemmaPOS: ossessione_EA, S0B0POS: S_EA, S0B0POSLemma: S_di, S0B0Token: ossessione_del, S0B1Lemma: ossessione_regista, S0B1LemmaPOS: ossessione_S, S0B1POS: S_S, S0B1POSLemma: S_regista, S0B1Token: ossessione_regista, S0Lemma: ossessione, S0POS: S, S0Token: ossessione, TransHistory3: 202, hasRighDep_comp: true, ossessione_di_hasRighDep_comp: true, ossessione_hasRighDep_comp: true, 

18- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [del, regista, per ,.. ]

B0Lemma: di, B0POS: EA, B0Token: del, TransHistory3: 020, 

19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [del]   B= [regista, per, una ,.. ]

B0Lemma: regista, B0POS: S, B0Token: regista, S0B0Lemma: di_regista, S0B0LemmaPOS: di_S, S0B0POS: EA_S, S0B0POSLemma: EA_regista, S0B0Token: del_regista, S0B1Lemma: di_per, S0B1LemmaPOS: di_E, S0B1POS: EA_E, S0B1POSLemma: EA_per, S0B1Token: del_per, S0Lemma: di, S0POS: EA, S0Token: del, TransHistory3: 202, di_hasRighDep_prep: true, di_regista_hasRighDep_prep: true, hasRighDep_prep: true, 

20- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [regista, per, una ,.. ]

B0Lemma: regista, B0POS: S, B0Token: regista, TransHistory3: 020, 

21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [regista]   B= [per, una, figura ,.. ]

B0Lemma: per, B0POS: E, B0Token: per, S0B0Lemma: regista_per, S0B0LemmaPOS: regista_E, S0B0POS: S_E, S0B0POSLemma: S_per, S0B0Token: regista_per, S0B1Lemma: regista_una, S0B1LemmaPOS: regista_RI, S0B1POS: S_RI, S0B1POSLemma: S_una, S0B1Token: regista_una, S0Lemma: regista, S0POS: S, S0Token: regista, TransHistory3: 202, 

22- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [per, una, figura ,.. ]

B0Lemma: per, B0POS: E, B0Token: per, TransHistory3: 020, 

23- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [per]   B= [una, figura, femminile ,.. ]

B0Lemma: una, B0POS: RI, B0Token: una, S0B0Lemma: per_una, S0B0LemmaPOS: per_RI, S0B0POS: E_RI, S0B0POSLemma: E_una, S0B0Token: per_una, S0B1Lemma: per_figura, S0B1LemmaPOS: per_S, S0B1POS: E_S, S0B1POSLemma: E_figura, S0B1Token: per_figura, S0Lemma: per, S0POS: E, S0Token: per, TransHistory3: 202, hasRighDep_prep: true, per_figura_hasRighDep_prep: true, per_hasRighDep_prep: true, 

24- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [una, figura, femminile ,.. ]

B0Lemma: una, B0POS: RI, B0Token: una, TransHistory3: 020, 

25- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [una]   B= [figura, femminile, tipica ,.. ]

B0Lemma: figura, B0POS: S, B0Token: figura, S0B0Lemma: una_figura, S0B0LemmaPOS: una_S, S0B0POS: RI_S, S0B0POSLemma: RI_figura, S0B0Token: una_figura, S0B1Lemma: una_femminile, S0B1LemmaPOS: una_A, S0B1POS: RI_A, S0B1POSLemma: RI_femminile, S0B1Token: una_femminile, S0Lemma: una, S0POS: RI, S0Token: una, TransHistory3: 202, una_isGouvernedBy_figura: true, una_isGouvernedBy_figura_det: true, 

26- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [figura, femminile, tipica ,.. ]

B0Lemma: figura, B0POS: S, B0Token: figura, TransHistory3: 020, 

27- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [figura]   B= [femminile, tipica, : ,.. ]

B0Lemma: femminile, B0POS: A, B0Token: femminile, S0B0Lemma: figura_femminile, S0B0LemmaPOS: figura_A, S0B0POS: S_A, S0B0POSLemma: S_femminile, S0B0Token: figura_femminile, S0B1Lemma: figura_tipico, S0B1LemmaPOS: figura_A, S0B1POS: S_A, S0B1POSLemma: S_tipico, S0B1Token: figura_tipica, S0Lemma: figura, S0POS: S, S0Token: figura, TransHistory3: 202, figura_femminile_hasRighDep_mod: true, figura_hasRighDep_mod: true, figura_tipico_hasRighDep_mod: true, hasRighDep_mod: true, 

28- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [femminile, tipica, : ,.. ]

B0Lemma: femminile, B0POS: A, B0Token: femminile, TransHistory3: 020, 

29- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [femminile]   B= [tipica, :, si ,.. ]

B0Lemma: tipico, B0POS: A, B0Token: tipica, S0B0Lemma: femminile_tipico, S0B0LemmaPOS: femminile_A, S0B0POS: A_A, S0B0POSLemma: A_tipico, S0B0Token: femminile_tipica, S0B1Lemma: femminile_:, S0B1LemmaPOS: femminile_FC, S0B1POS: A_FC, S0B1POSLemma: A_:, S0B1Token: femminile_:, S0Lemma: femminile, S0POS: A, S0Token: femminile, TransHistory3: 202, 

30- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [tipica, :, si ,.. ]

B0Lemma: tipico, B0POS: A, B0Token: tipica, TransHistory3: 020, 

31- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [tipica]   B= [:, si, tratta ,.. ]

B0Lemma: :, B0POS: FC, B0Token: :, S0B0Lemma: tipico_:, S0B0LemmaPOS: tipico_FC, S0B0POS: A_FC, S0B0POSLemma: A_:, S0B0Token: tipica_:, S0B1Lemma: tipico_si, S0B1LemmaPOS: tipico_PC, S0B1POS: A_PC, S0B1POSLemma: A_si, S0B1Token: tipica_si, S0Lemma: tipico, S0POS: A, S0Token: tipica, TransHistory3: 202, 

32- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [:, si, tratta ,.. ]

B0Lemma: :, B0POS: FC, B0Token: :, TransHistory3: 020, 

33- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [:]   B= [si, tratta, di ,.. ]

B0Lemma: si, B0POS: PC, B0Token: si, S0B0Lemma: :_si, S0B0LemmaPOS: :_PC, S0B0POS: FC_PC, S0B0POSLemma: FC_si, S0B0Token: :_si, S0B1Lemma: :_trattare, S0B1LemmaPOS: :_V, S0B1POS: FC_V, S0B1POSLemma: FC_trattare, S0B1Token: :_tratta, S0Lemma: :, S0POS: FC, S0Token: :, TransHistory3: 202, 

34- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [si, tratta, di ,.. ]

B0Lemma: si, B0POS: PC, B0Token: si, TransHistory3: 020, 

35- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [si]   B= [tratta, di, solito ,.. ]

B0Lemma: trattare, B0POS: V, B0Token: tratta, S0B0Lemma: si_trattare, S0B0LemmaPOS: si_V, S0B0POS: PC_V, S0B0POSLemma: PC_trattare, S0B0Token: si_tratta, S0B1Lemma: si_di, S0B1LemmaPOS: si_E, S0B1POS: PC_E, S0B1POSLemma: PC_di, S0B1Token: si_di, S0Lemma: si, S0POS: PC, S0Token: si, TransHistory3: 202, si_isGouvernedBy_trattare: true, si_isGouvernedBy_trattare_clit: true, 

36- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [si, tratta]   B= [di, solito, di ,.. ]

B0Lemma: di, B0POS: E, B0Token: di, S0B0Lemma: trattare_di, S0B0LemmaPOS: trattare_E, S0B0POS: V_E, S0B0POSLemma: V_di, S0B0Token: tratta_di, S0B1Lemma: trattare_solito, S0B1LemmaPOS: trattare_S, S0B1POS: V_S, S0B1POSLemma: V_solito, S0B1Token: tratta_solito, S0Lemma: trattare, S0POS: V, S0S1Distance: 1, S0Token: tratta, S1B0Lemma: si_di, S1B0LemmaPOS: si_E, S1B0POS: PC_E, S1B0POSLemma: PC_di, S1B0Token: si_di, S1Lemma: si, S1POS: PC, S1S0Lemma: si_trattare, S1S0LemmaPOS: si_V, S1S0POS: PC_V, S1S0POSLemma: PC_trattare, S1S0Token: si_tratta, S1Token: si, TransHistory3: 020, 

37- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[si, tratta]]   B= [di, solito, di ,.. ]

B0Lemma: di, B0POS: E, B0Token: di, S0B0Lemma: si_trattare_di, S0B0LemmaPOS: si_trattare_E, S0B0POS: PC_V_E, S0B0POSLemma: PC_V_di, S0B0Token: si_tratta_di, S0B1Lemma: si_trattare_solito, S0B1LemmaPOS: si_trattare_S, S0B1POS: PC_V_S, S0B1POSLemma: PC_V_solito, S0B1Token: si_tratta_solito, S0Lemma: si_trattare, S0POS: PC_V, S0Token: si_tratta, TransHistory3: 002, 

38- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [di, solito, di ,.. ]

B0Lemma: di, B0POS: E, B0Token: di, TransHistory3: 100, 

39- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [di]   B= [solito, di, una ,.. ]

B0Lemma: solito, B0POS: S, B0Token: solito, S0B0Lemma: di_solito, S0B0LemmaPOS: di_S, S0B0POS: E_S, S0B0POSLemma: E_solito, S0B0Token: di_solito, S0B1Lemma: di_di, S0B1LemmaPOS: di_E, S0B1POS: E_E, S0B1POSLemma: E_di, S0B1Token: di_di, S0Lemma: di, S0POS: E, S0Token: di, TransHistory3: 210, di_hasRighDep_prep: true, di_solito_hasRighDep_prep: true, hasRighDep_prep: true, 

40- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [solito, di, una ,.. ]

B0Lemma: solito, B0POS: S, B0Token: solito, TransHistory3: 021, 

41- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [solito]   B= [di, una, giovane ,.. ]

B0Lemma: di, B0POS: E, B0Token: di, S0B0Lemma: solito_di, S0B0LemmaPOS: solito_E, S0B0POS: S_E, S0B0POSLemma: S_di, S0B0Token: solito_di, S0B1Lemma: solito_una, S0B1LemmaPOS: solito_RI, S0B1POS: S_RI, S0B1POSLemma: S_una, S0B1Token: solito_una, S0Lemma: solito, S0POS: S, S0Token: solito, TransHistory3: 202, 

42- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [di, una, giovane ,.. ]

B0Lemma: di, B0POS: E, B0Token: di, TransHistory3: 020, 

43- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [di]   B= [una, giovane, donna ,.. ]

B0Lemma: una, B0POS: RI, B0Token: una, S0B0Lemma: di_una, S0B0LemmaPOS: di_RI, S0B0POS: E_RI, S0B0POSLemma: E_una, S0B0Token: di_una, S0B1Lemma: di_giovane, S0B1LemmaPOS: di_A, S0B1POS: E_A, S0B1POSLemma: E_giovane, S0B1Token: di_giovane, S0Lemma: di, S0POS: E, S0Token: di, TransHistory3: 202, di_donna_hasRighDep_prep: true, di_hasRighDep_prep: true, hasRighDep_prep: true, 

44- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [una, giovane, donna ,.. ]

B0Lemma: una, B0POS: RI, B0Token: una, TransHistory3: 020, 

45- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [una]   B= [giovane, donna, alta ,.. ]

B0Lemma: giovane, B0POS: A, B0Token: giovane, S0B0Lemma: una_giovane, S0B0LemmaPOS: una_A, S0B0POS: RI_A, S0B0POSLemma: RI_giovane, S0B0Token: una_giovane, S0B1Lemma: una_donna, S0B1LemmaPOS: una_S, S0B1POS: RI_S, S0B1POSLemma: RI_donna, S0B1Token: una_donna, S0Lemma: una, S0POS: RI, S0Token: una, TransHistory3: 202, una_isGouvernedBy_donna: true, una_isGouvernedBy_donna_det: true, 

46- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [giovane, donna, alta ,.. ]

B0Lemma: giovane, B0POS: A, B0Token: giovane, TransHistory3: 020, 

47- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [giovane]   B= [donna, alta, e ,.. ]

B0Lemma: donna, B0POS: S, B0Token: donna, S0B0Lemma: giovane_donna, S0B0LemmaPOS: giovane_S, S0B0POS: A_S, S0B0POSLemma: A_donna, S0B0Token: giovane_donna, S0B1Lemma: giovane_alto, S0B1LemmaPOS: giovane_A, S0B1POS: A_A, S0B1POSLemma: A_alto, S0B1Token: giovane_alta, S0Lemma: giovane, S0POS: A, S0Token: giovane, TransHistory3: 202, giovane_isGouvernedBy_donna: true, giovane_isGouvernedBy_donna_mod: true, 

48- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [donna, alta, e ,.. ]

B0Lemma: donna, B0POS: S, B0Token: donna, TransHistory3: 020, 

49- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [donna]   B= [alta, e, bionda ,.. ]

B0Lemma: alto, B0POS: A, B0Token: alta, S0B0Lemma: donna_alto, S0B0LemmaPOS: donna_A, S0B0POS: S_A, S0B0POSLemma: S_alto, S0B0Token: donna_alta, S0B1Lemma: donna_e, S0B1LemmaPOS: donna_CC, S0B1POS: S_CC, S0B1POSLemma: S_e, S0B1Token: donna_e, S0Lemma: donna, S0POS: S, S0Token: donna, TransHistory3: 202, donna_alto_hasRighDep_mod: true, donna_da_hasRighDep_comp: true, donna_hasRighDep_comp: true, donna_hasRighDep_mod: true, hasRighDep_comp: true, hasRighDep_mod: true, 

50- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [alta, e, bionda ,.. ]

B0Lemma: alto, B0POS: A, B0Token: alta, TransHistory3: 020, 

51- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [alta]   B= [e, bionda, , ,.. ]

B0Lemma: e, B0POS: CC, B0Token: e, S0B0Lemma: alto_e, S0B0LemmaPOS: alto_CC, S0B0POS: A_CC, S0B0POSLemma: A_e, S0B0Token: alta_e, S0B1Lemma: alto_biondo, S0B1LemmaPOS: alto_A, S0B1POS: A_A, S0B1POSLemma: A_biondo, S0B1Token: alta_bionda, S0Lemma: alto, S0POS: A, S0Token: alta, TransHistory3: 202, alto_biondo_hasRighDep_conj: true, alto_e_hasRighDep_con: true, alto_hasRighDep_con: true, alto_hasRighDep_conj: true, hasRighDep_con: true, hasRighDep_conj: true, 

52- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [e, bionda, , ,.. ]

B0Lemma: e, B0POS: CC, B0Token: e, TransHistory3: 020, 

53- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [e]   B= [bionda, ,, dai ,.. ]

B0Lemma: biondo, B0POS: A, B0Token: bionda, S0B0Lemma: e_biondo, S0B0LemmaPOS: e_A, S0B0POS: CC_A, S0B0POSLemma: CC_biondo, S0B0Token: e_bionda, S0B1Lemma: e_,, S0B1LemmaPOS: e_FF, S0B1POS: CC_FF, S0B1POSLemma: CC_,, S0B1Token: e_,, S0Lemma: e, S0POS: CC, S0Token: e, TransHistory3: 202, 

54- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [bionda, ,, dai ,.. ]

B0Lemma: biondo, B0POS: A, B0Token: bionda, TransHistory3: 020, 

55- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [bionda]   B= [,, dai, lineamenti ,.. ]

B0Lemma: ,, B0POS: FF, B0Token: ,, S0B0Lemma: biondo_,, S0B0LemmaPOS: biondo_FF, S0B0POS: A_FF, S0B0POSLemma: A_,, S0B0Token: bionda_,, S0B1Lemma: biondo_da, S0B1LemmaPOS: biondo_EA, S0B1POS: A_EA, S0B1POSLemma: A_da, S0B1Token: bionda_dai, S0Lemma: biondo, S0POS: A, S0Token: bionda, TransHistory3: 202, 

56- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, dai, lineamenti ,.. ]

B0Lemma: ,, B0POS: FF, B0Token: ,, TransHistory3: 020, 

57- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [dai, lineamenti, sottili ,.. ]

,_isGouvernedBy_da: true, ,_isGouvernedBy_da_punc: true, B0Lemma: da, B0POS: EA, B0Token: dai, S0B0Lemma: ,_da, S0B0LemmaPOS: ,_EA, S0B0POS: FF_EA, S0B0POSLemma: FF_da, S0B0Token: ,_dai, S0B1Lemma: ,_lineamento, S0B1LemmaPOS: ,_S, S0B1POS: FF_S, S0B1POSLemma: FF_lineamento, S0B1Token: ,_lineamenti, S0Lemma: ,, S0POS: FF, S0Token: ,, TransHistory3: 202, 

58- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [dai, lineamenti, sottili ,.. ]

B0Lemma: da, B0POS: EA, B0Token: dai, TransHistory3: 020, 

59- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [dai]   B= [lineamenti, sottili, e ,.. ]

B0Lemma: lineamento, B0POS: S, B0Token: lineamenti, S0B0Lemma: da_lineamento, S0B0LemmaPOS: da_S, S0B0POS: EA_S, S0B0POSLemma: EA_lineamento, S0B0Token: dai_lineamenti, S0B1Lemma: da_sottile, S0B1LemmaPOS: da_A, S0B1POS: EA_A, S0B1POSLemma: EA_sottile, S0B1Token: dai_sottili, S0Lemma: da, S0POS: EA, S0Token: dai, TransHistory3: 202, da_da_hasRighDep_conj: true, da_e_hasRighDep_con: true, da_hasRighDep_con: true, da_hasRighDep_conj: true, da_hasRighDep_prep: true, da_lineamento_hasRighDep_prep: true, hasRighDep_con: true, hasRighDep_conj: true, hasRighDep_prep: true, 

60- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [lineamenti, sottili, e ,.. ]

B0Lemma: lineamento, B0POS: S, B0Token: lineamenti, TransHistory3: 020, 

61- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [lineamenti]   B= [sottili, e, dall' ,.. ]

B0Lemma: sottile, B0POS: A, B0Token: sottili, S0B0Lemma: lineamento_sottile, S0B0LemmaPOS: lineamento_A, S0B0POS: S_A, S0B0POSLemma: S_sottile, S0B0Token: lineamenti_sottili, S0B1Lemma: lineamento_e, S0B1LemmaPOS: lineamento_CC, S0B1POS: S_CC, S0B1POSLemma: S_e, S0B1Token: lineamenti_e, S0Lemma: lineamento, S0POS: S, S0Token: lineamenti, TransHistory3: 202, hasRighDep_mod: true, lineamento_hasRighDep_mod: true, lineamento_sottile_hasRighDep_mod: true, 

62- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [sottili, e, dall' ,.. ]

B0Lemma: sottile, B0POS: A, B0Token: sottili, TransHistory3: 020, 

63- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [sottili]   B= [e, dall', aspetto ,.. ]

B0Lemma: e, B0POS: CC, B0Token: e, S0B0Lemma: sottile_e, S0B0LemmaPOS: sottile_CC, S0B0POS: A_CC, S0B0POSLemma: A_e, S0B0Token: sottili_e, S0B1Lemma: sottile_da, S0B1LemmaPOS: sottile_EA, S0B1POS: A_EA, S0B1POSLemma: A_da, S0B1Token: sottili_dall', S0Lemma: sottile, S0POS: A, S0Token: sottili, TransHistory3: 202, 

64- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [e, dall', aspetto ,.. ]

B0Lemma: e, B0POS: CC, B0Token: e, TransHistory3: 020, 

65- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [e]   B= [dall', aspetto, rassicurante ,.. ]

B0Lemma: da, B0POS: EA, B0Token: dall', S0B0Lemma: e_da, S0B0LemmaPOS: e_EA, S0B0POS: CC_EA, S0B0POSLemma: CC_da, S0B0Token: e_dall', S0B1Lemma: e_aspetto, S0B1LemmaPOS: e_S, S0B1POS: CC_S, S0B1POSLemma: CC_aspetto, S0B1Token: e_aspetto, S0Lemma: e, S0POS: CC, S0Token: e, TransHistory3: 202, 

66- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [dall', aspetto, rassicurante ,.. ]

B0Lemma: da, B0POS: EA, B0Token: dall', TransHistory3: 020, 

67- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [dall']   B= [aspetto, rassicurante, , ,.. ]

B0Lemma: aspetto, B0POS: S, B0Token: aspetto, S0B0Lemma: da_aspetto, S0B0LemmaPOS: da_S, S0B0POS: EA_S, S0B0POSLemma: EA_aspetto, S0B0Token: dall'_aspetto, S0B1Lemma: da_rassicurante, S0B1LemmaPOS: da_A, S0B1POS: EA_A, S0B1POSLemma: EA_rassicurante, S0B1Token: dall'_rassicurante, S0Lemma: da, S0POS: EA, S0Token: dall', TransHistory3: 202, da_aspetto_hasRighDep_prep: true, da_hasRighDep_prep: true, hasRighDep_prep: true, 

68- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [aspetto, rassicurante, , ,.. ]

B0Lemma: aspetto, B0POS: S, B0Token: aspetto, TransHistory3: 020, 

69- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [aspetto]   B= [rassicurante, ,, che ,.. ]

B0Lemma: rassicurante, B0POS: A, B0Token: rassicurante, S0B0Lemma: aspetto_rassicurante, S0B0LemmaPOS: aspetto_A, S0B0POS: S_A, S0B0POSLemma: S_rassicurante, S0B0Token: aspetto_rassicurante, S0B1Lemma: aspetto_,, S0B1LemmaPOS: aspetto_FF, S0B1POS: S_FF, S0B1POSLemma: S_,, S0B1Token: aspetto_,, S0Lemma: aspetto, S0POS: S, S0Token: aspetto, TransHistory3: 202, aspetto_,_hasRighDep_punc: true, aspetto_hasRighDep_mod: true, aspetto_hasRighDep_mod_rel: true, aspetto_hasRighDep_punc: true, aspetto_rassicurante_hasRighDep_mod: true, aspetto_rivelare_hasRighDep_mod_rel: true, hasRighDep_mod: true, hasRighDep_mod_rel: true, hasRighDep_punc: true, 

70- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [rassicurante, ,, che ,.. ]

B0Lemma: rassicurante, B0POS: A, B0Token: rassicurante, TransHistory3: 020, 

71- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [rassicurante]   B= [,, che, quasi ,.. ]

B0Lemma: ,, B0POS: FF, B0Token: ,, S0B0Lemma: rassicurante_,, S0B0LemmaPOS: rassicurante_FF, S0B0POS: A_FF, S0B0POSLemma: A_,, S0B0Token: rassicurante_,, S0B1Lemma: rassicurante_che, S0B1LemmaPOS: rassicurante_PR, S0B1POS: A_PR, S0B1POSLemma: A_che, S0B1Token: rassicurante_che, S0Lemma: rassicurante, S0POS: A, S0Token: rassicurante, TransHistory3: 202, 

72- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, che, quasi ,.. ]

B0Lemma: ,, B0POS: FF, B0Token: ,, TransHistory3: 020, 

73- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [che, quasi, sempre ,.. ]

B0Lemma: che, B0POS: PR, B0Token: che, S0B0Lemma: ,_che, S0B0LemmaPOS: ,_PR, S0B0POS: FF_PR, S0B0POSLemma: FF_che, S0B0Token: ,_che, S0B1Lemma: ,_quasi, S0B1LemmaPOS: ,_B, S0B1POS: FF_B, S0B1POSLemma: FF_quasi, S0B1Token: ,_quasi, S0Lemma: ,, S0POS: FF, S0Token: ,, TransHistory3: 202, 

74- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [che, quasi, sempre ,.. ]

B0Lemma: che, B0POS: PR, B0Token: che, TransHistory3: 020, 

75- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [che]   B= [quasi, sempre, si ,.. ]

B0Lemma: quasi, B0POS: B, B0Token: quasi, S0B0Lemma: che_quasi, S0B0LemmaPOS: che_B, S0B0POS: PR_B, S0B0POSLemma: PR_quasi, S0B0Token: che_quasi, S0B1Lemma: che_sempre, S0B1LemmaPOS: che_B, S0B1POS: PR_B, S0B1POSLemma: PR_sempre, S0B1Token: che_sempre, S0Lemma: che, S0POS: PR, S0Token: che, TransHistory3: 202, che_isGouvernedBy_rivelare: true, che_isGouvernedBy_rivelare_subj: true, 

76- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [quasi, sempre, si ,.. ]

B0Lemma: quasi, B0POS: B, B0Token: quasi, TransHistory3: 020, 

77- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [quasi]   B= [sempre, si, rivela ,.. ]

B0Lemma: sempre, B0POS: B, B0Token: sempre, S0B0Lemma: quasi_sempre, S0B0LemmaPOS: quasi_B, S0B0POS: B_B, S0B0POSLemma: B_sempre, S0B0Token: quasi_sempre, S0B1Lemma: quasi_si, S0B1LemmaPOS: quasi_PC, S0B1POS: B_PC, S0B1POSLemma: B_si, S0B1Token: quasi_si, S0Lemma: quasi, S0POS: B, S0Token: quasi, TransHistory3: 202, quasi_isGouvernedBy_sempre: true, quasi_isGouvernedBy_sempre_mod: true, 

78- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [sempre, si, rivela ,.. ]

B0Lemma: sempre, B0POS: B, B0Token: sempre, TransHistory3: 020, 

79- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [sempre]   B= [si, rivela, un ,.. ]

B0Lemma: si, B0POS: PC, B0Token: si, S0B0Lemma: sempre_si, S0B0LemmaPOS: sempre_PC, S0B0POS: B_PC, S0B0POSLemma: B_si, S0B0Token: sempre_si, S0B1Lemma: sempre_rivelare, S0B1LemmaPOS: sempre_V, S0B1POS: B_V, S0B1POSLemma: B_rivelare, S0B1Token: sempre_rivela, S0Lemma: sempre, S0POS: B, S0Token: sempre, TransHistory3: 202, sempre_isGouvernedBy_rivelare: true, sempre_isGouvernedBy_rivelare_mod: true, 

80- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [si, rivela, un ,.. ]

B0Lemma: si, B0POS: PC, B0Token: si, TransHistory3: 020, 

81- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [si]   B= [rivela, un, personaggio ,.. ]

B0Lemma: rivelare, B0POS: V, B0Token: rivela, S0B0Lemma: si_rivelare, S0B0LemmaPOS: si_V, S0B0POS: PC_V, S0B0POSLemma: PC_rivelare, S0B0Token: si_rivela, S0B1Lemma: si_un, S0B1LemmaPOS: si_RI, S0B1POS: PC_RI, S0B1POSLemma: PC_un, S0B1Token: si_un, S0Lemma: si, S0POS: PC, S0Token: si, TransHistory3: 202, si_isGouvernedBy_rivelare: true, si_isGouvernedBy_rivelare_clit: true, 

82- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [si, rivela]   B= [un, personaggio, ambiguo ,.. ]

B0Lemma: un, B0POS: RI, B0Token: un, S0B0Lemma: rivelare_un, S0B0LemmaPOS: rivelare_RI, S0B0POS: V_RI, S0B0POSLemma: V_un, S0B0Token: rivela_un, S0B1Lemma: rivelare_personaggio, S0B1LemmaPOS: rivelare_S, S0B1POS: V_S, S0B1POSLemma: V_personaggio, S0B1Token: rivela_personaggio, S0Lemma: rivelare, S0POS: V, S0S1Distance: 1, S0Token: rivela, S1B0Lemma: si_un, S1B0LemmaPOS: si_RI, S1B0POS: PC_RI, S1B0POSLemma: PC_un, S1B0Token: si_un, S1Lemma: si, S1POS: PC, S1S0Lemma: si_rivelare, S1S0LemmaPOS: si_V, S1S0POS: PC_V, S1S0POSLemma: PC_rivelare, S1S0Token: si_rivela, S1Token: si, SyntaxicRelation: -clit, TransHistory3: 020, hasRighDep_obj: true, rivelare_hasRighDep_obj: true, rivelare_personaggio_hasRighDep_obj: true, 

83- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[si, rivela]]   B= [un, personaggio, ambiguo ,.. ]

B0Lemma: un, B0POS: RI, B0Token: un, S0B0Lemma: si_rivelare_un, S0B0LemmaPOS: si_rivelare_RI, S0B0POS: PC_V_RI, S0B0POSLemma: PC_V_un, S0B0Token: si_rivela_un, S0B1Lemma: si_rivelare_personaggio, S0B1LemmaPOS: si_rivelare_S, S0B1POS: PC_V_S, S0B1POSLemma: PC_V_personaggio, S0B1Token: si_rivela_personaggio, S0Lemma: si_rivelare, S0POS: PC_V, S0Token: si_rivela, TransHistory3: 002, 

84- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [un, personaggio, ambiguo ,.. ]

B0Lemma: un, B0POS: RI, B0Token: un, TransHistory3: 100, 

85- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [un]   B= [personaggio, ambiguo, e ,.. ]

B0Lemma: personaggio, B0POS: S, B0Token: personaggio, S0B0Lemma: un_personaggio, S0B0LemmaPOS: un_S, S0B0POS: RI_S, S0B0POSLemma: RI_personaggio, S0B0Token: un_personaggio, S0B1Lemma: un_ambiguo, S0B1LemmaPOS: un_A, S0B1POS: RI_A, S0B1POSLemma: RI_ambiguo, S0B1Token: un_ambiguo, S0Lemma: un, S0POS: RI, S0Token: un, TransHistory3: 210, un_isGouvernedBy_personaggio: true, un_isGouvernedBy_personaggio_det: true, 

86- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [personaggio, ambiguo, e ,.. ]

B0Lemma: personaggio, B0POS: S, B0Token: personaggio, TransHistory3: 021, 

87- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [personaggio]   B= [ambiguo, e, malvagio ,.. ]

B0Lemma: ambiguo, B0POS: A, B0Token: ambiguo, S0B0Lemma: personaggio_ambiguo, S0B0LemmaPOS: personaggio_A, S0B0POS: S_A, S0B0POSLemma: S_ambiguo, S0B0Token: personaggio_ambiguo, S0B1Lemma: personaggio_e, S0B1LemmaPOS: personaggio_CC, S0B1POS: S_CC, S0B1POSLemma: S_e, S0B1Token: personaggio_e, S0Lemma: personaggio, S0POS: S, S0Token: personaggio, TransHistory3: 202, hasRighDep_conj: true, hasRighDep_mod: true, personaggio_Melanie_hasRighDep_conj: true, personaggio_ambiguo_hasRighDep_mod: true, personaggio_hasRighDep_conj: true, personaggio_hasRighDep_mod: true, 

88- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ambiguo, e, malvagio ,.. ]

B0Lemma: ambiguo, B0POS: A, B0Token: ambiguo, TransHistory3: 020, 

89- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ambiguo]   B= [e, malvagio, come ,.. ]

B0Lemma: e, B0POS: CC, B0Token: e, S0B0Lemma: ambiguo_e, S0B0LemmaPOS: ambiguo_CC, S0B0POS: A_CC, S0B0POSLemma: A_e, S0B0Token: ambiguo_e, S0B1Lemma: ambiguo_malvagio, S0B1LemmaPOS: ambiguo_A, S0B1POS: A_A, S0B1POSLemma: A_malvagio, S0B1Token: ambiguo_malvagio, S0Lemma: ambiguo, S0POS: A, S0Token: ambiguo, TransHistory3: 202, ambiguo_e_hasRighDep_con: true, ambiguo_hasRighDep_con: true, ambiguo_hasRighDep_conj: true, ambiguo_malvagio_hasRighDep_conj: true, hasRighDep_con: true, hasRighDep_conj: true, 

90- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [e, malvagio, come ,.. ]

B0Lemma: e, B0POS: CC, B0Token: e, TransHistory3: 020, 

91- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [e]   B= [malvagio, come, , ,.. ]

B0Lemma: malvagio, B0POS: A, B0Token: malvagio, S0B0Lemma: e_malvagio, S0B0LemmaPOS: e_A, S0B0POS: CC_A, S0B0POSLemma: CC_malvagio, S0B0Token: e_malvagio, S0B1Lemma: e_come, S0B1LemmaPOS: e_B, S0B1POS: CC_B, S0B1POSLemma: CC_come, S0B1Token: e_come, S0Lemma: e, S0POS: CC, S0Token: e, TransHistory3: 202, 

92- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [malvagio, come, , ,.. ]

B0Lemma: malvagio, B0POS: A, B0Token: malvagio, TransHistory3: 020, 

93- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [malvagio]   B= [come, ,, ad ,.. ]

B0Lemma: come, B0POS: B, B0Token: come, S0B0Lemma: malvagio_come, S0B0LemmaPOS: malvagio_B, S0B0POS: A_B, S0B0POSLemma: A_come, S0B0Token: malvagio_come, S0B1Lemma: malvagio_,, S0B1LemmaPOS: malvagio_FF, S0B1POS: A_FF, S0B1POSLemma: A_,, S0B1Token: malvagio_,, S0Lemma: malvagio, S0POS: A, S0Token: malvagio, TransHistory3: 202, hasRighDep_comp: true, hasRighDep_conj: true, malvagio_ad_hasRighDep_comp: true, malvagio_come_hasRighDep_conj: true, malvagio_hasRighDep_comp: true, malvagio_hasRighDep_conj: true, 

94- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [come, ,, ad ,.. ]

B0Lemma: come, B0POS: B, B0Token: come, TransHistory3: 020, 

95- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [come]   B= [,, ad, esempio ,.. ]

B0Lemma: ,, B0POS: FF, B0Token: ,, S0B0Lemma: come_,, S0B0LemmaPOS: come_FF, S0B0POS: B_FF, S0B0POSLemma: B_,, S0B0Token: come_,, S0B1Lemma: come_ad, S0B1LemmaPOS: come_E, S0B1POS: B_E, S0B1POSLemma: B_ad, S0B1Token: come_ad, S0Lemma: come, S0POS: B, S0Token: come, TransHistory3: 202, 

96- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, ad, esempio ,.. ]

B0Lemma: ,, B0POS: FF, B0Token: ,, TransHistory3: 020, 

97- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [ad, esempio, , ,.. ]

,_isGouvernedBy_ad: true, ,_isGouvernedBy_ad_punc: true, B0Lemma: ad, B0POS: E, B0Token: ad, S0B0Lemma: ,_ad, S0B0LemmaPOS: ,_E, S0B0POS: FF_E, S0B0POSLemma: FF_ad, S0B0Token: ,_ad, S0B1Lemma: ,_esempio, S0B1LemmaPOS: ,_S, S0B1POS: FF_S, S0B1POSLemma: FF_esempio, S0B1Token: ,_esempio, S0Lemma: ,, S0POS: FF, S0Token: ,, TransHistory3: 202, 

98- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ad, esempio, , ,.. ]

B0Lemma: ad, B0POS: E, B0Token: ad, TransHistory3: 020, 

99- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ad]   B= [esempio, ,, la ,.. ]

B0Lemma: esempio, B0POS: S, B0Token: esempio, S0B0Lemma: ad_esempio, S0B0LemmaPOS: ad_S, S0B0POS: E_S, S0B0POSLemma: E_esempio, S0B0Token: ad_esempio, S0B1Lemma: ad_,, S0B1LemmaPOS: ad_FF, S0B1POS: E_FF, S0B1POSLemma: E_,, S0B1Token: ad_,, S0Lemma: ad, S0POS: E, S0Token: ad, TransHistory3: 202, ad_,_hasRighDep_punc: true, ad_esempio_hasRighDep_prep: true, ad_hasRighDep_prep: true, ad_hasRighDep_punc: true, hasRighDep_prep: true, hasRighDep_punc: true, 

100- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [esempio, ,, la ,.. ]

B0Lemma: esempio, B0POS: S, B0Token: esempio, TransHistory3: 020, 

101- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [esempio]   B= [,, la, melanie ,.. ]

B0Lemma: ,, B0POS: FF, B0Token: ,, S0B0Lemma: esempio_,, S0B0LemmaPOS: esempio_FF, S0B0POS: S_FF, S0B0POSLemma: S_,, S0B0Token: esempio_,, S0B1Lemma: esempio_il, S0B1LemmaPOS: esempio_RD, S0B1POS: S_RD, S0B1POSLemma: S_il, S0B1Token: esempio_la, S0Lemma: esempio, S0POS: S, S0Token: esempio, TransHistory3: 202, 

102- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, la, melanie ,.. ]

B0Lemma: ,, B0POS: FF, B0Token: ,, TransHistory3: 020, 

103- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [la, melanie, daniels ,.. ]

B0Lemma: il, B0POS: RD, B0Token: la, S0B0Lemma: ,_il, S0B0LemmaPOS: ,_RD, S0B0POS: FF_RD, S0B0POSLemma: FF_il, S0B0Token: ,_la, S0B1Lemma: ,_Melanie, S0B1LemmaPOS: ,_SP, S0B1POS: FF_SP, S0B1POSLemma: FF_Melanie, S0B1Token: ,_melanie, S0Lemma: ,, S0POS: FF, S0Token: ,, TransHistory3: 202, 

104- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [la, melanie, daniels ,.. ]

B0Lemma: il, B0POS: RD, B0Token: la, TransHistory3: 020, 

105- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [la]   B= [melanie, daniels, de ,.. ]

B0Lemma: Melanie, B0POS: SP, B0Token: melanie, S0B0Lemma: il_Melanie, S0B0LemmaPOS: il_SP, S0B0POS: RD_SP, S0B0POSLemma: RD_Melanie, S0B0Token: la_melanie, S0B1Lemma: il_Daniels, S0B1LemmaPOS: il_SP, S0B1POS: RD_SP, S0B1POSLemma: RD_Daniels, S0B1Token: la_daniels, S0Lemma: il, S0POS: RD, S0Token: la, TransHistory3: 202, il_isGouvernedBy_Melanie: true, il_isGouvernedBy_Melanie_det: true, 

106- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [melanie, daniels, de ,.. ]

B0Lemma: Melanie, B0POS: SP, B0Token: melanie, TransHistory3: 020, 

107- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [melanie]   B= [daniels, de, " ,.. ]

B0Lemma: Daniels, B0POS: SP, B0Token: daniels, Melanie_Daniels_hasRighDep_mod: true, Melanie_Madeleine_hasRighDep_mod: true, Melanie_de_hasRighDep_mod: true, Melanie_hasRighDep_mod: true, Melanie_uccello_hasRighDep_mod: true, S0B0Lemma: Melanie_Daniels, S0B0LemmaPOS: Melanie_SP, S0B0POS: SP_SP, S0B0POSLemma: SP_Daniels, S0B0Token: melanie_daniels, S0B1Lemma: Melanie_de, S0B1LemmaPOS: Melanie_SW, S0B1POS: SP_SW, S0B1POSLemma: SP_de, S0B1Token: melanie_de, S0Lemma: Melanie, S0POS: SP, S0Token: melanie, TransHistory3: 202, hasRighDep_mod: true, 

108- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [daniels, de, " ,.. ]

B0Lemma: Daniels, B0POS: SP, B0Token: daniels, TransHistory3: 020, 

109- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [daniels]   B= [de, ", gli ,.. ]

B0Lemma: de, B0POS: SW, B0Token: de, S0B0Lemma: Daniels_de, S0B0LemmaPOS: Daniels_SW, S0B0POS: SP_SW, S0B0POSLemma: SP_de, S0B0Token: daniels_de, S0B1Lemma: Daniels_", S0B1LemmaPOS: Daniels_FB, S0B1POS: SP_FB, S0B1POSLemma: SP_", S0B1Token: daniels_", S0Lemma: Daniels, S0POS: SP, S0Token: daniels, TransHistory3: 202, 

110- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [de, ", gli ,.. ]

B0Lemma: de, B0POS: SW, B0Token: de, TransHistory3: 020, 

111- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [de]   B= [", gli, uccelli ,.. ]

B0Lemma: ", B0POS: FB, B0Token: ", S0B0Lemma: de_", S0B0LemmaPOS: de_FB, S0B0POS: SW_FB, S0B0POSLemma: SW_", S0B0Token: de_", S0B1Lemma: de_il, S0B1LemmaPOS: de_RD, S0B1POS: SW_RD, S0B1POSLemma: SW_il, S0B1Token: de_gli, S0Lemma: de, S0POS: SW, S0Token: de, TransHistory3: 202, 

112- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [", gli, uccelli ,.. ]

B0Lemma: ", B0POS: FB, B0Token: ", TransHistory3: 020, 

113- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= ["]   B= [gli, uccelli, " ,.. ]

"_isGouvernedBy_uccello: true, "_isGouvernedBy_uccello_punc: true, B0Lemma: il, B0POS: RD, B0Token: gli, S0B0Lemma: "_il, S0B0LemmaPOS: "_RD, S0B0POS: FB_RD, S0B0POSLemma: FB_il, S0B0Token: "_gli, S0B1Lemma: "_uccello, S0B1LemmaPOS: "_S, S0B1POS: FB_S, S0B1POSLemma: FB_uccello, S0B1Token: "_uccelli, S0Lemma: ", S0POS: FB, S0Token: ", TransHistory3: 202, 

114- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [gli, uccelli, " ,.. ]

B0Lemma: il, B0POS: RD, B0Token: gli, TransHistory3: 020, 

115- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [gli]   B= [uccelli, ", o ,.. ]

B0Lemma: uccello, B0POS: S, B0Token: uccelli, S0B0Lemma: il_uccello, S0B0LemmaPOS: il_S, S0B0POS: RD_S, S0B0POSLemma: RD_uccello, S0B0Token: gli_uccelli, S0B1Lemma: il_", S0B1LemmaPOS: il_FB, S0B1POS: RD_FB, S0B1POSLemma: RD_", S0B1Token: gli_", S0Lemma: il, S0POS: RD, S0Token: gli, TransHistory3: 202, il_isGouvernedBy_uccello: true, il_isGouvernedBy_uccello_det: true, 

116- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [uccelli, ", o ,.. ]

B0Lemma: uccello, B0POS: S, B0Token: uccelli, TransHistory3: 020, 

117- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [uccelli]   B= [", o, la ,.. ]

B0Lemma: ", B0POS: FB, B0Token: ", S0B0Lemma: uccello_", S0B0LemmaPOS: uccello_FB, S0B0POS: S_FB, S0B0POSLemma: S_", S0B0Token: uccelli_", S0B1Lemma: uccello_o, S0B1LemmaPOS: uccello_CC, S0B1POS: S_CC, S0B1POSLemma: S_o, S0B1Token: uccelli_o, S0Lemma: uccello, S0POS: S, S0Token: uccelli, TransHistory3: 202, hasRighDep_dis: true, uccello_hasRighDep_dis: true, uccello_o_hasRighDep_dis: true, 

118- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [", o, la ,.. ]

B0Lemma: ", B0POS: FB, B0Token: ", TransHistory3: 020, 

119- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= ["]   B= [o, la, madeleine ,.. ]

"_isGouvernedBy_o: true, "_isGouvernedBy_o_punc: true, B0Lemma: o, B0POS: CC, B0Token: o, S0B0Lemma: "_o, S0B0LemmaPOS: "_CC, S0B0POS: FB_CC, S0B0POSLemma: FB_o, S0B0Token: "_o, S0B1Lemma: "_il, S0B1LemmaPOS: "_RD, S0B1POS: FB_RD, S0B1POSLemma: FB_il, S0B1Token: "_la, S0Lemma: ", S0POS: FB, S0Token: ", TransHistory3: 202, 

120- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [o, la, madeleine ,.. ]

B0Lemma: o, B0POS: CC, B0Token: o, TransHistory3: 020, 

121- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [o]   B= [la, madeleine, de ,.. ]

B0Lemma: il, B0POS: RD, B0Token: la, S0B0Lemma: o_il, S0B0LemmaPOS: o_RD, S0B0POS: CC_RD, S0B0POSLemma: CC_il, S0B0Token: o_la, S0B1Lemma: o_Madeleine, S0B1LemmaPOS: o_SP, S0B1POS: CC_SP, S0B1POSLemma: CC_Madeleine, S0B1Token: o_madeleine, S0Lemma: o, S0POS: CC, S0Token: o, TransHistory3: 202, 

122- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [la, madeleine, de ,.. ]

B0Lemma: il, B0POS: RD, B0Token: la, TransHistory3: 020, 

123- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [la]   B= [madeleine, de, " ,.. ]

B0Lemma: Madeleine, B0POS: SP, B0Token: madeleine, S0B0Lemma: il_Madeleine, S0B0LemmaPOS: il_SP, S0B0POS: RD_SP, S0B0POSLemma: RD_Madeleine, S0B0Token: la_madeleine, S0B1Lemma: il_de, S0B1LemmaPOS: il_SW, S0B1POS: RD_SW, S0B1POSLemma: RD_de, S0B1Token: la_de, S0Lemma: il, S0POS: RD, S0Token: la, TransHistory3: 202, il_isGouvernedBy_Madeleine: true, il_isGouvernedBy_Madeleine_det: true, 

124- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [madeleine, de, " ,.. ]

B0Lemma: Madeleine, B0POS: SP, B0Token: madeleine, TransHistory3: 020, 

125- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [madeleine]   B= [de, ", la ,.. ]

B0Lemma: de, B0POS: SW, B0Token: de, Madeleine_de_hasRighDep_mod: true, Madeleine_donna_hasRighDep_mod: true, Madeleine_hasRighDep_mod: true, S0B0Lemma: Madeleine_de, S0B0LemmaPOS: Madeleine_SW, S0B0POS: SP_SW, S0B0POSLemma: SP_de, S0B0Token: madeleine_de, S0B1Lemma: Madeleine_", S0B1LemmaPOS: Madeleine_FB, S0B1POS: SP_FB, S0B1POSLemma: SP_", S0B1Token: madeleine_", S0Lemma: Madeleine, S0POS: SP, S0Token: madeleine, TransHistory3: 202, hasRighDep_mod: true, 

126- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [de, ", la ,.. ]

B0Lemma: de, B0POS: SW, B0Token: de, TransHistory3: 020, 

127- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [de]   B= [", la, donna ,.. ]

B0Lemma: ", B0POS: FB, B0Token: ", S0B0Lemma: de_", S0B0LemmaPOS: de_FB, S0B0POS: SW_FB, S0B0POSLemma: SW_", S0B0Token: de_", S0B1Lemma: de_il, S0B1LemmaPOS: de_RD, S0B1POS: SW_RD, S0B1POSLemma: SW_il, S0B1Token: de_la, S0Lemma: de, S0POS: SW, S0Token: de, TransHistory3: 202, 

128- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [", la, donna ,.. ]

B0Lemma: ", B0POS: FB, B0Token: ", TransHistory3: 020, 

129- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= ["]   B= [la, donna, che ,.. ]

"_isGouvernedBy_il: true, "_isGouvernedBy_il_punc: true, B0Lemma: il, B0POS: RD, B0Token: la, S0B0Lemma: "_il, S0B0LemmaPOS: "_RD, S0B0POS: FB_RD, S0B0POSLemma: FB_il, S0B0Token: "_la, S0B1Lemma: "_donna, S0B1LemmaPOS: "_S, S0B1POS: FB_S, S0B1POSLemma: FB_donna, S0B1Token: "_donna, S0Lemma: ", S0POS: FB, S0Token: ", TransHistory3: 202, 

130- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [la, donna, che ,.. ]

B0Lemma: il, B0POS: RD, B0Token: la, TransHistory3: 020, 

131- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [la]   B= [donna, che, visse ,.. ]

B0Lemma: donna, B0POS: S, B0Token: donna, S0B0Lemma: il_donna, S0B0LemmaPOS: il_S, S0B0POS: RD_S, S0B0POSLemma: RD_donna, S0B0Token: la_donna, S0B1Lemma: il_che, S0B1LemmaPOS: il_PR, S0B1POS: RD_PR, S0B1POSLemma: RD_che, S0B1Token: la_che, S0Lemma: il, S0POS: RD, S0Token: la, TransHistory3: 202, il_isGouvernedBy_donna: true, il_isGouvernedBy_donna_det: true, 

132- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [donna, che, visse ,.. ]

B0Lemma: donna, B0POS: S, B0Token: donna, TransHistory3: 020, 

133- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [donna]   B= [che, visse, due ,.. ]

B0Lemma: che, B0POS: PR, B0Token: che, S0B0Lemma: donna_che, S0B0LemmaPOS: donna_PR, S0B0POS: S_PR, S0B0POSLemma: S_che, S0B0Token: donna_che, S0B1Lemma: donna_vivere, S0B1LemmaPOS: donna_V, S0B1POS: S_V, S0B1POSLemma: S_vivere, S0B1Token: donna_visse, S0Lemma: donna, S0POS: S, S0Token: donna, TransHistory3: 202, donna_hasRighDep_mod_rel: true, donna_vivere_hasRighDep_mod_rel: true, hasRighDep_mod_rel: true, 

134- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [che, visse, due ,.. ]

B0Lemma: che, B0POS: PR, B0Token: che, TransHistory3: 020, 

135- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [che]   B= [visse, due, volte ,.. ]

B0Lemma: vivere, B0POS: V, B0Token: visse, S0B0Lemma: che_vivere, S0B0LemmaPOS: che_V, S0B0POS: PR_V, S0B0POSLemma: PR_vivere, S0B0Token: che_visse, S0B1Lemma: che_due, S0B1LemmaPOS: che_N, S0B1POS: PR_N, S0B1POSLemma: PR_due, S0B1Token: che_due, S0Lemma: che, S0POS: PR, S0Token: che, TransHistory3: 202, che_isGouvernedBy_vivere: true, che_isGouvernedBy_vivere_subj: true, 

136- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [visse, due, volte ,.. ]

B0Lemma: vivere, B0POS: V, B0Token: visse, TransHistory3: 020, 

137- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [visse]   B= [due, volte, " ,.. ]

B0Lemma: due, B0POS: N, B0Token: due, S0B0Lemma: vivere_due, S0B0LemmaPOS: vivere_N, S0B0POS: V_N, S0B0POSLemma: V_due, S0B0Token: visse_due, S0B1Lemma: vivere_volta, S0B1LemmaPOS: vivere_S, S0B1POS: V_S, S0B1POSLemma: V_volta, S0B1Token: visse_volte, S0Lemma: vivere, S0POS: V, S0Token: visse, TransHistory3: 202, hasRighDep_mod: true, vivere_hasRighDep_mod: true, vivere_volta_hasRighDep_mod: true, 

138- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [due, volte, " ,.. ]

B0Lemma: due, B0POS: N, B0Token: due, TransHistory3: 020, 

139- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [due]   B= [volte, ", . ,.. ]

B0Lemma: volta, B0POS: S, B0Token: volte, S0B0Lemma: due_volta, S0B0LemmaPOS: due_S, S0B0POS: N_S, S0B0POSLemma: N_volta, S0B0Token: due_volte, S0B1Lemma: due_", S0B1LemmaPOS: due_FB, S0B1POS: N_FB, S0B1POSLemma: N_", S0B1Token: due_", S0Lemma: due, S0POS: N, S0Token: due, TransHistory3: 202, due_isGouvernedBy_volta: true, due_isGouvernedBy_volta_mod: true, 

140- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [volte, ", . ,.. ]

B0Lemma: volta, B0POS: S, B0Token: volte, TransHistory3: 020, 

141- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [volte]   B= [", . ,.. ]

B0Lemma: ", B0POS: FB, B0Token: ", S0B0Lemma: volta_", S0B0LemmaPOS: volta_FB, S0B0POS: S_FB, S0B0POSLemma: S_", S0B0Token: volte_", S0B1Lemma: volta_., S0B1LemmaPOS: volta_FS, S0B1POS: S_FS, S0B1POSLemma: S_., S0B1Token: volte_., S0Lemma: volta, S0POS: S, S0Token: volte, TransHistory3: 202, hasRighDep_punc: true, volta_"_hasRighDep_punc: true, volta_hasRighDep_punc: true, 

142- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [", . ,.. ]

B0Lemma: ", B0POS: FB, B0Token: ", TransHistory3: 020, 

143- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= ["]   B= [.]

B0Lemma: ., B0POS: FS, B0Token: ., S0B0Lemma: "_., S0B0LemmaPOS: "_FS, S0B0POS: FB_FS, S0B0POSLemma: FB_., S0B0Token: "_., S0Lemma: ", S0POS: FB, S0Token: ", TransHistory3: 202, 

144- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [.]

B0Lemma: ., B0POS: FS, B0Token: ., TransHistory3: 020, 

145- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [ ]

S0Lemma: ., S0POS: FS, S0Token: ., TransHistory3: 202, 

146- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

## Sentence No. 203 - 
il sistema agronomico attuale è arrivato ad un livello di insopportabile illogicità essendo diventato , ormai da troppo tempo , tecnicamente assurdo e socialmente disonesto , tale da avere prodotto presso di noi un forte disagio esistenziale e la fame coatta presso altri ; il sistema industriale , da parte sua , ha deluso le aspettative con produzioni e metodi che hanno tradito le leggi fondamentali del pianeta : metodi e produzioni che sono stati trasferiti all' agricoltura spesso senza necessità e che hanno creato nella società un altrettanto forte disagio che è sotto gli occhi di tutti il quale , se colpisce nell' immediato soprattutto quelli che appartengono alle classi sociali inferiori , nasce dall' avere messo in dubbio , nello stesso tempo , la vita del pianeta ed il futuro di tutta l' umanità . 
### Existing MWEs: 
1- **tradito leggi** (ID)
2- **messo in dubbio** (ID)



0- &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [il, sistema, agronomico ,.. ]

B0Lemma: il, B0POS: RD, B0Token: il, 

1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [il]   B= [sistema, agronomico, attuale ,.. ]

B0Lemma: sistema, B0POS: S, B0Token: sistema, S0B0Lemma: il_sistema, S0B0LemmaPOS: il_S, S0B0POS: RD_S, S0B0POSLemma: RD_sistema, S0B0Token: il_sistema, S0B1Lemma: il_agronomico, S0B1LemmaPOS: il_A, S0B1POS: RD_A, S0B1POSLemma: RD_agronomico, S0B1Token: il_agronomico, S0Lemma: il, S0POS: RD, S0Token: il, il_isGouvernedBy_sistema: true, il_isGouvernedBy_sistema_det: true, 

2- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [sistema, agronomico, attuale ,.. ]

B0Lemma: sistema, B0POS: S, B0Token: sistema, 

3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [sistema]   B= [agronomico, attuale, è ,.. ]

B0Lemma: agronomico, B0POS: A, B0Token: agronomico, S0B0Lemma: sistema_agronomico, S0B0LemmaPOS: sistema_A, S0B0POS: S_A, S0B0POSLemma: S_agronomico, S0B0Token: sistema_agronomico, S0B1Lemma: sistema_attuale, S0B1LemmaPOS: sistema_A, S0B1POS: S_A, S0B1POSLemma: S_attuale, S0B1Token: sistema_attuale, S0Lemma: sistema, S0POS: S, S0Token: sistema, hasRighDep_mod: true, sistema_agronomico_hasRighDep_mod: true, sistema_attuale_hasRighDep_mod: true, sistema_hasRighDep_mod: true, sistema_isGouvernedBy_arrivare: true, sistema_isGouvernedBy_arrivare_subj: true, 

4- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [agronomico, attuale, è ,.. ]

B0Lemma: agronomico, B0POS: A, B0Token: agronomico, TransHistory3: 020, 

5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [agronomico]   B= [attuale, è, arrivato ,.. ]

B0Lemma: attuale, B0POS: A, B0Token: attuale, S0B0Lemma: agronomico_attuale, S0B0LemmaPOS: agronomico_A, S0B0POS: A_A, S0B0POSLemma: A_attuale, S0B0Token: agronomico_attuale, S0B1Lemma: agronomico_essere, S0B1LemmaPOS: agronomico_VA, S0B1POS: A_VA, S0B1POSLemma: A_essere, S0B1Token: agronomico_è, S0Lemma: agronomico, S0POS: A, S0Token: agronomico, TransHistory3: 202, 

6- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [attuale, è, arrivato ,.. ]

B0Lemma: attuale, B0POS: A, B0Token: attuale, TransHistory3: 020, 

7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [attuale]   B= [è, arrivato, ad ,.. ]

B0Lemma: essere, B0POS: VA, B0Token: è, S0B0Lemma: attuale_essere, S0B0LemmaPOS: attuale_VA, S0B0POS: A_VA, S0B0POSLemma: A_essere, S0B0Token: attuale_è, S0B1Lemma: attuale_arrivare, S0B1LemmaPOS: attuale_V, S0B1POS: A_V, S0B1POSLemma: A_arrivare, S0B1Token: attuale_arrivato, S0Lemma: attuale, S0POS: A, S0Token: attuale, TransHistory3: 202, 

8- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [è, arrivato, ad ,.. ]

B0Lemma: essere, B0POS: VA, B0Token: è, TransHistory3: 020, 

9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [è]   B= [arrivato, ad, un ,.. ]

B0Lemma: arrivare, B0POS: V, B0Token: arrivato, S0B0Lemma: essere_arrivare, S0B0LemmaPOS: essere_V, S0B0POS: VA_V, S0B0POSLemma: VA_arrivare, S0B0Token: è_arrivato, S0B1Lemma: essere_ad, S0B1LemmaPOS: essere_E, S0B1POS: VA_E, S0B1POSLemma: VA_ad, S0B1Token: è_ad, S0Lemma: essere, S0POS: VA, S0Token: è, TransHistory3: 202, essere_isGouvernedBy_arrivare: true, essere_isGouvernedBy_arrivare_aux: true, 

10- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [arrivato, ad, un ,.. ]

B0Lemma: arrivare, B0POS: V, B0Token: arrivato, TransHistory3: 020, 

11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [arrivato]   B= [ad, un, livello ,.. ]

B0Lemma: ad, B0POS: E, B0Token: ad, S0B0Lemma: arrivare_ad, S0B0LemmaPOS: arrivare_E, S0B0POS: V_E, S0B0POSLemma: V_ad, S0B0Token: arrivato_ad, S0B1Lemma: arrivare_un, S0B1LemmaPOS: arrivare_RI, S0B1POS: V_RI, S0B1POSLemma: V_un, S0B1Token: arrivato_un, S0Lemma: arrivare, S0POS: V, S0Token: arrivato, TransHistory3: 202, 

12- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ad, un, livello ,.. ]

B0Lemma: ad, B0POS: E, B0Token: ad, TransHistory3: 020, 

13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ad]   B= [un, livello, di ,.. ]

B0Lemma: un, B0POS: RI, B0Token: un, S0B0Lemma: ad_un, S0B0LemmaPOS: ad_RI, S0B0POS: E_RI, S0B0POSLemma: E_un, S0B0Token: ad_un, S0B1Lemma: ad_livello, S0B1LemmaPOS: ad_S, S0B1POS: E_S, S0B1POSLemma: E_livello, S0B1Token: ad_livello, S0Lemma: ad, S0POS: E, S0Token: ad, TransHistory3: 202, ad_hasRighDep_prep: true, ad_livello_hasRighDep_prep: true, hasRighDep_prep: true, 

14- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [un, livello, di ,.. ]

B0Lemma: un, B0POS: RI, B0Token: un, TransHistory3: 020, 

15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [un]   B= [livello, di, insopportabile ,.. ]

B0Lemma: livello, B0POS: S, B0Token: livello, S0B0Lemma: un_livello, S0B0LemmaPOS: un_S, S0B0POS: RI_S, S0B0POSLemma: RI_livello, S0B0Token: un_livello, S0B1Lemma: un_di, S0B1LemmaPOS: un_E, S0B1POS: RI_E, S0B1POSLemma: RI_di, S0B1Token: un_di, S0Lemma: un, S0POS: RI, S0Token: un, TransHistory3: 202, un_isGouvernedBy_livello: true, un_isGouvernedBy_livello_det: true, 

16- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [livello, di, insopportabile ,.. ]

B0Lemma: livello, B0POS: S, B0Token: livello, TransHistory3: 020, 

17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [livello]   B= [di, insopportabile, illogicità ,.. ]

B0Lemma: di, B0POS: E, B0Token: di, S0B0Lemma: livello_di, S0B0LemmaPOS: livello_E, S0B0POS: S_E, S0B0POSLemma: S_di, S0B0Token: livello_di, S0B1Lemma: livello_insopportabile, S0B1LemmaPOS: livello_A, S0B1POS: S_A, S0B1POSLemma: S_insopportabile, S0B1Token: livello_insopportabile, S0Lemma: livello, S0POS: S, S0Token: livello, TransHistory3: 202, hasRighDep_comp: true, livello_di_hasRighDep_comp: true, livello_hasRighDep_comp: true, 

18- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [di, insopportabile, illogicità ,.. ]

B0Lemma: di, B0POS: E, B0Token: di, TransHistory3: 020, 

19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [di]   B= [insopportabile, illogicità, essendo ,.. ]

B0Lemma: insopportabile, B0POS: A, B0Token: insopportabile, S0B0Lemma: di_insopportabile, S0B0LemmaPOS: di_A, S0B0POS: E_A, S0B0POSLemma: E_insopportabile, S0B0Token: di_insopportabile, S0B1Lemma: di_illogicità, S0B1LemmaPOS: di_S, S0B1POS: E_S, S0B1POSLemma: E_illogicità, S0B1Token: di_illogicità, S0Lemma: di, S0POS: E, S0Token: di, TransHistory3: 202, di_hasRighDep_prep: true, di_illogicità_hasRighDep_prep: true, hasRighDep_prep: true, 

20- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [insopportabile, illogicità, essendo ,.. ]

B0Lemma: insopportabile, B0POS: A, B0Token: insopportabile, TransHistory3: 020, 

21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [insopportabile]   B= [illogicità, essendo, diventato ,.. ]

B0Lemma: illogicità, B0POS: S, B0Token: illogicità, S0B0Lemma: insopportabile_illogicità, S0B0LemmaPOS: insopportabile_S, S0B0POS: A_S, S0B0POSLemma: A_illogicità, S0B0Token: insopportabile_illogicità, S0B1Lemma: insopportabile_essere, S0B1LemmaPOS: insopportabile_V, S0B1POS: A_V, S0B1POSLemma: A_essere, S0B1Token: insopportabile_essendo, S0Lemma: insopportabile, S0POS: A, S0Token: insopportabile, TransHistory3: 202, insopportabile_isGouvernedBy_illogicità: true, insopportabile_isGouvernedBy_illogicità_mod: true, 

22- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [illogicità, essendo, diventato ,.. ]

B0Lemma: illogicità, B0POS: S, B0Token: illogicità, TransHistory3: 020, 

23- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [illogicità]   B= [essendo, diventato, , ,.. ]

B0Lemma: essere, B0POS: V, B0Token: essendo, S0B0Lemma: illogicità_essere, S0B0LemmaPOS: illogicità_V, S0B0POS: S_V, S0B0POSLemma: S_essere, S0B0Token: illogicità_essendo, S0B1Lemma: illogicità_diventare, S0B1LemmaPOS: illogicità_V, S0B1POS: S_V, S0B1POSLemma: S_diventare, S0B1Token: illogicità_diventato, S0Lemma: illogicità, S0POS: S, S0Token: illogicità, TransHistory3: 202, 

24- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [essendo, diventato, , ,.. ]

B0Lemma: essere, B0POS: V, B0Token: essendo, TransHistory3: 020, 

25- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [essendo]   B= [diventato, ,, ormai ,.. ]

B0Lemma: diventare, B0POS: V, B0Token: diventato, S0B0Lemma: essere_diventare, S0B0LemmaPOS: essere_V, S0B0POS: V_V, S0B0POSLemma: V_diventare, S0B0Token: essendo_diventato, S0B1Lemma: essere_,, S0B1LemmaPOS: essere_FF, S0B1POS: V_FF, S0B1POSLemma: V_,, S0B1Token: essendo_,, S0Lemma: essere, S0POS: V, S0Token: essendo, TransHistory3: 202, essere_diventare_hasRighDep_pred: true, essere_hasRighDep_pred: true, hasRighDep_pred: true, 

26- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [diventato, ,, ormai ,.. ]

B0Lemma: diventare, B0POS: V, B0Token: diventato, TransHistory3: 020, 

27- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [diventato]   B= [,, ormai, da ,.. ]

B0Lemma: ,, B0POS: FF, B0Token: ,, S0B0Lemma: diventare_,, S0B0LemmaPOS: diventare_FF, S0B0POS: V_FF, S0B0POSLemma: V_,, S0B0Token: diventato_,, S0B1Lemma: diventare_ormai, S0B1LemmaPOS: diventare_B, S0B1POS: V_B, S0B1POSLemma: V_ormai, S0B1Token: diventato_ormai, S0Lemma: diventare, S0POS: V, S0Token: diventato, TransHistory3: 202, diventare_,_hasRighDep_con: true, diventare_da_hasRighDep_comp: true, diventare_hasRighDep_comp: true, diventare_hasRighDep_con: true, diventare_hasRighDep_mod: true, diventare_ormai_hasRighDep_mod: true, hasRighDep_comp: true, hasRighDep_con: true, hasRighDep_mod: true, 

28- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, ormai, da ,.. ]

B0Lemma: ,, B0POS: FF, B0Token: ,, TransHistory3: 020, 

29- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [ormai, da, troppo ,.. ]

B0Lemma: ormai, B0POS: B, B0Token: ormai, S0B0Lemma: ,_ormai, S0B0LemmaPOS: ,_B, S0B0POS: FF_B, S0B0POSLemma: FF_ormai, S0B0Token: ,_ormai, S0B1Lemma: ,_da, S0B1LemmaPOS: ,_E, S0B1POS: FF_E, S0B1POSLemma: FF_da, S0B1Token: ,_da, S0Lemma: ,, S0POS: FF, S0Token: ,, TransHistory3: 202, 

30- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ormai, da, troppo ,.. ]

B0Lemma: ormai, B0POS: B, B0Token: ormai, TransHistory3: 020, 

31- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ormai]   B= [da, troppo, tempo ,.. ]

B0Lemma: da, B0POS: E, B0Token: da, S0B0Lemma: ormai_da, S0B0LemmaPOS: ormai_E, S0B0POS: B_E, S0B0POSLemma: B_da, S0B0Token: ormai_da, S0B1Lemma: ormai_troppo, S0B1LemmaPOS: ormai_DI, S0B1POS: B_DI, S0B1POSLemma: B_troppo, S0B1Token: ormai_troppo, S0Lemma: ormai, S0POS: B, S0Token: ormai, TransHistory3: 202, 

32- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [da, troppo, tempo ,.. ]

B0Lemma: da, B0POS: E, B0Token: da, TransHistory3: 020, 

33- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [da]   B= [troppo, tempo, , ,.. ]

B0Lemma: troppo, B0POS: DI, B0Token: troppo, S0B0Lemma: da_troppo, S0B0LemmaPOS: da_DI, S0B0POS: E_DI, S0B0POSLemma: E_troppo, S0B0Token: da_troppo, S0B1Lemma: da_tempo, S0B1LemmaPOS: da_S, S0B1POS: E_S, S0B1POSLemma: E_tempo, S0B1Token: da_tempo, S0Lemma: da, S0POS: E, S0Token: da, TransHistory3: 202, da_hasRighDep_prep: true, da_tempo_hasRighDep_prep: true, hasRighDep_prep: true, 

34- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [troppo, tempo, , ,.. ]

B0Lemma: troppo, B0POS: DI, B0Token: troppo, TransHistory3: 020, 

35- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [troppo]   B= [tempo, ,, tecnicamente ,.. ]

B0Lemma: tempo, B0POS: S, B0Token: tempo, S0B0Lemma: troppo_tempo, S0B0LemmaPOS: troppo_S, S0B0POS: DI_S, S0B0POSLemma: DI_tempo, S0B0Token: troppo_tempo, S0B1Lemma: troppo_,, S0B1LemmaPOS: troppo_FF, S0B1POS: DI_FF, S0B1POSLemma: DI_,, S0B1Token: troppo_,, S0Lemma: troppo, S0POS: DI, S0Token: troppo, TransHistory3: 202, troppo_isGouvernedBy_tempo: true, troppo_isGouvernedBy_tempo_mod: true, 

36- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [tempo, ,, tecnicamente ,.. ]

B0Lemma: tempo, B0POS: S, B0Token: tempo, TransHistory3: 020, 

37- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [tempo]   B= [,, tecnicamente, assurdo ,.. ]

B0Lemma: ,, B0POS: FF, B0Token: ,, S0B0Lemma: tempo_,, S0B0LemmaPOS: tempo_FF, S0B0POS: S_FF, S0B0POSLemma: S_,, S0B0Token: tempo_,, S0B1Lemma: tempo_tecnico, S0B1LemmaPOS: tempo_B, S0B1POS: S_B, S0B1POSLemma: S_tecnico, S0B1Token: tempo_tecnicamente, S0Lemma: tempo, S0POS: S, S0Token: tempo, TransHistory3: 202, hasRighDep_con: true, hasRighDep_mod: true, hasRighDep_punc: true, tempo_,_hasRighDep_con: true, tempo_,_hasRighDep_punc: true, tempo_assurdo_hasRighDep_mod: true, tempo_disonesto_hasRighDep_mod: true, tempo_e_hasRighDep_con: true, tempo_hasRighDep_con: true, tempo_hasRighDep_mod: true, tempo_hasRighDep_punc: true, tempo_tale_hasRighDep_mod: true, 

38- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, tecnicamente, assurdo ,.. ]

B0Lemma: ,, B0POS: FF, B0Token: ,, TransHistory3: 020, 

39- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [tecnicamente, assurdo, e ,.. ]

B0Lemma: tecnico, B0POS: B, B0Token: tecnicamente, S0B0Lemma: ,_tecnico, S0B0LemmaPOS: ,_B, S0B0POS: FF_B, S0B0POSLemma: FF_tecnico, S0B0Token: ,_tecnicamente, S0B1Lemma: ,_assurdo, S0B1LemmaPOS: ,_A, S0B1POS: FF_A, S0B1POSLemma: FF_assurdo, S0B1Token: ,_assurdo, S0Lemma: ,, S0POS: FF, S0Token: ,, TransHistory3: 202, 

40- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [tecnicamente, assurdo, e ,.. ]

B0Lemma: tecnico, B0POS: B, B0Token: tecnicamente, TransHistory3: 020, 

41- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [tecnicamente]   B= [assurdo, e, socialmente ,.. ]

B0Lemma: assurdo, B0POS: A, B0Token: assurdo, S0B0Lemma: tecnico_assurdo, S0B0LemmaPOS: tecnico_A, S0B0POS: B_A, S0B0POSLemma: B_assurdo, S0B0Token: tecnicamente_assurdo, S0B1Lemma: tecnico_e, S0B1LemmaPOS: tecnico_CC, S0B1POS: B_CC, S0B1POSLemma: B_e, S0B1Token: tecnicamente_e, S0Lemma: tecnico, S0POS: B, S0Token: tecnicamente, TransHistory3: 202, tecnico_isGouvernedBy_assurdo: true, tecnico_isGouvernedBy_assurdo_mod: true, 

42- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [assurdo, e, socialmente ,.. ]

B0Lemma: assurdo, B0POS: A, B0Token: assurdo, TransHistory3: 020, 

43- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [assurdo]   B= [e, socialmente, disonesto ,.. ]

B0Lemma: e, B0POS: CC, B0Token: e, S0B0Lemma: assurdo_e, S0B0LemmaPOS: assurdo_CC, S0B0POS: A_CC, S0B0POSLemma: A_e, S0B0Token: assurdo_e, S0B1Lemma: assurdo_socialmente, S0B1LemmaPOS: assurdo_B, S0B1POS: A_B, S0B1POSLemma: A_socialmente, S0B1Token: assurdo_socialmente, S0Lemma: assurdo, S0POS: A, S0Token: assurdo, TransHistory3: 202, 

44- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [e, socialmente, disonesto ,.. ]

B0Lemma: e, B0POS: CC, B0Token: e, TransHistory3: 020, 

45- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [e]   B= [socialmente, disonesto, , ,.. ]

B0Lemma: socialmente, B0POS: B, B0Token: socialmente, S0B0Lemma: e_socialmente, S0B0LemmaPOS: e_B, S0B0POS: CC_B, S0B0POSLemma: CC_socialmente, S0B0Token: e_socialmente, S0B1Lemma: e_disonesto, S0B1LemmaPOS: e_A, S0B1POS: CC_A, S0B1POSLemma: CC_disonesto, S0B1Token: e_disonesto, S0Lemma: e, S0POS: CC, S0Token: e, TransHistory3: 202, 

46- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [socialmente, disonesto, , ,.. ]

B0Lemma: socialmente, B0POS: B, B0Token: socialmente, TransHistory3: 020, 

47- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [socialmente]   B= [disonesto, ,, tale ,.. ]

B0Lemma: disonesto, B0POS: A, B0Token: disonesto, S0B0Lemma: socialmente_disonesto, S0B0LemmaPOS: socialmente_A, S0B0POS: B_A, S0B0POSLemma: B_disonesto, S0B0Token: socialmente_disonesto, S0B1Lemma: socialmente_,, S0B1LemmaPOS: socialmente_FF, S0B1POS: B_FF, S0B1POSLemma: B_,, S0B1Token: socialmente_,, S0Lemma: socialmente, S0POS: B, S0Token: socialmente, TransHistory3: 202, socialmente_isGouvernedBy_disonesto: true, socialmente_isGouvernedBy_disonesto_mod: true, 

48- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [disonesto, ,, tale ,.. ]

B0Lemma: disonesto, B0POS: A, B0Token: disonesto, TransHistory3: 020, 

49- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [disonesto]   B= [,, tale, da ,.. ]

B0Lemma: ,, B0POS: FF, B0Token: ,, S0B0Lemma: disonesto_,, S0B0LemmaPOS: disonesto_FF, S0B0POS: A_FF, S0B0POSLemma: A_,, S0B0Token: disonesto_,, S0B1Lemma: disonesto_tale, S0B1LemmaPOS: disonesto_A, S0B1POS: A_A, S0B1POSLemma: A_tale, S0B1Token: disonesto_tale, S0Lemma: disonesto, S0POS: A, S0Token: disonesto, TransHistory3: 202, 

50- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, tale, da ,.. ]

B0Lemma: ,, B0POS: FF, B0Token: ,, TransHistory3: 020, 

51- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [tale, da, avere ,.. ]

B0Lemma: tale, B0POS: A, B0Token: tale, S0B0Lemma: ,_tale, S0B0LemmaPOS: ,_A, S0B0POS: FF_A, S0B0POSLemma: FF_tale, S0B0Token: ,_tale, S0B1Lemma: ,_da, S0B1LemmaPOS: ,_E, S0B1POS: FF_E, S0B1POSLemma: FF_da, S0B1Token: ,_da, S0Lemma: ,, S0POS: FF, S0Token: ,, TransHistory3: 202, 

52- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [tale, da, avere ,.. ]

B0Lemma: tale, B0POS: A, B0Token: tale, TransHistory3: 020, 

53- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [tale]   B= [da, avere, prodotto ,.. ]

B0Lemma: da, B0POS: E, B0Token: da, S0B0Lemma: tale_da, S0B0LemmaPOS: tale_E, S0B0POS: A_E, S0B0POSLemma: A_da, S0B0Token: tale_da, S0B1Lemma: tale_avere, S0B1LemmaPOS: tale_VA, S0B1POS: A_VA, S0B1POSLemma: A_avere, S0B1Token: tale_avere, S0Lemma: tale, S0POS: A, S0Token: tale, TransHistory3: 202, hasRighDep_arg: true, tale_da_hasRighDep_arg: true, tale_hasRighDep_arg: true, 

54- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [da, avere, prodotto ,.. ]

B0Lemma: da, B0POS: E, B0Token: da, TransHistory3: 020, 

55- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [da]   B= [avere, prodotto, presso ,.. ]

B0Lemma: avere, B0POS: VA, B0Token: avere, S0B0Lemma: da_avere, S0B0LemmaPOS: da_VA, S0B0POS: E_VA, S0B0POSLemma: E_avere, S0B0Token: da_avere, S0B1Lemma: da_produrre, S0B1LemmaPOS: da_V, S0B1POS: E_V, S0B1POSLemma: E_produrre, S0B1Token: da_prodotto, S0Lemma: da, S0POS: E, S0Token: da, TransHistory3: 202, da_hasRighDep_prep: true, da_produrre_hasRighDep_prep: true, hasRighDep_prep: true, 

56- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [avere, prodotto, presso ,.. ]

B0Lemma: avere, B0POS: VA, B0Token: avere, TransHistory3: 020, 

57- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [avere]   B= [prodotto, presso, di ,.. ]

B0Lemma: produrre, B0POS: V, B0Token: prodotto, S0B0Lemma: avere_produrre, S0B0LemmaPOS: avere_V, S0B0POS: VA_V, S0B0POSLemma: VA_produrre, S0B0Token: avere_prodotto, S0B1Lemma: avere_presso, S0B1LemmaPOS: avere_E, S0B1POS: VA_E, S0B1POSLemma: VA_presso, S0B1Token: avere_presso, S0Lemma: avere, S0POS: VA, S0Token: avere, TransHistory3: 202, avere_isGouvernedBy_produrre: true, avere_isGouvernedBy_produrre_aux: true, 

58- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [prodotto, presso, di ,.. ]

B0Lemma: produrre, B0POS: V, B0Token: prodotto, TransHistory3: 020, 

59- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [prodotto]   B= [presso, di, noi ,.. ]

B0Lemma: presso, B0POS: E, B0Token: presso, S0B0Lemma: produrre_presso, S0B0LemmaPOS: produrre_E, S0B0POS: V_E, S0B0POSLemma: V_presso, S0B0Token: prodotto_presso, S0B1Lemma: produrre_di, S0B1LemmaPOS: produrre_E, S0B1POS: V_E, S0B1POSLemma: V_di, S0B1Token: prodotto_di, S0Lemma: produrre, S0POS: V, S0Token: prodotto, TransHistory3: 202, hasRighDep_comp: true, produrre_hasRighDep_comp: true, produrre_presso_hasRighDep_comp: true, 

60- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [presso, di, noi ,.. ]

B0Lemma: presso, B0POS: E, B0Token: presso, TransHistory3: 020, 

61- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [presso]   B= [di, noi, un ,.. ]

B0Lemma: di, B0POS: E, B0Token: di, S0B0Lemma: presso_di, S0B0LemmaPOS: presso_E, S0B0POS: E_E, S0B0POSLemma: E_di, S0B0Token: presso_di, S0B1Lemma: presso_noi, S0B1LemmaPOS: presso_PE, S0B1POS: E_PE, S0B1POSLemma: E_noi, S0B1Token: presso_noi, S0Lemma: presso, S0POS: E, S0Token: presso, TransHistory3: 202, hasRighDep_concat: true, presso_di_hasRighDep_concat: true, presso_hasRighDep_concat: true, 

62- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [di, noi, un ,.. ]

B0Lemma: di, B0POS: E, B0Token: di, TransHistory3: 020, 

63- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [di]   B= [noi, un, forte ,.. ]

B0Lemma: noi, B0POS: PE, B0Token: noi, S0B0Lemma: di_noi, S0B0LemmaPOS: di_PE, S0B0POS: E_PE, S0B0POSLemma: E_noi, S0B0Token: di_noi, S0B1Lemma: di_un, S0B1LemmaPOS: di_RI, S0B1POS: E_RI, S0B1POSLemma: E_un, S0B1Token: di_un, S0Lemma: di, S0POS: E, S0Token: di, TransHistory3: 202, di_hasRighDep_prep: true, di_noi_hasRighDep_prep: true, hasRighDep_prep: true, 

64- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [noi, un, forte ,.. ]

B0Lemma: noi, B0POS: PE, B0Token: noi, TransHistory3: 020, 

65- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [noi]   B= [un, forte, disagio ,.. ]

B0Lemma: un, B0POS: RI, B0Token: un, S0B0Lemma: noi_un, S0B0LemmaPOS: noi_RI, S0B0POS: PE_RI, S0B0POSLemma: PE_un, S0B0Token: noi_un, S0B1Lemma: noi_forte, S0B1LemmaPOS: noi_A, S0B1POS: PE_A, S0B1POSLemma: PE_forte, S0B1Token: noi_forte, S0Lemma: noi, S0POS: PE, S0Token: noi, TransHistory3: 202, hasRighDep_conj: true, hasRighDep_mod: true, hasRighDep_prep: true, noi_disagio_hasRighDep_prep: true, noi_hasRighDep_conj: true, noi_hasRighDep_mod: true, noi_hasRighDep_prep: true, noi_metodo_hasRighDep_mod: true, noi_quello_hasRighDep_conj: true, 

66- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [un, forte, disagio ,.. ]

B0Lemma: un, B0POS: RI, B0Token: un, TransHistory3: 020, 

67- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [un]   B= [forte, disagio, esistenziale ,.. ]

B0Lemma: forte, B0POS: A, B0Token: forte, S0B0Lemma: un_forte, S0B0LemmaPOS: un_A, S0B0POS: RI_A, S0B0POSLemma: RI_forte, S0B0Token: un_forte, S0B1Lemma: un_disagio, S0B1LemmaPOS: un_S, S0B1POS: RI_S, S0B1POSLemma: RI_disagio, S0B1Token: un_disagio, S0Lemma: un, S0POS: RI, S0Token: un, TransHistory3: 202, un_isGouvernedBy_disagio: true, un_isGouvernedBy_disagio_det: true, 

68- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [forte, disagio, esistenziale ,.. ]

B0Lemma: forte, B0POS: A, B0Token: forte, TransHistory3: 020, 

69- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [forte]   B= [disagio, esistenziale, e ,.. ]

B0Lemma: disagio, B0POS: S, B0Token: disagio, S0B0Lemma: forte_disagio, S0B0LemmaPOS: forte_S, S0B0POS: A_S, S0B0POSLemma: A_disagio, S0B0Token: forte_disagio, S0B1Lemma: forte_esistenziale, S0B1LemmaPOS: forte_A, S0B1POS: A_A, S0B1POSLemma: A_esistenziale, S0B1Token: forte_esistenziale, S0Lemma: forte, S0POS: A, S0Token: forte, TransHistory3: 202, forte_isGouvernedBy_disagio: true, forte_isGouvernedBy_disagio_mod: true, 

70- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [disagio, esistenziale, e ,.. ]

B0Lemma: disagio, B0POS: S, B0Token: disagio, TransHistory3: 020, 

71- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [disagio]   B= [esistenziale, e, la ,.. ]

B0Lemma: esistenziale, B0POS: A, B0Token: esistenziale, S0B0Lemma: disagio_esistenziale, S0B0LemmaPOS: disagio_A, S0B0POS: S_A, S0B0POSLemma: S_esistenziale, S0B0Token: disagio_esistenziale, S0B1Lemma: disagio_e, S0B1LemmaPOS: disagio_CC, S0B1POS: S_CC, S0B1POSLemma: S_e, S0B1Token: disagio_e, S0Lemma: disagio, S0POS: S, S0Token: disagio, TransHistory3: 202, disagio_e_hasRighDep_con: true, disagio_esistenziale_hasRighDep_mod: true, disagio_fame_hasRighDep_conj: true, disagio_hasRighDep_con: true, disagio_hasRighDep_conj: true, disagio_hasRighDep_mod: true, disagio_sistema_hasRighDep_conj: true, hasRighDep_con: true, hasRighDep_conj: true, hasRighDep_mod: true, 

72- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [esistenziale, e, la ,.. ]

B0Lemma: esistenziale, B0POS: A, B0Token: esistenziale, TransHistory3: 020, 

73- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [esistenziale]   B= [e, la, fame ,.. ]

B0Lemma: e, B0POS: CC, B0Token: e, S0B0Lemma: esistenziale_e, S0B0LemmaPOS: esistenziale_CC, S0B0POS: A_CC, S0B0POSLemma: A_e, S0B0Token: esistenziale_e, S0B1Lemma: esistenziale_il, S0B1LemmaPOS: esistenziale_RD, S0B1POS: A_RD, S0B1POSLemma: A_il, S0B1Token: esistenziale_la, S0Lemma: esistenziale, S0POS: A, S0Token: esistenziale, TransHistory3: 202, 

74- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [e, la, fame ,.. ]

B0Lemma: e, B0POS: CC, B0Token: e, TransHistory3: 020, 

75- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [e]   B= [la, fame, coatta ,.. ]

B0Lemma: il, B0POS: RD, B0Token: la, S0B0Lemma: e_il, S0B0LemmaPOS: e_RD, S0B0POS: CC_RD, S0B0POSLemma: CC_il, S0B0Token: e_la, S0B1Lemma: e_fame, S0B1LemmaPOS: e_S, S0B1POS: CC_S, S0B1POSLemma: CC_fame, S0B1Token: e_fame, S0Lemma: e, S0POS: CC, S0Token: e, TransHistory3: 202, 

76- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [la, fame, coatta ,.. ]

B0Lemma: il, B0POS: RD, B0Token: la, TransHistory3: 020, 

77- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [la]   B= [fame, coatta, presso ,.. ]

B0Lemma: fame, B0POS: S, B0Token: fame, S0B0Lemma: il_fame, S0B0LemmaPOS: il_S, S0B0POS: RD_S, S0B0POSLemma: RD_fame, S0B0Token: la_fame, S0B1Lemma: il_coatto, S0B1LemmaPOS: il_A, S0B1POS: RD_A, S0B1POSLemma: RD_coatto, S0B1Token: la_coatta, S0Lemma: il, S0POS: RD, S0Token: la, TransHistory3: 202, il_isGouvernedBy_fame: true, il_isGouvernedBy_fame_det: true, 

78- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [fame, coatta, presso ,.. ]

B0Lemma: fame, B0POS: S, B0Token: fame, TransHistory3: 020, 

79- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [fame]   B= [coatta, presso, altri ,.. ]

B0Lemma: coatto, B0POS: A, B0Token: coatta, S0B0Lemma: fame_coatto, S0B0LemmaPOS: fame_A, S0B0POS: S_A, S0B0POSLemma: S_coatto, S0B0Token: fame_coatta, S0B1Lemma: fame_presso, S0B1LemmaPOS: fame_E, S0B1POS: S_E, S0B1POSLemma: S_presso, S0B1Token: fame_presso, S0Lemma: fame, S0POS: S, S0Token: fame, TransHistory3: 202, fame_coatto_hasRighDep_mod: true, fame_hasRighDep_comp: true, fame_hasRighDep_mod: true, fame_presso_hasRighDep_comp: true, hasRighDep_comp: true, hasRighDep_mod: true, 

80- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [coatta, presso, altri ,.. ]

B0Lemma: coatto, B0POS: A, B0Token: coatta, TransHistory3: 020, 

81- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [coatta]   B= [presso, altri, ; ,.. ]

B0Lemma: presso, B0POS: E, B0Token: presso, S0B0Lemma: coatto_presso, S0B0LemmaPOS: coatto_E, S0B0POS: A_E, S0B0POSLemma: A_presso, S0B0Token: coatta_presso, S0B1Lemma: coatto_altro, S0B1LemmaPOS: coatto_A, S0B1POS: A_A, S0B1POSLemma: A_altro, S0B1Token: coatta_altri, S0Lemma: coatto, S0POS: A, S0Token: coatta, TransHistory3: 202, 

82- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [presso, altri, ; ,.. ]

B0Lemma: presso, B0POS: E, B0Token: presso, TransHistory3: 020, 

83- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [presso]   B= [altri, ;, il ,.. ]

B0Lemma: altro, B0POS: A, B0Token: altri, S0B0Lemma: presso_altro, S0B0LemmaPOS: presso_A, S0B0POS: E_A, S0B0POSLemma: E_altro, S0B0Token: presso_altri, S0B1Lemma: presso_;, S0B1LemmaPOS: presso_FC, S0B1POS: E_FC, S0B1POSLemma: E_;, S0B1Token: presso_;, S0Lemma: presso, S0POS: E, S0Token: presso, TransHistory3: 202, hasRighDep_prep: true, presso_altro_hasRighDep_prep: true, presso_hasRighDep_prep: true, 

84- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [altri, ;, il ,.. ]

B0Lemma: altro, B0POS: A, B0Token: altri, TransHistory3: 020, 

85- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [altri]   B= [;, il, sistema ,.. ]

B0Lemma: ;, B0POS: FC, B0Token: ;, S0B0Lemma: altro_;, S0B0LemmaPOS: altro_FC, S0B0POS: A_FC, S0B0POSLemma: A_;, S0B0Token: altri_;, S0B1Lemma: altro_il, S0B1LemmaPOS: altro_RD, S0B1POS: A_RD, S0B1POSLemma: A_il, S0B1Token: altri_il, S0Lemma: altro, S0POS: A, S0Token: altri, TransHistory3: 202, altro_;_hasRighDep_punc: true, altro_hasRighDep_punc: true, hasRighDep_punc: true, 

86- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [;, il, sistema ,.. ]

B0Lemma: ;, B0POS: FC, B0Token: ;, TransHistory3: 020, 

87- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [;]   B= [il, sistema, industriale ,.. ]

B0Lemma: il, B0POS: RD, B0Token: il, S0B0Lemma: ;_il, S0B0LemmaPOS: ;_RD, S0B0POS: FC_RD, S0B0POSLemma: FC_il, S0B0Token: ;_il, S0B1Lemma: ;_sistema, S0B1LemmaPOS: ;_S, S0B1POS: FC_S, S0B1POSLemma: FC_sistema, S0B1Token: ;_sistema, S0Lemma: ;, S0POS: FC, S0Token: ;, TransHistory3: 202, 

88- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [il, sistema, industriale ,.. ]

B0Lemma: il, B0POS: RD, B0Token: il, TransHistory3: 020, 

89- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [il]   B= [sistema, industriale, , ,.. ]

B0Lemma: sistema, B0POS: S, B0Token: sistema, S0B0Lemma: il_sistema, S0B0LemmaPOS: il_S, S0B0POS: RD_S, S0B0POSLemma: RD_sistema, S0B0Token: il_sistema, S0B1Lemma: il_industriale, S0B1LemmaPOS: il_A, S0B1POS: RD_A, S0B1POSLemma: RD_industriale, S0B1Token: il_industriale, S0Lemma: il, S0POS: RD, S0Token: il, TransHistory3: 202, il_isGouvernedBy_sistema: true, il_isGouvernedBy_sistema_det: true, 

90- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [sistema, industriale, , ,.. ]

B0Lemma: sistema, B0POS: S, B0Token: sistema, TransHistory3: 020, 

91- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [sistema]   B= [industriale, ,, da ,.. ]

B0Lemma: industriale, B0POS: A, B0Token: industriale, S0B0Lemma: sistema_industriale, S0B0LemmaPOS: sistema_A, S0B0POS: S_A, S0B0POSLemma: S_industriale, S0B0Token: sistema_industriale, S0B1Lemma: sistema_,, S0B1LemmaPOS: sistema_FF, S0B1POS: S_FF, S0B1POSLemma: S_,, S0B1Token: sistema_,, S0Lemma: sistema, S0POS: S, S0Token: sistema, TransHistory3: 202, hasRighDep_comp: true, hasRighDep_mod: true, hasRighDep_mod_rel: true, sistema_da_hasRighDep_comp: true, sistema_deludere_hasRighDep_mod_rel: true, sistema_hasRighDep_comp: true, sistema_hasRighDep_mod: true, sistema_hasRighDep_mod_rel: true, sistema_industriale_hasRighDep_mod: true, 

92- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [industriale, ,, da ,.. ]

B0Lemma: industriale, B0POS: A, B0Token: industriale, TransHistory3: 020, 

93- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [industriale]   B= [,, da, parte ,.. ]

B0Lemma: ,, B0POS: FF, B0Token: ,, S0B0Lemma: industriale_,, S0B0LemmaPOS: industriale_FF, S0B0POS: A_FF, S0B0POSLemma: A_,, S0B0Token: industriale_,, S0B1Lemma: industriale_da, S0B1LemmaPOS: industriale_E, S0B1POS: A_E, S0B1POSLemma: A_da, S0B1Token: industriale_da, S0Lemma: industriale, S0POS: A, S0Token: industriale, TransHistory3: 202, 

94- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, da, parte ,.. ]

B0Lemma: ,, B0POS: FF, B0Token: ,, TransHistory3: 020, 

95- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [da, parte, sua ,.. ]

,_isGouvernedBy_da: true, ,_isGouvernedBy_da_punc: true, B0Lemma: da, B0POS: E, B0Token: da, S0B0Lemma: ,_da, S0B0LemmaPOS: ,_E, S0B0POS: FF_E, S0B0POSLemma: FF_da, S0B0Token: ,_da, S0B1Lemma: ,_parte, S0B1LemmaPOS: ,_S, S0B1POS: FF_S, S0B1POSLemma: FF_parte, S0B1Token: ,_parte, S0Lemma: ,, S0POS: FF, S0Token: ,, TransHistory3: 202, 

96- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [da, parte, sua ,.. ]

B0Lemma: da, B0POS: E, B0Token: da, TransHistory3: 020, 

97- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [da]   B= [parte, sua, , ,.. ]

B0Lemma: parte, B0POS: S, B0Token: parte, S0B0Lemma: da_parte, S0B0LemmaPOS: da_S, S0B0POS: E_S, S0B0POSLemma: E_parte, S0B0Token: da_parte, S0B1Lemma: da_suo, S0B1LemmaPOS: da_AP, S0B1POS: E_AP, S0B1POSLemma: E_suo, S0B1Token: da_sua, S0Lemma: da, S0POS: E, S0Token: da, TransHistory3: 202, da_,_hasRighDep_punc: true, da_hasRighDep_prep: true, da_hasRighDep_punc: true, da_parte_hasRighDep_prep: true, hasRighDep_prep: true, hasRighDep_punc: true, 

98- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [parte, sua, , ,.. ]

B0Lemma: parte, B0POS: S, B0Token: parte, TransHistory3: 020, 

99- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [parte]   B= [sua, ,, ha ,.. ]

B0Lemma: suo, B0POS: AP, B0Token: sua, S0B0Lemma: parte_suo, S0B0LemmaPOS: parte_AP, S0B0POS: S_AP, S0B0POSLemma: S_suo, S0B0Token: parte_sua, S0B1Lemma: parte_,, S0B1LemmaPOS: parte_FF, S0B1POS: S_FF, S0B1POSLemma: S_,, S0B1Token: parte_,, S0Lemma: parte, S0POS: S, S0Token: parte, TransHistory3: 202, hasRighDep_mod: true, parte_hasRighDep_mod: true, parte_suo_hasRighDep_mod: true, 

100- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [sua, ,, ha ,.. ]

B0Lemma: suo, B0POS: AP, B0Token: sua, TransHistory3: 020, 

101- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [sua]   B= [,, ha, deluso ,.. ]

B0Lemma: ,, B0POS: FF, B0Token: ,, S0B0Lemma: suo_,, S0B0LemmaPOS: suo_FF, S0B0POS: AP_FF, S0B0POSLemma: AP_,, S0B0Token: sua_,, S0B1Lemma: suo_avere, S0B1LemmaPOS: suo_VA, S0B1POS: AP_VA, S0B1POSLemma: AP_avere, S0B1Token: sua_ha, S0Lemma: suo, S0POS: AP, S0Token: sua, TransHistory3: 202, 

102- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, ha, deluso ,.. ]

B0Lemma: ,, B0POS: FF, B0Token: ,, TransHistory3: 020, 

103- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [ha, deluso, le ,.. ]

B0Lemma: avere, B0POS: VA, B0Token: ha, S0B0Lemma: ,_avere, S0B0LemmaPOS: ,_VA, S0B0POS: FF_VA, S0B0POSLemma: FF_avere, S0B0Token: ,_ha, S0B1Lemma: ,_deludere, S0B1LemmaPOS: ,_V, S0B1POS: FF_V, S0B1POSLemma: FF_deludere, S0B1Token: ,_deluso, S0Lemma: ,, S0POS: FF, S0Token: ,, TransHistory3: 202, 

104- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ha, deluso, le ,.. ]

B0Lemma: avere, B0POS: VA, B0Token: ha, TransHistory3: 020, 

105- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ha]   B= [deluso, le, aspettative ,.. ]

B0Lemma: deludere, B0POS: V, B0Token: deluso, S0B0Lemma: avere_deludere, S0B0LemmaPOS: avere_V, S0B0POS: VA_V, S0B0POSLemma: VA_deludere, S0B0Token: ha_deluso, S0B1Lemma: avere_il, S0B1LemmaPOS: avere_RD, S0B1POS: VA_RD, S0B1POSLemma: VA_il, S0B1Token: ha_le, S0Lemma: avere, S0POS: VA, S0Token: ha, TransHistory3: 202, avere_isGouvernedBy_deludere: true, avere_isGouvernedBy_deludere_aux: true, 

106- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [deluso, le, aspettative ,.. ]

B0Lemma: deludere, B0POS: V, B0Token: deluso, TransHistory3: 020, 

107- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [deluso]   B= [le, aspettative, con ,.. ]

B0Lemma: il, B0POS: RD, B0Token: le, S0B0Lemma: deludere_il, S0B0LemmaPOS: deludere_RD, S0B0POS: V_RD, S0B0POSLemma: V_il, S0B0Token: deluso_le, S0B1Lemma: deludere_aspettativa, S0B1LemmaPOS: deludere_S, S0B1POS: V_S, S0B1POSLemma: V_aspettativa, S0B1Token: deluso_aspettative, S0Lemma: deludere, S0POS: V, S0Token: deluso, TransHistory3: 202, deludere_:_hasRighDep_punc: true, deludere_aspettativa_hasRighDep_obj: true, deludere_con_hasRighDep_comp: true, deludere_hasRighDep_comp: true, deludere_hasRighDep_obj: true, deludere_hasRighDep_punc: true, hasRighDep_comp: true, hasRighDep_obj: true, hasRighDep_punc: true, 

108- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [le, aspettative, con ,.. ]

B0Lemma: il, B0POS: RD, B0Token: le, TransHistory3: 020, 

109- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [le]   B= [aspettative, con, produzioni ,.. ]

B0Lemma: aspettativa, B0POS: S, B0Token: aspettative, S0B0Lemma: il_aspettativa, S0B0LemmaPOS: il_S, S0B0POS: RD_S, S0B0POSLemma: RD_aspettativa, S0B0Token: le_aspettative, S0B1Lemma: il_con, S0B1LemmaPOS: il_E, S0B1POS: RD_E, S0B1POSLemma: RD_con, S0B1Token: le_con, S0Lemma: il, S0POS: RD, S0Token: le, TransHistory3: 202, il_isGouvernedBy_aspettativa: true, il_isGouvernedBy_aspettativa_det: true, 

110- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [aspettative, con, produzioni ,.. ]

B0Lemma: aspettativa, B0POS: S, B0Token: aspettative, TransHistory3: 020, 

111- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [aspettative]   B= [con, produzioni, e ,.. ]

B0Lemma: con, B0POS: E, B0Token: con, S0B0Lemma: aspettativa_con, S0B0LemmaPOS: aspettativa_E, S0B0POS: S_E, S0B0POSLemma: S_con, S0B0Token: aspettative_con, S0B1Lemma: aspettativa_produzione, S0B1LemmaPOS: aspettativa_S, S0B1POS: S_S, S0B1POSLemma: S_produzione, S0B1Token: aspettative_produzioni, S0Lemma: aspettativa, S0POS: S, S0Token: aspettative, TransHistory3: 202, 

112- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [con, produzioni, e ,.. ]

B0Lemma: con, B0POS: E, B0Token: con, TransHistory3: 020, 

113- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [con]   B= [produzioni, e, metodi ,.. ]

B0Lemma: produzione, B0POS: S, B0Token: produzioni, S0B0Lemma: con_produzione, S0B0LemmaPOS: con_S, S0B0POS: E_S, S0B0POSLemma: E_produzione, S0B0Token: con_produzioni, S0B1Lemma: con_e, S0B1LemmaPOS: con_CC, S0B1POS: E_CC, S0B1POSLemma: E_e, S0B1Token: con_e, S0Lemma: con, S0POS: E, S0Token: con, TransHistory3: 202, con_hasRighDep_prep: true, con_produzione_hasRighDep_prep: true, hasRighDep_prep: true, 

114- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [produzioni, e, metodi ,.. ]

B0Lemma: produzione, B0POS: S, B0Token: produzioni, TransHistory3: 020, 

115- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [produzioni]   B= [e, metodi, che ,.. ]

B0Lemma: e, B0POS: CC, B0Token: e, S0B0Lemma: produzione_e, S0B0LemmaPOS: produzione_CC, S0B0POS: S_CC, S0B0POSLemma: S_e, S0B0Token: produzioni_e, S0B1Lemma: produzione_metodo, S0B1LemmaPOS: produzione_S, S0B1POS: S_S, S0B1POSLemma: S_metodo, S0B1Token: produzioni_metodi, S0Lemma: produzione, S0POS: S, S0Token: produzioni, TransHistory3: 202, hasRighDep_con: true, hasRighDep_conj: true, produzione_e_hasRighDep_con: true, produzione_hasRighDep_con: true, produzione_hasRighDep_conj: true, produzione_metodo_hasRighDep_conj: true, 

116- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [e, metodi, che ,.. ]

B0Lemma: e, B0POS: CC, B0Token: e, TransHistory3: 020, 

117- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [e]   B= [metodi, che, hanno ,.. ]

B0Lemma: metodo, B0POS: S, B0Token: metodi, S0B0Lemma: e_metodo, S0B0LemmaPOS: e_S, S0B0POS: CC_S, S0B0POSLemma: CC_metodo, S0B0Token: e_metodi, S0B1Lemma: e_che, S0B1LemmaPOS: e_PR, S0B1POS: CC_PR, S0B1POSLemma: CC_che, S0B1Token: e_che, S0Lemma: e, S0POS: CC, S0Token: e, TransHistory3: 202, 

118- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [metodi, che, hanno ,.. ]

B0Lemma: metodo, B0POS: S, B0Token: metodi, TransHistory3: 020, 

119- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [metodi]   B= [che, hanno, tradito ,.. ]

B0Lemma: che, B0POS: PR, B0Token: che, S0B0Lemma: metodo_che, S0B0LemmaPOS: metodo_PR, S0B0POS: S_PR, S0B0POSLemma: S_che, S0B0Token: metodi_che, S0B1Lemma: metodo_avere, S0B1LemmaPOS: metodo_VA, S0B1POS: S_VA, S0B1POSLemma: S_avere, S0B1Token: metodi_hanno, S0Lemma: metodo, S0POS: S, S0Token: metodi, TransHistory3: 202, hasRighDep_mod_rel: true, metodo_hasRighDep_mod_rel: true, metodo_tradire_hasRighDep_mod_rel: true, 

120- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [che, hanno, tradito ,.. ]

B0Lemma: che, B0POS: PR, B0Token: che, TransHistory3: 020, 

121- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [che]   B= [hanno, tradito, le ,.. ]

B0Lemma: avere, B0POS: VA, B0Token: hanno, S0B0Lemma: che_avere, S0B0LemmaPOS: che_VA, S0B0POS: PR_VA, S0B0POSLemma: PR_avere, S0B0Token: che_hanno, S0B1Lemma: che_tradire, S0B1LemmaPOS: che_V, S0B1POS: PR_V, S0B1POSLemma: PR_tradire, S0B1Token: che_tradito, S0Lemma: che, S0POS: PR, S0Token: che, TransHistory3: 202, che_isGouvernedBy_tradire: true, che_isGouvernedBy_tradire_subj: true, 

122- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [hanno, tradito, le ,.. ]

B0Lemma: avere, B0POS: VA, B0Token: hanno, TransHistory3: 020, 

123- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [hanno]   B= [tradito, le, leggi ,.. ]

B0Lemma: tradire, B0POS: V, B0Token: tradito, S0B0Lemma: avere_tradire, S0B0LemmaPOS: avere_V, S0B0POS: VA_V, S0B0POSLemma: VA_tradire, S0B0Token: hanno_tradito, S0B1Lemma: avere_il, S0B1LemmaPOS: avere_RD, S0B1POS: VA_RD, S0B1POSLemma: VA_il, S0B1Token: hanno_le, S0Lemma: avere, S0POS: VA, S0Token: hanno, TransHistory3: 202, avere_isGouvernedBy_tradire: true, avere_isGouvernedBy_tradire_aux: true, 

124- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [tradito, le, leggi ,.. ]

B0Lemma: tradire, B0POS: V, B0Token: tradito, TransHistory3: 020, 

125- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [tradito]   B= [le, leggi, fondamentali ,.. ]

B0Lemma: il, B0POS: RD, B0Token: le, S0B0Lemma: tradire_il, S0B0LemmaPOS: tradire_RD, S0B0POS: V_RD, S0B0POSLemma: V_il, S0B0Token: tradito_le, S0B1Lemma: tradire_legge, S0B1LemmaPOS: tradire_S, S0B1POS: V_S, S0B1POSLemma: V_legge, S0B1Token: tradito_leggi, S0Lemma: tradire, S0POS: V, S0Token: tradito, TransHistory3: 202, hasRighDep_obj: true, tradire_hasRighDep_obj: true, tradire_legge_hasRighDep_obj: true, 

126- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [tradito, le]   B= [leggi, fondamentali, del ,.. ]

B0Lemma: legge, B0POS: S, B0Token: leggi, S0B0Lemma: il_legge, S0B0LemmaPOS: il_S, S0B0POS: RD_S, S0B0POSLemma: RD_legge, S0B0Token: le_leggi, S0B1Lemma: il_fondamentale, S0B1LemmaPOS: il_A, S0B1POS: RD_A, S0B1POSLemma: RD_fondamentale, S0B1Token: le_fondamentali, S0Lemma: il, S0POS: RD, S0S1Distance: 1, S0Token: le, S1B0Lemma: tradire_legge, S1B0LemmaPOS: tradire_S, S1B0POS: V_S, S1B0POSLemma: V_legge, S1B0Token: tradito_leggi, S1Lemma: tradire, S1POS: V, S1S0Lemma: tradire_il, S1S0LemmaPOS: tradire_RD, S1S0POS: V_RD, S1S0POSLemma: V_il, S1S0Token: tradito_le, S1Token: tradito, TransHistory3: 020, il_isGouvernedBy_legge: true, il_isGouvernedBy_legge_det: true, 

127- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [tradito]   B= [leggi, fondamentali, del ,.. ]

B0Lemma: legge, B0POS: S, B0Token: leggi, S0B0Lemma: tradire_legge, S0B0LemmaPOS: tradire_S, S0B0POS: V_S, S0B0POSLemma: V_legge, S0B0Token: tradito_leggi, S0B1Lemma: tradire_fondamentale, S0B1LemmaPOS: tradire_A, S0B1POS: V_A, S0B1POSLemma: V_fondamentale, S0B1Token: tradito_fondamentali, S0Lemma: tradire, S0POS: V, S0Token: tradito, TransHistory3: 002, hasRighDep_obj: true, tradire_hasRighDep_obj: true, tradire_legge_hasRighDep_obj: true, 

128- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [tradito, leggi]   B= [fondamentali, del, pianeta ,.. ]

B0Lemma: fondamentale, B0POS: A, B0Token: fondamentali, S0B0Lemma: legge_fondamentale, S0B0LemmaPOS: legge_A, S0B0POS: S_A, S0B0POSLemma: S_fondamentale, S0B0Token: leggi_fondamentali, S0B1Lemma: legge_di, S0B1LemmaPOS: legge_EA, S0B1POS: S_EA, S0B1POSLemma: S_di, S0B1Token: leggi_del, S0Lemma: legge, S0POS: S, S0S1Distance: 2, S0Token: leggi, S1B0Lemma: tradire_fondamentale, S1B0LemmaPOS: tradire_A, S1B0POS: V_A, S1B0POSLemma: V_fondamentale, S1B0Token: tradito_fondamentali, S1Lemma: tradire, S1POS: V, S1S0Lemma: tradire_legge, S1S0LemmaPOS: tradire_S, S1S0POS: V_S, S1S0POSLemma: V_legge, S1S0Token: tradito_leggi, S1Token: tradito, SyntaxicRelation: +obj, TransHistory3: 200, hasRighDep_comp: true, hasRighDep_mod: true, legge_di_hasRighDep_comp: true, legge_fondamentale_hasRighDep_mod: true, legge_hasRighDep_comp: true, legge_hasRighDep_mod: true, 

129- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[tradito, leggi]]   B= [fondamentali, del, pianeta ,.. ]

B0Lemma: fondamentale, B0POS: A, B0Token: fondamentali, S0B0Lemma: tradire_legge_fondamentale, S0B0LemmaPOS: tradire_legge_A, S0B0POS: V_S_A, S0B0POSLemma: V_S_fondamentale, S0B0Token: tradito_leggi_fondamentali, S0B1Lemma: tradire_legge_di, S0B1LemmaPOS: tradire_legge_EA, S0B1POS: V_S_EA, S0B1POSLemma: V_S_di, S0B1Token: tradito_leggi_del, S0Lemma: tradire_legge, S0POS: V_S, S0Token: tradito_leggi, TransHistory3: 020, 

130- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [fondamentali, del, pianeta ,.. ]

B0Lemma: fondamentale, B0POS: A, B0Token: fondamentali, TransHistory3: 102, 

131- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [fondamentali]   B= [del, pianeta, : ,.. ]

B0Lemma: di, B0POS: EA, B0Token: del, S0B0Lemma: fondamentale_di, S0B0LemmaPOS: fondamentale_EA, S0B0POS: A_EA, S0B0POSLemma: A_di, S0B0Token: fondamentali_del, S0B1Lemma: fondamentale_pianeta, S0B1LemmaPOS: fondamentale_S, S0B1POS: A_S, S0B1POSLemma: A_pianeta, S0B1Token: fondamentali_pianeta, S0Lemma: fondamentale, S0POS: A, S0Token: fondamentali, TransHistory3: 210, 

132- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [del, pianeta, : ,.. ]

B0Lemma: di, B0POS: EA, B0Token: del, TransHistory3: 021, 

133- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [del]   B= [pianeta, :, metodi ,.. ]

B0Lemma: pianeta, B0POS: S, B0Token: pianeta, S0B0Lemma: di_pianeta, S0B0LemmaPOS: di_S, S0B0POS: EA_S, S0B0POSLemma: EA_pianeta, S0B0Token: del_pianeta, S0B1Lemma: di_:, S0B1LemmaPOS: di_FC, S0B1POS: EA_FC, S0B1POSLemma: EA_:, S0B1Token: del_:, S0Lemma: di, S0POS: EA, S0Token: del, TransHistory3: 202, di_hasRighDep_prep: true, di_pianeta_hasRighDep_prep: true, hasRighDep_prep: true, 

134- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [pianeta, :, metodi ,.. ]

B0Lemma: pianeta, B0POS: S, B0Token: pianeta, TransHistory3: 020, 

135- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [pianeta]   B= [:, metodi, e ,.. ]

B0Lemma: :, B0POS: FC, B0Token: :, S0B0Lemma: pianeta_:, S0B0LemmaPOS: pianeta_FC, S0B0POS: S_FC, S0B0POSLemma: S_:, S0B0Token: pianeta_:, S0B1Lemma: pianeta_metodo, S0B1LemmaPOS: pianeta_S, S0B1POS: S_S, S0B1POSLemma: S_metodo, S0B1Token: pianeta_metodi, S0Lemma: pianeta, S0POS: S, S0Token: pianeta, TransHistory3: 202, 

136- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [:, metodi, e ,.. ]

B0Lemma: :, B0POS: FC, B0Token: :, TransHistory3: 020, 

137- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [:]   B= [metodi, e, produzioni ,.. ]

B0Lemma: metodo, B0POS: S, B0Token: metodi, S0B0Lemma: :_metodo, S0B0LemmaPOS: :_S, S0B0POS: FC_S, S0B0POSLemma: FC_metodo, S0B0Token: :_metodi, S0B1Lemma: :_e, S0B1LemmaPOS: :_CC, S0B1POS: FC_CC, S0B1POSLemma: FC_e, S0B1Token: :_e, S0Lemma: :, S0POS: FC, S0Token: :, TransHistory3: 202, 

138- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [metodi, e, produzioni ,.. ]

B0Lemma: metodo, B0POS: S, B0Token: metodi, TransHistory3: 020, 

139- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [metodi]   B= [e, produzioni, che ,.. ]

B0Lemma: e, B0POS: CC, B0Token: e, S0B0Lemma: metodo_e, S0B0LemmaPOS: metodo_CC, S0B0POS: S_CC, S0B0POSLemma: S_e, S0B0Token: metodi_e, S0B1Lemma: metodo_produzione, S0B1LemmaPOS: metodo_S, S0B1POS: S_S, S0B1POSLemma: S_produzione, S0B1Token: metodi_produzioni, S0Lemma: metodo, S0POS: S, S0Token: metodi, TransHistory3: 202, hasRighDep_con: true, hasRighDep_conj: true, metodo_,_hasRighDep_con: true, metodo_e_hasRighDep_con: true, metodo_hasRighDep_con: true, metodo_hasRighDep_conj: true, metodo_produzione_hasRighDep_conj: true, metodo_tutto_hasRighDep_conj: true, 

140- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [e, produzioni, che ,.. ]

B0Lemma: e, B0POS: CC, B0Token: e, TransHistory3: 020, 

141- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [e]   B= [produzioni, che, sono ,.. ]

B0Lemma: produzione, B0POS: S, B0Token: produzioni, S0B0Lemma: e_produzione, S0B0LemmaPOS: e_S, S0B0POS: CC_S, S0B0POSLemma: CC_produzione, S0B0Token: e_produzioni, S0B1Lemma: e_che, S0B1LemmaPOS: e_PR, S0B1POS: CC_PR, S0B1POSLemma: CC_che, S0B1Token: e_che, S0Lemma: e, S0POS: CC, S0Token: e, TransHistory3: 202, 

142- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [produzioni, che, sono ,.. ]

B0Lemma: produzione, B0POS: S, B0Token: produzioni, TransHistory3: 020, 

143- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [produzioni]   B= [che, sono, stati ,.. ]

B0Lemma: che, B0POS: PR, B0Token: che, S0B0Lemma: produzione_che, S0B0LemmaPOS: produzione_PR, S0B0POS: S_PR, S0B0POSLemma: S_che, S0B0Token: produzioni_che, S0B1Lemma: produzione_essere, S0B1LemmaPOS: produzione_VA, S0B1POS: S_VA, S0B1POSLemma: S_essere, S0B1Token: produzioni_sono, S0Lemma: produzione, S0POS: S, S0Token: produzioni, TransHistory3: 202, hasRighDep_mod_rel: true, produzione_hasRighDep_mod_rel: true, produzione_trasferire_hasRighDep_mod_rel: true, 

144- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [che, sono, stati ,.. ]

B0Lemma: che, B0POS: PR, B0Token: che, TransHistory3: 020, 

145- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [che]   B= [sono, stati, trasferiti ,.. ]

B0Lemma: essere, B0POS: VA, B0Token: sono, S0B0Lemma: che_essere, S0B0LemmaPOS: che_VA, S0B0POS: PR_VA, S0B0POSLemma: PR_essere, S0B0Token: che_sono, S0B1Lemma: che_essere, S0B1LemmaPOS: che_VA, S0B1POS: PR_VA, S0B1POSLemma: PR_essere, S0B1Token: che_stati, S0Lemma: che, S0POS: PR, S0Token: che, TransHistory3: 202, che_isGouvernedBy_trasferire: true, che_isGouvernedBy_trasferire_subj: true, 

146- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [sono, stati, trasferiti ,.. ]

B0Lemma: essere, B0POS: VA, B0Token: sono, TransHistory3: 020, 

147- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [sono]   B= [stati, trasferiti, all' ,.. ]

B0Lemma: essere, B0POS: VA, B0Token: stati, S0B0Lemma: essere_essere, S0B0LemmaPOS: essere_VA, S0B0POS: VA_VA, S0B0POSLemma: VA_essere, S0B0Token: sono_stati, S0B1Lemma: essere_trasferire, S0B1LemmaPOS: essere_V, S0B1POS: VA_V, S0B1POSLemma: VA_trasferire, S0B1Token: sono_trasferiti, S0Lemma: essere, S0POS: VA, S0Token: sono, TransHistory3: 202, essere_isGouvernedBy_essere: true, essere_isGouvernedBy_essere_aux: true, 

148- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [stati, trasferiti, all' ,.. ]

B0Lemma: essere, B0POS: VA, B0Token: stati, TransHistory3: 020, 

149- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [stati]   B= [trasferiti, all', agricoltura ,.. ]

B0Lemma: trasferire, B0POS: V, B0Token: trasferiti, S0B0Lemma: essere_trasferire, S0B0LemmaPOS: essere_V, S0B0POS: VA_V, S0B0POSLemma: VA_trasferire, S0B0Token: stati_trasferiti, S0B1Lemma: essere_al, S0B1LemmaPOS: essere_EA, S0B1POS: VA_EA, S0B1POSLemma: VA_al, S0B1Token: stati_all', S0Lemma: essere, S0POS: VA, S0Token: stati, TransHistory3: 202, essere_isGouvernedBy_trasferire: true, essere_isGouvernedBy_trasferire_aux: true, 

150- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [trasferiti, all', agricoltura ,.. ]

B0Lemma: trasferire, B0POS: V, B0Token: trasferiti, TransHistory3: 020, 

151- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [trasferiti]   B= [all', agricoltura, spesso ,.. ]

B0Lemma: al, B0POS: EA, B0Token: all', S0B0Lemma: trasferire_al, S0B0LemmaPOS: trasferire_EA, S0B0POS: V_EA, S0B0POSLemma: V_al, S0B0Token: trasferiti_all', S0B1Lemma: trasferire_agricoltura, S0B1LemmaPOS: trasferire_S, S0B1POS: V_S, S0B1POSLemma: V_agricoltura, S0B1Token: trasferiti_agricoltura, S0Lemma: trasferire, S0POS: V, S0Token: trasferiti, TransHistory3: 202, hasRighDep_comp: true, hasRighDep_comp_loc: true, hasRighDep_con: true, hasRighDep_conj: true, trasferire_al_hasRighDep_comp_loc: true, trasferire_creare_hasRighDep_conj: true, trasferire_e_hasRighDep_con: true, trasferire_hasRighDep_comp: true, trasferire_hasRighDep_comp_loc: true, trasferire_hasRighDep_con: true, trasferire_hasRighDep_conj: true, trasferire_senza_hasRighDep_comp: true, 

152- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [all', agricoltura, spesso ,.. ]

B0Lemma: al, B0POS: EA, B0Token: all', TransHistory3: 020, 

153- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [all']   B= [agricoltura, spesso, senza ,.. ]

B0Lemma: agricoltura, B0POS: S, B0Token: agricoltura, S0B0Lemma: al_agricoltura, S0B0LemmaPOS: al_S, S0B0POS: EA_S, S0B0POSLemma: EA_agricoltura, S0B0Token: all'_agricoltura, S0B1Lemma: al_spesso, S0B1LemmaPOS: al_B, S0B1POS: EA_B, S0B1POSLemma: EA_spesso, S0B1Token: all'_spesso, S0Lemma: al, S0POS: EA, S0Token: all', TransHistory3: 202, al_agricoltura_hasRighDep_prep: true, al_hasRighDep_prep: true, hasRighDep_prep: true, 

154- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [agricoltura, spesso, senza ,.. ]

B0Lemma: agricoltura, B0POS: S, B0Token: agricoltura, TransHistory3: 020, 

155- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [agricoltura]   B= [spesso, senza, necessità ,.. ]

B0Lemma: spesso, B0POS: B, B0Token: spesso, S0B0Lemma: agricoltura_spesso, S0B0LemmaPOS: agricoltura_B, S0B0POS: S_B, S0B0POSLemma: S_spesso, S0B0Token: agricoltura_spesso, S0B1Lemma: agricoltura_senza, S0B1LemmaPOS: agricoltura_E, S0B1POS: S_E, S0B1POSLemma: S_senza, S0B1Token: agricoltura_senza, S0Lemma: agricoltura, S0POS: S, S0Token: agricoltura, TransHistory3: 202, 

156- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [spesso, senza, necessità ,.. ]

B0Lemma: spesso, B0POS: B, B0Token: spesso, TransHistory3: 020, 

157- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [spesso]   B= [senza, necessità, e ,.. ]

B0Lemma: senza, B0POS: E, B0Token: senza, S0B0Lemma: spesso_senza, S0B0LemmaPOS: spesso_E, S0B0POS: B_E, S0B0POSLemma: B_senza, S0B0Token: spesso_senza, S0B1Lemma: spesso_necessità, S0B1LemmaPOS: spesso_S, S0B1POS: B_S, S0B1POSLemma: B_necessità, S0B1Token: spesso_necessità, S0Lemma: spesso, S0POS: B, S0Token: spesso, TransHistory3: 202, spesso_isGouvernedBy_senza: true, spesso_isGouvernedBy_senza_mod: true, 

158- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [senza, necessità, e ,.. ]

B0Lemma: senza, B0POS: E, B0Token: senza, TransHistory3: 020, 

159- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [senza]   B= [necessità, e, che ,.. ]

B0Lemma: necessità, B0POS: S, B0Token: necessità, S0B0Lemma: senza_necessità, S0B0LemmaPOS: senza_S, S0B0POS: E_S, S0B0POSLemma: E_necessità, S0B0Token: senza_necessità, S0B1Lemma: senza_e, S0B1LemmaPOS: senza_CC, S0B1POS: E_CC, S0B1POSLemma: E_e, S0B1Token: senza_e, S0Lemma: senza, S0POS: E, S0Token: senza, TransHistory3: 202, hasRighDep_prep: true, senza_hasRighDep_prep: true, senza_necessità_hasRighDep_prep: true, 

160- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [necessità, e, che ,.. ]

B0Lemma: necessità, B0POS: S, B0Token: necessità, TransHistory3: 020, 

161- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [necessità]   B= [e, che, hanno ,.. ]

B0Lemma: e, B0POS: CC, B0Token: e, S0B0Lemma: necessità_e, S0B0LemmaPOS: necessità_CC, S0B0POS: S_CC, S0B0POSLemma: S_e, S0B0Token: necessità_e, S0B1Lemma: necessità_che, S0B1LemmaPOS: necessità_PR, S0B1POS: S_PR, S0B1POSLemma: S_che, S0B1Token: necessità_che, S0Lemma: necessità, S0POS: S, S0Token: necessità, TransHistory3: 202, 

162- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [e, che, hanno ,.. ]

B0Lemma: e, B0POS: CC, B0Token: e, TransHistory3: 020, 

163- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [e]   B= [che, hanno, creato ,.. ]

B0Lemma: che, B0POS: PR, B0Token: che, S0B0Lemma: e_che, S0B0LemmaPOS: e_PR, S0B0POS: CC_PR, S0B0POSLemma: CC_che, S0B0Token: e_che, S0B1Lemma: e_avere, S0B1LemmaPOS: e_VA, S0B1POS: CC_VA, S0B1POSLemma: CC_avere, S0B1Token: e_hanno, S0Lemma: e, S0POS: CC, S0Token: e, TransHistory3: 202, 

164- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [che, hanno, creato ,.. ]

B0Lemma: che, B0POS: PR, B0Token: che, TransHistory3: 020, 

165- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [che]   B= [hanno, creato, nella ,.. ]

B0Lemma: avere, B0POS: VA, B0Token: hanno, S0B0Lemma: che_avere, S0B0LemmaPOS: che_VA, S0B0POS: PR_VA, S0B0POSLemma: PR_avere, S0B0Token: che_hanno, S0B1Lemma: che_creare, S0B1LemmaPOS: che_V, S0B1POS: PR_V, S0B1POSLemma: PR_creare, S0B1Token: che_creato, S0Lemma: che, S0POS: PR, S0Token: che, TransHistory3: 202, che_isGouvernedBy_creare: true, che_isGouvernedBy_creare_subj: true, 

166- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [hanno, creato, nella ,.. ]

B0Lemma: avere, B0POS: VA, B0Token: hanno, TransHistory3: 020, 

167- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [hanno]   B= [creato, nella, società ,.. ]

B0Lemma: creare, B0POS: V, B0Token: creato, S0B0Lemma: avere_creare, S0B0LemmaPOS: avere_V, S0B0POS: VA_V, S0B0POSLemma: VA_creare, S0B0Token: hanno_creato, S0B1Lemma: avere_in, S0B1LemmaPOS: avere_EA, S0B1POS: VA_EA, S0B1POSLemma: VA_in, S0B1Token: hanno_nella, S0Lemma: avere, S0POS: VA, S0Token: hanno, TransHistory3: 202, avere_isGouvernedBy_creare: true, avere_isGouvernedBy_creare_aux: true, 

168- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [creato, nella, società ,.. ]

B0Lemma: creare, B0POS: V, B0Token: creato, TransHistory3: 020, 

169- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [creato]   B= [nella, società, un ,.. ]

B0Lemma: in, B0POS: EA, B0Token: nella, S0B0Lemma: creare_in, S0B0LemmaPOS: creare_EA, S0B0POS: V_EA, S0B0POSLemma: V_in, S0B0Token: creato_nella, S0B1Lemma: creare_società, S0B1LemmaPOS: creare_S, S0B1POS: V_S, S0B1POSLemma: V_società, S0B1Token: creato_società, S0Lemma: creare, S0POS: V, S0Token: creato, TransHistory3: 202, creare_hasRighDep_comp_loc: true, creare_in_hasRighDep_comp_loc: true, hasRighDep_comp_loc: true, 

170- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [nella, società, un ,.. ]

B0Lemma: in, B0POS: EA, B0Token: nella, TransHistory3: 020, 

171- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [nella]   B= [società, un, altrettanto ,.. ]

B0Lemma: società, B0POS: S, B0Token: società, S0B0Lemma: in_società, S0B0LemmaPOS: in_S, S0B0POS: EA_S, S0B0POSLemma: EA_società, S0B0Token: nella_società, S0B1Lemma: in_un, S0B1LemmaPOS: in_RI, S0B1POS: EA_RI, S0B1POSLemma: EA_un, S0B1Token: nella_un, S0Lemma: in, S0POS: EA, S0Token: nella, TransHistory3: 202, hasRighDep_prep: true, in_disagio_hasRighDep_prep: true, in_hasRighDep_prep: true, in_società_hasRighDep_prep: true, 

172- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [società, un, altrettanto ,.. ]

B0Lemma: società, B0POS: S, B0Token: società, TransHistory3: 020, 

173- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [società]   B= [un, altrettanto, forte ,.. ]

B0Lemma: un, B0POS: RI, B0Token: un, S0B0Lemma: società_un, S0B0LemmaPOS: società_RI, S0B0POS: S_RI, S0B0POSLemma: S_un, S0B0Token: società_un, S0B1Lemma: società_altrettanto, S0B1LemmaPOS: società_B, S0B1POS: S_B, S0B1POSLemma: S_altrettanto, S0B1Token: società_altrettanto, S0Lemma: società, S0POS: S, S0Token: società, TransHistory3: 202, 

174- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [un, altrettanto, forte ,.. ]

B0Lemma: un, B0POS: RI, B0Token: un, TransHistory3: 020, 

175- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [un]   B= [altrettanto, forte, disagio ,.. ]

B0Lemma: altrettanto, B0POS: B, B0Token: altrettanto, S0B0Lemma: un_altrettanto, S0B0LemmaPOS: un_B, S0B0POS: RI_B, S0B0POSLemma: RI_altrettanto, S0B0Token: un_altrettanto, S0B1Lemma: un_forte, S0B1LemmaPOS: un_A, S0B1POS: RI_A, S0B1POSLemma: RI_forte, S0B1Token: un_forte, S0Lemma: un, S0POS: RI, S0Token: un, TransHistory3: 202, un_isGouvernedBy_disagio: true, un_isGouvernedBy_disagio_det: true, 

176- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [altrettanto, forte, disagio ,.. ]

B0Lemma: altrettanto, B0POS: B, B0Token: altrettanto, TransHistory3: 020, 

177- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [altrettanto]   B= [forte, disagio, che ,.. ]

B0Lemma: forte, B0POS: A, B0Token: forte, S0B0Lemma: altrettanto_forte, S0B0LemmaPOS: altrettanto_A, S0B0POS: B_A, S0B0POSLemma: B_forte, S0B0Token: altrettanto_forte, S0B1Lemma: altrettanto_disagio, S0B1LemmaPOS: altrettanto_S, S0B1POS: B_S, S0B1POSLemma: B_disagio, S0B1Token: altrettanto_disagio, S0Lemma: altrettanto, S0POS: B, S0Token: altrettanto, TransHistory3: 202, altrettanto_isGouvernedBy_disagio: true, altrettanto_isGouvernedBy_disagio_mod: true, 

178- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [forte, disagio, che ,.. ]

B0Lemma: forte, B0POS: A, B0Token: forte, TransHistory3: 020, 

179- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [forte]   B= [disagio, che, è ,.. ]

B0Lemma: disagio, B0POS: S, B0Token: disagio, S0B0Lemma: forte_disagio, S0B0LemmaPOS: forte_S, S0B0POS: A_S, S0B0POSLemma: A_disagio, S0B0Token: forte_disagio, S0B1Lemma: forte_che, S0B1LemmaPOS: forte_PR, S0B1POS: A_PR, S0B1POSLemma: A_che, S0B1Token: forte_che, S0Lemma: forte, S0POS: A, S0Token: forte, TransHistory3: 202, forte_isGouvernedBy_disagio: true, forte_isGouvernedBy_disagio_mod: true, 

180- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [disagio, che, è ,.. ]

B0Lemma: disagio, B0POS: S, B0Token: disagio, TransHistory3: 020, 

181- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [disagio]   B= [che, è, sotto ,.. ]

B0Lemma: che, B0POS: PR, B0Token: che, S0B0Lemma: disagio_che, S0B0LemmaPOS: disagio_PR, S0B0POS: S_PR, S0B0POSLemma: S_che, S0B0Token: disagio_che, S0B1Lemma: disagio_essere, S0B1LemmaPOS: disagio_V, S0B1POS: S_V, S0B1POSLemma: S_essere, S0B1Token: disagio_è, S0Lemma: disagio, S0POS: S, S0Token: disagio, TransHistory3: 202, disagio_essere_hasRighDep_mod_rel: true, disagio_hasRighDep_mod_rel: true, hasRighDep_mod_rel: true, 

182- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [che, è, sotto ,.. ]

B0Lemma: che, B0POS: PR, B0Token: che, TransHistory3: 020, 

183- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [che]   B= [è, sotto, gli ,.. ]

B0Lemma: essere, B0POS: V, B0Token: è, S0B0Lemma: che_essere, S0B0LemmaPOS: che_V, S0B0POS: PR_V, S0B0POSLemma: PR_essere, S0B0Token: che_è, S0B1Lemma: che_sotto, S0B1LemmaPOS: che_E, S0B1POS: PR_E, S0B1POSLemma: PR_sotto, S0B1Token: che_sotto, S0Lemma: che, S0POS: PR, S0Token: che, TransHistory3: 202, che_isGouvernedBy_essere: true, che_isGouvernedBy_essere_subj: true, 

184- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [è, sotto, gli ,.. ]

B0Lemma: essere, B0POS: V, B0Token: è, TransHistory3: 020, 

185- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [è]   B= [sotto, gli, occhi ,.. ]

B0Lemma: sotto, B0POS: E, B0Token: sotto, S0B0Lemma: essere_sotto, S0B0LemmaPOS: essere_E, S0B0POS: V_E, S0B0POSLemma: V_sotto, S0B0Token: è_sotto, S0B1Lemma: essere_il, S0B1LemmaPOS: essere_RD, S0B1POS: V_RD, S0B1POSLemma: V_il, S0B1Token: è_gli, S0Lemma: essere, S0POS: V, S0Token: è, TransHistory3: 202, essere_hasRighDep_pred: true, essere_sotto_hasRighDep_pred: true, hasRighDep_pred: true, 

186- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [sotto, gli, occhi ,.. ]

B0Lemma: sotto, B0POS: E, B0Token: sotto, TransHistory3: 020, 

187- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [sotto]   B= [gli, occhi, di ,.. ]

B0Lemma: il, B0POS: RD, B0Token: gli, S0B0Lemma: sotto_il, S0B0LemmaPOS: sotto_RD, S0B0POS: E_RD, S0B0POSLemma: E_il, S0B0Token: sotto_gli, S0B1Lemma: sotto_occhio, S0B1LemmaPOS: sotto_S, S0B1POS: E_S, S0B1POSLemma: E_occhio, S0B1Token: sotto_occhi, S0Lemma: sotto, S0POS: E, S0Token: sotto, TransHistory3: 202, hasRighDep_prep: true, sotto_hasRighDep_prep: true, sotto_occhio_hasRighDep_prep: true, 

188- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [gli, occhi, di ,.. ]

B0Lemma: il, B0POS: RD, B0Token: gli, TransHistory3: 020, 

189- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [gli]   B= [occhi, di, tutti ,.. ]

B0Lemma: occhio, B0POS: S, B0Token: occhi, S0B0Lemma: il_occhio, S0B0LemmaPOS: il_S, S0B0POS: RD_S, S0B0POSLemma: RD_occhio, S0B0Token: gli_occhi, S0B1Lemma: il_di, S0B1LemmaPOS: il_E, S0B1POS: RD_E, S0B1POSLemma: RD_di, S0B1Token: gli_di, S0Lemma: il, S0POS: RD, S0Token: gli, TransHistory3: 202, il_isGouvernedBy_occhio: true, il_isGouvernedBy_occhio_det: true, 

190- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [occhi, di, tutti ,.. ]

B0Lemma: occhio, B0POS: S, B0Token: occhi, TransHistory3: 020, 

191- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [occhi]   B= [di, tutti, il ,.. ]

B0Lemma: di, B0POS: E, B0Token: di, S0B0Lemma: occhio_di, S0B0LemmaPOS: occhio_E, S0B0POS: S_E, S0B0POSLemma: S_di, S0B0Token: occhi_di, S0B1Lemma: occhio_tutto, S0B1LemmaPOS: occhio_T, S0B1POS: S_T, S0B1POSLemma: S_tutto, S0B1Token: occhi_tutti, S0Lemma: occhio, S0POS: S, S0Token: occhi, TransHistory3: 202, hasRighDep_comp: true, occhio_di_hasRighDep_comp: true, occhio_hasRighDep_comp: true, 

192- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [di, tutti, il ,.. ]

B0Lemma: di, B0POS: E, B0Token: di, TransHistory3: 020, 

193- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [di]   B= [tutti, il, quale ,.. ]

B0Lemma: tutto, B0POS: T, B0Token: tutti, S0B0Lemma: di_tutto, S0B0LemmaPOS: di_T, S0B0POS: E_T, S0B0POSLemma: E_tutto, S0B0Token: di_tutti, S0B1Lemma: di_il, S0B1LemmaPOS: di_RD, S0B1POS: E_RD, S0B1POSLemma: E_il, S0B1Token: di_il, S0Lemma: di, S0POS: E, S0Token: di, TransHistory3: 202, 

194- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [tutti, il, quale ,.. ]

B0Lemma: tutto, B0POS: T, B0Token: tutti, TransHistory3: 020, 

195- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [tutti]   B= [il, quale, , ,.. ]

B0Lemma: il, B0POS: RD, B0Token: il, S0B0Lemma: tutto_il, S0B0LemmaPOS: tutto_RD, S0B0POS: T_RD, S0B0POSLemma: T_il, S0B0Token: tutti_il, S0B1Lemma: tutto_quale, S0B1LemmaPOS: tutto_PR, S0B1POS: T_PR, S0B1POSLemma: T_quale, S0B1Token: tutti_quale, S0Lemma: tutto, S0POS: T, S0Token: tutti, TransHistory3: 202, hasRighDep_mod: true, tutto_hasRighDep_mod: true, tutto_quale_hasRighDep_mod: true, 

196- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [il, quale, , ,.. ]

B0Lemma: il, B0POS: RD, B0Token: il, TransHistory3: 020, 

197- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [il]   B= [quale, ,, se ,.. ]

B0Lemma: quale, B0POS: PR, B0Token: quale, S0B0Lemma: il_quale, S0B0LemmaPOS: il_PR, S0B0POS: RD_PR, S0B0POSLemma: RD_quale, S0B0Token: il_quale, S0B1Lemma: il_,, S0B1LemmaPOS: il_FF, S0B1POS: RD_FF, S0B1POSLemma: RD_,, S0B1Token: il_,, S0Lemma: il, S0POS: RD, S0Token: il, TransHistory3: 202, il_isGouvernedBy_quale: true, il_isGouvernedBy_quale_det: true, 

198- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [quale, ,, se ,.. ]

B0Lemma: quale, B0POS: PR, B0Token: quale, TransHistory3: 020, 

199- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [quale]   B= [,, se, colpisce ,.. ]

B0Lemma: ,, B0POS: FF, B0Token: ,, S0B0Lemma: quale_,, S0B0LemmaPOS: quale_FF, S0B0POS: PR_FF, S0B0POSLemma: PR_,, S0B0Token: quale_,, S0B1Lemma: quale_se, S0B1LemmaPOS: quale_CS, S0B1POS: PR_CS, S0B1POSLemma: PR_se, S0B1Token: quale_se, S0Lemma: quale, S0POS: PR, S0Token: quale, TransHistory3: 202, 

200- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, se, colpisce ,.. ]

B0Lemma: ,, B0POS: FF, B0Token: ,, TransHistory3: 020, 

201- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [se, colpisce, nell' ,.. ]

B0Lemma: se, B0POS: CS, B0Token: se, S0B0Lemma: ,_se, S0B0LemmaPOS: ,_CS, S0B0POS: FF_CS, S0B0POSLemma: FF_se, S0B0Token: ,_se, S0B1Lemma: ,_colpire, S0B1LemmaPOS: ,_V, S0B1POS: FF_V, S0B1POSLemma: FF_colpire, S0B1Token: ,_colpisce, S0Lemma: ,, S0POS: FF, S0Token: ,, TransHistory3: 202, 

202- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [se, colpisce, nell' ,.. ]

B0Lemma: se, B0POS: CS, B0Token: se, TransHistory3: 020, 

203- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [se]   B= [colpisce, nell', immediato ,.. ]

B0Lemma: colpire, B0POS: V, B0Token: colpisce, S0B0Lemma: se_colpire, S0B0LemmaPOS: se_V, S0B0POS: CS_V, S0B0POSLemma: CS_colpire, S0B0Token: se_colpisce, S0B1Lemma: se_in, S0B1LemmaPOS: se_EA, S0B1POS: CS_EA, S0B1POSLemma: CS_in, S0B1Token: se_nell', S0Lemma: se, S0POS: CS, S0Token: se, TransHistory3: 202, hasRighDep_sub: true, se_colpire_hasRighDep_sub: true, se_hasRighDep_sub: true, se_isGouvernedBy_quello: true, se_isGouvernedBy_quello_mod: true, 

204- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [colpisce, nell', immediato ,.. ]

B0Lemma: colpire, B0POS: V, B0Token: colpisce, TransHistory3: 020, 

205- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [colpisce]   B= [nell', immediato, soprattutto ,.. ]

B0Lemma: in, B0POS: EA, B0Token: nell', S0B0Lemma: colpire_in, S0B0LemmaPOS: colpire_EA, S0B0POS: V_EA, S0B0POSLemma: V_in, S0B0Token: colpisce_nell', S0B1Lemma: colpire_immediato, S0B1LemmaPOS: colpire_A, S0B1POS: V_A, S0B1POSLemma: V_immediato, S0B1Token: colpisce_immediato, S0Lemma: colpire, S0POS: V, S0Token: colpisce, TransHistory3: 202, colpire_hasRighDep_comp: true, colpire_in_hasRighDep_comp: true, hasRighDep_comp: true, 

206- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [nell', immediato, soprattutto ,.. ]

B0Lemma: in, B0POS: EA, B0Token: nell', TransHistory3: 020, 

207- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [nell']   B= [immediato, soprattutto, quelli ,.. ]

B0Lemma: immediato, B0POS: A, B0Token: immediato, S0B0Lemma: in_immediato, S0B0LemmaPOS: in_A, S0B0POS: EA_A, S0B0POSLemma: EA_immediato, S0B0Token: nell'_immediato, S0B1Lemma: in_soprattutto, S0B1LemmaPOS: in_B, S0B1POS: EA_B, S0B1POSLemma: EA_soprattutto, S0B1Token: nell'_soprattutto, S0Lemma: in, S0POS: EA, S0Token: nell', TransHistory3: 202, hasRighDep_prep: true, in_hasRighDep_prep: true, in_immediato_hasRighDep_prep: true, 

208- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [immediato, soprattutto, quelli ,.. ]

B0Lemma: immediato, B0POS: A, B0Token: immediato, TransHistory3: 020, 

209- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [immediato]   B= [soprattutto, quelli, che ,.. ]

B0Lemma: soprattutto, B0POS: B, B0Token: soprattutto, S0B0Lemma: immediato_soprattutto, S0B0LemmaPOS: immediato_B, S0B0POS: A_B, S0B0POSLemma: A_soprattutto, S0B0Token: immediato_soprattutto, S0B1Lemma: immediato_quello, S0B1LemmaPOS: immediato_PD, S0B1POS: A_PD, S0B1POSLemma: A_quello, S0B1Token: immediato_quelli, S0Lemma: immediato, S0POS: A, S0Token: immediato, TransHistory3: 202, 

210- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [soprattutto, quelli, che ,.. ]

B0Lemma: soprattutto, B0POS: B, B0Token: soprattutto, TransHistory3: 020, 

211- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [soprattutto]   B= [quelli, che, appartengono ,.. ]

B0Lemma: quello, B0POS: PD, B0Token: quelli, S0B0Lemma: soprattutto_quello, S0B0LemmaPOS: soprattutto_PD, S0B0POS: B_PD, S0B0POSLemma: B_quello, S0B0Token: soprattutto_quelli, S0B1Lemma: soprattutto_che, S0B1LemmaPOS: soprattutto_PR, S0B1POS: B_PR, S0B1POSLemma: B_che, S0B1Token: soprattutto_che, S0Lemma: soprattutto, S0POS: B, S0Token: soprattutto, TransHistory3: 202, soprattutto_isGouvernedBy_quello: true, soprattutto_isGouvernedBy_quello_mod: true, 

212- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [quelli, che, appartengono ,.. ]

B0Lemma: quello, B0POS: PD, B0Token: quelli, TransHistory3: 020, 

213- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [quelli]   B= [che, appartengono, alle ,.. ]

B0Lemma: che, B0POS: PR, B0Token: che, S0B0Lemma: quello_che, S0B0LemmaPOS: quello_PR, S0B0POS: PD_PR, S0B0POSLemma: PD_che, S0B0Token: quelli_che, S0B1Lemma: quello_appartenere, S0B1LemmaPOS: quello_V, S0B1POS: PD_V, S0B1POSLemma: PD_appartenere, S0B1Token: quelli_appartengono, S0Lemma: quello, S0POS: PD, S0Token: quelli, TransHistory3: 202, hasRighDep_mod_rel: true, quello_appartenere_hasRighDep_mod_rel: true, quello_hasRighDep_mod_rel: true, 

214- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [che, appartengono, alle ,.. ]

B0Lemma: che, B0POS: PR, B0Token: che, TransHistory3: 020, 

215- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [che]   B= [appartengono, alle, classi ,.. ]

B0Lemma: appartenere, B0POS: V, B0Token: appartengono, S0B0Lemma: che_appartenere, S0B0LemmaPOS: che_V, S0B0POS: PR_V, S0B0POSLemma: PR_appartenere, S0B0Token: che_appartengono, S0B1Lemma: che_al, S0B1LemmaPOS: che_EA, S0B1POS: PR_EA, S0B1POSLemma: PR_al, S0B1Token: che_alle, S0Lemma: che, S0POS: PR, S0Token: che, TransHistory3: 202, che_isGouvernedBy_appartenere: true, che_isGouvernedBy_appartenere_subj: true, 

216- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [appartengono, alle, classi ,.. ]

B0Lemma: appartenere, B0POS: V, B0Token: appartengono, TransHistory3: 020, 

217- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [appartengono]   B= [alle, classi, sociali ,.. ]

B0Lemma: al, B0POS: EA, B0Token: alle, S0B0Lemma: appartenere_al, S0B0LemmaPOS: appartenere_EA, S0B0POS: V_EA, S0B0POSLemma: V_al, S0B0Token: appartengono_alle, S0B1Lemma: appartenere_classe, S0B1LemmaPOS: appartenere_S, S0B1POS: V_S, S0B1POSLemma: V_classe, S0B1Token: appartengono_classi, S0Lemma: appartenere, S0POS: V, S0Token: appartengono, TransHistory3: 202, appartenere_al_hasRighDep_comp_ind: true, appartenere_hasRighDep_comp_ind: true, appartenere_hasRighDep_mod: true, appartenere_nascere_hasRighDep_mod: true, hasRighDep_comp_ind: true, hasRighDep_mod: true, 

218- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [alle, classi, sociali ,.. ]

B0Lemma: al, B0POS: EA, B0Token: alle, TransHistory3: 020, 

219- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [alle]   B= [classi, sociali, inferiori ,.. ]

B0Lemma: classe, B0POS: S, B0Token: classi, S0B0Lemma: al_classe, S0B0LemmaPOS: al_S, S0B0POS: EA_S, S0B0POSLemma: EA_classe, S0B0Token: alle_classi, S0B1Lemma: al_sociale, S0B1LemmaPOS: al_A, S0B1POS: EA_A, S0B1POSLemma: EA_sociale, S0B1Token: alle_sociali, S0Lemma: al, S0POS: EA, S0Token: alle, TransHistory3: 202, al_classe_hasRighDep_prep: true, al_hasRighDep_prep: true, hasRighDep_prep: true, 

220- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [classi, sociali, inferiori ,.. ]

B0Lemma: classe, B0POS: S, B0Token: classi, TransHistory3: 020, 

221- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [classi]   B= [sociali, inferiori, , ,.. ]

B0Lemma: sociale, B0POS: A, B0Token: sociali, S0B0Lemma: classe_sociale, S0B0LemmaPOS: classe_A, S0B0POS: S_A, S0B0POSLemma: S_sociale, S0B0Token: classi_sociali, S0B1Lemma: classe_inferiore, S0B1LemmaPOS: classe_A, S0B1POS: S_A, S0B1POSLemma: S_inferiore, S0B1Token: classi_inferiori, S0Lemma: classe, S0POS: S, S0Token: classi, TransHistory3: 202, classe_hasRighDep_mod: true, classe_inferiore_hasRighDep_mod: true, classe_sociale_hasRighDep_mod: true, hasRighDep_mod: true, 

222- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [sociali, inferiori, , ,.. ]

B0Lemma: sociale, B0POS: A, B0Token: sociali, TransHistory3: 020, 

223- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [sociali]   B= [inferiori, ,, nasce ,.. ]

B0Lemma: inferiore, B0POS: A, B0Token: inferiori, S0B0Lemma: sociale_inferiore, S0B0LemmaPOS: sociale_A, S0B0POS: A_A, S0B0POSLemma: A_inferiore, S0B0Token: sociali_inferiori, S0B1Lemma: sociale_,, S0B1LemmaPOS: sociale_FF, S0B1POS: A_FF, S0B1POSLemma: A_,, S0B1Token: sociali_,, S0Lemma: sociale, S0POS: A, S0Token: sociali, TransHistory3: 202, 

224- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [inferiori, ,, nasce ,.. ]

B0Lemma: inferiore, B0POS: A, B0Token: inferiori, TransHistory3: 020, 

225- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [inferiori]   B= [,, nasce, dall' ,.. ]

B0Lemma: ,, B0POS: FF, B0Token: ,, S0B0Lemma: inferiore_,, S0B0LemmaPOS: inferiore_FF, S0B0POS: A_FF, S0B0POSLemma: A_,, S0B0Token: inferiori_,, S0B1Lemma: inferiore_nascere, S0B1LemmaPOS: inferiore_V, S0B1POS: A_V, S0B1POSLemma: A_nascere, S0B1Token: inferiori_nasce, S0Lemma: inferiore, S0POS: A, S0Token: inferiori, TransHistory3: 202, 

226- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, nasce, dall' ,.. ]

B0Lemma: ,, B0POS: FF, B0Token: ,, TransHistory3: 020, 

227- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [nasce, dall', avere ,.. ]

,_isGouvernedBy_nascere: true, ,_isGouvernedBy_nascere_punc: true, B0Lemma: nascere, B0POS: V, B0Token: nasce, S0B0Lemma: ,_nascere, S0B0LemmaPOS: ,_V, S0B0POS: FF_V, S0B0POSLemma: FF_nascere, S0B0Token: ,_nasce, S0B1Lemma: ,_da, S0B1LemmaPOS: ,_EA, S0B1POS: FF_EA, S0B1POSLemma: FF_da, S0B1Token: ,_dall', S0Lemma: ,, S0POS: FF, S0Token: ,, TransHistory3: 202, 

228- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [nasce, dall', avere ,.. ]

B0Lemma: nascere, B0POS: V, B0Token: nasce, TransHistory3: 020, 

229- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [nasce]   B= [dall', avere, messo ,.. ]

B0Lemma: da, B0POS: EA, B0Token: dall', S0B0Lemma: nascere_da, S0B0LemmaPOS: nascere_EA, S0B0POS: V_EA, S0B0POSLemma: V_da, S0B0Token: nasce_dall', S0B1Lemma: nascere_avere, S0B1LemmaPOS: nascere_VA, S0B1POS: V_VA, S0B1POSLemma: V_avere, S0B1Token: nasce_avere, S0Lemma: nascere, S0POS: V, S0Token: nasce, TransHistory3: 202, hasRighDep_comp: true, nascere_da_hasRighDep_comp: true, nascere_hasRighDep_comp: true, 

230- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [dall', avere, messo ,.. ]

B0Lemma: da, B0POS: EA, B0Token: dall', TransHistory3: 020, 

231- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [dall']   B= [avere, messo, in ,.. ]

B0Lemma: avere, B0POS: VA, B0Token: avere, S0B0Lemma: da_avere, S0B0LemmaPOS: da_VA, S0B0POS: EA_VA, S0B0POSLemma: EA_avere, S0B0Token: dall'_avere, S0B1Lemma: da_mettere, S0B1LemmaPOS: da_V, S0B1POS: EA_V, S0B1POSLemma: EA_mettere, S0B1Token: dall'_messo, S0Lemma: da, S0POS: EA, S0Token: dall', TransHistory3: 202, da_hasRighDep_prep: true, da_mettere_hasRighDep_prep: true, hasRighDep_prep: true, 

232- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [avere, messo, in ,.. ]

B0Lemma: avere, B0POS: VA, B0Token: avere, TransHistory3: 020, 

233- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [avere]   B= [messo, in, dubbio ,.. ]

B0Lemma: mettere, B0POS: V, B0Token: messo, S0B0Lemma: avere_mettere, S0B0LemmaPOS: avere_V, S0B0POS: VA_V, S0B0POSLemma: VA_mettere, S0B0Token: avere_messo, S0B1Lemma: avere_in, S0B1LemmaPOS: avere_E, S0B1POS: VA_E, S0B1POSLemma: VA_in, S0B1Token: avere_in, S0Lemma: avere, S0POS: VA, S0Token: avere, TransHistory3: 202, avere_isGouvernedBy_mettere: true, avere_isGouvernedBy_mettere_aux: true, 

234- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [messo, in, dubbio ,.. ]

B0Lemma: mettere, B0POS: V, B0Token: messo, TransHistory3: 020, 

235- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [messo]   B= [in, dubbio, , ,.. ]

B0Lemma: in, B0POS: E, B0Token: in, S0B0Lemma: mettere_in, S0B0LemmaPOS: mettere_E, S0B0POS: V_E, S0B0POSLemma: V_in, S0B0Token: messo_in, S0B1Lemma: mettere_dubbio, S0B1LemmaPOS: mettere_S, S0B1POS: V_S, S0B1POSLemma: V_dubbio, S0B1Token: messo_dubbio, S0Lemma: mettere, S0POS: V, S0Token: messo, TransHistory3: 202, hasRighDep_comp: true, hasRighDep_con: true, hasRighDep_obj: true, mettere_,_hasRighDep_con: true, mettere_hasRighDep_comp: true, mettere_hasRighDep_con: true, mettere_hasRighDep_obj: true, mettere_in_hasRighDep_comp: true, mettere_vita_hasRighDep_obj: true, 

236- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [messo, in]   B= [dubbio, ,, nello ,.. ]

B0Lemma: dubbio, B0POS: S, B0Token: dubbio, S0B0Lemma: in_dubbio, S0B0LemmaPOS: in_S, S0B0POS: E_S, S0B0POSLemma: E_dubbio, S0B0Token: in_dubbio, S0B1Lemma: in_,, S0B1LemmaPOS: in_FF, S0B1POS: E_FF, S0B1POSLemma: E_,, S0B1Token: in_,, S0Lemma: in, S0POS: E, S0S1Distance: 1, S0Token: in, S1B0Lemma: mettere_dubbio, S1B0LemmaPOS: mettere_S, S1B0POS: V_S, S1B0POSLemma: V_dubbio, S1B0Token: messo_dubbio, S1Lemma: mettere, S1POS: V, S1S0Lemma: mettere_in, S1S0LemmaPOS: mettere_E, S1S0POS: V_E, S1S0POSLemma: V_in, S1S0Token: messo_in, S1Token: messo, SyntaxicRelation: +comp, TransHistory3: 020, hasRighDep_prep: true, in_dubbio_hasRighDep_prep: true, in_hasRighDep_prep: true, 

237- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [messo, in, dubbio]   B= [,, nello, stesso ,.. ]

B0Lemma: ,, B0POS: FF, B0Token: ,, S0B0Lemma: dubbio_,, S0B0LemmaPOS: dubbio_FF, S0B0POS: S_FF, S0B0POSLemma: S_,, S0B0Token: dubbio_,, S0B1Lemma: dubbio_in, S0B1LemmaPOS: dubbio_EA, S0B1POS: S_EA, S0B1POSLemma: S_in, S0B1Token: dubbio_nello, S0Lemma: dubbio, S0POS: S, S0S1Distance: 1, S0Token: dubbio, S1B0Lemma: in_,, S1B0LemmaPOS: in_FF, S1B0POS: E_FF, S1B0POSLemma: E_,, S1B0Token: in_,, S1Lemma: in, S1POS: E, S1S0Lemma: in_dubbio, S1S0LemmaPOS: in_S, S1S0POS: E_S, S1S0POSLemma: E_dubbio, S1S0Token: in_dubbio, S1Token: in, SyntaxicRelation: +prep, TransHistory3: 002, 

238- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [messo, [in, dubbio]]   B= [,, nello, stesso ,.. ]

B0Lemma: ,, B0POS: FF, B0Token: ,, S0B0Lemma: in_dubbio_,, S0B0LemmaPOS: in_dubbio_FF, S0B0POS: E_S_FF, S0B0POSLemma: E_S_,, S0B0Token: in_dubbio_,, S0B1Lemma: in_dubbio_in, S0B1LemmaPOS: in_dubbio_EA, S0B1POS: E_S_EA, S0B1POSLemma: E_S_in, S0B1Token: in_dubbio_nello, S0Lemma: in_dubbio, S0POS: E_S, S0Token: in_dubbio, S1B0Lemma: mettere_,, S1B0LemmaPOS: mettere_FF, S1B0POS: V_FF, S1B0POSLemma: V_,, S1B0Token: messo_,, S1Lemma: mettere, S1POS: V, S1S0Lemma: mettere_in_dubbio, S1S0LemmaPOS: mettere_E_S, S1S0POS: V_E_S, S1S0POSLemma: V_in_dubbio, S1S0Token: messo_in_dubbio, S1Token: messo, TransHistory3: 000, 

239- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[messo, [in, dubbio]]]   B= [,, nello, stesso ,.. ]

B0Lemma: ,, B0POS: FF, B0Token: ,, S0B0Lemma: mettere_in_dubbio_,, S0B0LemmaPOS: mettere_in_dubbio_FF, S0B0POS: V_E_S_FF, S0B0POSLemma: V_E_S_,, S0B0Token: messo_in_dubbio_,, S0B1Lemma: mettere_in_dubbio_in, S0B1LemmaPOS: mettere_in_dubbio_EA, S0B1POS: V_E_S_EA, S0B1POSLemma: V_E_S_in, S0B1Token: messo_in_dubbio_nello, S0Lemma: mettere_in_dubbio, S0POS: V_E_S, S0Token: messo_in_dubbio, TransHistory3: 100, 

240- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, nello, stesso ,.. ]

B0Lemma: ,, B0POS: FF, B0Token: ,, TransHistory3: 110, 

241- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [nello, stesso, tempo ,.. ]

B0Lemma: in, B0POS: EA, B0Token: nello, S0B0Lemma: ,_in, S0B0LemmaPOS: ,_EA, S0B0POS: FF_EA, S0B0POSLemma: FF_in, S0B0Token: ,_nello, S0B1Lemma: ,_stesso, S0B1LemmaPOS: ,_A, S0B1POS: FF_A, S0B1POSLemma: FF_stesso, S0B1Token: ,_stesso, S0Lemma: ,, S0POS: FF, S0Token: ,, TransHistory3: 211, 

242- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [nello, stesso, tempo ,.. ]

B0Lemma: in, B0POS: EA, B0Token: nello, TransHistory3: 021, 

243- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [nello]   B= [stesso, tempo, , ,.. ]

B0Lemma: stesso, B0POS: A, B0Token: stesso, S0B0Lemma: in_stesso, S0B0LemmaPOS: in_A, S0B0POS: EA_A, S0B0POSLemma: EA_stesso, S0B0Token: nello_stesso, S0B1Lemma: in_tempo, S0B1LemmaPOS: in_S, S0B1POS: EA_S, S0B1POSLemma: EA_tempo, S0B1Token: nello_tempo, S0Lemma: in, S0POS: EA, S0Token: nello, TransHistory3: 202, hasRighDep_prep: true, hasRighDep_punc: true, in_,_hasRighDep_punc: true, in_hasRighDep_prep: true, in_hasRighDep_punc: true, in_tempo_hasRighDep_prep: true, 

244- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [stesso, tempo, , ,.. ]

B0Lemma: stesso, B0POS: A, B0Token: stesso, TransHistory3: 020, 

245- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [stesso]   B= [tempo, ,, la ,.. ]

B0Lemma: tempo, B0POS: S, B0Token: tempo, S0B0Lemma: stesso_tempo, S0B0LemmaPOS: stesso_S, S0B0POS: A_S, S0B0POSLemma: A_tempo, S0B0Token: stesso_tempo, S0B1Lemma: stesso_,, S0B1LemmaPOS: stesso_FF, S0B1POS: A_FF, S0B1POSLemma: A_,, S0B1Token: stesso_,, S0Lemma: stesso, S0POS: A, S0Token: stesso, TransHistory3: 202, stesso_isGouvernedBy_tempo: true, stesso_isGouvernedBy_tempo_mod: true, 

246- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [tempo, ,, la ,.. ]

B0Lemma: tempo, B0POS: S, B0Token: tempo, TransHistory3: 020, 

247- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [tempo]   B= [,, la, vita ,.. ]

B0Lemma: ,, B0POS: FF, B0Token: ,, S0B0Lemma: tempo_,, S0B0LemmaPOS: tempo_FF, S0B0POS: S_FF, S0B0POSLemma: S_,, S0B0Token: tempo_,, S0B1Lemma: tempo_il, S0B1LemmaPOS: tempo_RD, S0B1POS: S_RD, S0B1POSLemma: S_il, S0B1Token: tempo_la, S0Lemma: tempo, S0POS: S, S0Token: tempo, TransHistory3: 202, 

248- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, la, vita ,.. ]

B0Lemma: ,, B0POS: FF, B0Token: ,, TransHistory3: 020, 

249- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [la, vita, del ,.. ]

B0Lemma: il, B0POS: RD, B0Token: la, S0B0Lemma: ,_il, S0B0LemmaPOS: ,_RD, S0B0POS: FF_RD, S0B0POSLemma: FF_il, S0B0Token: ,_la, S0B1Lemma: ,_vita, S0B1LemmaPOS: ,_S, S0B1POS: FF_S, S0B1POSLemma: FF_vita, S0B1Token: ,_vita, S0Lemma: ,, S0POS: FF, S0Token: ,, TransHistory3: 202, 

250- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [la, vita, del ,.. ]

B0Lemma: il, B0POS: RD, B0Token: la, TransHistory3: 020, 

251- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [la]   B= [vita, del, pianeta ,.. ]

B0Lemma: vita, B0POS: S, B0Token: vita, S0B0Lemma: il_vita, S0B0LemmaPOS: il_S, S0B0POS: RD_S, S0B0POSLemma: RD_vita, S0B0Token: la_vita, S0B1Lemma: il_di, S0B1LemmaPOS: il_EA, S0B1POS: RD_EA, S0B1POSLemma: RD_di, S0B1Token: la_del, S0Lemma: il, S0POS: RD, S0Token: la, TransHistory3: 202, il_isGouvernedBy_vita: true, il_isGouvernedBy_vita_det: true, 

252- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [vita, del, pianeta ,.. ]

B0Lemma: vita, B0POS: S, B0Token: vita, TransHistory3: 020, 

253- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [vita]   B= [del, pianeta, ed ,.. ]

B0Lemma: di, B0POS: EA, B0Token: del, S0B0Lemma: vita_di, S0B0LemmaPOS: vita_EA, S0B0POS: S_EA, S0B0POSLemma: S_di, S0B0Token: vita_del, S0B1Lemma: vita_pianeta, S0B1LemmaPOS: vita_S, S0B1POS: S_S, S0B1POSLemma: S_pianeta, S0B1Token: vita_pianeta, S0Lemma: vita, S0POS: S, S0Token: vita, TransHistory3: 202, hasRighDep_comp: true, hasRighDep_con: true, hasRighDep_conj: true, vita_di_hasRighDep_comp: true, vita_ed_hasRighDep_con: true, vita_futuro_hasRighDep_conj: true, vita_hasRighDep_comp: true, vita_hasRighDep_con: true, vita_hasRighDep_conj: true, 

254- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [del, pianeta, ed ,.. ]

B0Lemma: di, B0POS: EA, B0Token: del, TransHistory3: 020, 

255- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [del]   B= [pianeta, ed, il ,.. ]

B0Lemma: pianeta, B0POS: S, B0Token: pianeta, S0B0Lemma: di_pianeta, S0B0LemmaPOS: di_S, S0B0POS: EA_S, S0B0POSLemma: EA_pianeta, S0B0Token: del_pianeta, S0B1Lemma: di_ed, S0B1LemmaPOS: di_CC, S0B1POS: EA_CC, S0B1POSLemma: EA_ed, S0B1Token: del_ed, S0Lemma: di, S0POS: EA, S0Token: del, TransHistory3: 202, di_hasRighDep_prep: true, di_pianeta_hasRighDep_prep: true, hasRighDep_prep: true, 

256- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [pianeta, ed, il ,.. ]

B0Lemma: pianeta, B0POS: S, B0Token: pianeta, TransHistory3: 020, 

257- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [pianeta]   B= [ed, il, futuro ,.. ]

B0Lemma: ed, B0POS: CC, B0Token: ed, S0B0Lemma: pianeta_ed, S0B0LemmaPOS: pianeta_CC, S0B0POS: S_CC, S0B0POSLemma: S_ed, S0B0Token: pianeta_ed, S0B1Lemma: pianeta_il, S0B1LemmaPOS: pianeta_RD, S0B1POS: S_RD, S0B1POSLemma: S_il, S0B1Token: pianeta_il, S0Lemma: pianeta, S0POS: S, S0Token: pianeta, TransHistory3: 202, 

258- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ed, il, futuro ,.. ]

B0Lemma: ed, B0POS: CC, B0Token: ed, TransHistory3: 020, 

259- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ed]   B= [il, futuro, di ,.. ]

B0Lemma: il, B0POS: RD, B0Token: il, S0B0Lemma: ed_il, S0B0LemmaPOS: ed_RD, S0B0POS: CC_RD, S0B0POSLemma: CC_il, S0B0Token: ed_il, S0B1Lemma: ed_futuro, S0B1LemmaPOS: ed_S, S0B1POS: CC_S, S0B1POSLemma: CC_futuro, S0B1Token: ed_futuro, S0Lemma: ed, S0POS: CC, S0Token: ed, TransHistory3: 202, 

260- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [il, futuro, di ,.. ]

B0Lemma: il, B0POS: RD, B0Token: il, TransHistory3: 020, 

261- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [il]   B= [futuro, di, tutta ,.. ]

B0Lemma: futuro, B0POS: S, B0Token: futuro, S0B0Lemma: il_futuro, S0B0LemmaPOS: il_S, S0B0POS: RD_S, S0B0POSLemma: RD_futuro, S0B0Token: il_futuro, S0B1Lemma: il_di, S0B1LemmaPOS: il_E, S0B1POS: RD_E, S0B1POSLemma: RD_di, S0B1Token: il_di, S0Lemma: il, S0POS: RD, S0Token: il, TransHistory3: 202, il_isGouvernedBy_futuro: true, il_isGouvernedBy_futuro_det: true, 

262- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [futuro, di, tutta ,.. ]

B0Lemma: futuro, B0POS: S, B0Token: futuro, TransHistory3: 020, 

263- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [futuro]   B= [di, tutta, l' ,.. ]

B0Lemma: di, B0POS: E, B0Token: di, S0B0Lemma: futuro_di, S0B0LemmaPOS: futuro_E, S0B0POS: S_E, S0B0POSLemma: S_di, S0B0Token: futuro_di, S0B1Lemma: futuro_tutto, S0B1LemmaPOS: futuro_T, S0B1POS: S_T, S0B1POSLemma: S_tutto, S0B1Token: futuro_tutta, S0Lemma: futuro, S0POS: S, S0Token: futuro, TransHistory3: 202, futuro_di_hasRighDep_comp: true, futuro_hasRighDep_comp: true, hasRighDep_comp: true, 

264- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [di, tutta, l' ,.. ]

B0Lemma: di, B0POS: E, B0Token: di, TransHistory3: 020, 

265- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [di]   B= [tutta, l', umanità ,.. ]

B0Lemma: tutto, B0POS: T, B0Token: tutta, S0B0Lemma: di_tutto, S0B0LemmaPOS: di_T, S0B0POS: E_T, S0B0POSLemma: E_tutto, S0B0Token: di_tutta, S0B1Lemma: di_il, S0B1LemmaPOS: di_RD, S0B1POS: E_RD, S0B1POSLemma: E_il, S0B1Token: di_l', S0Lemma: di, S0POS: E, S0Token: di, TransHistory3: 202, di_hasRighDep_prep: true, di_umanità_hasRighDep_prep: true, hasRighDep_prep: true, 

266- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [tutta, l', umanità ,.. ]

B0Lemma: tutto, B0POS: T, B0Token: tutta, TransHistory3: 020, 

267- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [tutta]   B= [l', umanità, . ,.. ]

B0Lemma: il, B0POS: RD, B0Token: l', S0B0Lemma: tutto_il, S0B0LemmaPOS: tutto_RD, S0B0POS: T_RD, S0B0POSLemma: T_il, S0B0Token: tutta_l', S0B1Lemma: tutto_umanità, S0B1LemmaPOS: tutto_S, S0B1POS: T_S, S0B1POSLemma: T_umanità, S0B1Token: tutta_umanità, S0Lemma: tutto, S0POS: T, S0Token: tutta, TransHistory3: 202, tutto_isGouvernedBy_umanità: true, tutto_isGouvernedBy_umanità_mod: true, 

268- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [l', umanità, . ,.. ]

B0Lemma: il, B0POS: RD, B0Token: l', TransHistory3: 020, 

269- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [l']   B= [umanità, . ,.. ]

B0Lemma: umanità, B0POS: S, B0Token: umanità, S0B0Lemma: il_umanità, S0B0LemmaPOS: il_S, S0B0POS: RD_S, S0B0POSLemma: RD_umanità, S0B0Token: l'_umanità, S0B1Lemma: il_., S0B1LemmaPOS: il_FS, S0B1POS: RD_FS, S0B1POSLemma: RD_., S0B1Token: l'_., S0Lemma: il, S0POS: RD, S0Token: l', TransHistory3: 202, il_isGouvernedBy_umanità: true, il_isGouvernedBy_umanità_det: true, 

270- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [umanità, . ,.. ]

B0Lemma: umanità, B0POS: S, B0Token: umanità, TransHistory3: 020, 

271- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [umanità]   B= [.]

B0Lemma: ., B0POS: FS, B0Token: ., S0B0Lemma: umanità_., S0B0LemmaPOS: umanità_FS, S0B0POS: S_FS, S0B0POSLemma: S_., S0B0Token: umanità_., S0Lemma: umanità, S0POS: S, S0Token: umanità, TransHistory3: 202, 

272- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [.]

B0Lemma: ., B0POS: FS, B0Token: ., TransHistory3: 020, 

273- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [ ]

S0Lemma: ., S0POS: FS, S0Token: ., TransHistory3: 202, 

274- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

## Sentence No. 302 - 
ci rispondiamo sempre che tanto loro hanno i soldi e noi ci spacchiamo la testa dietro alla crisi . 
### Existing MWEs: 
1- **ci spacchiamo la testa** (ID)
2- **ci spacchiamo** (IReflV), Embedded



0- &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ci, rispondiamo, sempre ,.. ]

B0Lemma: ci, B0POS: PC, B0Token: ci, 

1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ci]   B= [rispondiamo, sempre, che ,.. ]

B0Lemma: rispondere, B0POS: V, B0Token: rispondiamo, S0B0Lemma: ci_rispondere, S0B0LemmaPOS: ci_V, S0B0POS: PC_V, S0B0POSLemma: PC_rispondere, S0B0Token: ci_rispondiamo, S0B1Lemma: ci_sempre, S0B1LemmaPOS: ci_B, S0B1POS: PC_B, S0B1POSLemma: PC_sempre, S0B1Token: ci_sempre, S0Lemma: ci, S0POS: PC, S0Token: ci, ci_isGouvernedBy_rispondere: true, ci_isGouvernedBy_rispondere_comp: true, 

2- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [rispondiamo, sempre, che ,.. ]

B0Lemma: rispondere, B0POS: V, B0Token: rispondiamo, 

3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [rispondiamo]   B= [sempre, che, tanto ,.. ]

B0Lemma: sempre, B0POS: B, B0Token: sempre, S0B0Lemma: rispondere_sempre, S0B0LemmaPOS: rispondere_B, S0B0POS: V_B, S0B0POSLemma: V_sempre, S0B0Token: rispondiamo_sempre, S0B1Lemma: rispondere_che, S0B1LemmaPOS: rispondere_CC, S0B1POS: V_CC, S0B1POSLemma: V_che, S0B1Token: rispondiamo_che, S0Lemma: rispondere, S0POS: V, S0Token: rispondiamo, 

4- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [sempre, che, tanto ,.. ]

B0Lemma: sempre, B0POS: B, B0Token: sempre, TransHistory3: 020, 

5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [sempre]   B= [che, tanto, loro ,.. ]

B0Lemma: che, B0POS: CC, B0Token: che, S0B0Lemma: sempre_che, S0B0LemmaPOS: sempre_CC, S0B0POS: B_CC, S0B0POSLemma: B_che, S0B0Token: sempre_che, S0B1Lemma: sempre_tanto, S0B1LemmaPOS: sempre_B, S0B1POS: B_B, S0B1POSLemma: B_tanto, S0B1Token: sempre_tanto, S0Lemma: sempre, S0POS: B, S0Token: sempre, TransHistory3: 202, hasRighDep_con: true, hasRighDep_mod: true, sempre_che_hasRighDep_con: true, sempre_hasRighDep_con: true, sempre_hasRighDep_mod: true, sempre_tanto_hasRighDep_mod: true, 

6- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [che, tanto, loro ,.. ]

B0Lemma: che, B0POS: CC, B0Token: che, TransHistory3: 020, 

7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [che]   B= [tanto, loro, hanno ,.. ]

B0Lemma: tanto, B0POS: B, B0Token: tanto, S0B0Lemma: che_tanto, S0B0LemmaPOS: che_B, S0B0POS: CC_B, S0B0POSLemma: CC_tanto, S0B0Token: che_tanto, S0B1Lemma: che_loro, S0B1LemmaPOS: che_PE, S0B1POS: CC_PE, S0B1POSLemma: CC_loro, S0B1Token: che_loro, S0Lemma: che, S0POS: CC, S0Token: che, TransHistory3: 202, 

8- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [tanto, loro, hanno ,.. ]

B0Lemma: tanto, B0POS: B, B0Token: tanto, TransHistory3: 020, 

9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [tanto]   B= [loro, hanno, i ,.. ]

B0Lemma: loro, B0POS: PE, B0Token: loro, S0B0Lemma: tanto_loro, S0B0LemmaPOS: tanto_PE, S0B0POS: B_PE, S0B0POSLemma: B_loro, S0B0Token: tanto_loro, S0B1Lemma: tanto_avere, S0B1LemmaPOS: tanto_VA, S0B1POS: B_VA, S0B1POSLemma: B_avere, S0B1Token: tanto_hanno, S0Lemma: tanto, S0POS: B, S0Token: tanto, TransHistory3: 202, hasRighDep_mod: true, tanto_hasRighDep_mod: true, tanto_loro_hasRighDep_mod: true, 

10- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [loro, hanno, i ,.. ]

B0Lemma: loro, B0POS: PE, B0Token: loro, TransHistory3: 020, 

11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [loro]   B= [hanno, i, soldi ,.. ]

B0Lemma: avere, B0POS: VA, B0Token: hanno, S0B0Lemma: loro_avere, S0B0LemmaPOS: loro_VA, S0B0POS: PE_VA, S0B0POSLemma: PE_avere, S0B0Token: loro_hanno, S0B1Lemma: loro_il, S0B1LemmaPOS: loro_RD, S0B1POS: PE_RD, S0B1POSLemma: PE_il, S0B1Token: loro_i, S0Lemma: loro, S0POS: PE, S0Token: loro, TransHistory3: 202, 

12- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [hanno, i, soldi ,.. ]

B0Lemma: avere, B0POS: VA, B0Token: hanno, TransHistory3: 020, 

13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [hanno]   B= [i, soldi, e ,.. ]

B0Lemma: il, B0POS: RD, B0Token: i, S0B0Lemma: avere_il, S0B0LemmaPOS: avere_RD, S0B0POS: VA_RD, S0B0POSLemma: VA_il, S0B0Token: hanno_i, S0B1Lemma: avere_soldo, S0B1LemmaPOS: avere_S, S0B1POS: VA_S, S0B1POSLemma: VA_soldo, S0B1Token: hanno_soldi, S0Lemma: avere, S0POS: VA, S0Token: hanno, TransHistory3: 202, avere_hasRighDep_obj: true, avere_soldo_hasRighDep_obj: true, hasRighDep_obj: true, 

14- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [i, soldi, e ,.. ]

B0Lemma: il, B0POS: RD, B0Token: i, TransHistory3: 020, 

15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [i]   B= [soldi, e, noi ,.. ]

B0Lemma: soldo, B0POS: S, B0Token: soldi, S0B0Lemma: il_soldo, S0B0LemmaPOS: il_S, S0B0POS: RD_S, S0B0POSLemma: RD_soldo, S0B0Token: i_soldi, S0B1Lemma: il_e, S0B1LemmaPOS: il_CC, S0B1POS: RD_CC, S0B1POSLemma: RD_e, S0B1Token: i_e, S0Lemma: il, S0POS: RD, S0Token: i, TransHistory3: 202, il_isGouvernedBy_soldo: true, il_isGouvernedBy_soldo_det: true, 

16- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [soldi, e, noi ,.. ]

B0Lemma: soldo, B0POS: S, B0Token: soldi, TransHistory3: 020, 

17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [soldi]   B= [e, noi, ci ,.. ]

B0Lemma: e, B0POS: CC, B0Token: e, S0B0Lemma: soldo_e, S0B0LemmaPOS: soldo_CC, S0B0POS: S_CC, S0B0POSLemma: S_e, S0B0Token: soldi_e, S0B1Lemma: soldo_noi, S0B1LemmaPOS: soldo_PE, S0B1POS: S_PE, S0B1POSLemma: S_noi, S0B1Token: soldi_noi, S0Lemma: soldo, S0POS: S, S0Token: soldi, TransHistory3: 202, 

18- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [e, noi, ci ,.. ]

B0Lemma: e, B0POS: CC, B0Token: e, TransHistory3: 020, 

19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [e]   B= [noi, ci, spacchiamo ,.. ]

B0Lemma: noi, B0POS: PE, B0Token: noi, S0B0Lemma: e_noi, S0B0LemmaPOS: e_PE, S0B0POS: CC_PE, S0B0POSLemma: CC_noi, S0B0Token: e_noi, S0B1Lemma: e_ci, S0B1LemmaPOS: e_PC, S0B1POS: CC_PC, S0B1POSLemma: CC_ci, S0B1Token: e_ci, S0Lemma: e, S0POS: CC, S0Token: e, TransHistory3: 202, 

20- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [noi, ci, spacchiamo ,.. ]

B0Lemma: noi, B0POS: PE, B0Token: noi, TransHistory3: 020, 

21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [noi]   B= [ci, spacchiamo, la ,.. ]

B0Lemma: ci, B0POS: PC, B0Token: ci, S0B0Lemma: noi_ci, S0B0LemmaPOS: noi_PC, S0B0POS: PE_PC, S0B0POSLemma: PE_ci, S0B0Token: noi_ci, S0B1Lemma: noi_spaccare, S0B1LemmaPOS: noi_V, S0B1POS: PE_V, S0B1POSLemma: PE_spaccare, S0B1Token: noi_spacchiamo, S0Lemma: noi, S0POS: PE, S0Token: noi, TransHistory3: 202, noi_isGouvernedBy_spaccare: true, noi_isGouvernedBy_spaccare_subj: true, 

22- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ci, spacchiamo, la ,.. ]

B0Lemma: ci, B0POS: PC, B0Token: ci, TransHistory3: 020, 

23- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ci]   B= [spacchiamo, la, testa ,.. ]

B0Lemma: spaccare, B0POS: V, B0Token: spacchiamo, S0B0Lemma: ci_spaccare, S0B0LemmaPOS: ci_V, S0B0POS: PC_V, S0B0POSLemma: PC_spaccare, S0B0Token: ci_spacchiamo, S0B1Lemma: ci_il, S0B1LemmaPOS: ci_RD, S0B1POS: PC_RD, S0B1POSLemma: PC_il, S0B1Token: ci_la, S0Lemma: ci, S0POS: PC, S0Token: ci, TransHistory3: 202, ci_isGouvernedBy_spaccare: true, ci_isGouvernedBy_spaccare_comp: true, 

24- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ci, spacchiamo]   B= [la, testa, dietro ,.. ]

B0Lemma: il, B0POS: RD, B0Token: la, S0B0Lemma: spaccare_il, S0B0LemmaPOS: spaccare_RD, S0B0POS: V_RD, S0B0POSLemma: V_il, S0B0Token: spacchiamo_la, S0B1Lemma: spaccare_testa, S0B1LemmaPOS: spaccare_S, S0B1POS: V_S, S0B1POSLemma: V_testa, S0B1Token: spacchiamo_testa, S0Lemma: spaccare, S0POS: V, S0S1Distance: 1, S0Token: spacchiamo, S1B0Lemma: ci_il, S1B0LemmaPOS: ci_RD, S1B0POS: PC_RD, S1B0POSLemma: PC_il, S1B0Token: ci_la, S1Lemma: ci, S1POS: PC, S1S0Lemma: ci_spaccare, S1S0LemmaPOS: ci_V, S1S0POS: PC_V, S1S0POSLemma: PC_spaccare, S1S0Token: ci_spacchiamo, S1Token: ci, SyntaxicRelation: -comp, TransHistory3: 020, hasRighDep_comp: true, hasRighDep_mod: true, hasRighDep_obj: true, spaccare_al_hasRighDep_comp: true, spaccare_dietro_hasRighDep_mod: true, spaccare_hasRighDep_comp: true, spaccare_hasRighDep_mod: true, spaccare_hasRighDep_obj: true, spaccare_testa_hasRighDep_obj: true, 

25- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ci, spacchiamo, la]   B= [testa, dietro, alla ,.. ]

B0Lemma: testa, B0POS: S, B0Token: testa, S0B0Lemma: il_testa, S0B0LemmaPOS: il_S, S0B0POS: RD_S, S0B0POSLemma: RD_testa, S0B0Token: la_testa, S0B1Lemma: il_dietro, S0B1LemmaPOS: il_B, S0B1POS: RD_B, S0B1POSLemma: RD_dietro, S0B1Token: la_dietro, S0Lemma: il, S0POS: RD, S0S1Distance: 1, S0Token: la, S1B0Lemma: spaccare_testa, S1B0LemmaPOS: spaccare_S, S1B0POS: V_S, S1B0POSLemma: V_testa, S1B0Token: spacchiamo_testa, S1Lemma: spaccare, S1POS: V, S1S0Lemma: spaccare_il, S1S0LemmaPOS: spaccare_RD, S1S0POS: V_RD, S1S0POSLemma: V_il, S1S0Token: spacchiamo_la, S1Token: spacchiamo, TransHistory3: 002, il_isGouvernedBy_testa: true, il_isGouvernedBy_testa_det: true, 

26- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ci, spacchiamo, la, testa]   B= [dietro, alla, crisi ,.. ]

B0Lemma: dietro, B0POS: B, B0Token: dietro, S0B0Lemma: testa_dietro, S0B0LemmaPOS: testa_B, S0B0POS: S_B, S0B0POSLemma: S_dietro, S0B0Token: testa_dietro, S0B1Lemma: testa_al, S0B1LemmaPOS: testa_EA, S0B1POS: S_EA, S0B1POSLemma: S_al, S0B1Token: testa_alla, S0Lemma: testa, S0POS: S, S0S1Distance: 1, S0Token: testa, S1B0Lemma: il_dietro, S1B0LemmaPOS: il_B, S1B0POS: RD_B, S1B0POSLemma: RD_dietro, S1B0Token: la_dietro, S1Lemma: il, S1POS: RD, S1S0Lemma: il_testa, S1S0LemmaPOS: il_S, S1S0POS: RD_S, S1S0POSLemma: RD_testa, S1S0Token: la_testa, S1Token: la, SyntaxicRelation: -det, TransHistory3: 000, 

27- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ci, spacchiamo, [la, testa]]   B= [dietro, alla, crisi ,.. ]

B0Lemma: dietro, B0POS: B, B0Token: dietro, S0B0Lemma: il_testa_dietro, S0B0LemmaPOS: il_testa_B, S0B0POS: RD_S_B, S0B0POSLemma: RD_S_dietro, S0B0Token: la_testa_dietro, S0B1Lemma: il_testa_al, S0B1LemmaPOS: il_testa_EA, S0B1POS: RD_S_EA, S0B1POSLemma: RD_S_al, S0B1Token: la_testa_alla, S0Lemma: il_testa, S0POS: RD_S, S0Token: la_testa, S1B0Lemma: spaccare_dietro, S1B0LemmaPOS: spaccare_B, S1B0POS: V_B, S1B0POSLemma: V_dietro, S1B0Token: spacchiamo_dietro, S1Lemma: spaccare, S1POS: V, S1S0Lemma: spaccare_il_testa, S1S0LemmaPOS: spaccare_RD_S, S1S0POS: V_RD_S, S1S0POSLemma: V_il_testa, S1S0Token: spacchiamo_la_testa, S1Token: spacchiamo, TransHistory3: 000, 

28- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ci, [spacchiamo, [la, testa]]]   B= [dietro, alla, crisi ,.. ]

B0Lemma: dietro, B0POS: B, B0Token: dietro, S0B0Lemma: spaccare_il_testa_dietro, S0B0LemmaPOS: spaccare_il_testa_B, S0B0POS: V_RD_S_B, S0B0POSLemma: V_RD_S_dietro, S0B0Token: spacchiamo_la_testa_dietro, S0B1Lemma: spaccare_il_testa_al, S0B1LemmaPOS: spaccare_il_testa_EA, S0B1POS: V_RD_S_EA, S0B1POSLemma: V_RD_S_al, S0B1Token: spacchiamo_la_testa_alla, S0Lemma: spaccare_il_testa, S0POS: V_RD_S, S0Token: spacchiamo_la_testa, S1B0Lemma: ci_dietro, S1B0LemmaPOS: ci_B, S1B0POS: PC_B, S1B0POSLemma: PC_dietro, S1B0Token: ci_dietro, S1Lemma: ci, S1POS: PC, S1S0Lemma: ci_spaccare_il_testa, S1S0LemmaPOS: ci_V_RD_S, S1S0POS: PC_V_RD_S, S1S0POSLemma: PC_spaccare_il_testa, S1S0Token: ci_spacchiamo_la_testa, S1Token: ci, TransHistory3: 100, 

29- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[ci, [spacchiamo, [la, testa]]]]   B= [dietro, alla, crisi ,.. ]

B0Lemma: dietro, B0POS: B, B0Token: dietro, S0B0Lemma: ci_spaccare_il_testa_dietro, S0B0LemmaPOS: ci_spaccare_il_testa_B, S0B0POS: PC_V_RD_S_B, S0B0POSLemma: PC_V_RD_S_dietro, S0B0Token: ci_spacchiamo_la_testa_dietro, S0B1Lemma: ci_spaccare_il_testa_al, S0B1LemmaPOS: ci_spaccare_il_testa_EA, S0B1POS: PC_V_RD_S_EA, S0B1POSLemma: PC_V_RD_S_al, S0B1Token: ci_spacchiamo_la_testa_alla, S0Lemma: ci_spaccare_il_testa, S0POS: PC_V_RD_S, S0Token: ci_spacchiamo_la_testa, TransHistory3: 110, 

30- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [dietro, alla, crisi ,.. ]

B0Lemma: dietro, B0POS: B, B0Token: dietro, TransHistory3: 111, 

31- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [dietro]   B= [alla, crisi, . ,.. ]

B0Lemma: al, B0POS: EA, B0Token: alla, S0B0Lemma: dietro_al, S0B0LemmaPOS: dietro_EA, S0B0POS: B_EA, S0B0POSLemma: B_al, S0B0Token: dietro_alla, S0B1Lemma: dietro_crisi, S0B1LemmaPOS: dietro_S, S0B1POS: B_S, S0B1POSLemma: B_crisi, S0B1Token: dietro_crisi, S0Lemma: dietro, S0POS: B, S0Token: dietro, TransHistory3: 211, 

32- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [alla, crisi, . ,.. ]

B0Lemma: al, B0POS: EA, B0Token: alla, TransHistory3: 021, 

33- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [alla]   B= [crisi, . ,.. ]

B0Lemma: crisi, B0POS: S, B0Token: crisi, S0B0Lemma: al_crisi, S0B0LemmaPOS: al_S, S0B0POS: EA_S, S0B0POSLemma: EA_crisi, S0B0Token: alla_crisi, S0B1Lemma: al_., S0B1LemmaPOS: al_FS, S0B1POS: EA_FS, S0B1POSLemma: EA_., S0B1Token: alla_., S0Lemma: al, S0POS: EA, S0Token: alla, TransHistory3: 202, al_crisi_hasRighDep_prep: true, al_hasRighDep_prep: true, hasRighDep_prep: true, 

34- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [crisi, . ,.. ]

B0Lemma: crisi, B0POS: S, B0Token: crisi, TransHistory3: 020, 

35- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [crisi]   B= [.]

B0Lemma: ., B0POS: FS, B0Token: ., S0B0Lemma: crisi_., S0B0LemmaPOS: crisi_FS, S0B0POS: S_FS, S0B0POSLemma: S_., S0B0Token: crisi_., S0Lemma: crisi, S0POS: S, S0Token: crisi, TransHistory3: 202, 

36- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [.]

B0Lemma: ., B0POS: FS, B0Token: ., TransHistory3: 020, 

37- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [ ]

S0Lemma: ., S0POS: FS, S0Token: ., TransHistory3: 202, 

38- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

