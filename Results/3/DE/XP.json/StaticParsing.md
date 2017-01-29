## Sentence No. 6253 - 
ein fataler entschluss : der mann stürzte ab dieter schormann geht davon aus , dass jetzt mit blick auf die letzten sommerwochen in der gastronomie im kreis mettmann noch einmal zusätzliche mini-jobber angeworben werden , um spitzen abzudecken . 
### Existing MWEs: 
1- **stürzte ab** (VPC)
2- **geht aus** (VPC)
3- **geht davon aus** (ID), Interleaving 



0- &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ein, fataler, entschluss ,.. ]

B0IsInLexic: true, B0Token: ein, B0_LastThreeLetters: ein, B0_LastTwoLetters: in, 

1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ein]   B= [fataler, entschluss, : ,.. ]

B0Token: fataler, B0_LastThreeLetters: ler, B0_LastTwoLetters: er, S0B0Token: ein_fataler, S0B1Token: ein_entschluss, S0B2Token: ein_:, S0IsInLexic: true, S0Token: ein, S0_LastThreeLetters: ein, S0_LastTwoLetters: in, ein_isGouvernedBy_Entschluss: true, ein_isGouvernedBy_Entschluss_det: true, 

2- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [fataler, entschluss, : ,.. ]

B0Token: fataler, B0_LastThreeLetters: ler, B0_LastTwoLetters: er, 

3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [fataler]   B= [entschluss, :, der ,.. ]

B0Token: entschluss, B0_LastThreeLetters: uss, B0_LastTwoLetters: ss, S0B0Token: fataler_entschluss, S0B1Token: fataler_:, S0B2Token: fataler_der, S0Token: fataler, S0_LastThreeLetters: ler, S0_LastTwoLetters: er, fatal_isGouvernedBy_Entschluss: true, fatal_isGouvernedBy_Entschluss_amod: true, 

4- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [entschluss, :, der ,.. ]

B0Token: entschluss, B0_LastThreeLetters: uss, B0_LastTwoLetters: ss, 

5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [entschluss]   B= [:, der, mann ,.. ]

B0Token: :, B0_LastThreeLetters: :, B0_LastTwoLetters: :, Entschluss_:_hasRighDep_punct: true, Entschluss_hasRighDep_punct: true, Entschluss_isGouvernedBy_stürzen: true, Entschluss_isGouvernedBy_stürzen_dep: true, S0B0Token: entschluss_:, S0B1Token: entschluss_der, S0B2Token: entschluss_mann, S0Token: entschluss, S0_LastThreeLetters: uss, S0_LastTwoLetters: ss, hasRighDep_punct: true, 

6- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [:, der, mann ,.. ]

B0Token: :, B0_LastThreeLetters: :, B0_LastTwoLetters: :, 

7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [:]   B= [der, mann, stürzte ,.. ]

B0IsInLexic: true, B0Token: der, B0_LastThreeLetters: der, B0_LastTwoLetters: er, S0B0Token: :_der, S0B1Token: :_mann, S0B2Token: :_stürzte, S0Token: :, S0_LastThreeLetters: :, S0_LastTwoLetters: :, 

8- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [der, mann, stürzte ,.. ]

B0IsInLexic: true, B0Token: der, B0_LastThreeLetters: der, B0_LastTwoLetters: er, 

9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [der]   B= [mann, stürzte, ab ,.. ]

B0Token: mann, B0_LastThreeLetters: ann, B0_LastTwoLetters: nn, S0B0Token: der_mann, S0B1Token: der_stürzte, S0B2Token: der_ab, S0IsInLexic: true, S0Token: der, S0_LastThreeLetters: der, S0_LastTwoLetters: er, der_isGouvernedBy_Mann: true, der_isGouvernedBy_Mann_det: true, 

10- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [mann, stürzte, ab ,.. ]

B0Token: mann, B0_LastThreeLetters: ann, B0_LastTwoLetters: nn, 

11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [mann]   B= [stürzte, ab, dieter ,.. ]

B0IsInLexic: true, B0Token: stürzte, B0_LastThreeLetters: zte, B0_LastTwoLetters: te, Mann_isGouvernedBy_stürzen: true, Mann_isGouvernedBy_stürzen_nsubj: true, S0B0Token: mann_stürzte, S0B1Token: mann_ab, S0B2Token: mann_dieter, S0Token: mann, S0_LastThreeLetters: ann, S0_LastTwoLetters: nn, 

12- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [stürzte, ab, dieter ,.. ]

B0IsInLexic: true, B0Token: stürzte, B0_LastThreeLetters: zte, B0_LastTwoLetters: te, 

13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [stürzte]   B= [ab, dieter, schormann ,.. ]

B0IsInLexic: true, B0Token: ab, B0_LastThreeLetters: ab, B0_LastTwoLetters: ab, S0B0Token: stürzte_ab, S0B1Token: stürzte_dieter, S0B2Token: stürzte_schormann, S0IsInLexic: true, S0Token: stürzte, S0_LastThreeLetters: zte, S0_LastTwoLetters: te, 

14- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [stürzte, ab]   B= [dieter, schormann, geht ,.. ]

B0Token: dieter, B0_LastThreeLetters: ter, B0_LastTwoLetters: er, S0B0Token: ab_dieter, S0B1Token: ab_schormann, S0B2Token: ab_geht, S0IsInLexic: true, S0S1Distance: 1, S0Token: ab, S0_LastThreeLetters: ab, S0_LastTwoLetters: ab, S1B0Token: stürzte_dieter, S1IsInLexic: true, S1S0B0Token: stürzte_ab_dieter, S1S0Token: stürzte_ab, S1Token: stürzte, S1_LastThreeLetters: zte, S1_LastTwoLetters: te, ab_isGouvernedBy_Schormann: true, ab_isGouvernedBy_Schormann_case: true, 

15- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[stürzte, ab]]   B= [dieter, schormann, geht ,.. ]

B0Token: dieter, B0_LastThreeLetters: ter, B0_LastTwoLetters: er, S0B0Token: stürzte_ab_dieter, S0B1Token: stürzte_ab_schormann, S0B2Token: stürzte_ab_geht, S0Token: stürzte_ab, 

16- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [dieter, schormann, geht ,.. ]

B0Token: dieter, B0_LastThreeLetters: ter, B0_LastTwoLetters: er, 

17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [dieter]   B= [schormann, geht, davon ,.. ]

B0Token: schormann, B0_LastThreeLetters: ann, B0_LastTwoLetters: nn, Dieter_isGouvernedBy_Schormann: true, Dieter_isGouvernedBy_Schormann_name: true, S0B0Token: dieter_schormann, S0B1Token: dieter_geht, S0B2Token: dieter_davon, S0Token: dieter, S0_LastThreeLetters: ter, S0_LastTwoLetters: er, 

18- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [schormann, geht, davon ,.. ]

B0Token: schormann, B0_LastThreeLetters: ann, B0_LastTwoLetters: nn, 

19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [schormann]   B= [geht, davon, aus ,.. ]

B0IsInLexic: true, B0Token: geht, B0_LastThreeLetters: eht, B0_LastTwoLetters: ht, S0B0Token: schormann_geht, S0B1Token: schormann_davon, S0B2Token: schormann_aus, S0Token: schormann, S0_LastThreeLetters: ann, S0_LastTwoLetters: nn, 

20- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [geht, davon, aus ,.. ]

B0IsInLexic: true, B0Token: geht, B0_LastThreeLetters: eht, B0_LastTwoLetters: ht, 

21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [geht]   B= [davon, aus, , ,.. ]

B0IsInLexic: true, B0Token: davon, B0_LastThreeLetters: von, B0_LastTwoLetters: on, S0B0Token: geht_davon, S0B1Token: geht_aus, S0B2Token: geht_,, S0IsInLexic: true, S0Token: geht, S0_LastThreeLetters: eht, S0_LastTwoLetters: ht, gehen_,_hasRighDep_punct: true, gehen_anwerben_hasRighDep_ccomp: true, gehen_aus_hasRighDep_compound:prt: true, gehen_davon_hasRighDep_dep: true, gehen_hasRighDep_ccomp: true, gehen_hasRighDep_compound:prt: true, gehen_hasRighDep_dep: true, gehen_hasRighDep_punct: true, hasRighDep_ccomp: true, hasRighDep_compound:prt: true, hasRighDep_dep: true, hasRighDep_punct: true, 

22- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [geht, davon]   B= [aus, ,, dass ,.. ]

B0IsInLexic: true, B0Token: aus, B0_LastThreeLetters: aus, B0_LastTwoLetters: us, S0B0Token: davon_aus, S0B1Token: davon_,, S0B2Token: davon_dass, S0IsInLexic: true, S0S1Distance: 1, S0Token: davon, S0_LastThreeLetters: von, S0_LastTwoLetters: on, S1B0Token: geht_aus, S1IsInLexic: true, S1S0B0Token: geht_davon_aus, S1S0Token: geht_davon, S1Token: geht, S1_LastThreeLetters: eht, S1_LastTwoLetters: ht, SyntaxicRelation: +dep, 

23- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [geht]   B= [aus, ,, dass ,.. ]

B0IsInLexic: true, B0Token: aus, B0_LastThreeLetters: aus, B0_LastTwoLetters: us, S0B0Token: geht_aus, S0B1Token: geht_,, S0B2Token: geht_dass, S0IsInLexic: true, S0Token: geht, S0_LastThreeLetters: eht, S0_LastTwoLetters: ht, gehen_,_hasRighDep_punct: true, gehen_anwerben_hasRighDep_ccomp: true, gehen_aus_hasRighDep_compound:prt: true, gehen_hasRighDep_ccomp: true, gehen_hasRighDep_compound:prt: true, gehen_hasRighDep_punct: true, hasRighDep_ccomp: true, hasRighDep_compound:prt: true, hasRighDep_punct: true, 

24- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [geht, aus]   B= [,, dass, jetzt ,.. ]

B0Token: ,, B0_LastThreeLetters: ,, B0_LastTwoLetters: ,, S0B0Token: aus_,, S0B1Token: aus_dass, S0B2Token: aus_jetzt, S0IsInLexic: true, S0S1Distance: 2, S0Token: aus, S0_LastThreeLetters: aus, S0_LastTwoLetters: us, S1B0Token: geht_,, S1IsInLexic: true, S1S0B0Token: geht_aus_,, S1S0Token: geht_aus, S1Token: geht, S1_LastThreeLetters: eht, S1_LastTwoLetters: ht, SyntaxicRelation: +compound:prt, 

25- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[geht, aus]]   B= [,, dass, jetzt ,.. ]

B0Token: ,, B0_LastThreeLetters: ,, B0_LastTwoLetters: ,, S0B0Token: geht_aus_,, S0B1Token: geht_aus_dass, S0B2Token: geht_aus_jetzt, S0Token: geht_aus, 

26- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, dass, jetzt ,.. ]

B0Token: ,, B0_LastThreeLetters: ,, B0_LastTwoLetters: ,, 

27- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [dass, jetzt, mit ,.. ]

B0Token: dass, B0_LastThreeLetters: ass, B0_LastTwoLetters: ss, S0B0Token: ,_dass, S0B1Token: ,_jetzt, S0B2Token: ,_mit, S0Token: ,, S0_LastThreeLetters: ,, S0_LastTwoLetters: ,, 

28- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [dass, jetzt, mit ,.. ]

B0Token: dass, B0_LastThreeLetters: ass, B0_LastTwoLetters: ss, 

29- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [dass]   B= [jetzt, mit, blick ,.. ]

B0Token: jetzt, B0_LastThreeLetters: tzt, B0_LastTwoLetters: zt, S0B0Token: dass_jetzt, S0B1Token: dass_mit, S0B2Token: dass_blick, S0Token: dass, S0_LastThreeLetters: ass, S0_LastTwoLetters: ss, dass_isGouvernedBy_anwerben: true, dass_isGouvernedBy_anwerben_mark: true, 

30- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [jetzt, mit, blick ,.. ]

B0Token: jetzt, B0_LastThreeLetters: tzt, B0_LastTwoLetters: zt, 

31- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [jetzt]   B= [mit, blick, auf ,.. ]

B0IsInLexic: true, B0Token: mit, B0_LastThreeLetters: mit, B0_LastTwoLetters: it, S0B0Token: jetzt_mit, S0B1Token: jetzt_blick, S0B2Token: jetzt_auf, S0Token: jetzt, S0_LastThreeLetters: tzt, S0_LastTwoLetters: zt, jetzt_isGouvernedBy_anwerben: true, jetzt_isGouvernedBy_anwerben_advmod: true, 

32- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [mit, blick, auf ,.. ]

B0IsInLexic: true, B0Token: mit, B0_LastThreeLetters: mit, B0_LastTwoLetters: it, 

33- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [mit]   B= [blick, auf, die ,.. ]

B0Token: blick, B0_LastThreeLetters: ick, B0_LastTwoLetters: ck, S0B0Token: mit_blick, S0B1Token: mit_auf, S0B2Token: mit_die, S0IsInLexic: true, S0Token: mit, S0_LastThreeLetters: mit, S0_LastTwoLetters: it, mit_isGouvernedBy_Blick: true, mit_isGouvernedBy_Blick_case: true, 

34- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [blick, auf, die ,.. ]

B0Token: blick, B0_LastThreeLetters: ick, B0_LastTwoLetters: ck, 

35- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [blick]   B= [auf, die, letzten ,.. ]

B0IsInLexic: true, B0Token: auf, B0_LastThreeLetters: auf, B0_LastTwoLetters: uf, Blick_Sommerwochen_hasRighDep_nmod: true, Blick_hasRighDep_nmod: true, Blick_isGouvernedBy_anwerben: true, Blick_isGouvernedBy_anwerben_nmod: true, S0B0Token: blick_auf, S0B1Token: blick_die, S0B2Token: blick_letzten, S0Token: blick, S0_LastThreeLetters: ick, S0_LastTwoLetters: ck, hasRighDep_nmod: true, 

36- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [auf, die, letzten ,.. ]

B0IsInLexic: true, B0Token: auf, B0_LastThreeLetters: auf, B0_LastTwoLetters: uf, 

37- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [auf]   B= [die, letzten, sommerwochen ,.. ]

B0IsInLexic: true, B0Token: die, B0_LastThreeLetters: die, B0_LastTwoLetters: ie, S0B0Token: auf_die, S0B1Token: auf_letzten, S0B2Token: auf_sommerwochen, S0IsInLexic: true, S0Token: auf, S0_LastThreeLetters: auf, S0_LastTwoLetters: uf, auf_isGouvernedBy_Sommerwochen: true, auf_isGouvernedBy_Sommerwochen_case: true, 

38- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [die, letzten, sommerwochen ,.. ]

B0IsInLexic: true, B0Token: die, B0_LastThreeLetters: die, B0_LastTwoLetters: ie, 

39- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [die]   B= [letzten, sommerwochen, in ,.. ]

B0Token: letzten, B0_LastThreeLetters: ten, B0_LastTwoLetters: en, S0B0Token: die_letzten, S0B1Token: die_sommerwochen, S0B2Token: die_in, S0IsInLexic: true, S0Token: die, S0_LastThreeLetters: die, S0_LastTwoLetters: ie, der_isGouvernedBy_Sommerwochen: true, der_isGouvernedBy_Sommerwochen_det: true, 

40- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [letzten, sommerwochen, in ,.. ]

B0Token: letzten, B0_LastThreeLetters: ten, B0_LastTwoLetters: en, 

41- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [letzten]   B= [sommerwochen, in, der ,.. ]

B0Token: sommerwochen, B0_LastThreeLetters: hen, B0_LastTwoLetters: en, S0B0Token: letzten_sommerwochen, S0B1Token: letzten_in, S0B2Token: letzten_der, S0Token: letzten, S0_LastThreeLetters: ten, S0_LastTwoLetters: en, letzt_isGouvernedBy_Sommerwochen: true, letzt_isGouvernedBy_Sommerwochen_amod: true, 

42- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [sommerwochen, in, der ,.. ]

B0Token: sommerwochen, B0_LastThreeLetters: hen, B0_LastTwoLetters: en, 

43- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [sommerwochen]   B= [in, der, gastronomie ,.. ]

B0IsInLexic: true, B0Token: in, B0_LastThreeLetters: in, B0_LastTwoLetters: in, S0B0Token: sommerwochen_in, S0B1Token: sommerwochen_der, S0B2Token: sommerwochen_gastronomie, S0Token: sommerwochen, S0_LastThreeLetters: hen, S0_LastTwoLetters: en, 

44- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [in, der, gastronomie ,.. ]

B0IsInLexic: true, B0Token: in, B0_LastThreeLetters: in, B0_LastTwoLetters: in, 

45- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [in]   B= [der, gastronomie, im ,.. ]

B0IsInLexic: true, B0Token: der, B0_LastThreeLetters: der, B0_LastTwoLetters: er, S0B0Token: in_der, S0B1Token: in_gastronomie, S0B2Token: in_im, S0IsInLexic: true, S0Token: in, S0_LastThreeLetters: in, S0_LastTwoLetters: in, in_isGouvernedBy_Gastronomie: true, in_isGouvernedBy_Gastronomie_case: true, 

46- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [der, gastronomie, im ,.. ]

B0IsInLexic: true, B0Token: der, B0_LastThreeLetters: der, B0_LastTwoLetters: er, 

47- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [der]   B= [gastronomie, im, kreis ,.. ]

B0Token: gastronomie, B0_LastThreeLetters: mie, B0_LastTwoLetters: ie, S0B0Token: der_gastronomie, S0B1Token: der_im, S0B2Token: der_kreis, S0IsInLexic: true, S0Token: der, S0_LastThreeLetters: der, S0_LastTwoLetters: er, der_isGouvernedBy_Gastronomie: true, der_isGouvernedBy_Gastronomie_det: true, 

48- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [gastronomie, im, kreis ,.. ]

B0Token: gastronomie, B0_LastThreeLetters: mie, B0_LastTwoLetters: ie, 

49- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [gastronomie]   B= [im, kreis, mettmann ,.. ]

B0IsInLexic: true, B0Token: im, B0_LastThreeLetters: im, B0_LastTwoLetters: im, Gastronomie_isGouvernedBy_anwerben: true, Gastronomie_isGouvernedBy_anwerben_nmod: true, S0B0Token: gastronomie_im, S0B1Token: gastronomie_kreis, S0B2Token: gastronomie_mettmann, S0Token: gastronomie, S0_LastThreeLetters: mie, S0_LastTwoLetters: ie, 

50- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [im, kreis, mettmann ,.. ]

B0IsInLexic: true, B0Token: im, B0_LastThreeLetters: im, B0_LastTwoLetters: im, 

51- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [im]   B= [kreis, mettmann, noch ,.. ]

B0Token: kreis, B0_LastThreeLetters: eis, B0_LastTwoLetters: is, S0B0Token: im_kreis, S0B1Token: im_mettmann, S0B2Token: im_noch, S0IsInLexic: true, S0Token: im, S0_LastThreeLetters: im, S0_LastTwoLetters: im, in+der_isGouvernedBy_Kreis: true, in+der_isGouvernedBy_Kreis_case: true, 

52- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [kreis, mettmann, noch ,.. ]

B0Token: kreis, B0_LastThreeLetters: eis, B0_LastTwoLetters: is, 

53- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [kreis]   B= [mettmann, noch, einmal ,.. ]

B0Token: mettmann, B0_LastThreeLetters: ann, B0_LastTwoLetters: nn, Kreis_Mettmann_hasRighDep_appos: true, Kreis_hasRighDep_appos: true, Kreis_isGouvernedBy_anwerben: true, Kreis_isGouvernedBy_anwerben_nmod: true, S0B0Token: kreis_mettmann, S0B1Token: kreis_noch, S0B2Token: kreis_einmal, S0Token: kreis, S0_LastThreeLetters: eis, S0_LastTwoLetters: is, hasRighDep_appos: true, 

54- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [mettmann, noch, einmal ,.. ]

B0Token: mettmann, B0_LastThreeLetters: ann, B0_LastTwoLetters: nn, 

55- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [mettmann]   B= [noch, einmal, zusätzliche ,.. ]

B0IsInLexic: true, B0Token: noch, B0_LastThreeLetters: och, B0_LastTwoLetters: ch, S0B0Token: mettmann_noch, S0B1Token: mettmann_einmal, S0B2Token: mettmann_zusätzliche, S0Token: mettmann, S0_LastThreeLetters: ann, S0_LastTwoLetters: nn, 

56- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [noch, einmal, zusätzliche ,.. ]

B0IsInLexic: true, B0Token: noch, B0_LastThreeLetters: och, B0_LastTwoLetters: ch, 

57- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [noch]   B= [einmal, zusätzliche, mini-jobber ,.. ]

B0Token: einmal, B0_LastThreeLetters: mal, B0_LastTwoLetters: al, S0B0Token: noch_einmal, S0B1Token: noch_zusätzliche, S0B2Token: noch_mini-jobber, S0IsInLexic: true, S0Token: noch, S0_LastThreeLetters: och, S0_LastTwoLetters: ch, noch_isGouvernedBy_anwerben: true, noch_isGouvernedBy_anwerben_advmod: true, 

58- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [einmal, zusätzliche, mini-jobber ,.. ]

B0Token: einmal, B0_LastThreeLetters: mal, B0_LastTwoLetters: al, 

59- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [einmal]   B= [zusätzliche, mini-jobber, angeworben ,.. ]

B0Token: zusätzliche, B0_LastThreeLetters: che, B0_LastTwoLetters: he, S0B0Token: einmal_zusätzliche, S0B1Token: einmal_mini-jobber, S0B2Token: einmal_angeworben, S0Token: einmal, S0_LastThreeLetters: mal, S0_LastTwoLetters: al, einmal_isGouvernedBy_anwerben: true, einmal_isGouvernedBy_anwerben_advmod: true, 

60- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [zusätzliche, mini-jobber, angeworben ,.. ]

B0Token: zusätzliche, B0_LastThreeLetters: che, B0_LastTwoLetters: he, 

61- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [zusätzliche]   B= [mini-jobber, angeworben, werden ,.. ]

B0Token: mini-jobber, B0_LastThreeLetters: ber, B0_LastTwoLetters: er, S0B0Token: zusätzliche_mini-jobber, S0B1Token: zusätzliche_angeworben, S0B2Token: zusätzliche_werden, S0Token: zusätzliche, S0_LastThreeLetters: che, S0_LastTwoLetters: he, zusätzlich_isGouvernedBy_Mini-Jobber: true, zusätzlich_isGouvernedBy_Mini-Jobber_amod: true, 

62- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [mini-jobber, angeworben, werden ,.. ]

B0Token: mini-jobber, B0_LastThreeLetters: ber, B0_LastTwoLetters: er, 

63- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [mini-jobber]   B= [angeworben, werden, , ,.. ]

B0Token: angeworben, B0_LastThreeLetters: ben, B0_LastTwoLetters: en, Mini-Jobber_isGouvernedBy_anwerben: true, Mini-Jobber_isGouvernedBy_anwerben_nsubjpass: true, S0B0Token: mini-jobber_angeworben, S0B1Token: mini-jobber_werden, S0B2Token: mini-jobber_,, S0Token: mini-jobber, S0_LastThreeLetters: ber, S0_LastTwoLetters: er, 

64- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [angeworben, werden, , ,.. ]

B0Token: angeworben, B0_LastThreeLetters: ben, B0_LastTwoLetters: en, 

65- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [angeworben]   B= [werden, ,, um ,.. ]

B0IsInLexic: true, B0Token: werden, B0_LastThreeLetters: den, B0_LastTwoLetters: en, S0B0Token: angeworben_werden, S0B1Token: angeworben_,, S0B2Token: angeworben_um, S0Token: angeworben, S0_LastThreeLetters: ben, S0_LastTwoLetters: en, anwerben_,_hasRighDep_punct: true, anwerben_hasRighDep_auxpass: true, anwerben_hasRighDep_punct: true, anwerben_werden_hasRighDep_auxpass: true, hasRighDep_auxpass: true, hasRighDep_punct: true, 

66- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [werden, ,, um ,.. ]

B0IsInLexic: true, B0Token: werden, B0_LastThreeLetters: den, B0_LastTwoLetters: en, 

67- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [werden]   B= [,, um, spitzen ,.. ]

B0Token: ,, B0_LastThreeLetters: ,, B0_LastTwoLetters: ,, S0B0Token: werden_,, S0B1Token: werden_um, S0B2Token: werden_spitzen, S0IsInLexic: true, S0Token: werden, S0_LastThreeLetters: den, S0_LastTwoLetters: en, 

68- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, um, spitzen ,.. ]

B0Token: ,, B0_LastThreeLetters: ,, B0_LastTwoLetters: ,, 

69- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [um, spitzen, abzudecken ,.. ]

B0IsInLexic: true, B0Token: um, B0_LastThreeLetters: um, B0_LastTwoLetters: um, S0B0Token: ,_um, S0B1Token: ,_spitzen, S0B2Token: ,_abzudecken, S0Token: ,, S0_LastThreeLetters: ,, S0_LastTwoLetters: ,, 

70- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [um, spitzen, abzudecken ,.. ]

B0IsInLexic: true, B0Token: um, B0_LastThreeLetters: um, B0_LastTwoLetters: um, 

71- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [um]   B= [spitzen, abzudecken, . ,.. ]

B0Token: spitzen, B0_LastThreeLetters: zen, B0_LastTwoLetters: en, S0B0Token: um_spitzen, S0B1Token: um_abzudecken, S0B2Token: um_., S0IsInLexic: true, S0Token: um, S0_LastThreeLetters: um, S0_LastTwoLetters: um, um_isGouvernedBy_Spitze: true, um_isGouvernedBy_Spitze_case: true, 

72- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [spitzen, abzudecken, . ,.. ]

B0Token: spitzen, B0_LastThreeLetters: zen, B0_LastTwoLetters: en, 

73- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [spitzen]   B= [abzudecken, . ,.. ]

B0Token: abzudecken, B0_LastThreeLetters: ken, B0_LastTwoLetters: en, S0B0Token: spitzen_abzudecken, S0B1Token: spitzen_., S0Token: spitzen, S0_LastThreeLetters: zen, S0_LastTwoLetters: en, 

74- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [abzudecken, . ,.. ]

B0Token: abzudecken, B0_LastThreeLetters: ken, B0_LastTwoLetters: en, 

75- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [abzudecken]   B= [.]

B0Token: ., B0_LastThreeLetters: ., B0_LastTwoLetters: ., S0B0Token: abzudecken_., S0Token: abzudecken, S0_LastThreeLetters: ken, S0_LastTwoLetters: en, 

76- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [.]

B0Token: ., B0_LastThreeLetters: ., B0_LastTwoLetters: ., 

77- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [ ]

S0Token: ., S0_LastThreeLetters: ., S0_LastTwoLetters: ., 

78- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

## Sentence No. 18 - 
zwietracht bei der öffentlich-privaten partnerschaft da haben wir gegenüber dem ballungsraum keine chance und fallen immer durch den rost . 
### Existing MWEs: 
1- **haben chance** (ID)
2- **fallen durch rost** (ID)



0- &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [zwietracht, bei, der ,.. ]

B0Token: zwietracht, B0_LastThreeLetters: cht, B0_LastTwoLetters: ht, 

1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [zwietracht]   B= [bei, der, öffentlich-privaten ,.. ]

B0IsInLexic: true, B0Token: bei, B0_LastThreeLetters: bei, B0_LastTwoLetters: ei, S0B0Token: zwietracht_bei, S0B1Token: zwietracht_der, S0B2Token: zwietracht_öffentlich-privaten, S0Token: zwietracht, S0_LastThreeLetters: cht, S0_LastTwoLetters: ht, Zwietracht_hasRighDep_nmod: true, Zwietracht_isGouvernedBy_fallen: true, Zwietracht_isGouvernedBy_fallen_nmod: true, Zwietracht_öffentlich-privaten_hasRighDep_nmod: true, hasRighDep_nmod: true, 

2- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [bei, der, öffentlich-privaten ,.. ]

B0IsInLexic: true, B0Token: bei, B0_LastThreeLetters: bei, B0_LastTwoLetters: ei, 

3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [bei]   B= [der, öffentlich-privaten, partnerschaft ,.. ]

B0IsInLexic: true, B0Token: der, B0_LastThreeLetters: der, B0_LastTwoLetters: er, S0B0Token: bei_der, S0B1Token: bei_öffentlich-privaten, S0B2Token: bei_partnerschaft, S0IsInLexic: true, S0Token: bei, S0_LastThreeLetters: bei, S0_LastTwoLetters: ei, bei_isGouvernedBy_öffentlich-privaten: true, bei_isGouvernedBy_öffentlich-privaten_case: true, 

4- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [der, öffentlich-privaten, partnerschaft ,.. ]

B0IsInLexic: true, B0Token: der, B0_LastThreeLetters: der, B0_LastTwoLetters: er, 

5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [der]   B= [öffentlich-privaten, partnerschaft, da ,.. ]

B0Token: öffentlich-privaten, B0_LastThreeLetters: ten, B0_LastTwoLetters: en, S0B0Token: der_öffentlich-privaten, S0B1Token: der_partnerschaft, S0B2Token: der_da, S0IsInLexic: true, S0Token: der, S0_LastThreeLetters: der, S0_LastTwoLetters: er, der_isGouvernedBy_öffentlich-privaten: true, der_isGouvernedBy_öffentlich-privaten_det: true, 

6- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [öffentlich-privaten, partnerschaft, da ,.. ]

B0Token: öffentlich-privaten, B0_LastThreeLetters: ten, B0_LastTwoLetters: en, 

7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [öffentlich-privaten]   B= [partnerschaft, da, haben ,.. ]

B0Token: partnerschaft, B0_LastThreeLetters: aft, B0_LastTwoLetters: ft, S0B0Token: öffentlich-privaten_partnerschaft, S0B1Token: öffentlich-privaten_da, S0B2Token: öffentlich-privaten_haben, S0Token: öffentlich-privaten, S0_LastThreeLetters: ten, S0_LastTwoLetters: en, hasRighDep_appos: true, öffentlich-privaten_Da_hasRighDep_appos: true, öffentlich-privaten_hasRighDep_appos: true, 

8- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [partnerschaft, da, haben ,.. ]

B0Token: partnerschaft, B0_LastThreeLetters: aft, B0_LastTwoLetters: ft, 

9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [partnerschaft]   B= [da, haben, wir ,.. ]

B0Token: da, B0_LastThreeLetters: da, B0_LastTwoLetters: da, Partnerschaft_isGouvernedBy_Da: true, Partnerschaft_isGouvernedBy_Da_name: true, S0B0Token: partnerschaft_da, S0B1Token: partnerschaft_haben, S0B2Token: partnerschaft_wir, S0Token: partnerschaft, S0_LastThreeLetters: aft, S0_LastTwoLetters: ft, 

10- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [da, haben, wir ,.. ]

B0Token: da, B0_LastThreeLetters: da, B0_LastTwoLetters: da, 

11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [da]   B= [haben, wir, gegenüber ,.. ]

B0IsInLexic: true, B0Token: haben, B0_LastThreeLetters: ben, B0_LastTwoLetters: en, S0B0Token: da_haben, S0B1Token: da_wir, S0B2Token: da_gegenüber, S0Token: da, S0_LastThreeLetters: da, S0_LastTwoLetters: da, 

12- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [haben, wir, gegenüber ,.. ]

B0IsInLexic: true, B0Token: haben, B0_LastThreeLetters: ben, B0_LastTwoLetters: en, 

13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [haben]   B= [wir, gegenüber, dem ,.. ]

B0IsInLexic: true, B0Token: wir, B0_LastThreeLetters: wir, B0_LastTwoLetters: ir, S0B0Token: haben_wir, S0B1Token: haben_gegenüber, S0B2Token: haben_dem, S0IsInLexic: true, S0Token: haben, S0_LastThreeLetters: ben, S0_LastTwoLetters: en, haben_isGouvernedBy_fallen: true, haben_isGouvernedBy_fallen_aux: true, 

14- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [haben, wir]   B= [gegenüber, dem, ballungsraum ,.. ]

B0Token: gegenüber, B0_LastThreeLetters: ber, B0_LastTwoLetters: er, S0B0Token: wir_gegenüber, S0B1Token: wir_dem, S0B2Token: wir_ballungsraum, S0IsInLexic: true, S0S1Distance: 1, S0Token: wir, S0_LastThreeLetters: wir, S0_LastTwoLetters: ir, S1B0Token: haben_gegenüber, S1IsInLexic: true, S1S0B0Token: haben_wir_gegenüber, S1S0Token: haben_wir, S1Token: haben, S1_LastThreeLetters: ben, S1_LastTwoLetters: en, wir_isGouvernedBy_fallen: true, wir_isGouvernedBy_fallen_nsubj: true, 

15- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [haben]   B= [gegenüber, dem, ballungsraum ,.. ]

B0Token: gegenüber, B0_LastThreeLetters: ber, B0_LastTwoLetters: er, S0B0Token: haben_gegenüber, S0B1Token: haben_dem, S0B2Token: haben_ballungsraum, S0IsInLexic: true, S0Token: haben, S0_LastThreeLetters: ben, S0_LastTwoLetters: en, haben_isGouvernedBy_fallen: true, haben_isGouvernedBy_fallen_aux: true, 

16- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [haben, gegenüber]   B= [dem, ballungsraum, keine ,.. ]

B0IsInLexic: true, B0Token: dem, B0_LastThreeLetters: dem, B0_LastTwoLetters: em, S0B0Token: gegenüber_dem, S0B1Token: gegenüber_ballungsraum, S0B2Token: gegenüber_keine, S0S1Distance: 2, S0Token: gegenüber, S0_LastThreeLetters: ber, S0_LastTwoLetters: er, S1B0Token: haben_dem, S1IsInLexic: true, S1S0B0Token: haben_gegenüber_dem, S1S0Token: haben_gegenüber, S1Token: haben, S1_LastThreeLetters: ben, S1_LastTwoLetters: en, gegenüber_isGouvernedBy_Ballungsraum: true, gegenüber_isGouvernedBy_Ballungsraum_case: true, 

17- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [haben]   B= [dem, ballungsraum, keine ,.. ]

B0IsInLexic: true, B0Token: dem, B0_LastThreeLetters: dem, B0_LastTwoLetters: em, S0B0Token: haben_dem, S0B1Token: haben_ballungsraum, S0B2Token: haben_keine, S0IsInLexic: true, S0Token: haben, S0_LastThreeLetters: ben, S0_LastTwoLetters: en, haben_isGouvernedBy_fallen: true, haben_isGouvernedBy_fallen_aux: true, 

18- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [haben, dem]   B= [ballungsraum, keine, chance ,.. ]

B0Token: ballungsraum, B0_LastThreeLetters: aum, B0_LastTwoLetters: um, S0B0Token: dem_ballungsraum, S0B1Token: dem_keine, S0B2Token: dem_chance, S0IsInLexic: true, S0S1Distance: 3, S0Token: dem, S0_LastThreeLetters: dem, S0_LastTwoLetters: em, S1B0Token: haben_ballungsraum, S1IsInLexic: true, S1S0B0Token: haben_dem_ballungsraum, S1S0Token: haben_dem, S1Token: haben, S1_LastThreeLetters: ben, S1_LastTwoLetters: en, der_isGouvernedBy_Ballungsraum: true, der_isGouvernedBy_Ballungsraum_det: true, 

19- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [haben]   B= [ballungsraum, keine, chance ,.. ]

B0Token: ballungsraum, B0_LastThreeLetters: aum, B0_LastTwoLetters: um, S0B0Token: haben_ballungsraum, S0B1Token: haben_keine, S0B2Token: haben_chance, S0IsInLexic: true, S0Token: haben, S0_LastThreeLetters: ben, S0_LastTwoLetters: en, haben_isGouvernedBy_fallen: true, haben_isGouvernedBy_fallen_aux: true, 

20- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [haben, ballungsraum]   B= [keine, chance, und ,.. ]

B0IsInLexic: true, B0Token: keine, B0_LastThreeLetters: ine, B0_LastTwoLetters: ne, Ballungsraum_isGouvernedBy_fallen: true, Ballungsraum_isGouvernedBy_fallen_nmod: true, S0B0Token: ballungsraum_keine, S0B1Token: ballungsraum_chance, S0B2Token: ballungsraum_und, S0S1Distance: 4, S0Token: ballungsraum, S0_LastThreeLetters: aum, S0_LastTwoLetters: um, S1B0Token: haben_keine, S1IsInLexic: true, S1S0B0Token: haben_ballungsraum_keine, S1S0Token: haben_ballungsraum, S1Token: haben, S1_LastThreeLetters: ben, S1_LastTwoLetters: en, 

21- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [haben]   B= [keine, chance, und ,.. ]

B0IsInLexic: true, B0Token: keine, B0_LastThreeLetters: ine, B0_LastTwoLetters: ne, S0B0Token: haben_keine, S0B1Token: haben_chance, S0B2Token: haben_und, S0IsInLexic: true, S0Token: haben, S0_LastThreeLetters: ben, S0_LastTwoLetters: en, haben_isGouvernedBy_fallen: true, haben_isGouvernedBy_fallen_aux: true, 

22- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [haben, keine]   B= [chance, und, fallen ,.. ]

B0IsInLexic: true, B0Token: chance, B0_LastThreeLetters: nce, B0_LastTwoLetters: ce, S0B0Token: keine_chance, S0B1Token: keine_und, S0B2Token: keine_fallen, S0IsInLexic: true, S0S1Distance: 5, S0Token: keine, S0_LastThreeLetters: ine, S0_LastTwoLetters: ne, S1B0Token: haben_chance, S1IsInLexic: true, S1S0B0Token: haben_keine_chance, S1S0Token: haben_keine, S1Token: haben, S1_LastThreeLetters: ben, S1_LastTwoLetters: en, kein_isGouvernedBy_Chance: true, kein_isGouvernedBy_Chance_neg: true, 

23- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [haben]   B= [chance, und, fallen ,.. ]

B0IsInLexic: true, B0Token: chance, B0_LastThreeLetters: nce, B0_LastTwoLetters: ce, S0B0Token: haben_chance, S0B1Token: haben_und, S0B2Token: haben_fallen, S0IsInLexic: true, S0Token: haben, S0_LastThreeLetters: ben, S0_LastTwoLetters: en, haben_isGouvernedBy_fallen: true, haben_isGouvernedBy_fallen_aux: true, 

24- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [haben, chance]   B= [und, fallen, immer ,.. ]

B0IsInLexic: true, B0Token: und, B0_LastThreeLetters: und, B0_LastTwoLetters: nd, Chance_hasRighDep_cc: true, Chance_isGouvernedBy_fallen: true, Chance_isGouvernedBy_fallen_dobj: true, Chance_und_hasRighDep_cc: true, S0B0Token: chance_und, S0B1Token: chance_fallen, S0B2Token: chance_immer, S0IsInLexic: true, S0S1Distance: 6, S0Token: chance, S0_LastThreeLetters: nce, S0_LastTwoLetters: ce, S1B0Token: haben_und, S1IsInLexic: true, S1S0B0Token: haben_chance_und, S1S0Token: haben_chance, S1Token: haben, S1_LastThreeLetters: ben, S1_LastTwoLetters: en, hasRighDep_cc: true, 

25- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[haben, chance]]   B= [und, fallen, immer ,.. ]

B0IsInLexic: true, B0Token: und, B0_LastThreeLetters: und, B0_LastTwoLetters: nd, S0B0Token: haben_chance_und, S0B1Token: haben_chance_fallen, S0B2Token: haben_chance_immer, S0Token: haben_chance, 

26- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [und, fallen, immer ,.. ]

B0IsInLexic: true, B0Token: und, B0_LastThreeLetters: und, B0_LastTwoLetters: nd, 

27- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [und]   B= [fallen, immer, durch ,.. ]

B0IsInLexic: true, B0Token: fallen, B0_LastThreeLetters: len, B0_LastTwoLetters: en, S0B0Token: und_fallen, S0B1Token: und_immer, S0B2Token: und_durch, S0IsInLexic: true, S0Token: und, S0_LastThreeLetters: und, S0_LastTwoLetters: nd, 

28- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [fallen, immer, durch ,.. ]

B0IsInLexic: true, B0Token: fallen, B0_LastThreeLetters: len, B0_LastTwoLetters: en, 

29- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [fallen]   B= [immer, durch, den ,.. ]

B0Token: immer, B0_LastThreeLetters: mer, B0_LastTwoLetters: er, S0B0Token: fallen_immer, S0B1Token: fallen_durch, S0B2Token: fallen_den, S0IsInLexic: true, S0Token: fallen, S0_LastThreeLetters: len, S0_LastTwoLetters: en, 

30- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [fallen, immer]   B= [durch, den, rost ,.. ]

B0IsInLexic: true, B0Token: durch, B0_LastThreeLetters: rch, B0_LastTwoLetters: ch, S0B0Token: immer_durch, S0B1Token: immer_den, S0B2Token: immer_rost, S0S1Distance: 1, S0Token: immer, S0_LastThreeLetters: mer, S0_LastTwoLetters: er, S1B0Token: fallen_durch, S1IsInLexic: true, S1S0B0Token: fallen_immer_durch, S1S0Token: fallen_immer, S1Token: fallen, S1_LastThreeLetters: len, S1_LastTwoLetters: en, SyntaxicRelation: +advmod, 

31- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [fallen]   B= [durch, den, rost ,.. ]

B0IsInLexic: true, B0Token: durch, B0_LastThreeLetters: rch, B0_LastTwoLetters: ch, S0B0Token: fallen_durch, S0B1Token: fallen_den, S0B2Token: fallen_rost, S0IsInLexic: true, S0Token: fallen, S0_LastThreeLetters: len, S0_LastTwoLetters: en, 

32- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [fallen, durch]   B= [den, rost, . ,.. ]

B0IsInLexic: true, B0Token: den, B0_LastThreeLetters: den, B0_LastTwoLetters: en, S0B0Token: durch_den, S0B1Token: durch_rost, S0B2Token: durch_., S0IsInLexic: true, S0S1Distance: 2, S0Token: durch, S0_LastThreeLetters: rch, S0_LastTwoLetters: ch, S1B0Token: fallen_den, S1IsInLexic: true, S1S0B0Token: fallen_durch_den, S1S0Token: fallen_durch, S1Token: fallen, S1_LastThreeLetters: len, S1_LastTwoLetters: en, durch_isGouvernedBy_Rost: true, durch_isGouvernedBy_Rost_case: true, 

33- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [fallen, durch, den]   B= [rost, . ,.. ]

B0IsInLexic: true, B0Token: rost, B0_LastThreeLetters: ost, B0_LastTwoLetters: st, S0B0Token: den_rost, S0B1Token: den_., S0IsInLexic: true, S0S1Distance: 1, S0Token: den, S0_LastThreeLetters: den, S0_LastTwoLetters: en, S1B0Token: durch_rost, S1IsInLexic: true, S1S0B0Token: durch_den_rost, S1S0Token: durch_den, S1Token: durch, S1_LastThreeLetters: rch, S1_LastTwoLetters: ch, der_isGouvernedBy_Rost: true, der_isGouvernedBy_Rost_det: true, 

34- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [fallen, durch]   B= [rost, . ,.. ]

B0IsInLexic: true, B0Token: rost, B0_LastThreeLetters: ost, B0_LastTwoLetters: st, S0B0Token: durch_rost, S0B1Token: durch_., S0IsInLexic: true, S0S1Distance: 2, S0Token: durch, S0_LastThreeLetters: rch, S0_LastTwoLetters: ch, S1B0Token: fallen_rost, S1IsInLexic: true, S1S0B0Token: fallen_durch_rost, S1S0Token: fallen_durch, S1Token: fallen, S1_LastThreeLetters: len, S1_LastTwoLetters: en, durch_isGouvernedBy_Rost: true, durch_isGouvernedBy_Rost_case: true, 

35- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [fallen, durch, rost]   B= [.]

B0Token: ., B0_LastThreeLetters: ., B0_LastTwoLetters: ., S0B0Token: rost_., S0IsInLexic: true, S0S1Distance: 2, S0Token: rost, S0_LastThreeLetters: ost, S0_LastTwoLetters: st, S1B0Token: durch_., S1IsInLexic: true, S1S0B0Token: durch_rost_., S1S0Token: durch_rost, S1Token: durch, S1_LastThreeLetters: rch, S1_LastTwoLetters: ch, SyntaxicRelation: -case, 

36- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [fallen, [durch, rost]]   B= [.]

B0Token: ., B0_LastThreeLetters: ., B0_LastTwoLetters: ., S0B0Token: durch_rost_., S0Token: durch_rost, S1B0Token: fallen_., S1IsInLexic: true, S1S0B0Token: fallen_durch_rost_., S1S0Token: fallen_durch_rost, S1Token: fallen, S1_LastThreeLetters: len, S1_LastTwoLetters: en, 

37- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[fallen, [durch, rost]]]   B= [.]

B0Token: ., B0_LastThreeLetters: ., B0_LastTwoLetters: ., S0B0Token: fallen_durch_rost_., S0Token: fallen_durch_rost, 

38- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [.]

B0Token: ., B0_LastThreeLetters: ., B0_LastTwoLetters: ., 

39- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [ ]

S0Token: ., S0_LastThreeLetters: ., S0_LastTwoLetters: ., 

40- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

## Sentence No. 46 - 
das ist aber noch nichts gegen die schmerzhafte analfissur , die sie sich bei der verhassten - und wieder mal viel zu schnell angelegten - intimrasur zugezogen hat . 
### Existing MWEs: 
1- **angelegten** (VPC)
2- **zugezogen** (VPC)



0- &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [das, ist, aber ,.. ]

B0IsInLexic: true, B0Token: das, B0_LastThreeLetters: das, B0_LastTwoLetters: as, 

1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [das]   B= [ist, aber, noch ,.. ]

B0IsInLexic: true, B0Token: ist, B0_LastThreeLetters: ist, B0_LastTwoLetters: st, S0B0Token: das_ist, S0B1Token: das_aber, S0B2Token: das_noch, S0IsInLexic: true, S0Token: das, S0_LastThreeLetters: das, S0_LastTwoLetters: as, der_isGouvernedBy_nichts: true, der_isGouvernedBy_nichts_nsubj: true, 

2- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ist, aber, noch ,.. ]

B0IsInLexic: true, B0Token: ist, B0_LastThreeLetters: ist, B0_LastTwoLetters: st, 

3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ist]   B= [aber, noch, nichts ,.. ]

B0Token: aber, B0_LastThreeLetters: ber, B0_LastTwoLetters: er, S0B0Token: ist_aber, S0B1Token: ist_noch, S0B2Token: ist_nichts, S0IsInLexic: true, S0Token: ist, S0_LastThreeLetters: ist, S0_LastTwoLetters: st, sein_isGouvernedBy_nichts: true, sein_isGouvernedBy_nichts_cop: true, 

4- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [aber, noch, nichts ,.. ]

B0Token: aber, B0_LastThreeLetters: ber, B0_LastTwoLetters: er, 

5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [aber]   B= [noch, nichts, gegen ,.. ]

B0IsInLexic: true, B0Token: noch, B0_LastThreeLetters: och, B0_LastTwoLetters: ch, S0B0Token: aber_noch, S0B1Token: aber_nichts, S0B2Token: aber_gegen, S0Token: aber, S0_LastThreeLetters: ber, S0_LastTwoLetters: er, aber_isGouvernedBy_nichts: true, aber_isGouvernedBy_nichts_advmod: true, 

6- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [noch, nichts, gegen ,.. ]

B0IsInLexic: true, B0Token: noch, B0_LastThreeLetters: och, B0_LastTwoLetters: ch, 

7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [noch]   B= [nichts, gegen, die ,.. ]

B0IsInLexic: true, B0Token: nichts, B0_LastThreeLetters: hts, B0_LastTwoLetters: ts, S0B0Token: noch_nichts, S0B1Token: noch_gegen, S0B2Token: noch_die, S0IsInLexic: true, S0Token: noch, S0_LastThreeLetters: och, S0_LastTwoLetters: ch, noch_isGouvernedBy_nichts: true, noch_isGouvernedBy_nichts_advmod: true, 

8- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [nichts, gegen, die ,.. ]

B0IsInLexic: true, B0Token: nichts, B0_LastThreeLetters: hts, B0_LastTwoLetters: ts, 

9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [nichts]   B= [gegen, die, schmerzhafte ,.. ]

B0Token: gegen, B0_LastThreeLetters: gen, B0_LastTwoLetters: en, S0B0Token: nichts_gegen, S0B1Token: nichts_die, S0B2Token: nichts_schmerzhafte, S0IsInLexic: true, S0Token: nichts, S0_LastThreeLetters: hts, S0_LastTwoLetters: ts, 

10- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [gegen, die, schmerzhafte ,.. ]

B0Token: gegen, B0_LastThreeLetters: gen, B0_LastTwoLetters: en, 

11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [gegen]   B= [die, schmerzhafte, analfissur ,.. ]

B0IsInLexic: true, B0Token: die, B0_LastThreeLetters: die, B0_LastTwoLetters: ie, S0B0Token: gegen_die, S0B1Token: gegen_schmerzhafte, S0B2Token: gegen_analfissur, S0Token: gegen, S0_LastThreeLetters: gen, S0_LastTwoLetters: en, gegen_isGouvernedBy_Analfissur: true, gegen_isGouvernedBy_Analfissur_case: true, 

12- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [die, schmerzhafte, analfissur ,.. ]

B0IsInLexic: true, B0Token: die, B0_LastThreeLetters: die, B0_LastTwoLetters: ie, 

13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [die]   B= [schmerzhafte, analfissur, , ,.. ]

B0Token: schmerzhafte, B0_LastThreeLetters: fte, B0_LastTwoLetters: te, S0B0Token: die_schmerzhafte, S0B1Token: die_analfissur, S0B2Token: die_,, S0IsInLexic: true, S0Token: die, S0_LastThreeLetters: die, S0_LastTwoLetters: ie, der_isGouvernedBy_Analfissur: true, der_isGouvernedBy_Analfissur_det: true, 

14- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [schmerzhafte, analfissur, , ,.. ]

B0Token: schmerzhafte, B0_LastThreeLetters: fte, B0_LastTwoLetters: te, 

15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [schmerzhafte]   B= [analfissur, ,, die ,.. ]

B0Token: analfissur, B0_LastThreeLetters: sur, B0_LastTwoLetters: ur, S0B0Token: schmerzhafte_analfissur, S0B1Token: schmerzhafte_,, S0B2Token: schmerzhafte_die, S0Token: schmerzhafte, S0_LastThreeLetters: fte, S0_LastTwoLetters: te, schmerzhaft_isGouvernedBy_Analfissur: true, schmerzhaft_isGouvernedBy_Analfissur_amod: true, 

16- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [analfissur, ,, die ,.. ]

B0Token: analfissur, B0_LastThreeLetters: sur, B0_LastTwoLetters: ur, 

17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [analfissur]   B= [,, die, sie ,.. ]

Analfissur_,_hasRighDep_punct: true, Analfissur_hasRighDep_acl: true, Analfissur_hasRighDep_punct: true, Analfissur_zugeziehen_hasRighDep_acl: true, B0Token: ,, B0_LastThreeLetters: ,, B0_LastTwoLetters: ,, S0B0Token: analfissur_,, S0B1Token: analfissur_die, S0B2Token: analfissur_sie, S0Token: analfissur, S0_LastThreeLetters: sur, S0_LastTwoLetters: ur, hasRighDep_acl: true, hasRighDep_punct: true, 

18- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, die, sie ,.. ]

B0Token: ,, B0_LastThreeLetters: ,, B0_LastTwoLetters: ,, 

19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [die, sie, sich ,.. ]

B0IsInLexic: true, B0Token: die, B0_LastThreeLetters: die, B0_LastTwoLetters: ie, S0B0Token: ,_die, S0B1Token: ,_sie, S0B2Token: ,_sich, S0Token: ,, S0_LastThreeLetters: ,, S0_LastTwoLetters: ,, 

20- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [die, sie, sich ,.. ]

B0IsInLexic: true, B0Token: die, B0_LastThreeLetters: die, B0_LastTwoLetters: ie, 

21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [die]   B= [sie, sich, bei ,.. ]

B0IsInLexic: true, B0Token: sie, B0_LastThreeLetters: sie, B0_LastTwoLetters: ie, S0B0Token: die_sie, S0B1Token: die_sich, S0B2Token: die_bei, S0IsInLexic: true, S0Token: die, S0_LastThreeLetters: die, S0_LastTwoLetters: ie, der_isGouvernedBy_zugeziehen: true, der_isGouvernedBy_zugeziehen_dobj: true, 

22- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [sie, sich, bei ,.. ]

B0IsInLexic: true, B0Token: sie, B0_LastThreeLetters: sie, B0_LastTwoLetters: ie, 

23- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [sie]   B= [sich, bei, der ,.. ]

B0IsInLexic: true, B0Token: sich, B0_LastThreeLetters: ich, B0_LastTwoLetters: ch, S0B0Token: sie_sich, S0B1Token: sie_bei, S0B2Token: sie_der, S0IsInLexic: true, S0Token: sie, S0_LastThreeLetters: sie, S0_LastTwoLetters: ie, sie_isGouvernedBy_zugeziehen: true, sie_isGouvernedBy_zugeziehen_nsubj: true, 

24- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [sich, bei, der ,.. ]

B0IsInLexic: true, B0Token: sich, B0_LastThreeLetters: ich, B0_LastTwoLetters: ch, 

25- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [sich]   B= [bei, der, verhassten ,.. ]

B0IsInLexic: true, B0Token: bei, B0_LastThreeLetters: bei, B0_LastTwoLetters: ei, S0B0Token: sich_bei, S0B1Token: sich_der, S0B2Token: sich_verhassten, S0IsInLexic: true, S0Token: sich, S0_LastThreeLetters: ich, S0_LastTwoLetters: ch, er|es|sie_isGouvernedBy_zugeziehen: true, er|es|sie_isGouvernedBy_zugeziehen_iobj: true, 

26- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [bei, der, verhassten ,.. ]

B0IsInLexic: true, B0Token: bei, B0_LastThreeLetters: bei, B0_LastTwoLetters: ei, 

27- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [bei]   B= [der, verhassten, - ,.. ]

B0IsInLexic: true, B0Token: der, B0_LastThreeLetters: der, B0_LastTwoLetters: er, S0B0Token: bei_der, S0B1Token: bei_verhassten, S0B2Token: bei_-, S0IsInLexic: true, S0Token: bei, S0_LastThreeLetters: bei, S0_LastTwoLetters: ei, bei_isGouvernedBy_Intimrasur: true, bei_isGouvernedBy_Intimrasur_case: true, 

28- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [der, verhassten, - ,.. ]

B0IsInLexic: true, B0Token: der, B0_LastThreeLetters: der, B0_LastTwoLetters: er, 

29- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [der]   B= [verhassten, -, und ,.. ]

B0Token: verhassten, B0_LastThreeLetters: ten, B0_LastTwoLetters: en, S0B0Token: der_verhassten, S0B1Token: der_-, S0B2Token: der_und, S0IsInLexic: true, S0Token: der, S0_LastThreeLetters: der, S0_LastTwoLetters: er, der_isGouvernedBy_Intimrasur: true, der_isGouvernedBy_Intimrasur_det: true, 

30- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [verhassten, -, und ,.. ]

B0Token: verhassten, B0_LastThreeLetters: ten, B0_LastTwoLetters: en, 

31- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [verhassten]   B= [-, und, wieder ,.. ]

B0Token: -, B0_LastThreeLetters: -, B0_LastTwoLetters: -, S0B0Token: verhassten_-, S0B1Token: verhassten_und, S0B2Token: verhassten_wieder, S0Token: verhassten, S0_LastThreeLetters: ten, S0_LastTwoLetters: en, hasRighDep_cc: true, hasRighDep_conj: true, hasRighDep_punct: true, verhas_-_hasRighDep_punct: true, verhas_hasRighDep_cc: true, verhas_hasRighDep_conj: true, verhas_hasRighDep_punct: true, verhas_isGouvernedBy_Intimrasur: true, verhas_isGouvernedBy_Intimrasur_amod: true, verhas_schnell_hasRighDep_conj: true, verhas_und_hasRighDep_cc: true, 

32- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [-, und, wieder ,.. ]

B0Token: -, B0_LastThreeLetters: -, B0_LastTwoLetters: -, 

33- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [-]   B= [und, wieder, mal ,.. ]

B0IsInLexic: true, B0Token: und, B0_LastThreeLetters: und, B0_LastTwoLetters: nd, S0B0Token: -_und, S0B1Token: -_wieder, S0B2Token: -_mal, S0Token: -, S0_LastThreeLetters: -, S0_LastTwoLetters: -, 

34- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [und, wieder, mal ,.. ]

B0IsInLexic: true, B0Token: und, B0_LastThreeLetters: und, B0_LastTwoLetters: nd, 

35- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [und]   B= [wieder, mal, viel ,.. ]

B0Token: wieder, B0_LastThreeLetters: der, B0_LastTwoLetters: er, S0B0Token: und_wieder, S0B1Token: und_mal, S0B2Token: und_viel, S0IsInLexic: true, S0Token: und, S0_LastThreeLetters: und, S0_LastTwoLetters: nd, 

36- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [wieder, mal, viel ,.. ]

B0Token: wieder, B0_LastThreeLetters: der, B0_LastTwoLetters: er, 

37- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [wieder]   B= [mal, viel, zu ,.. ]

B0Token: mal, B0_LastThreeLetters: mal, B0_LastTwoLetters: al, S0B0Token: wieder_mal, S0B1Token: wieder_viel, S0B2Token: wieder_zu, S0Token: wieder, S0_LastThreeLetters: der, S0_LastTwoLetters: er, wieder_isGouvernedBy_schnell: true, wieder_isGouvernedBy_schnell_advmod: true, 

38- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [mal, viel, zu ,.. ]

B0Token: mal, B0_LastThreeLetters: mal, B0_LastTwoLetters: al, 

39- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [mal]   B= [viel, zu, schnell ,.. ]

B0IsInLexic: true, B0Token: viel, B0_LastThreeLetters: iel, B0_LastTwoLetters: el, S0B0Token: mal_viel, S0B1Token: mal_zu, S0B2Token: mal_schnell, S0Token: mal, S0_LastThreeLetters: mal, S0_LastTwoLetters: al, mal_isGouvernedBy_schnell: true, mal_isGouvernedBy_schnell_advmod: true, 

40- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [viel, zu, schnell ,.. ]

B0IsInLexic: true, B0Token: viel, B0_LastThreeLetters: iel, B0_LastTwoLetters: el, 

41- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [viel]   B= [zu, schnell, angelegten ,.. ]

B0IsInLexic: true, B0Token: zu, B0_LastThreeLetters: zu, B0_LastTwoLetters: zu, S0B0Token: viel_zu, S0B1Token: viel_schnell, S0B2Token: viel_angelegten, S0IsInLexic: true, S0Token: viel, S0_LastThreeLetters: iel, S0_LastTwoLetters: el, viel_isGouvernedBy_schnell: true, viel_isGouvernedBy_schnell_advmod: true, 

42- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [zu, schnell, angelegten ,.. ]

B0IsInLexic: true, B0Token: zu, B0_LastThreeLetters: zu, B0_LastTwoLetters: zu, 

43- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [zu]   B= [schnell, angelegten, - ,.. ]

B0Token: schnell, B0_LastThreeLetters: ell, B0_LastTwoLetters: ll, S0B0Token: zu_schnell, S0B1Token: zu_angelegten, S0B2Token: zu_-, S0IsInLexic: true, S0Token: zu, S0_LastThreeLetters: zu, S0_LastTwoLetters: zu, zu_isGouvernedBy_schnell: true, zu_isGouvernedBy_schnell_advmod: true, 

44- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [schnell, angelegten, - ,.. ]

B0Token: schnell, B0_LastThreeLetters: ell, B0_LastTwoLetters: ll, 

45- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [schnell]   B= [angelegten, -, intimrasur ,.. ]

B0IsInLexic: true, B0Token: angelegten, B0_LastThreeLetters: ten, B0_LastTwoLetters: en, S0B0Token: schnell_angelegten, S0B1Token: schnell_-, S0B2Token: schnell_intimrasur, S0Token: schnell, S0_LastThreeLetters: ell, S0_LastTwoLetters: ll, 

46- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [angelegten, -, intimrasur ,.. ]

B0IsInLexic: true, B0Token: angelegten, B0_LastThreeLetters: ten, B0_LastTwoLetters: en, 

47- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [angelegten]   B= [-, intimrasur, zugezogen ,.. ]

B0Token: -, B0_LastThreeLetters: -, B0_LastTwoLetters: -, S0B0Token: angelegten_-, S0B1Token: angelegten_intimrasur, S0B2Token: angelegten_zugezogen, S0IsInLexic: true, S0Token: angelegten, S0_LastThreeLetters: ten, S0_LastTwoLetters: en, angelegt_isGouvernedBy_Intimrasur: true, angelegt_isGouvernedBy_Intimrasur_amod: true, 

48- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [-, intimrasur, zugezogen ,.. ]

B0Token: -, B0_LastThreeLetters: -, B0_LastTwoLetters: -, 

49- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [-]   B= [intimrasur, zugezogen, hat ,.. ]

-_isGouvernedBy_Intimrasur: true, -_isGouvernedBy_Intimrasur_punct: true, B0Token: intimrasur, B0_LastThreeLetters: sur, B0_LastTwoLetters: ur, S0B0Token: -_intimrasur, S0B1Token: -_zugezogen, S0B2Token: -_hat, S0Token: -, S0_LastThreeLetters: -, S0_LastTwoLetters: -, 

50- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [intimrasur, zugezogen, hat ,.. ]

B0Token: intimrasur, B0_LastThreeLetters: sur, B0_LastTwoLetters: ur, 

51- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [intimrasur]   B= [zugezogen, hat, . ,.. ]

B0IsInLexic: true, B0Token: zugezogen, B0_LastThreeLetters: gen, B0_LastTwoLetters: en, Intimrasur_isGouvernedBy_zugeziehen: true, Intimrasur_isGouvernedBy_zugeziehen_nmod: true, S0B0Token: intimrasur_zugezogen, S0B1Token: intimrasur_hat, S0B2Token: intimrasur_., S0Token: intimrasur, S0_LastThreeLetters: sur, S0_LastTwoLetters: ur, 

52- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [zugezogen, hat, . ,.. ]

B0IsInLexic: true, B0Token: zugezogen, B0_LastThreeLetters: gen, B0_LastTwoLetters: en, 

53- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [zugezogen]   B= [hat, . ,.. ]

B0IsInLexic: true, B0Token: hat, B0_LastThreeLetters: hat, B0_LastTwoLetters: at, S0B0Token: zugezogen_hat, S0B1Token: zugezogen_., S0IsInLexic: true, S0Token: zugezogen, S0_LastThreeLetters: gen, S0_LastTwoLetters: en, hasRighDep_aux: true, zugeziehen_haben_hasRighDep_aux: true, zugeziehen_hasRighDep_aux: true, 

54- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [hat, . ,.. ]

B0IsInLexic: true, B0Token: hat, B0_LastThreeLetters: hat, B0_LastTwoLetters: at, 

55- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [hat]   B= [.]

B0Token: ., B0_LastThreeLetters: ., B0_LastTwoLetters: ., S0B0Token: hat_., S0IsInLexic: true, S0Token: hat, S0_LastThreeLetters: hat, S0_LastTwoLetters: at, 

56- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [.]

B0Token: ., B0_LastThreeLetters: ., B0_LastTwoLetters: ., 

57- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [ ]

S0Token: ., S0_LastThreeLetters: ., S0_LastTwoLetters: ., 

58- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

## Sentence No. 88 - 
wäre es sinnvoll , eine elementarschadenversicherung gesetzlich vorzuschreiben , wie das etwa bei der kfz-haftpflichtversicherung der fall ist ? 
### Existing MWEs: 
1- **vorzuschreiben** (VPC)
2- **der fall ist** (ID)



0- &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [wäre, es, sinnvoll ,.. ]

B0IsInLexic: true, B0Token: wäre, B0_LastThreeLetters: �re, B0_LastTwoLetters: re, 

1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [wäre]   B= [es, sinnvoll, , ,.. ]

B0IsInLexic: true, B0Token: es, B0_LastThreeLetters: es, B0_LastTwoLetters: es, S0B0Token: wäre_es, S0B1Token: wäre_sinnvoll, S0B2Token: wäre_,, S0IsInLexic: true, S0Token: wäre, S0_LastThreeLetters: �re, S0_LastTwoLetters: re, sein_isGouvernedBy_sinnvellen: true, sein_isGouvernedBy_sinnvellen_aux: true, 

2- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [es, sinnvoll, , ,.. ]

B0IsInLexic: true, B0Token: es, B0_LastThreeLetters: es, B0_LastTwoLetters: es, 

3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [es]   B= [sinnvoll, ,, eine ,.. ]

B0Token: sinnvoll, B0_LastThreeLetters: oll, B0_LastTwoLetters: ll, S0B0Token: es_sinnvoll, S0B1Token: es_,, S0B2Token: es_eine, S0IsInLexic: true, S0Token: es, S0_LastThreeLetters: es, S0_LastTwoLetters: es, es_isGouvernedBy_sinnvellen: true, es_isGouvernedBy_sinnvellen_nsubj: true, 

4- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [sinnvoll, ,, eine ,.. ]

B0Token: sinnvoll, B0_LastThreeLetters: oll, B0_LastTwoLetters: ll, 

5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [sinnvoll]   B= [,, eine, elementarschadenversicherung ,.. ]

B0Token: ,, B0_LastThreeLetters: ,, B0_LastTwoLetters: ,, S0B0Token: sinnvoll_,, S0B1Token: sinnvoll_eine, S0B2Token: sinnvoll_elementarschadenversicherung, S0Token: sinnvoll, S0_LastThreeLetters: oll, S0_LastTwoLetters: ll, 

6- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, eine, elementarschadenversicherung ,.. ]

B0Token: ,, B0_LastThreeLetters: ,, B0_LastTwoLetters: ,, 

7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [eine, elementarschadenversicherung, gesetzlich ,.. ]

B0IsInLexic: true, B0Token: eine, B0_LastThreeLetters: ine, B0_LastTwoLetters: ne, S0B0Token: ,_eine, S0B1Token: ,_elementarschadenversicherung, S0B2Token: ,_gesetzlich, S0Token: ,, S0_LastThreeLetters: ,, S0_LastTwoLetters: ,, 

8- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [eine, elementarschadenversicherung, gesetzlich ,.. ]

B0IsInLexic: true, B0Token: eine, B0_LastThreeLetters: ine, B0_LastTwoLetters: ne, 

9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [eine]   B= [elementarschadenversicherung, gesetzlich, vorzuschreiben ,.. ]

B0Token: elementarschadenversicherung, B0_LastThreeLetters: ung, B0_LastTwoLetters: ng, S0B0Token: eine_elementarschadenversicherung, S0B1Token: eine_gesetzlich, S0B2Token: eine_vorzuschreiben, S0IsInLexic: true, S0Token: eine, S0_LastThreeLetters: ine, S0_LastTwoLetters: ne, ein_isGouvernedBy_Elementarschadenversicherung: true, ein_isGouvernedBy_Elementarschadenversicherung_det: true, 

10- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [elementarschadenversicherung, gesetzlich, vorzuschreiben ,.. ]

B0Token: elementarschadenversicherung, B0_LastThreeLetters: ung, B0_LastTwoLetters: ng, 

11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [elementarschadenversicherung]   B= [gesetzlich, vorzuschreiben, , ,.. ]

B0Token: gesetzlich, B0_LastThreeLetters: ich, B0_LastTwoLetters: ch, Elementarschadenversicherung_isGouvernedBy_vorzuschreiben: true, Elementarschadenversicherung_isGouvernedBy_vorzuschreiben_dobj: true, S0B0Token: elementarschadenversicherung_gesetzlich, S0B1Token: elementarschadenversicherung_vorzuschreiben, S0B2Token: elementarschadenversicherung_,, S0Token: elementarschadenversicherung, S0_LastThreeLetters: ung, S0_LastTwoLetters: ng, 

12- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [gesetzlich, vorzuschreiben, , ,.. ]

B0Token: gesetzlich, B0_LastThreeLetters: ich, B0_LastTwoLetters: ch, 

13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [gesetzlich]   B= [vorzuschreiben, ,, wie ,.. ]

B0IsInLexic: true, B0Token: vorzuschreiben, B0_LastThreeLetters: ben, B0_LastTwoLetters: en, S0B0Token: gesetzlich_vorzuschreiben, S0B1Token: gesetzlich_,, S0B2Token: gesetzlich_wie, S0Token: gesetzlich, S0_LastThreeLetters: ich, S0_LastTwoLetters: ch, gesetzlich_isGouvernedBy_vorzuschreiben: true, gesetzlich_isGouvernedBy_vorzuschreiben_advmod: true, 

14- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [vorzuschreiben, ,, wie ,.. ]

B0IsInLexic: true, B0Token: vorzuschreiben, B0_LastThreeLetters: ben, B0_LastTwoLetters: en, 

15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [vorzuschreiben]   B= [,, wie, das ,.. ]

B0Token: ,, B0_LastThreeLetters: ,, B0_LastTwoLetters: ,, S0B0Token: vorzuschreiben_,, S0B1Token: vorzuschreiben_wie, S0B2Token: vorzuschreiben_das, S0IsInLexic: true, S0Token: vorzuschreiben, S0_LastThreeLetters: ben, S0_LastTwoLetters: en, 

16- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, wie, das ,.. ]

B0Token: ,, B0_LastThreeLetters: ,, B0_LastTwoLetters: ,, 

17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [wie, das, etwa ,.. ]

B0IsInLexic: true, B0Token: wie, B0_LastThreeLetters: wie, B0_LastTwoLetters: ie, S0B0Token: ,_wie, S0B1Token: ,_das, S0B2Token: ,_etwa, S0Token: ,, S0_LastThreeLetters: ,, S0_LastTwoLetters: ,, 

18- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [wie, das, etwa ,.. ]

B0IsInLexic: true, B0Token: wie, B0_LastThreeLetters: wie, B0_LastTwoLetters: ie, 

19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [wie]   B= [das, etwa, bei ,.. ]

B0IsInLexic: true, B0Token: das, B0_LastThreeLetters: das, B0_LastTwoLetters: as, S0B0Token: wie_das, S0B1Token: wie_etwa, S0B2Token: wie_bei, S0IsInLexic: true, S0Token: wie, S0_LastThreeLetters: wie, S0_LastTwoLetters: ie, wie_isGouvernedBy_sein: true, wie_isGouvernedBy_sein_mark: true, 

20- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [das, etwa, bei ,.. ]

B0IsInLexic: true, B0Token: das, B0_LastThreeLetters: das, B0_LastTwoLetters: as, 

21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [das]   B= [etwa, bei, der ,.. ]

B0Token: etwa, B0_LastThreeLetters: twa, B0_LastTwoLetters: wa, S0B0Token: das_etwa, S0B1Token: das_bei, S0B2Token: das_der, S0IsInLexic: true, S0Token: das, S0_LastThreeLetters: das, S0_LastTwoLetters: as, der_isGouvernedBy_sein: true, der_isGouvernedBy_sein_nsubj: true, 

22- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [etwa, bei, der ,.. ]

B0Token: etwa, B0_LastThreeLetters: twa, B0_LastTwoLetters: wa, 

23- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [etwa]   B= [bei, der, kfz-haftpflichtversicherung ,.. ]

B0IsInLexic: true, B0Token: bei, B0_LastThreeLetters: bei, B0_LastTwoLetters: ei, S0B0Token: etwa_bei, S0B1Token: etwa_der, S0B2Token: etwa_kfz-haftpflichtversicherung, S0Token: etwa, S0_LastThreeLetters: twa, S0_LastTwoLetters: wa, etwa_isGouvernedBy_Kfz-Haftpflichtversicherung: true, etwa_isGouvernedBy_Kfz-Haftpflichtversicherung_advmod: true, 

24- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [bei, der, kfz-haftpflichtversicherung ,.. ]

B0IsInLexic: true, B0Token: bei, B0_LastThreeLetters: bei, B0_LastTwoLetters: ei, 

25- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [bei]   B= [der, kfz-haftpflichtversicherung, der ,.. ]

B0IsInLexic: true, B0Token: der, B0_LastThreeLetters: der, B0_LastTwoLetters: er, S0B0Token: bei_der, S0B1Token: bei_kfz-haftpflichtversicherung, S0B2Token: bei_der, S0IsInLexic: true, S0Token: bei, S0_LastThreeLetters: bei, S0_LastTwoLetters: ei, bei_isGouvernedBy_Kfz-Haftpflichtversicherung: true, bei_isGouvernedBy_Kfz-Haftpflichtversicherung_case: true, 

26- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [der, kfz-haftpflichtversicherung, der ,.. ]

