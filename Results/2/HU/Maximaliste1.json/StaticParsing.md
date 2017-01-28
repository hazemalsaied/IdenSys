## Sentence No. 212 - 
ebből a túl általánosnak tűnő meghatározásból nehezen körvonalazható iratok körét szerintünk a gt. ( új ) 72. § (2) bekezdés és 77. § (2) bekezdéssel összhangban lehet értelmezni , ezért ezek az iratok az átalakulással összefüggő iratok körére terjedhetnek ki . 
### Existing MWEs: 
1- **bekezdés** (VPC)
2- **összefüggő** (VPC)



0- &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ebből, a, túl ,.. ]

B0Lemma: ez, B0POS: P, B0Token: ebből, B1Lemma: a, B1POS: T, B1Token: a, 

1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ebből]   B= [a, túl, általánosnak ,.. ]

B0Lemma: a, B0POS: T, B0Token: a, B1Lemma: túl, B1POS: R, B1Token: túl, S0B0Lemma: ez_a, S0B0LemmaPOS: ez_T, S0B0POS: P_T, S0B0POSLemma: P_a, S0B0Token: ebből_a, S0B1Lemma: ez_túl, S0B1LemmaPOS: ez_R, S0B1POS: P_R, S0B1POSLemma: P_túl, S0B1Token: ebből_túl, S0Lemma: ez, S0POS: P, S0Token: ebből, ez_isGouvernedBy_meghatározás: true, ez_isGouvernedBy_meghatározás_OBL: true, 

2- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [a, túl, általánosnak ,.. ]

B0Lemma: a, B0POS: T, B0Token: a, B1Lemma: túl, B1POS: R, B1Token: túl, TransHistory1: 0, 

3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [a]   B= [túl, általánosnak, tűnő ,.. ]

B0Lemma: túl, B0POS: R, B0Token: túl, B1Lemma: általános, B1POS: A, B1Token: általánosnak, S0B0Lemma: a_túl, S0B0LemmaPOS: a_R, S0B0POS: T_R, S0B0POSLemma: T_túl, S0B0Token: a_túl, S0B1Lemma: a_általános, S0B1LemmaPOS: a_A, S0B1POS: T_A, S0B1POSLemma: T_általános, S0B1Token: a_általánosnak, S0Lemma: a, S0POS: T, S0Token: a, TransHistory1: 2, TransHistory2: 20, a_isGouvernedBy_meghatározás: true, a_isGouvernedBy_meghatározás_DET: true, 

4- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [túl, általánosnak, tűnő ,.. ]

B0Lemma: túl, B0POS: R, B0Token: túl, B1Lemma: általános, B1POS: A, B1Token: általánosnak, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [túl]   B= [általánosnak, tűnő, meghatározásból ,.. ]

B0Lemma: általános, B0POS: A, B0Token: általánosnak, B1Lemma: tűnő, B1POS: A, B1Token: tűnő, S0B0Lemma: túl_általános, S0B0LemmaPOS: túl_A, S0B0POS: R_A, S0B0POSLemma: R_általános, S0B0Token: túl_általánosnak, S0B1Lemma: túl_tűnő, S0B1LemmaPOS: túl_A, S0B1POS: R_A, S0B1POSLemma: R_tűnő, S0B1Token: túl_tűnő, S0Lemma: túl, S0POS: R, S0Token: túl, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, túl_isGouvernedBy_tűnő: true, túl_isGouvernedBy_tűnő_MODE: true, 

6- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [általánosnak, tűnő, meghatározásból ,.. ]

B0Lemma: általános, B0POS: A, B0Token: általánosnak, B1Lemma: tűnő, B1POS: A, B1Token: tűnő, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [általánosnak]   B= [tűnő, meghatározásból, nehezen ,.. ]

B0Lemma: tűnő, B0POS: A, B0Token: tűnő, B1IsInLexic: true, B1Lemma: meghatározás, B1POS: N, B1Token: meghatározásból, S0B0Lemma: általános_tűnő, S0B0LemmaPOS: általános_A, S0B0POS: A_A, S0B0POSLemma: A_tűnő, S0B0Token: általánosnak_tűnő, S0B1Lemma: általános_meghatározás, S0B1LemmaPOS: általános_N, S0B1POS: A_N, S0B1POSLemma: A_meghatározás, S0B1Token: általánosnak_meghatározásból, S0Lemma: általános, S0POS: A, S0Token: általánosnak, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, általános_isGouvernedBy_tűnő: true, általános_isGouvernedBy_tűnő_ATT: true, 

8- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [tűnő, meghatározásból, nehezen ,.. ]

B0Lemma: tűnő, B0POS: A, B0Token: tűnő, B1IsInLexic: true, B1Lemma: meghatározás, B1POS: N, B1Token: meghatározásból, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [tűnő]   B= [meghatározásból, nehezen, körvonalazható ,.. ]

B0IsInLexic: true, B0Lemma: meghatározás, B0POS: N, B0Token: meghatározásból, B1Lemma: nehéz, B1POS: A, B1Token: nehezen, S0B0Lemma: tűnő_meghatározás, S0B0LemmaPOS: tűnő_N, S0B0POS: A_N, S0B0POSLemma: A_meghatározás, S0B0Token: tűnő_meghatározásból, S0B1Lemma: tűnő_nehéz, S0B1LemmaPOS: tűnő_A, S0B1POS: A_A, S0B1POSLemma: A_nehéz, S0B1Token: tűnő_nehezen, S0Lemma: tűnő, S0POS: A, S0Token: tűnő, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, tűnő_isGouvernedBy_meghatározás: true, tűnő_isGouvernedBy_meghatározás_ATT: true, 

10- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [meghatározásból, nehezen, körvonalazható ,.. ]

B0IsInLexic: true, B0Lemma: meghatározás, B0POS: N, B0Token: meghatározásból, B1Lemma: nehéz, B1POS: A, B1Token: nehezen, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [meghatározásból]   B= [nehezen, körvonalazható, iratok ,.. ]

B0Lemma: nehéz, B0POS: A, B0Token: nehezen, B1Lemma: körvonalazható, B1POS: A, B1Token: körvonalazható, S0B0Lemma: meghatározás_nehéz, S0B0LemmaPOS: meghatározás_A, S0B0POS: N_A, S0B0POSLemma: N_nehéz, S0B0Token: meghatározásból_nehezen, S0B1Lemma: meghatározás_körvonalazható, S0B1LemmaPOS: meghatározás_A, S0B1POS: N_A, S0B1POSLemma: N_körvonalazható, S0B1Token: meghatározásból_körvonalazható, S0IsInLexic: true, S0Lemma: meghatározás, S0POS: N, S0Token: meghatározásból, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, meghatározás_isGouvernedBy_körvonalazható: true, meghatározás_isGouvernedBy_körvonalazható_OBL: true, 

12- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [nehezen, körvonalazható, iratok ,.. ]

B0Lemma: nehéz, B0POS: A, B0Token: nehezen, B1Lemma: körvonalazható, B1POS: A, B1Token: körvonalazható, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [nehezen]   B= [körvonalazható, iratok, körét ,.. ]

B0Lemma: körvonalazható, B0POS: A, B0Token: körvonalazható, B1Lemma: irat, B1POS: N, B1Token: iratok, S0B0Lemma: nehéz_körvonalazható, S0B0LemmaPOS: nehéz_A, S0B0POS: A_A, S0B0POSLemma: A_körvonalazható, S0B0Token: nehezen_körvonalazható, S0B1Lemma: nehéz_irat, S0B1LemmaPOS: nehéz_N, S0B1POS: A_N, S0B1POSLemma: A_irat, S0B1Token: nehezen_iratok, S0Lemma: nehéz, S0POS: A, S0Token: nehezen, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, nehéz_isGouvernedBy_körvonalazható: true, nehéz_isGouvernedBy_körvonalazható_MODE: true, 

14- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [körvonalazható, iratok, körét ,.. ]

B0Lemma: körvonalazható, B0POS: A, B0Token: körvonalazható, B1Lemma: irat, B1POS: N, B1Token: iratok, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [körvonalazható]   B= [iratok, körét, szerintünk ,.. ]

B0Lemma: irat, B0POS: N, B0Token: iratok, B1Lemma: kör, B1POS: N, B1Token: körét, S0B0Lemma: körvonalazható_irat, S0B0LemmaPOS: körvonalazható_N, S0B0POS: A_N, S0B0POSLemma: A_irat, S0B0Token: körvonalazható_iratok, S0B1Lemma: körvonalazható_kör, S0B1LemmaPOS: körvonalazható_N, S0B1POS: A_N, S0B1POSLemma: A_kör, S0B1Token: körvonalazható_körét, S0Lemma: körvonalazható, S0POS: A, S0Token: körvonalazható, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, körvonalazható_isGouvernedBy_irat: true, körvonalazható_isGouvernedBy_irat_ATT: true, 

16- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [iratok, körét, szerintünk ,.. ]

B0Lemma: irat, B0POS: N, B0Token: iratok, B1Lemma: kör, B1POS: N, B1Token: körét, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [iratok]   B= [körét, szerintünk, a ,.. ]

B0Lemma: kör, B0POS: N, B0Token: körét, B1Lemma: szerinte, B1POS: R, B1Token: szerintünk, S0B0Lemma: irat_kör, S0B0LemmaPOS: irat_N, S0B0POS: N_N, S0B0POSLemma: N_kör, S0B0Token: iratok_körét, S0B1Lemma: irat_szerinte, S0B1LemmaPOS: irat_R, S0B1POS: N_R, S0B1POSLemma: N_szerinte, S0B1Token: iratok_szerintünk, S0Lemma: irat, S0POS: N, S0Token: iratok, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, irat_isGouvernedBy_kör: true, irat_isGouvernedBy_kör_ATT: true, 

18- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [körét, szerintünk, a ,.. ]

B0Lemma: kör, B0POS: N, B0Token: körét, B1Lemma: szerinte, B1POS: R, B1Token: szerintünk, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [körét]   B= [szerintünk, a, gt. ,.. ]

B0Lemma: szerinte, B0POS: R, B0Token: szerintünk, B1Lemma: a, B1POS: T, B1Token: a, S0B0Lemma: kör_szerinte, S0B0LemmaPOS: kör_R, S0B0POS: N_R, S0B0POSLemma: N_szerinte, S0B0Token: körét_szerintünk, S0B1Lemma: kör_a, S0B1LemmaPOS: kör_T, S0B1POS: N_T, S0B1POSLemma: N_a, S0B1Token: körét_a, S0Lemma: kör, S0POS: N, S0Token: körét, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, kör_isGouvernedBy_értelmez: true, kör_isGouvernedBy_értelmez_OBJ: true, 

20- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [szerintünk, a, gt. ,.. ]

B0Lemma: szerinte, B0POS: R, B0Token: szerintünk, B1Lemma: a, B1POS: T, B1Token: a, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [szerintünk]   B= [a, gt., ( ,.. ]

B0Lemma: a, B0POS: T, B0Token: a, B1Lemma: Gt., B1POS: N, B1Token: gt., S0B0Lemma: szerinte_a, S0B0LemmaPOS: szerinte_T, S0B0POS: R_T, S0B0POSLemma: R_a, S0B0Token: szerintünk_a, S0B1Lemma: szerinte_Gt., S0B1LemmaPOS: szerinte_N, S0B1POS: R_N, S0B1POSLemma: R_Gt., S0B1Token: szerintünk_gt., S0Lemma: szerinte, S0POS: R, S0Token: szerintünk, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, szerinte_isGouvernedBy_lehet: true, szerinte_isGouvernedBy_lehet_MODE: true, 

22- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [a, gt., ( ,.. ]

B0Lemma: a, B0POS: T, B0Token: a, B1Lemma: Gt., B1POS: N, B1Token: gt., TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

23- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [a]   B= [gt., (, új ,.. ]

B0Lemma: Gt., B0POS: N, B0Token: gt., B1Lemma: (, B1POS: (, B1Token: (, S0B0Lemma: a_Gt., S0B0LemmaPOS: a_N, S0B0POS: T_N, S0B0POSLemma: T_Gt., S0B0Token: a_gt., S0B1Lemma: a_(, S0B1LemmaPOS: a_(, S0B1POS: T_(, S0B1POSLemma: T_(, S0B1Token: a_(, S0Lemma: a, S0POS: T, S0Token: a, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, a_isGouvernedBy_§: true, a_isGouvernedBy_§_DET: true, 

24- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [gt., (, új ,.. ]

B0Lemma: Gt., B0POS: N, B0Token: gt., B1Lemma: (, B1POS: (, B1Token: (, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

25- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [gt.]   B= [(, új, ) ,.. ]

B0Lemma: (, B0POS: (, B0Token: (, B1Lemma: új, B1POS: A, B1Token: új, Gt._hasRighDep_ATT: true, Gt._isGouvernedBy_§: true, Gt._isGouvernedBy_§_ATT: true, Gt._új_hasRighDep_ATT: true, S0B0Lemma: Gt._(, S0B0LemmaPOS: Gt._(, S0B0POS: N_(, S0B0POSLemma: N_(, S0B0Token: gt._(, S0B1Lemma: Gt._új, S0B1LemmaPOS: Gt._A, S0B1POS: N_A, S0B1POSLemma: N_új, S0B1Token: gt._új, S0Lemma: Gt., S0POS: N, S0Token: gt., TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, hasRighDep_ATT: true, 

26- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [(, új, ) ,.. ]

B0Lemma: (, B0POS: (, B0Token: (, B1Lemma: új, B1POS: A, B1Token: új, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

27- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [(]   B= [új, ), 72. ,.. ]

(_isGouvernedBy_új: true, (_isGouvernedBy_új_PUNCT: true, B0Lemma: új, B0POS: A, B0Token: új, B1Lemma: ), B1POS: ), B1Token: ), S0B0Lemma: (_új, S0B0LemmaPOS: (_A, S0B0POS: (_A, S0B0POSLemma: (_új, S0B0Token: (_új, S0B1Lemma: (_), S0B1LemmaPOS: (_), S0B1POS: (_), S0B1POSLemma: (_), S0B1Token: (_), S0Lemma: (, S0POS: (, S0Token: (, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

28- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [új, ), 72. ,.. ]

B0Lemma: új, B0POS: A, B0Token: új, B1Lemma: ), B1POS: ), B1Token: ), TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

29- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [új]   B= [), 72., § ,.. ]

B0Lemma: ), B0POS: ), B0Token: ), B1Lemma: 72., B1POS: M, B1Token: 72., S0B0Lemma: új_), S0B0LemmaPOS: új_), S0B0POS: A_), S0B0POSLemma: A_), S0B0Token: új_), S0B1Lemma: új_72., S0B1LemmaPOS: új_M, S0B1POS: A_M, S0B1POSLemma: A_72., S0B1Token: új_72., S0Lemma: új, S0POS: A, S0Token: új, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, hasRighDep_PUNCT: true, új_)_hasRighDep_PUNCT: true, új_hasRighDep_PUNCT: true, 

30- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [), 72., § ,.. ]

B0Lemma: ), B0POS: ), B0Token: ), B1Lemma: 72., B1POS: M, B1Token: 72., TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

31- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [)]   B= [72., §, (2) ,.. ]

B0Lemma: 72., B0POS: M, B0Token: 72., B1Lemma: §, B1POS: §, B1Token: §, S0B0Lemma: )_72., S0B0LemmaPOS: )_M, S0B0POS: )_M, S0B0POSLemma: )_72., S0B0Token: )_72., S0B1Lemma: )_§, S0B1LemmaPOS: )_§, S0B1POS: )_§, S0B1POSLemma: )_§, S0B1Token: )_§, S0Lemma: ), S0POS: ), S0Token: ), TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

32- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [72., §, (2) ,.. ]

B0Lemma: 72., B0POS: M, B0Token: 72., B1Lemma: §, B1POS: §, B1Token: §, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

33- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [72.]   B= [§, (2), bekezdés ,.. ]

72._isGouvernedBy_§: true, 72._isGouvernedBy_§_ATT: true, B0Lemma: §, B0POS: §, B0Token: §, B1Lemma: (2), B1POS: O, B1Token: (2), S0B0Lemma: 72._§, S0B0LemmaPOS: 72._§, S0B0POS: M_§, S0B0POSLemma: M_§, S0B0Token: 72._§, S0B1Lemma: 72._(2), S0B1LemmaPOS: 72._O, S0B1POS: M_O, S0B1POSLemma: M_(2), S0B1Token: 72._(2), S0Lemma: 72., S0POS: M, S0Token: 72., TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

34- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [§, (2), bekezdés ,.. ]

B0Lemma: §, B0POS: §, B0Token: §, B1Lemma: (2), B1POS: O, B1Token: (2), TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

35- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [§]   B= [(2), bekezdés, és ,.. ]

B0Lemma: (2), B0POS: O, B0Token: (2), B1IsInLexic: true, B1Lemma: bekezdés, B1POS: N, B1Token: bekezdés, S0B0Lemma: §_(2), S0B0LemmaPOS: §_O, S0B0POS: §_O, S0B0POSLemma: §_(2), S0B0Token: §_(2), S0B1Lemma: §_bekezdés, S0B1LemmaPOS: §_N, S0B1POS: §_N, S0B1POSLemma: §_bekezdés, S0B1Token: §_bekezdés, S0Lemma: §, S0POS: §, S0Token: §, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, §_isGouvernedBy_bekezdés: true, §_isGouvernedBy_bekezdés_ATT: true, 

36- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [(2), bekezdés, és ,.. ]

B0Lemma: (2), B0POS: O, B0Token: (2), B1IsInLexic: true, B1Lemma: bekezdés, B1POS: N, B1Token: bekezdés, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

37- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [(2)]   B= [bekezdés, és, 77. ,.. ]

(2)_isGouvernedBy_bekezdés: true, (2)_isGouvernedBy_bekezdés_ATT: true, B0IsInLexic: true, B0Lemma: bekezdés, B0POS: N, B0Token: bekezdés, B1Lemma: és, B1POS: C, B1Token: és, S0B0Lemma: (2)_bekezdés, S0B0LemmaPOS: (2)_N, S0B0POS: O_N, S0B0POSLemma: O_bekezdés, S0B0Token: (2)_bekezdés, S0B1Lemma: (2)_és, S0B1LemmaPOS: (2)_C, S0B1POS: O_C, S0B1POSLemma: O_és, S0B1Token: (2)_és, S0Lemma: (2), S0POS: O, S0Token: (2), TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

38- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [bekezdés, és, 77. ,.. ]

B0IsInLexic: true, B0Lemma: bekezdés, B0POS: N, B0Token: bekezdés, B1Lemma: és, B1POS: C, B1Token: és, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

39- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [bekezdés]   B= [és, 77., § ,.. ]

B0Lemma: és, B0POS: C, B0Token: és, B1Lemma: 77., B1POS: M, B1Token: 77., S0B0Lemma: bekezdés_és, S0B0LemmaPOS: bekezdés_C, S0B0POS: N_C, S0B0POSLemma: N_és, S0B0Token: bekezdés_és, S0B1Lemma: bekezdés_77., S0B1LemmaPOS: bekezdés_M, S0B1POS: N_M, S0B1POSLemma: N_77., S0B1Token: bekezdés_77., S0IsInLexic: true, S0Lemma: bekezdés, S0POS: N, S0Token: bekezdés, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, bekezdés_hasRighDep_CONJ: true, bekezdés_isGouvernedBy_összhang: true, bekezdés_isGouvernedBy_összhang_OBL: true, bekezdés_és_hasRighDep_CONJ: true, hasRighDep_CONJ: true, 

40- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [és, 77., § ,.. ]

B0Lemma: és, B0POS: C, B0Token: és, B1Lemma: 77., B1POS: M, B1Token: 77., TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

41- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [és]   B= [77., §, (2) ,.. ]

B0Lemma: 77., B0POS: M, B0Token: 77., B1Lemma: §, B1POS: §, B1Token: §, S0B0Lemma: és_77., S0B0LemmaPOS: és_M, S0B0POS: C_M, S0B0POSLemma: C_77., S0B0Token: és_77., S0B1Lemma: és_§, S0B1LemmaPOS: és_§, S0B1POS: C_§, S0B1POSLemma: C_§, S0B1Token: és_§, S0Lemma: és, S0POS: C, S0Token: és, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, hasRighDep_COORD: true, és_bekezdés_hasRighDep_COORD: true, és_hasRighDep_COORD: true, 

42- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [77., §, (2) ,.. ]

B0Lemma: 77., B0POS: M, B0Token: 77., B1Lemma: §, B1POS: §, B1Token: §, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

43- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [77.]   B= [§, (2), bekezdéssel ,.. ]

77._isGouvernedBy_§: true, 77._isGouvernedBy_§_ATT: true, B0Lemma: §, B0POS: §, B0Token: §, B1Lemma: (2), B1POS: O, B1Token: (2), S0B0Lemma: 77._§, S0B0LemmaPOS: 77._§, S0B0POS: M_§, S0B0POSLemma: M_§, S0B0Token: 77._§, S0B1Lemma: 77._(2), S0B1LemmaPOS: 77._O, S0B1POS: M_O, S0B1POSLemma: M_(2), S0B1Token: 77._(2), S0Lemma: 77., S0POS: M, S0Token: 77., TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

44- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [§, (2), bekezdéssel ,.. ]

B0Lemma: §, B0POS: §, B0Token: §, B1Lemma: (2), B1POS: O, B1Token: (2), TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

45- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [§]   B= [(2), bekezdéssel, összhangban ,.. ]

B0Lemma: (2), B0POS: O, B0Token: (2), B1IsInLexic: true, B1Lemma: bekezdés, B1POS: N, B1Token: bekezdéssel, S0B0Lemma: §_(2), S0B0LemmaPOS: §_O, S0B0POS: §_O, S0B0POSLemma: §_(2), S0B0Token: §_(2), S0B1Lemma: §_bekezdés, S0B1LemmaPOS: §_N, S0B1POS: §_N, S0B1POSLemma: §_bekezdés, S0B1Token: §_bekezdéssel, S0Lemma: §, S0POS: §, S0Token: §, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, §_isGouvernedBy_bekezdés: true, §_isGouvernedBy_bekezdés_ATT: true, 

46- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [(2), bekezdéssel, összhangban ,.. ]

B0Lemma: (2), B0POS: O, B0Token: (2), B1IsInLexic: true, B1Lemma: bekezdés, B1POS: N, B1Token: bekezdéssel, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

47- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [(2)]   B= [bekezdéssel, összhangban, lehet ,.. ]

(2)_isGouvernedBy_bekezdés: true, (2)_isGouvernedBy_bekezdés_ATT: true, B0IsInLexic: true, B0Lemma: bekezdés, B0POS: N, B0Token: bekezdéssel, B1IsInLexic: true, B1Lemma: összhang, B1POS: N, B1Token: összhangban, S0B0Lemma: (2)_bekezdés, S0B0LemmaPOS: (2)_N, S0B0POS: O_N, S0B0POSLemma: O_bekezdés, S0B0Token: (2)_bekezdéssel, S0B1Lemma: (2)_összhang, S0B1LemmaPOS: (2)_N, S0B1POS: O_N, S0B1POSLemma: O_összhang, S0B1Token: (2)_összhangban, S0Lemma: (2), S0POS: O, S0Token: (2), TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

48- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [bekezdéssel, összhangban, lehet ,.. ]

B0IsInLexic: true, B0Lemma: bekezdés, B0POS: N, B0Token: bekezdéssel, B1IsInLexic: true, B1Lemma: összhang, B1POS: N, B1Token: összhangban, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

49- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [bekezdéssel]   B= [összhangban, lehet, értelmezni ,.. ]

B0IsInLexic: true, B0Lemma: összhang, B0POS: N, B0Token: összhangban, B1Lemma: lehet, B1POS: V, B1Token: lehet, S0B0Lemma: bekezdés_összhang, S0B0LemmaPOS: bekezdés_N, S0B0POS: N_N, S0B0POSLemma: N_összhang, S0B0Token: bekezdéssel_összhangban, S0B1Lemma: bekezdés_lehet, S0B1LemmaPOS: bekezdés_V, S0B1POS: N_V, S0B1POSLemma: N_lehet, S0B1Token: bekezdéssel_lehet, S0IsInLexic: true, S0Lemma: bekezdés, S0POS: N, S0Token: bekezdéssel, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

50- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [összhangban, lehet, értelmezni ,.. ]

B0IsInLexic: true, B0Lemma: összhang, B0POS: N, B0Token: összhangban, B1Lemma: lehet, B1POS: V, B1Token: lehet, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

51- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [összhangban]   B= [lehet, értelmezni, , ,.. ]

B0Lemma: lehet, B0POS: V, B0Token: lehet, B1Lemma: értelmez, B1POS: V, B1Token: értelmezni, S0B0Lemma: összhang_lehet, S0B0LemmaPOS: összhang_V, S0B0POS: N_V, S0B0POSLemma: N_lehet, S0B0Token: összhangban_lehet, S0B1Lemma: összhang_értelmez, S0B1LemmaPOS: összhang_V, S0B1POS: N_V, S0B1POSLemma: N_értelmez, S0B1Token: összhangban_értelmezni, S0IsInLexic: true, S0Lemma: összhang, S0POS: N, S0Token: összhangban, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, összhang_isGouvernedBy_értelmez: true, összhang_isGouvernedBy_értelmez_OBL: true, 

52- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [lehet, értelmezni, , ,.. ]

B0Lemma: lehet, B0POS: V, B0Token: lehet, B1Lemma: értelmez, B1POS: V, B1Token: értelmezni, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

53- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [lehet]   B= [értelmezni, ,, ezért ,.. ]

B0Lemma: értelmez, B0POS: V, B0Token: értelmezni, B1Lemma: ,, B1POS: ,, B1Token: ,, S0B0Lemma: lehet_értelmez, S0B0LemmaPOS: lehet_V, S0B0POS: V_V, S0B0POSLemma: V_értelmez, S0B0Token: lehet_értelmezni, S0B1Lemma: lehet_,, S0B1LemmaPOS: lehet_,, S0B1POS: V_,, S0B1POSLemma: V_,, S0B1Token: lehet_,, S0Lemma: lehet, S0POS: V, S0Token: lehet, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

54- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [értelmezni, ,, ezért ,.. ]

B0Lemma: értelmez, B0POS: V, B0Token: értelmezni, B1Lemma: ,, B1POS: ,, B1Token: ,, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

55- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [értelmezni]   B= [,, ezért, ezek ,.. ]

B0Lemma: ,, B0POS: ,, B0Token: ,, B1Lemma: ezért, B1POS: C, B1Token: ezért, S0B0Lemma: értelmez_,, S0B0LemmaPOS: értelmez_,, S0B0POS: V_,, S0B0POSLemma: V_,, S0B0Token: értelmezni_,, S0B1Lemma: értelmez_ezért, S0B1LemmaPOS: értelmez_C, S0B1POS: V_C, S0B1POSLemma: V_ezért, S0B1Token: értelmezni_ezért, S0Lemma: értelmez, S0POS: V, S0Token: értelmezni, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

56- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, ezért, ezek ,.. ]

B0Lemma: ,, B0POS: ,, B0Token: ,, B1Lemma: ezért, B1POS: C, B1Token: ezért, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

57- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [ezért, ezek, az ,.. ]

B0Lemma: ezért, B0POS: C, B0Token: ezért, B1Lemma: ez, B1POS: P, B1Token: ezek, S0B0Lemma: ,_ezért, S0B0LemmaPOS: ,_C, S0B0POS: ,_C, S0B0POSLemma: ,_ezért, S0B0Token: ,_ezért, S0B1Lemma: ,_ez, S0B1LemmaPOS: ,_P, S0B1POS: ,_P, S0B1POSLemma: ,_ez, S0B1Token: ,_ezek, S0Lemma: ,, S0POS: ,, S0Token: ,, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

58- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ezért, ezek, az ,.. ]

B0Lemma: ezért, B0POS: C, B0Token: ezért, B1Lemma: ez, B1POS: P, B1Token: ezek, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

59- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ezért]   B= [ezek, az, iratok ,.. ]

B0Lemma: ez, B0POS: P, B0Token: ezek, B1Lemma: az, B1POS: T, B1Token: az, S0B0Lemma: ezért_ez, S0B0LemmaPOS: ezért_P, S0B0POS: C_P, S0B0POSLemma: C_ez, S0B0Token: ezért_ezek, S0B1Lemma: ezért_az, S0B1LemmaPOS: ezért_T, S0B1POS: C_T, S0B1POSLemma: C_az, S0B1Token: ezért_az, S0Lemma: ezért, S0POS: C, S0Token: ezért, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, ezért_hasRighDep_COORD: true, ezért_terjedhet_hasRighDep_COORD: true, hasRighDep_COORD: true, 

60- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ezek, az, iratok ,.. ]

B0Lemma: ez, B0POS: P, B0Token: ezek, B1Lemma: az, B1POS: T, B1Token: az, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

61- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ezek]   B= [az, iratok, az ,.. ]

B0Lemma: az, B0POS: T, B0Token: az, B1Lemma: irat, B1POS: N, B1Token: iratok, S0B0Lemma: ez_az, S0B0LemmaPOS: ez_T, S0B0POS: P_T, S0B0POSLemma: P_az, S0B0Token: ezek_az, S0B1Lemma: ez_irat, S0B1LemmaPOS: ez_N, S0B1POS: P_N, S0B1POSLemma: P_irat, S0B1Token: ezek_iratok, S0Lemma: ez, S0POS: P, S0Token: ezek, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, ez_isGouvernedBy_irat: true, ez_isGouvernedBy_irat_ATT: true, 

62- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [az, iratok, az ,.. ]

B0Lemma: az, B0POS: T, B0Token: az, B1Lemma: irat, B1POS: N, B1Token: iratok, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

63- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [az]   B= [iratok, az, átalakulással ,.. ]

B0Lemma: irat, B0POS: N, B0Token: iratok, B1Lemma: az, B1POS: T, B1Token: az, S0B0Lemma: az_irat, S0B0LemmaPOS: az_N, S0B0POS: T_N, S0B0POSLemma: T_irat, S0B0Token: az_iratok, S0B1Lemma: az_az, S0B1LemmaPOS: az_T, S0B1POS: T_T, S0B1POSLemma: T_az, S0B1Token: az_az, S0Lemma: az, S0POS: T, S0Token: az, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, az_isGouvernedBy_irat: true, az_isGouvernedBy_irat_DET: true, 

64- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [iratok, az, átalakulással ,.. ]

B0Lemma: irat, B0POS: N, B0Token: iratok, B1Lemma: az, B1POS: T, B1Token: az, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

65- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [iratok]   B= [az, átalakulással, összefüggő ,.. ]

B0Lemma: az, B0POS: T, B0Token: az, B1Lemma: átalakulás, B1POS: N, B1Token: átalakulással, S0B0Lemma: irat_az, S0B0LemmaPOS: irat_T, S0B0POS: N_T, S0B0POSLemma: N_az, S0B0Token: iratok_az, S0B1Lemma: irat_átalakulás, S0B1LemmaPOS: irat_N, S0B1POS: N_N, S0B1POSLemma: N_átalakulás, S0B1Token: iratok_átalakulással, S0Lemma: irat, S0POS: N, S0Token: iratok, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, irat_isGouvernedBy_terjedhet: true, irat_isGouvernedBy_terjedhet_SUBJ: true, 

66- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [az, átalakulással, összefüggő ,.. ]

B0Lemma: az, B0POS: T, B0Token: az, B1Lemma: átalakulás, B1POS: N, B1Token: átalakulással, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

67- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [az]   B= [átalakulással, összefüggő, iratok ,.. ]

B0Lemma: átalakulás, B0POS: N, B0Token: átalakulással, B1IsInLexic: true, B1Lemma: összefüggő, B1POS: A, B1Token: összefüggő, S0B0Lemma: az_átalakulás, S0B0LemmaPOS: az_N, S0B0POS: T_N, S0B0POSLemma: T_átalakulás, S0B0Token: az_átalakulással, S0B1Lemma: az_összefüggő, S0B1LemmaPOS: az_A, S0B1POS: T_A, S0B1POSLemma: T_összefüggő, S0B1Token: az_összefüggő, S0Lemma: az, S0POS: T, S0Token: az, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, az_isGouvernedBy_átalakulás: true, az_isGouvernedBy_átalakulás_DET: true, 

68- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [átalakulással, összefüggő, iratok ,.. ]

B0Lemma: átalakulás, B0POS: N, B0Token: átalakulással, B1IsInLexic: true, B1Lemma: összefüggő, B1POS: A, B1Token: összefüggő, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

69- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [átalakulással]   B= [összefüggő, iratok, körére ,.. ]

B0IsInLexic: true, B0Lemma: összefüggő, B0POS: A, B0Token: összefüggő, B1Lemma: irat, B1POS: N, B1Token: iratok, S0B0Lemma: átalakulás_összefüggő, S0B0LemmaPOS: átalakulás_A, S0B0POS: N_A, S0B0POSLemma: N_összefüggő, S0B0Token: átalakulással_összefüggő, S0B1Lemma: átalakulás_irat, S0B1LemmaPOS: átalakulás_N, S0B1POS: N_N, S0B1POSLemma: N_irat, S0B1Token: átalakulással_iratok, S0Lemma: átalakulás, S0POS: N, S0Token: átalakulással, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, átalakulás_isGouvernedBy_összefüggő: true, átalakulás_isGouvernedBy_összefüggő_OBL: true, 

70- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [összefüggő, iratok, körére ,.. ]

B0IsInLexic: true, B0Lemma: összefüggő, B0POS: A, B0Token: összefüggő, B1Lemma: irat, B1POS: N, B1Token: iratok, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

71- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [összefüggő]   B= [iratok, körére, terjedhetnek ,.. ]

B0Lemma: irat, B0POS: N, B0Token: iratok, B1Lemma: kör, B1POS: N, B1Token: körére, S0B0Lemma: összefüggő_irat, S0B0LemmaPOS: összefüggő_N, S0B0POS: A_N, S0B0POSLemma: A_irat, S0B0Token: összefüggő_iratok, S0B1Lemma: összefüggő_kör, S0B1LemmaPOS: összefüggő_N, S0B1POS: A_N, S0B1POSLemma: A_kör, S0B1Token: összefüggő_körére, S0IsInLexic: true, S0Lemma: összefüggő, S0POS: A, S0Token: összefüggő, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, összefüggő_isGouvernedBy_irat: true, összefüggő_isGouvernedBy_irat_ATT: true, 

72- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [iratok, körére, terjedhetnek ,.. ]

B0Lemma: irat, B0POS: N, B0Token: iratok, B1Lemma: kör, B1POS: N, B1Token: körére, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

73- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [iratok]   B= [körére, terjedhetnek, ki ,.. ]

B0Lemma: kör, B0POS: N, B0Token: körére, B1Lemma: terjedhet, B1POS: V, B1Token: terjedhetnek, S0B0Lemma: irat_kör, S0B0LemmaPOS: irat_N, S0B0POS: N_N, S0B0POSLemma: N_kör, S0B0Token: iratok_körére, S0B1Lemma: irat_terjedhet, S0B1LemmaPOS: irat_V, S0B1POS: N_V, S0B1POSLemma: N_terjedhet, S0B1Token: iratok_terjedhetnek, S0Lemma: irat, S0POS: N, S0Token: iratok, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, irat_isGouvernedBy_kör: true, irat_isGouvernedBy_kör_ATT: true, 

74- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [körére, terjedhetnek, ki ,.. ]

B0Lemma: kör, B0POS: N, B0Token: körére, B1Lemma: terjedhet, B1POS: V, B1Token: terjedhetnek, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

75- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [körére]   B= [terjedhetnek, ki, . ,.. ]

B0Lemma: terjedhet, B0POS: V, B0Token: terjedhetnek, B1IsInLexic: true, B1Lemma: ki, B1POS: R, B1Token: ki, S0B0Lemma: kör_terjedhet, S0B0LemmaPOS: kör_V, S0B0POS: N_V, S0B0POSLemma: N_terjedhet, S0B0Token: körére_terjedhetnek, S0B1Lemma: kör_ki, S0B1LemmaPOS: kör_R, S0B1POS: N_R, S0B1POSLemma: N_ki, S0B1Token: körére_ki, S0Lemma: kör, S0POS: N, S0Token: körére, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, kör_isGouvernedBy_terjedhet: true, kör_isGouvernedBy_terjedhet_OBL: true, 

76- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [terjedhetnek, ki, . ,.. ]

B0Lemma: terjedhet, B0POS: V, B0Token: terjedhetnek, B1IsInLexic: true, B1Lemma: ki, B1POS: R, B1Token: ki, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

77- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [terjedhetnek]   B= [ki, . ,.. ]

B0IsInLexic: true, B0Lemma: ki, B0POS: R, B0Token: ki, B1Lemma: ., B1POS: ., B1Token: ., S0B0Lemma: terjedhet_ki, S0B0LemmaPOS: terjedhet_R, S0B0POS: V_R, S0B0POSLemma: V_ki, S0B0Token: terjedhetnek_ki, S0B1Lemma: terjedhet_., S0B1LemmaPOS: terjedhet_., S0B1POS: V_., S0B1POSLemma: V_., S0B1Token: terjedhetnek_., S0Lemma: terjedhet, S0POS: V, S0Token: terjedhetnek, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, hasRighDep_PREVERB: true, terjedhet_hasRighDep_PREVERB: true, terjedhet_ki_hasRighDep_PREVERB: true, 

78- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ki, . ,.. ]

B0IsInLexic: true, B0Lemma: ki, B0POS: R, B0Token: ki, B1Lemma: ., B1POS: ., B1Token: ., TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

79- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ki]   B= [.]

B0Lemma: ., B0POS: ., B0Token: ., S0B0Lemma: ki_., S0B0LemmaPOS: ki_., S0B0POS: R_., S0B0POSLemma: R_., S0B0Token: ki_., S0IsInLexic: true, S0Lemma: ki, S0POS: R, S0Token: ki, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

80- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [.]

B0Lemma: ., B0POS: ., B0Token: ., TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

81- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [ ]

S0Lemma: ., S0POS: ., S0Token: ., TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

82- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

## Sentence No. 214 - 
- a gt. ( új ) 76. § (5) bekezdése alapján a vagyonmérleg tervezetet készítő könyvvizsgálónak , vagy más , az egyesülő részvénytársaságtól független szakértőnek a részvénytársaság felkérésére nyilatkozatnia kell az egyesülési szerződés és a tisztségviselők beszámolójának a megalapozottságáról . 
### Existing MWEs: 
1- **bekezdése** (VPC)
2- **beszámolójának** (VPC)