B0IsInLexic: true, B0Token: der, B0_LastThreeLetters: der, B0_LastTwoLetters: er, 

27- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [der]   B= [kfz-haftpflichtversicherung, der, fall ,.. ]

B0Token: kfz-haftpflichtversicherung, B0_LastThreeLetters: ung, B0_LastTwoLetters: ng, S0B0Token: der_kfz-haftpflichtversicherung, S0B1Token: der_der, S0B2Token: der_fall, S0IsInLexic: true, S0Token: der, S0_LastThreeLetters: der, S0_LastTwoLetters: er, der_isGouvernedBy_Kfz-Haftpflichtversicherung: true, der_isGouvernedBy_Kfz-Haftpflichtversicherung_det: true, 

28- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [kfz-haftpflichtversicherung, der, fall ,.. ]

B0Token: kfz-haftpflichtversicherung, B0_LastThreeLetters: ung, B0_LastTwoLetters: ng, 

29- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [kfz-haftpflichtversicherung]   B= [der, fall, ist ,.. ]

B0IsInLexic: true, B0Token: der, B0_LastThreeLetters: der, B0_LastTwoLetters: er, Kfz-Haftpflichtversicherung_Fall_hasRighDep_nmod: true, Kfz-Haftpflichtversicherung_hasRighDep_nmod: true, Kfz-Haftpflichtversicherung_isGouvernedBy_sein: true, Kfz-Haftpflichtversicherung_isGouvernedBy_sein_nmod: true, S0B0Token: kfz-haftpflichtversicherung_der, S0B1Token: kfz-haftpflichtversicherung_fall, S0B2Token: kfz-haftpflichtversicherung_ist, S0Token: kfz-haftpflichtversicherung, S0_LastThreeLetters: ung, S0_LastTwoLetters: ng, hasRighDep_nmod: true, 

30- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [der, fall, ist ,.. ]

B0IsInLexic: true, B0Token: der, B0_LastThreeLetters: der, B0_LastTwoLetters: er, 

31- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [der]   B= [fall, ist, ? ,.. ]

B0IsInLexic: true, B0Token: fall, B0_LastThreeLetters: all, B0_LastTwoLetters: ll, S0B0Token: der_fall, S0B1Token: der_ist, S0B2Token: der_?, S0IsInLexic: true, S0Token: der, S0_LastThreeLetters: der, S0_LastTwoLetters: er, der_isGouvernedBy_Fall: true, der_isGouvernedBy_Fall_det: true, 

32- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [der, fall]   B= [ist, ? ,.. ]

B0IsInLexic: true, B0Token: ist, B0_LastThreeLetters: ist, B0_LastTwoLetters: st, S0B0Token: fall_ist, S0B1Token: fall_?, S0IsInLexic: true, S0S1Distance: 1, S0Token: fall, S0_LastThreeLetters: all, S0_LastTwoLetters: ll, S1B0Token: der_ist, S1IsInLexic: true, S1S0B0Token: der_fall_ist, S1S0Token: der_fall, S1Token: der, S1_LastThreeLetters: der, S1_LastTwoLetters: er, SyntaxicRelation: -det, 

33- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [der, fall, ist]   B= [?]

B0Token: ?, B0_LastThreeLetters: ?, B0_LastTwoLetters: ?, S0B0Token: ist_?, S0IsInLexic: true, S0S1Distance: 1, S0Token: ist, S0_LastThreeLetters: ist, S0_LastTwoLetters: st, S1B0Token: fall_?, S1IsInLexic: true, S1S0B0Token: fall_ist_?, S1S0Token: fall_ist, S1Token: fall, S1_LastThreeLetters: all, S1_LastTwoLetters: ll, 

34- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [der, [fall, ist]]   B= [?]

B0Token: ?, B0_LastThreeLetters: ?, B0_LastTwoLetters: ?, S0B0Token: fall_ist_?, S0Token: fall_ist, S1B0Token: der_?, S1IsInLexic: true, S1S0B0Token: der_fall_ist_?, S1S0Token: der_fall_ist, S1Token: der, S1_LastThreeLetters: der, S1_LastTwoLetters: er, 

35- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[der, [fall, ist]]]   B= [?]

B0Token: ?, B0_LastThreeLetters: ?, B0_LastTwoLetters: ?, S0B0Token: der_fall_ist_?, S0Token: der_fall_ist, 

36- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [?]

B0Token: ?, B0_LastThreeLetters: ?, B0_LastTwoLetters: ?, 

37- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [?]   B= [ ]

S0Token: ?, S0_LastThreeLetters: ?, S0_LastTwoLetters: ?, 

38- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

## Sentence No. 111 - 
tonje haugland , die diegräfin mariza geben wird , hatte mit hardi lang als baronzsupan sichtlich spaß am ebenso populären song " komm mit nach varasdin " .... nach einem etwas holprigen wahlkampf-start hatte thöle in den vergangenen wochen den eindruck , dass die spd wieder stärker punkten konnte . 
### Existing MWEs: 
2- **hatte spaß** (ID)
1- **hatte eindruck** (ID)



0- &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [tonje, haugland, , ,.. ]

B0Token: tonje, B0_LastThreeLetters: nje, B0_LastTwoLetters: je, 

1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [tonje]   B= [haugland, ,, die ,.. ]

B0Token: haugland, B0_LastThreeLetters: and, B0_LastTwoLetters: nd, S0B0Token: tonje_haugland, S0B1Token: tonje_,, S0B2Token: tonje_die, S0Token: tonje, S0_LastThreeLetters: nje, S0_LastTwoLetters: je, Tonje_isGouvernedBy_Haugland: true, Tonje_isGouvernedBy_Haugland_name: true, 

2- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [haugland, ,, die ,.. ]

B0Token: haugland, B0_LastThreeLetters: and, B0_LastTwoLetters: nd, 

3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [haugland]   B= [,, die, diegräfin ,.. ]

B0Token: ,, B0_LastThreeLetters: ,, B0_LastTwoLetters: ,, Haugland_,_hasRighDep_punct: true, Haugland_Mariza_hasRighDep_appos: true, Haugland_hasRighDep_appos: true, Haugland_hasRighDep_punct: true, Haugland_isGouvernedBy_ben: true, Haugland_isGouvernedBy_ben_nsubjpass: true, S0B0Token: haugland_,, S0B1Token: haugland_die, S0B2Token: haugland_diegräfin, S0Token: haugland, S0_LastThreeLetters: and, S0_LastTwoLetters: nd, hasRighDep_appos: true, hasRighDep_punct: true, 

4- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, die, diegräfin ,.. ]

B0Token: ,, B0_LastThreeLetters: ,, B0_LastTwoLetters: ,, 

5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [die, diegräfin, mariza ,.. ]

B0IsInLexic: true, B0Token: die, B0_LastThreeLetters: die, B0_LastTwoLetters: ie, S0B0Token: ,_die, S0B1Token: ,_diegräfin, S0B2Token: ,_mariza, S0Token: ,, S0_LastThreeLetters: ,, S0_LastTwoLetters: ,, 

6- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [die, diegräfin, mariza ,.. ]

B0IsInLexic: true, B0Token: die, B0_LastThreeLetters: die, B0_LastTwoLetters: ie, 

7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [die]   B= [diegräfin, mariza, geben ,.. ]

B0Token: diegräfin, B0_LastThreeLetters: fin, B0_LastTwoLetters: in, S0B0Token: die_diegräfin, S0B1Token: die_mariza, S0B2Token: die_geben, S0IsInLexic: true, S0Token: die, S0_LastThreeLetters: die, S0_LastTwoLetters: ie, der_isGouvernedBy_dieGräfin: true, der_isGouvernedBy_dieGräfin_det: true, 

8- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [diegräfin, mariza, geben ,.. ]

B0Token: diegräfin, B0_LastThreeLetters: fin, B0_LastTwoLetters: in, 

9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [diegräfin]   B= [mariza, geben, wird ,.. ]

B0Token: mariza, B0_LastThreeLetters: iza, B0_LastTwoLetters: za, S0B0Token: diegräfin_mariza, S0B1Token: diegräfin_geben, S0B2Token: diegräfin_wird, S0Token: diegräfin, S0_LastThreeLetters: fin, S0_LastTwoLetters: in, dieGräfin_isGouvernedBy_Mariza: true, dieGräfin_isGouvernedBy_Mariza_name: true, 

10- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [mariza, geben, wird ,.. ]

B0Token: mariza, B0_LastThreeLetters: iza, B0_LastTwoLetters: za, 

11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [mariza]   B= [geben, wird, , ,.. ]

B0IsInLexic: true, B0Token: geben, B0_LastThreeLetters: ben, B0_LastTwoLetters: en, S0B0Token: mariza_geben, S0B1Token: mariza_wird, S0B2Token: mariza_,, S0Token: mariza, S0_LastThreeLetters: iza, S0_LastTwoLetters: za, 

12- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [geben, wird, , ,.. ]

B0IsInLexic: true, B0Token: geben, B0_LastThreeLetters: ben, B0_LastTwoLetters: en, 

13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [geben]   B= [wird, ,, hatte ,.. ]

B0IsInLexic: true, B0Token: wird, B0_LastThreeLetters: ird, B0_LastTwoLetters: rd, S0B0Token: geben_wird, S0B1Token: geben_,, S0B2Token: geben_hatte, S0IsInLexic: true, S0Token: geben, S0_LastThreeLetters: ben, S0_LastTwoLetters: en, 

14- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [wird, ,, hatte ,.. ]

B0IsInLexic: true, B0Token: wird, B0_LastThreeLetters: ird, B0_LastTwoLetters: rd, 

15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [wird]   B= [,, hatte, mit ,.. ]

B0Token: ,, B0_LastThreeLetters: ,, B0_LastTwoLetters: ,, S0B0Token: wird_,, S0B1Token: wird_hatte, S0B2Token: wird_mit, S0IsInLexic: true, S0Token: wird, S0_LastThreeLetters: ird, S0_LastTwoLetters: rd, 

16- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, hatte, mit ,.. ]

B0Token: ,, B0_LastThreeLetters: ,, B0_LastTwoLetters: ,, 

17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [hatte, mit, hardi ,.. ]

B0IsInLexic: true, B0Token: hatte, B0_LastThreeLetters: tte, B0_LastTwoLetters: te, S0B0Token: ,_hatte, S0B1Token: ,_mit, S0B2Token: ,_hardi, S0Token: ,, S0_LastThreeLetters: ,, S0_LastTwoLetters: ,, 

18- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [hatte, mit, hardi ,.. ]

B0IsInLexic: true, B0Token: hatte, B0_LastThreeLetters: tte, B0_LastTwoLetters: te, 

19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [hatte]   B= [mit, hardi, lang ,.. ]

B0IsInLexic: true, B0Token: mit, B0_LastThreeLetters: mit, B0_LastTwoLetters: it, S0B0Token: hatte_mit, S0B1Token: hatte_hardi, S0B2Token: hatte_lang, S0IsInLexic: true, S0Token: hatte, S0_LastThreeLetters: tte, S0_LastTwoLetters: te, haben_isGouvernedBy_punken: true, haben_isGouvernedBy_punken_aux: true, 

20- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [hatte, mit]   B= [hardi, lang, als ,.. ]

B0Token: hardi, B0_LastThreeLetters: rdi, B0_LastTwoLetters: di, S0B0Token: mit_hardi, S0B1Token: mit_lang, S0B2Token: mit_als, S0IsInLexic: true, S0S1Distance: 1, S0Token: mit, S0_LastThreeLetters: mit, S0_LastTwoLetters: it, S1B0Token: hatte_hardi, S1IsInLexic: true, S1S0B0Token: hatte_mit_hardi, S1S0Token: hatte_mit, S1Token: hatte, S1_LastThreeLetters: tte, S1_LastTwoLetters: te, mit_isGouvernedBy_Lang: true, mit_isGouvernedBy_Lang_case: true, 

21- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [hatte]   B= [hardi, lang, als ,.. ]

B0Token: hardi, B0_LastThreeLetters: rdi, B0_LastTwoLetters: di, S0B0Token: hatte_hardi, S0B1Token: hatte_lang, S0B2Token: hatte_als, S0IsInLexic: true, S0Token: hatte, S0_LastThreeLetters: tte, S0_LastTwoLetters: te, haben_isGouvernedBy_punken: true, haben_isGouvernedBy_punken_aux: true, 

22- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [hatte, hardi]   B= [lang, als, baronzsupan ,.. ]

B0Token: lang, B0_LastThreeLetters: ang, B0_LastTwoLetters: ng, Hardi_isGouvernedBy_Lang: true, Hardi_isGouvernedBy_Lang_name: true, S0B0Token: hardi_lang, S0B1Token: hardi_als, S0B2Token: hardi_baronzsupan, S0S1Distance: 2, S0Token: hardi, S0_LastThreeLetters: rdi, S0_LastTwoLetters: di, S1B0Token: hatte_lang, S1IsInLexic: true, S1S0B0Token: hatte_hardi_lang, S1S0Token: hatte_hardi, S1Token: hatte, S1_LastThreeLetters: tte, S1_LastTwoLetters: te, 

23- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [hatte]   B= [lang, als, baronzsupan ,.. ]

B0Token: lang, B0_LastThreeLetters: ang, B0_LastTwoLetters: ng, S0B0Token: hatte_lang, S0B1Token: hatte_als, S0B2Token: hatte_baronzsupan, S0IsInLexic: true, S0Token: hatte, S0_LastThreeLetters: tte, S0_LastTwoLetters: te, haben_isGouvernedBy_punken: true, haben_isGouvernedBy_punken_aux: true, 

24- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [hatte, lang]   B= [als, baronzsupan, sichtlich ,.. ]

B0IsInLexic: true, B0Token: als, B0_LastThreeLetters: als, B0_LastTwoLetters: ls, Lang_BaronZsupan_hasRighDep_nmod: true, Lang_hasRighDep_nmod: true, Lang_isGouvernedBy_punken: true, Lang_isGouvernedBy_punken_nmod: true, S0B0Token: lang_als, S0B1Token: lang_baronzsupan, S0B2Token: lang_sichtlich, S0S1Distance: 3, S0Token: lang, S0_LastThreeLetters: ang, S0_LastTwoLetters: ng, S1B0Token: hatte_als, S1IsInLexic: true, S1S0B0Token: hatte_lang_als, S1S0Token: hatte_lang, S1Token: hatte, S1_LastThreeLetters: tte, S1_LastTwoLetters: te, hasRighDep_nmod: true, 

25- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [hatte]   B= [als, baronzsupan, sichtlich ,.. ]

B0IsInLexic: true, B0Token: als, B0_LastThreeLetters: als, B0_LastTwoLetters: ls, S0B0Token: hatte_als, S0B1Token: hatte_baronzsupan, S0B2Token: hatte_sichtlich, S0IsInLexic: true, S0Token: hatte, S0_LastThreeLetters: tte, S0_LastTwoLetters: te, haben_isGouvernedBy_punken: true, haben_isGouvernedBy_punken_aux: true, 

26- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [hatte, als]   B= [baronzsupan, sichtlich, spaß ,.. ]

B0Token: baronzsupan, B0_LastThreeLetters: pan, B0_LastTwoLetters: an, S0B0Token: als_baronzsupan, S0B1Token: als_sichtlich, S0B2Token: als_spaß, S0IsInLexic: true, S0S1Distance: 4, S0Token: als, S0_LastThreeLetters: als, S0_LastTwoLetters: ls, S1B0Token: hatte_baronzsupan, S1IsInLexic: true, S1S0B0Token: hatte_als_baronzsupan, S1S0Token: hatte_als, S1Token: hatte, S1_LastThreeLetters: tte, S1_LastTwoLetters: te, als_isGouvernedBy_BaronZsupan: true, als_isGouvernedBy_BaronZsupan_case: true, 

27- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [hatte]   B= [baronzsupan, sichtlich, spaß ,.. ]

B0Token: baronzsupan, B0_LastThreeLetters: pan, B0_LastTwoLetters: an, S0B0Token: hatte_baronzsupan, S0B1Token: hatte_sichtlich, S0B2Token: hatte_spaß, S0IsInLexic: true, S0Token: hatte, S0_LastThreeLetters: tte, S0_LastTwoLetters: te, haben_isGouvernedBy_punken: true, haben_isGouvernedBy_punken_aux: true, 

28- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [hatte, baronzsupan]   B= [sichtlich, spaß, am ,.. ]

B0Token: sichtlich, B0_LastThreeLetters: ich, B0_LastTwoLetters: ch, S0B0Token: baronzsupan_sichtlich, S0B1Token: baronzsupan_spaß, S0B2Token: baronzsupan_am, S0S1Distance: 5, S0Token: baronzsupan, S0_LastThreeLetters: pan, S0_LastTwoLetters: an, S1B0Token: hatte_sichtlich, S1IsInLexic: true, S1S0B0Token: hatte_baronzsupan_sichtlich, S1S0Token: hatte_baronzsupan, S1Token: hatte, S1_LastThreeLetters: tte, S1_LastTwoLetters: te, 

29- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [hatte]   B= [sichtlich, spaß, am ,.. ]

B0Token: sichtlich, B0_LastThreeLetters: ich, B0_LastTwoLetters: ch, S0B0Token: hatte_sichtlich, S0B1Token: hatte_spaß, S0B2Token: hatte_am, S0IsInLexic: true, S0Token: hatte, S0_LastThreeLetters: tte, S0_LastTwoLetters: te, haben_isGouvernedBy_punken: true, haben_isGouvernedBy_punken_aux: true, 

30- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [hatte, sichtlich]   B= [spaß, am, ebenso ,.. ]

B0IsInLexic: true, B0Token: spaß, B0_LastThreeLetters: aß, B0_LastTwoLetters: ß, S0B0Token: sichtlich_spaß, S0B1Token: sichtlich_am, S0B2Token: sichtlich_ebenso, S0S1Distance: 6, S0Token: sichtlich, S0_LastThreeLetters: ich, S0_LastTwoLetters: ch, S1B0Token: hatte_spaß, S1IsInLexic: true, S1S0B0Token: hatte_sichtlich_spaß, S1S0Token: hatte_sichtlich, S1Token: hatte, S1_LastThreeLetters: tte, S1_LastTwoLetters: te, sichtlich_isGouvernedBy_Spaß: true, sichtlich_isGouvernedBy_Spaß_advmod: true, 

31- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [hatte]   B= [spaß, am, ebenso ,.. ]

B0IsInLexic: true, B0Token: spaß, B0_LastThreeLetters: aß, B0_LastTwoLetters: ß, S0B0Token: hatte_spaß, S0B1Token: hatte_am, S0B2Token: hatte_ebenso, S0IsInLexic: true, S0Token: hatte, S0_LastThreeLetters: tte, S0_LastTwoLetters: te, haben_isGouvernedBy_punken: true, haben_isGouvernedBy_punken_aux: true, 

32- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [hatte, spaß]   B= [am, ebenso, populären ,.. ]

B0IsInLexic: true, B0Token: am, B0_LastThreeLetters: am, B0_LastTwoLetters: am, S0B0Token: spaß_am, S0B1Token: spaß_ebenso, S0B2Token: spaß_populären, S0IsInLexic: true, S0S1Distance: 7, S0Token: spaß, S0_LastThreeLetters: aß, S0_LastTwoLetters: ß, S1B0Token: hatte_am, S1IsInLexic: true, S1S0B0Token: hatte_spaß_am, S1S0Token: hatte_spaß, S1Token: hatte, S1_LastThreeLetters: tte, S1_LastTwoLetters: te, Spaß_isGouvernedBy_punken: true, Spaß_isGouvernedBy_punken_dobj: true, 

33- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[hatte, spaß]]   B= [am, ebenso, populären ,.. ]

B0IsInLexic: true, B0Token: am, B0_LastThreeLetters: am, B0_LastTwoLetters: am, S0B0Token: hatte_spaß_am, S0B1Token: hatte_spaß_ebenso, S0B2Token: hatte_spaß_populären, S0Token: hatte_spaß, 

34- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [am, ebenso, populären ,.. ]

B0IsInLexic: true, B0Token: am, B0_LastThreeLetters: am, B0_LastTwoLetters: am, 

35- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [am]   B= [ebenso, populären, song ,.. ]

B0Token: ebenso, B0_LastThreeLetters: nso, B0_LastTwoLetters: so, S0B0Token: am_ebenso, S0B1Token: am_populären, S0B2Token: am_song, S0IsInLexic: true, S0Token: am, S0_LastThreeLetters: am, S0_LastTwoLetters: am, an+der_isGouvernedBy_Song: true, an+der_isGouvernedBy_Song_case: true, 

36- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ebenso, populären, song ,.. ]

B0Token: ebenso, B0_LastThreeLetters: nso, B0_LastTwoLetters: so, 

37- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ebenso]   B= [populären, song, " ,.. ]

B0Token: populären, B0_LastThreeLetters: ren, B0_LastTwoLetters: en, S0B0Token: ebenso_populären, S0B1Token: ebenso_song, S0B2Token: ebenso_", S0Token: ebenso, S0_LastThreeLetters: nso, S0_LastTwoLetters: so, ebenso_isGouvernedBy_populär: true, ebenso_isGouvernedBy_populär_advmod: true, 

38- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [populären, song, " ,.. ]

B0Token: populären, B0_LastThreeLetters: ren, B0_LastTwoLetters: en, 

39- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [populären]   B= [song, ", komm ,.. ]

B0Token: song, B0_LastThreeLetters: ong, B0_LastTwoLetters: ng, S0B0Token: populären_song, S0B1Token: populären_", S0B2Token: populären_komm, S0Token: populären, S0_LastThreeLetters: ren, S0_LastTwoLetters: en, populär_isGouvernedBy_Song: true, populär_isGouvernedBy_Song_amod: true, 

40- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [song, ", komm ,.. ]

B0Token: song, B0_LastThreeLetters: ong, B0_LastTwoLetters: ng, 

41- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [song]   B= [", komm, mit ,.. ]

B0Token: ", B0_LastThreeLetters: ", B0_LastTwoLetters: ", S0B0Token: song_", S0B1Token: song_komm, S0B2Token: song_mit, S0Token: song, S0_LastThreeLetters: ong, S0_LastTwoLetters: ng, Song_isGouvernedBy_Komm: true, Song_isGouvernedBy_Komm_nmod: true, 

42- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [", komm, mit ,.. ]

B0Token: ", B0_LastThreeLetters: ", B0_LastTwoLetters: ", 

43- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= ["]   B= [komm, mit, nach ,.. ]

"_isGouvernedBy_Komm: true, "_isGouvernedBy_Komm_punct: true, B0Token: komm, B0_LastThreeLetters: omm, B0_LastTwoLetters: mm, S0B0Token: "_komm, S0B1Token: "_mit, S0B2Token: "_nach, S0Token: ", S0_LastThreeLetters: ", S0_LastTwoLetters: ", 

44- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [komm, mit, nach ,.. ]

B0Token: komm, B0_LastThreeLetters: omm, B0_LastTwoLetters: mm, 

45- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [komm]   B= [mit, nach, varasdin ,.. ]

B0IsInLexic: true, B0Token: mit, B0_LastThreeLetters: mit, B0_LastTwoLetters: it, Komm_...._hasRighDep_punct: true, Komm_Varasdin_hasRighDep_nmod: true, Komm_hasRighDep_nmod: true, Komm_hasRighDep_punct: true, Komm_isGouvernedBy_punken: true, Komm_isGouvernedBy_punken_nsubj: true, S0B0Token: komm_mit, S0B1Token: komm_nach, S0B2Token: komm_varasdin, S0Token: komm, S0_LastThreeLetters: omm, S0_LastTwoLetters: mm, hasRighDep_nmod: true, hasRighDep_punct: true, 

46- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [mit, nach, varasdin ,.. ]

B0IsInLexic: true, B0Token: mit, B0_LastThreeLetters: mit, B0_LastTwoLetters: it, 

47- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [mit]   B= [nach, varasdin, " ,.. ]

B0IsInLexic: true, B0Token: nach, B0_LastThreeLetters: ach, B0_LastTwoLetters: ch, S0B0Token: mit_nach, S0B1Token: mit_varasdin, S0B2Token: mit_", S0IsInLexic: true, S0Token: mit, S0_LastThreeLetters: mit, S0_LastTwoLetters: it, mit_isGouvernedBy_Varasdin: true, mit_isGouvernedBy_Varasdin_case: true, 

48- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [nach, varasdin, " ,.. ]

B0IsInLexic: true, B0Token: nach, B0_LastThreeLetters: ach, B0_LastTwoLetters: ch, 

49- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [nach]   B= [varasdin, ", .... ,.. ]

B0Token: varasdin, B0_LastThreeLetters: din, B0_LastTwoLetters: in, S0B0Token: nach_varasdin, S0B1Token: nach_", S0B2Token: nach_...., S0IsInLexic: true, S0Token: nach, S0_LastThreeLetters: ach, S0_LastTwoLetters: ch, nach_isGouvernedBy_Varasdin: true, nach_isGouvernedBy_Varasdin_case: true, 

50- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [varasdin, ", .... ,.. ]

B0Token: varasdin, B0_LastThreeLetters: din, B0_LastTwoLetters: in, 

51- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [varasdin]   B= [", ...., nach ,.. ]

B0Token: ", B0_LastThreeLetters: ", B0_LastTwoLetters: ", S0B0Token: varasdin_", S0B1Token: varasdin_...., S0B2Token: varasdin_nach, S0Token: varasdin, S0_LastThreeLetters: din, S0_LastTwoLetters: in, Varasdin_"_hasRighDep_punct: true, Varasdin_hasRighDep_punct: true, hasRighDep_punct: true, 

52- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [", ...., nach ,.. ]

B0Token: ", B0_LastThreeLetters: ", B0_LastTwoLetters: ", 

53- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= ["]   B= [...., nach, einem ,.. ]

B0Token: ...., B0_LastThreeLetters: ..., B0_LastTwoLetters: .., S0B0Token: "_...., S0B1Token: "_nach, S0B2Token: "_einem, S0Token: ", S0_LastThreeLetters: ", S0_LastTwoLetters: ", 

54- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [...., nach, einem ,.. ]

B0Token: ...., B0_LastThreeLetters: ..., B0_LastTwoLetters: .., 

55- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [....]   B= [nach, einem, etwas ,.. ]

B0IsInLexic: true, B0Token: nach, B0_LastThreeLetters: ach, B0_LastTwoLetters: ch, S0B0Token: ...._nach, S0B1Token: ...._einem, S0B2Token: ...._etwas, S0Token: ...., S0_LastThreeLetters: ..., S0_LastTwoLetters: .., 

56- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [nach, einem, etwas ,.. ]

B0IsInLexic: true, B0Token: nach, B0_LastThreeLetters: ach, B0_LastTwoLetters: ch, 

57- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [nach]   B= [einem, etwas, holprigen ,.. ]

B0IsInLexic: true, B0Token: einem, B0_LastThreeLetters: nem, B0_LastTwoLetters: em, S0B0Token: nach_einem, S0B1Token: nach_etwas, S0B2Token: nach_holprigen, S0IsInLexic: true, S0Token: nach, S0_LastThreeLetters: ach, S0_LastTwoLetters: ch, nach_isGouvernedBy_Wahlkampf-Start: true, nach_isGouvernedBy_Wahlkampf-Start_case: true, 

58- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [einem, etwas, holprigen ,.. ]

B0IsInLexic: true, B0Token: einem, B0_LastThreeLetters: nem, B0_LastTwoLetters: em, 

59- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [einem]   B= [etwas, holprigen, wahlkampf-start ,.. ]

B0Token: etwas, B0_LastThreeLetters: was, B0_LastTwoLetters: as, S0B0Token: einem_etwas, S0B1Token: einem_holprigen, S0B2Token: einem_wahlkampf-start, S0IsInLexic: true, S0Token: einem, S0_LastThreeLetters: nem, S0_LastTwoLetters: em, ein_isGouvernedBy_Wahlkampf-Start: true, ein_isGouvernedBy_Wahlkampf-Start_det: true, 

60- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [etwas, holprigen, wahlkampf-start ,.. ]

B0Token: etwas, B0_LastThreeLetters: was, B0_LastTwoLetters: as, 

61- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [etwas]   B= [holprigen, wahlkampf-start, hatte ,.. ]

B0Token: holprigen, B0_LastThreeLetters: gen, B0_LastTwoLetters: en, S0B0Token: etwas_holprigen, S0B1Token: etwas_wahlkampf-start, S0B2Token: etwas_hatte, S0Token: etwas, S0_LastThreeLetters: was, S0_LastTwoLetters: as, etwas_isGouvernedBy_holprig: true, etwas_isGouvernedBy_holprig_advmod: true, 

62- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [holprigen, wahlkampf-start, hatte ,.. ]

B0Token: holprigen, B0_LastThreeLetters: gen, B0_LastTwoLetters: en, 

63- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [holprigen]   B= [wahlkampf-start, hatte, thöle ,.. ]

B0Token: wahlkampf-start, B0_LastThreeLetters: art, B0_LastTwoLetters: rt, S0B0Token: holprigen_wahlkampf-start, S0B1Token: holprigen_hatte, S0B2Token: holprigen_thöle, S0Token: holprigen, S0_LastThreeLetters: gen, S0_LastTwoLetters: en, holprig_isGouvernedBy_Wahlkampf-Start: true, holprig_isGouvernedBy_Wahlkampf-Start_amod: true, 

64- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [wahlkampf-start, hatte, thöle ,.. ]

B0Token: wahlkampf-start, B0_LastThreeLetters: art, B0_LastTwoLetters: rt, 

65- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [wahlkampf-start]   B= [hatte, thöle, in ,.. ]

B0IsInLexic: true, B0Token: hatte, B0_LastThreeLetters: tte, B0_LastTwoLetters: te, S0B0Token: wahlkampf-start_hatte, S0B1Token: wahlkampf-start_thöle, S0B2Token: wahlkampf-start_in, S0Token: wahlkampf-start, S0_LastThreeLetters: art, S0_LastTwoLetters: rt, Wahlkampf-Start_Woche_hasRighDep_nmod: true, Wahlkampf-Start_der_hasRighDep_det: true, Wahlkampf-Start_haben_hasRighDep_aux: true, Wahlkampf-Start_hasRighDep_aux: true, Wahlkampf-Start_hasRighDep_det: true, Wahlkampf-Start_hasRighDep_nmod: true, Wahlkampf-Start_isGouvernedBy_Eindruck: true, Wahlkampf-Start_isGouvernedBy_Eindruck_nmod: true, hasRighDep_aux: true, hasRighDep_det: true, hasRighDep_nmod: true, 

66- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [hatte, thöle, in ,.. ]

B0IsInLexic: true, B0Token: hatte, B0_LastThreeLetters: tte, B0_LastTwoLetters: te, 

67- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [hatte]   B= [thöle, in, den ,.. ]

B0Token: thöle, B0_LastThreeLetters: �le, B0_LastTwoLetters: le, S0B0Token: hatte_thöle, S0B1Token: hatte_in, S0B2Token: hatte_den, S0IsInLexic: true, S0Token: hatte, S0_LastThreeLetters: tte, S0_LastTwoLetters: te, haben_Thöle_hasRighDep_appos: true, haben_hasRighDep_appos: true, hasRighDep_appos: true, 

68- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [hatte, thöle]   B= [in, den, vergangenen ,.. ]

B0IsInLexic: true, B0Token: in, B0_LastThreeLetters: in, B0_LastTwoLetters: in, S0B0Token: thöle_in, S0B1Token: thöle_den, S0B2Token: thöle_vergangenen, S0S1Distance: 1, S0Token: thöle, S0_LastThreeLetters: �le, S0_LastTwoLetters: le, S1B0Token: hatte_in, S1IsInLexic: true, S1S0B0Token: hatte_thöle_in, S1S0Token: hatte_thöle, S1Token: hatte, S1_LastThreeLetters: tte, S1_LastTwoLetters: te, SyntaxicRelation: +appos, 

69- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [hatte]   B= [in, den, vergangenen ,.. ]

B0IsInLexic: true, B0Token: in, B0_LastThreeLetters: in, B0_LastTwoLetters: in, S0B0Token: hatte_in, S0B1Token: hatte_den, S0B2Token: hatte_vergangenen, S0IsInLexic: true, S0Token: hatte, S0_LastThreeLetters: tte, S0_LastTwoLetters: te, 

70- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [hatte, in]   B= [den, vergangenen, wochen ,.. ]

B0IsInLexic: true, B0Token: den, B0_LastThreeLetters: den, B0_LastTwoLetters: en, S0B0Token: in_den, S0B1Token: in_vergangenen, S0B2Token: in_wochen, S0IsInLexic: true, S0S1Distance: 2, S0Token: in, S0_LastThreeLetters: in, S0_LastTwoLetters: in, S1B0Token: hatte_den, S1IsInLexic: true, S1S0B0Token: hatte_in_den, S1S0Token: hatte_in, S1Token: hatte, S1_LastThreeLetters: tte, S1_LastTwoLetters: te, in_isGouvernedBy_Woche: true, in_isGouvernedBy_Woche_case: true, 

71- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [hatte]   B= [den, vergangenen, wochen ,.. ]

B0IsInLexic: true, B0Token: den, B0_LastThreeLetters: den, B0_LastTwoLetters: en, S0B0Token: hatte_den, S0B1Token: hatte_vergangenen, S0B2Token: hatte_wochen, S0IsInLexic: true, S0Token: hatte, S0_LastThreeLetters: tte, S0_LastTwoLetters: te, 

72- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [hatte, den]   B= [vergangenen, wochen, den ,.. ]

B0Token: vergangenen, B0_LastThreeLetters: nen, B0_LastTwoLetters: en, S0B0Token: den_vergangenen, S0B1Token: den_wochen, S0B2Token: den_den, S0IsInLexic: true, S0S1Distance: 3, S0Token: den, S0_LastThreeLetters: den, S0_LastTwoLetters: en, S1B0Token: hatte_vergangenen, S1IsInLexic: true, S1S0B0Token: hatte_den_vergangenen, S1S0Token: hatte_den, S1Token: hatte, S1_LastThreeLetters: tte, S1_LastTwoLetters: te, der_isGouvernedBy_Woche: true, der_isGouvernedBy_Woche_det: true, 

73- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [hatte]   B= [vergangenen, wochen, den ,.. ]

B0Token: vergangenen, B0_LastThreeLetters: nen, B0_LastTwoLetters: en, S0B0Token: hatte_vergangenen, S0B1Token: hatte_wochen, S0B2Token: hatte_den, S0IsInLexic: true, S0Token: hatte, S0_LastThreeLetters: tte, S0_LastTwoLetters: te, 

74- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [hatte, vergangenen]   B= [wochen, den, eindruck ,.. ]

B0Token: wochen, B0_LastThreeLetters: hen, B0_LastTwoLetters: en, S0B0Token: vergangenen_wochen, S0B1Token: vergangenen_den, S0B2Token: vergangenen_eindruck, S0S1Distance: 4, S0Token: vergangenen, S0_LastThreeLetters: nen, S0_LastTwoLetters: en, S1B0Token: hatte_wochen, S1IsInLexic: true, S1S0B0Token: hatte_vergangenen_wochen, S1S0Token: hatte_vergangenen, S1Token: hatte, S1_LastThreeLetters: tte, S1_LastTwoLetters: te, vergangen_isGouvernedBy_Woche: true, vergangen_isGouvernedBy_Woche_amod: true, 

75- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [hatte]   B= [wochen, den, eindruck ,.. ]

B0Token: wochen, B0_LastThreeLetters: hen, B0_LastTwoLetters: en, S0B0Token: hatte_wochen, S0B1Token: hatte_den, S0B2Token: hatte_eindruck, S0IsInLexic: true, S0Token: hatte, S0_LastThreeLetters: tte, S0_LastTwoLetters: te, 

76- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [hatte, wochen]   B= [den, eindruck, , ,.. ]

B0IsInLexic: true, B0Token: den, B0_LastThreeLetters: den, B0_LastTwoLetters: en, S0B0Token: wochen_den, S0B1Token: wochen_eindruck, S0B2Token: wochen_,, S0S1Distance: 5, S0Token: wochen, S0_LastThreeLetters: hen, S0_LastTwoLetters: en, S1B0Token: hatte_den, S1IsInLexic: true, S1S0B0Token: hatte_wochen_den, S1S0Token: hatte_wochen, S1Token: hatte, S1_LastThreeLetters: tte, S1_LastTwoLetters: te, 

77- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [hatte]   B= [den, eindruck, , ,.. ]

B0IsInLexic: true, B0Token: den, B0_LastThreeLetters: den, B0_LastTwoLetters: en, S0B0Token: hatte_den, S0B1Token: hatte_eindruck, S0B2Token: hatte_,, S0IsInLexic: true, S0Token: hatte, S0_LastThreeLetters: tte, S0_LastTwoLetters: te, 

78- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [hatte, den]   B= [eindruck, ,, dass ,.. ]

B0IsInLexic: true, B0Token: eindruck, B0_LastThreeLetters: uck, B0_LastTwoLetters: ck, S0B0Token: den_eindruck, S0B1Token: den_,, S0B2Token: den_dass, S0IsInLexic: true, S0S1Distance: 6, S0Token: den, S0_LastThreeLetters: den, S0_LastTwoLetters: en, S1B0Token: hatte_eindruck, S1IsInLexic: true, S1S0B0Token: hatte_den_eindruck, S1S0Token: hatte_den, S1Token: hatte, S1_LastThreeLetters: tte, S1_LastTwoLetters: te, 

79- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [hatte]   B= [eindruck, ,, dass ,.. ]

B0IsInLexic: true, B0Token: eindruck, B0_LastThreeLetters: uck, B0_LastTwoLetters: ck, S0B0Token: hatte_eindruck, S0B1Token: hatte_,, S0B2Token: hatte_dass, S0IsInLexic: true, S0Token: hatte, S0_LastThreeLetters: tte, S0_LastTwoLetters: te, 

80- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [hatte, eindruck]   B= [,, dass, die ,.. ]

B0Token: ,, B0_LastThreeLetters: ,, B0_LastTwoLetters: ,, Eindruck_,_hasRighDep_punct: true, Eindruck_hasRighDep_punct: true, Eindruck_isGouvernedBy_punken: true, Eindruck_isGouvernedBy_punken_dobj: true, S0B0Token: eindruck_,, S0B1Token: eindruck_dass, S0B2Token: eindruck_die, S0IsInLexic: true, S0S1Distance: 7, S0Token: eindruck, S0_LastThreeLetters: uck, S0_LastTwoLetters: ck, S1B0Token: hatte_,, S1IsInLexic: true, S1S0B0Token: hatte_eindruck_,, S1S0Token: hatte_eindruck, S1Token: hatte, S1_LastThreeLetters: tte, S1_LastTwoLetters: te, hasRighDep_punct: true, 

81- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[hatte, eindruck]]   B= [,, dass, die ,.. ]

B0Token: ,, B0_LastThreeLetters: ,, B0_LastTwoLetters: ,, S0B0Token: hatte_eindruck_,, S0B1Token: hatte_eindruck_dass, S0B2Token: hatte_eindruck_die, S0Token: hatte_eindruck, 

82- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, dass, die ,.. ]

B0Token: ,, B0_LastThreeLetters: ,, B0_LastTwoLetters: ,, 

83- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [dass, die, spd ,.. ]

B0Token: dass, B0_LastThreeLetters: ass, B0_LastTwoLetters: ss, S0B0Token: ,_dass, S0B1Token: ,_die, S0B2Token: ,_spd, S0Token: ,, S0_LastThreeLetters: ,, S0_LastTwoLetters: ,, 

84- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [dass, die, spd ,.. ]

B0Token: dass, B0_LastThreeLetters: ass, B0_LastTwoLetters: ss, 

85- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [dass]   B= [die, spd, wieder ,.. ]

B0IsInLexic: true, B0Token: die, B0_LastThreeLetters: die, B0_LastTwoLetters: ie, S0B0Token: dass_die, S0B1Token: dass_spd, S0B2Token: dass_wieder, S0Token: dass, S0_LastThreeLetters: ass, S0_LastTwoLetters: ss, dass_isGouvernedBy_punken: true, dass_isGouvernedBy_punken_mark: true, 

86- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [die, spd, wieder ,.. ]

B0IsInLexic: true, B0Token: die, B0_LastThreeLetters: die, B0_LastTwoLetters: ie, 

87- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [die]   B= [spd, wieder, stärker ,.. ]

B0Token: spd, B0_LastThreeLetters: spd, B0_LastTwoLetters: pd, S0B0Token: die_spd, S0B1Token: die_wieder, S0B2Token: die_stärker, S0IsInLexic: true, S0Token: die, S0_LastThreeLetters: die, S0_LastTwoLetters: ie, der_isGouvernedBy_SPD: true, der_isGouvernedBy_SPD_det: true, 

88- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [spd, wieder, stärker ,.. ]

B0Token: spd, B0_LastThreeLetters: spd, B0_LastTwoLetters: pd, 

89- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [spd]   B= [wieder, stärker, punkten ,.. ]

B0Token: wieder, B0_LastThreeLetters: der, B0_LastTwoLetters: er, S0B0Token: spd_wieder, S0B1Token: spd_stärker, S0B2Token: spd_punkten, S0Token: spd, S0_LastThreeLetters: spd, S0_LastTwoLetters: pd, SPD_isGouvernedBy_punken: true, SPD_isGouvernedBy_punken_nsubj: true, 

90- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [wieder, stärker, punkten ,.. ]

B0Token: wieder, B0_LastThreeLetters: der, B0_LastTwoLetters: er, 

91- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [wieder]   B= [stärker, punkten, konnte ,.. ]

B0Token: stärker, B0_LastThreeLetters: ker, B0_LastTwoLetters: er, S0B0Token: wieder_stärker, S0B1Token: wieder_punkten, S0B2Token: wieder_konnte, S0Token: wieder, S0_LastThreeLetters: der, S0_LastTwoLetters: er, wieder_isGouvernedBy_punken: true, wieder_isGouvernedBy_punken_advmod: true, 

92- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [stärker, punkten, konnte ,.. ]

B0Token: stärker, B0_LastThreeLetters: ker, B0_LastTwoLetters: er, 

93- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [stärker]   B= [punkten, konnte, . ,.. ]

B0Token: punkten, B0_LastThreeLetters: ten, B0_LastTwoLetters: en, S0B0Token: stärker_punkten, S0B1Token: stärker_konnte, S0B2Token: stärker_., S0Token: stärker, S0_LastThreeLetters: ker, S0_LastTwoLetters: er, stark_isGouvernedBy_punken: true, stark_isGouvernedBy_punken_xcomp: true, 

94- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [punkten, konnte, . ,.. ]

B0Token: punkten, B0_LastThreeLetters: ten, B0_LastTwoLetters: en, 

95- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [punkten]   B= [konnte, . ,.. ]

B0IsInLexic: true, B0Token: konnte, B0_LastThreeLetters: nte, B0_LastTwoLetters: te, S0B0Token: punkten_konnte, S0B1Token: punkten_., S0Token: punkten, S0_LastThreeLetters: ten, S0_LastTwoLetters: en, hasRighDep_aux: true, punken_hasRighDep_aux: true, punken_können_hasRighDep_aux: true, 

96- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [konnte, . ,.. ]

B0IsInLexic: true, B0Token: konnte, B0_LastThreeLetters: nte, B0_LastTwoLetters: te, 

97- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [konnte]   B= [.]

B0Token: ., B0_LastThreeLetters: ., B0_LastTwoLetters: ., S0B0Token: konnte_., S0IsInLexic: true, S0Token: konnte, S0_LastThreeLetters: nte, S0_LastTwoLetters: te, 

98- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [.]

B0Token: ., B0_LastThreeLetters: ., B0_LastTwoLetters: ., 

99- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [ ]

S0Token: ., S0_LastThreeLetters: ., S0_LastTwoLetters: ., 

100- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