0- &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [-, a, gt. ,.. ]

B0Lemma: -, B0POS: -, B0Token: -, B1Lemma: a, B1POS: T, B1Token: a, 

1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [-]   B= [a, gt., ( ,.. ]

-_isGouvernedBy_kell: true, -_isGouvernedBy_kell_PUNCT: true, B0Lemma: a, B0POS: T, B0Token: a, B1Lemma: Gt., B1POS: N, B1Token: gt., S0B0Lemma: -_a, S0B0LemmaPOS: -_T, S0B0POS: -_T, S0B0POSLemma: -_a, S0B0Token: -_a, S0B1Lemma: -_Gt., S0B1LemmaPOS: -_N, S0B1POS: -_N, S0B1POSLemma: -_Gt., S0B1Token: -_gt., S0Lemma: -, S0POS: -, S0Token: -, 

2- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [a, gt., ( ,.. ]

B0Lemma: a, B0POS: T, B0Token: a, B1Lemma: Gt., B1POS: N, B1Token: gt., TransHistory1: 0, 

3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [a]   B= [gt., (, új ,.. ]

B0Lemma: Gt., B0POS: N, B0Token: gt., B1Lemma: (, B1POS: (, B1Token: (, S0B0Lemma: a_Gt., S0B0LemmaPOS: a_N, S0B0POS: T_N, S0B0POSLemma: T_Gt., S0B0Token: a_gt., S0B1Lemma: a_(, S0B1LemmaPOS: a_(, S0B1POS: T_(, S0B1POSLemma: T_(, S0B1Token: a_(, S0Lemma: a, S0POS: T, S0Token: a, TransHistory1: 2, TransHistory2: 20, a_isGouvernedBy_§: true, a_isGouvernedBy_§_DET: true, 

4- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [gt., (, új ,.. ]

B0Lemma: Gt., B0POS: N, B0Token: gt., B1Lemma: (, B1POS: (, B1Token: (, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [gt.]   B= [(, új, ) ,.. ]

B0Lemma: (, B0POS: (, B0Token: (, B1Lemma: új, B1POS: A, B1Token: új, Gt._hasRighDep_ATT: true, Gt._isGouvernedBy_§: true, Gt._isGouvernedBy_§_ATT: true, Gt._új_hasRighDep_ATT: true, S0B0Lemma: Gt._(, S0B0LemmaPOS: Gt._(, S0B0POS: N_(, S0B0POSLemma: N_(, S0B0Token: gt._(, S0B1Lemma: Gt._új, S0B1LemmaPOS: Gt._A, S0B1POS: N_A, S0B1POSLemma: N_új, S0B1Token: gt._új, S0Lemma: Gt., S0POS: N, S0Token: gt., TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, hasRighDep_ATT: true, 

6- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [(, új, ) ,.. ]

B0Lemma: (, B0POS: (, B0Token: (, B1Lemma: új, B1POS: A, B1Token: új, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [(]   B= [új, ), 76. ,.. ]

(_isGouvernedBy_új: true, (_isGouvernedBy_új_PUNCT: true, B0Lemma: új, B0POS: A, B0Token: új, B1Lemma: ), B1POS: ), B1Token: ), S0B0Lemma: (_új, S0B0LemmaPOS: (_A, S0B0POS: (_A, S0B0POSLemma: (_új, S0B0Token: (_új, S0B1Lemma: (_), S0B1LemmaPOS: (_), S0B1POS: (_), S0B1POSLemma: (_), S0B1Token: (_), S0Lemma: (, S0POS: (, S0Token: (, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

8- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [új, ), 76. ,.. ]

B0Lemma: új, B0POS: A, B0Token: új, B1Lemma: ), B1POS: ), B1Token: ), TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [új]   B= [), 76., § ,.. ]

B0Lemma: ), B0POS: ), B0Token: ), B1Lemma: 76., B1POS: M, B1Token: 76., S0B0Lemma: új_), S0B0LemmaPOS: új_), S0B0POS: A_), S0B0POSLemma: A_), S0B0Token: új_), S0B1Lemma: új_76., S0B1LemmaPOS: új_M, S0B1POS: A_M, S0B1POSLemma: A_76., S0B1Token: új_76., S0Lemma: új, S0POS: A, S0Token: új, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, hasRighDep_PUNCT: true, új_)_hasRighDep_PUNCT: true, új_hasRighDep_PUNCT: true, 

10- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [), 76., § ,.. ]

B0Lemma: ), B0POS: ), B0Token: ), B1Lemma: 76., B1POS: M, B1Token: 76., TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [)]   B= [76., §, (5) ,.. ]

B0Lemma: 76., B0POS: M, B0Token: 76., B1Lemma: §, B1POS: §, B1Token: §, S0B0Lemma: )_76., S0B0LemmaPOS: )_M, S0B0POS: )_M, S0B0POSLemma: )_76., S0B0Token: )_76., S0B1Lemma: )_§, S0B1LemmaPOS: )_§, S0B1POS: )_§, S0B1POSLemma: )_§, S0B1Token: )_§, S0Lemma: ), S0POS: ), S0Token: ), TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

12- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [76., §, (5) ,.. ]

B0Lemma: 76., B0POS: M, B0Token: 76., B1Lemma: §, B1POS: §, B1Token: §, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [76.]   B= [§, (5), bekezdése ,.. ]

76._isGouvernedBy_§: true, 76._isGouvernedBy_§_ATT: true, B0Lemma: §, B0POS: §, B0Token: §, B1Lemma: (5), B1POS: O, B1Token: (5), S0B0Lemma: 76._§, S0B0LemmaPOS: 76._§, S0B0POS: M_§, S0B0POSLemma: M_§, S0B0Token: 76._§, S0B1Lemma: 76._(5), S0B1LemmaPOS: 76._O, S0B1POS: M_O, S0B1POSLemma: M_(5), S0B1Token: 76._(5), S0Lemma: 76., S0POS: M, S0Token: 76., TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

14- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [§, (5), bekezdése ,.. ]

B0Lemma: §, B0POS: §, B0Token: §, B1Lemma: (5), B1POS: O, B1Token: (5), TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [§]   B= [(5), bekezdése, alapján ,.. ]

B0Lemma: (5), B0POS: O, B0Token: (5), B1IsInLexic: true, B1Lemma: bekezdés, B1POS: N, B1Token: bekezdése, S0B0Lemma: §_(5), S0B0LemmaPOS: §_O, S0B0POS: §_O, S0B0POSLemma: §_(5), S0B0Token: §_(5), S0B1Lemma: §_bekezdés, S0B1LemmaPOS: §_N, S0B1POS: §_N, S0B1POSLemma: §_bekezdés, S0B1Token: §_bekezdése, S0Lemma: §, S0POS: §, S0Token: §, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, §_isGouvernedBy_bekezdés: true, §_isGouvernedBy_bekezdés_ATT: true, 

16- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [(5), bekezdése, alapján ,.. ]

B0Lemma: (5), B0POS: O, B0Token: (5), B1IsInLexic: true, B1Lemma: bekezdés, B1POS: N, B1Token: bekezdése, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [(5)]   B= [bekezdése, alapján, a ,.. ]

(5)_isGouvernedBy_bekezdés: true, (5)_isGouvernedBy_bekezdés_ATT: true, B0IsInLexic: true, B0Lemma: bekezdés, B0POS: N, B0Token: bekezdése, B1Lemma: alap, B1POS: N, B1Token: alapján, S0B0Lemma: (5)_bekezdés, S0B0LemmaPOS: (5)_N, S0B0POS: O_N, S0B0POSLemma: O_bekezdés, S0B0Token: (5)_bekezdése, S0B1Lemma: (5)_alap, S0B1LemmaPOS: (5)_N, S0B1POS: O_N, S0B1POSLemma: O_alap, S0B1Token: (5)_alapján, S0Lemma: (5), S0POS: O, S0Token: (5), TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

18- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [bekezdése, alapján, a ,.. ]

B0IsInLexic: true, B0Lemma: bekezdés, B0POS: N, B0Token: bekezdése, B1Lemma: alap, B1POS: N, B1Token: alapján, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [bekezdése]   B= [alapján, a, vagyonmérleg ,.. ]

B0Lemma: alap, B0POS: N, B0Token: alapján, B1Lemma: a, B1POS: T, B1Token: a, S0B0Lemma: bekezdés_alap, S0B0LemmaPOS: bekezdés_N, S0B0POS: N_N, S0B0POSLemma: N_alap, S0B0Token: bekezdése_alapján, S0B1Lemma: bekezdés_a, S0B1LemmaPOS: bekezdés_T, S0B1POS: N_T, S0B1POSLemma: N_a, S0B1Token: bekezdése_a, S0IsInLexic: true, S0Lemma: bekezdés, S0POS: N, S0Token: bekezdése, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, bekezdés_isGouvernedBy_alap: true, bekezdés_isGouvernedBy_alap_ATT: true, 

20- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [alapján, a, vagyonmérleg ,.. ]

B0Lemma: alap, B0POS: N, B0Token: alapján, B1Lemma: a, B1POS: T, B1Token: a, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [alapján]   B= [a, vagyonmérleg, tervezetet ,.. ]

B0Lemma: a, B0POS: T, B0Token: a, B1Lemma: vagyonmérleg, B1POS: N, B1Token: vagyonmérleg, S0B0Lemma: alap_a, S0B0LemmaPOS: alap_T, S0B0POS: N_T, S0B0POSLemma: N_a, S0B0Token: alapján_a, S0B1Lemma: alap_vagyonmérleg, S0B1LemmaPOS: alap_N, S0B1POS: N_N, S0B1POSLemma: N_vagyonmérleg, S0B1Token: alapján_vagyonmérleg, S0Lemma: alap, S0POS: N, S0Token: alapján, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, alap_isGouvernedBy_kell: true, alap_isGouvernedBy_kell_OBL: true, 

22- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [a, vagyonmérleg, tervezetet ,.. ]

B0Lemma: a, B0POS: T, B0Token: a, B1Lemma: vagyonmérleg, B1POS: N, B1Token: vagyonmérleg, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

23- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [a]   B= [vagyonmérleg, tervezetet, készítő ,.. ]

B0Lemma: vagyonmérleg, B0POS: N, B0Token: vagyonmérleg, B1Lemma: tervezet, B1POS: N, B1Token: tervezetet, S0B0Lemma: a_vagyonmérleg, S0B0LemmaPOS: a_N, S0B0POS: T_N, S0B0POSLemma: T_vagyonmérleg, S0B0Token: a_vagyonmérleg, S0B1Lemma: a_tervezet, S0B1LemmaPOS: a_N, S0B1POS: T_N, S0B1POSLemma: T_tervezet, S0B1Token: a_tervezetet, S0Lemma: a, S0POS: T, S0Token: a, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, a_isGouvernedBy_tervezet: true, a_isGouvernedBy_tervezet_DET: true, 

24- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [vagyonmérleg, tervezetet, készítő ,.. ]

B0Lemma: vagyonmérleg, B0POS: N, B0Token: vagyonmérleg, B1Lemma: tervezet, B1POS: N, B1Token: tervezetet, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

25- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [vagyonmérleg]   B= [tervezetet, készítő, könyvvizsgálónak ,.. ]

B0Lemma: tervezet, B0POS: N, B0Token: tervezetet, B1Lemma: készítő, B1POS: A, B1Token: készítő, S0B0Lemma: vagyonmérleg_tervezet, S0B0LemmaPOS: vagyonmérleg_N, S0B0POS: N_N, S0B0POSLemma: N_tervezet, S0B0Token: vagyonmérleg_tervezetet, S0B1Lemma: vagyonmérleg_készítő, S0B1LemmaPOS: vagyonmérleg_A, S0B1POS: N_A, S0B1POSLemma: N_készítő, S0B1Token: vagyonmérleg_készítő, S0Lemma: vagyonmérleg, S0POS: N, S0Token: vagyonmérleg, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, vagyonmérleg_isGouvernedBy_tervezet: true, vagyonmérleg_isGouvernedBy_tervezet_ATT: true, 

26- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [tervezetet, készítő, könyvvizsgálónak ,.. ]

B0Lemma: tervezet, B0POS: N, B0Token: tervezetet, B1Lemma: készítő, B1POS: A, B1Token: készítő, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

27- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [tervezetet]   B= [készítő, könyvvizsgálónak, , ,.. ]

B0Lemma: készítő, B0POS: A, B0Token: készítő, B1Lemma: könyvvizsgáló, B1POS: N, B1Token: könyvvizsgálónak, S0B0Lemma: tervezet_készítő, S0B0LemmaPOS: tervezet_A, S0B0POS: N_A, S0B0POSLemma: N_készítő, S0B0Token: tervezetet_készítő, S0B1Lemma: tervezet_könyvvizsgáló, S0B1LemmaPOS: tervezet_N, S0B1POS: N_N, S0B1POSLemma: N_könyvvizsgáló, S0B1Token: tervezetet_könyvvizsgálónak, S0Lemma: tervezet, S0POS: N, S0Token: tervezetet, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, tervezet_isGouvernedBy_készítő: true, tervezet_isGouvernedBy_készítő_OBJ: true, 

28- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [készítő, könyvvizsgálónak, , ,.. ]

B0Lemma: készítő, B0POS: A, B0Token: készítő, B1Lemma: könyvvizsgáló, B1POS: N, B1Token: könyvvizsgálónak, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

29- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [készítő]   B= [könyvvizsgálónak, ,, vagy ,.. ]

B0Lemma: könyvvizsgáló, B0POS: N, B0Token: könyvvizsgálónak, B1Lemma: ,, B1POS: ,, B1Token: ,, S0B0Lemma: készítő_könyvvizsgáló, S0B0LemmaPOS: készítő_N, S0B0POS: A_N, S0B0POSLemma: A_könyvvizsgáló, S0B0Token: készítő_könyvvizsgálónak, S0B1Lemma: készítő_,, S0B1LemmaPOS: készítő_,, S0B1POS: A_,, S0B1POSLemma: A_,, S0B1Token: készítő_,, S0Lemma: készítő, S0POS: A, S0Token: készítő, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, készítő_isGouvernedBy_könyvvizsgáló: true, készítő_isGouvernedBy_könyvvizsgáló_ATT: true, 

30- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [könyvvizsgálónak, ,, vagy ,.. ]

B0Lemma: könyvvizsgáló, B0POS: N, B0Token: könyvvizsgálónak, B1Lemma: ,, B1POS: ,, B1Token: ,, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

31- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [könyvvizsgálónak]   B= [,, vagy, más ,.. ]

B0Lemma: ,, B0POS: ,, B0Token: ,, B1Lemma: vagy, B1POS: C, B1Token: vagy, S0B0Lemma: könyvvizsgáló_,, S0B0LemmaPOS: könyvvizsgáló_,, S0B0POS: N_,, S0B0POSLemma: N_,, S0B0Token: könyvvizsgálónak_,, S0B1Lemma: könyvvizsgáló_vagy, S0B1LemmaPOS: könyvvizsgáló_C, S0B1POS: N_C, S0B1POSLemma: N_vagy, S0B1Token: könyvvizsgálónak_vagy, S0Lemma: könyvvizsgáló, S0POS: N, S0Token: könyvvizsgálónak, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, hasRighDep_CONJ: true, hasRighDep_PUNCT: true, könyvvizsgáló_,_hasRighDep_PUNCT: true, könyvvizsgáló_hasRighDep_CONJ: true, könyvvizsgáló_hasRighDep_PUNCT: true, könyvvizsgáló_isGouvernedBy_kell: true, könyvvizsgáló_isGouvernedBy_kell_ATT: true, könyvvizsgáló_vagy_hasRighDep_CONJ: true, 

32- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, vagy, más ,.. ]

B0Lemma: ,, B0POS: ,, B0Token: ,, B1Lemma: vagy, B1POS: C, B1Token: vagy, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

33- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [vagy, más, , ,.. ]

B0Lemma: vagy, B0POS: C, B0Token: vagy, B1Lemma: más, B1POS: P, B1Token: más, S0B0Lemma: ,_vagy, S0B0LemmaPOS: ,_C, S0B0POS: ,_C, S0B0POSLemma: ,_vagy, S0B0Token: ,_vagy, S0B1Lemma: ,_más, S0B1LemmaPOS: ,_P, S0B1POS: ,_P, S0B1POSLemma: ,_más, S0B1Token: ,_más, S0Lemma: ,, S0POS: ,, S0Token: ,, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

34- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [vagy, más, , ,.. ]

B0Lemma: vagy, B0POS: C, B0Token: vagy, B1Lemma: más, B1POS: P, B1Token: más, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

35- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [vagy]   B= [más, ,, az ,.. ]

B0Lemma: más, B0POS: P, B0Token: más, B1Lemma: ,, B1POS: ,, B1Token: ,, S0B0Lemma: vagy_más, S0B0LemmaPOS: vagy_P, S0B0POS: C_P, S0B0POSLemma: C_más, S0B0Token: vagy_más, S0B1Lemma: vagy_,, S0B1LemmaPOS: vagy_,, S0B1POS: C_,, S0B1POSLemma: C_,, S0B1Token: vagy_,, S0Lemma: vagy, S0POS: C, S0Token: vagy, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, hasRighDep_COORD: true, vagy_hasRighDep_COORD: true, vagy_szakértő_hasRighDep_COORD: true, 

36- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [más, ,, az ,.. ]

B0Lemma: más, B0POS: P, B0Token: más, B1Lemma: ,, B1POS: ,, B1Token: ,, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

37- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [más]   B= [,, az, egyesülő ,.. ]

B0Lemma: ,, B0POS: ,, B0Token: ,, B1Lemma: az, B1POS: T, B1Token: az, S0B0Lemma: más_,, S0B0LemmaPOS: más_,, S0B0POS: P_,, S0B0POSLemma: P_,, S0B0Token: más_,, S0B1Lemma: más_az, S0B1LemmaPOS: más_T, S0B1POS: P_T, S0B1POSLemma: P_az, S0B1Token: más_az, S0Lemma: más, S0POS: P, S0Token: más, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, más_isGouvernedBy_szakértő: true, más_isGouvernedBy_szakértő_ATT: true, 

38- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, az, egyesülő ,.. ]

B0Lemma: ,, B0POS: ,, B0Token: ,, B1Lemma: az, B1POS: T, B1Token: az, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

39- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [az, egyesülő, részvénytársaságtól ,.. ]

,_isGouvernedBy_szakértő: true, ,_isGouvernedBy_szakértő_PUNCT: true, B0Lemma: az, B0POS: T, B0Token: az, B1Lemma: egyesülő, B1POS: A, B1Token: egyesülő, S0B0Lemma: ,_az, S0B0LemmaPOS: ,_T, S0B0POS: ,_T, S0B0POSLemma: ,_az, S0B0Token: ,_az, S0B1Lemma: ,_egyesülő, S0B1LemmaPOS: ,_A, S0B1POS: ,_A, S0B1POSLemma: ,_egyesülő, S0B1Token: ,_egyesülő, S0Lemma: ,, S0POS: ,, S0Token: ,, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

40- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [az, egyesülő, részvénytársaságtól ,.. ]

B0Lemma: az, B0POS: T, B0Token: az, B1Lemma: egyesülő, B1POS: A, B1Token: egyesülő, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

41- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [az]   B= [egyesülő, részvénytársaságtól, független ,.. ]

B0Lemma: egyesülő, B0POS: A, B0Token: egyesülő, B1Lemma: részvénytársaság, B1POS: N, B1Token: részvénytársaságtól, S0B0Lemma: az_egyesülő, S0B0LemmaPOS: az_A, S0B0POS: T_A, S0B0POSLemma: T_egyesülő, S0B0Token: az_egyesülő, S0B1Lemma: az_részvénytársaság, S0B1LemmaPOS: az_N, S0B1POS: T_N, S0B1POSLemma: T_részvénytársaság, S0B1Token: az_részvénytársaságtól, S0Lemma: az, S0POS: T, S0Token: az, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, az_isGouvernedBy_részvénytársaság: true, az_isGouvernedBy_részvénytársaság_DET: true, 

42- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [egyesülő, részvénytársaságtól, független ,.. ]

B0Lemma: egyesülő, B0POS: A, B0Token: egyesülő, B1Lemma: részvénytársaság, B1POS: N, B1Token: részvénytársaságtól, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

43- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [egyesülő]   B= [részvénytársaságtól, független, szakértőnek ,.. ]

B0Lemma: részvénytársaság, B0POS: N, B0Token: részvénytársaságtól, B1Lemma: független, B1POS: A, B1Token: független, S0B0Lemma: egyesülő_részvénytársaság, S0B0LemmaPOS: egyesülő_N, S0B0POS: A_N, S0B0POSLemma: A_részvénytársaság, S0B0Token: egyesülő_részvénytársaságtól, S0B1Lemma: egyesülő_független, S0B1LemmaPOS: egyesülő_A, S0B1POS: A_A, S0B1POSLemma: A_független, S0B1Token: egyesülő_független, S0Lemma: egyesülő, S0POS: A, S0Token: egyesülő, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, egyesülő_isGouvernedBy_részvénytársaság: true, egyesülő_isGouvernedBy_részvénytársaság_ATT: true, 

44- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [részvénytársaságtól, független, szakértőnek ,.. ]

B0Lemma: részvénytársaság, B0POS: N, B0Token: részvénytársaságtól, B1Lemma: független, B1POS: A, B1Token: független, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

45- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [részvénytársaságtól]   B= [független, szakértőnek, a ,.. ]

B0Lemma: független, B0POS: A, B0Token: független, B1Lemma: szakértő, B1POS: N, B1Token: szakértőnek, S0B0Lemma: részvénytársaság_független, S0B0LemmaPOS: részvénytársaság_A, S0B0POS: N_A, S0B0POSLemma: N_független, S0B0Token: részvénytársaságtól_független, S0B1Lemma: részvénytársaság_szakértő, S0B1LemmaPOS: részvénytársaság_N, S0B1POS: N_N, S0B1POSLemma: N_szakértő, S0B1Token: részvénytársaságtól_szakértőnek, S0Lemma: részvénytársaság, S0POS: N, S0Token: részvénytársaságtól, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, részvénytársaság_isGouvernedBy_független: true, részvénytársaság_isGouvernedBy_független_OBL: true, 

46- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [független, szakértőnek, a ,.. ]

B0Lemma: független, B0POS: A, B0Token: független, B1Lemma: szakértő, B1POS: N, B1Token: szakértőnek, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

47- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [független]   B= [szakértőnek, a, részvénytársaság ,.. ]

B0Lemma: szakértő, B0POS: N, B0Token: szakértőnek, B1Lemma: a, B1POS: T, B1Token: a, S0B0Lemma: független_szakértő, S0B0LemmaPOS: független_N, S0B0POS: A_N, S0B0POSLemma: A_szakértő, S0B0Token: független_szakértőnek, S0B1Lemma: független_a, S0B1LemmaPOS: független_T, S0B1POS: A_T, S0B1POSLemma: A_a, S0B1Token: független_a, S0Lemma: független, S0POS: A, S0Token: független, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, független_isGouvernedBy_szakértő: true, független_isGouvernedBy_szakértő_ATT: true, 

48- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [szakértőnek, a, részvénytársaság ,.. ]

B0Lemma: szakértő, B0POS: N, B0Token: szakértőnek, B1Lemma: a, B1POS: T, B1Token: a, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

49- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [szakértőnek]   B= [a, részvénytársaság, felkérésére ,.. ]

B0Lemma: a, B0POS: T, B0Token: a, B1Lemma: részvénytársaság, B1POS: N, B1Token: részvénytársaság, S0B0Lemma: szakértő_a, S0B0LemmaPOS: szakértő_T, S0B0POS: N_T, S0B0POSLemma: N_a, S0B0Token: szakértőnek_a, S0B1Lemma: szakértő_részvénytársaság, S0B1LemmaPOS: szakértő_N, S0B1POS: N_N, S0B1POSLemma: N_részvénytársaság, S0B1Token: szakértőnek_részvénytársaság, S0Lemma: szakértő, S0POS: N, S0Token: szakértőnek, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

50- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [a, részvénytársaság, felkérésére ,.. ]

B0Lemma: a, B0POS: T, B0Token: a, B1Lemma: részvénytársaság, B1POS: N, B1Token: részvénytársaság, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

51- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [a]   B= [részvénytársaság, felkérésére, nyilatkozatnia ,.. ]

B0Lemma: részvénytársaság, B0POS: N, B0Token: részvénytársaság, B1Lemma: felkérés, B1POS: N, B1Token: felkérésére, S0B0Lemma: a_részvénytársaság, S0B0LemmaPOS: a_N, S0B0POS: T_N, S0B0POSLemma: T_részvénytársaság, S0B0Token: a_részvénytársaság, S0B1Lemma: a_felkérés, S0B1LemmaPOS: a_N, S0B1POS: T_N, S0B1POSLemma: T_felkérés, S0B1Token: a_felkérésére, S0Lemma: a, S0POS: T, S0Token: a, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, a_isGouvernedBy_részvénytársaság: true, a_isGouvernedBy_részvénytársaság_DET: true, 

52- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [részvénytársaság, felkérésére, nyilatkozatnia ,.. ]

B0Lemma: részvénytársaság, B0POS: N, B0Token: részvénytársaság, B1Lemma: felkérés, B1POS: N, B1Token: felkérésére, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

53- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [részvénytársaság]   B= [felkérésére, nyilatkozatnia, kell ,.. ]

B0Lemma: felkérés, B0POS: N, B0Token: felkérésére, B1Lemma: nyilatkozatnia, B1POS: X, B1Token: nyilatkozatnia, S0B0Lemma: részvénytársaság_felkérés, S0B0LemmaPOS: részvénytársaság_N, S0B0POS: N_N, S0B0POSLemma: N_felkérés, S0B0Token: részvénytársaság_felkérésére, S0B1Lemma: részvénytársaság_nyilatkozatnia, S0B1LemmaPOS: részvénytársaság_X, S0B1POS: N_X, S0B1POSLemma: N_nyilatkozatnia, S0B1Token: részvénytársaság_nyilatkozatnia, S0Lemma: részvénytársaság, S0POS: N, S0Token: részvénytársaság, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, részvénytársaság_isGouvernedBy_felkérés: true, részvénytársaság_isGouvernedBy_felkérés_ATT: true, 

54- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [felkérésére, nyilatkozatnia, kell ,.. ]

B0Lemma: felkérés, B0POS: N, B0Token: felkérésére, B1Lemma: nyilatkozatnia, B1POS: X, B1Token: nyilatkozatnia, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

55- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [felkérésére]   B= [nyilatkozatnia, kell, az ,.. ]

B0Lemma: nyilatkozatnia, B0POS: X, B0Token: nyilatkozatnia, B1Lemma: kell, B1POS: V, B1Token: kell, S0B0Lemma: felkérés_nyilatkozatnia, S0B0LemmaPOS: felkérés_X, S0B0POS: N_X, S0B0POSLemma: N_nyilatkozatnia, S0B0Token: felkérésére_nyilatkozatnia, S0B1Lemma: felkérés_kell, S0B1LemmaPOS: felkérés_V, S0B1POS: N_V, S0B1POSLemma: N_kell, S0B1Token: felkérésére_kell, S0Lemma: felkérés, S0POS: N, S0Token: felkérésére, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, felkérés_isGouvernedBy_kell: true, felkérés_isGouvernedBy_kell_OBL: true, 

56- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [nyilatkozatnia, kell, az ,.. ]

B0Lemma: nyilatkozatnia, B0POS: X, B0Token: nyilatkozatnia, B1Lemma: kell, B1POS: V, B1Token: kell, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

57- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [nyilatkozatnia]   B= [kell, az, egyesülési ,.. ]

B0Lemma: kell, B0POS: V, B0Token: kell, B1Lemma: az, B1POS: T, B1Token: az, S0B0Lemma: nyilatkozatnia_kell, S0B0LemmaPOS: nyilatkozatnia_V, S0B0POS: X_V, S0B0POSLemma: X_kell, S0B0Token: nyilatkozatnia_kell, S0B1Lemma: nyilatkozatnia_az, S0B1LemmaPOS: nyilatkozatnia_T, S0B1POS: X_T, S0B1POSLemma: X_az, S0B1Token: nyilatkozatnia_az, S0Lemma: nyilatkozatnia, S0POS: X, S0Token: nyilatkozatnia, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, nyilatkozatnia_isGouvernedBy_kell: true, nyilatkozatnia_isGouvernedBy_kell_INF: true, 

58- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [kell, az, egyesülési ,.. ]

B0Lemma: kell, B0POS: V, B0Token: kell, B1Lemma: az, B1POS: T, B1Token: az, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

59- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [kell]   B= [az, egyesülési, szerződés ,.. ]

B0Lemma: az, B0POS: T, B0Token: az, B1Lemma: egyesülési, B1POS: A, B1Token: egyesülési, S0B0Lemma: kell_az, S0B0LemmaPOS: kell_T, S0B0POS: V_T, S0B0POSLemma: V_az, S0B0Token: kell_az, S0B1Lemma: kell_egyesülési, S0B1LemmaPOS: kell_A, S0B1POS: V_A, S0B1POSLemma: V_egyesülési, S0B1Token: kell_egyesülési, S0Lemma: kell, S0POS: V, S0Token: kell, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

60- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [az, egyesülési, szerződés ,.. ]

B0Lemma: az, B0POS: T, B0Token: az, B1Lemma: egyesülési, B1POS: A, B1Token: egyesülési, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

61- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [az]   B= [egyesülési, szerződés, és ,.. ]

B0Lemma: egyesülési, B0POS: A, B0Token: egyesülési, B1IsInLexic: true, B1Lemma: szerződés, B1POS: N, B1Token: szerződés, S0B0Lemma: az_egyesülési, S0B0LemmaPOS: az_A, S0B0POS: T_A, S0B0POSLemma: T_egyesülési, S0B0Token: az_egyesülési, S0B1Lemma: az_szerződés, S0B1LemmaPOS: az_N, S0B1POS: T_N, S0B1POSLemma: T_szerződés, S0B1Token: az_szerződés, S0Lemma: az, S0POS: T, S0Token: az, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, az_isGouvernedBy_szerződés: true, az_isGouvernedBy_szerződés_DET: true, 

62- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [egyesülési, szerződés, és ,.. ]

B0Lemma: egyesülési, B0POS: A, B0Token: egyesülési, B1IsInLexic: true, B1Lemma: szerződés, B1POS: N, B1Token: szerződés, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

63- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [egyesülési]   B= [szerződés, és, a ,.. ]

B0IsInLexic: true, B0Lemma: szerződés, B0POS: N, B0Token: szerződés, B1Lemma: és, B1POS: C, B1Token: és, S0B0Lemma: egyesülési_szerződés, S0B0LemmaPOS: egyesülési_N, S0B0POS: A_N, S0B0POSLemma: A_szerződés, S0B0Token: egyesülési_szerződés, S0B1Lemma: egyesülési_és, S0B1LemmaPOS: egyesülési_C, S0B1POS: A_C, S0B1POSLemma: A_és, S0B1Token: egyesülési_és, S0Lemma: egyesülési, S0POS: A, S0Token: egyesülési, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, egyesülési_isGouvernedBy_szerződés: true, egyesülési_isGouvernedBy_szerződés_ATT: true, 

64- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [szerződés, és, a ,.. ]

B0IsInLexic: true, B0Lemma: szerződés, B0POS: N, B0Token: szerződés, B1Lemma: és, B1POS: C, B1Token: és, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

65- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [szerződés]   B= [és, a, tisztségviselők ,.. ]

B0Lemma: és, B0POS: C, B0Token: és, B1Lemma: a, B1POS: T, B1Token: a, S0B0Lemma: szerződés_és, S0B0LemmaPOS: szerződés_C, S0B0POS: N_C, S0B0POSLemma: N_és, S0B0Token: szerződés_és, S0B1Lemma: szerződés_a, S0B1LemmaPOS: szerződés_T, S0B1POS: N_T, S0B1POSLemma: N_a, S0B1Token: szerződés_a, S0IsInLexic: true, S0Lemma: szerződés, S0POS: N, S0Token: szerződés, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, hasRighDep_CONJ: true, szerződés_hasRighDep_CONJ: true, szerződés_isGouvernedBy_megalapozottság: true, szerződés_isGouvernedBy_megalapozottság_ATT: true, szerződés_és_hasRighDep_CONJ: true, 

66- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [és, a, tisztségviselők ,.. ]

B0Lemma: és, B0POS: C, B0Token: és, B1Lemma: a, B1POS: T, B1Token: a, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

67- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [és]   B= [a, tisztségviselők, beszámolójának ,.. ]

B0Lemma: a, B0POS: T, B0Token: a, B1Lemma: tisztségviselő, B1POS: N, B1Token: tisztségviselők, S0B0Lemma: és_a, S0B0LemmaPOS: és_T, S0B0POS: C_T, S0B0POSLemma: C_a, S0B0Token: és_a, S0B1Lemma: és_tisztségviselő, S0B1LemmaPOS: és_N, S0B1POS: C_N, S0B1POSLemma: C_tisztségviselő, S0B1Token: és_tisztségviselők, S0Lemma: és, S0POS: C, S0Token: és, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, hasRighDep_COORD: true, és_beszámoló_hasRighDep_COORD: true, és_hasRighDep_COORD: true, 

68- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [a, tisztségviselők, beszámolójának ,.. ]

B0Lemma: a, B0POS: T, B0Token: a, B1Lemma: tisztségviselő, B1POS: N, B1Token: tisztségviselők, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

69- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [a]   B= [tisztségviselők, beszámolójának, a ,.. ]

B0Lemma: tisztségviselő, B0POS: N, B0Token: tisztségviselők, B1IsInLexic: true, B1Lemma: beszámoló, B1POS: N, B1Token: beszámolójának, S0B0Lemma: a_tisztségviselő, S0B0LemmaPOS: a_N, S0B0POS: T_N, S0B0POSLemma: T_tisztségviselő, S0B0Token: a_tisztségviselők, S0B1Lemma: a_beszámoló, S0B1LemmaPOS: a_N, S0B1POS: T_N, S0B1POSLemma: T_beszámoló, S0B1Token: a_beszámolójának, S0Lemma: a, S0POS: T, S0Token: a, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, a_isGouvernedBy_tisztségviselő: true, a_isGouvernedBy_tisztségviselő_DET: true, 

70- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [tisztségviselők, beszámolójának, a ,.. ]

B0Lemma: tisztségviselő, B0POS: N, B0Token: tisztségviselők, B1IsInLexic: true, B1Lemma: beszámoló, B1POS: N, B1Token: beszámolójának, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

71- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [tisztségviselők]   B= [beszámolójának, a, megalapozottságáról ,.. ]

B0IsInLexic: true, B0Lemma: beszámoló, B0POS: N, B0Token: beszámolójának, B1Lemma: a, B1POS: T, B1Token: a, S0B0Lemma: tisztségviselő_beszámoló, S0B0LemmaPOS: tisztségviselő_N, S0B0POS: N_N, S0B0POSLemma: N_beszámoló, S0B0Token: tisztségviselők_beszámolójának, S0B1Lemma: tisztségviselő_a, S0B1LemmaPOS: tisztségviselő_T, S0B1POS: N_T, S0B1POSLemma: N_a, S0B1Token: tisztségviselők_a, S0Lemma: tisztségviselő, S0POS: N, S0Token: tisztségviselők, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, tisztségviselő_isGouvernedBy_beszámoló: true, tisztségviselő_isGouvernedBy_beszámoló_ATT: true, 

72- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [beszámolójának, a, megalapozottságáról ,.. ]

B0IsInLexic: true, B0Lemma: beszámoló, B0POS: N, B0Token: beszámolójának, B1Lemma: a, B1POS: T, B1Token: a, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

73- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [beszámolójának]   B= [a, megalapozottságáról, . ,.. ]

B0Lemma: a, B0POS: T, B0Token: a, B1Lemma: megalapozottság, B1POS: N, B1Token: megalapozottságáról, S0B0Lemma: beszámoló_a, S0B0LemmaPOS: beszámoló_T, S0B0POS: N_T, S0B0POSLemma: N_a, S0B0Token: beszámolójának_a, S0B1Lemma: beszámoló_megalapozottság, S0B1LemmaPOS: beszámoló_N, S0B1POS: N_N, S0B1POSLemma: N_megalapozottság, S0B1Token: beszámolójának_megalapozottságáról, S0IsInLexic: true, S0Lemma: beszámoló, S0POS: N, S0Token: beszámolójának, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

74- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [a, megalapozottságáról, . ,.. ]

B0Lemma: a, B0POS: T, B0Token: a, B1Lemma: megalapozottság, B1POS: N, B1Token: megalapozottságáról, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

75- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [a]   B= [megalapozottságáról, . ,.. ]

B0Lemma: megalapozottság, B0POS: N, B0Token: megalapozottságáról, B1Lemma: ., B1POS: ., B1Token: ., S0B0Lemma: a_megalapozottság, S0B0LemmaPOS: a_N, S0B0POS: T_N, S0B0POSLemma: T_megalapozottság, S0B0Token: a_megalapozottságáról, S0B1Lemma: a_., S0B1LemmaPOS: a_., S0B1POS: T_., S0B1POSLemma: T_., S0B1Token: a_., S0Lemma: a, S0POS: T, S0Token: a, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, a_isGouvernedBy_megalapozottság: true, a_isGouvernedBy_megalapozottság_DET: true, 

76- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [megalapozottságáról, . ,.. ]

B0Lemma: megalapozottság, B0POS: N, B0Token: megalapozottságáról, B1Lemma: ., B1POS: ., B1Token: ., TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

77- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [megalapozottságáról]   B= [.]

B0Lemma: ., B0POS: ., B0Token: ., S0B0Lemma: megalapozottság_., S0B0LemmaPOS: megalapozottság_., S0B0POS: N_., S0B0POSLemma: N_., S0B0Token: megalapozottságáról_., S0Lemma: megalapozottság, S0POS: N, S0Token: megalapozottságáról, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

78- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [.]

B0Lemma: ., B0POS: ., B0Token: ., TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

79- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [ ]

S0Lemma: ., S0POS: ., S0Token: ., TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

80- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

## Sentence No. 233 - 
ilyen eseteknél ugyanis a törvényhely felmentést ad a 76. § (2)-(5) és 77. § (2)-(3) bekezdésében előírtak teljesítése alól . 
### Existing MWEs: 
1- **felmentést ad** (LVC)
2- **bekezdésében** (VPC)



0- &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ilyen, eseteknél, ugyanis ,.. ]

B0Lemma: ilyen, B0POS: P, B0Token: ilyen, B1Lemma: eset, B1POS: N, B1Token: eseteknél, 

1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ilyen]   B= [eseteknél, ugyanis, a ,.. ]

B0Lemma: eset, B0POS: N, B0Token: eseteknél, B1Lemma: ugyanis, B1POS: C, B1Token: ugyanis, S0B0Lemma: ilyen_eset, S0B0LemmaPOS: ilyen_N, S0B0POS: P_N, S0B0POSLemma: P_eset, S0B0Token: ilyen_eseteknél, S0B1Lemma: ilyen_ugyanis, S0B1LemmaPOS: ilyen_C, S0B1POS: P_C, S0B1POSLemma: P_ugyanis, S0B1Token: ilyen_ugyanis, S0Lemma: ilyen, S0POS: P, S0Token: ilyen, ilyen_isGouvernedBy_eset: true, ilyen_isGouvernedBy_eset_ATT: true, 

2- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [eseteknél, ugyanis, a ,.. ]

B0Lemma: eset, B0POS: N, B0Token: eseteknél, B1Lemma: ugyanis, B1POS: C, B1Token: ugyanis, TransHistory1: 0, 

3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [eseteknél]   B= [ugyanis, a, törvényhely ,.. ]

B0Lemma: ugyanis, B0POS: C, B0Token: ugyanis, B1Lemma: a, B1POS: T, B1Token: a, S0B0Lemma: eset_ugyanis, S0B0LemmaPOS: eset_C, S0B0POS: N_C, S0B0POSLemma: N_ugyanis, S0B0Token: eseteknél_ugyanis, S0B1Lemma: eset_a, S0B1LemmaPOS: eset_T, S0B1POS: N_T, S0B1POSLemma: N_a, S0B1Token: eseteknél_a, S0Lemma: eset, S0POS: N, S0Token: eseteknél, TransHistory1: 2, TransHistory2: 20, eset_isGouvernedBy_ad: true, eset_isGouvernedBy_ad_OBL: true, 

4- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ugyanis, a, törvényhely ,.. ]

B0Lemma: ugyanis, B0POS: C, B0Token: ugyanis, B1Lemma: a, B1POS: T, B1Token: a, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ugyanis]   B= [a, törvényhely, felmentést ,.. ]

B0Lemma: a, B0POS: T, B0Token: a, B1Lemma: törvényhely, B1POS: N, B1Token: törvényhely, S0B0Lemma: ugyanis_a, S0B0LemmaPOS: ugyanis_T, S0B0POS: C_T, S0B0POSLemma: C_a, S0B0Token: ugyanis_a, S0B1Lemma: ugyanis_törvényhely, S0B1LemmaPOS: ugyanis_N, S0B1POS: C_N, S0B1POSLemma: C_törvényhely, S0B1Token: ugyanis_törvényhely, S0Lemma: ugyanis, S0POS: C, S0Token: ugyanis, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, ugyanis_isGouvernedBy_ad: true, ugyanis_isGouvernedBy_ad_CONJ: true, 

6- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [a, törvényhely, felmentést ,.. ]

B0Lemma: a, B0POS: T, B0Token: a, B1Lemma: törvényhely, B1POS: N, B1Token: törvényhely, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [a]   B= [törvényhely, felmentést, ad ,.. ]

B0Lemma: törvényhely, B0POS: N, B0Token: törvényhely, B1IsInLexic: true, B1Lemma: felmentés, B1POS: N, B1Token: felmentést, S0B0Lemma: a_törvényhely, S0B0LemmaPOS: a_N, S0B0POS: T_N, S0B0POSLemma: T_törvényhely, S0B0Token: a_törvényhely, S0B1Lemma: a_felmentés, S0B1LemmaPOS: a_N, S0B1POS: T_N, S0B1POSLemma: T_felmentés, S0B1Token: a_felmentést, S0Lemma: a, S0POS: T, S0Token: a, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, a_isGouvernedBy_törvényhely: true, a_isGouvernedBy_törvényhely_DET: true, 

8- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [törvényhely, felmentést, ad ,.. ]

B0Lemma: törvényhely, B0POS: N, B0Token: törvényhely, B1IsInLexic: true, B1Lemma: felmentés, B1POS: N, B1Token: felmentést, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [törvényhely]   B= [felmentést, ad, a ,.. ]

B0IsInLexic: true, B0Lemma: felmentés, B0POS: N, B0Token: felmentést, B1IsInLexic: true, B1Lemma: ad, B1POS: V, B1Token: ad, S0B0Lemma: törvényhely_felmentés, S0B0LemmaPOS: törvényhely_N, S0B0POS: N_N, S0B0POSLemma: N_felmentés, S0B0Token: törvényhely_felmentést, S0B1Lemma: törvényhely_ad, S0B1LemmaPOS: törvényhely_V, S0B1POS: N_V, S0B1POSLemma: N_ad, S0B1Token: törvényhely_ad, S0Lemma: törvényhely, S0POS: N, S0Token: törvényhely, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, törvényhely_isGouvernedBy_ad: true, törvényhely_isGouvernedBy_ad_SUBJ: true, 

10- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [felmentést, ad, a ,.. ]

B0IsInLexic: true, B0Lemma: felmentés, B0POS: N, B0Token: felmentést, B1IsInLexic: true, B1Lemma: ad, B1POS: V, B1Token: ad, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [felmentést]   B= [ad, a, 76. ,.. ]

B0IsInLexic: true, B0Lemma: ad, B0POS: V, B0Token: ad, B1Lemma: a, B1POS: T, B1Token: a, S0B0Lemma: felmentés_ad, S0B0LemmaPOS: felmentés_V, S0B0POS: N_V, S0B0POSLemma: N_ad, S0B0Token: felmentést_ad, S0B1Lemma: felmentés_a, S0B1LemmaPOS: felmentés_T, S0B1POS: N_T, S0B1POSLemma: N_a, S0B1Token: felmentést_a, S0IsInLexic: true, S0Lemma: felmentés, S0POS: N, S0Token: felmentést, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, felmentés_isGouvernedBy_ad: true, felmentés_isGouvernedBy_ad_OBJ: true, 

12- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [felmentést, ad]   B= [a, 76., § ,.. ]

B0Lemma: a, B0POS: T, B0Token: a, B1Lemma: 76., B1POS: M, B1Token: 76., S0B0Lemma: ad_a, S0B0LemmaPOS: ad_T, S0B0POS: V_T, S0B0POSLemma: V_a, S0B0Token: ad_a, S0B1Lemma: ad_76., S0B1LemmaPOS: ad_M, S0B1POS: V_M, S0B1POSLemma: V_76., S0B1Token: ad_76., S0IsInLexic: true, S0Lemma: ad, S0POS: V, S0Token: ad, S1B0Lemma: felmentés_a, S1B0LemmaPOS: felmentés_T, S1B0POS: N_T, S1B0POSLemma: N_a, S1B0Token: felmentést_a, S1IsInLexic: true, S1Lemma: felmentés, S1POS: N, S1S0B0Lemma: felmentés_ad_a, S1S0B0LemmaPOS: felmentés_V_T, S1S0B0POS: N_V_T, S1S0B0POSLemma: N_V_a, S1S0B0Token: felmentést_ad_a, S1S0Lemma: felmentés_ad, S1S0LemmaPOS: felmentés_V, S1S0POS: N_V, S1S0POSLemma: N_ad, S1S0Token: felmentést_ad, S1Token: felmentést, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

13- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[felmentést, ad]]   B= [a, 76., § ,.. ]

B0Lemma: a, B0POS: T, B0Token: a, B1Lemma: 76., B1POS: M, B1Token: 76., S0B0Lemma: felmentés_ad_a, S0B0LemmaPOS: felmentés_ad_T, S0B0POS: N_V_T, S0B0POSLemma: N_V_a, S0B0Token: felmentést_ad_a, S0B1Lemma: felmentés_ad_76., S0B1LemmaPOS: felmentés_ad_M, S0B1POS: N_V_M, S0B1POSLemma: N_V_76., S0B1Token: felmentést_ad_76., S0Lemma: felmentés_ad, S0POS: N_V, S0Token: felmentést_ad, TransHistory1: 0, TransHistory2: 00, TransHistory3: 002, 

14- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [a, 76., § ,.. ]

B0Lemma: a, B0POS: T, B0Token: a, B1Lemma: 76., B1POS: M, B1Token: 76., TransHistory1: 1, TransHistory2: 10, TransHistory3: 100, 

15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [a]   B= [76., §, (2)-(5) ,.. ]

B0Lemma: 76., B0POS: M, B0Token: 76., B1Lemma: §, B1POS: §, B1Token: §, S0B0Lemma: a_76., S0B0LemmaPOS: a_M, S0B0POS: T_M, S0B0POSLemma: T_76., S0B0Token: a_76., S0B1Lemma: a_§, S0B1LemmaPOS: a_§, S0B1POS: T_§, S0B1POSLemma: T_§, S0B1Token: a_§, S0Lemma: a, S0POS: T, S0Token: a, TransHistory1: 2, TransHistory2: 21, TransHistory3: 210, a_isGouvernedBy_§: true, a_isGouvernedBy_§_DET: true, 

16- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [76., §, (2)-(5) ,.. ]

B0Lemma: 76., B0POS: M, B0Token: 76., B1Lemma: §, B1POS: §, B1Token: §, TransHistory1: 0, TransHistory2: 02, TransHistory3: 021, 

17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [76.]   B= [§, (2)-(5), és ,.. ]

76._isGouvernedBy_§: true, 76._isGouvernedBy_§_ATT: true, B0Lemma: §, B0POS: §, B0Token: §, B1Lemma: (2)-(5), B1POS: O, B1Token: (2)-(5), S0B0Lemma: 76._§, S0B0LemmaPOS: 76._§, S0B0POS: M_§, S0B0POSLemma: M_§, S0B0Token: 76._§, S0B1Lemma: 76._(2)-(5), S0B1LemmaPOS: 76._O, S0B1POS: M_O, S0B1POSLemma: M_(2)-(5), S0B1Token: 76._(2)-(5), S0Lemma: 76., S0POS: M, S0Token: 76., TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

18- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [§, (2)-(5), és ,.. ]

B0Lemma: §, B0POS: §, B0Token: §, B1Lemma: (2)-(5), B1POS: O, B1Token: (2)-(5), TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [§]   B= [(2)-(5), és, 77. ,.. ]

B0Lemma: (2)-(5), B0POS: O, B0Token: (2)-(5), B1Lemma: és, B1POS: C, B1Token: és, S0B0Lemma: §_(2)-(5), S0B0LemmaPOS: §_O, S0B0POS: §_O, S0B0POSLemma: §_(2)-(5), S0B0Token: §_(2)-(5), S0B1Lemma: §_és, S0B1LemmaPOS: §_C, S0B1POS: §_C, S0B1POSLemma: §_és, S0B1Token: §_és, S0Lemma: §, S0POS: §, S0Token: §, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, §_isGouvernedBy_(2)-(5): true, §_isGouvernedBy_(2)-(5)_ATT: true, 

20- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [(2)-(5), és, 77. ,.. ]

B0Lemma: (2)-(5), B0POS: O, B0Token: (2)-(5), B1Lemma: és, B1POS: C, B1Token: és, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [(2)-(5)]   B= [és, 77., § ,.. ]

(2)-(5)_hasRighDep_CONJ: true, (2)-(5)_isGouvernedBy_bekezdés: true, (2)-(5)_isGouvernedBy_bekezdés_ATT: true, (2)-(5)_és_hasRighDep_CONJ: true, B0Lemma: és, B0POS: C, B0Token: és, B1Lemma: 77., B1POS: M, B1Token: 77., S0B0Lemma: (2)-(5)_és, S0B0LemmaPOS: (2)-(5)_C, S0B0POS: O_C, S0B0POSLemma: O_és, S0B0Token: (2)-(5)_és, S0B1Lemma: (2)-(5)_77., S0B1LemmaPOS: (2)-(5)_M, S0B1POS: O_M, S0B1POSLemma: O_77., S0B1Token: (2)-(5)_77., S0Lemma: (2)-(5), S0POS: O, S0Token: (2)-(5), TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, hasRighDep_CONJ: true, 

22- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [és, 77., § ,.. ]

B0Lemma: és, B0POS: C, B0Token: és, B1Lemma: 77., B1POS: M, B1Token: 77., TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

23- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [és]   B= [77., §, (2)-(3) ,.. ]

B0Lemma: 77., B0POS: M, B0Token: 77., B1Lemma: §, B1POS: §, B1Token: §, S0B0Lemma: és_77., S0B0LemmaPOS: és_M, S0B0POS: C_M, S0B0POSLemma: C_77., S0B0Token: és_77., S0B1Lemma: és_§, S0B1LemmaPOS: és_§, S0B1POS: C_§, S0B1POSLemma: C_§, S0B1Token: és_§, S0Lemma: és, S0POS: C, S0Token: és, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, hasRighDep_COORD: true, és_(2)-(3)_hasRighDep_COORD: true, és_hasRighDep_COORD: true, 

24- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [77., §, (2)-(3) ,.. ]

B0Lemma: 77., B0POS: M, B0Token: 77., B1Lemma: §, B1POS: §, B1Token: §, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

25- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [77.]   B= [§, (2)-(3), bekezdésében ,.. ]

77._isGouvernedBy_§: true, 77._isGouvernedBy_§_ATT: true, B0Lemma: §, B0POS: §, B0Token: §, B1Lemma: (2)-(3), B1POS: O, B1Token: (2)-(3), S0B0Lemma: 77._§, S0B0LemmaPOS: 77._§, S0B0POS: M_§, S0B0POSLemma: M_§, S0B0Token: 77._§, S0B1Lemma: 77._(2)-(3), S0B1LemmaPOS: 77._O, S0B1POS: M_O, S0B1POSLemma: M_(2)-(3), S0B1Token: 77._(2)-(3), S0Lemma: 77., S0POS: M, S0Token: 77., TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

26- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [§, (2)-(3), bekezdésében ,.. ]

B0Lemma: §, B0POS: §, B0Token: §, B1Lemma: (2)-(3), B1POS: O, B1Token: (2)-(3), TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

27- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [§]   B= [(2)-(3), bekezdésében, előírtak ,.. ]

B0Lemma: (2)-(3), B0POS: O, B0Token: (2)-(3), B1IsInLexic: true, B1Lemma: bekezdés, B1POS: N, B1Token: bekezdésében, S0B0Lemma: §_(2)-(3), S0B0LemmaPOS: §_O, S0B0POS: §_O, S0B0POSLemma: §_(2)-(3), S0B0Token: §_(2)-(3), S0B1Lemma: §_bekezdés, S0B1LemmaPOS: §_N, S0B1POS: §_N, S0B1POSLemma: §_bekezdés, S0B1Token: §_bekezdésében, S0Lemma: §, S0POS: §, S0Token: §, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, §_isGouvernedBy_(2)-(3): true, §_isGouvernedBy_(2)-(3)_ATT: true, 

28- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [(2)-(3), bekezdésében, előírtak ,.. ]

B0Lemma: (2)-(3), B0POS: O, B0Token: (2)-(3), B1IsInLexic: true, B1Lemma: bekezdés, B1POS: N, B1Token: bekezdésében, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

29- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [(2)-(3)]   B= [bekezdésében, előírtak, teljesítése ,.. ]

B0IsInLexic: true, B0Lemma: bekezdés, B0POS: N, B0Token: bekezdésében, B1IsInLexic: true, B1Lemma: előírt, B1POS: N, B1Token: előírtak, S0B0Lemma: (2)-(3)_bekezdés, S0B0LemmaPOS: (2)-(3)_N, S0B0POS: O_N, S0B0POSLemma: O_bekezdés, S0B0Token: (2)-(3)_bekezdésében, S0B1Lemma: (2)-(3)_előírt, S0B1LemmaPOS: (2)-(3)_N, S0B1POS: O_N, S0B1POSLemma: O_előírt, S0B1Token: (2)-(3)_előírtak, S0Lemma: (2)-(3), S0POS: O, S0Token: (2)-(3), TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

30- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [bekezdésében, előírtak, teljesítése ,.. ]

B0IsInLexic: true, B0Lemma: bekezdés, B0POS: N, B0Token: bekezdésében, B1IsInLexic: true, B1Lemma: előírt, B1POS: N, B1Token: előírtak, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

31- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [bekezdésében]   B= [előírtak, teljesítése, alól ,.. ]

B0IsInLexic: true, B0Lemma: előírt, B0POS: N, B0Token: előírtak, B1Lemma: teljesítés, B1POS: N, B1Token: teljesítése, S0B0Lemma: bekezdés_előírt, S0B0LemmaPOS: bekezdés_N, S0B0POS: N_N, S0B0POSLemma: N_előírt, S0B0Token: bekezdésében_előírtak, S0B1Lemma: bekezdés_teljesítés, S0B1LemmaPOS: bekezdés_N, S0B1POS: N_N, S0B1POSLemma: N_teljesítés, S0B1Token: bekezdésében_teljesítése, S0IsInLexic: true, S0Lemma: bekezdés, S0POS: N, S0Token: bekezdésében, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, bekezdés_isGouvernedBy_előírt: true, bekezdés_isGouvernedBy_előírt_OBL: true, 

32- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [előírtak, teljesítése, alól ,.. ]

B0IsInLexic: true, B0Lemma: előírt, B0POS: N, B0Token: előírtak, B1Lemma: teljesítés, B1POS: N, B1Token: teljesítése, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

33- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [előírtak]   B= [teljesítése, alól, . ,.. ]

B0Lemma: teljesítés, B0POS: N, B0Token: teljesítése, B1Lemma: alól, B1POS: S, B1Token: alól, S0B0Lemma: előírt_teljesítés, S0B0LemmaPOS: előírt_N, S0B0POS: N_N, S0B0POSLemma: N_teljesítés, S0B0Token: előírtak_teljesítése, S0B1Lemma: előírt_alól, S0B1LemmaPOS: előírt_S, S0B1POS: N_S, S0B1POSLemma: N_alól, S0B1Token: előírtak_alól, S0IsInLexic: true, S0Lemma: előírt, S0POS: N, S0Token: előírtak, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, előírt_isGouvernedBy_teljesítés: true, előírt_isGouvernedBy_teljesítés_ATT: true, 

34- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [teljesítése, alól, . ,.. ]

B0Lemma: teljesítés, B0POS: N, B0Token: teljesítése, B1Lemma: alól, B1POS: S, B1Token: alól, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

35- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [teljesítése]   B= [alól, . ,.. ]

B0Lemma: alól, B0POS: S, B0Token: alól, B1Lemma: ., B1POS: ., B1Token: ., S0B0Lemma: teljesítés_alól, S0B0LemmaPOS: teljesítés_S, S0B0POS: N_S, S0B0POSLemma: N_alól, S0B0Token: teljesítése_alól, S0B1Lemma: teljesítés_., S0B1LemmaPOS: teljesítés_., S0B1POS: N_., S0B1POSLemma: N_., S0B1Token: teljesítése_., S0Lemma: teljesítés, S0POS: N, S0Token: teljesítése, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, teljesítés_isGouvernedBy_alól: true, teljesítés_isGouvernedBy_alól_ATT: true, 

36- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [alól, . ,.. ]

B0Lemma: alól, B0POS: S, B0Token: alól, B1Lemma: ., B1POS: ., B1Token: ., TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

37- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [alól]   B= [.]

B0Lemma: ., B0POS: ., B0Token: ., S0B0Lemma: alól_., S0B0LemmaPOS: alól_., S0B0POS: S_., S0B0POSLemma: S_., S0B0Token: alól_., S0Lemma: alól, S0POS: S, S0Token: alól, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

38- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [.]

B0Lemma: ., B0POS: ., B0Token: ., TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

39- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [ ]

S0Lemma: ., S0POS: ., S0Token: ., TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

40- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

## Sentence No. 242 - 
az 1988. évi vi. tv. viii. fejezetébe 1992-ben beiktatott rendelkezések viszont már több támpontot adtak a gyakorlat számára , de az egyesülésre való visszautalásnak még mindig tág teret adtak . 
### Existing MWEs: 
1- **támpontot adtak** (LVC)
2- **teret adtak** (LVC)



0- &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [az, 1988., évi ,.. ]

B0Lemma: az, B0POS: T, B0Token: az, B1Lemma: 1988., B1POS: M, B1Token: 1988., 

1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [az]   B= [1988., évi, vi. ,.. ]

B0Lemma: 1988., B0POS: M, B0Token: 1988., B1Lemma: évi, B1POS: A, B1Token: évi, S0B0Lemma: az_1988., S0B0LemmaPOS: az_M, S0B0POS: T_M, S0B0POSLemma: T_1988., S0B0Token: az_1988., S0B1Lemma: az_évi, S0B1LemmaPOS: az_A, S0B1POS: T_A, S0B1POSLemma: T_évi, S0B1Token: az_évi, S0Lemma: az, S0POS: T, S0Token: az, az_isGouvernedBy_tv.: true, az_isGouvernedBy_tv._DET: true, 

2- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [1988., évi, vi. ,.. ]

B0Lemma: 1988., B0POS: M, B0Token: 1988., B1Lemma: évi, B1POS: A, B1Token: évi, TransHistory1: 0, 

3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [1988.]   B= [évi, vi., tv. ,.. ]

1988._isGouvernedBy_évi: true, 1988._isGouvernedBy_évi_ATT: true, B0Lemma: évi, B0POS: A, B0Token: évi, B1Lemma: 6., B1POS: M, B1Token: vi., S0B0Lemma: 1988._évi, S0B0LemmaPOS: 1988._A, S0B0POS: M_A, S0B0POSLemma: M_évi, S0B0Token: 1988._évi, S0B1Lemma: 1988._6., S0B1LemmaPOS: 1988._M, S0B1POS: M_M, S0B1POSLemma: M_6., S0B1Token: 1988._vi., S0Lemma: 1988., S0POS: M, S0Token: 1988., TransHistory1: 2, TransHistory2: 20, 

4- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [évi, vi., tv. ,.. ]

B0Lemma: évi, B0POS: A, B0Token: évi, B1Lemma: 6., B1POS: M, B1Token: vi., TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [évi]   B= [vi., tv., viii. ,.. ]

B0Lemma: 6., B0POS: M, B0Token: vi., B1Lemma: tv., B1POS: N, B1Token: tv., S0B0Lemma: évi_6., S0B0LemmaPOS: évi_M, S0B0POS: A_M, S0B0POSLemma: A_6., S0B0Token: évi_vi., S0B1Lemma: évi_tv., S0B1LemmaPOS: évi_N, S0B1POS: A_N, S0B1POSLemma: A_tv., S0B1Token: évi_tv., S0Lemma: évi, S0POS: A, S0Token: évi, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, évi_isGouvernedBy_tv.: true, évi_isGouvernedBy_tv._ATT: true, 

6- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [vi., tv., viii. ,.. ]

B0Lemma: 6., B0POS: M, B0Token: vi., B1Lemma: tv., B1POS: N, B1Token: tv., TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [vi.]   B= [tv., viii., fejezetébe ,.. ]

6._isGouvernedBy_tv.: true, 6._isGouvernedBy_tv._ATT: true, B0Lemma: tv., B0POS: N, B0Token: tv., B1Lemma: 8., B1POS: M, B1Token: viii., S0B0Lemma: 6._tv., S0B0LemmaPOS: 6._N, S0B0POS: M_N, S0B0POSLemma: M_tv., S0B0Token: vi._tv., S0B1Lemma: 6._8., S0B1LemmaPOS: 6._M, S0B1POS: M_M, S0B1POSLemma: M_8., S0B1Token: vi._viii., S0Lemma: 6., S0POS: M, S0Token: vi., TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

8- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [tv., viii., fejezetébe ,.. ]

B0Lemma: tv., B0POS: N, B0Token: tv., B1Lemma: 8., B1POS: M, B1Token: viii., TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [tv.]   B= [viii., fejezetébe, 1992-ben ,.. ]

B0Lemma: 8., B0POS: M, B0Token: viii., B1Lemma: fejezet, B1POS: N, B1Token: fejezetébe, S0B0Lemma: tv._8., S0B0LemmaPOS: tv._M, S0B0POS: N_M, S0B0POSLemma: N_8., S0B0Token: tv._viii., S0B1Lemma: tv._fejezet, S0B1LemmaPOS: tv._N, S0B1POS: N_N, S0B1POSLemma: N_fejezet, S0B1Token: tv._fejezetébe, S0Lemma: tv., S0POS: N, S0Token: tv., TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, tv._isGouvernedBy_fejezet: true, tv._isGouvernedBy_fejezet_ATT: true, 

10- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [viii., fejezetébe, 1992-ben ,.. ]

B0Lemma: 8., B0POS: M, B0Token: viii., B1Lemma: fejezet, B1POS: N, B1Token: fejezetébe, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [viii.]   B= [fejezetébe, 1992-ben, beiktatott ,.. ]

8._isGouvernedBy_fejezet: true, 8._isGouvernedBy_fejezet_ATT: true, B0Lemma: fejezet, B0POS: N, B0Token: fejezetébe, B1Lemma: 1992, B1POS: M, B1Token: 1992-ben, S0B0Lemma: 8._fejezet, S0B0LemmaPOS: 8._N, S0B0POS: M_N, S0B0POSLemma: M_fejezet, S0B0Token: viii._fejezetébe, S0B1Lemma: 8._1992, S0B1LemmaPOS: 8._M, S0B1POS: M_M, S0B1POSLemma: M_1992, S0B1Token: viii._1992-ben, S0Lemma: 8., S0POS: M, S0Token: viii., TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

12- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [fejezetébe, 1992-ben, beiktatott ,.. ]

B0Lemma: fejezet, B0POS: N, B0Token: fejezetébe, B1Lemma: 1992, B1POS: M, B1Token: 1992-ben, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [fejezetébe]   B= [1992-ben, beiktatott, rendelkezések ,.. ]

B0Lemma: 1992, B0POS: M, B0Token: 1992-ben, B1Lemma: beiktatott, B1POS: A, B1Token: beiktatott, S0B0Lemma: fejezet_1992, S0B0LemmaPOS: fejezet_M, S0B0POS: N_M, S0B0POSLemma: N_1992, S0B0Token: fejezetébe_1992-ben, S0B1Lemma: fejezet_beiktatott, S0B1LemmaPOS: fejezet_A, S0B1POS: N_A, S0B1POSLemma: N_beiktatott, S0B1Token: fejezetébe_beiktatott, S0Lemma: fejezet, S0POS: N, S0Token: fejezetébe, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, fejezet_isGouvernedBy_beiktatott: true, fejezet_isGouvernedBy_beiktatott_OBL: true, 

14- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [1992-ben, beiktatott, rendelkezések ,.. ]

B0Lemma: 1992, B0POS: M, B0Token: 1992-ben, B1Lemma: beiktatott, B1POS: A, B1Token: beiktatott, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [1992-ben]   B= [beiktatott, rendelkezések, viszont ,.. ]

1992_isGouvernedBy_beiktatott: true, 1992_isGouvernedBy_beiktatott_OBL: true, B0Lemma: beiktatott, B0POS: A, B0Token: beiktatott, B1IsInLexic: true, B1Lemma: rendelkezés, B1POS: N, B1Token: rendelkezések, S0B0Lemma: 1992_beiktatott, S0B0LemmaPOS: 1992_A, S0B0POS: M_A, S0B0POSLemma: M_beiktatott, S0B0Token: 1992-ben_beiktatott, S0B1Lemma: 1992_rendelkezés, S0B1LemmaPOS: 1992_N, S0B1POS: M_N, S0B1POSLemma: M_rendelkezés, S0B1Token: 1992-ben_rendelkezések, S0Lemma: 1992, S0POS: M, S0Token: 1992-ben, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

16- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [beiktatott, rendelkezések, viszont ,.. ]

B0Lemma: beiktatott, B0POS: A, B0Token: beiktatott, B1IsInLexic: true, B1Lemma: rendelkezés, B1POS: N, B1Token: rendelkezések, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [beiktatott]   B= [rendelkezések, viszont, már ,.. ]

B0IsInLexic: true, B0Lemma: rendelkezés, B0POS: N, B0Token: rendelkezések, B1Lemma: viszont, B1POS: C, B1Token: viszont, S0B0Lemma: beiktatott_rendelkezés, S0B0LemmaPOS: beiktatott_N, S0B0POS: A_N, S0B0POSLemma: A_rendelkezés, S0B0Token: beiktatott_rendelkezések, S0B1Lemma: beiktatott_viszont, S0B1LemmaPOS: beiktatott_C, S0B1POS: A_C, S0B1POSLemma: A_viszont, S0B1Token: beiktatott_viszont, S0Lemma: beiktatott, S0POS: A, S0Token: beiktatott, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, beiktatott_isGouvernedBy_rendelkezés: true, beiktatott_isGouvernedBy_rendelkezés_ATT: true, 

18- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [rendelkezések, viszont, már ,.. ]

B0IsInLexic: true, B0Lemma: rendelkezés, B0POS: N, B0Token: rendelkezések, B1Lemma: viszont, B1POS: C, B1Token: viszont, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [rendelkezések]   B= [viszont, már, több ,.. ]

B0Lemma: viszont, B0POS: C, B0Token: viszont, B1Lemma: már, B1POS: R, B1Token: már, S0B0Lemma: rendelkezés_viszont, S0B0LemmaPOS: rendelkezés_C, S0B0POS: N_C, S0B0POSLemma: N_viszont, S0B0Token: rendelkezések_viszont, S0B1Lemma: rendelkezés_már, S0B1LemmaPOS: rendelkezés_R, S0B1POS: N_R, S0B1POSLemma: N_már, S0B1Token: rendelkezések_már, S0IsInLexic: true, S0Lemma: rendelkezés, S0POS: N, S0Token: rendelkezések, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, rendelkezés_isGouvernedBy_ad: true, rendelkezés_isGouvernedBy_ad_SUBJ: true, 

20- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [viszont, már, több ,.. ]

B0Lemma: viszont, B0POS: C, B0Token: viszont, B1Lemma: már, B1POS: R, B1Token: már, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [viszont]   B= [már, több, támpontot ,.. ]

B0Lemma: már, B0POS: R, B0Token: már, B1Lemma: több, B1POS: M, B1Token: több, S0B0Lemma: viszont_már, S0B0LemmaPOS: viszont_R, S0B0POS: C_R, S0B0POSLemma: C_már, S0B0Token: viszont_már, S0B1Lemma: viszont_több, S0B1LemmaPOS: viszont_M, S0B1POS: C_M, S0B1POSLemma: C_több, S0B1Token: viszont_több, S0Lemma: viszont, S0POS: C, S0Token: viszont, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, viszont_isGouvernedBy_ad: true, viszont_isGouvernedBy_ad_CONJ: true, 

22- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [már, több, támpontot ,.. ]

B0Lemma: már, B0POS: R, B0Token: már, B1Lemma: több, B1POS: M, B1Token: több, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

23- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [már]   B= [több, támpontot, adtak ,.. ]

B0Lemma: több, B0POS: M, B0Token: több, B1IsInLexic: true, B1Lemma: támpont, B1POS: N, B1Token: támpontot, S0B0Lemma: már_több, S0B0LemmaPOS: már_M, S0B0POS: R_M, S0B0POSLemma: R_több, S0B0Token: már_több, S0B1Lemma: már_támpont, S0B1LemmaPOS: már_N, S0B1POS: R_N, S0B1POSLemma: R_támpont, S0B1Token: már_támpontot, S0Lemma: már, S0POS: R, S0Token: már, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, már_isGouvernedBy_ad: true, már_isGouvernedBy_ad_TLOCY: true, 

24- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [több, támpontot, adtak ,.. ]

B0Lemma: több, B0POS: M, B0Token: több, B1IsInLexic: true, B1Lemma: támpont, B1POS: N, B1Token: támpontot, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

25- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [több]   B= [támpontot, adtak, a ,.. ]

B0IsInLexic: true, B0Lemma: támpont, B0POS: N, B0Token: támpontot, B1IsInLexic: true, B1Lemma: ad, B1POS: V, B1Token: adtak, S0B0Lemma: több_támpont, S0B0LemmaPOS: több_N, S0B0POS: M_N, S0B0POSLemma: M_támpont, S0B0Token: több_támpontot, S0B1Lemma: több_ad, S0B1LemmaPOS: több_V, S0B1POS: M_V, S0B1POSLemma: M_ad, S0B1Token: több_adtak, S0Lemma: több, S0POS: M, S0Token: több, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, több_isGouvernedBy_támpont: true, több_isGouvernedBy_támpont_ATT: true, 

26- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [támpontot, adtak, a ,.. ]

B0IsInLexic: true, B0Lemma: támpont, B0POS: N, B0Token: támpontot, B1IsInLexic: true, B1Lemma: ad, B1POS: V, B1Token: adtak, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

27- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [támpontot]   B= [adtak, a, gyakorlat ,.. ]

B0IsInLexic: true, B0Lemma: ad, B0POS: V, B0Token: adtak, B1Lemma: a, B1POS: T, B1Token: a, S0B0Lemma: támpont_ad, S0B0LemmaPOS: támpont_V, S0B0POS: N_V, S0B0POSLemma: N_ad, S0B0Token: támpontot_adtak, S0B1Lemma: támpont_a, S0B1LemmaPOS: támpont_T, S0B1POS: N_T, S0B1POSLemma: N_a, S0B1Token: támpontot_a, S0IsInLexic: true, S0Lemma: támpont, S0POS: N, S0Token: támpontot, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, támpont_isGouvernedBy_ad: true, támpont_isGouvernedBy_ad_OBJ: true, 

28- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [támpontot, adtak]   B= [a, gyakorlat, számára ,.. ]

B0Lemma: a, B0POS: T, B0Token: a, B1Lemma: gyakorlat, B1POS: N, B1Token: gyakorlat, S0B0Lemma: ad_a, S0B0LemmaPOS: ad_T, S0B0POS: V_T, S0B0POSLemma: V_a, S0B0Token: adtak_a, S0B1Lemma: ad_gyakorlat, S0B1LemmaPOS: ad_N, S0B1POS: V_N, S0B1POSLemma: V_gyakorlat, S0B1Token: adtak_gyakorlat, S0IsInLexic: true, S0Lemma: ad, S0POS: V, S0Token: adtak, S1B0Lemma: támpont_a, S1B0LemmaPOS: támpont_T, S1B0POS: N_T, S1B0POSLemma: N_a, S1B0Token: támpontot_a, S1IsInLexic: true, S1Lemma: támpont, S1POS: N, S1S0B0Lemma: támpont_ad_a, S1S0B0LemmaPOS: támpont_V_T, S1S0B0POS: N_V_T, S1S0B0POSLemma: N_V_a, S1S0B0Token: támpontot_adtak_a, S1S0Lemma: támpont_ad, S1S0LemmaPOS: támpont_V, S1S0POS: N_V, S1S0POSLemma: N_ad, S1S0Token: támpontot_adtak, S1Token: támpontot, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

29- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[támpontot, adtak]]   B= [a, gyakorlat, számára ,.. ]

B0Lemma: a, B0POS: T, B0Token: a, B1Lemma: gyakorlat, B1POS: N, B1Token: gyakorlat, S0B0Lemma: támpont_ad_a, S0B0LemmaPOS: támpont_ad_T, S0B0POS: N_V_T, S0B0POSLemma: N_V_a, S0B0Token: támpontot_adtak_a, S0B1Lemma: támpont_ad_gyakorlat, S0B1LemmaPOS: támpont_ad_N, S0B1POS: N_V_N, S0B1POSLemma: N_V_gyakorlat, S0B1Token: támpontot_adtak_gyakorlat, S0Lemma: támpont_ad, S0POS: N_V, S0Token: támpontot_adtak, TransHistory1: 0, TransHistory2: 00, TransHistory3: 002, 

30- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [a, gyakorlat, számára ,.. ]

B0Lemma: a, B0POS: T, B0Token: a, B1Lemma: gyakorlat, B1POS: N, B1Token: gyakorlat, TransHistory1: 1, TransHistory2: 10, TransHistory3: 100, 

31- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [a]   B= [gyakorlat, számára, , ,.. ]

B0Lemma: gyakorlat, B0POS: N, B0Token: gyakorlat, B1Lemma: számára, B1POS: S, B1Token: számára, S0B0Lemma: a_gyakorlat, S0B0LemmaPOS: a_N, S0B0POS: T_N, S0B0POSLemma: T_gyakorlat, S0B0Token: a_gyakorlat, S0B1Lemma: a_számára, S0B1LemmaPOS: a_S, S0B1POS: T_S, S0B1POSLemma: T_számára, S0B1Token: a_számára, S0Lemma: a, S0POS: T, S0Token: a, TransHistory1: 2, TransHistory2: 21, TransHistory3: 210, a_isGouvernedBy_gyakorlat: true, a_isGouvernedBy_gyakorlat_DET: true, 

32- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [gyakorlat, számára, , ,.. ]

B0Lemma: gyakorlat, B0POS: N, B0Token: gyakorlat, B1Lemma: számára, B1POS: S, B1Token: számára, TransHistory1: 0, TransHistory2: 02, TransHistory3: 021, 

33- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [gyakorlat]   B= [számára, ,, de ,.. ]

B0Lemma: számára, B0POS: S, B0Token: számára, B1Lemma: ,, B1POS: ,, B1Token: ,, S0B0Lemma: gyakorlat_számára, S0B0LemmaPOS: gyakorlat_S, S0B0POS: N_S, S0B0POSLemma: N_számára, S0B0Token: gyakorlat_számára, S0B1Lemma: gyakorlat_,, S0B1LemmaPOS: gyakorlat_,, S0B1POS: N_,, S0B1POSLemma: N_,, S0B1Token: gyakorlat_,, S0Lemma: gyakorlat, S0POS: N, S0Token: gyakorlat, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, gyakorlat_isGouvernedBy_számára: true, gyakorlat_isGouvernedBy_számára_ATT: true, 

34- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [számára, ,, de ,.. ]

B0Lemma: számára, B0POS: S, B0Token: számára, B1Lemma: ,, B1POS: ,, B1Token: ,, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

35- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [számára]   B= [,, de, az ,.. ]

B0Lemma: ,, B0POS: ,, B0Token: ,, B1Lemma: de, B1POS: C, B1Token: de, S0B0Lemma: számára_,, S0B0LemmaPOS: számára_,, S0B0POS: S_,, S0B0POSLemma: S_,, S0B0Token: számára_,, S0B1Lemma: számára_de, S0B1LemmaPOS: számára_C, S0B1POS: S_C, S0B1POSLemma: S_de, S0B1Token: számára_de, S0Lemma: számára, S0POS: S, S0Token: számára, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

36- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, de, az ,.. ]

B0Lemma: ,, B0POS: ,, B0Token: ,, B1Lemma: de, B1POS: C, B1Token: de, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

37- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [de, az, egyesülésre ,.. ]

B0Lemma: de, B0POS: C, B0Token: de, B1Lemma: az, B1POS: T, B1Token: az, S0B0Lemma: ,_de, S0B0LemmaPOS: ,_C, S0B0POS: ,_C, S0B0POSLemma: ,_de, S0B0Token: ,_de, S0B1Lemma: ,_az, S0B1LemmaPOS: ,_T, S0B1POS: ,_T, S0B1POSLemma: ,_az, S0B1Token: ,_az, S0Lemma: ,, S0POS: ,, S0Token: ,, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

38- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [de, az, egyesülésre ,.. ]

B0Lemma: de, B0POS: C, B0Token: de, B1Lemma: az, B1POS: T, B1Token: az, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

39- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [de]   B= [az, egyesülésre, való ,.. ]

B0Lemma: az, B0POS: T, B0Token: az, B1Lemma: egyesülés, B1POS: N, B1Token: egyesülésre, S0B0Lemma: de_az, S0B0LemmaPOS: de_T, S0B0POS: C_T, S0B0POSLemma: C_az, S0B0Token: de_az, S0B1Lemma: de_egyesülés, S0B1LemmaPOS: de_N, S0B1POS: C_N, S0B1POSLemma: C_egyesülés, S0B1Token: de_egyesülésre, S0Lemma: de, S0POS: C, S0Token: de, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, de_ad_hasRighDep_COORD: true, de_hasRighDep_COORD: true, hasRighDep_COORD: true, 

40- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [az, egyesülésre, való ,.. ]

B0Lemma: az, B0POS: T, B0Token: az, B1Lemma: egyesülés, B1POS: N, B1Token: egyesülésre, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

41- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [az]   B= [egyesülésre, való, visszautalásnak ,.. ]

B0Lemma: egyesülés, B0POS: N, B0Token: egyesülésre, B1Lemma: való, B1POS: A, B1Token: való, S0B0Lemma: az_egyesülés, S0B0LemmaPOS: az_N, S0B0POS: T_N, S0B0POSLemma: T_egyesülés, S0B0Token: az_egyesülésre, S0B1Lemma: az_való, S0B1LemmaPOS: az_A, S0B1POS: T_A, S0B1POSLemma: T_való, S0B1Token: az_való, S0Lemma: az, S0POS: T, S0Token: az, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, az_isGouvernedBy_egyesülés: true, az_isGouvernedBy_egyesülés_DET: true, 

42- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [egyesülésre, való, visszautalásnak ,.. ]

B0Lemma: egyesülés, B0POS: N, B0Token: egyesülésre, B1Lemma: való, B1POS: A, B1Token: való, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

43- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [egyesülésre]   B= [való, visszautalásnak, még ,.. ]

B0Lemma: való, B0POS: A, B0Token: való, B1Lemma: visszautalás, B1POS: N, B1Token: visszautalásnak, S0B0Lemma: egyesülés_való, S0B0LemmaPOS: egyesülés_A, S0B0POS: N_A, S0B0POSLemma: N_való, S0B0Token: egyesülésre_való, S0B1Lemma: egyesülés_visszautalás, S0B1LemmaPOS: egyesülés_N, S0B1POS: N_N, S0B1POSLemma: N_visszautalás, S0B1Token: egyesülésre_visszautalásnak, S0Lemma: egyesülés, S0POS: N, S0Token: egyesülésre, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, egyesülés_isGouvernedBy_való: true, egyesülés_isGouvernedBy_való_OBL: true, 

44- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [való, visszautalásnak, még ,.. ]

B0Lemma: való, B0POS: A, B0Token: való, B1Lemma: visszautalás, B1POS: N, B1Token: visszautalásnak, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

45- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [való]   B= [visszautalásnak, még, mindig ,.. ]

B0Lemma: visszautalás, B0POS: N, B0Token: visszautalásnak, B1Lemma: még, B1POS: R, B1Token: még, S0B0Lemma: való_visszautalás, S0B0LemmaPOS: való_N, S0B0POS: A_N, S0B0POSLemma: A_visszautalás, S0B0Token: való_visszautalásnak, S0B1Lemma: való_még, S0B1LemmaPOS: való_R, S0B1POS: A_R, S0B1POSLemma: A_még, S0B1Token: való_még, S0Lemma: való, S0POS: A, S0Token: való, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, való_isGouvernedBy_visszautalás: true, való_isGouvernedBy_visszautalás_ATT: true, 

46- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [visszautalásnak, még, mindig ,.. ]

B0Lemma: visszautalás, B0POS: N, B0Token: visszautalásnak, B1Lemma: még, B1POS: R, B1Token: még, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

47- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [visszautalásnak]   B= [még, mindig, tág ,.. ]

B0Lemma: még, B0POS: R, B0Token: még, B1Lemma: mindig, B1POS: R, B1Token: mindig, S0B0Lemma: visszautalás_még, S0B0LemmaPOS: visszautalás_R, S0B0POS: N_R, S0B0POSLemma: N_még, S0B0Token: visszautalásnak_még, S0B1Lemma: visszautalás_mindig, S0B1LemmaPOS: visszautalás_R, S0B1POS: N_R, S0B1POSLemma: N_mindig, S0B1Token: visszautalásnak_mindig, S0Lemma: visszautalás, S0POS: N, S0Token: visszautalásnak, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, visszautalás_isGouvernedBy_ad: true, visszautalás_isGouvernedBy_ad_DAT: true, 

48- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [még, mindig, tág ,.. ]

B0Lemma: még, B0POS: R, B0Token: még, B1Lemma: mindig, B1POS: R, B1Token: mindig, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

49- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [még]   B= [mindig, tág, teret ,.. ]

B0Lemma: mindig, B0POS: R, B0Token: mindig, B1Lemma: tág, B1POS: A, B1Token: tág, S0B0Lemma: még_mindig, S0B0LemmaPOS: még_R, S0B0POS: R_R, S0B0POSLemma: R_mindig, S0B0Token: még_mindig, S0B1Lemma: még_tág, S0B1LemmaPOS: még_A, S0B1POS: R_A, S0B1POSLemma: R_tág, S0B1Token: még_tág, S0Lemma: még, S0POS: R, S0Token: még, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, még_isGouvernedBy_ad: true, még_isGouvernedBy_ad_TLOCY: true, 

50- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [mindig, tág, teret ,.. ]

B0Lemma: mindig, B0POS: R, B0Token: mindig, B1Lemma: tág, B1POS: A, B1Token: tág, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

51- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [mindig]   B= [tág, teret, adtak ,.. ]

B0Lemma: tág, B0POS: A, B0Token: tág, B1IsInLexic: true, B1Lemma: tér, B1POS: N, B1Token: teret, S0B0Lemma: mindig_tág, S0B0LemmaPOS: mindig_A, S0B0POS: R_A, S0B0POSLemma: R_tág, S0B0Token: mindig_tág, S0B1Lemma: mindig_tér, S0B1LemmaPOS: mindig_N, S0B1POS: R_N, S0B1POSLemma: R_tér, S0B1Token: mindig_teret, S0Lemma: mindig, S0POS: R, S0Token: mindig, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, mindig_isGouvernedBy_ad: true, mindig_isGouvernedBy_ad_TLOCY: true, 

52- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [tág, teret, adtak ,.. ]

B0Lemma: tág, B0POS: A, B0Token: tág, B1IsInLexic: true, B1Lemma: tér, B1POS: N, B1Token: teret, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

53- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [tág]   B= [teret, adtak, . ,.. ]

B0IsInLexic: true, B0Lemma: tér, B0POS: N, B0Token: teret, B1IsInLexic: true, B1Lemma: ad, B1POS: V, B1Token: adtak, S0B0Lemma: tág_tér, S0B0LemmaPOS: tág_N, S0B0POS: A_N, S0B0POSLemma: A_tér, S0B0Token: tág_teret, S0B1Lemma: tág_ad, S0B1LemmaPOS: tág_V, S0B1POS: A_V, S0B1POSLemma: A_ad, S0B1Token: tág_adtak, S0Lemma: tág, S0POS: A, S0Token: tág, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, tág_isGouvernedBy_tér: true, tág_isGouvernedBy_tér_ATT: true, 

54- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [teret, adtak, . ,.. ]

B0IsInLexic: true, B0Lemma: tér, B0POS: N, B0Token: teret, B1IsInLexic: true, B1Lemma: ad, B1POS: V, B1Token: adtak, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

55- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [teret]   B= [adtak, . ,.. ]

B0IsInLexic: true, B0Lemma: ad, B0POS: V, B0Token: adtak, B1Lemma: ., B1POS: ., B1Token: ., S0B0Lemma: tér_ad, S0B0LemmaPOS: tér_V, S0B0POS: N_V, S0B0POSLemma: N_ad, S0B0Token: teret_adtak, S0B1Lemma: tér_., S0B1LemmaPOS: tér_., S0B1POS: N_., S0B1POSLemma: N_., S0B1Token: teret_., S0IsInLexic: true, S0Lemma: tér, S0POS: N, S0Token: teret, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, tér_isGouvernedBy_ad: true, tér_isGouvernedBy_ad_OBJ: true, 

56- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [teret, adtak]   B= [.]

B0Lemma: ., B0POS: ., B0Token: ., S0B0Lemma: ad_., S0B0LemmaPOS: ad_., S0B0POS: V_., S0B0POSLemma: V_., S0B0Token: adtak_., S0IsInLexic: true, S0Lemma: ad, S0POS: V, S0Token: adtak, S1B0Lemma: tér_., S1B0LemmaPOS: tér_., S1B0POS: N_., S1B0POSLemma: N_., S1B0Token: teret_., S1IsInLexic: true, S1Lemma: tér, S1POS: N, S1S0B0Lemma: tér_ad_., S1S0B0LemmaPOS: tér_V_., S1S0B0POS: N_V_., S1S0B0POSLemma: N_V_., S1S0B0Token: teret_adtak_., S1S0Lemma: tér_ad, S1S0LemmaPOS: tér_V, S1S0POS: N_V, S1S0POSLemma: N_ad, S1S0Token: teret_adtak, S1Token: teret, SyntaxicRelation: -OBJ, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

57- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[teret, adtak]]   B= [.]

B0Lemma: ., B0POS: ., B0Token: ., S0B0Lemma: tér_ad_., S0B0LemmaPOS: tér_ad_., S0B0POS: N_V_., S0B0POSLemma: N_V_., S0B0Token: teret_adtak_., S0Lemma: tér_ad, S0POS: N_V, S0Token: teret_adtak, TransHistory1: 0, TransHistory2: 00, TransHistory3: 002, 

58- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [.]

B0Lemma: ., B0POS: ., B0Token: ., TransHistory1: 1, TransHistory2: 10, TransHistory3: 100, 

59- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [ ]

S0Lemma: ., S0POS: ., S0Token: ., TransHistory1: 2, TransHistory2: 21, TransHistory3: 210, 

60- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

## Sentence No. 251 - 
a szétválás a gt. ( új ) 78. § (1) bekezdéseiben említett két formáját , a különválást és a kiválást a gt. ( új ) 78. § (3)-(4) bekezdése részletezi . 
### Existing MWEs: 
1- **bekezdéseiben** (VPC)
2- **bekezdése** (VPC)



0- &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [a, szétválás, a ,.. ]

B0Lemma: a, B0POS: T, B0Token: a, B1Lemma: szétválás, B1POS: N, B1Token: szétválás, 

1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [a]   B= [szétválás, a, gt. ,.. ]

B0Lemma: szétválás, B0POS: N, B0Token: szétválás, B1Lemma: a, B1POS: T, B1Token: a, S0B0Lemma: a_szétválás, S0B0LemmaPOS: a_N, S0B0POS: T_N, S0B0POSLemma: T_szétválás, S0B0Token: a_szétválás, S0B1Lemma: a_a, S0B1LemmaPOS: a_T, S0B1POS: T_T, S0B1POSLemma: T_a, S0B1Token: a_a, S0Lemma: a, S0POS: T, S0Token: a, a_isGouvernedBy_szétválás: true, a_isGouvernedBy_szétválás_DET: true, 

2- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [szétválás, a, gt. ,.. ]

B0Lemma: szétválás, B0POS: N, B0Token: szétválás, B1Lemma: a, B1POS: T, B1Token: a, TransHistory1: 0, 

3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [szétválás]   B= [a, gt., ( ,.. ]

B0Lemma: a, B0POS: T, B0Token: a, B1Lemma: Gt., B1POS: N, B1Token: gt., S0B0Lemma: szétválás_a, S0B0LemmaPOS: szétválás_T, S0B0POS: N_T, S0B0POSLemma: N_a, S0B0Token: szétválás_a, S0B1Lemma: szétválás_Gt., S0B1LemmaPOS: szétválás_N, S0B1POS: N_N, S0B1POSLemma: N_Gt., S0B1Token: szétválás_gt., S0Lemma: szétválás, S0POS: N, S0Token: szétválás, TransHistory1: 2, TransHistory2: 20, szétválás_isGouvernedBy_forma: true, szétválás_isGouvernedBy_forma_ATT: true, 

4- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [a, gt., ( ,.. ]

B0Lemma: a, B0POS: T, B0Token: a, B1Lemma: Gt., B1POS: N, B1Token: gt., TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [a]   B= [gt., (, új ,.. ]

B0Lemma: Gt., B0POS: N, B0Token: gt., B1Lemma: (, B1POS: (, B1Token: (, S0B0Lemma: a_Gt., S0B0LemmaPOS: a_N, S0B0POS: T_N, S0B0POSLemma: T_Gt., S0B0Token: a_gt., S0B1Lemma: a_(, S0B1LemmaPOS: a_(, S0B1POS: T_(, S0B1POSLemma: T_(, S0B1Token: a_(, S0Lemma: a, S0POS: T, S0Token: a, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, a_isGouvernedBy_§: true, a_isGouvernedBy_§_DET: true, 

6- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [gt., (, új ,.. ]

B0Lemma: Gt., B0POS: N, B0Token: gt., B1Lemma: (, B1POS: (, B1Token: (, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [gt.]   B= [(, új, ) ,.. ]

B0Lemma: (, B0POS: (, B0Token: (, B1Lemma: új, B1POS: A, B1Token: új, Gt._hasRighDep_ATT: true, Gt._isGouvernedBy_§: true, Gt._isGouvernedBy_§_ATT: true, Gt._új_hasRighDep_ATT: true, S0B0Lemma: Gt._(, S0B0LemmaPOS: Gt._(, S0B0POS: N_(, S0B0POSLemma: N_(, S0B0Token: gt._(, S0B1Lemma: Gt._új, S0B1LemmaPOS: Gt._A, S0B1POS: N_A, S0B1POSLemma: N_új, S0B1Token: gt._új, S0Lemma: Gt., S0POS: N, S0Token: gt., TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, hasRighDep_ATT: true, 

8- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [(, új, ) ,.. ]

B0Lemma: (, B0POS: (, B0Token: (, B1Lemma: új, B1POS: A, B1Token: új, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [(]   B= [új, ), 78. ,.. ]

(_isGouvernedBy_új: true, (_isGouvernedBy_új_PUNCT: true, B0Lemma: új, B0POS: A, B0Token: új, B1Lemma: ), B1POS: ), B1Token: ), S0B0Lemma: (_új, S0B0LemmaPOS: (_A, S0B0POS: (_A, S0B0POSLemma: (_új, S0B0Token: (_új, S0B1Lemma: (_), S0B1LemmaPOS: (_), S0B1POS: (_), S0B1POSLemma: (_), S0B1Token: (_), S0Lemma: (, S0POS: (, S0Token: (, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

10- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [új, ), 78. ,.. ]

B0Lemma: új, B0POS: A, B0Token: új, B1Lemma: ), B1POS: ), B1Token: ), TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [új]   B= [), 78., § ,.. ]

B0Lemma: ), B0POS: ), B0Token: ), B1Lemma: 78., B1POS: M, B1Token: 78., S0B0Lemma: új_), S0B0LemmaPOS: új_), S0B0POS: A_), S0B0POSLemma: A_), S0B0Token: új_), S0B1Lemma: új_78., S0B1LemmaPOS: új_M, S0B1POS: A_M, S0B1POSLemma: A_78., S0B1Token: új_78., S0Lemma: új, S0POS: A, S0Token: új, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, hasRighDep_PUNCT: true, új_)_hasRighDep_PUNCT: true, új_hasRighDep_PUNCT: true, 

12- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [), 78., § ,.. ]

B0Lemma: ), B0POS: ), B0Token: ), B1Lemma: 78., B1POS: M, B1Token: 78., TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [)]   B= [78., §, (1) ,.. ]

B0Lemma: 78., B0POS: M, B0Token: 78., B1Lemma: §, B1POS: §, B1Token: §, S0B0Lemma: )_78., S0B0LemmaPOS: )_M, S0B0POS: )_M, S0B0POSLemma: )_78., S0B0Token: )_78., S0B1Lemma: )_§, S0B1LemmaPOS: )_§, S0B1POS: )_§, S0B1POSLemma: )_§, S0B1Token: )_§, S0Lemma: ), S0POS: ), S0Token: ), TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

14- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [78., §, (1) ,.. ]

B0Lemma: 78., B0POS: M, B0Token: 78., B1Lemma: §, B1POS: §, B1Token: §, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [78.]   B= [§, (1), bekezdéseiben ,.. ]

78._isGouvernedBy_§: true, 78._isGouvernedBy_§_ATT: true, B0Lemma: §, B0POS: §, B0Token: §, B1Lemma: (1), B1POS: O, B1Token: (1), S0B0Lemma: 78._§, S0B0LemmaPOS: 78._§, S0B0POS: M_§, S0B0POSLemma: M_§, S0B0Token: 78._§, S0B1Lemma: 78._(1), S0B1LemmaPOS: 78._O, S0B1POS: M_O, S0B1POSLemma: M_(1), S0B1Token: 78._(1), S0Lemma: 78., S0POS: M, S0Token: 78., TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

16- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [§, (1), bekezdéseiben ,.. ]

B0Lemma: §, B0POS: §, B0Token: §, B1Lemma: (1), B1POS: O, B1Token: (1), TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [§]   B= [(1), bekezdéseiben, említett ,.. ]

B0Lemma: (1), B0POS: O, B0Token: (1), B1IsInLexic: true, B1Lemma: bekezdés, B1POS: N, B1Token: bekezdéseiben, S0B0Lemma: §_(1), S0B0LemmaPOS: §_O, S0B0POS: §_O, S0B0POSLemma: §_(1), S0B0Token: §_(1), S0B1Lemma: §_bekezdés, S0B1LemmaPOS: §_N, S0B1POS: §_N, S0B1POSLemma: §_bekezdés, S0B1Token: §_bekezdéseiben, S0Lemma: §, S0POS: §, S0Token: §, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, §_isGouvernedBy_bekezdés: true, §_isGouvernedBy_bekezdés_ATT: true, 

18- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [(1), bekezdéseiben, említett ,.. ]

B0Lemma: (1), B0POS: O, B0Token: (1), B1IsInLexic: true, B1Lemma: bekezdés, B1POS: N, B1Token: bekezdéseiben, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [(1)]   B= [bekezdéseiben, említett, két ,.. ]

(1)_isGouvernedBy_bekezdés: true, (1)_isGouvernedBy_bekezdés_ATT: true, B0IsInLexic: true, B0Lemma: bekezdés, B0POS: N, B0Token: bekezdéseiben, B1Lemma: említett, B1POS: A, B1Token: említett, S0B0Lemma: (1)_bekezdés, S0B0LemmaPOS: (1)_N, S0B0POS: O_N, S0B0POSLemma: O_bekezdés, S0B0Token: (1)_bekezdéseiben, S0B1Lemma: (1)_említett, S0B1LemmaPOS: (1)_A, S0B1POS: O_A, S0B1POSLemma: O_említett, S0B1Token: (1)_említett, S0Lemma: (1), S0POS: O, S0Token: (1), TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

20- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [bekezdéseiben, említett, két ,.. ]

B0IsInLexic: true, B0Lemma: bekezdés, B0POS: N, B0Token: bekezdéseiben, B1Lemma: említett, B1POS: A, B1Token: említett, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [bekezdéseiben]   B= [említett, két, formáját ,.. ]

B0Lemma: említett, B0POS: A, B0Token: említett, B1Lemma: két, B1POS: M, B1Token: két, S0B0Lemma: bekezdés_említett, S0B0LemmaPOS: bekezdés_A, S0B0POS: N_A, S0B0POSLemma: N_említett, S0B0Token: bekezdéseiben_említett, S0B1Lemma: bekezdés_két, S0B1LemmaPOS: bekezdés_M, S0B1POS: N_M, S0B1POSLemma: N_két, S0B1Token: bekezdéseiben_két, S0IsInLexic: true, S0Lemma: bekezdés, S0POS: N, S0Token: bekezdéseiben, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, bekezdés_isGouvernedBy_említett: true, bekezdés_isGouvernedBy_említett_OBL: true, 

22- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [említett, két, formáját ,.. ]

B0Lemma: említett, B0POS: A, B0Token: említett, B1Lemma: két, B1POS: M, B1Token: két, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

23- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [említett]   B= [két, formáját, , ,.. ]

B0Lemma: két, B0POS: M, B0Token: két, B1Lemma: forma, B1POS: N, B1Token: formáját, S0B0Lemma: említett_két, S0B0LemmaPOS: említett_M, S0B0POS: A_M, S0B0POSLemma: A_két, S0B0Token: említett_két, S0B1Lemma: említett_forma, S0B1LemmaPOS: említett_N, S0B1POS: A_N, S0B1POSLemma: A_forma, S0B1Token: említett_formáját, S0Lemma: említett, S0POS: A, S0Token: említett, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, említett_isGouvernedBy_forma: true, említett_isGouvernedBy_forma_ATT: true, 

24- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [két, formáját, , ,.. ]

B0Lemma: két, B0POS: M, B0Token: két, B1Lemma: forma, B1POS: N, B1Token: formáját, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

25- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [két]   B= [formáját, ,, a ,.. ]

B0Lemma: forma, B0POS: N, B0Token: formáját, B1Lemma: ,, B1POS: ,, B1Token: ,, S0B0Lemma: két_forma, S0B0LemmaPOS: két_N, S0B0POS: M_N, S0B0POSLemma: M_forma, S0B0Token: két_formáját, S0B1Lemma: két_,, S0B1LemmaPOS: két_,, S0B1POS: M_,, S0B1POSLemma: M_,, S0B1Token: két_,, S0Lemma: két, S0POS: M, S0Token: két, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, két_isGouvernedBy_forma: true, két_isGouvernedBy_forma_ATT: true, 

26- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [formáját, ,, a ,.. ]

B0Lemma: forma, B0POS: N, B0Token: formáját, B1Lemma: ,, B1POS: ,, B1Token: ,, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

27- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [formáját]   B= [,, a, különválást ,.. ]

B0Lemma: ,, B0POS: ,, B0Token: ,, B1Lemma: a, B1POS: T, B1Token: a, S0B0Lemma: forma_,, S0B0LemmaPOS: forma_,, S0B0POS: N_,, S0B0POSLemma: N_,, S0B0Token: formáját_,, S0B1Lemma: forma_a, S0B1LemmaPOS: forma_T, S0B1POS: N_T, S0B1POSLemma: N_a, S0B1Token: formáját_a, S0Lemma: forma, S0POS: N, S0Token: formáját, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, forma_,_hasRighDep_PUNCT: true, forma_hasRighDep_COORD: true, forma_hasRighDep_PUNCT: true, forma_isGouvernedBy_részletez: true, forma_isGouvernedBy_részletez_OBJ: true, forma_különválás_hasRighDep_COORD: true, hasRighDep_COORD: true, hasRighDep_PUNCT: true, 

28- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, a, különválást ,.. ]

B0Lemma: ,, B0POS: ,, B0Token: ,, B1Lemma: a, B1POS: T, B1Token: a, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

29- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [a, különválást, és ,.. ]

B0Lemma: a, B0POS: T, B0Token: a, B1Lemma: különválás, B1POS: N, B1Token: különválást, S0B0Lemma: ,_a, S0B0LemmaPOS: ,_T, S0B0POS: ,_T, S0B0POSLemma: ,_a, S0B0Token: ,_a, S0B1Lemma: ,_különválás, S0B1LemmaPOS: ,_N, S0B1POS: ,_N, S0B1POSLemma: ,_különválás, S0B1Token: ,_különválást, S0Lemma: ,, S0POS: ,, S0Token: ,, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

30- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [a, különválást, és ,.. ]

B0Lemma: a, B0POS: T, B0Token: a, B1Lemma: különválás, B1POS: N, B1Token: különválást, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

31- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [a]   B= [különválást, és, a ,.. ]

B0Lemma: különválás, B0POS: N, B0Token: különválást, B1Lemma: és, B1POS: C, B1Token: és, S0B0Lemma: a_különválás, S0B0LemmaPOS: a_N, S0B0POS: T_N, S0B0POSLemma: T_különválás, S0B0Token: a_különválást, S0B1Lemma: a_és, S0B1LemmaPOS: a_C, S0B1POS: T_C, S0B1POSLemma: T_és, S0B1Token: a_és, S0Lemma: a, S0POS: T, S0Token: a, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, a_isGouvernedBy_különválás: true, a_isGouvernedBy_különválás_DET: true, 

32- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [különválást, és, a ,.. ]

B0Lemma: különválás, B0POS: N, B0Token: különválást, B1Lemma: és, B1POS: C, B1Token: és, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

33- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [különválást]   B= [és, a, kiválást ,.. ]

B0Lemma: és, B0POS: C, B0Token: és, B1Lemma: a, B1POS: T, B1Token: a, S0B0Lemma: különválás_és, S0B0LemmaPOS: különválás_C, S0B0POS: N_C, S0B0POSLemma: N_és, S0B0Token: különválást_és, S0B1Lemma: különválás_a, S0B1LemmaPOS: különválás_T, S0B1POS: N_T, S0B1POSLemma: N_a, S0B1Token: különválást_a, S0Lemma: különválás, S0POS: N, S0Token: különválást, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, hasRighDep_ATT: true, különválás_hasRighDep_ATT: true, különválás_és_hasRighDep_ATT: true, 

34- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [és, a, kiválást ,.. ]

B0Lemma: és, B0POS: C, B0Token: és, B1Lemma: a, B1POS: T, B1Token: a, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

35- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [és]   B= [a, kiválást, a ,.. ]

B0Lemma: a, B0POS: T, B0Token: a, B1Lemma: kiválás, B1POS: N, B1Token: kiválást, S0B0Lemma: és_a, S0B0LemmaPOS: és_T, S0B0POS: C_T, S0B0POSLemma: C_a, S0B0Token: és_a, S0B1Lemma: és_kiválás, S0B1LemmaPOS: és_N, S0B1POS: C_N, S0B1POSLemma: C_kiválás, S0B1Token: és_kiválást, S0Lemma: és, S0POS: C, S0Token: és, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, hasRighDep_COORD: true, és_hasRighDep_COORD: true, és_kiválás_hasRighDep_COORD: true, 

36- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [a, kiválást, a ,.. ]

B0Lemma: a, B0POS: T, B0Token: a, B1Lemma: kiválás, B1POS: N, B1Token: kiválást, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

37- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [a]   B= [kiválást, a, gt. ,.. ]

B0Lemma: kiválás, B0POS: N, B0Token: kiválást, B1Lemma: a, B1POS: T, B1Token: a, S0B0Lemma: a_kiválás, S0B0LemmaPOS: a_N, S0B0POS: T_N, S0B0POSLemma: T_kiválás, S0B0Token: a_kiválást, S0B1Lemma: a_a, S0B1LemmaPOS: a_T, S0B1POS: T_T, S0B1POSLemma: T_a, S0B1Token: a_a, S0Lemma: a, S0POS: T, S0Token: a, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, a_isGouvernedBy_kiválás: true, a_isGouvernedBy_kiválás_DET: true, 

38- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [kiválást, a, gt. ,.. ]

B0Lemma: kiválás, B0POS: N, B0Token: kiválást, B1Lemma: a, B1POS: T, B1Token: a, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

39- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [kiválást]   B= [a, gt., ( ,.. ]

B0Lemma: a, B0POS: T, B0Token: a, B1Lemma: Gt., B1POS: N, B1Token: gt., S0B0Lemma: kiválás_a, S0B0LemmaPOS: kiválás_T, S0B0POS: N_T, S0B0POSLemma: N_a, S0B0Token: kiválást_a, S0B1Lemma: kiválás_Gt., S0B1LemmaPOS: kiválás_N, S0B1POS: N_N, S0B1POSLemma: N_Gt., S0B1Token: kiválást_gt., S0Lemma: kiválás, S0POS: N, S0Token: kiválást, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

40- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [a, gt., ( ,.. ]

B0Lemma: a, B0POS: T, B0Token: a, B1Lemma: Gt., B1POS: N, B1Token: gt., TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

41- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [a]   B= [gt., (, új ,.. ]

B0Lemma: Gt., B0POS: N, B0Token: gt., B1Lemma: (, B1POS: (, B1Token: (, S0B0Lemma: a_Gt., S0B0LemmaPOS: a_N, S0B0POS: T_N, S0B0POSLemma: T_Gt., S0B0Token: a_gt., S0B1Lemma: a_(, S0B1LemmaPOS: a_(, S0B1POS: T_(, S0B1POSLemma: T_(, S0B1Token: a_(, S0Lemma: a, S0POS: T, S0Token: a, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, a_isGouvernedBy_§: true, a_isGouvernedBy_§_DET: true, 

42- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [gt., (, új ,.. ]

B0Lemma: Gt., B0POS: N, B0Token: gt., B1Lemma: (, B1POS: (, B1Token: (, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

43- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [gt.]   B= [(, új, ) ,.. ]

B0Lemma: (, B0POS: (, B0Token: (, B1Lemma: új, B1POS: A, B1Token: új, Gt._hasRighDep_ATT: true, Gt._isGouvernedBy_§: true, Gt._isGouvernedBy_§_ATT: true, Gt._új_hasRighDep_ATT: true, S0B0Lemma: Gt._(, S0B0LemmaPOS: Gt._(, S0B0POS: N_(, S0B0POSLemma: N_(, S0B0Token: gt._(, S0B1Lemma: Gt._új, S0B1LemmaPOS: Gt._A, S0B1POS: N_A, S0B1POSLemma: N_új, S0B1Token: gt._új, S0Lemma: Gt., S0POS: N, S0Token: gt., TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, hasRighDep_ATT: true, 

44- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [(, új, ) ,.. ]

B0Lemma: (, B0POS: (, B0Token: (, B1Lemma: új, B1POS: A, B1Token: új, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

45- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [(]   B= [új, ), 78. ,.. ]

(_isGouvernedBy_új: true, (_isGouvernedBy_új_PUNCT: true, B0Lemma: új, B0POS: A, B0Token: új, B1Lemma: ), B1POS: ), B1Token: ), S0B0Lemma: (_új, S0B0LemmaPOS: (_A, S0B0POS: (_A, S0B0POSLemma: (_új, S0B0Token: (_új, S0B1Lemma: (_), S0B1LemmaPOS: (_), S0B1POS: (_), S0B1POSLemma: (_), S0B1Token: (_), S0Lemma: (, S0POS: (, S0Token: (, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

46- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [új, ), 78. ,.. ]

B0Lemma: új, B0POS: A, B0Token: új, B1Lemma: ), B1POS: ), B1Token: ), TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

47- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [új]   B= [), 78., § ,.. ]

B0Lemma: ), B0POS: ), B0Token: ), B1Lemma: 78., B1POS: M, B1Token: 78., S0B0Lemma: új_), S0B0LemmaPOS: új_), S0B0POS: A_), S0B0POSLemma: A_), S0B0Token: új_), S0B1Lemma: új_78., S0B1LemmaPOS: új_M, S0B1POS: A_M, S0B1POSLemma: A_78., S0B1Token: új_78., S0Lemma: új, S0POS: A, S0Token: új, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, hasRighDep_PUNCT: true, új_)_hasRighDep_PUNCT: true, új_hasRighDep_PUNCT: true, 

48- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [), 78., § ,.. ]

B0Lemma: ), B0POS: ), B0Token: ), B1Lemma: 78., B1POS: M, B1Token: 78., TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

49- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [)]   B= [78., §, (3)-(4) ,.. ]

B0Lemma: 78., B0POS: M, B0Token: 78., B1Lemma: §, B1POS: §, B1Token: §, S0B0Lemma: )_78., S0B0LemmaPOS: )_M, S0B0POS: )_M, S0B0POSLemma: )_78., S0B0Token: )_78., S0B1Lemma: )_§, S0B1LemmaPOS: )_§, S0B1POS: )_§, S0B1POSLemma: )_§, S0B1Token: )_§, S0Lemma: ), S0POS: ), S0Token: ), TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

50- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [78., §, (3)-(4) ,.. ]

B0Lemma: 78., B0POS: M, B0Token: 78., B1Lemma: §, B1POS: §, B1Token: §, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

51- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [78.]   B= [§, (3)-(4), bekezdése ,.. ]

78._isGouvernedBy_§: true, 78._isGouvernedBy_§_ATT: true, B0Lemma: §, B0POS: §, B0Token: §, B1Lemma: (3)-(4), B1POS: O, B1Token: (3)-(4), S0B0Lemma: 78._§, S0B0LemmaPOS: 78._§, S0B0POS: M_§, S0B0POSLemma: M_§, S0B0Token: 78._§, S0B1Lemma: 78._(3)-(4), S0B1LemmaPOS: 78._O, S0B1POS: M_O, S0B1POSLemma: M_(3)-(4), S0B1Token: 78._(3)-(4), S0Lemma: 78., S0POS: M, S0Token: 78., TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

52- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [§, (3)-(4), bekezdése ,.. ]

B0Lemma: §, B0POS: §, B0Token: §, B1Lemma: (3)-(4), B1POS: O, B1Token: (3)-(4), TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

53- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [§]   B= [(3)-(4), bekezdése, részletezi ,.. ]

B0Lemma: (3)-(4), B0POS: O, B0Token: (3)-(4), B1IsInLexic: true, B1Lemma: bekezdés, B1POS: N, B1Token: bekezdése, S0B0Lemma: §_(3)-(4), S0B0LemmaPOS: §_O, S0B0POS: §_O, S0B0POSLemma: §_(3)-(4), S0B0Token: §_(3)-(4), S0B1Lemma: §_bekezdés, S0B1LemmaPOS: §_N, S0B1POS: §_N, S0B1POSLemma: §_bekezdés, S0B1Token: §_bekezdése, S0Lemma: §, S0POS: §, S0Token: §, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, §_isGouvernedBy_bekezdés: true, §_isGouvernedBy_bekezdés_ATT: true, 

54- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [(3)-(4), bekezdése, részletezi ,.. ]

B0Lemma: (3)-(4), B0POS: O, B0Token: (3)-(4), B1IsInLexic: true, B1Lemma: bekezdés, B1POS: N, B1Token: bekezdése, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

55- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [(3)-(4)]   B= [bekezdése, részletezi, . ,.. ]

(3)-(4)_isGouvernedBy_bekezdés: true, (3)-(4)_isGouvernedBy_bekezdés_ATT: true, B0IsInLexic: true, B0Lemma: bekezdés, B0POS: N, B0Token: bekezdése, B1Lemma: részletez, B1POS: V, B1Token: részletezi, S0B0Lemma: (3)-(4)_bekezdés, S0B0LemmaPOS: (3)-(4)_N, S0B0POS: O_N, S0B0POSLemma: O_bekezdés, S0B0Token: (3)-(4)_bekezdése, S0B1Lemma: (3)-(4)_részletez, S0B1LemmaPOS: (3)-(4)_V, S0B1POS: O_V, S0B1POSLemma: O_részletez, S0B1Token: (3)-(4)_részletezi, S0Lemma: (3)-(4), S0POS: O, S0Token: (3)-(4), TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

56- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [bekezdése, részletezi, . ,.. ]

B0IsInLexic: true, B0Lemma: bekezdés, B0POS: N, B0Token: bekezdése, B1Lemma: részletez, B1POS: V, B1Token: részletezi, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

57- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [bekezdése]   B= [részletezi, . ,.. ]

B0Lemma: részletez, B0POS: V, B0Token: részletezi, B1Lemma: ., B1POS: ., B1Token: ., S0B0Lemma: bekezdés_részletez, S0B0LemmaPOS: bekezdés_V, S0B0POS: N_V, S0B0POSLemma: N_részletez, S0B0Token: bekezdése_részletezi, S0B1Lemma: bekezdés_., S0B1LemmaPOS: bekezdés_., S0B1POS: N_., S0B1POSLemma: N_., S0B1Token: bekezdése_., S0IsInLexic: true, S0Lemma: bekezdés, S0POS: N, S0Token: bekezdése, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, bekezdés_isGouvernedBy_részletez: true, bekezdés_isGouvernedBy_részletez_SUBJ: true, 

58- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [részletezi, . ,.. ]

B0Lemma: részletez, B0POS: V, B0Token: részletezi, B1Lemma: ., B1POS: ., B1Token: ., TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

59- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [részletezi]   B= [.]

B0Lemma: ., B0POS: ., B0Token: ., S0B0Lemma: részletez_., S0B0LemmaPOS: részletez_., S0B0POS: V_., S0B0POSLemma: V_., S0B0Token: részletezi_., S0Lemma: részletez, S0POS: V, S0Token: részletezi, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

60- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [.]

B0Lemma: ., B0POS: ., B0Token: ., TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

61- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [ ]

S0Lemma: ., S0POS: ., S0Token: ., TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

62- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

