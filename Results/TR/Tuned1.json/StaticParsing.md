## Sentence No. 1383 - 
" Galatasaray'ın bugün bir adası var . Şu _ andaki konumu ile ne üyeye iyi hizmet veriyor , ne de yönetim yatırımının karşılığını alıyor . Four Seasons Oteller zinciri ile _ anlaşıp , Kuruçeşme Adası'na 60 yataklı lüks bir otel _ yapmayı planlıyoruz . Kalamış Tesisleri'ni ise Sosyal hizmet _ eden bir görev _ yükleyip , _ yüzme şubesinin _ çalışmalarını _ yapmayı _ düşündüğümüz komplike başka bir tesise taşıyacağız . Artık tek seçeneğimiz var ; o da kar _ etmek . Kulübü 14 milyon dolar borçla devir aldık . 1998 yılında bu borcu dört milyon dolara _ indirmeyi hedefliyoruz . 2001 yılında ise hiç borcumuz kalmayacak . Galatasaray Fan Kulüp ve master Card ile _ yaptığımız anlaşmayla _ gerçekleşecek kredi kartı ek gelirlerimizi arttıracak . Bir şirket oluyoruz ve bunu halka _ açarak borsaya da gireceğiz . Markamızın patentini _ alıp , promosyonlarımızı pazarlayacağız . Amerika'da _ anlaştığımız bir dizayn şirketi bize yılda üç ayrı forma hazırlayacak . Taraftarlarımıza bunları vereceğiz . Çok büyük gelirlerin kapısını açıyoruz " . 
### Existing MWEs: 
1- **hizmet veriyor** (OTH)
2- **kar etmek** (LVC)
3- **devir aldık** (ID)



0- &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [", Galatasaray'ın, bugün ,.. ]

B0Lemma: ", B0POS: Punc, B0Token: ", B1Lemma: Galatasaray, B1POS: Noun, B1Token: Galatasaray'ın, 

1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= ["]   B= [Galatasaray'ın, bugün, bir ,.. ]

B0Lemma: Galatasaray, B0POS: Noun, B0Token: Galatasaray'ın, B1Lemma: bugün, B1POS: Adverb, B1Token: bugün, S0B0Distance: 1, S0B0Lemma: "_Galatasaray, S0B0LemmaPOS: "_Noun, S0B0POS: Punc_Noun, S0B0POSLemma: Punc_Galatasaray, S0B0Token: "_Galatasaray'ın, S0B1Lemma: "_bugün, S0B1LemmaPOS: "_Adverb, S0B1POS: Punc_Adverb, S0B1POSLemma: Punc_bugün, S0B1Token: "_bugün, S0Lemma: ", S0POS: Punc, S0Token: ", 

2- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Galatasaray'ın, bugün, bir ,.. ]

B0Lemma: Galatasaray, B0POS: Noun, B0Token: Galatasaray'ın, B1Lemma: bugün, B1POS: Adverb, B1Token: bugün, transitionHistoryLength1: 0, 

3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Galatasaray'ın]   B= [bugün, bir, adası ,.. ]

B0Lemma: bugün, B0POS: Adverb, B0Token: bugün, B1Lemma: bir, B1POS: Adj, B1Token: bir, Galatasaray_isGouvernedBy_ada: true, Galatasaray_isGouvernedBy_ada_POSSESSOR: true, S0B0Distance: 1, S0B0Lemma: Galatasaray_bugün, S0B0LemmaPOS: Galatasaray_Adverb, S0B0POS: Noun_Adverb, S0B0POSLemma: Noun_bugün, S0B0Token: Galatasaray'ın_bugün, S0B1Lemma: Galatasaray_bir, S0B1LemmaPOS: Galatasaray_Adj, S0B1POS: Noun_Adj, S0B1POSLemma: Noun_bir, S0B1Token: Galatasaray'ın_bir, S0Lemma: Galatasaray, S0POS: Noun, S0Token: Galatasaray'ın, transitionHistoryLength1: 2, transitionHistoryLength2: 20, 

4- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [bugün, bir, adası ,.. ]

B0Lemma: bugün, B0POS: Adverb, B0Token: bugün, B1Lemma: bir, B1POS: Adj, B1Token: bir, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [bugün]   B= [bir, adası, var ,.. ]

B0Lemma: bir, B0POS: Adj, B0Token: bir, B1Lemma: ada, B1POS: Noun, B1Token: adası, S0B0Distance: 1, S0B0Lemma: bugün_bir, S0B0LemmaPOS: bugün_Adj, S0B0POS: Adverb_Adj, S0B0POSLemma: Adverb_bir, S0B0Token: bugün_bir, S0B1Lemma: bugün_ada, S0B1LemmaPOS: bugün_Noun, S0B1POS: Adverb_Noun, S0B1POSLemma: Adverb_ada, S0B1Token: bugün_adası, S0Lemma: bugün, S0POS: Adverb, S0Token: bugün, bugün_isGouvernedBy_ada: true, bugün_isGouvernedBy_ada_MODIFIER: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

6- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [bir, adası, var ,.. ]

B0Lemma: bir, B0POS: Adj, B0Token: bir, B1Lemma: ada, B1POS: Noun, B1Token: adası, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [bir]   B= [adası, var, . ,.. ]

B0Lemma: ada, B0POS: Noun, B0Token: adası, B1Lemma: var, B1POS: Adj, B1Token: var, S0B0Distance: 1, S0B0Lemma: bir_ada, S0B0LemmaPOS: bir_Noun, S0B0POS: Adj_Noun, S0B0POSLemma: Adj_ada, S0B0Token: bir_adası, S0B1Lemma: bir_var, S0B1LemmaPOS: bir_Adj, S0B1POS: Adj_Adj, S0B1POSLemma: Adj_var, S0B1Token: bir_var, S0Lemma: bir, S0POS: Adj, S0Token: bir, bir_isGouvernedBy_ada: true, bir_isGouvernedBy_ada_DETERMINER: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

8- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [adası, var, . ,.. ]

B0Lemma: ada, B0POS: Noun, B0Token: adası, B1Lemma: var, B1POS: Adj, B1Token: var, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [adası]   B= [var, ., Şu ,.. ]

B0Lemma: var, B0POS: Adj, B0Token: var, B1Lemma: ., B1POS: Punc, B1Token: ., S0B0Distance: 1, S0B0Lemma: ada_var, S0B0LemmaPOS: ada_Adj, S0B0POS: Noun_Adj, S0B0POSLemma: Noun_var, S0B0Token: adası_var, S0B1Lemma: ada_., S0B1LemmaPOS: ada_Punc, S0B1POS: Noun_Punc, S0B1POSLemma: Noun_., S0B1Token: adası_., S0Lemma: ada, S0POS: Noun, S0Token: adası, ada_isGouvernedBy_var: true, ada_isGouvernedBy_var_SUBJECT: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

10- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [var, ., Şu ,.. ]

B0Lemma: var, B0POS: Adj, B0Token: var, B1Lemma: ., B1POS: Punc, B1Token: ., transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [var]   B= [., Şu, _ ,.. ]

B0Lemma: ., B0POS: Punc, B0Token: ., B1Lemma: şu, B1POS: Det, B1Token: Şu, S0B0Distance: 1, S0B0Lemma: var_., S0B0LemmaPOS: var_Punc, S0B0POS: Adj_Punc, S0B0POSLemma: Adj_., S0B0Token: var_., S0B1Lemma: var_şu, S0B1LemmaPOS: var_Det, S0B1POS: Adj_Det, S0B1POSLemma: Adj_şu, S0B1Token: var_Şu, S0Lemma: var, S0POS: Adj, S0Token: var, hasRighDep_PUNCTUATION: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, var_._hasRighDep_PUNCTUATION: true, var_hasRighDep_PUNCTUATION: true, var_isGouvernedBy_ver: true, var_isGouvernedBy_ver_COORDINATION: true, 

12- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [., Şu, _ ,.. ]

B0Lemma: ., B0POS: Punc, B0Token: ., B1Lemma: şu, B1POS: Det, B1Token: Şu, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [Şu, _, andaki ,.. ]

B0Lemma: şu, B0POS: Det, B0Token: Şu, B1Lemma: an, B1POS: Noun, B1Token: _, S0B0Distance: 1, S0B0Lemma: ._şu, S0B0LemmaPOS: ._Det, S0B0POS: Punc_Det, S0B0POSLemma: Punc_şu, S0B0Token: ._Şu, S0B1Lemma: ._an, S0B1LemmaPOS: ._Noun, S0B1POS: Punc_Noun, S0B1POSLemma: Punc_an, S0B1Token: .__, S0Lemma: ., S0POS: Punc, S0Token: ., transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

14- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Şu, _, andaki ,.. ]

B0Lemma: şu, B0POS: Det, B0Token: Şu, B1Lemma: an, B1POS: Noun, B1Token: _, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Şu]   B= [_, andaki, konumu ,.. ]

B0Lemma: an, B0POS: Noun, B0Token: _, B1Lemma: _, B1POS: Adj, B1Token: andaki, S0B0Distance: 1, S0B0Lemma: şu_an, S0B0LemmaPOS: şu_Noun, S0B0POS: Det_Noun, S0B0POSLemma: Det_an, S0B0Token: Şu__, S0B1Lemma: şu__, S0B1LemmaPOS: şu_Adj, S0B1POS: Det_Adj, S0B1POSLemma: Det__, S0B1Token: Şu_andaki, S0Lemma: şu, S0POS: Det, S0Token: Şu, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, şu_isGouvernedBy_an: true, şu_isGouvernedBy_an_DETERMINER: true, 

16- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [_, andaki, konumu ,.. ]

B0Lemma: an, B0POS: Noun, B0Token: _, B1Lemma: _, B1POS: Adj, B1Token: andaki, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [_]   B= [andaki, konumu, ile ,.. ]

B0Lemma: _, B0POS: Adj, B0Token: andaki, B1Lemma: konum, B1POS: Noun, B1Token: konumu, S0B0Distance: 1, S0B0Lemma: an__, S0B0LemmaPOS: an_Adj, S0B0POS: Noun_Adj, S0B0POSLemma: Noun__, S0B0Token: __andaki, S0B1Lemma: an_konum, S0B1LemmaPOS: an_Noun, S0B1POS: Noun_Noun, S0B1POSLemma: Noun_konum, S0B1Token: __konumu, S0Lemma: an, S0POS: Noun, S0Token: _, an_isGouvernedBy__: true, an_isGouvernedBy___DERIV: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

18- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [andaki, konumu, ile ,.. ]

B0Lemma: _, B0POS: Adj, B0Token: andaki, B1Lemma: konum, B1POS: Noun, B1Token: konumu, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [andaki]   B= [konumu, ile, ne ,.. ]

B0Lemma: konum, B0POS: Noun, B0Token: konumu, B1Lemma: ile, B1POS: Conj, B1Token: ile, S0B0Distance: 1, S0B0Lemma: __konum, S0B0LemmaPOS: __Noun, S0B0POS: Adj_Noun, S0B0POSLemma: Adj_konum, S0B0Token: andaki_konumu, S0B1Lemma: __ile, S0B1LemmaPOS: __Conj, S0B1POS: Adj_Conj, S0B1POSLemma: Adj_ile, S0B1Token: andaki_ile, S0Lemma: _, S0POS: Adj, S0Token: andaki, __isGouvernedBy_konum: true, __isGouvernedBy_konum_MODIFIER: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

20- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [konumu, ile, ne ,.. ]

B0Lemma: konum, B0POS: Noun, B0Token: konumu, B1Lemma: ile, B1POS: Conj, B1Token: ile, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [konumu]   B= [ile, ne, üyeye ,.. ]

B0Lemma: ile, B0POS: Conj, B0Token: ile, B1Lemma: ne, B1POS: Pron, B1Token: ne, S0B0Distance: 1, S0B0Lemma: konum_ile, S0B0LemmaPOS: konum_Conj, S0B0POS: Noun_Conj, S0B0POSLemma: Noun_ile, S0B0Token: konumu_ile, S0B1Lemma: konum_ne, S0B1LemmaPOS: konum_Pron, S0B1POS: Noun_Pron, S0B1POSLemma: Noun_ne, S0B1Token: konumu_ne, S0Lemma: konum, S0POS: Noun, S0Token: konumu, hasRighDep_CONJUNCTION: true, konum_hasRighDep_CONJUNCTION: true, konum_ile_hasRighDep_CONJUNCTION: true, konum_isGouvernedBy_üye: true, konum_isGouvernedBy_üye_COORDINATION: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

22- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ile, ne, üyeye ,.. ]

B0Lemma: ile, B0POS: Conj, B0Token: ile, B1Lemma: ne, B1POS: Pron, B1Token: ne, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

23- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ile]   B= [ne, üyeye, iyi ,.. ]

B0Lemma: ne, B0POS: Pron, B0Token: ne, B1Lemma: üye, B1POS: Noun, B1Token: üyeye, S0B0Distance: 1, S0B0Lemma: ile_ne, S0B0LemmaPOS: ile_Pron, S0B0POS: Conj_Pron, S0B0POSLemma: Conj_ne, S0B0Token: ile_ne, S0B1Lemma: ile_üye, S0B1LemmaPOS: ile_Noun, S0B1POS: Conj_Noun, S0B1POSLemma: Conj_üye, S0B1Token: ile_üyeye, S0Lemma: ile, S0POS: Conj, S0Token: ile, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

24- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ne, üyeye, iyi ,.. ]

B0Lemma: ne, B0POS: Pron, B0Token: ne, B1Lemma: üye, B1POS: Noun, B1Token: üyeye, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

25- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ne]   B= [üyeye, iyi, hizmet ,.. ]

B0Lemma: üye, B0POS: Noun, B0Token: üyeye, B1Lemma: iyi, B1POS: Adj, B1Token: iyi, S0B0Distance: 1, S0B0Lemma: ne_üye, S0B0LemmaPOS: ne_Noun, S0B0POS: Pron_Noun, S0B0POSLemma: Pron_üye, S0B0Token: ne_üyeye, S0B1Lemma: ne_iyi, S0B1LemmaPOS: ne_Adj, S0B1POS: Pron_Adj, S0B1POSLemma: Pron_iyi, S0B1Token: ne_iyi, S0Lemma: ne, S0POS: Pron, S0Token: ne, ne_isGouvernedBy_üye: true, ne_isGouvernedBy_üye_MODIFIER: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

26- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [üyeye, iyi, hizmet ,.. ]

B0Lemma: üye, B0POS: Noun, B0Token: üyeye, B1Lemma: iyi, B1POS: Adj, B1Token: iyi, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

27- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [üyeye]   B= [iyi, hizmet, veriyor ,.. ]

B0Lemma: iyi, B0POS: Adj, B0Token: iyi, B1Lemma: hizmet, B1POS: Noun, B1Token: hizmet, S0B0Distance: 1, S0B0Lemma: üye_iyi, S0B0LemmaPOS: üye_Adj, S0B0POS: Noun_Adj, S0B0POSLemma: Noun_iyi, S0B0Token: üyeye_iyi, S0B1Lemma: üye_hizmet, S0B1LemmaPOS: üye_Noun, S0B1POS: Noun_Noun, S0B1POSLemma: Noun_hizmet, S0B1Token: üyeye_hizmet, S0Lemma: üye, S0POS: Noun, S0Token: üyeye, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, üye_isGouvernedBy_ver: true, üye_isGouvernedBy_ver_MODIFIER: true, 

28- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [iyi, hizmet, veriyor ,.. ]

B0Lemma: iyi, B0POS: Adj, B0Token: iyi, B1Lemma: hizmet, B1POS: Noun, B1Token: hizmet, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

29- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [iyi]   B= [hizmet, veriyor, , ,.. ]

B0Lemma: hizmet, B0POS: Noun, B0Token: hizmet, B1Lemma: ver, B1POS: Verb, B1Token: veriyor, S0B0Distance: 1, S0B0Lemma: iyi_hizmet, S0B0LemmaPOS: iyi_Noun, S0B0POS: Adj_Noun, S0B0POSLemma: Adj_hizmet, S0B0Token: iyi_hizmet, S0B1Lemma: iyi_ver, S0B1LemmaPOS: iyi_Verb, S0B1POS: Adj_Verb, S0B1POSLemma: Adj_ver, S0B1Token: iyi_veriyor, S0Lemma: iyi, S0POS: Adj, S0Token: iyi, iyi_isGouvernedBy_hizmet: true, iyi_isGouvernedBy_hizmet_MODIFIER: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

30- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [hizmet, veriyor, , ,.. ]

B0Lemma: hizmet, B0POS: Noun, B0Token: hizmet, B1Lemma: ver, B1POS: Verb, B1Token: veriyor, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

31- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [hizmet]   B= [veriyor, ,, ne ,.. ]

B0Lemma: ver, B0POS: Verb, B0Token: veriyor, B1Lemma: ,, B1POS: Punc, B1Token: ,, S0B0Distance: 1, S0B0Lemma: hizmet_ver, S0B0LemmaPOS: hizmet_Verb, S0B0POS: Noun_Verb, S0B0POSLemma: Noun_ver, S0B0Token: hizmet_veriyor, S0B1Lemma: hizmet_,, S0B1LemmaPOS: hizmet_Punc, S0B1POS: Noun_Punc, S0B1POSLemma: Noun_,, S0B1Token: hizmet_,, S0Lemma: hizmet, S0POS: Noun, S0Token: hizmet, hizmet_isGouvernedBy_ver: true, hizmet_isGouvernedBy_ver_OBJECT: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

32- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [hizmet, veriyor]   B= [,, ne, de ,.. ]

B0Lemma: ,, B0POS: Punc, B0Token: ,, B1Lemma: ne, B1POS: Conj, B1Token: ne, S0B0Distance: 1, S0B0Lemma: ver_,, S0B0LemmaPOS: ver_Punc, S0B0POS: Verb_Punc, S0B0POSLemma: Verb_,, S0B0Token: veriyor_,, S0B1Lemma: ver_ne, S0B1LemmaPOS: ver_Conj, S0B1POS: Verb_Conj, S0B1POSLemma: Verb_ne, S0B1Token: veriyor_ne, S0Lemma: ver, S0POS: Verb, S0Token: veriyor, S1B0Lemma: hizmet_,, S1B0LemmaPOS: hizmet_Punc, S1B0POS: Noun_Punc, S1B0POSLemma: Noun_,, S1B0Token: hizmet_,, S1Lemma: hizmet, S1POS: Noun, S1S0Lemma: hizmet_ver, S1S0LemmaPOS: hizmet_Verb, S1S0POS: Noun_Verb, S1S0POSLemma: Noun_ver, S1S0Token: hizmet_veriyor, S1Token: hizmet, SyntaxicRelation: -OBJECT, hasRighDep_CONJUNCTION: true, hasRighDep_PUNCTUATION: true, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, ver_,_hasRighDep_PUNCTUATION: true, ver_hasRighDep_CONJUNCTION: true, ver_hasRighDep_PUNCTUATION: true, ver_isGouvernedBy_al: true, ver_isGouvernedBy_al_COORDINATION: true, ver_ne_hasRighDep_CONJUNCTION: true, 

33- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[hizmet, veriyor]]   B= [,, ne, de ,.. ]

B0Lemma: ,, B0POS: Punc, B0Token: ,, B1Lemma: ne, B1POS: Conj, B1Token: ne, S0B0Distance: 1, S0B0Lemma: hizmet_ver_,, S0B0LemmaPOS: hizmet_ver_Punc, S0B0POS: Noun_Verb_Punc, S0B0POSLemma: Noun_Verb_,, S0B0Token: hizmet_veriyor_,, S0B1Lemma: hizmet_ver_ne, S0B1LemmaPOS: hizmet_ver_Conj, S0B1POS: Noun_Verb_Conj, S0B1POSLemma: Noun_Verb_ne, S0B1Token: hizmet_veriyor_ne, S0Lemma: hizmet_ver, S0POS: Noun_Verb, S0Token: hizmet_veriyor, transitionHistoryLength1: 0, transitionHistoryLength2: 00, transitionHistoryLength3: 002, 

34- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, ne, de ,.. ]

B0Lemma: ,, B0POS: Punc, B0Token: ,, B1Lemma: ne, B1POS: Conj, B1Token: ne, transitionHistoryLength1: 1, transitionHistoryLength2: 10, transitionHistoryLength3: 100, 

35- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [ne, de, yönetim ,.. ]

B0Lemma: ne, B0POS: Conj, B0Token: ne, B1Lemma: de, B1POS: Conj, B1Token: de, S0B0Distance: 1, S0B0Lemma: ,_ne, S0B0LemmaPOS: ,_Conj, S0B0POS: Punc_Conj, S0B0POSLemma: Punc_ne, S0B0Token: ,_ne, S0B1Lemma: ,_de, S0B1LemmaPOS: ,_Conj, S0B1POS: Punc_Conj, S0B1POSLemma: Punc_de, S0B1Token: ,_de, S0Lemma: ,, S0POS: Punc, S0Token: ,, transitionHistoryLength1: 2, transitionHistoryLength2: 21, transitionHistoryLength3: 210, 

36- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ne, de, yönetim ,.. ]

B0Lemma: ne, B0POS: Conj, B0Token: ne, B1Lemma: de, B1POS: Conj, B1Token: de, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 021, 

37- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ne]   B= [de, yönetim, yatırımının ,.. ]

B0Lemma: de, B0POS: Conj, B0Token: de, B1Lemma: yönetim, B1POS: Noun, B1Token: yönetim, S0B0Distance: 1, S0B0Lemma: ne_de, S0B0LemmaPOS: ne_Conj, S0B0POS: Conj_Conj, S0B0POSLemma: Conj_de, S0B0Token: ne_de, S0B1Lemma: ne_yönetim, S0B1LemmaPOS: ne_Noun, S0B1POS: Conj_Noun, S0B1POSLemma: Conj_yönetim, S0B1Token: ne_yönetim, S0Lemma: ne, S0POS: Conj, S0Token: ne, hasRighDep_INTENSIFIER: true, ne_de_hasRighDep_INTENSIFIER: true, ne_hasRighDep_INTENSIFIER: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

38- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [de, yönetim, yatırımının ,.. ]

B0Lemma: de, B0POS: Conj, B0Token: de, B1Lemma: yönetim, B1POS: Noun, B1Token: yönetim, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

39- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [de]   B= [yönetim, yatırımının, karşılığını ,.. ]

B0Lemma: yönetim, B0POS: Noun, B0Token: yönetim, B1Lemma: yatırım, B1POS: Noun, B1Token: yatırımının, S0B0Distance: 1, S0B0Lemma: de_yönetim, S0B0LemmaPOS: de_Noun, S0B0POS: Conj_Noun, S0B0POSLemma: Conj_yönetim, S0B0Token: de_yönetim, S0B1Lemma: de_yatırım, S0B1LemmaPOS: de_Noun, S0B1POS: Conj_Noun, S0B1POSLemma: Conj_yatırım, S0B1Token: de_yatırımının, S0Lemma: de, S0POS: Conj, S0Token: de, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

40- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [yönetim, yatırımının, karşılığını ,.. ]

B0Lemma: yönetim, B0POS: Noun, B0Token: yönetim, B1Lemma: yatırım, B1POS: Noun, B1Token: yatırımının, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

41- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [yönetim]   B= [yatırımının, karşılığını, alıyor ,.. ]

B0Lemma: yatırım, B0POS: Noun, B0Token: yatırımının, B1Lemma: karşılık, B1POS: Noun, B1Token: karşılığını, S0B0Distance: 1, S0B0Lemma: yönetim_yatırım, S0B0LemmaPOS: yönetim_Noun, S0B0POS: Noun_Noun, S0B0POSLemma: Noun_yatırım, S0B0Token: yönetim_yatırımının, S0B1Lemma: yönetim_karşılık, S0B1LemmaPOS: yönetim_Noun, S0B1POS: Noun_Noun, S0B1POSLemma: Noun_karşılık, S0B1Token: yönetim_karşılığını, S0Lemma: yönetim, S0POS: Noun, S0Token: yönetim, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, yönetim_isGouvernedBy_yatırım: true, yönetim_isGouvernedBy_yatırım_POSSESSOR: true, 

42- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [yatırımının, karşılığını, alıyor ,.. ]

B0Lemma: yatırım, B0POS: Noun, B0Token: yatırımının, B1Lemma: karşılık, B1POS: Noun, B1Token: karşılığını, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

43- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [yatırımının]   B= [karşılığını, alıyor, . ,.. ]

B0Lemma: karşılık, B0POS: Noun, B0Token: karşılığını, B1Lemma: al, B1POS: Verb, B1Token: alıyor, S0B0Distance: 1, S0B0Lemma: yatırım_karşılık, S0B0LemmaPOS: yatırım_Noun, S0B0POS: Noun_Noun, S0B0POSLemma: Noun_karşılık, S0B0Token: yatırımının_karşılığını, S0B1Lemma: yatırım_al, S0B1LemmaPOS: yatırım_Verb, S0B1POS: Noun_Verb, S0B1POSLemma: Noun_al, S0B1Token: yatırımının_alıyor, S0Lemma: yatırım, S0POS: Noun, S0Token: yatırımının, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, yatırım_isGouvernedBy_karşılık: true, yatırım_isGouvernedBy_karşılık_POSSESSOR: true, 

44- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [karşılığını, alıyor, . ,.. ]

B0Lemma: karşılık, B0POS: Noun, B0Token: karşılığını, B1Lemma: al, B1POS: Verb, B1Token: alıyor, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

45- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [karşılığını]   B= [alıyor, ., Four ,.. ]

B0Lemma: al, B0POS: Verb, B0Token: alıyor, B1Lemma: ., B1POS: Punc, B1Token: ., S0B0Distance: 1, S0B0Lemma: karşılık_al, S0B0LemmaPOS: karşılık_Verb, S0B0POS: Noun_Verb, S0B0POSLemma: Noun_al, S0B0Token: karşılığını_alıyor, S0B1Lemma: karşılık_., S0B1LemmaPOS: karşılık_Punc, S0B1POS: Noun_Punc, S0B1POSLemma: Noun_., S0B1Token: karşılığını_., S0Lemma: karşılık, S0POS: Noun, S0Token: karşılığını, karşılık_isGouvernedBy_al: true, karşılık_isGouvernedBy_al_OBJECT: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

46- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [alıyor, ., Four ,.. ]

B0Lemma: al, B0POS: Verb, B0Token: alıyor, B1Lemma: ., B1POS: Punc, B1Token: ., transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

47- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [alıyor]   B= [., Four, Seasons ,.. ]

B0Lemma: ., B0POS: Punc, B0Token: ., B1Lemma: Four, B1POS: Noun, B1Token: Four, S0B0Distance: 1, S0B0Lemma: al_., S0B0LemmaPOS: al_Punc, S0B0POS: Verb_Punc, S0B0POSLemma: Verb_., S0B0Token: alıyor_., S0B1Lemma: al_Four, S0B1LemmaPOS: al_Noun, S0B1POS: Verb_Noun, S0B1POSLemma: Verb_Four, S0B1Token: alıyor_Four, S0Lemma: al, S0POS: Verb, S0Token: alıyor, al_._hasRighDep_PUNCTUATION: true, al_hasRighDep_PUNCTUATION: true, al_isGouvernedBy_planla: true, al_isGouvernedBy_planla_COORDINATION: true, hasRighDep_PUNCTUATION: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

48- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [., Four, Seasons ,.. ]

B0Lemma: ., B0POS: Punc, B0Token: ., B1Lemma: Four, B1POS: Noun, B1Token: Four, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

49- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [Four, Seasons, Oteller ,.. ]

B0Lemma: Four, B0POS: Noun, B0Token: Four, B1Lemma: Seasons, B1POS: Noun, B1Token: Seasons, S0B0Distance: 1, S0B0Lemma: ._Four, S0B0LemmaPOS: ._Noun, S0B0POS: Punc_Noun, S0B0POSLemma: Punc_Four, S0B0Token: ._Four, S0B1Lemma: ._Seasons, S0B1LemmaPOS: ._Noun, S0B1POS: Punc_Noun, S0B1POSLemma: Punc_Seasons, S0B1Token: ._Seasons, S0Lemma: ., S0POS: Punc, S0Token: ., transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

50- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Four, Seasons, Oteller ,.. ]

B0Lemma: Four, B0POS: Noun, B0Token: Four, B1Lemma: Seasons, B1POS: Noun, B1Token: Seasons, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

51- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Four]   B= [Seasons, Oteller, zinciri ,.. ]

B0Lemma: Seasons, B0POS: Noun, B0Token: Seasons, B1Lemma: otel, B1POS: Noun, B1Token: Oteller, Four_isGouvernedBy_Seasons: true, Four_isGouvernedBy_Seasons_MWE: true, S0B0Distance: 1, S0B0Lemma: Four_Seasons, S0B0LemmaPOS: Four_Noun, S0B0POS: Noun_Noun, S0B0POSLemma: Noun_Seasons, S0B0Token: Four_Seasons, S0B1Lemma: Four_otel, S0B1LemmaPOS: Four_Noun, S0B1POS: Noun_Noun, S0B1POSLemma: Noun_otel, S0B1Token: Four_Oteller, S0Lemma: Four, S0POS: Noun, S0Token: Four, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

52- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Seasons, Oteller, zinciri ,.. ]

B0Lemma: Seasons, B0POS: Noun, B0Token: Seasons, B1Lemma: otel, B1POS: Noun, B1Token: Oteller, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

53- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Seasons]   B= [Oteller, zinciri, ile ,.. ]

B0Lemma: otel, B0POS: Noun, B0Token: Oteller, B1Lemma: zincir, B1POS: Noun, B1Token: zinciri, S0B0Distance: 1, S0B0Lemma: Seasons_otel, S0B0LemmaPOS: Seasons_Noun, S0B0POS: Noun_Noun, S0B0POSLemma: Noun_otel, S0B0Token: Seasons_Oteller, S0B1Lemma: Seasons_zincir, S0B1LemmaPOS: Seasons_Noun, S0B1POS: Noun_Noun, S0B1POSLemma: Noun_zincir, S0B1Token: Seasons_zinciri, S0Lemma: Seasons, S0POS: Noun, S0Token: Seasons, Seasons_isGouvernedBy_planla: true, Seasons_isGouvernedBy_planla_SUBJECT: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

54- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Oteller, zinciri, ile ,.. ]

B0Lemma: otel, B0POS: Noun, B0Token: Oteller, B1Lemma: zincir, B1POS: Noun, B1Token: zinciri, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

55- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Oteller]   B= [zinciri, ile, _ ,.. ]

B0Lemma: zincir, B0POS: Noun, B0Token: zinciri, B1Lemma: ile, B1POS: Conj, B1Token: ile, S0B0Distance: 1, S0B0Lemma: otel_zincir, S0B0LemmaPOS: otel_Noun, S0B0POS: Noun_Noun, S0B0POSLemma: Noun_zincir, S0B0Token: Oteller_zinciri, S0B1Lemma: otel_ile, S0B1LemmaPOS: otel_Conj, S0B1POS: Noun_Conj, S0B1POSLemma: Noun_ile, S0B1Token: Oteller_ile, S0Lemma: otel, S0POS: Noun, S0Token: Oteller, otel_isGouvernedBy_zincir: true, otel_isGouvernedBy_zincir_POSSESSOR: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

56- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [zinciri, ile, _ ,.. ]

B0Lemma: zincir, B0POS: Noun, B0Token: zinciri, B1Lemma: ile, B1POS: Conj, B1Token: ile, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

57- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [zinciri]   B= [ile, _, anlaşıp ,.. ]

B0Lemma: ile, B0POS: Conj, B0Token: ile, B1Lemma: anlaş, B1POS: Verb, B1Token: _, S0B0Distance: 1, S0B0Lemma: zincir_ile, S0B0LemmaPOS: zincir_Conj, S0B0POS: Noun_Conj, S0B0POSLemma: Noun_ile, S0B0Token: zinciri_ile, S0B1Lemma: zincir_anlaş, S0B1LemmaPOS: zincir_Verb, S0B1POS: Noun_Verb, S0B1POSLemma: Noun_anlaş, S0B1Token: zinciri__, S0Lemma: zincir, S0POS: Noun, S0Token: zinciri, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, zincir_isGouvernedBy_ile: true, zincir_isGouvernedBy_ile_ARGUMENT: true, 

58- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ile, _, anlaşıp ,.. ]

B0Lemma: ile, B0POS: Conj, B0Token: ile, B1Lemma: anlaş, B1POS: Verb, B1Token: _, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

59- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ile]   B= [_, anlaşıp, , ,.. ]

B0Lemma: anlaş, B0POS: Verb, B0Token: _, B1Lemma: _, B1POS: Adverb, B1Token: anlaşıp, S0B0Distance: 1, S0B0Lemma: ile_anlaş, S0B0LemmaPOS: ile_Verb, S0B0POS: Conj_Verb, S0B0POSLemma: Conj_anlaş, S0B0Token: ile__, S0B1Lemma: ile__, S0B1LemmaPOS: ile_Adverb, S0B1POS: Conj_Adverb, S0B1POSLemma: Conj__, S0B1Token: ile_anlaşıp, S0Lemma: ile, S0POS: Conj, S0Token: ile, ile_isGouvernedBy_anlaş: true, ile_isGouvernedBy_anlaş_MODIFIER: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

60- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [_, anlaşıp, , ,.. ]

B0Lemma: anlaş, B0POS: Verb, B0Token: _, B1Lemma: _, B1POS: Adverb, B1Token: anlaşıp, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

61- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [_]   B= [anlaşıp, ,, Kuruçeşme ,.. ]

B0Lemma: _, B0POS: Adverb, B0Token: anlaşıp, B1Lemma: ,, B1POS: Punc, B1Token: ,, S0B0Distance: 1, S0B0Lemma: anlaş__, S0B0LemmaPOS: anlaş_Adverb, S0B0POS: Verb_Adverb, S0B0POSLemma: Verb__, S0B0Token: __anlaşıp, S0B1Lemma: anlaş_,, S0B1LemmaPOS: anlaş_Punc, S0B1POS: Verb_Punc, S0B1POSLemma: Verb_,, S0B1Token: __,, S0Lemma: anlaş, S0POS: Verb, S0Token: _, anlaş_isGouvernedBy__: true, anlaş_isGouvernedBy___DERIV: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

62- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [anlaşıp, ,, Kuruçeşme ,.. ]

B0Lemma: _, B0POS: Adverb, B0Token: anlaşıp, B1Lemma: ,, B1POS: Punc, B1Token: ,, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

63- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [anlaşıp]   B= [,, Kuruçeşme, Adası'na ,.. ]

B0Lemma: ,, B0POS: Punc, B0Token: ,, B1Lemma: Kuruçeşme, B1POS: Noun, B1Token: Kuruçeşme, S0B0Distance: 1, S0B0Lemma: __,, S0B0LemmaPOS: __Punc, S0B0POS: Adverb_Punc, S0B0POSLemma: Adverb_,, S0B0Token: anlaşıp_,, S0B1Lemma: __Kuruçeşme, S0B1LemmaPOS: __Noun, S0B1POS: Adverb_Noun, S0B1POSLemma: Adverb_Kuruçeşme, S0B1Token: anlaşıp_Kuruçeşme, S0Lemma: _, S0POS: Adverb, S0Token: anlaşıp, __,_hasRighDep_PUNCTUATION: true, __hasRighDep_PUNCTUATION: true, __isGouvernedBy_planla: true, __isGouvernedBy_planla_MODIFIER: true, hasRighDep_PUNCTUATION: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

64- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, Kuruçeşme, Adası'na ,.. ]

B0Lemma: ,, B0POS: Punc, B0Token: ,, B1Lemma: Kuruçeşme, B1POS: Noun, B1Token: Kuruçeşme, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

65- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [Kuruçeşme, Adası'na, 60 ,.. ]

B0Lemma: Kuruçeşme, B0POS: Noun, B0Token: Kuruçeşme, B1Lemma: ada, B1POS: Noun, B1Token: Adası'na, S0B0Distance: 1, S0B0Lemma: ,_Kuruçeşme, S0B0LemmaPOS: ,_Noun, S0B0POS: Punc_Noun, S0B0POSLemma: Punc_Kuruçeşme, S0B0Token: ,_Kuruçeşme, S0B1Lemma: ,_ada, S0B1LemmaPOS: ,_Noun, S0B1POS: Punc_Noun, S0B1POSLemma: Punc_ada, S0B1Token: ,_Adası'na, S0Lemma: ,, S0POS: Punc, S0Token: ,, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

66- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Kuruçeşme, Adası'na, 60 ,.. ]

B0Lemma: Kuruçeşme, B0POS: Noun, B0Token: Kuruçeşme, B1Lemma: ada, B1POS: Noun, B1Token: Adası'na, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

67- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Kuruçeşme]   B= [Adası'na, 60, yataklı ,.. ]

B0Lemma: ada, B0POS: Noun, B0Token: Adası'na, B1Lemma: 60, B1POS: Adj, B1Token: 60, Kuruçeşme_isGouvernedBy_ada: true, Kuruçeşme_isGouvernedBy_ada_MWE: true, S0B0Distance: 1, S0B0Lemma: Kuruçeşme_ada, S0B0LemmaPOS: Kuruçeşme_Noun, S0B0POS: Noun_Noun, S0B0POSLemma: Noun_ada, S0B0Token: Kuruçeşme_Adası'na, S0B1Lemma: Kuruçeşme_60, S0B1LemmaPOS: Kuruçeşme_Adj, S0B1POS: Noun_Adj, S0B1POSLemma: Noun_60, S0B1Token: Kuruçeşme_60, S0Lemma: Kuruçeşme, S0POS: Noun, S0Token: Kuruçeşme, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

68- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Adası'na, 60, yataklı ,.. ]

B0Lemma: ada, B0POS: Noun, B0Token: Adası'na, B1Lemma: 60, B1POS: Adj, B1Token: 60, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

69- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Adası'na]   B= [60, yataklı, lüks ,.. ]

B0Lemma: 60, B0POS: Adj, B0Token: 60, B1Lemma: yataklı, B1POS: Adj, B1Token: yataklı, S0B0Distance: 1, S0B0Lemma: ada_60, S0B0LemmaPOS: ada_Adj, S0B0POS: Noun_Adj, S0B0POSLemma: Noun_60, S0B0Token: Adası'na_60, S0B1Lemma: ada_yataklı, S0B1LemmaPOS: ada_Adj, S0B1POS: Noun_Adj, S0B1POSLemma: Noun_yataklı, S0B1Token: Adası'na_yataklı, S0Lemma: ada, S0POS: Noun, S0Token: Adası'na, ada_isGouvernedBy_yap: true, ada_isGouvernedBy_yap_MODIFIER: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

70- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [60, yataklı, lüks ,.. ]

B0Lemma: 60, B0POS: Adj, B0Token: 60, B1Lemma: yataklı, B1POS: Adj, B1Token: yataklı, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

71- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [60]   B= [yataklı, lüks, bir ,.. ]

60_isGouvernedBy_yataklı: true, 60_isGouvernedBy_yataklı_MODIFIER: true, B0Lemma: yataklı, B0POS: Adj, B0Token: yataklı, B1Lemma: lüks, B1POS: Adj, B1Token: lüks, S0B0Distance: 1, S0B0Lemma: 60_yataklı, S0B0LemmaPOS: 60_Adj, S0B0POS: Adj_Adj, S0B0POSLemma: Adj_yataklı, S0B0Token: 60_yataklı, S0B1Lemma: 60_lüks, S0B1LemmaPOS: 60_Adj, S0B1POS: Adj_Adj, S0B1POSLemma: Adj_lüks, S0B1Token: 60_lüks, S0Lemma: 60, S0POS: Adj, S0Token: 60, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

72- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [yataklı, lüks, bir ,.. ]

B0Lemma: yataklı, B0POS: Adj, B0Token: yataklı, B1Lemma: lüks, B1POS: Adj, B1Token: lüks, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

73- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [yataklı]   B= [lüks, bir, otel ,.. ]

B0Lemma: lüks, B0POS: Adj, B0Token: lüks, B1Lemma: bir, B1POS: Adj, B1Token: bir, S0B0Distance: 1, S0B0Lemma: yataklı_lüks, S0B0LemmaPOS: yataklı_Adj, S0B0POS: Adj_Adj, S0B0POSLemma: Adj_lüks, S0B0Token: yataklı_lüks, S0B1Lemma: yataklı_bir, S0B1LemmaPOS: yataklı_Adj, S0B1POS: Adj_Adj, S0B1POSLemma: Adj_bir, S0B1Token: yataklı_bir, S0Lemma: yataklı, S0POS: Adj, S0Token: yataklı, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, yataklı_isGouvernedBy_otel: true, yataklı_isGouvernedBy_otel_MODIFIER: true, 

74- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [lüks, bir, otel ,.. ]

B0Lemma: lüks, B0POS: Adj, B0Token: lüks, B1Lemma: bir, B1POS: Adj, B1Token: bir, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

75- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [lüks]   B= [bir, otel, _ ,.. ]

B0Lemma: bir, B0POS: Adj, B0Token: bir, B1Lemma: otel, B1POS: Noun, B1Token: otel, S0B0Distance: 1, S0B0Lemma: lüks_bir, S0B0LemmaPOS: lüks_Adj, S0B0POS: Adj_Adj, S0B0POSLemma: Adj_bir, S0B0Token: lüks_bir, S0B1Lemma: lüks_otel, S0B1LemmaPOS: lüks_Noun, S0B1POS: Adj_Noun, S0B1POSLemma: Adj_otel, S0B1Token: lüks_otel, S0Lemma: lüks, S0POS: Adj, S0Token: lüks, lüks_isGouvernedBy_otel: true, lüks_isGouvernedBy_otel_MODIFIER: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

76- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [bir, otel, _ ,.. ]

B0Lemma: bir, B0POS: Adj, B0Token: bir, B1Lemma: otel, B1POS: Noun, B1Token: otel, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

77- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [bir]   B= [otel, _, yapmayı ,.. ]

B0Lemma: otel, B0POS: Noun, B0Token: otel, B1Lemma: yap, B1POS: Verb, B1Token: _, S0B0Distance: 1, S0B0Lemma: bir_otel, S0B0LemmaPOS: bir_Noun, S0B0POS: Adj_Noun, S0B0POSLemma: Adj_otel, S0B0Token: bir_otel, S0B1Lemma: bir_yap, S0B1LemmaPOS: bir_Verb, S0B1POS: Adj_Verb, S0B1POSLemma: Adj_yap, S0B1Token: bir__, S0Lemma: bir, S0POS: Adj, S0Token: bir, bir_isGouvernedBy_otel: true, bir_isGouvernedBy_otel_DETERMINER: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

78- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [otel, _, yapmayı ,.. ]

B0Lemma: otel, B0POS: Noun, B0Token: otel, B1Lemma: yap, B1POS: Verb, B1Token: _, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

79- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [otel]   B= [_, yapmayı, planlıyoruz ,.. ]

B0Lemma: yap, B0POS: Verb, B0Token: _, B1Lemma: _, B1POS: Noun, B1Token: yapmayı, S0B0Distance: 1, S0B0Lemma: otel_yap, S0B0LemmaPOS: otel_Verb, S0B0POS: Noun_Verb, S0B0POSLemma: Noun_yap, S0B0Token: otel__, S0B1Lemma: otel__, S0B1LemmaPOS: otel_Noun, S0B1POS: Noun_Noun, S0B1POSLemma: Noun__, S0B1Token: otel_yapmayı, S0Lemma: otel, S0POS: Noun, S0Token: otel, otel_isGouvernedBy_yap: true, otel_isGouvernedBy_yap_OBJECT: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

80- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [_, yapmayı, planlıyoruz ,.. ]

B0Lemma: yap, B0POS: Verb, B0Token: _, B1Lemma: _, B1POS: Noun, B1Token: yapmayı, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

81- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [_]   B= [yapmayı, planlıyoruz, . ,.. ]

B0Lemma: _, B0POS: Noun, B0Token: yapmayı, B1Lemma: planla, B1POS: Verb, B1Token: planlıyoruz, S0B0Distance: 1, S0B0Lemma: yap__, S0B0LemmaPOS: yap_Noun, S0B0POS: Verb_Noun, S0B0POSLemma: Verb__, S0B0Token: __yapmayı, S0B1Lemma: yap_planla, S0B1LemmaPOS: yap_Verb, S0B1POS: Verb_Verb, S0B1POSLemma: Verb_planla, S0B1Token: __planlıyoruz, S0Lemma: yap, S0POS: Verb, S0Token: _, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, yap_isGouvernedBy__: true, yap_isGouvernedBy___DERIV: true, 

82- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [yapmayı, planlıyoruz, . ,.. ]

B0Lemma: _, B0POS: Noun, B0Token: yapmayı, B1Lemma: planla, B1POS: Verb, B1Token: planlıyoruz, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

83- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [yapmayı]   B= [planlıyoruz, ., Kalamış ,.. ]

B0Lemma: planla, B0POS: Verb, B0Token: planlıyoruz, B1Lemma: ., B1POS: Punc, B1Token: ., S0B0Distance: 1, S0B0Lemma: __planla, S0B0LemmaPOS: __Verb, S0B0POS: Noun_Verb, S0B0POSLemma: Noun_planla, S0B0Token: yapmayı_planlıyoruz, S0B1Lemma: __., S0B1LemmaPOS: __Punc, S0B1POS: Noun_Punc, S0B1POSLemma: Noun_., S0B1Token: yapmayı_., S0Lemma: _, S0POS: Noun, S0Token: yapmayı, __isGouvernedBy_planla: true, __isGouvernedBy_planla_OBJECT: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

84- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [planlıyoruz, ., Kalamış ,.. ]

B0Lemma: planla, B0POS: Verb, B0Token: planlıyoruz, B1Lemma: ., B1POS: Punc, B1Token: ., transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

85- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [planlıyoruz]   B= [., Kalamış, Tesisleri'ni ,.. ]

B0Lemma: ., B0POS: Punc, B0Token: ., B1Lemma: Kalamış, B1POS: Noun, B1Token: Kalamış, S0B0Distance: 1, S0B0Lemma: planla_., S0B0LemmaPOS: planla_Punc, S0B0POS: Verb_Punc, S0B0POSLemma: Verb_., S0B0Token: planlıyoruz_., S0B1Lemma: planla_Kalamış, S0B1LemmaPOS: planla_Noun, S0B1POS: Verb_Noun, S0B1POSLemma: Verb_Kalamış, S0B1Token: planlıyoruz_Kalamış, S0Lemma: planla, S0POS: Verb, S0Token: planlıyoruz, hasRighDep_PUNCTUATION: true, planla_._hasRighDep_PUNCTUATION: true, planla_hasRighDep_PUNCTUATION: true, planla_isGouvernedBy_taşı: true, planla_isGouvernedBy_taşı_COORDINATION: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

86- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [., Kalamış, Tesisleri'ni ,.. ]

B0Lemma: ., B0POS: Punc, B0Token: ., B1Lemma: Kalamış, B1POS: Noun, B1Token: Kalamış, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

87- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [Kalamış, Tesisleri'ni, ise ,.. ]

B0Lemma: Kalamış, B0POS: Noun, B0Token: Kalamış, B1Lemma: tesis, B1POS: Noun, B1Token: Tesisleri'ni, S0B0Distance: 1, S0B0Lemma: ._Kalamış, S0B0LemmaPOS: ._Noun, S0B0POS: Punc_Noun, S0B0POSLemma: Punc_Kalamış, S0B0Token: ._Kalamış, S0B1Lemma: ._tesis, S0B1LemmaPOS: ._Noun, S0B1POS: Punc_Noun, S0B1POSLemma: Punc_tesis, S0B1Token: ._Tesisleri'ni, S0Lemma: ., S0POS: Punc, S0Token: ., transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

88- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Kalamış, Tesisleri'ni, ise ,.. ]

B0Lemma: Kalamış, B0POS: Noun, B0Token: Kalamış, B1Lemma: tesis, B1POS: Noun, B1Token: Tesisleri'ni, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

89- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Kalamış]   B= [Tesisleri'ni, ise, Sosyal ,.. ]

B0Lemma: tesis, B0POS: Noun, B0Token: Tesisleri'ni, B1Lemma: ise, B1POS: Postp, B1Token: ise, Kalamış_isGouvernedBy_tesis: true, Kalamış_isGouvernedBy_tesis_POSSESSOR: true, S0B0Distance: 1, S0B0Lemma: Kalamış_tesis, S0B0LemmaPOS: Kalamış_Noun, S0B0POS: Noun_Noun, S0B0POSLemma: Noun_tesis, S0B0Token: Kalamış_Tesisleri'ni, S0B1Lemma: Kalamış_ise, S0B1LemmaPOS: Kalamış_Postp, S0B1POS: Noun_Postp, S0B1POSLemma: Noun_ise, S0B1Token: Kalamış_ise, S0Lemma: Kalamış, S0POS: Noun, S0Token: Kalamış, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

90- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Tesisleri'ni, ise, Sosyal ,.. ]

B0Lemma: tesis, B0POS: Noun, B0Token: Tesisleri'ni, B1Lemma: ise, B1POS: Postp, B1Token: ise, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

91- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Tesisleri'ni]   B= [ise, Sosyal, hizmet ,.. ]

B0Lemma: ise, B0POS: Postp, B0Token: ise, B1Lemma: sosyal, B1POS: Adj, B1Token: Sosyal, S0B0Distance: 1, S0B0Lemma: tesis_ise, S0B0LemmaPOS: tesis_Postp, S0B0POS: Noun_Postp, S0B0POSLemma: Noun_ise, S0B0Token: Tesisleri'ni_ise, S0B1Lemma: tesis_sosyal, S0B1LemmaPOS: tesis_Adj, S0B1POS: Noun_Adj, S0B1POSLemma: Noun_sosyal, S0B1Token: Tesisleri'ni_Sosyal, S0Lemma: tesis, S0POS: Noun, S0Token: Tesisleri'ni, tesis_isGouvernedBy_ise: true, tesis_isGouvernedBy_ise_ARGUMENT: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

92- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ise, Sosyal, hizmet ,.. ]

B0Lemma: ise, B0POS: Postp, B0Token: ise, B1Lemma: sosyal, B1POS: Adj, B1Token: Sosyal, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

93- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ise]   B= [Sosyal, hizmet, _ ,.. ]

B0Lemma: sosyal, B0POS: Adj, B0Token: Sosyal, B1Lemma: hizmet, B1POS: Noun, B1Token: hizmet, S0B0Distance: 1, S0B0Lemma: ise_sosyal, S0B0LemmaPOS: ise_Adj, S0B0POS: Postp_Adj, S0B0POSLemma: Postp_sosyal, S0B0Token: ise_Sosyal, S0B1Lemma: ise_hizmet, S0B1LemmaPOS: ise_Noun, S0B1POS: Postp_Noun, S0B1POSLemma: Postp_hizmet, S0B1Token: ise_hizmet, S0Lemma: ise, S0POS: Postp, S0Token: ise, ise_isGouvernedBy_et: true, ise_isGouvernedBy_et_MODIFIER: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

94- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Sosyal, hizmet, _ ,.. ]

B0Lemma: sosyal, B0POS: Adj, B0Token: Sosyal, B1Lemma: hizmet, B1POS: Noun, B1Token: hizmet, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

95- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Sosyal]   B= [hizmet, _, eden ,.. ]

B0Lemma: hizmet, B0POS: Noun, B0Token: hizmet, B1Lemma: et, B1POS: Verb, B1Token: _, S0B0Distance: 1, S0B0Lemma: sosyal_hizmet, S0B0LemmaPOS: sosyal_Noun, S0B0POS: Adj_Noun, S0B0POSLemma: Adj_hizmet, S0B0Token: Sosyal_hizmet, S0B1Lemma: sosyal_et, S0B1LemmaPOS: sosyal_Verb, S0B1POS: Adj_Verb, S0B1POSLemma: Adj_et, S0B1Token: Sosyal__, S0Lemma: sosyal, S0POS: Adj, S0Token: Sosyal, sosyal_isGouvernedBy_hizmet: true, sosyal_isGouvernedBy_hizmet_MODIFIER: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

96- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [hizmet, _, eden ,.. ]

B0Lemma: hizmet, B0POS: Noun, B0Token: hizmet, B1Lemma: et, B1POS: Verb, B1Token: _, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

97- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [hizmet]   B= [_, eden, bir ,.. ]

B0Lemma: et, B0POS: Verb, B0Token: _, B1Lemma: _, B1POS: Adj, B1Token: eden, S0B0Distance: 1, S0B0Lemma: hizmet_et, S0B0LemmaPOS: hizmet_Verb, S0B0POS: Noun_Verb, S0B0POSLemma: Noun_et, S0B0Token: hizmet__, S0B1Lemma: hizmet__, S0B1LemmaPOS: hizmet_Adj, S0B1POS: Noun_Adj, S0B1POSLemma: Noun__, S0B1Token: hizmet_eden, S0Lemma: hizmet, S0POS: Noun, S0Token: hizmet, hizmet_isGouvernedBy_et: true, hizmet_isGouvernedBy_et_MWE: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

98- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [_, eden, bir ,.. ]

B0Lemma: et, B0POS: Verb, B0Token: _, B1Lemma: _, B1POS: Adj, B1Token: eden, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

99- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [_]   B= [eden, bir, görev ,.. ]

B0Lemma: _, B0POS: Adj, B0Token: eden, B1Lemma: bir, B1POS: Adj, B1Token: bir, S0B0Distance: 1, S0B0Lemma: et__, S0B0LemmaPOS: et_Adj, S0B0POS: Verb_Adj, S0B0POSLemma: Verb__, S0B0Token: __eden, S0B1Lemma: et_bir, S0B1LemmaPOS: et_Adj, S0B1POS: Verb_Adj, S0B1POSLemma: Verb_bir, S0B1Token: __bir, S0Lemma: et, S0POS: Verb, S0Token: _, et_isGouvernedBy__: true, et_isGouvernedBy___DERIV: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

100- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [eden, bir, görev ,.. ]

B0Lemma: _, B0POS: Adj, B0Token: eden, B1Lemma: bir, B1POS: Adj, B1Token: bir, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

101- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [eden]   B= [bir, görev, _ ,.. ]

B0Lemma: bir, B0POS: Adj, B0Token: bir, B1Lemma: görev, B1POS: Noun, B1Token: görev, S0B0Distance: 1, S0B0Lemma: __bir, S0B0LemmaPOS: __Adj, S0B0POS: Adj_Adj, S0B0POSLemma: Adj_bir, S0B0Token: eden_bir, S0B1Lemma: __görev, S0B1LemmaPOS: __Noun, S0B1POS: Adj_Noun, S0B1POSLemma: Adj_görev, S0B1Token: eden_görev, S0Lemma: _, S0POS: Adj, S0Token: eden, __isGouvernedBy_görev: true, __isGouvernedBy_görev_MODIFIER: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

102- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [bir, görev, _ ,.. ]

B0Lemma: bir, B0POS: Adj, B0Token: bir, B1Lemma: görev, B1POS: Noun, B1Token: görev, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

103- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [bir]   B= [görev, _, yükleyip ,.. ]

B0Lemma: görev, B0POS: Noun, B0Token: görev, B1Lemma: yükle, B1POS: Verb, B1Token: _, S0B0Distance: 1, S0B0Lemma: bir_görev, S0B0LemmaPOS: bir_Noun, S0B0POS: Adj_Noun, S0B0POSLemma: Adj_görev, S0B0Token: bir_görev, S0B1Lemma: bir_yükle, S0B1LemmaPOS: bir_Verb, S0B1POS: Adj_Verb, S0B1POSLemma: Adj_yükle, S0B1Token: bir__, S0Lemma: bir, S0POS: Adj, S0Token: bir, bir_isGouvernedBy_görev: true, bir_isGouvernedBy_görev_DETERMINER: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

104- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [görev, _, yükleyip ,.. ]

B0Lemma: görev, B0POS: Noun, B0Token: görev, B1Lemma: yükle, B1POS: Verb, B1Token: _, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

105- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [görev]   B= [_, yükleyip, , ,.. ]

B0Lemma: yükle, B0POS: Verb, B0Token: _, B1Lemma: _, B1POS: Adverb, B1Token: yükleyip, S0B0Distance: 1, S0B0Lemma: görev_yükle, S0B0LemmaPOS: görev_Verb, S0B0POS: Noun_Verb, S0B0POSLemma: Noun_yükle, S0B0Token: görev__, S0B1Lemma: görev__, S0B1LemmaPOS: görev_Adverb, S0B1POS: Noun_Adverb, S0B1POSLemma: Noun__, S0B1Token: görev_yükleyip, S0Lemma: görev, S0POS: Noun, S0Token: görev, görev_isGouvernedBy__: true, görev_isGouvernedBy___OBJECT: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

106- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [_, yükleyip, , ,.. ]

B0Lemma: yükle, B0POS: Verb, B0Token: _, B1Lemma: _, B1POS: Adverb, B1Token: yükleyip, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

107- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [_]   B= [yükleyip, ,, _ ,.. ]

B0Lemma: _, B0POS: Adverb, B0Token: yükleyip, B1Lemma: ,, B1POS: Punc, B1Token: ,, S0B0Distance: 1, S0B0Lemma: yükle__, S0B0LemmaPOS: yükle_Adverb, S0B0POS: Verb_Adverb, S0B0POSLemma: Verb__, S0B0Token: __yükleyip, S0B1Lemma: yükle_,, S0B1LemmaPOS: yükle_Punc, S0B1POS: Verb_Punc, S0B1POSLemma: Verb_,, S0B1Token: __,, S0Lemma: yükle, S0POS: Verb, S0Token: _, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, yükle_isGouvernedBy__: true, yükle_isGouvernedBy___DERIV: true, 

108- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [yükleyip, ,, _ ,.. ]

B0Lemma: _, B0POS: Adverb, B0Token: yükleyip, B1Lemma: ,, B1POS: Punc, B1Token: ,, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

109- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [yükleyip]   B= [,, _, yüzme ,.. ]

B0Lemma: ,, B0POS: Punc, B0Token: ,, B1Lemma: yüz, B1POS: Verb, B1Token: _, S0B0Distance: 1, S0B0Lemma: __,, S0B0LemmaPOS: __Punc, S0B0POS: Adverb_Punc, S0B0POSLemma: Adverb_,, S0B0Token: yükleyip_,, S0B1Lemma: __yüz, S0B1LemmaPOS: __Verb, S0B1POS: Adverb_Verb, S0B1POSLemma: Adverb_yüz, S0B1Token: yükleyip__, S0Lemma: _, S0POS: Adverb, S0Token: yükleyip, __,_hasRighDep_PUNCTUATION: true, __hasRighDep_PUNCTUATION: true, __isGouvernedBy_taşı: true, __isGouvernedBy_taşı_COORDINATION: true, hasRighDep_PUNCTUATION: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

110- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, _, yüzme ,.. ]

B0Lemma: ,, B0POS: Punc, B0Token: ,, B1Lemma: yüz, B1POS: Verb, B1Token: _, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

111- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [_, yüzme, şubesinin ,.. ]

B0Lemma: yüz, B0POS: Verb, B0Token: _, B1Lemma: _, B1POS: Noun, B1Token: yüzme, S0B0Distance: 1, S0B0Lemma: ,_yüz, S0B0LemmaPOS: ,_Verb, S0B0POS: Punc_Verb, S0B0POSLemma: Punc_yüz, S0B0Token: ,__, S0B1Lemma: ,__, S0B1LemmaPOS: ,_Noun, S0B1POS: Punc_Noun, S0B1POSLemma: Punc__, S0B1Token: ,_yüzme, S0Lemma: ,, S0POS: Punc, S0Token: ,, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

112- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [_, yüzme, şubesinin ,.. ]

B0Lemma: yüz, B0POS: Verb, B0Token: _, B1Lemma: _, B1POS: Noun, B1Token: yüzme, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

113- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [_]   B= [yüzme, şubesinin, _ ,.. ]

B0Lemma: _, B0POS: Noun, B0Token: yüzme, B1Lemma: şube, B1POS: Noun, B1Token: şubesinin, S0B0Distance: 1, S0B0Lemma: yüz__, S0B0LemmaPOS: yüz_Noun, S0B0POS: Verb_Noun, S0B0POSLemma: Verb__, S0B0Token: __yüzme, S0B1Lemma: yüz_şube, S0B1LemmaPOS: yüz_Noun, S0B1POS: Verb_Noun, S0B1POSLemma: Verb_şube, S0B1Token: __şubesinin, S0Lemma: yüz, S0POS: Verb, S0Token: _, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, yüz_isGouvernedBy__: true, yüz_isGouvernedBy___DERIV: true, 

114- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [yüzme, şubesinin, _ ,.. ]

B0Lemma: _, B0POS: Noun, B0Token: yüzme, B1Lemma: şube, B1POS: Noun, B1Token: şubesinin, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

115- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [yüzme]   B= [şubesinin, _, çalışmalarını ,.. ]

B0Lemma: şube, B0POS: Noun, B0Token: şubesinin, B1Lemma: çalış, B1POS: Verb, B1Token: _, S0B0Distance: 1, S0B0Lemma: __şube, S0B0LemmaPOS: __Noun, S0B0POS: Noun_Noun, S0B0POSLemma: Noun_şube, S0B0Token: yüzme_şubesinin, S0B1Lemma: __çalış, S0B1LemmaPOS: __Verb, S0B1POS: Noun_Verb, S0B1POSLemma: Noun_çalış, S0B1Token: yüzme__, S0Lemma: _, S0POS: Noun, S0Token: yüzme, __isGouvernedBy_şube: true, __isGouvernedBy_şube_POSSESSOR: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

116- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [şubesinin, _, çalışmalarını ,.. ]

B0Lemma: şube, B0POS: Noun, B0Token: şubesinin, B1Lemma: çalış, B1POS: Verb, B1Token: _, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

117- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [şubesinin]   B= [_, çalışmalarını, _ ,.. ]

B0Lemma: çalış, B0POS: Verb, B0Token: _, B1Lemma: _, B1POS: Noun, B1Token: çalışmalarını, S0B0Distance: 1, S0B0Lemma: şube_çalış, S0B0LemmaPOS: şube_Verb, S0B0POS: Noun_Verb, S0B0POSLemma: Noun_çalış, S0B0Token: şubesinin__, S0B1Lemma: şube__, S0B1LemmaPOS: şube_Noun, S0B1POS: Noun_Noun, S0B1POSLemma: Noun__, S0B1Token: şubesinin_çalışmalarını, S0Lemma: şube, S0POS: Noun, S0Token: şubesinin, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, şube_isGouvernedBy__: true, şube_isGouvernedBy___POSSESSOR: true, 

118- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [_, çalışmalarını, _ ,.. ]

B0Lemma: çalış, B0POS: Verb, B0Token: _, B1Lemma: _, B1POS: Noun, B1Token: çalışmalarını, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

119- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [_]   B= [çalışmalarını, _, yapmayı ,.. ]

B0Lemma: _, B0POS: Noun, B0Token: çalışmalarını, B1Lemma: yap, B1POS: Verb, B1Token: _, S0B0Distance: 1, S0B0Lemma: çalış__, S0B0LemmaPOS: çalış_Noun, S0B0POS: Verb_Noun, S0B0POSLemma: Verb__, S0B0Token: __çalışmalarını, S0B1Lemma: çalış_yap, S0B1LemmaPOS: çalış_Verb, S0B1POS: Verb_Verb, S0B1POSLemma: Verb_yap, S0B1Token: ___, S0Lemma: çalış, S0POS: Verb, S0Token: _, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, çalış_isGouvernedBy__: true, çalış_isGouvernedBy___DERIV: true, 

120- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [çalışmalarını, _, yapmayı ,.. ]

B0Lemma: _, B0POS: Noun, B0Token: çalışmalarını, B1Lemma: yap, B1POS: Verb, B1Token: _, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

121- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [çalışmalarını]   B= [_, yapmayı, _ ,.. ]

B0Lemma: yap, B0POS: Verb, B0Token: _, B1Lemma: _, B1POS: Noun, B1Token: yapmayı, S0B0Distance: 1, S0B0Lemma: __yap, S0B0LemmaPOS: __Verb, S0B0POS: Noun_Verb, S0B0POSLemma: Noun_yap, S0B0Token: çalışmalarını__, S0B1Lemma: ___, S0B1LemmaPOS: __Noun, S0B1POS: Noun_Noun, S0B1POSLemma: Noun__, S0B1Token: çalışmalarını_yapmayı, S0Lemma: _, S0POS: Noun, S0Token: çalışmalarını, __isGouvernedBy_yap: true, __isGouvernedBy_yap_OBJECT: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

122- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [_, yapmayı, _ ,.. ]

B0Lemma: yap, B0POS: Verb, B0Token: _, B1Lemma: _, B1POS: Noun, B1Token: yapmayı, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

123- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [_]   B= [yapmayı, _, düşündüğümüz ,.. ]

B0Lemma: _, B0POS: Noun, B0Token: yapmayı, B1Lemma: düşün, B1POS: Verb, B1Token: _, S0B0Distance: 1, S0B0Lemma: yap__, S0B0LemmaPOS: yap_Noun, S0B0POS: Verb_Noun, S0B0POSLemma: Verb__, S0B0Token: __yapmayı, S0B1Lemma: yap_düşün, S0B1LemmaPOS: yap_Verb, S0B1POS: Verb_Verb, S0B1POSLemma: Verb_düşün, S0B1Token: ___, S0Lemma: yap, S0POS: Verb, S0Token: _, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, yap_isGouvernedBy__: true, yap_isGouvernedBy___DERIV: true, 

124- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [yapmayı, _, düşündüğümüz ,.. ]

B0Lemma: _, B0POS: Noun, B0Token: yapmayı, B1Lemma: düşün, B1POS: Verb, B1Token: _, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

125- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [yapmayı]   B= [_, düşündüğümüz, komplike ,.. ]

B0Lemma: düşün, B0POS: Verb, B0Token: _, B1Lemma: _, B1POS: Adj, B1Token: düşündüğümüz, S0B0Distance: 1, S0B0Lemma: __düşün, S0B0LemmaPOS: __Verb, S0B0POS: Noun_Verb, S0B0POSLemma: Noun_düşün, S0B0Token: yapmayı__, S0B1Lemma: ___, S0B1LemmaPOS: __Adj, S0B1POS: Noun_Adj, S0B1POSLemma: Noun__, S0B1Token: yapmayı_düşündüğümüz, S0Lemma: _, S0POS: Noun, S0Token: yapmayı, __isGouvernedBy_düşün: true, __isGouvernedBy_düşün_OBJECT: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

126- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [_, düşündüğümüz, komplike ,.. ]

B0Lemma: düşün, B0POS: Verb, B0Token: _, B1Lemma: _, B1POS: Adj, B1Token: düşündüğümüz, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

127- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [_]   B= [düşündüğümüz, komplike, başka ,.. ]

B0Lemma: _, B0POS: Adj, B0Token: düşündüğümüz, B1Lemma: komplike, B1POS: Adj, B1Token: komplike, S0B0Distance: 1, S0B0Lemma: düşün__, S0B0LemmaPOS: düşün_Adj, S0B0POS: Verb_Adj, S0B0POSLemma: Verb__, S0B0Token: __düşündüğümüz, S0B1Lemma: düşün_komplike, S0B1LemmaPOS: düşün_Adj, S0B1POS: Verb_Adj, S0B1POSLemma: Verb_komplike, S0B1Token: __komplike, S0Lemma: düşün, S0POS: Verb, S0Token: _, düşün_isGouvernedBy__: true, düşün_isGouvernedBy___DERIV: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

128- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [düşündüğümüz, komplike, başka ,.. ]

B0Lemma: _, B0POS: Adj, B0Token: düşündüğümüz, B1Lemma: komplike, B1POS: Adj, B1Token: komplike, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

129- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [düşündüğümüz]   B= [komplike, başka, bir ,.. ]

B0Lemma: komplike, B0POS: Adj, B0Token: komplike, B1Lemma: başka, B1POS: Adj, B1Token: başka, S0B0Distance: 1, S0B0Lemma: __komplike, S0B0LemmaPOS: __Adj, S0B0POS: Adj_Adj, S0B0POSLemma: Adj_komplike, S0B0Token: düşündüğümüz_komplike, S0B1Lemma: __başka, S0B1LemmaPOS: __Adj, S0B1POS: Adj_Adj, S0B1POSLemma: Adj_başka, S0B1Token: düşündüğümüz_başka, S0Lemma: _, S0POS: Adj, S0Token: düşündüğümüz, __isGouvernedBy_tesis: true, __isGouvernedBy_tesis_MODIFIER: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

130- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [komplike, başka, bir ,.. ]

B0Lemma: komplike, B0POS: Adj, B0Token: komplike, B1Lemma: başka, B1POS: Adj, B1Token: başka, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

131- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [komplike]   B= [başka, bir, tesise ,.. ]

B0Lemma: başka, B0POS: Adj, B0Token: başka, B1Lemma: bir, B1POS: Adj, B1Token: bir, S0B0Distance: 1, S0B0Lemma: komplike_başka, S0B0LemmaPOS: komplike_Adj, S0B0POS: Adj_Adj, S0B0POSLemma: Adj_başka, S0B0Token: komplike_başka, S0B1Lemma: komplike_bir, S0B1LemmaPOS: komplike_Adj, S0B1POS: Adj_Adj, S0B1POSLemma: Adj_bir, S0B1Token: komplike_bir, S0Lemma: komplike, S0POS: Adj, S0Token: komplike, komplike_isGouvernedBy_tesis: true, komplike_isGouvernedBy_tesis_MODIFIER: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

132- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [başka, bir, tesise ,.. ]

B0Lemma: başka, B0POS: Adj, B0Token: başka, B1Lemma: bir, B1POS: Adj, B1Token: bir, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

133- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [başka]   B= [bir, tesise, taşıyacağız ,.. ]

B0Lemma: bir, B0POS: Adj, B0Token: bir, B1Lemma: tesis, B1POS: Noun, B1Token: tesise, S0B0Distance: 1, S0B0Lemma: başka_bir, S0B0LemmaPOS: başka_Adj, S0B0POS: Adj_Adj, S0B0POSLemma: Adj_bir, S0B0Token: başka_bir, S0B1Lemma: başka_tesis, S0B1LemmaPOS: başka_Noun, S0B1POS: Adj_Noun, S0B1POSLemma: Adj_tesis, S0B1Token: başka_tesise, S0Lemma: başka, S0POS: Adj, S0Token: başka, başka_isGouvernedBy_tesis: true, başka_isGouvernedBy_tesis_MODIFIER: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

134- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [bir, tesise, taşıyacağız ,.. ]

B0Lemma: bir, B0POS: Adj, B0Token: bir, B1Lemma: tesis, B1POS: Noun, B1Token: tesise, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

135- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [bir]   B= [tesise, taşıyacağız, . ,.. ]

B0Lemma: tesis, B0POS: Noun, B0Token: tesise, B1Lemma: taşı, B1POS: Verb, B1Token: taşıyacağız, S0B0Distance: 1, S0B0Lemma: bir_tesis, S0B0LemmaPOS: bir_Noun, S0B0POS: Adj_Noun, S0B0POSLemma: Adj_tesis, S0B0Token: bir_tesise, S0B1Lemma: bir_taşı, S0B1LemmaPOS: bir_Verb, S0B1POS: Adj_Verb, S0B1POSLemma: Adj_taşı, S0B1Token: bir_taşıyacağız, S0Lemma: bir, S0POS: Adj, S0Token: bir, bir_isGouvernedBy_tesis: true, bir_isGouvernedBy_tesis_DETERMINER: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

136- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [tesise, taşıyacağız, . ,.. ]

B0Lemma: tesis, B0POS: Noun, B0Token: tesise, B1Lemma: taşı, B1POS: Verb, B1Token: taşıyacağız, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

137- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [tesise]   B= [taşıyacağız, ., Artık ,.. ]

B0Lemma: taşı, B0POS: Verb, B0Token: taşıyacağız, B1Lemma: ., B1POS: Punc, B1Token: ., S0B0Distance: 1, S0B0Lemma: tesis_taşı, S0B0LemmaPOS: tesis_Verb, S0B0POS: Noun_Verb, S0B0POSLemma: Noun_taşı, S0B0Token: tesise_taşıyacağız, S0B1Lemma: tesis_., S0B1LemmaPOS: tesis_Punc, S0B1POS: Noun_Punc, S0B1POSLemma: Noun_., S0B1Token: tesise_., S0Lemma: tesis, S0POS: Noun, S0Token: tesise, tesis_isGouvernedBy_taşı: true, tesis_isGouvernedBy_taşı_MODIFIER: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

138- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [taşıyacağız, ., Artık ,.. ]

B0Lemma: taşı, B0POS: Verb, B0Token: taşıyacağız, B1Lemma: ., B1POS: Punc, B1Token: ., transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

139- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [taşıyacağız]   B= [., Artık, tek ,.. ]

B0Lemma: ., B0POS: Punc, B0Token: ., B1Lemma: artık, B1POS: Adverb, B1Token: Artık, S0B0Distance: 1, S0B0Lemma: taşı_., S0B0LemmaPOS: taşı_Punc, S0B0POS: Verb_Punc, S0B0POSLemma: Verb_., S0B0Token: taşıyacağız_., S0B1Lemma: taşı_artık, S0B1LemmaPOS: taşı_Adverb, S0B1POS: Verb_Adverb, S0B1POSLemma: Verb_artık, S0B1Token: taşıyacağız_Artık, S0Lemma: taşı, S0POS: Verb, S0Token: taşıyacağız, hasRighDep_PUNCTUATION: true, taşı_._hasRighDep_PUNCTUATION: true, taşı_hasRighDep_PUNCTUATION: true, taşı_isGouvernedBy_var: true, taşı_isGouvernedBy_var_COORDINATION: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

140- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [., Artık, tek ,.. ]

B0Lemma: ., B0POS: Punc, B0Token: ., B1Lemma: artık, B1POS: Adverb, B1Token: Artık, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

141- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [Artık, tek, seçeneğimiz ,.. ]

B0Lemma: artık, B0POS: Adverb, B0Token: Artık, B1Lemma: tek, B1POS: Adj, B1Token: tek, S0B0Distance: 1, S0B0Lemma: ._artık, S0B0LemmaPOS: ._Adverb, S0B0POS: Punc_Adverb, S0B0POSLemma: Punc_artık, S0B0Token: ._Artık, S0B1Lemma: ._tek, S0B1LemmaPOS: ._Adj, S0B1POS: Punc_Adj, S0B1POSLemma: Punc_tek, S0B1Token: ._tek, S0Lemma: ., S0POS: Punc, S0Token: ., transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

142- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Artık, tek, seçeneğimiz ,.. ]

B0Lemma: artık, B0POS: Adverb, B0Token: Artık, B1Lemma: tek, B1POS: Adj, B1Token: tek, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

143- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Artık]   B= [tek, seçeneğimiz, var ,.. ]

B0Lemma: tek, B0POS: Adj, B0Token: tek, B1Lemma: seçenek, B1POS: Noun, B1Token: seçeneğimiz, S0B0Distance: 1, S0B0Lemma: artık_tek, S0B0LemmaPOS: artık_Adj, S0B0POS: Adverb_Adj, S0B0POSLemma: Adverb_tek, S0B0Token: Artık_tek, S0B1Lemma: artık_seçenek, S0B1LemmaPOS: artık_Noun, S0B1POS: Adverb_Noun, S0B1POSLemma: Adverb_seçenek, S0B1Token: Artık_seçeneğimiz, S0Lemma: artık, S0POS: Adverb, S0Token: Artık, artık_isGouvernedBy_var: true, artık_isGouvernedBy_var_MODIFIER: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

144- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [tek, seçeneğimiz, var ,.. ]

B0Lemma: tek, B0POS: Adj, B0Token: tek, B1Lemma: seçenek, B1POS: Noun, B1Token: seçeneğimiz, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

145- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [tek]   B= [seçeneğimiz, var, ; ,.. ]

B0Lemma: seçenek, B0POS: Noun, B0Token: seçeneğimiz, B1Lemma: var, B1POS: Adj, B1Token: var, S0B0Distance: 1, S0B0Lemma: tek_seçenek, S0B0LemmaPOS: tek_Noun, S0B0POS: Adj_Noun, S0B0POSLemma: Adj_seçenek, S0B0Token: tek_seçeneğimiz, S0B1Lemma: tek_var, S0B1LemmaPOS: tek_Adj, S0B1POS: Adj_Adj, S0B1POSLemma: Adj_var, S0B1Token: tek_var, S0Lemma: tek, S0POS: Adj, S0Token: tek, tek_isGouvernedBy_seçenek: true, tek_isGouvernedBy_seçenek_MODIFIER: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

146- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [seçeneğimiz, var, ; ,.. ]

B0Lemma: seçenek, B0POS: Noun, B0Token: seçeneğimiz, B1Lemma: var, B1POS: Adj, B1Token: var, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

147- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [seçeneğimiz]   B= [var, ;, o ,.. ]

B0Lemma: var, B0POS: Adj, B0Token: var, B1Lemma: ;, B1POS: Punc, B1Token: ;, S0B0Distance: 1, S0B0Lemma: seçenek_var, S0B0LemmaPOS: seçenek_Adj, S0B0POS: Noun_Adj, S0B0POSLemma: Noun_var, S0B0Token: seçeneğimiz_var, S0B1Lemma: seçenek_;, S0B1LemmaPOS: seçenek_Punc, S0B1POS: Noun_Punc, S0B1POSLemma: Noun_;, S0B1Token: seçeneğimiz_;, S0Lemma: seçenek, S0POS: Noun, S0Token: seçeneğimiz, seçenek_isGouvernedBy_var: true, seçenek_isGouvernedBy_var_SUBJECT: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

148- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [var, ;, o ,.. ]

B0Lemma: var, B0POS: Adj, B0Token: var, B1Lemma: ;, B1POS: Punc, B1Token: ;, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

149- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [var]   B= [;, o, da ,.. ]

B0Lemma: ;, B0POS: Punc, B0Token: ;, B1Lemma: o, B1POS: Pron, B1Token: o, S0B0Distance: 1, S0B0Lemma: var_;, S0B0LemmaPOS: var_Punc, S0B0POS: Adj_Punc, S0B0POSLemma: Adj_;, S0B0Token: var_;, S0B1Lemma: var_o, S0B1LemmaPOS: var_Pron, S0B1POS: Adj_Pron, S0B1POSLemma: Adj_o, S0B1Token: var_o, S0Lemma: var, S0POS: Adj, S0Token: var, hasRighDep_PUNCTUATION: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, var_;_hasRighDep_PUNCTUATION: true, var_hasRighDep_PUNCTUATION: true, var_isGouvernedBy__: true, var_isGouvernedBy___COORDINATION: true, 

150- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [;, o, da ,.. ]

B0Lemma: ;, B0POS: Punc, B0Token: ;, B1Lemma: o, B1POS: Pron, B1Token: o, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

151- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [;]   B= [o, da, kar ,.. ]

B0Lemma: o, B0POS: Pron, B0Token: o, B1Lemma: da, B1POS: Conj, B1Token: da, S0B0Distance: 1, S0B0Lemma: ;_o, S0B0LemmaPOS: ;_Pron, S0B0POS: Punc_Pron, S0B0POSLemma: Punc_o, S0B0Token: ;_o, S0B1Lemma: ;_da, S0B1LemmaPOS: ;_Conj, S0B1POS: Punc_Conj, S0B1POSLemma: Punc_da, S0B1Token: ;_da, S0Lemma: ;, S0POS: Punc, S0Token: ;, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

152- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [o, da, kar ,.. ]

B0Lemma: o, B0POS: Pron, B0Token: o, B1Lemma: da, B1POS: Conj, B1Token: da, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

153- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [o]   B= [da, kar, _ ,.. ]

B0Lemma: da, B0POS: Conj, B0Token: da, B1Lemma: kar, B1POS: Noun, B1Token: kar, S0B0Distance: 1, S0B0Lemma: o_da, S0B0LemmaPOS: o_Conj, S0B0POS: Pron_Conj, S0B0POSLemma: Pron_da, S0B0Token: o_da, S0B1Lemma: o_kar, S0B1LemmaPOS: o_Noun, S0B1POS: Pron_Noun, S0B1POSLemma: Pron_kar, S0B1Token: o_kar, S0Lemma: o, S0POS: Pron, S0Token: o, hasRighDep_INTENSIFIER: true, o_da_hasRighDep_INTENSIFIER: true, o_hasRighDep_INTENSIFIER: true, o_isGouvernedBy__: true, o_isGouvernedBy___SUBJECT: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

154- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [da, kar, _ ,.. ]

B0Lemma: da, B0POS: Conj, B0Token: da, B1Lemma: kar, B1POS: Noun, B1Token: kar, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

155- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [da]   B= [kar, _, etmek ,.. ]

B0Lemma: kar, B0POS: Noun, B0Token: kar, B1Lemma: et, B1POS: Verb, B1Token: _, S0B0Distance: 1, S0B0Lemma: da_kar, S0B0LemmaPOS: da_Noun, S0B0POS: Conj_Noun, S0B0POSLemma: Conj_kar, S0B0Token: da_kar, S0B1Lemma: da_et, S0B1LemmaPOS: da_Verb, S0B1POS: Conj_Verb, S0B1POSLemma: Conj_et, S0B1Token: da__, S0Lemma: da, S0POS: Conj, S0Token: da, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

156- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [kar, _, etmek ,.. ]

B0Lemma: kar, B0POS: Noun, B0Token: kar, B1Lemma: et, B1POS: Verb, B1Token: _, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

157- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [kar]   B= [_, etmek, . ,.. ]

B0Lemma: et, B0POS: Verb, B0Token: _, B1Lemma: _, B1POS: Noun, B1Token: etmek, S0B0Distance: 1, S0B0Lemma: kar_et, S0B0LemmaPOS: kar_Verb, S0B0POS: Noun_Verb, S0B0POSLemma: Noun_et, S0B0Token: kar__, S0B1Lemma: kar__, S0B1LemmaPOS: kar_Noun, S0B1POS: Noun_Noun, S0B1POSLemma: Noun__, S0B1Token: kar_etmek, S0Lemma: kar, S0POS: Noun, S0Token: kar, kar_isGouvernedBy_et: true, kar_isGouvernedBy_et_MWE: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

158- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [kar, _]   B= [etmek, ., Kulübü ,.. ]

B0Lemma: _, B0POS: Noun, B0Token: etmek, B1Lemma: ., B1POS: Punc, B1Token: ., S0B0Distance: 1, S0B0Lemma: et__, S0B0LemmaPOS: et_Noun, S0B0POS: Verb_Noun, S0B0POSLemma: Verb__, S0B0Token: __etmek, S0B1Lemma: et_., S0B1LemmaPOS: et_Punc, S0B1POS: Verb_Punc, S0B1POSLemma: Verb_., S0B1Token: __., S0Lemma: et, S0POS: Verb, S0Token: _, S1B0Lemma: kar__, S1B0LemmaPOS: kar_Noun, S1B0POS: Noun_Noun, S1B0POSLemma: Noun__, S1B0Token: kar_etmek, S1Lemma: kar, S1POS: Noun, S1S0Lemma: kar_et, S1S0LemmaPOS: kar_Verb, S1S0POS: Noun_Verb, S1S0POSLemma: Noun_et, S1S0Token: kar__, S1Token: kar, SyntaxicRelation: -MWE, et_isGouvernedBy__: true, et_isGouvernedBy___DERIV: true, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

159- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [kar]   B= [etmek, ., Kulübü ,.. ]

B0Lemma: _, B0POS: Noun, B0Token: etmek, B1Lemma: ., B1POS: Punc, B1Token: ., S0B0Distance: 2, S0B0Lemma: kar__, S0B0LemmaPOS: kar_Noun, S0B0POS: Noun_Noun, S0B0POSLemma: Noun__, S0B0Token: kar_etmek, S0B1Lemma: kar_., S0B1LemmaPOS: kar_Punc, S0B1POS: Noun_Punc, S0B1POSLemma: Noun_., S0B1Token: kar_., S0Lemma: kar, S0POS: Noun, S0Token: kar, transitionHistoryLength1: 0, transitionHistoryLength2: 00, transitionHistoryLength3: 002, 

160- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [kar, etmek]   B= [., Kulübü, 14 ,.. ]

B0Lemma: ., B0POS: Punc, B0Token: ., B1Lemma: kulüp, B1POS: Noun, B1Token: Kulübü, S0B0Distance: 1, S0B0Lemma: __., S0B0LemmaPOS: __Punc, S0B0POS: Noun_Punc, S0B0POSLemma: Noun_., S0B0Token: etmek_., S0B1Lemma: __kulüp, S0B1LemmaPOS: __Noun, S0B1POS: Noun_Noun, S0B1POSLemma: Noun_kulüp, S0B1Token: etmek_Kulübü, S0Lemma: _, S0POS: Noun, S0Token: etmek, S1B0Lemma: kar_., S1B0LemmaPOS: kar_Punc, S1B0POS: Noun_Punc, S1B0POSLemma: Noun_., S1B0Token: kar_., S1Lemma: kar, S1POS: Noun, S1S0Lemma: kar__, S1S0LemmaPOS: kar_Noun, S1S0POS: Noun_Noun, S1S0POSLemma: Noun__, S1S0Token: kar_etmek, S1Token: kar, __._hasRighDep_PUNCTUATION: true, __hasRighDep_PUNCTUATION: true, __isGouvernedBy_al: true, __isGouvernedBy_al_SUBJECT: true, hasRighDep_PUNCTUATION: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 200, 

161- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[kar, etmek]]   B= [., Kulübü, 14 ,.. ]

B0Lemma: ., B0POS: Punc, B0Token: ., B1Lemma: kulüp, B1POS: Noun, B1Token: Kulübü, S0B0Distance: 1, S0B0Lemma: kar___., S0B0LemmaPOS: kar___Punc, S0B0POS: Noun_Noun_Punc, S0B0POSLemma: Noun_Noun_., S0B0Token: kar_etmek_., S0B1Lemma: kar___kulüp, S0B1LemmaPOS: kar___Noun, S0B1POS: Noun_Noun_Noun, S0B1POSLemma: Noun_Noun_kulüp, S0B1Token: kar_etmek_Kulübü, S0Lemma: kar__, S0POS: Noun_Noun, S0Token: kar_etmek, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

162- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [., Kulübü, 14 ,.. ]

B0Lemma: ., B0POS: Punc, B0Token: ., B1Lemma: kulüp, B1POS: Noun, B1Token: Kulübü, transitionHistoryLength1: 1, transitionHistoryLength2: 10, transitionHistoryLength3: 102, 

163- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [Kulübü, 14, milyon ,.. ]

B0Lemma: kulüp, B0POS: Noun, B0Token: Kulübü, B1Lemma: 14, B1POS: Adj, B1Token: 14, S0B0Distance: 1, S0B0Lemma: ._kulüp, S0B0LemmaPOS: ._Noun, S0B0POS: Punc_Noun, S0B0POSLemma: Punc_kulüp, S0B0Token: ._Kulübü, S0B1Lemma: ._14, S0B1LemmaPOS: ._Adj, S0B1POS: Punc_Adj, S0B1POSLemma: Punc_14, S0B1Token: ._14, S0Lemma: ., S0POS: Punc, S0Token: ., transitionHistoryLength1: 2, transitionHistoryLength2: 21, transitionHistoryLength3: 210, 

164- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Kulübü, 14, milyon ,.. ]

B0Lemma: kulüp, B0POS: Noun, B0Token: Kulübü, B1Lemma: 14, B1POS: Adj, B1Token: 14, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 021, 

165- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Kulübü]   B= [14, milyon, dolar ,.. ]

B0Lemma: 14, B0POS: Adj, B0Token: 14, B1Lemma: milyon, B1POS: Adj, B1Token: milyon, S0B0Distance: 1, S0B0Lemma: kulüp_14, S0B0LemmaPOS: kulüp_Adj, S0B0POS: Noun_Adj, S0B0POSLemma: Noun_14, S0B0Token: Kulübü_14, S0B1Lemma: kulüp_milyon, S0B1LemmaPOS: kulüp_Adj, S0B1POS: Noun_Adj, S0B1POSLemma: Noun_milyon, S0B1Token: Kulübü_milyon, S0Lemma: kulüp, S0POS: Noun, S0Token: Kulübü, kulüp_isGouvernedBy_al: true, kulüp_isGouvernedBy_al_OBJECT: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

166- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [14, milyon, dolar ,.. ]

B0Lemma: 14, B0POS: Adj, B0Token: 14, B1Lemma: milyon, B1POS: Adj, B1Token: milyon, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

167- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [14]   B= [milyon, dolar, borçla ,.. ]

14_isGouvernedBy_milyon: true, 14_isGouvernedBy_milyon_MWE: true, B0Lemma: milyon, B0POS: Adj, B0Token: milyon, B1Lemma: dolar, B1POS: Noun, B1Token: dolar, S0B0Distance: 1, S0B0Lemma: 14_milyon, S0B0LemmaPOS: 14_Adj, S0B0POS: Adj_Adj, S0B0POSLemma: Adj_milyon, S0B0Token: 14_milyon, S0B1Lemma: 14_dolar, S0B1LemmaPOS: 14_Noun, S0B1POS: Adj_Noun, S0B1POSLemma: Adj_dolar, S0B1Token: 14_dolar, S0Lemma: 14, S0POS: Adj, S0Token: 14, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

168- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [milyon, dolar, borçla ,.. ]

B0Lemma: milyon, B0POS: Adj, B0Token: milyon, B1Lemma: dolar, B1POS: Noun, B1Token: dolar, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

169- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [milyon]   B= [dolar, borçla, devir ,.. ]

B0Lemma: dolar, B0POS: Noun, B0Token: dolar, B1Lemma: borç, B1POS: Noun, B1Token: borçla, S0B0Distance: 1, S0B0Lemma: milyon_dolar, S0B0LemmaPOS: milyon_Noun, S0B0POS: Adj_Noun, S0B0POSLemma: Adj_dolar, S0B0Token: milyon_dolar, S0B1Lemma: milyon_borç, S0B1LemmaPOS: milyon_Noun, S0B1POS: Adj_Noun, S0B1POSLemma: Adj_borç, S0B1Token: milyon_borçla, S0Lemma: milyon, S0POS: Adj, S0Token: milyon, milyon_isGouvernedBy_dolar: true, milyon_isGouvernedBy_dolar_MODIFIER: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

170- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [dolar, borçla, devir ,.. ]

B0Lemma: dolar, B0POS: Noun, B0Token: dolar, B1Lemma: borç, B1POS: Noun, B1Token: borçla, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

171- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [dolar]   B= [borçla, devir, aldık ,.. ]

B0Lemma: borç, B0POS: Noun, B0Token: borçla, B1Lemma: devir, B1POS: Noun, B1Token: devir, S0B0Distance: 1, S0B0Lemma: dolar_borç, S0B0LemmaPOS: dolar_Noun, S0B0POS: Noun_Noun, S0B0POSLemma: Noun_borç, S0B0Token: dolar_borçla, S0B1Lemma: dolar_devir, S0B1LemmaPOS: dolar_Noun, S0B1POS: Noun_Noun, S0B1POSLemma: Noun_devir, S0B1Token: dolar_devir, S0Lemma: dolar, S0POS: Noun, S0Token: dolar, dolar_isGouvernedBy_borç: true, dolar_isGouvernedBy_borç_MODIFIER: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

172- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [borçla, devir, aldık ,.. ]

B0Lemma: borç, B0POS: Noun, B0Token: borçla, B1Lemma: devir, B1POS: Noun, B1Token: devir, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

173- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [borçla]   B= [devir, aldık, . ,.. ]

B0Lemma: devir, B0POS: Noun, B0Token: devir, B1Lemma: al, B1POS: Verb, B1Token: aldık, S0B0Distance: 1, S0B0Lemma: borç_devir, S0B0LemmaPOS: borç_Noun, S0B0POS: Noun_Noun, S0B0POSLemma: Noun_devir, S0B0Token: borçla_devir, S0B1Lemma: borç_al, S0B1LemmaPOS: borç_Verb, S0B1POS: Noun_Verb, S0B1POSLemma: Noun_al, S0B1Token: borçla_aldık, S0Lemma: borç, S0POS: Noun, S0Token: borçla, borç_isGouvernedBy_al: true, borç_isGouvernedBy_al_MODIFIER: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

174- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [devir, aldık, . ,.. ]

B0Lemma: devir, B0POS: Noun, B0Token: devir, B1Lemma: al, B1POS: Verb, B1Token: aldık, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

175- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [devir]   B= [aldık, ., 1998 ,.. ]

B0Lemma: al, B0POS: Verb, B0Token: aldık, B1Lemma: ., B1POS: Punc, B1Token: ., S0B0Distance: 1, S0B0Lemma: devir_al, S0B0LemmaPOS: devir_Verb, S0B0POS: Noun_Verb, S0B0POSLemma: Noun_al, S0B0Token: devir_aldık, S0B1Lemma: devir_., S0B1LemmaPOS: devir_Punc, S0B1POS: Noun_Punc, S0B1POSLemma: Noun_., S0B1Token: devir_., S0Lemma: devir, S0POS: Noun, S0Token: devir, devir_isGouvernedBy_al: true, devir_isGouvernedBy_al_OBJECT: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

176- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [devir, aldık]   B= [., 1998, yılında ,.. ]

B0Lemma: ., B0POS: Punc, B0Token: ., B1Lemma: 1998, B1POS: Adj, B1Token: 1998, S0B0Distance: 1, S0B0Lemma: al_., S0B0LemmaPOS: al_Punc, S0B0POS: Verb_Punc, S0B0POSLemma: Verb_., S0B0Token: aldık_., S0B1Lemma: al_1998, S0B1LemmaPOS: al_Adj, S0B1POS: Verb_Adj, S0B1POSLemma: Verb_1998, S0B1Token: aldık_1998, S0Lemma: al, S0POS: Verb, S0Token: aldık, S1B0Lemma: devir_., S1B0LemmaPOS: devir_Punc, S1B0POS: Noun_Punc, S1B0POSLemma: Noun_., S1B0Token: devir_., S1Lemma: devir, S1POS: Noun, S1S0Lemma: devir_al, S1S0LemmaPOS: devir_Verb, S1S0POS: Noun_Verb, S1S0POSLemma: Noun_al, S1S0Token: devir_aldık, S1Token: devir, SyntaxicRelation: -OBJECT, al_._hasRighDep_PUNCTUATION: true, al_hasRighDep_PUNCTUATION: true, al_isGouvernedBy_hedefle: true, al_isGouvernedBy_hedefle_COORDINATION: true, hasRighDep_PUNCTUATION: true, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

177- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[devir, aldık]]   B= [., 1998, yılında ,.. ]

B0Lemma: ., B0POS: Punc, B0Token: ., B1Lemma: 1998, B1POS: Adj, B1Token: 1998, S0B0Distance: 1, S0B0Lemma: devir_al_., S0B0LemmaPOS: devir_al_Punc, S0B0POS: Noun_Verb_Punc, S0B0POSLemma: Noun_Verb_., S0B0Token: devir_aldık_., S0B1Lemma: devir_al_1998, S0B1LemmaPOS: devir_al_Adj, S0B1POS: Noun_Verb_Adj, S0B1POSLemma: Noun_Verb_1998, S0B1Token: devir_aldık_1998, S0Lemma: devir_al, S0POS: Noun_Verb, S0Token: devir_aldık, transitionHistoryLength1: 0, transitionHistoryLength2: 00, transitionHistoryLength3: 002, 

178- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [., 1998, yılında ,.. ]

B0Lemma: ., B0POS: Punc, B0Token: ., B1Lemma: 1998, B1POS: Adj, B1Token: 1998, transitionHistoryLength1: 1, transitionHistoryLength2: 10, transitionHistoryLength3: 100, 

179- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [1998, yılında, bu ,.. ]

B0Lemma: 1998, B0POS: Adj, B0Token: 1998, B1Lemma: yıl, B1POS: Noun, B1Token: yılında, S0B0Distance: 1, S0B0Lemma: ._1998, S0B0LemmaPOS: ._Adj, S0B0POS: Punc_Adj, S0B0POSLemma: Punc_1998, S0B0Token: ._1998, S0B1Lemma: ._yıl, S0B1LemmaPOS: ._Noun, S0B1POS: Punc_Noun, S0B1POSLemma: Punc_yıl, S0B1Token: ._yılında, S0Lemma: ., S0POS: Punc, S0Token: ., transitionHistoryLength1: 2, transitionHistoryLength2: 21, transitionHistoryLength3: 210, 

180- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [1998, yılında, bu ,.. ]

B0Lemma: 1998, B0POS: Adj, B0Token: 1998, B1Lemma: yıl, B1POS: Noun, B1Token: yılında, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 021, 

181- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [1998]   B= [yılında, bu, borcu ,.. ]

1998_isGouvernedBy_yıl: true, 1998_isGouvernedBy_yıl_MODIFIER: true, B0Lemma: yıl, B0POS: Noun, B0Token: yılında, B1Lemma: bu, B1POS: Det, B1Token: bu, S0B0Distance: 1, S0B0Lemma: 1998_yıl, S0B0LemmaPOS: 1998_Noun, S0B0POS: Adj_Noun, S0B0POSLemma: Adj_yıl, S0B0Token: 1998_yılında, S0B1Lemma: 1998_bu, S0B1LemmaPOS: 1998_Det, S0B1POS: Adj_Det, S0B1POSLemma: Adj_bu, S0B1Token: 1998_bu, S0Lemma: 1998, S0POS: Adj, S0Token: 1998, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

182- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [yılında, bu, borcu ,.. ]

B0Lemma: yıl, B0POS: Noun, B0Token: yılında, B1Lemma: bu, B1POS: Det, B1Token: bu, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

183- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [yılında]   B= [bu, borcu, dört ,.. ]

B0Lemma: bu, B0POS: Det, B0Token: bu, B1Lemma: borç, B1POS: Noun, B1Token: borcu, S0B0Distance: 1, S0B0Lemma: yıl_bu, S0B0LemmaPOS: yıl_Det, S0B0POS: Noun_Det, S0B0POSLemma: Noun_bu, S0B0Token: yılında_bu, S0B1Lemma: yıl_borç, S0B1LemmaPOS: yıl_Noun, S0B1POS: Noun_Noun, S0B1POSLemma: Noun_borç, S0B1Token: yılında_borcu, S0Lemma: yıl, S0POS: Noun, S0Token: yılında, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, yıl_isGouvernedBy_in: true, yıl_isGouvernedBy_in_MODIFIER: true, 

184- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [bu, borcu, dört ,.. ]

B0Lemma: bu, B0POS: Det, B0Token: bu, B1Lemma: borç, B1POS: Noun, B1Token: borcu, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

185- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [bu]   B= [borcu, dört, milyon ,.. ]

B0Lemma: borç, B0POS: Noun, B0Token: borcu, B1Lemma: dört, B1POS: Adj, B1Token: dört, S0B0Distance: 1, S0B0Lemma: bu_borç, S0B0LemmaPOS: bu_Noun, S0B0POS: Det_Noun, S0B0POSLemma: Det_borç, S0B0Token: bu_borcu, S0B1Lemma: bu_dört, S0B1LemmaPOS: bu_Adj, S0B1POS: Det_Adj, S0B1POSLemma: Det_dört, S0B1Token: bu_dört, S0Lemma: bu, S0POS: Det, S0Token: bu, bu_isGouvernedBy_borç: true, bu_isGouvernedBy_borç_DETERMINER: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

186- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [borcu, dört, milyon ,.. ]

B0Lemma: borç, B0POS: Noun, B0Token: borcu, B1Lemma: dört, B1POS: Adj, B1Token: dört, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

187- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [borcu]   B= [dört, milyon, dolara ,.. ]

B0Lemma: dört, B0POS: Adj, B0Token: dört, B1Lemma: milyon, B1POS: Adj, B1Token: milyon, S0B0Distance: 1, S0B0Lemma: borç_dört, S0B0LemmaPOS: borç_Adj, S0B0POS: Noun_Adj, S0B0POSLemma: Noun_dört, S0B0Token: borcu_dört, S0B1Lemma: borç_milyon, S0B1LemmaPOS: borç_Adj, S0B1POS: Noun_Adj, S0B1POSLemma: Noun_milyon, S0B1Token: borcu_milyon, S0Lemma: borç, S0POS: Noun, S0Token: borcu, borç_isGouvernedBy_in: true, borç_isGouvernedBy_in_OBJECT: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

188- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [dört, milyon, dolara ,.. ]

B0Lemma: dört, B0POS: Adj, B0Token: dört, B1Lemma: milyon, B1POS: Adj, B1Token: milyon, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

189- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [dört]   B= [milyon, dolara, _ ,.. ]

B0Lemma: milyon, B0POS: Adj, B0Token: milyon, B1Lemma: dolar, B1POS: Noun, B1Token: dolara, S0B0Distance: 1, S0B0Lemma: dört_milyon, S0B0LemmaPOS: dört_Adj, S0B0POS: Adj_Adj, S0B0POSLemma: Adj_milyon, S0B0Token: dört_milyon, S0B1Lemma: dört_dolar, S0B1LemmaPOS: dört_Noun, S0B1POS: Adj_Noun, S0B1POSLemma: Adj_dolar, S0B1Token: dört_dolara, S0Lemma: dört, S0POS: Adj, S0Token: dört, dört_isGouvernedBy_milyon: true, dört_isGouvernedBy_milyon_MWE: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

190- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [milyon, dolara, _ ,.. ]

B0Lemma: milyon, B0POS: Adj, B0Token: milyon, B1Lemma: dolar, B1POS: Noun, B1Token: dolara, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

191- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [milyon]   B= [dolara, _, indirmeyi ,.. ]

B0Lemma: dolar, B0POS: Noun, B0Token: dolara, B1Lemma: in, B1POS: Verb, B1Token: _, S0B0Distance: 1, S0B0Lemma: milyon_dolar, S0B0LemmaPOS: milyon_Noun, S0B0POS: Adj_Noun, S0B0POSLemma: Adj_dolar, S0B0Token: milyon_dolara, S0B1Lemma: milyon_in, S0B1LemmaPOS: milyon_Verb, S0B1POS: Adj_Verb, S0B1POSLemma: Adj_in, S0B1Token: milyon__, S0Lemma: milyon, S0POS: Adj, S0Token: milyon, milyon_isGouvernedBy_dolar: true, milyon_isGouvernedBy_dolar_MODIFIER: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

192- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [dolara, _, indirmeyi ,.. ]

B0Lemma: dolar, B0POS: Noun, B0Token: dolara, B1Lemma: in, B1POS: Verb, B1Token: _, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

193- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [dolara]   B= [_, indirmeyi, hedefliyoruz ,.. ]

B0Lemma: in, B0POS: Verb, B0Token: _, B1Lemma: _, B1POS: Noun, B1Token: indirmeyi, S0B0Distance: 1, S0B0Lemma: dolar_in, S0B0LemmaPOS: dolar_Verb, S0B0POS: Noun_Verb, S0B0POSLemma: Noun_in, S0B0Token: dolara__, S0B1Lemma: dolar__, S0B1LemmaPOS: dolar_Noun, S0B1POS: Noun_Noun, S0B1POSLemma: Noun__, S0B1Token: dolara_indirmeyi, S0Lemma: dolar, S0POS: Noun, S0Token: dolara, dolar_isGouvernedBy_in: true, dolar_isGouvernedBy_in_MODIFIER: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

194- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [_, indirmeyi, hedefliyoruz ,.. ]

B0Lemma: in, B0POS: Verb, B0Token: _, B1Lemma: _, B1POS: Noun, B1Token: indirmeyi, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

195- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [_]   B= [indirmeyi, hedefliyoruz, . ,.. ]

B0Lemma: _, B0POS: Noun, B0Token: indirmeyi, B1Lemma: hedefle, B1POS: Verb, B1Token: hedefliyoruz, S0B0Distance: 1, S0B0Lemma: in__, S0B0LemmaPOS: in_Noun, S0B0POS: Verb_Noun, S0B0POSLemma: Verb__, S0B0Token: __indirmeyi, S0B1Lemma: in_hedefle, S0B1LemmaPOS: in_Verb, S0B1POS: Verb_Verb, S0B1POSLemma: Verb_hedefle, S0B1Token: __hedefliyoruz, S0Lemma: in, S0POS: Verb, S0Token: _, in_isGouvernedBy__: true, in_isGouvernedBy___DERIV: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

196- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [indirmeyi, hedefliyoruz, . ,.. ]

B0Lemma: _, B0POS: Noun, B0Token: indirmeyi, B1Lemma: hedefle, B1POS: Verb, B1Token: hedefliyoruz, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

197- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [indirmeyi]   B= [hedefliyoruz, ., 2001 ,.. ]

B0Lemma: hedefle, B0POS: Verb, B0Token: hedefliyoruz, B1Lemma: ., B1POS: Punc, B1Token: ., S0B0Distance: 1, S0B0Lemma: __hedefle, S0B0LemmaPOS: __Verb, S0B0POS: Noun_Verb, S0B0POSLemma: Noun_hedefle, S0B0Token: indirmeyi_hedefliyoruz, S0B1Lemma: __., S0B1LemmaPOS: __Punc, S0B1POS: Noun_Punc, S0B1POSLemma: Noun_., S0B1Token: indirmeyi_., S0Lemma: _, S0POS: Noun, S0Token: indirmeyi, __isGouvernedBy_hedefle: true, __isGouvernedBy_hedefle_OBJECT: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

198- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [hedefliyoruz, ., 2001 ,.. ]

B0Lemma: hedefle, B0POS: Verb, B0Token: hedefliyoruz, B1Lemma: ., B1POS: Punc, B1Token: ., transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

199- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [hedefliyoruz]   B= [., 2001, yılında ,.. ]

B0Lemma: ., B0POS: Punc, B0Token: ., B1Lemma: 2001, B1POS: Adj, B1Token: 2001, S0B0Distance: 1, S0B0Lemma: hedefle_., S0B0LemmaPOS: hedefle_Punc, S0B0POS: Verb_Punc, S0B0POSLemma: Verb_., S0B0Token: hedefliyoruz_., S0B1Lemma: hedefle_2001, S0B1LemmaPOS: hedefle_Adj, S0B1POS: Verb_Adj, S0B1POSLemma: Verb_2001, S0B1Token: hedefliyoruz_2001, S0Lemma: hedefle, S0POS: Verb, S0Token: hedefliyoruz, hasRighDep_PUNCTUATION: true, hedefle_._hasRighDep_PUNCTUATION: true, hedefle_hasRighDep_PUNCTUATION: true, hedefle_isGouvernedBy_kal: true, hedefle_isGouvernedBy_kal_COORDINATION: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

200- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [., 2001, yılında ,.. ]

B0Lemma: ., B0POS: Punc, B0Token: ., B1Lemma: 2001, B1POS: Adj, B1Token: 2001, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

201- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [2001, yılında, ise ,.. ]

B0Lemma: 2001, B0POS: Adj, B0Token: 2001, B1Lemma: yıl, B1POS: Noun, B1Token: yılında, S0B0Distance: 1, S0B0Lemma: ._2001, S0B0LemmaPOS: ._Adj, S0B0POS: Punc_Adj, S0B0POSLemma: Punc_2001, S0B0Token: ._2001, S0B1Lemma: ._yıl, S0B1LemmaPOS: ._Noun, S0B1POS: Punc_Noun, S0B1POSLemma: Punc_yıl, S0B1Token: ._yılında, S0Lemma: ., S0POS: Punc, S0Token: ., transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

202- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [2001, yılında, ise ,.. ]

B0Lemma: 2001, B0POS: Adj, B0Token: 2001, B1Lemma: yıl, B1POS: Noun, B1Token: yılında, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

203- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [2001]   B= [yılında, ise, hiç ,.. ]

2001_isGouvernedBy_yıl: true, 2001_isGouvernedBy_yıl_MODIFIER: true, B0Lemma: yıl, B0POS: Noun, B0Token: yılında, B1Lemma: ise, B1POS: Postp, B1Token: ise, S0B0Distance: 1, S0B0Lemma: 2001_yıl, S0B0LemmaPOS: 2001_Noun, S0B0POS: Adj_Noun, S0B0POSLemma: Adj_yıl, S0B0Token: 2001_yılında, S0B1Lemma: 2001_ise, S0B1LemmaPOS: 2001_Postp, S0B1POS: Adj_Postp, S0B1POSLemma: Adj_ise, S0B1Token: 2001_ise, S0Lemma: 2001, S0POS: Adj, S0Token: 2001, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

204- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [yılında, ise, hiç ,.. ]

B0Lemma: yıl, B0POS: Noun, B0Token: yılında, B1Lemma: ise, B1POS: Postp, B1Token: ise, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

205- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [yılında]   B= [ise, hiç, borcumuz ,.. ]

B0Lemma: ise, B0POS: Postp, B0Token: ise, B1Lemma: hiç, B1POS: Adverb, B1Token: hiç, S0B0Distance: 1, S0B0Lemma: yıl_ise, S0B0LemmaPOS: yıl_Postp, S0B0POS: Noun_Postp, S0B0POSLemma: Noun_ise, S0B0Token: yılında_ise, S0B1Lemma: yıl_hiç, S0B1LemmaPOS: yıl_Adverb, S0B1POS: Noun_Adverb, S0B1POSLemma: Noun_hiç, S0B1Token: yılında_hiç, S0Lemma: yıl, S0POS: Noun, S0Token: yılında, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, yıl_isGouvernedBy_ise: true, yıl_isGouvernedBy_ise_ARGUMENT: true, 

206- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ise, hiç, borcumuz ,.. ]

B0Lemma: ise, B0POS: Postp, B0Token: ise, B1Lemma: hiç, B1POS: Adverb, B1Token: hiç, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

207- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ise]   B= [hiç, borcumuz, kalmayacak ,.. ]

B0Lemma: hiç, B0POS: Adverb, B0Token: hiç, B1Lemma: borç, B1POS: Noun, B1Token: borcumuz, S0B0Distance: 1, S0B0Lemma: ise_hiç, S0B0LemmaPOS: ise_Adverb, S0B0POS: Postp_Adverb, S0B0POSLemma: Postp_hiç, S0B0Token: ise_hiç, S0B1Lemma: ise_borç, S0B1LemmaPOS: ise_Noun, S0B1POS: Postp_Noun, S0B1POSLemma: Postp_borç, S0B1Token: ise_borcumuz, S0Lemma: ise, S0POS: Postp, S0Token: ise, ise_isGouvernedBy_kal: true, ise_isGouvernedBy_kal_MODIFIER: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

208- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [hiç, borcumuz, kalmayacak ,.. ]

B0Lemma: hiç, B0POS: Adverb, B0Token: hiç, B1Lemma: borç, B1POS: Noun, B1Token: borcumuz, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

209- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [hiç]   B= [borcumuz, kalmayacak, . ,.. ]

B0Lemma: borç, B0POS: Noun, B0Token: borcumuz, B1Lemma: kal, B1POS: Verb, B1Token: kalmayacak, S0B0Distance: 1, S0B0Lemma: hiç_borç, S0B0LemmaPOS: hiç_Noun, S0B0POS: Adverb_Noun, S0B0POSLemma: Adverb_borç, S0B0Token: hiç_borcumuz, S0B1Lemma: hiç_kal, S0B1LemmaPOS: hiç_Verb, S0B1POS: Adverb_Verb, S0B1POSLemma: Adverb_kal, S0B1Token: hiç_kalmayacak, S0Lemma: hiç, S0POS: Adverb, S0Token: hiç, hiç_isGouvernedBy_kal: true, hiç_isGouvernedBy_kal_MODIFIER: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

210- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [borcumuz, kalmayacak, . ,.. ]

B0Lemma: borç, B0POS: Noun, B0Token: borcumuz, B1Lemma: kal, B1POS: Verb, B1Token: kalmayacak, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

211- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [borcumuz]   B= [kalmayacak, ., Galatasaray ,.. ]

B0Lemma: kal, B0POS: Verb, B0Token: kalmayacak, B1Lemma: ., B1POS: Punc, B1Token: ., S0B0Distance: 1, S0B0Lemma: borç_kal, S0B0LemmaPOS: borç_Verb, S0B0POS: Noun_Verb, S0B0POSLemma: Noun_kal, S0B0Token: borcumuz_kalmayacak, S0B1Lemma: borç_., S0B1LemmaPOS: borç_Punc, S0B1POS: Noun_Punc, S0B1POSLemma: Noun_., S0B1Token: borcumuz_., S0Lemma: borç, S0POS: Noun, S0Token: borcumuz, borç_isGouvernedBy_kal: true, borç_isGouvernedBy_kal_OBJECT: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

212- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [kalmayacak, ., Galatasaray ,.. ]

B0Lemma: kal, B0POS: Verb, B0Token: kalmayacak, B1Lemma: ., B1POS: Punc, B1Token: ., transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

213- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [kalmayacak]   B= [., Galatasaray, Fan ,.. ]

B0Lemma: ., B0POS: Punc, B0Token: ., B1Lemma: Galatasaray, B1POS: Noun, B1Token: Galatasaray, S0B0Distance: 1, S0B0Lemma: kal_., S0B0LemmaPOS: kal_Punc, S0B0POS: Verb_Punc, S0B0POSLemma: Verb_., S0B0Token: kalmayacak_., S0B1Lemma: kal_Galatasaray, S0B1LemmaPOS: kal_Noun, S0B1POS: Verb_Noun, S0B1POSLemma: Verb_Galatasaray, S0B1Token: kalmayacak_Galatasaray, S0Lemma: kal, S0POS: Verb, S0Token: kalmayacak, hasRighDep_PUNCTUATION: true, kal_._hasRighDep_PUNCTUATION: true, kal_hasRighDep_PUNCTUATION: true, kal_isGouvernedBy_art: true, kal_isGouvernedBy_art_COORDINATION: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

214- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [., Galatasaray, Fan ,.. ]

B0Lemma: ., B0POS: Punc, B0Token: ., B1Lemma: Galatasaray, B1POS: Noun, B1Token: Galatasaray, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

215- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [Galatasaray, Fan, Kulüp ,.. ]

B0Lemma: Galatasaray, B0POS: Noun, B0Token: Galatasaray, B1Lemma: fan, B1POS: Noun, B1Token: Fan, S0B0Distance: 1, S0B0Lemma: ._Galatasaray, S0B0LemmaPOS: ._Noun, S0B0POS: Punc_Noun, S0B0POSLemma: Punc_Galatasaray, S0B0Token: ._Galatasaray, S0B1Lemma: ._fan, S0B1LemmaPOS: ._Noun, S0B1POS: Punc_Noun, S0B1POSLemma: Punc_fan, S0B1Token: ._Fan, S0Lemma: ., S0POS: Punc, S0Token: ., transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

216- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Galatasaray, Fan, Kulüp ,.. ]

B0Lemma: Galatasaray, B0POS: Noun, B0Token: Galatasaray, B1Lemma: fan, B1POS: Noun, B1Token: Fan, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

217- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Galatasaray]   B= [Fan, Kulüp, ve ,.. ]

B0Lemma: fan, B0POS: Noun, B0Token: Fan, B1Lemma: kulüp, B1POS: Noun, B1Token: Kulüp, Galatasaray_isGouvernedBy_fan: true, Galatasaray_isGouvernedBy_fan_MWE: true, S0B0Distance: 1, S0B0Lemma: Galatasaray_fan, S0B0LemmaPOS: Galatasaray_Noun, S0B0POS: Noun_Noun, S0B0POSLemma: Noun_fan, S0B0Token: Galatasaray_Fan, S0B1Lemma: Galatasaray_kulüp, S0B1LemmaPOS: Galatasaray_Noun, S0B1POS: Noun_Noun, S0B1POSLemma: Noun_kulüp, S0B1Token: Galatasaray_Kulüp, S0Lemma: Galatasaray, S0POS: Noun, S0Token: Galatasaray, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

218- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Fan, Kulüp, ve ,.. ]

B0Lemma: fan, B0POS: Noun, B0Token: Fan, B1Lemma: kulüp, B1POS: Noun, B1Token: Kulüp, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

219- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Fan]   B= [Kulüp, ve, master ,.. ]

B0Lemma: kulüp, B0POS: Noun, B0Token: Kulüp, B1Lemma: ve, B1POS: Conj, B1Token: ve, S0B0Distance: 1, S0B0Lemma: fan_kulüp, S0B0LemmaPOS: fan_Noun, S0B0POS: Noun_Noun, S0B0POSLemma: Noun_kulüp, S0B0Token: Fan_Kulüp, S0B1Lemma: fan_ve, S0B1LemmaPOS: fan_Conj, S0B1POS: Noun_Conj, S0B1POSLemma: Noun_ve, S0B1Token: Fan_ve, S0Lemma: fan, S0POS: Noun, S0Token: Fan, fan_isGouvernedBy_kart: true, fan_isGouvernedBy_kart_POSSESSOR: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

220- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Kulüp, ve, master ,.. ]

B0Lemma: kulüp, B0POS: Noun, B0Token: Kulüp, B1Lemma: ve, B1POS: Conj, B1Token: ve, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

221- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Kulüp]   B= [ve, master, Card ,.. ]

B0Lemma: ve, B0POS: Conj, B0Token: ve, B1Lemma: master, B1POS: Noun, B1Token: master, S0B0Distance: 1, S0B0Lemma: kulüp_ve, S0B0LemmaPOS: kulüp_Conj, S0B0POS: Noun_Conj, S0B0POSLemma: Noun_ve, S0B0Token: Kulüp_ve, S0B1Lemma: kulüp_master, S0B1LemmaPOS: kulüp_Noun, S0B1POS: Noun_Noun, S0B1POSLemma: Noun_master, S0B1Token: Kulüp_master, S0Lemma: kulüp, S0POS: Noun, S0Token: Kulüp, hasRighDep_CONJUNCTION: true, kulüp_hasRighDep_CONJUNCTION: true, kulüp_isGouvernedBy_master: true, kulüp_isGouvernedBy_master_COORDINATION: true, kulüp_ve_hasRighDep_CONJUNCTION: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

222- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ve, master, Card ,.. ]

B0Lemma: ve, B0POS: Conj, B0Token: ve, B1Lemma: master, B1POS: Noun, B1Token: master, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

223- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ve]   B= [master, Card, ile ,.. ]

B0Lemma: master, B0POS: Noun, B0Token: master, B1Lemma: Card, B1POS: Noun, B1Token: Card, S0B0Distance: 1, S0B0Lemma: ve_master, S0B0LemmaPOS: ve_Noun, S0B0POS: Conj_Noun, S0B0POSLemma: Conj_master, S0B0Token: ve_master, S0B1Lemma: ve_Card, S0B1LemmaPOS: ve_Noun, S0B1POS: Conj_Noun, S0B1POSLemma: Conj_Card, S0B1Token: ve_Card, S0Lemma: ve, S0POS: Conj, S0Token: ve, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

224- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [master, Card, ile ,.. ]

B0Lemma: master, B0POS: Noun, B0Token: master, B1Lemma: Card, B1POS: Noun, B1Token: Card, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

225- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [master]   B= [Card, ile, _ ,.. ]

B0Lemma: Card, B0POS: Noun, B0Token: Card, B1Lemma: ile, B1POS: Conj, B1Token: ile, S0B0Distance: 1, S0B0Lemma: master_Card, S0B0LemmaPOS: master_Noun, S0B0POS: Noun_Noun, S0B0POSLemma: Noun_Card, S0B0Token: master_Card, S0B1Lemma: master_ile, S0B1LemmaPOS: master_Conj, S0B1POS: Noun_Conj, S0B1POSLemma: Noun_ile, S0B1Token: master_ile, S0Lemma: master, S0POS: Noun, S0Token: master, master_isGouvernedBy_Card: true, master_isGouvernedBy_Card_MODIFIER: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

226- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Card, ile, _ ,.. ]

B0Lemma: Card, B0POS: Noun, B0Token: Card, B1Lemma: ile, B1POS: Conj, B1Token: ile, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

227- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Card]   B= [ile, _, yaptığımız ,.. ]

B0Lemma: ile, B0POS: Conj, B0Token: ile, B1Lemma: yap, B1POS: Verb, B1Token: _, Card_isGouvernedBy_ile: true, Card_isGouvernedBy_ile_ARGUMENT: true, S0B0Distance: 1, S0B0Lemma: Card_ile, S0B0LemmaPOS: Card_Conj, S0B0POS: Noun_Conj, S0B0POSLemma: Noun_ile, S0B0Token: Card_ile, S0B1Lemma: Card_yap, S0B1LemmaPOS: Card_Verb, S0B1POS: Noun_Verb, S0B1POSLemma: Noun_yap, S0B1Token: Card__, S0Lemma: Card, S0POS: Noun, S0Token: Card, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

228- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ile, _, yaptığımız ,.. ]

B0Lemma: ile, B0POS: Conj, B0Token: ile, B1Lemma: yap, B1POS: Verb, B1Token: _, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

229- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ile]   B= [_, yaptığımız, anlaşmayla ,.. ]

B0Lemma: yap, B0POS: Verb, B0Token: _, B1Lemma: _, B1POS: Adj, B1Token: yaptığımız, S0B0Distance: 1, S0B0Lemma: ile_yap, S0B0LemmaPOS: ile_Verb, S0B0POS: Conj_Verb, S0B0POSLemma: Conj_yap, S0B0Token: ile__, S0B1Lemma: ile__, S0B1LemmaPOS: ile_Adj, S0B1POS: Conj_Adj, S0B1POSLemma: Conj__, S0B1Token: ile_yaptığımız, S0Lemma: ile, S0POS: Conj, S0Token: ile, ile_isGouvernedBy_yap: true, ile_isGouvernedBy_yap_MODIFIER: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

230- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [_, yaptığımız, anlaşmayla ,.. ]

B0Lemma: yap, B0POS: Verb, B0Token: _, B1Lemma: _, B1POS: Adj, B1Token: yaptığımız, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

231- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [_]   B= [yaptığımız, anlaşmayla, _ ,.. ]

B0Lemma: _, B0POS: Adj, B0Token: yaptığımız, B1Lemma: anlaşma, B1POS: Noun, B1Token: anlaşmayla, S0B0Distance: 1, S0B0Lemma: yap__, S0B0LemmaPOS: yap_Adj, S0B0POS: Verb_Adj, S0B0POSLemma: Verb__, S0B0Token: __yaptığımız, S0B1Lemma: yap_anlaşma, S0B1LemmaPOS: yap_Noun, S0B1POS: Verb_Noun, S0B1POSLemma: Verb_anlaşma, S0B1Token: __anlaşmayla, S0Lemma: yap, S0POS: Verb, S0Token: _, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, yap_isGouvernedBy__: true, yap_isGouvernedBy___DERIV: true, 

232- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [yaptığımız, anlaşmayla, _ ,.. ]

B0Lemma: _, B0POS: Adj, B0Token: yaptığımız, B1Lemma: anlaşma, B1POS: Noun, B1Token: anlaşmayla, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

233- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [yaptığımız]   B= [anlaşmayla, _, gerçekleşecek ,.. ]

B0Lemma: anlaşma, B0POS: Noun, B0Token: anlaşmayla, B1Lemma: gerçekleş, B1POS: Verb, B1Token: _, S0B0Distance: 1, S0B0Lemma: __anlaşma, S0B0LemmaPOS: __Noun, S0B0POS: Adj_Noun, S0B0POSLemma: Adj_anlaşma, S0B0Token: yaptığımız_anlaşmayla, S0B1Lemma: __gerçekleş, S0B1LemmaPOS: __Verb, S0B1POS: Adj_Verb, S0B1POSLemma: Adj_gerçekleş, S0B1Token: yaptığımız__, S0Lemma: _, S0POS: Adj, S0Token: yaptığımız, __isGouvernedBy_anlaşma: true, __isGouvernedBy_anlaşma_MODIFIER: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

234- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [anlaşmayla, _, gerçekleşecek ,.. ]

B0Lemma: anlaşma, B0POS: Noun, B0Token: anlaşmayla, B1Lemma: gerçekleş, B1POS: Verb, B1Token: _, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

235- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [anlaşmayla]   B= [_, gerçekleşecek, kredi ,.. ]

B0Lemma: gerçekleş, B0POS: Verb, B0Token: _, B1Lemma: _, B1POS: Adj, B1Token: gerçekleşecek, S0B0Distance: 1, S0B0Lemma: anlaşma_gerçekleş, S0B0LemmaPOS: anlaşma_Verb, S0B0POS: Noun_Verb, S0B0POSLemma: Noun_gerçekleş, S0B0Token: anlaşmayla__, S0B1Lemma: anlaşma__, S0B1LemmaPOS: anlaşma_Adj, S0B1POS: Noun_Adj, S0B1POSLemma: Noun__, S0B1Token: anlaşmayla_gerçekleşecek, S0Lemma: anlaşma, S0POS: Noun, S0Token: anlaşmayla, anlaşma_isGouvernedBy_gerçekleş: true, anlaşma_isGouvernedBy_gerçekleş_MODIFIER: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

236- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [_, gerçekleşecek, kredi ,.. ]

B0Lemma: gerçekleş, B0POS: Verb, B0Token: _, B1Lemma: _, B1POS: Adj, B1Token: gerçekleşecek, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

237- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [_]   B= [gerçekleşecek, kredi, kartı ,.. ]

B0Lemma: _, B0POS: Adj, B0Token: gerçekleşecek, B1Lemma: kredi, B1POS: Noun, B1Token: kredi, S0B0Distance: 1, S0B0Lemma: gerçekleş__, S0B0LemmaPOS: gerçekleş_Adj, S0B0POS: Verb_Adj, S0B0POSLemma: Verb__, S0B0Token: __gerçekleşecek, S0B1Lemma: gerçekleş_kredi, S0B1LemmaPOS: gerçekleş_Noun, S0B1POS: Verb_Noun, S0B1POSLemma: Verb_kredi, S0B1Token: __kredi, S0Lemma: gerçekleş, S0POS: Verb, S0Token: _, gerçekleş_isGouvernedBy__: true, gerçekleş_isGouvernedBy___DERIV: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

238- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [gerçekleşecek, kredi, kartı ,.. ]

B0Lemma: _, B0POS: Adj, B0Token: gerçekleşecek, B1Lemma: kredi, B1POS: Noun, B1Token: kredi, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

239- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [gerçekleşecek]   B= [kredi, kartı, ek ,.. ]

B0Lemma: kredi, B0POS: Noun, B0Token: kredi, B1Lemma: kart, B1POS: Noun, B1Token: kartı, S0B0Distance: 1, S0B0Lemma: __kredi, S0B0LemmaPOS: __Noun, S0B0POS: Adj_Noun, S0B0POSLemma: Adj_kredi, S0B0Token: gerçekleşecek_kredi, S0B1Lemma: __kart, S0B1LemmaPOS: __Noun, S0B1POS: Adj_Noun, S0B1POSLemma: Adj_kart, S0B1Token: gerçekleşecek_kartı, S0Lemma: _, S0POS: Adj, S0Token: gerçekleşecek, __isGouvernedBy_kredi: true, __isGouvernedBy_kredi_MODIFIER: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

240- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [kredi, kartı, ek ,.. ]

B0Lemma: kredi, B0POS: Noun, B0Token: kredi, B1Lemma: kart, B1POS: Noun, B1Token: kartı, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

241- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [kredi]   B= [kartı, ek, gelirlerimizi ,.. ]

B0Lemma: kart, B0POS: Noun, B0Token: kartı, B1Lemma: ek, B1POS: Adj, B1Token: ek, S0B0Distance: 1, S0B0Lemma: kredi_kart, S0B0LemmaPOS: kredi_Noun, S0B0POS: Noun_Noun, S0B0POSLemma: Noun_kart, S0B0Token: kredi_kartı, S0B1Lemma: kredi_ek, S0B1LemmaPOS: kredi_Adj, S0B1POS: Noun_Adj, S0B1POSLemma: Noun_ek, S0B1Token: kredi_ek, S0Lemma: kredi, S0POS: Noun, S0Token: kredi, kredi_isGouvernedBy_kart: true, kredi_isGouvernedBy_kart_MODIFIER: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

242- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [kartı, ek, gelirlerimizi ,.. ]

B0Lemma: kart, B0POS: Noun, B0Token: kartı, B1Lemma: ek, B1POS: Adj, B1Token: ek, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

243- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [kartı]   B= [ek, gelirlerimizi, arttıracak ,.. ]

B0Lemma: ek, B0POS: Adj, B0Token: ek, B1Lemma: gelir, B1POS: Noun, B1Token: gelirlerimizi, S0B0Distance: 1, S0B0Lemma: kart_ek, S0B0LemmaPOS: kart_Adj, S0B0POS: Noun_Adj, S0B0POSLemma: Noun_ek, S0B0Token: kartı_ek, S0B1Lemma: kart_gelir, S0B1LemmaPOS: kart_Noun, S0B1POS: Noun_Noun, S0B1POSLemma: Noun_gelir, S0B1Token: kartı_gelirlerimizi, S0Lemma: kart, S0POS: Noun, S0Token: kartı, kart_isGouvernedBy_art: true, kart_isGouvernedBy_art_SUBJECT: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

244- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ek, gelirlerimizi, arttıracak ,.. ]

B0Lemma: ek, B0POS: Adj, B0Token: ek, B1Lemma: gelir, B1POS: Noun, B1Token: gelirlerimizi, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

245- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ek]   B= [gelirlerimizi, arttıracak, . ,.. ]

B0Lemma: gelir, B0POS: Noun, B0Token: gelirlerimizi, B1Lemma: art, B1POS: Verb, B1Token: arttıracak, S0B0Distance: 1, S0B0Lemma: ek_gelir, S0B0LemmaPOS: ek_Noun, S0B0POS: Adj_Noun, S0B0POSLemma: Adj_gelir, S0B0Token: ek_gelirlerimizi, S0B1Lemma: ek_art, S0B1LemmaPOS: ek_Verb, S0B1POS: Adj_Verb, S0B1POSLemma: Adj_art, S0B1Token: ek_arttıracak, S0Lemma: ek, S0POS: Adj, S0Token: ek, ek_isGouvernedBy_gelir: true, ek_isGouvernedBy_gelir_MODIFIER: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

246- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [gelirlerimizi, arttıracak, . ,.. ]

B0Lemma: gelir, B0POS: Noun, B0Token: gelirlerimizi, B1Lemma: art, B1POS: Verb, B1Token: arttıracak, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

247- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [gelirlerimizi]   B= [arttıracak, ., Bir ,.. ]

B0Lemma: art, B0POS: Verb, B0Token: arttıracak, B1Lemma: ., B1POS: Punc, B1Token: ., S0B0Distance: 1, S0B0Lemma: gelir_art, S0B0LemmaPOS: gelir_Verb, S0B0POS: Noun_Verb, S0B0POSLemma: Noun_art, S0B0Token: gelirlerimizi_arttıracak, S0B1Lemma: gelir_., S0B1LemmaPOS: gelir_Punc, S0B1POS: Noun_Punc, S0B1POSLemma: Noun_., S0B1Token: gelirlerimizi_., S0Lemma: gelir, S0POS: Noun, S0Token: gelirlerimizi, gelir_isGouvernedBy_art: true, gelir_isGouvernedBy_art_OBJECT: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

248- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [arttıracak, ., Bir ,.. ]

B0Lemma: art, B0POS: Verb, B0Token: arttıracak, B1Lemma: ., B1POS: Punc, B1Token: ., transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

249- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [arttıracak]   B= [., Bir, şirket ,.. ]

B0Lemma: ., B0POS: Punc, B0Token: ., B1Lemma: bir, B1POS: Adj, B1Token: Bir, S0B0Distance: 1, S0B0Lemma: art_., S0B0LemmaPOS: art_Punc, S0B0POS: Verb_Punc, S0B0POSLemma: Verb_., S0B0Token: arttıracak_., S0B1Lemma: art_bir, S0B1LemmaPOS: art_Adj, S0B1POS: Verb_Adj, S0B1POSLemma: Verb_bir, S0B1Token: arttıracak_Bir, S0Lemma: art, S0POS: Verb, S0Token: arttıracak, art_._hasRighDep_PUNCTUATION: true, art_hasRighDep_PUNCTUATION: true, art_isGouvernedBy_ol: true, art_isGouvernedBy_ol_COORDINATION: true, hasRighDep_PUNCTUATION: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

250- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [., Bir, şirket ,.. ]

B0Lemma: ., B0POS: Punc, B0Token: ., B1Lemma: bir, B1POS: Adj, B1Token: Bir, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

251- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [Bir, şirket, oluyoruz ,.. ]

B0Lemma: bir, B0POS: Adj, B0Token: Bir, B1Lemma: şirket, B1POS: Noun, B1Token: şirket, S0B0Distance: 1, S0B0Lemma: ._bir, S0B0LemmaPOS: ._Adj, S0B0POS: Punc_Adj, S0B0POSLemma: Punc_bir, S0B0Token: ._Bir, S0B1Lemma: ._şirket, S0B1LemmaPOS: ._Noun, S0B1POS: Punc_Noun, S0B1POSLemma: Punc_şirket, S0B1Token: ._şirket, S0Lemma: ., S0POS: Punc, S0Token: ., transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

252- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Bir, şirket, oluyoruz ,.. ]

B0Lemma: bir, B0POS: Adj, B0Token: Bir, B1Lemma: şirket, B1POS: Noun, B1Token: şirket, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

253- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Bir]   B= [şirket, oluyoruz, ve ,.. ]

B0Lemma: şirket, B0POS: Noun, B0Token: şirket, B1Lemma: ol, B1POS: Verb, B1Token: oluyoruz, S0B0Distance: 1, S0B0Lemma: bir_şirket, S0B0LemmaPOS: bir_Noun, S0B0POS: Adj_Noun, S0B0POSLemma: Adj_şirket, S0B0Token: Bir_şirket, S0B1Lemma: bir_ol, S0B1LemmaPOS: bir_Verb, S0B1POS: Adj_Verb, S0B1POSLemma: Adj_ol, S0B1Token: Bir_oluyoruz, S0Lemma: bir, S0POS: Adj, S0Token: Bir, bir_isGouvernedBy_şirket: true, bir_isGouvernedBy_şirket_DETERMINER: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

254- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [şirket, oluyoruz, ve ,.. ]

B0Lemma: şirket, B0POS: Noun, B0Token: şirket, B1Lemma: ol, B1POS: Verb, B1Token: oluyoruz, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

255- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [şirket]   B= [oluyoruz, ve, bunu ,.. ]

B0Lemma: ol, B0POS: Verb, B0Token: oluyoruz, B1Lemma: ve, B1POS: Conj, B1Token: ve, S0B0Distance: 1, S0B0Lemma: şirket_ol, S0B0LemmaPOS: şirket_Verb, S0B0POS: Noun_Verb, S0B0POSLemma: Noun_ol, S0B0Token: şirket_oluyoruz, S0B1Lemma: şirket_ve, S0B1LemmaPOS: şirket_Conj, S0B1POS: Noun_Conj, S0B1POSLemma: Noun_ve, S0B1Token: şirket_ve, S0Lemma: şirket, S0POS: Noun, S0Token: şirket, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, şirket_isGouvernedBy_ol: true, şirket_isGouvernedBy_ol_OBJECT: true, 

256- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [oluyoruz, ve, bunu ,.. ]

B0Lemma: ol, B0POS: Verb, B0Token: oluyoruz, B1Lemma: ve, B1POS: Conj, B1Token: ve, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

257- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [oluyoruz]   B= [ve, bunu, halka ,.. ]

B0Lemma: ve, B0POS: Conj, B0Token: ve, B1Lemma: bu, B1POS: Pron, B1Token: bunu, S0B0Distance: 1, S0B0Lemma: ol_ve, S0B0LemmaPOS: ol_Conj, S0B0POS: Verb_Conj, S0B0POSLemma: Verb_ve, S0B0Token: oluyoruz_ve, S0B1Lemma: ol_bu, S0B1LemmaPOS: ol_Pron, S0B1POS: Verb_Pron, S0B1POSLemma: Verb_bu, S0B1Token: oluyoruz_bunu, S0Lemma: ol, S0POS: Verb, S0Token: oluyoruz, hasRighDep_CONJUNCTION: true, ol_hasRighDep_CONJUNCTION: true, ol_isGouvernedBy_gir: true, ol_isGouvernedBy_gir_COORDINATION: true, ol_ve_hasRighDep_CONJUNCTION: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

258- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ve, bunu, halka ,.. ]

B0Lemma: ve, B0POS: Conj, B0Token: ve, B1Lemma: bu, B1POS: Pron, B1Token: bunu, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

259- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ve]   B= [bunu, halka, _ ,.. ]

B0Lemma: bu, B0POS: Pron, B0Token: bunu, B1Lemma: halk, B1POS: Noun, B1Token: halka, S0B0Distance: 1, S0B0Lemma: ve_bu, S0B0LemmaPOS: ve_Pron, S0B0POS: Conj_Pron, S0B0POSLemma: Conj_bu, S0B0Token: ve_bunu, S0B1Lemma: ve_halk, S0B1LemmaPOS: ve_Noun, S0B1POS: Conj_Noun, S0B1POSLemma: Conj_halk, S0B1Token: ve_halka, S0Lemma: ve, S0POS: Conj, S0Token: ve, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

260- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [bunu, halka, _ ,.. ]

B0Lemma: bu, B0POS: Pron, B0Token: bunu, B1Lemma: halk, B1POS: Noun, B1Token: halka, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

261- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [bunu]   B= [halka, _, açarak ,.. ]

B0Lemma: halk, B0POS: Noun, B0Token: halka, B1Lemma: aç, B1POS: Verb, B1Token: _, S0B0Distance: 1, S0B0Lemma: bu_halk, S0B0LemmaPOS: bu_Noun, S0B0POS: Pron_Noun, S0B0POSLemma: Pron_halk, S0B0Token: bunu_halka, S0B1Lemma: bu_aç, S0B1LemmaPOS: bu_Verb, S0B1POS: Pron_Verb, S0B1POSLemma: Pron_aç, S0B1Token: bunu__, S0Lemma: bu, S0POS: Pron, S0Token: bunu, bu_isGouvernedBy_aç: true, bu_isGouvernedBy_aç_OBJECT: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

262- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [halka, _, açarak ,.. ]

B0Lemma: halk, B0POS: Noun, B0Token: halka, B1Lemma: aç, B1POS: Verb, B1Token: _, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

263- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [halka]   B= [_, açarak, borsaya ,.. ]

B0Lemma: aç, B0POS: Verb, B0Token: _, B1Lemma: _, B1POS: Adverb, B1Token: açarak, S0B0Distance: 1, S0B0Lemma: halk_aç, S0B0LemmaPOS: halk_Verb, S0B0POS: Noun_Verb, S0B0POSLemma: Noun_aç, S0B0Token: halka__, S0B1Lemma: halk__, S0B1LemmaPOS: halk_Adverb, S0B1POS: Noun_Adverb, S0B1POSLemma: Noun__, S0B1Token: halka_açarak, S0Lemma: halk, S0POS: Noun, S0Token: halka, halk_isGouvernedBy_aç: true, halk_isGouvernedBy_aç_MODIFIER: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

264- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [_, açarak, borsaya ,.. ]

B0Lemma: aç, B0POS: Verb, B0Token: _, B1Lemma: _, B1POS: Adverb, B1Token: açarak, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

265- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [_]   B= [açarak, borsaya, da ,.. ]

B0Lemma: _, B0POS: Adverb, B0Token: açarak, B1Lemma: borsa, B1POS: Noun, B1Token: borsaya, S0B0Distance: 1, S0B0Lemma: aç__, S0B0LemmaPOS: aç_Adverb, S0B0POS: Verb_Adverb, S0B0POSLemma: Verb__, S0B0Token: __açarak, S0B1Lemma: aç_borsa, S0B1LemmaPOS: aç_Noun, S0B1POS: Verb_Noun, S0B1POSLemma: Verb_borsa, S0B1Token: __borsaya, S0Lemma: aç, S0POS: Verb, S0Token: _, aç_isGouvernedBy__: true, aç_isGouvernedBy___DERIV: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

266- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [açarak, borsaya, da ,.. ]

B0Lemma: _, B0POS: Adverb, B0Token: açarak, B1Lemma: borsa, B1POS: Noun, B1Token: borsaya, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

267- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [açarak]   B= [borsaya, da, gireceğiz ,.. ]

B0Lemma: borsa, B0POS: Noun, B0Token: borsaya, B1Lemma: da, B1POS: Conj, B1Token: da, S0B0Distance: 1, S0B0Lemma: __borsa, S0B0LemmaPOS: __Noun, S0B0POS: Adverb_Noun, S0B0POSLemma: Adverb_borsa, S0B0Token: açarak_borsaya, S0B1Lemma: __da, S0B1LemmaPOS: __Conj, S0B1POS: Adverb_Conj, S0B1POSLemma: Adverb_da, S0B1Token: açarak_da, S0Lemma: _, S0POS: Adverb, S0Token: açarak, __isGouvernedBy_gir: true, __isGouvernedBy_gir_MODIFIER: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

268- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [borsaya, da, gireceğiz ,.. ]

B0Lemma: borsa, B0POS: Noun, B0Token: borsaya, B1Lemma: da, B1POS: Conj, B1Token: da, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

269- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [borsaya]   B= [da, gireceğiz, . ,.. ]

B0Lemma: da, B0POS: Conj, B0Token: da, B1Lemma: gir, B1POS: Verb, B1Token: gireceğiz, S0B0Distance: 1, S0B0Lemma: borsa_da, S0B0LemmaPOS: borsa_Conj, S0B0POS: Noun_Conj, S0B0POSLemma: Noun_da, S0B0Token: borsaya_da, S0B1Lemma: borsa_gir, S0B1LemmaPOS: borsa_Verb, S0B1POS: Noun_Verb, S0B1POSLemma: Noun_gir, S0B1Token: borsaya_gireceğiz, S0Lemma: borsa, S0POS: Noun, S0Token: borsaya, borsa_da_hasRighDep_INTENSIFIER: true, borsa_hasRighDep_INTENSIFIER: true, borsa_isGouvernedBy_gir: true, borsa_isGouvernedBy_gir_MODIFIER: true, hasRighDep_INTENSIFIER: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

270- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [da, gireceğiz, . ,.. ]

B0Lemma: da, B0POS: Conj, B0Token: da, B1Lemma: gir, B1POS: Verb, B1Token: gireceğiz, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

271- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [da]   B= [gireceğiz, ., Markamızın ,.. ]

B0Lemma: gir, B0POS: Verb, B0Token: gireceğiz, B1Lemma: ., B1POS: Punc, B1Token: ., S0B0Distance: 1, S0B0Lemma: da_gir, S0B0LemmaPOS: da_Verb, S0B0POS: Conj_Verb, S0B0POSLemma: Conj_gir, S0B0Token: da_gireceğiz, S0B1Lemma: da_., S0B1LemmaPOS: da_Punc, S0B1POS: Conj_Punc, S0B1POSLemma: Conj_., S0B1Token: da_., S0Lemma: da, S0POS: Conj, S0Token: da, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

272- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [gireceğiz, ., Markamızın ,.. ]

B0Lemma: gir, B0POS: Verb, B0Token: gireceğiz, B1Lemma: ., B1POS: Punc, B1Token: ., transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

273- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [gireceğiz]   B= [., Markamızın, patentini ,.. ]

B0Lemma: ., B0POS: Punc, B0Token: ., B1Lemma: marka, B1POS: Noun, B1Token: Markamızın, S0B0Distance: 1, S0B0Lemma: gir_., S0B0LemmaPOS: gir_Punc, S0B0POS: Verb_Punc, S0B0POSLemma: Verb_., S0B0Token: gireceğiz_., S0B1Lemma: gir_marka, S0B1LemmaPOS: gir_Noun, S0B1POS: Verb_Noun, S0B1POSLemma: Verb_marka, S0B1Token: gireceğiz_Markamızın, S0Lemma: gir, S0POS: Verb, S0Token: gireceğiz, gir_._hasRighDep_PUNCTUATION: true, gir_hasRighDep_PUNCTUATION: true, gir_isGouvernedBy_pazarla: true, gir_isGouvernedBy_pazarla_COORDINATION: true, hasRighDep_PUNCTUATION: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

274- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [., Markamızın, patentini ,.. ]

B0Lemma: ., B0POS: Punc, B0Token: ., B1Lemma: marka, B1POS: Noun, B1Token: Markamızın, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

275- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [Markamızın, patentini, _ ,.. ]

B0Lemma: marka, B0POS: Noun, B0Token: Markamızın, B1Lemma: patent, B1POS: Noun, B1Token: patentini, S0B0Distance: 1, S0B0Lemma: ._marka, S0B0LemmaPOS: ._Noun, S0B0POS: Punc_Noun, S0B0POSLemma: Punc_marka, S0B0Token: ._Markamızın, S0B1Lemma: ._patent, S0B1LemmaPOS: ._Noun, S0B1POS: Punc_Noun, S0B1POSLemma: Punc_patent, S0B1Token: ._patentini, S0Lemma: ., S0POS: Punc, S0Token: ., transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

276- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Markamızın, patentini, _ ,.. ]

B0Lemma: marka, B0POS: Noun, B0Token: Markamızın, B1Lemma: patent, B1POS: Noun, B1Token: patentini, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

277- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Markamızın]   B= [patentini, _, alıp ,.. ]

B0Lemma: patent, B0POS: Noun, B0Token: patentini, B1Lemma: al, B1POS: Verb, B1Token: _, S0B0Distance: 1, S0B0Lemma: marka_patent, S0B0LemmaPOS: marka_Noun, S0B0POS: Noun_Noun, S0B0POSLemma: Noun_patent, S0B0Token: Markamızın_patentini, S0B1Lemma: marka_al, S0B1LemmaPOS: marka_Verb, S0B1POS: Noun_Verb, S0B1POSLemma: Noun_al, S0B1Token: Markamızın__, S0Lemma: marka, S0POS: Noun, S0Token: Markamızın, marka_isGouvernedBy_patent: true, marka_isGouvernedBy_patent_POSSESSOR: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

278- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [patentini, _, alıp ,.. ]

B0Lemma: patent, B0POS: Noun, B0Token: patentini, B1Lemma: al, B1POS: Verb, B1Token: _, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

279- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [patentini]   B= [_, alıp, , ,.. ]

B0Lemma: al, B0POS: Verb, B0Token: _, B1Lemma: _, B1POS: Adverb, B1Token: alıp, S0B0Distance: 1, S0B0Lemma: patent_al, S0B0LemmaPOS: patent_Verb, S0B0POS: Noun_Verb, S0B0POSLemma: Noun_al, S0B0Token: patentini__, S0B1Lemma: patent__, S0B1LemmaPOS: patent_Adverb, S0B1POS: Noun_Adverb, S0B1POSLemma: Noun__, S0B1Token: patentini_alıp, S0Lemma: patent, S0POS: Noun, S0Token: patentini, patent_isGouvernedBy_al: true, patent_isGouvernedBy_al_OBJECT: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

280- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [_, alıp, , ,.. ]

B0Lemma: al, B0POS: Verb, B0Token: _, B1Lemma: _, B1POS: Adverb, B1Token: alıp, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

281- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [_]   B= [alıp, ,, promosyonlarımızı ,.. ]

B0Lemma: _, B0POS: Adverb, B0Token: alıp, B1Lemma: ,, B1POS: Punc, B1Token: ,, S0B0Distance: 1, S0B0Lemma: al__, S0B0LemmaPOS: al_Adverb, S0B0POS: Verb_Adverb, S0B0POSLemma: Verb__, S0B0Token: __alıp, S0B1Lemma: al_,, S0B1LemmaPOS: al_Punc, S0B1POS: Verb_Punc, S0B1POSLemma: Verb_,, S0B1Token: __,, S0Lemma: al, S0POS: Verb, S0Token: _, al_isGouvernedBy__: true, al_isGouvernedBy___DERIV: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

282- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [alıp, ,, promosyonlarımızı ,.. ]

B0Lemma: _, B0POS: Adverb, B0Token: alıp, B1Lemma: ,, B1POS: Punc, B1Token: ,, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

283- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [alıp]   B= [,, promosyonlarımızı, pazarlayacağız ,.. ]

B0Lemma: ,, B0POS: Punc, B0Token: ,, B1Lemma: promosyon, B1POS: Noun, B1Token: promosyonlarımızı, S0B0Distance: 1, S0B0Lemma: __,, S0B0LemmaPOS: __Punc, S0B0POS: Adverb_Punc, S0B0POSLemma: Adverb_,, S0B0Token: alıp_,, S0B1Lemma: __promosyon, S0B1LemmaPOS: __Noun, S0B1POS: Adverb_Noun, S0B1POSLemma: Adverb_promosyon, S0B1Token: alıp_promosyonlarımızı, S0Lemma: _, S0POS: Adverb, S0Token: alıp, __,_hasRighDep_PUNCTUATION: true, __hasRighDep_PUNCTUATION: true, __isGouvernedBy_pazarla: true, __isGouvernedBy_pazarla_MODIFIER: true, hasRighDep_PUNCTUATION: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

284- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, promosyonlarımızı, pazarlayacağız ,.. ]

B0Lemma: ,, B0POS: Punc, B0Token: ,, B1Lemma: promosyon, B1POS: Noun, B1Token: promosyonlarımızı, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

285- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [promosyonlarımızı, pazarlayacağız, . ,.. ]

B0Lemma: promosyon, B0POS: Noun, B0Token: promosyonlarımızı, B1Lemma: pazarla, B1POS: Verb, B1Token: pazarlayacağız, S0B0Distance: 1, S0B0Lemma: ,_promosyon, S0B0LemmaPOS: ,_Noun, S0B0POS: Punc_Noun, S0B0POSLemma: Punc_promosyon, S0B0Token: ,_promosyonlarımızı, S0B1Lemma: ,_pazarla, S0B1LemmaPOS: ,_Verb, S0B1POS: Punc_Verb, S0B1POSLemma: Punc_pazarla, S0B1Token: ,_pazarlayacağız, S0Lemma: ,, S0POS: Punc, S0Token: ,, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

286- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [promosyonlarımızı, pazarlayacağız, . ,.. ]

B0Lemma: promosyon, B0POS: Noun, B0Token: promosyonlarımızı, B1Lemma: pazarla, B1POS: Verb, B1Token: pazarlayacağız, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

287- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [promosyonlarımızı]   B= [pazarlayacağız, ., Amerika'da ,.. ]

B0Lemma: pazarla, B0POS: Verb, B0Token: pazarlayacağız, B1Lemma: ., B1POS: Punc, B1Token: ., S0B0Distance: 1, S0B0Lemma: promosyon_pazarla, S0B0LemmaPOS: promosyon_Verb, S0B0POS: Noun_Verb, S0B0POSLemma: Noun_pazarla, S0B0Token: promosyonlarımızı_pazarlayacağız, S0B1Lemma: promosyon_., S0B1LemmaPOS: promosyon_Punc, S0B1POS: Noun_Punc, S0B1POSLemma: Noun_., S0B1Token: promosyonlarımızı_., S0Lemma: promosyon, S0POS: Noun, S0Token: promosyonlarımızı, promosyon_isGouvernedBy_pazarla: true, promosyon_isGouvernedBy_pazarla_OBJECT: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

288- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [pazarlayacağız, ., Amerika'da ,.. ]

B0Lemma: pazarla, B0POS: Verb, B0Token: pazarlayacağız, B1Lemma: ., B1POS: Punc, B1Token: ., transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

289- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [pazarlayacağız]   B= [., Amerika'da, _ ,.. ]

B0Lemma: ., B0POS: Punc, B0Token: ., B1Lemma: Amerika, B1POS: Noun, B1Token: Amerika'da, S0B0Distance: 1, S0B0Lemma: pazarla_., S0B0LemmaPOS: pazarla_Punc, S0B0POS: Verb_Punc, S0B0POSLemma: Verb_., S0B0Token: pazarlayacağız_., S0B1Lemma: pazarla_Amerika, S0B1LemmaPOS: pazarla_Noun, S0B1POS: Verb_Noun, S0B1POSLemma: Verb_Amerika, S0B1Token: pazarlayacağız_Amerika'da, S0Lemma: pazarla, S0POS: Verb, S0Token: pazarlayacağız, hasRighDep_PUNCTUATION: true, pazarla_._hasRighDep_PUNCTUATION: true, pazarla_hasRighDep_PUNCTUATION: true, pazarla_isGouvernedBy_hazırla: true, pazarla_isGouvernedBy_hazırla_COORDINATION: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

290- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [., Amerika'da, _ ,.. ]

B0Lemma: ., B0POS: Punc, B0Token: ., B1Lemma: Amerika, B1POS: Noun, B1Token: Amerika'da, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

291- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [Amerika'da, _, anlaştığımız ,.. ]

B0Lemma: Amerika, B0POS: Noun, B0Token: Amerika'da, B1Lemma: anlaş, B1POS: Verb, B1Token: _, S0B0Distance: 1, S0B0Lemma: ._Amerika, S0B0LemmaPOS: ._Noun, S0B0POS: Punc_Noun, S0B0POSLemma: Punc_Amerika, S0B0Token: ._Amerika'da, S0B1Lemma: ._anlaş, S0B1LemmaPOS: ._Verb, S0B1POS: Punc_Verb, S0B1POSLemma: Punc_anlaş, S0B1Token: .__, S0Lemma: ., S0POS: Punc, S0Token: ., transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

292- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Amerika'da, _, anlaştığımız ,.. ]

B0Lemma: Amerika, B0POS: Noun, B0Token: Amerika'da, B1Lemma: anlaş, B1POS: Verb, B1Token: _, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

293- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Amerika'da]   B= [_, anlaştığımız, bir ,.. ]

Amerika_isGouvernedBy_anlaş: true, Amerika_isGouvernedBy_anlaş_MODIFIER: true, B0Lemma: anlaş, B0POS: Verb, B0Token: _, B1Lemma: _, B1POS: Adj, B1Token: anlaştığımız, S0B0Distance: 1, S0B0Lemma: Amerika_anlaş, S0B0LemmaPOS: Amerika_Verb, S0B0POS: Noun_Verb, S0B0POSLemma: Noun_anlaş, S0B0Token: Amerika'da__, S0B1Lemma: Amerika__, S0B1LemmaPOS: Amerika_Adj, S0B1POS: Noun_Adj, S0B1POSLemma: Noun__, S0B1Token: Amerika'da_anlaştığımız, S0Lemma: Amerika, S0POS: Noun, S0Token: Amerika'da, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

294- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [_, anlaştığımız, bir ,.. ]

B0Lemma: anlaş, B0POS: Verb, B0Token: _, B1Lemma: _, B1POS: Adj, B1Token: anlaştığımız, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

295- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [_]   B= [anlaştığımız, bir, dizayn ,.. ]

B0Lemma: _, B0POS: Adj, B0Token: anlaştığımız, B1Lemma: bir, B1POS: Adj, B1Token: bir, S0B0Distance: 1, S0B0Lemma: anlaş__, S0B0LemmaPOS: anlaş_Adj, S0B0POS: Verb_Adj, S0B0POSLemma: Verb__, S0B0Token: __anlaştığımız, S0B1Lemma: anlaş_bir, S0B1LemmaPOS: anlaş_Adj, S0B1POS: Verb_Adj, S0B1POSLemma: Verb_bir, S0B1Token: __bir, S0Lemma: anlaş, S0POS: Verb, S0Token: _, anlaş_isGouvernedBy__: true, anlaş_isGouvernedBy___DERIV: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

296- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [anlaştığımız, bir, dizayn ,.. ]

B0Lemma: _, B0POS: Adj, B0Token: anlaştığımız, B1Lemma: bir, B1POS: Adj, B1Token: bir, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

297- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [anlaştığımız]   B= [bir, dizayn, şirketi ,.. ]

B0Lemma: bir, B0POS: Adj, B0Token: bir, B1Lemma: dizayn, B1POS: Noun, B1Token: dizayn, S0B0Distance: 1, S0B0Lemma: __bir, S0B0LemmaPOS: __Adj, S0B0POS: Adj_Adj, S0B0POSLemma: Adj_bir, S0B0Token: anlaştığımız_bir, S0B1Lemma: __dizayn, S0B1LemmaPOS: __Noun, S0B1POS: Adj_Noun, S0B1POSLemma: Adj_dizayn, S0B1Token: anlaştığımız_dizayn, S0Lemma: _, S0POS: Adj, S0Token: anlaştığımız, __isGouvernedBy_dizayn: true, __isGouvernedBy_dizayn_MODIFIER: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

298- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [bir, dizayn, şirketi ,.. ]

B0Lemma: bir, B0POS: Adj, B0Token: bir, B1Lemma: dizayn, B1POS: Noun, B1Token: dizayn, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

299- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [bir]   B= [dizayn, şirketi, bize ,.. ]

B0Lemma: dizayn, B0POS: Noun, B0Token: dizayn, B1Lemma: şirket, B1POS: Noun, B1Token: şirketi, S0B0Distance: 1, S0B0Lemma: bir_dizayn, S0B0LemmaPOS: bir_Noun, S0B0POS: Adj_Noun, S0B0POSLemma: Adj_dizayn, S0B0Token: bir_dizayn, S0B1Lemma: bir_şirket, S0B1LemmaPOS: bir_Noun, S0B1POS: Adj_Noun, S0B1POSLemma: Adj_şirket, S0B1Token: bir_şirketi, S0Lemma: bir, S0POS: Adj, S0Token: bir, bir_isGouvernedBy_dizayn: true, bir_isGouvernedBy_dizayn_DETERMINER: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

300- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [dizayn, şirketi, bize ,.. ]

B0Lemma: dizayn, B0POS: Noun, B0Token: dizayn, B1Lemma: şirket, B1POS: Noun, B1Token: şirketi, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

301- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [dizayn]   B= [şirketi, bize, yılda ,.. ]

B0Lemma: şirket, B0POS: Noun, B0Token: şirketi, B1Lemma: biz, B1POS: Pron, B1Token: bize, S0B0Distance: 1, S0B0Lemma: dizayn_şirket, S0B0LemmaPOS: dizayn_Noun, S0B0POS: Noun_Noun, S0B0POSLemma: Noun_şirket, S0B0Token: dizayn_şirketi, S0B1Lemma: dizayn_biz, S0B1LemmaPOS: dizayn_Pron, S0B1POS: Noun_Pron, S0B1POSLemma: Noun_biz, S0B1Token: dizayn_bize, S0Lemma: dizayn, S0POS: Noun, S0Token: dizayn, dizayn_isGouvernedBy_şirket: true, dizayn_isGouvernedBy_şirket_POSSESSOR: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

302- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [şirketi, bize, yılda ,.. ]

B0Lemma: şirket, B0POS: Noun, B0Token: şirketi, B1Lemma: biz, B1POS: Pron, B1Token: bize, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

303- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [şirketi]   B= [bize, yılda, üç ,.. ]

B0Lemma: biz, B0POS: Pron, B0Token: bize, B1Lemma: yıl, B1POS: Noun, B1Token: yılda, S0B0Distance: 1, S0B0Lemma: şirket_biz, S0B0LemmaPOS: şirket_Pron, S0B0POS: Noun_Pron, S0B0POSLemma: Noun_biz, S0B0Token: şirketi_bize, S0B1Lemma: şirket_yıl, S0B1LemmaPOS: şirket_Noun, S0B1POS: Noun_Noun, S0B1POSLemma: Noun_yıl, S0B1Token: şirketi_yılda, S0Lemma: şirket, S0POS: Noun, S0Token: şirketi, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, şirket_isGouvernedBy_hazırla: true, şirket_isGouvernedBy_hazırla_OBJECT: true, 

304- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [bize, yılda, üç ,.. ]

B0Lemma: biz, B0POS: Pron, B0Token: bize, B1Lemma: yıl, B1POS: Noun, B1Token: yılda, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

305- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [bize]   B= [yılda, üç, ayrı ,.. ]

B0Lemma: yıl, B0POS: Noun, B0Token: yılda, B1Lemma: üç, B1POS: Adj, B1Token: üç, S0B0Distance: 1, S0B0Lemma: biz_yıl, S0B0LemmaPOS: biz_Noun, S0B0POS: Pron_Noun, S0B0POSLemma: Pron_yıl, S0B0Token: bize_yılda, S0B1Lemma: biz_üç, S0B1LemmaPOS: biz_Adj, S0B1POS: Pron_Adj, S0B1POSLemma: Pron_üç, S0B1Token: bize_üç, S0Lemma: biz, S0POS: Pron, S0Token: bize, biz_isGouvernedBy_hazırla: true, biz_isGouvernedBy_hazırla_MODIFIER: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

306- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [yılda, üç, ayrı ,.. ]

B0Lemma: yıl, B0POS: Noun, B0Token: yılda, B1Lemma: üç, B1POS: Adj, B1Token: üç, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

307- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [yılda]   B= [üç, ayrı, forma ,.. ]

B0Lemma: üç, B0POS: Adj, B0Token: üç, B1Lemma: ayrı, B1POS: Adj, B1Token: ayrı, S0B0Distance: 1, S0B0Lemma: yıl_üç, S0B0LemmaPOS: yıl_Adj, S0B0POS: Noun_Adj, S0B0POSLemma: Noun_üç, S0B0Token: yılda_üç, S0B1Lemma: yıl_ayrı, S0B1LemmaPOS: yıl_Adj, S0B1POS: Noun_Adj, S0B1POSLemma: Noun_ayrı, S0B1Token: yılda_ayrı, S0Lemma: yıl, S0POS: Noun, S0Token: yılda, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, yıl_isGouvernedBy_hazırla: true, yıl_isGouvernedBy_hazırla_MODIFIER: true, 

308- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [üç, ayrı, forma ,.. ]

B0Lemma: üç, B0POS: Adj, B0Token: üç, B1Lemma: ayrı, B1POS: Adj, B1Token: ayrı, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

309- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [üç]   B= [ayrı, forma, hazırlayacak ,.. ]

B0Lemma: ayrı, B0POS: Adj, B0Token: ayrı, B1Lemma: forma, B1POS: Noun, B1Token: forma, S0B0Distance: 1, S0B0Lemma: üç_ayrı, S0B0LemmaPOS: üç_Adj, S0B0POS: Adj_Adj, S0B0POSLemma: Adj_ayrı, S0B0Token: üç_ayrı, S0B1Lemma: üç_forma, S0B1LemmaPOS: üç_Noun, S0B1POS: Adj_Noun, S0B1POSLemma: Adj_forma, S0B1Token: üç_forma, S0Lemma: üç, S0POS: Adj, S0Token: üç, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, üç_isGouvernedBy_ayrı: true, üç_isGouvernedBy_ayrı_MODIFIER: true, 

310- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ayrı, forma, hazırlayacak ,.. ]

B0Lemma: ayrı, B0POS: Adj, B0Token: ayrı, B1Lemma: forma, B1POS: Noun, B1Token: forma, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

311- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ayrı]   B= [forma, hazırlayacak, . ,.. ]

B0Lemma: forma, B0POS: Noun, B0Token: forma, B1Lemma: hazırla, B1POS: Verb, B1Token: hazırlayacak, S0B0Distance: 1, S0B0Lemma: ayrı_forma, S0B0LemmaPOS: ayrı_Noun, S0B0POS: Adj_Noun, S0B0POSLemma: Adj_forma, S0B0Token: ayrı_forma, S0B1Lemma: ayrı_hazırla, S0B1LemmaPOS: ayrı_Verb, S0B1POS: Adj_Verb, S0B1POSLemma: Adj_hazırla, S0B1Token: ayrı_hazırlayacak, S0Lemma: ayrı, S0POS: Adj, S0Token: ayrı, ayrı_isGouvernedBy_forma: true, ayrı_isGouvernedBy_forma_MODIFIER: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

312- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [forma, hazırlayacak, . ,.. ]

B0Lemma: forma, B0POS: Noun, B0Token: forma, B1Lemma: hazırla, B1POS: Verb, B1Token: hazırlayacak, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

313- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [forma]   B= [hazırlayacak, ., Taraftarlarımıza ,.. ]

B0Lemma: hazırla, B0POS: Verb, B0Token: hazırlayacak, B1Lemma: ., B1POS: Punc, B1Token: ., S0B0Distance: 1, S0B0Lemma: forma_hazırla, S0B0LemmaPOS: forma_Verb, S0B0POS: Noun_Verb, S0B0POSLemma: Noun_hazırla, S0B0Token: forma_hazırlayacak, S0B1Lemma: forma_., S0B1LemmaPOS: forma_Punc, S0B1POS: Noun_Punc, S0B1POSLemma: Noun_., S0B1Token: forma_., S0Lemma: forma, S0POS: Noun, S0Token: forma, forma_isGouvernedBy_hazırla: true, forma_isGouvernedBy_hazırla_OBJECT: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

314- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [hazırlayacak, ., Taraftarlarımıza ,.. ]

B0Lemma: hazırla, B0POS: Verb, B0Token: hazırlayacak, B1Lemma: ., B1POS: Punc, B1Token: ., transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

315- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [hazırlayacak]   B= [., Taraftarlarımıza, bunları ,.. ]

B0Lemma: ., B0POS: Punc, B0Token: ., B1Lemma: taraftar, B1POS: Noun, B1Token: Taraftarlarımıza, S0B0Distance: 1, S0B0Lemma: hazırla_., S0B0LemmaPOS: hazırla_Punc, S0B0POS: Verb_Punc, S0B0POSLemma: Verb_., S0B0Token: hazırlayacak_., S0B1Lemma: hazırla_taraftar, S0B1LemmaPOS: hazırla_Noun, S0B1POS: Verb_Noun, S0B1POSLemma: Verb_taraftar, S0B1Token: hazırlayacak_Taraftarlarımıza, S0Lemma: hazırla, S0POS: Verb, S0Token: hazırlayacak, hasRighDep_PUNCTUATION: true, hazırla_._hasRighDep_PUNCTUATION: true, hazırla_hasRighDep_PUNCTUATION: true, hazırla_isGouvernedBy_ver: true, hazırla_isGouvernedBy_ver_COORDINATION: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

316- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [., Taraftarlarımıza, bunları ,.. ]

B0Lemma: ., B0POS: Punc, B0Token: ., B1Lemma: taraftar, B1POS: Noun, B1Token: Taraftarlarımıza, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

317- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [Taraftarlarımıza, bunları, vereceğiz ,.. ]

B0Lemma: taraftar, B0POS: Noun, B0Token: Taraftarlarımıza, B1Lemma: bu, B1POS: Pron, B1Token: bunları, S0B0Distance: 1, S0B0Lemma: ._taraftar, S0B0LemmaPOS: ._Noun, S0B0POS: Punc_Noun, S0B0POSLemma: Punc_taraftar, S0B0Token: ._Taraftarlarımıza, S0B1Lemma: ._bu, S0B1LemmaPOS: ._Pron, S0B1POS: Punc_Pron, S0B1POSLemma: Punc_bu, S0B1Token: ._bunları, S0Lemma: ., S0POS: Punc, S0Token: ., transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

318- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Taraftarlarımıza, bunları, vereceğiz ,.. ]

B0Lemma: taraftar, B0POS: Noun, B0Token: Taraftarlarımıza, B1Lemma: bu, B1POS: Pron, B1Token: bunları, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

319- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Taraftarlarımıza]   B= [bunları, vereceğiz, . ,.. ]

B0Lemma: bu, B0POS: Pron, B0Token: bunları, B1Lemma: ver, B1POS: Verb, B1Token: vereceğiz, S0B0Distance: 1, S0B0Lemma: taraftar_bu, S0B0LemmaPOS: taraftar_Pron, S0B0POS: Noun_Pron, S0B0POSLemma: Noun_bu, S0B0Token: Taraftarlarımıza_bunları, S0B1Lemma: taraftar_ver, S0B1LemmaPOS: taraftar_Verb, S0B1POS: Noun_Verb, S0B1POSLemma: Noun_ver, S0B1Token: Taraftarlarımıza_vereceğiz, S0Lemma: taraftar, S0POS: Noun, S0Token: Taraftarlarımıza, taraftar_isGouvernedBy_ver: true, taraftar_isGouvernedBy_ver_MODIFIER: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

320- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [bunları, vereceğiz, . ,.. ]

B0Lemma: bu, B0POS: Pron, B0Token: bunları, B1Lemma: ver, B1POS: Verb, B1Token: vereceğiz, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

321- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [bunları]   B= [vereceğiz, ., Çok ,.. ]

B0Lemma: ver, B0POS: Verb, B0Token: vereceğiz, B1Lemma: ., B1POS: Punc, B1Token: ., S0B0Distance: 1, S0B0Lemma: bu_ver, S0B0LemmaPOS: bu_Verb, S0B0POS: Pron_Verb, S0B0POSLemma: Pron_ver, S0B0Token: bunları_vereceğiz, S0B1Lemma: bu_., S0B1LemmaPOS: bu_Punc, S0B1POS: Pron_Punc, S0B1POSLemma: Pron_., S0B1Token: bunları_., S0Lemma: bu, S0POS: Pron, S0Token: bunları, bu_isGouvernedBy_ver: true, bu_isGouvernedBy_ver_OBJECT: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

322- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [vereceğiz, ., Çok ,.. ]

B0Lemma: ver, B0POS: Verb, B0Token: vereceğiz, B1Lemma: ., B1POS: Punc, B1Token: ., transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

323- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [vereceğiz]   B= [., Çok, büyük ,.. ]

B0Lemma: ., B0POS: Punc, B0Token: ., B1Lemma: çok, B1POS: Adverb, B1Token: Çok, S0B0Distance: 1, S0B0Lemma: ver_., S0B0LemmaPOS: ver_Punc, S0B0POS: Verb_Punc, S0B0POSLemma: Verb_., S0B0Token: vereceğiz_., S0B1Lemma: ver_çok, S0B1LemmaPOS: ver_Adverb, S0B1POS: Verb_Adverb, S0B1POSLemma: Verb_çok, S0B1Token: vereceğiz_Çok, S0Lemma: ver, S0POS: Verb, S0Token: vereceğiz, hasRighDep_PUNCTUATION: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, ver_._hasRighDep_PUNCTUATION: true, ver_hasRighDep_PUNCTUATION: true, ver_isGouvernedBy_aç: true, ver_isGouvernedBy_aç_COORDINATION: true, 

324- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [., Çok, büyük ,.. ]

B0Lemma: ., B0POS: Punc, B0Token: ., B1Lemma: çok, B1POS: Adverb, B1Token: Çok, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

325- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [Çok, büyük, gelirlerin ,.. ]

B0Lemma: çok, B0POS: Adverb, B0Token: Çok, B1Lemma: büyük, B1POS: Adj, B1Token: büyük, S0B0Distance: 1, S0B0Lemma: ._çok, S0B0LemmaPOS: ._Adverb, S0B0POS: Punc_Adverb, S0B0POSLemma: Punc_çok, S0B0Token: ._Çok, S0B1Lemma: ._büyük, S0B1LemmaPOS: ._Adj, S0B1POS: Punc_Adj, S0B1POSLemma: Punc_büyük, S0B1Token: ._büyük, S0Lemma: ., S0POS: Punc, S0Token: ., transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

326- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Çok, büyük, gelirlerin ,.. ]

B0Lemma: çok, B0POS: Adverb, B0Token: Çok, B1Lemma: büyük, B1POS: Adj, B1Token: büyük, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

327- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Çok]   B= [büyük, gelirlerin, kapısını ,.. ]

B0Lemma: büyük, B0POS: Adj, B0Token: büyük, B1Lemma: gelir, B1POS: Noun, B1Token: gelirlerin, S0B0Distance: 1, S0B0Lemma: çok_büyük, S0B0LemmaPOS: çok_Adj, S0B0POS: Adverb_Adj, S0B0POSLemma: Adverb_büyük, S0B0Token: Çok_büyük, S0B1Lemma: çok_gelir, S0B1LemmaPOS: çok_Noun, S0B1POS: Adverb_Noun, S0B1POSLemma: Adverb_gelir, S0B1Token: Çok_gelirlerin, S0Lemma: çok, S0POS: Adverb, S0Token: Çok, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, çok_isGouvernedBy_büyük: true, çok_isGouvernedBy_büyük_DETERMINER: true, 

328- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [büyük, gelirlerin, kapısını ,.. ]

B0Lemma: büyük, B0POS: Adj, B0Token: büyük, B1Lemma: gelir, B1POS: Noun, B1Token: gelirlerin, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

329- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [büyük]   B= [gelirlerin, kapısını, açıyoruz ,.. ]

B0Lemma: gelir, B0POS: Noun, B0Token: gelirlerin, B1Lemma: kapı, B1POS: Noun, B1Token: kapısını, S0B0Distance: 1, S0B0Lemma: büyük_gelir, S0B0LemmaPOS: büyük_Noun, S0B0POS: Adj_Noun, S0B0POSLemma: Adj_gelir, S0B0Token: büyük_gelirlerin, S0B1Lemma: büyük_kapı, S0B1LemmaPOS: büyük_Noun, S0B1POS: Adj_Noun, S0B1POSLemma: Adj_kapı, S0B1Token: büyük_kapısını, S0Lemma: büyük, S0POS: Adj, S0Token: büyük, büyük_isGouvernedBy_gelir: true, büyük_isGouvernedBy_gelir_MODIFIER: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

330- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [gelirlerin, kapısını, açıyoruz ,.. ]

B0Lemma: gelir, B0POS: Noun, B0Token: gelirlerin, B1Lemma: kapı, B1POS: Noun, B1Token: kapısını, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

331- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [gelirlerin]   B= [kapısını, açıyoruz, " ,.. ]

B0Lemma: kapı, B0POS: Noun, B0Token: kapısını, B1Lemma: aç, B1POS: Verb, B1Token: açıyoruz, S0B0Distance: 1, S0B0Lemma: gelir_kapı, S0B0LemmaPOS: gelir_Noun, S0B0POS: Noun_Noun, S0B0POSLemma: Noun_kapı, S0B0Token: gelirlerin_kapısını, S0B1Lemma: gelir_aç, S0B1LemmaPOS: gelir_Verb, S0B1POS: Noun_Verb, S0B1POSLemma: Noun_aç, S0B1Token: gelirlerin_açıyoruz, S0Lemma: gelir, S0POS: Noun, S0Token: gelirlerin, gelir_isGouvernedBy_kapı: true, gelir_isGouvernedBy_kapı_POSSESSOR: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

332- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [kapısını, açıyoruz, " ,.. ]

B0Lemma: kapı, B0POS: Noun, B0Token: kapısını, B1Lemma: aç, B1POS: Verb, B1Token: açıyoruz, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

333- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [kapısını]   B= [açıyoruz, ", . ,.. ]

B0Lemma: aç, B0POS: Verb, B0Token: açıyoruz, B1Lemma: ", B1POS: Punc, B1Token: ", S0B0Distance: 1, S0B0Lemma: kapı_aç, S0B0LemmaPOS: kapı_Verb, S0B0POS: Noun_Verb, S0B0POSLemma: Noun_aç, S0B0Token: kapısını_açıyoruz, S0B1Lemma: kapı_", S0B1LemmaPOS: kapı_Punc, S0B1POS: Noun_Punc, S0B1POSLemma: Noun_", S0B1Token: kapısını_", S0Lemma: kapı, S0POS: Noun, S0Token: kapısını, kapı_isGouvernedBy_aç: true, kapı_isGouvernedBy_aç_OBJECT: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

334- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [açıyoruz, ", . ,.. ]

B0Lemma: aç, B0POS: Verb, B0Token: açıyoruz, B1Lemma: ", B1POS: Punc, B1Token: ", transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

335- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [açıyoruz]   B= [", . ,.. ]

B0Lemma: ", B0POS: Punc, B0Token: ", B1Lemma: ., B1POS: Punc, B1Token: ., S0B0Distance: 1, S0B0Lemma: aç_", S0B0LemmaPOS: aç_Punc, S0B0POS: Verb_Punc, S0B0POSLemma: Verb_", S0B0Token: açıyoruz_", S0B1Lemma: aç_., S0B1LemmaPOS: aç_Punc, S0B1POS: Verb_Punc, S0B1POSLemma: Verb_., S0B1Token: açıyoruz_., S0Lemma: aç, S0POS: Verb, S0Token: açıyoruz, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

336- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [", . ,.. ]

B0Lemma: ", B0POS: Punc, B0Token: ", B1Lemma: ., B1POS: Punc, B1Token: ., transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

337- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= ["]   B= [.]

B0Lemma: ., B0POS: Punc, B0Token: ., S0B0Distance: 1, S0B0Lemma: "_., S0B0LemmaPOS: "_Punc, S0B0POS: Punc_Punc, S0B0POSLemma: Punc_., S0B0Token: "_., S0Lemma: ", S0POS: Punc, S0Token: ", transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

338- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [.]

B0Lemma: ., B0POS: Punc, B0Token: ., transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

339- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [ ]

S0Lemma: ., S0POS: Punc, S0Token: ., transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

340- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

## Sentence No. 1894 - 
Türkiye'nin öncülük _ ettiği 8 Müslüman ülkeden _ oluşan D - 8'lerin açılış toplantısında Başbakan Erbakan ve Yardımcısı Çiller , Batı'ya " rahat olun " mesajı verdi . 
### Existing MWEs: 
1- **öncülük ettiği** (LVC)
2- **rahat olun** (LVC)
3- **mesajı verdi** (OTH)



0- &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Türkiye'nin, öncülük, _ ,.. ]

B0Lemma: Türkiye, B0POS: Noun, B0Token: Türkiye'nin, B1Lemma: öncülük, B1POS: Noun, B1Token: öncülük, 

1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Türkiye'nin]   B= [öncülük, _, ettiği ,.. ]

B0Lemma: öncülük, B0POS: Noun, B0Token: öncülük, B1Lemma: et, B1POS: Verb, B1Token: _, S0B0Distance: 1, S0B0Lemma: Türkiye_öncülük, S0B0LemmaPOS: Türkiye_Noun, S0B0POS: Noun_Noun, S0B0POSLemma: Noun_öncülük, S0B0Token: Türkiye'nin_öncülük, S0B1Lemma: Türkiye_et, S0B1LemmaPOS: Türkiye_Verb, S0B1POS: Noun_Verb, S0B1POSLemma: Noun_et, S0B1Token: Türkiye'nin__, S0Lemma: Türkiye, S0POS: Noun, S0Token: Türkiye'nin, Türkiye_isGouvernedBy__: true, Türkiye_isGouvernedBy___POSSESSOR: true, 

2- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [öncülük, _, ettiği ,.. ]

B0Lemma: öncülük, B0POS: Noun, B0Token: öncülük, B1Lemma: et, B1POS: Verb, B1Token: _, transitionHistoryLength1: 0, 

3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [öncülük]   B= [_, ettiği, 8 ,.. ]

B0Lemma: et, B0POS: Verb, B0Token: _, B1Lemma: _, B1POS: Adj, B1Token: ettiği, S0B0Distance: 1, S0B0Lemma: öncülük_et, S0B0LemmaPOS: öncülük_Verb, S0B0POS: Noun_Verb, S0B0POSLemma: Noun_et, S0B0Token: öncülük__, S0B1Lemma: öncülük__, S0B1LemmaPOS: öncülük_Adj, S0B1POS: Noun_Adj, S0B1POSLemma: Noun__, S0B1Token: öncülük_ettiği, S0Lemma: öncülük, S0POS: Noun, S0Token: öncülük, transitionHistoryLength1: 2, transitionHistoryLength2: 20, öncülük_isGouvernedBy_et: true, öncülük_isGouvernedBy_et_MWE: true, 

4- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [öncülük, _]   B= [ettiği, 8, Müslüman ,.. ]

B0Lemma: _, B0POS: Adj, B0Token: ettiği, B1Lemma: 8, B1POS: Adj, B1Token: 8, S0B0Distance: 1, S0B0Lemma: et__, S0B0LemmaPOS: et_Adj, S0B0POS: Verb_Adj, S0B0POSLemma: Verb__, S0B0Token: __ettiği, S0B1Lemma: et_8, S0B1LemmaPOS: et_Adj, S0B1POS: Verb_Adj, S0B1POSLemma: Verb_8, S0B1Token: __8, S0Lemma: et, S0POS: Verb, S0Token: _, S1B0Lemma: öncülük__, S1B0LemmaPOS: öncülük_Adj, S1B0POS: Noun_Adj, S1B0POSLemma: Noun__, S1B0Token: öncülük_ettiği, S1Lemma: öncülük, S1POS: Noun, S1S0Lemma: öncülük_et, S1S0LemmaPOS: öncülük_Verb, S1S0POS: Noun_Verb, S1S0POSLemma: Noun_et, S1S0Token: öncülük__, S1Token: öncülük, SyntaxicRelation: -MWE, et_isGouvernedBy__: true, et_isGouvernedBy___DERIV: true, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

5- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [öncülük]   B= [ettiği, 8, Müslüman ,.. ]

B0Lemma: _, B0POS: Adj, B0Token: ettiği, B1Lemma: 8, B1POS: Adj, B1Token: 8, S0B0Distance: 2, S0B0Lemma: öncülük__, S0B0LemmaPOS: öncülük_Adj, S0B0POS: Noun_Adj, S0B0POSLemma: Noun__, S0B0Token: öncülük_ettiği, S0B1Lemma: öncülük_8, S0B1LemmaPOS: öncülük_Adj, S0B1POS: Noun_Adj, S0B1POSLemma: Noun_8, S0B1Token: öncülük_8, S0Lemma: öncülük, S0POS: Noun, S0Token: öncülük, transitionHistoryLength1: 0, transitionHistoryLength2: 00, transitionHistoryLength3: 002, 

6- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [öncülük, ettiği]   B= [8, Müslüman, ülkeden ,.. ]

B0Lemma: 8, B0POS: Adj, B0Token: 8, B1Lemma: müslüman, B1POS: Adj, B1Token: Müslüman, S0B0Distance: 1, S0B0Lemma: __8, S0B0LemmaPOS: __Adj, S0B0POS: Adj_Adj, S0B0POSLemma: Adj_8, S0B0Token: ettiği_8, S0B1Lemma: __müslüman, S0B1LemmaPOS: __Adj, S0B1POS: Adj_Adj, S0B1POSLemma: Adj_müslüman, S0B1Token: ettiği_Müslüman, S0Lemma: _, S0POS: Adj, S0Token: ettiği, S1B0Lemma: öncülük_8, S1B0LemmaPOS: öncülük_Adj, S1B0POS: Noun_Adj, S1B0POSLemma: Noun_8, S1B0Token: öncülük_8, S1Lemma: öncülük, S1POS: Noun, S1S0Lemma: öncülük__, S1S0LemmaPOS: öncülük_Adj, S1S0POS: Noun_Adj, S1S0POSLemma: Noun__, S1S0Token: öncülük_ettiği, S1Token: öncülük, __isGouvernedBy_ülke: true, __isGouvernedBy_ülke_MODIFIER: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 200, 

7- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[öncülük, ettiği]]   B= [8, Müslüman, ülkeden ,.. ]

B0Lemma: 8, B0POS: Adj, B0Token: 8, B1Lemma: müslüman, B1POS: Adj, B1Token: Müslüman, S0B0Distance: 1, S0B0Lemma: öncülük___8, S0B0LemmaPOS: öncülük___Adj, S0B0POS: Noun_Adj_Adj, S0B0POSLemma: Noun_Adj_8, S0B0Token: öncülük_ettiği_8, S0B1Lemma: öncülük___müslüman, S0B1LemmaPOS: öncülük___Adj, S0B1POS: Noun_Adj_Adj, S0B1POSLemma: Noun_Adj_müslüman, S0B1Token: öncülük_ettiği_Müslüman, S0Lemma: öncülük__, S0POS: Noun_Adj, S0Token: öncülük_ettiği, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

8- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [8, Müslüman, ülkeden ,.. ]

B0Lemma: 8, B0POS: Adj, B0Token: 8, B1Lemma: müslüman, B1POS: Adj, B1Token: Müslüman, transitionHistoryLength1: 1, transitionHistoryLength2: 10, transitionHistoryLength3: 102, 

9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [8]   B= [Müslüman, ülkeden, _ ,.. ]

8_isGouvernedBy_ülke: true, 8_isGouvernedBy_ülke_MODIFIER: true, B0Lemma: müslüman, B0POS: Adj, B0Token: Müslüman, B1Lemma: ülke, B1POS: Noun, B1Token: ülkeden, S0B0Distance: 1, S0B0Lemma: 8_müslüman, S0B0LemmaPOS: 8_Adj, S0B0POS: Adj_Adj, S0B0POSLemma: Adj_müslüman, S0B0Token: 8_Müslüman, S0B1Lemma: 8_ülke, S0B1LemmaPOS: 8_Noun, S0B1POS: Adj_Noun, S0B1POSLemma: Adj_ülke, S0B1Token: 8_ülkeden, S0Lemma: 8, S0POS: Adj, S0Token: 8, transitionHistoryLength1: 2, transitionHistoryLength2: 21, transitionHistoryLength3: 210, 

10- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Müslüman, ülkeden, _ ,.. ]

B0Lemma: müslüman, B0POS: Adj, B0Token: Müslüman, B1Lemma: ülke, B1POS: Noun, B1Token: ülkeden, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 021, 

11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Müslüman]   B= [ülkeden, _, oluşan ,.. ]

B0Lemma: ülke, B0POS: Noun, B0Token: ülkeden, B1Lemma: oluş, B1POS: Verb, B1Token: _, S0B0Distance: 1, S0B0Lemma: müslüman_ülke, S0B0LemmaPOS: müslüman_Noun, S0B0POS: Adj_Noun, S0B0POSLemma: Adj_ülke, S0B0Token: Müslüman_ülkeden, S0B1Lemma: müslüman_oluş, S0B1LemmaPOS: müslüman_Verb, S0B1POS: Adj_Verb, S0B1POSLemma: Adj_oluş, S0B1Token: Müslüman__, S0Lemma: müslüman, S0POS: Adj, S0Token: Müslüman, müslüman_isGouvernedBy_ülke: true, müslüman_isGouvernedBy_ülke_MODIFIER: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

12- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ülkeden, _, oluşan ,.. ]

B0Lemma: ülke, B0POS: Noun, B0Token: ülkeden, B1Lemma: oluş, B1POS: Verb, B1Token: _, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ülkeden]   B= [_, oluşan, D ,.. ]

B0Lemma: oluş, B0POS: Verb, B0Token: _, B1Lemma: _, B1POS: Adj, B1Token: oluşan, S0B0Distance: 1, S0B0Lemma: ülke_oluş, S0B0LemmaPOS: ülke_Verb, S0B0POS: Noun_Verb, S0B0POSLemma: Noun_oluş, S0B0Token: ülkeden__, S0B1Lemma: ülke__, S0B1LemmaPOS: ülke_Adj, S0B1POS: Noun_Adj, S0B1POSLemma: Noun__, S0B1Token: ülkeden_oluşan, S0Lemma: ülke, S0POS: Noun, S0Token: ülkeden, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, ülke_isGouvernedBy_oluş: true, ülke_isGouvernedBy_oluş_MODIFIER: true, 

14- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [_, oluşan, D ,.. ]

B0Lemma: oluş, B0POS: Verb, B0Token: _, B1Lemma: _, B1POS: Adj, B1Token: oluşan, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [_]   B= [oluşan, D, - ,.. ]

B0Lemma: _, B0POS: Adj, B0Token: oluşan, B1Lemma: d, B1POS: Noun, B1Token: D, S0B0Distance: 1, S0B0Lemma: oluş__, S0B0LemmaPOS: oluş_Adj, S0B0POS: Verb_Adj, S0B0POSLemma: Verb__, S0B0Token: __oluşan, S0B1Lemma: oluş_d, S0B1LemmaPOS: oluş_Noun, S0B1POS: Verb_Noun, S0B1POSLemma: Verb_d, S0B1Token: __D, S0Lemma: oluş, S0POS: Verb, S0Token: _, oluş_isGouvernedBy__: true, oluş_isGouvernedBy___DERIV: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

16- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [oluşan, D, - ,.. ]

B0Lemma: _, B0POS: Adj, B0Token: oluşan, B1Lemma: d, B1POS: Noun, B1Token: D, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [oluşan]   B= [D, -, 8'lerin ,.. ]

B0Lemma: d, B0POS: Noun, B0Token: D, B1Lemma: -, B1POS: Punc, B1Token: -, S0B0Distance: 1, S0B0Lemma: __d, S0B0LemmaPOS: __Noun, S0B0POS: Adj_Noun, S0B0POSLemma: Adj_d, S0B0Token: oluşan_D, S0B1Lemma: __-, S0B1LemmaPOS: __Punc, S0B1POS: Adj_Punc, S0B1POSLemma: Adj_-, S0B1Token: oluşan_-, S0Lemma: _, S0POS: Adj, S0Token: oluşan, __isGouvernedBy_d: true, __isGouvernedBy_d_MODIFIER: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

18- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [D, -, 8'lerin ,.. ]

B0Lemma: d, B0POS: Noun, B0Token: D, B1Lemma: -, B1POS: Punc, B1Token: -, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [D]   B= [-, 8'lerin, açılış ,.. ]

B0Lemma: -, B0POS: Punc, B0Token: -, B1Lemma: 8, B1POS: Noun, B1Token: 8'lerin, S0B0Distance: 1, S0B0Lemma: d_-, S0B0LemmaPOS: d_Punc, S0B0POS: Noun_Punc, S0B0POSLemma: Noun_-, S0B0Token: D_-, S0B1Lemma: d_8, S0B1LemmaPOS: d_Noun, S0B1POS: Noun_Noun, S0B1POSLemma: Noun_8, S0B1Token: D_8'lerin, S0Lemma: d, S0POS: Noun, S0Token: D, d_-_hasRighDep_PUNCTUATION: true, d_hasRighDep_PUNCTUATION: true, d_isGouvernedBy_ver: true, d_isGouvernedBy_ver_SUBJECT: true, hasRighDep_PUNCTUATION: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

20- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [-, 8'lerin, açılış ,.. ]

B0Lemma: -, B0POS: Punc, B0Token: -, B1Lemma: 8, B1POS: Noun, B1Token: 8'lerin, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [-]   B= [8'lerin, açılış, toplantısında ,.. ]

B0Lemma: 8, B0POS: Noun, B0Token: 8'lerin, B1Lemma: açılış, B1POS: Noun, B1Token: açılış, S0B0Distance: 1, S0B0Lemma: -_8, S0B0LemmaPOS: -_Noun, S0B0POS: Punc_Noun, S0B0POSLemma: Punc_8, S0B0Token: -_8'lerin, S0B1Lemma: -_açılış, S0B1LemmaPOS: -_Noun, S0B1POS: Punc_Noun, S0B1POSLemma: Punc_açılış, S0B1Token: -_açılış, S0Lemma: -, S0POS: Punc, S0Token: -, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

22- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [8'lerin, açılış, toplantısında ,.. ]

B0Lemma: 8, B0POS: Noun, B0Token: 8'lerin, B1Lemma: açılış, B1POS: Noun, B1Token: açılış, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

23- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [8'lerin]   B= [açılış, toplantısında, Başbakan ,.. ]

8_isGouvernedBy_toplantı: true, 8_isGouvernedBy_toplantı_POSSESSOR: true, B0Lemma: açılış, B0POS: Noun, B0Token: açılış, B1Lemma: toplantı, B1POS: Noun, B1Token: toplantısında, S0B0Distance: 1, S0B0Lemma: 8_açılış, S0B0LemmaPOS: 8_Noun, S0B0POS: Noun_Noun, S0B0POSLemma: Noun_açılış, S0B0Token: 8'lerin_açılış, S0B1Lemma: 8_toplantı, S0B1LemmaPOS: 8_Noun, S0B1POS: Noun_Noun, S0B1POSLemma: Noun_toplantı, S0B1Token: 8'lerin_toplantısında, S0Lemma: 8, S0POS: Noun, S0Token: 8'lerin, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

24- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [açılış, toplantısında, Başbakan ,.. ]

B0Lemma: açılış, B0POS: Noun, B0Token: açılış, B1Lemma: toplantı, B1POS: Noun, B1Token: toplantısında, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

25- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [açılış]   B= [toplantısında, Başbakan, Erbakan ,.. ]

B0Lemma: toplantı, B0POS: Noun, B0Token: toplantısında, B1Lemma: başbakan, B1POS: Noun, B1Token: Başbakan, S0B0Distance: 1, S0B0Lemma: açılış_toplantı, S0B0LemmaPOS: açılış_Noun, S0B0POS: Noun_Noun, S0B0POSLemma: Noun_toplantı, S0B0Token: açılış_toplantısında, S0B1Lemma: açılış_başbakan, S0B1LemmaPOS: açılış_Noun, S0B1POS: Noun_Noun, S0B1POSLemma: Noun_başbakan, S0B1Token: açılış_Başbakan, S0Lemma: açılış, S0POS: Noun, S0Token: açılış, açılış_isGouvernedBy_toplantı: true, açılış_isGouvernedBy_toplantı_POSSESSOR: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

26- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [toplantısında, Başbakan, Erbakan ,.. ]

B0Lemma: toplantı, B0POS: Noun, B0Token: toplantısında, B1Lemma: başbakan, B1POS: Noun, B1Token: Başbakan, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

27- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [toplantısında]   B= [Başbakan, Erbakan, ve ,.. ]

B0Lemma: başbakan, B0POS: Noun, B0Token: Başbakan, B1Lemma: Erbakan, B1POS: Noun, B1Token: Erbakan, S0B0Distance: 1, S0B0Lemma: toplantı_başbakan, S0B0LemmaPOS: toplantı_Noun, S0B0POS: Noun_Noun, S0B0POSLemma: Noun_başbakan, S0B0Token: toplantısında_Başbakan, S0B1Lemma: toplantı_Erbakan, S0B1LemmaPOS: toplantı_Noun, S0B1POS: Noun_Noun, S0B1POSLemma: Noun_Erbakan, S0B1Token: toplantısında_Erbakan, S0Lemma: toplantı, S0POS: Noun, S0Token: toplantısında, toplantı_isGouvernedBy_ver: true, toplantı_isGouvernedBy_ver_MODIFIER: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

28- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Başbakan, Erbakan, ve ,.. ]

B0Lemma: başbakan, B0POS: Noun, B0Token: Başbakan, B1Lemma: Erbakan, B1POS: Noun, B1Token: Erbakan, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

29- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Başbakan]   B= [Erbakan, ve, Yardımcısı ,.. ]

B0Lemma: Erbakan, B0POS: Noun, B0Token: Erbakan, B1Lemma: ve, B1POS: Conj, B1Token: ve, S0B0Distance: 1, S0B0Lemma: başbakan_Erbakan, S0B0LemmaPOS: başbakan_Noun, S0B0POS: Noun_Noun, S0B0POSLemma: Noun_Erbakan, S0B0Token: Başbakan_Erbakan, S0B1Lemma: başbakan_ve, S0B1LemmaPOS: başbakan_Conj, S0B1POS: Noun_Conj, S0B1POSLemma: Noun_ve, S0B1Token: Başbakan_ve, S0Lemma: başbakan, S0POS: Noun, S0Token: Başbakan, başbakan_isGouvernedBy_Erbakan: true, başbakan_isGouvernedBy_Erbakan_MWE: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

30- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Erbakan, ve, Yardımcısı ,.. ]

B0Lemma: Erbakan, B0POS: Noun, B0Token: Erbakan, B1Lemma: ve, B1POS: Conj, B1Token: ve, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

31- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Erbakan]   B= [ve, Yardımcısı, Çiller ,.. ]

B0Lemma: ve, B0POS: Conj, B0Token: ve, B1Lemma: yardımcı, B1POS: Noun, B1Token: Yardımcısı, Erbakan_hasRighDep_CONJUNCTION: true, Erbakan_isGouvernedBy_Çiller: true, Erbakan_isGouvernedBy_Çiller_COORDINATION: true, Erbakan_ve_hasRighDep_CONJUNCTION: true, S0B0Distance: 1, S0B0Lemma: Erbakan_ve, S0B0LemmaPOS: Erbakan_Conj, S0B0POS: Noun_Conj, S0B0POSLemma: Noun_ve, S0B0Token: Erbakan_ve, S0B1Lemma: Erbakan_yardımcı, S0B1LemmaPOS: Erbakan_Noun, S0B1POS: Noun_Noun, S0B1POSLemma: Noun_yardımcı, S0B1Token: Erbakan_Yardımcısı, S0Lemma: Erbakan, S0POS: Noun, S0Token: Erbakan, hasRighDep_CONJUNCTION: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

32- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ve, Yardımcısı, Çiller ,.. ]

B0Lemma: ve, B0POS: Conj, B0Token: ve, B1Lemma: yardımcı, B1POS: Noun, B1Token: Yardımcısı, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

33- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ve]   B= [Yardımcısı, Çiller, , ,.. ]

B0Lemma: yardımcı, B0POS: Noun, B0Token: Yardımcısı, B1Lemma: Çiller, B1POS: Noun, B1Token: Çiller, S0B0Distance: 1, S0B0Lemma: ve_yardımcı, S0B0LemmaPOS: ve_Noun, S0B0POS: Conj_Noun, S0B0POSLemma: Conj_yardımcı, S0B0Token: ve_Yardımcısı, S0B1Lemma: ve_Çiller, S0B1LemmaPOS: ve_Noun, S0B1POS: Conj_Noun, S0B1POSLemma: Conj_Çiller, S0B1Token: ve_Çiller, S0Lemma: ve, S0POS: Conj, S0Token: ve, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

34- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Yardımcısı, Çiller, , ,.. ]

B0Lemma: yardımcı, B0POS: Noun, B0Token: Yardımcısı, B1Lemma: Çiller, B1POS: Noun, B1Token: Çiller, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

35- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Yardımcısı]   B= [Çiller, ,, Batı'ya ,.. ]

B0Lemma: Çiller, B0POS: Noun, B0Token: Çiller, B1Lemma: ,, B1POS: Punc, B1Token: ,, S0B0Distance: 1, S0B0Lemma: yardımcı_Çiller, S0B0LemmaPOS: yardımcı_Noun, S0B0POS: Noun_Noun, S0B0POSLemma: Noun_Çiller, S0B0Token: Yardımcısı_Çiller, S0B1Lemma: yardımcı_,, S0B1LemmaPOS: yardımcı_Punc, S0B1POS: Noun_Punc, S0B1POSLemma: Noun_,, S0B1Token: Yardımcısı_,, S0Lemma: yardımcı, S0POS: Noun, S0Token: Yardımcısı, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, yardımcı_isGouvernedBy_Çiller: true, yardımcı_isGouvernedBy_Çiller_MWE: true, 

36- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Çiller, ,, Batı'ya ,.. ]

B0Lemma: Çiller, B0POS: Noun, B0Token: Çiller, B1Lemma: ,, B1POS: Punc, B1Token: ,, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

37- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Çiller]   B= [,, Batı'ya, " ,.. ]

B0Lemma: ,, B0POS: Punc, B0Token: ,, B1Lemma: Batı, B1POS: Noun, B1Token: Batı'ya, S0B0Distance: 1, S0B0Lemma: Çiller_,, S0B0LemmaPOS: Çiller_Punc, S0B0POS: Noun_Punc, S0B0POSLemma: Noun_,, S0B0Token: Çiller_,, S0B1Lemma: Çiller_Batı, S0B1LemmaPOS: Çiller_Noun, S0B1POS: Noun_Noun, S0B1POSLemma: Noun_Batı, S0B1Token: Çiller_Batı'ya, S0Lemma: Çiller, S0POS: Noun, S0Token: Çiller, hasRighDep_PUNCTUATION: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, Çiller_,_hasRighDep_PUNCTUATION: true, Çiller_hasRighDep_PUNCTUATION: true, Çiller_isGouvernedBy_ver: true, Çiller_isGouvernedBy_ver_SUBJECT: true, 

38- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, Batı'ya, " ,.. ]

B0Lemma: ,, B0POS: Punc, B0Token: ,, B1Lemma: Batı, B1POS: Noun, B1Token: Batı'ya, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

39- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [Batı'ya, ", rahat ,.. ]

B0Lemma: Batı, B0POS: Noun, B0Token: Batı'ya, B1Lemma: ", B1POS: Punc, B1Token: ", S0B0Distance: 1, S0B0Lemma: ,_Batı, S0B0LemmaPOS: ,_Noun, S0B0POS: Punc_Noun, S0B0POSLemma: Punc_Batı, S0B0Token: ,_Batı'ya, S0B1Lemma: ,_", S0B1LemmaPOS: ,_Punc, S0B1POS: Punc_Punc, S0B1POSLemma: Punc_", S0B1Token: ,_", S0Lemma: ,, S0POS: Punc, S0Token: ,, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

40- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Batı'ya, ", rahat ,.. ]

B0Lemma: Batı, B0POS: Noun, B0Token: Batı'ya, B1Lemma: ", B1POS: Punc, B1Token: ", transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

41- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Batı'ya]   B= [", rahat, olun ,.. ]

B0Lemma: ", B0POS: Punc, B0Token: ", B1Lemma: rahat, B1POS: Noun, B1Token: rahat, Batı_"_hasRighDep_PUNCTUATION: true, Batı_hasRighDep_PUNCTUATION: true, Batı_isGouvernedBy_ver: true, Batı_isGouvernedBy_ver_MODIFIER: true, S0B0Distance: 1, S0B0Lemma: Batı_", S0B0LemmaPOS: Batı_Punc, S0B0POS: Noun_Punc, S0B0POSLemma: Noun_", S0B0Token: Batı'ya_", S0B1Lemma: Batı_rahat, S0B1LemmaPOS: Batı_Noun, S0B1POS: Noun_Noun, S0B1POSLemma: Noun_rahat, S0B1Token: Batı'ya_rahat, S0Lemma: Batı, S0POS: Noun, S0Token: Batı'ya, hasRighDep_PUNCTUATION: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

42- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [", rahat, olun ,.. ]

B0Lemma: ", B0POS: Punc, B0Token: ", B1Lemma: rahat, B1POS: Noun, B1Token: rahat, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

43- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= ["]   B= [rahat, olun, " ,.. ]

B0Lemma: rahat, B0POS: Noun, B0Token: rahat, B1Lemma: ol, B1POS: Verb, B1Token: olun, S0B0Distance: 1, S0B0Lemma: "_rahat, S0B0LemmaPOS: "_Noun, S0B0POS: Punc_Noun, S0B0POSLemma: Punc_rahat, S0B0Token: "_rahat, S0B1Lemma: "_ol, S0B1LemmaPOS: "_Verb, S0B1POS: Punc_Verb, S0B1POSLemma: Punc_ol, S0B1Token: "_olun, S0Lemma: ", S0POS: Punc, S0Token: ", transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

44- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [rahat, olun, " ,.. ]

B0Lemma: rahat, B0POS: Noun, B0Token: rahat, B1Lemma: ol, B1POS: Verb, B1Token: olun, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

45- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [rahat]   B= [olun, ", mesajı ,.. ]

B0Lemma: ol, B0POS: Verb, B0Token: olun, B1Lemma: ", B1POS: Punc, B1Token: ", S0B0Distance: 1, S0B0Lemma: rahat_ol, S0B0LemmaPOS: rahat_Verb, S0B0POS: Noun_Verb, S0B0POSLemma: Noun_ol, S0B0Token: rahat_olun, S0B1Lemma: rahat_", S0B1LemmaPOS: rahat_Punc, S0B1POS: Noun_Punc, S0B1POSLemma: Noun_", S0B1Token: rahat_", S0Lemma: rahat, S0POS: Noun, S0Token: rahat, rahat_isGouvernedBy_ol: true, rahat_isGouvernedBy_ol_OBJECT: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

46- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [rahat, olun]   B= [", mesajı, verdi ,.. ]

B0Lemma: ", B0POS: Punc, B0Token: ", B1Lemma: mesaj, B1POS: Noun, B1Token: mesajı, S0B0Distance: 1, S0B0Lemma: ol_", S0B0LemmaPOS: ol_Punc, S0B0POS: Verb_Punc, S0B0POSLemma: Verb_", S0B0Token: olun_", S0B1Lemma: ol_mesaj, S0B1LemmaPOS: ol_Noun, S0B1POS: Verb_Noun, S0B1POSLemma: Verb_mesaj, S0B1Token: olun_mesajı, S0Lemma: ol, S0POS: Verb, S0Token: olun, S1B0Lemma: rahat_", S1B0LemmaPOS: rahat_Punc, S1B0POS: Noun_Punc, S1B0POSLemma: Noun_", S1B0Token: rahat_", S1Lemma: rahat, S1POS: Noun, S1S0Lemma: rahat_ol, S1S0LemmaPOS: rahat_Verb, S1S0POS: Noun_Verb, S1S0POSLemma: Noun_ol, S1S0Token: rahat_olun, S1Token: rahat, SyntaxicRelation: -OBJECT, hasRighDep_PUNCTUATION: true, ol_"_hasRighDep_PUNCTUATION: true, ol_hasRighDep_PUNCTUATION: true, ol_isGouvernedBy_mesaj: true, ol_isGouvernedBy_mesaj_POSSESSOR: true, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

47- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[rahat, olun]]   B= [", mesajı, verdi ,.. ]

B0Lemma: ", B0POS: Punc, B0Token: ", B1Lemma: mesaj, B1POS: Noun, B1Token: mesajı, S0B0Distance: 1, S0B0Lemma: rahat_ol_", S0B0LemmaPOS: rahat_ol_Punc, S0B0POS: Noun_Verb_Punc, S0B0POSLemma: Noun_Verb_", S0B0Token: rahat_olun_", S0B1Lemma: rahat_ol_mesaj, S0B1LemmaPOS: rahat_ol_Noun, S0B1POS: Noun_Verb_Noun, S0B1POSLemma: Noun_Verb_mesaj, S0B1Token: rahat_olun_mesajı, S0Lemma: rahat_ol, S0POS: Noun_Verb, S0Token: rahat_olun, transitionHistoryLength1: 0, transitionHistoryLength2: 00, transitionHistoryLength3: 002, 

48- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [", mesajı, verdi ,.. ]

B0Lemma: ", B0POS: Punc, B0Token: ", B1Lemma: mesaj, B1POS: Noun, B1Token: mesajı, transitionHistoryLength1: 1, transitionHistoryLength2: 10, transitionHistoryLength3: 100, 

49- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= ["]   B= [mesajı, verdi, . ,.. ]

B0Lemma: mesaj, B0POS: Noun, B0Token: mesajı, B1Lemma: ver, B1POS: Verb, B1Token: verdi, S0B0Distance: 1, S0B0Lemma: "_mesaj, S0B0LemmaPOS: "_Noun, S0B0POS: Punc_Noun, S0B0POSLemma: Punc_mesaj, S0B0Token: "_mesajı, S0B1Lemma: "_ver, S0B1LemmaPOS: "_Verb, S0B1POS: Punc_Verb, S0B1POSLemma: Punc_ver, S0B1Token: "_verdi, S0Lemma: ", S0POS: Punc, S0Token: ", transitionHistoryLength1: 2, transitionHistoryLength2: 21, transitionHistoryLength3: 210, 

50- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [mesajı, verdi, . ,.. ]

B0Lemma: mesaj, B0POS: Noun, B0Token: mesajı, B1Lemma: ver, B1POS: Verb, B1Token: verdi, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 021, 

51- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [mesajı]   B= [verdi, . ,.. ]

B0Lemma: ver, B0POS: Verb, B0Token: verdi, B1Lemma: ., B1POS: Punc, B1Token: ., S0B0Distance: 1, S0B0Lemma: mesaj_ver, S0B0LemmaPOS: mesaj_Verb, S0B0POS: Noun_Verb, S0B0POSLemma: Noun_ver, S0B0Token: mesajı_verdi, S0B1Lemma: mesaj_., S0B1LemmaPOS: mesaj_Punc, S0B1POS: Noun_Punc, S0B1POSLemma: Noun_., S0B1Token: mesajı_., S0Lemma: mesaj, S0POS: Noun, S0Token: mesajı, mesaj_isGouvernedBy_ver: true, mesaj_isGouvernedBy_ver_OBJECT: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

52- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [mesajı, verdi]   B= [.]

B0Lemma: ., B0POS: Punc, B0Token: ., S0B0Distance: 1, S0B0Lemma: ver_., S0B0LemmaPOS: ver_Punc, S0B0POS: Verb_Punc, S0B0POSLemma: Verb_., S0B0Token: verdi_., S0Lemma: ver, S0POS: Verb, S0Token: verdi, S1B0Lemma: mesaj_., S1B0LemmaPOS: mesaj_Punc, S1B0POS: Noun_Punc, S1B0POSLemma: Noun_., S1B0Token: mesajı_., S1Lemma: mesaj, S1POS: Noun, S1S0Lemma: mesaj_ver, S1S0LemmaPOS: mesaj_Verb, S1S0POS: Noun_Verb, S1S0POSLemma: Noun_ver, S1S0Token: mesajı_verdi, S1Token: mesajı, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

53- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[mesajı, verdi]]   B= [.]

B0Lemma: ., B0POS: Punc, B0Token: ., S0B0Distance: 1, S0B0Lemma: mesaj_ver_., S0B0LemmaPOS: mesaj_ver_Punc, S0B0POS: Noun_Verb_Punc, S0B0POSLemma: Noun_Verb_., S0B0Token: mesajı_verdi_., S0Lemma: mesaj_ver, S0POS: Noun_Verb, S0Token: mesajı_verdi, transitionHistoryLength1: 0, transitionHistoryLength2: 00, transitionHistoryLength3: 002, 

54- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [.]

B0Lemma: ., B0POS: Punc, B0Token: ., transitionHistoryLength1: 1, transitionHistoryLength2: 10, transitionHistoryLength3: 100, 

55- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [ ]

S0Lemma: ., S0POS: Punc, S0Token: ., transitionHistoryLength1: 2, transitionHistoryLength2: 21, transitionHistoryLength3: 210, 

56- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

## Sentence No. 2158 - 
Bu ülkelerin biraraya _ gelerek _ yapmak _ istedikleri iş ; bütün ülkeleri _ kucaklamak , bütün insanlık için _ çalışmalar _ _ yapmaktır . " . Özellikle ticari ve ekonomik alanda işbirliği önerilerinin ön plana _ çıktığı toplantıda , Dışişleri bakanları 9 Kasım'da Ankara'da _ _ şekillenen raporu tartışacak . Merkez bankalarının arasında işbirliği , ortak yatırımları teşvik , ortak özelleştirmelerin _ öngörüldüğü raporda , tarafların serbest ticaret bölgesi _ kurmaları , ticari engellerin _ kaldırılması gibi maddeler de yer alıyor , ancak bu işbirliği çerçevesinde gümrüklere ilişkin nasıl adımlar _ atılacağı konusunda somut bir öneri bulunuyor . AVRUPA ÖRNEĞİ . D - 8 Zirvesi'nin barışçıl amaçlar _ taşıdığını _ vurgulayan Çiller de " Müslüman - 8'ler " isminin yanlış bir _ algılamaya yol _ açtığını şu sözlerle açıkladı : " D - 8'ler dine dayalı bir _ örgütlenme değildir . 
### Existing MWEs: 
1- **ön plana çıktığı** (ID)
2- **yer alıyor** (ID)
3- **yol açtığını** (ID)



0- &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Bu, ülkelerin, biraraya ,.. ]

B0Lemma: bu, B0POS: Det, B0Token: Bu, B1Lemma: ülke, B1POS: Noun, B1Token: ülkelerin, 

1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Bu]   B= [ülkelerin, biraraya, _ ,.. ]

B0Lemma: ülke, B0POS: Noun, B0Token: ülkelerin, B1Lemma: birara, B1POS: Noun, B1Token: biraraya, S0B0Distance: 1, S0B0Lemma: bu_ülke, S0B0LemmaPOS: bu_Noun, S0B0POS: Det_Noun, S0B0POSLemma: Det_ülke, S0B0Token: Bu_ülkelerin, S0B1Lemma: bu_birara, S0B1LemmaPOS: bu_Noun, S0B1POS: Det_Noun, S0B1POSLemma: Det_birara, S0B1Token: Bu_biraraya, S0Lemma: bu, S0POS: Det, S0Token: Bu, bu_isGouvernedBy_ülke: true, bu_isGouvernedBy_ülke_DETERMINER: true, 

2- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ülkelerin, biraraya, _ ,.. ]

B0Lemma: ülke, B0POS: Noun, B0Token: ülkelerin, B1Lemma: birara, B1POS: Noun, B1Token: biraraya, transitionHistoryLength1: 0, 

3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ülkelerin]   B= [biraraya, _, gelerek ,.. ]

B0Lemma: birara, B0POS: Noun, B0Token: biraraya, B1Lemma: gel, B1POS: Verb, B1Token: _, S0B0Distance: 1, S0B0Lemma: ülke_birara, S0B0LemmaPOS: ülke_Noun, S0B0POS: Noun_Noun, S0B0POSLemma: Noun_birara, S0B0Token: ülkelerin_biraraya, S0B1Lemma: ülke_gel, S0B1LemmaPOS: ülke_Verb, S0B1POS: Noun_Verb, S0B1POSLemma: Noun_gel, S0B1Token: ülkelerin__, S0Lemma: ülke, S0POS: Noun, S0Token: ülkelerin, transitionHistoryLength1: 2, transitionHistoryLength2: 20, ülke_isGouvernedBy__: true, ülke_isGouvernedBy___POSSESSOR: true, 

4- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [biraraya, _, gelerek ,.. ]

B0Lemma: birara, B0POS: Noun, B0Token: biraraya, B1Lemma: gel, B1POS: Verb, B1Token: _, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [biraraya]   B= [_, gelerek, _ ,.. ]

B0Lemma: gel, B0POS: Verb, B0Token: _, B1Lemma: _, B1POS: Adverb, B1Token: gelerek, S0B0Distance: 1, S0B0Lemma: birara_gel, S0B0LemmaPOS: birara_Verb, S0B0POS: Noun_Verb, S0B0POSLemma: Noun_gel, S0B0Token: biraraya__, S0B1Lemma: birara__, S0B1LemmaPOS: birara_Adverb, S0B1POS: Noun_Adverb, S0B1POSLemma: Noun__, S0B1Token: biraraya_gelerek, S0Lemma: birara, S0POS: Noun, S0Token: biraraya, birara_isGouvernedBy_gel: true, birara_isGouvernedBy_gel_MODIFIER: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

6- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [_, gelerek, _ ,.. ]

B0Lemma: gel, B0POS: Verb, B0Token: _, B1Lemma: _, B1POS: Adverb, B1Token: gelerek, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [_]   B= [gelerek, _, yapmak ,.. ]

B0Lemma: _, B0POS: Adverb, B0Token: gelerek, B1Lemma: yap, B1POS: Verb, B1Token: _, S0B0Distance: 1, S0B0Lemma: gel__, S0B0LemmaPOS: gel_Adverb, S0B0POS: Verb_Adverb, S0B0POSLemma: Verb__, S0B0Token: __gelerek, S0B1Lemma: gel_yap, S0B1LemmaPOS: gel_Verb, S0B1POS: Verb_Verb, S0B1POSLemma: Verb_yap, S0B1Token: ___, S0Lemma: gel, S0POS: Verb, S0Token: _, gel_isGouvernedBy__: true, gel_isGouvernedBy___DERIV: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

8- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [gelerek, _, yapmak ,.. ]

B0Lemma: _, B0POS: Adverb, B0Token: gelerek, B1Lemma: yap, B1POS: Verb, B1Token: _, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [gelerek]   B= [_, yapmak, _ ,.. ]

B0Lemma: yap, B0POS: Verb, B0Token: _, B1Lemma: _, B1POS: Noun, B1Token: yapmak, S0B0Distance: 1, S0B0Lemma: __yap, S0B0LemmaPOS: __Verb, S0B0POS: Adverb_Verb, S0B0POSLemma: Adverb_yap, S0B0Token: gelerek__, S0B1Lemma: ___, S0B1LemmaPOS: __Noun, S0B1POS: Adverb_Noun, S0B1POSLemma: Adverb__, S0B1Token: gelerek_yapmak, S0Lemma: _, S0POS: Adverb, S0Token: gelerek, __isGouvernedBy_yap: true, __isGouvernedBy_yap_MODIFIER: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

10- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [_, yapmak, _ ,.. ]

B0Lemma: yap, B0POS: Verb, B0Token: _, B1Lemma: _, B1POS: Noun, B1Token: yapmak, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [_]   B= [yapmak, _, istedikleri ,.. ]

B0Lemma: _, B0POS: Noun, B0Token: yapmak, B1Lemma: iste, B1POS: Verb, B1Token: _, S0B0Distance: 1, S0B0Lemma: yap__, S0B0LemmaPOS: yap_Noun, S0B0POS: Verb_Noun, S0B0POSLemma: Verb__, S0B0Token: __yapmak, S0B1Lemma: yap_iste, S0B1LemmaPOS: yap_Verb, S0B1POS: Verb_Verb, S0B1POSLemma: Verb_iste, S0B1Token: ___, S0Lemma: yap, S0POS: Verb, S0Token: _, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, yap_isGouvernedBy__: true, yap_isGouvernedBy___DERIV: true, 

12- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [yapmak, _, istedikleri ,.. ]

B0Lemma: _, B0POS: Noun, B0Token: yapmak, B1Lemma: iste, B1POS: Verb, B1Token: _, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [yapmak]   B= [_, istedikleri, iş ,.. ]

B0Lemma: iste, B0POS: Verb, B0Token: _, B1Lemma: _, B1POS: Adj, B1Token: istedikleri, S0B0Distance: 1, S0B0Lemma: __iste, S0B0LemmaPOS: __Verb, S0B0POS: Noun_Verb, S0B0POSLemma: Noun_iste, S0B0Token: yapmak__, S0B1Lemma: ___, S0B1LemmaPOS: __Adj, S0B1POS: Noun_Adj, S0B1POSLemma: Noun__, S0B1Token: yapmak_istedikleri, S0Lemma: _, S0POS: Noun, S0Token: yapmak, __isGouvernedBy_iste: true, __isGouvernedBy_iste_OBJECT: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

14- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [_, istedikleri, iş ,.. ]

B0Lemma: iste, B0POS: Verb, B0Token: _, B1Lemma: _, B1POS: Adj, B1Token: istedikleri, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [_]   B= [istedikleri, iş, ; ,.. ]

B0Lemma: _, B0POS: Adj, B0Token: istedikleri, B1Lemma: iş, B1POS: Noun, B1Token: iş, S0B0Distance: 1, S0B0Lemma: iste__, S0B0LemmaPOS: iste_Adj, S0B0POS: Verb_Adj, S0B0POSLemma: Verb__, S0B0Token: __istedikleri, S0B1Lemma: iste_iş, S0B1LemmaPOS: iste_Noun, S0B1POS: Verb_Noun, S0B1POSLemma: Verb_iş, S0B1Token: __iş, S0Lemma: iste, S0POS: Verb, S0Token: _, iste_isGouvernedBy__: true, iste_isGouvernedBy___DERIV: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

16- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [istedikleri, iş, ; ,.. ]

B0Lemma: _, B0POS: Adj, B0Token: istedikleri, B1Lemma: iş, B1POS: Noun, B1Token: iş, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [istedikleri]   B= [iş, ;, bütün ,.. ]

B0Lemma: iş, B0POS: Noun, B0Token: iş, B1Lemma: ;, B1POS: Punc, B1Token: ;, S0B0Distance: 1, S0B0Lemma: __iş, S0B0LemmaPOS: __Noun, S0B0POS: Adj_Noun, S0B0POSLemma: Adj_iş, S0B0Token: istedikleri_iş, S0B1Lemma: __;, S0B1LemmaPOS: __Punc, S0B1POS: Adj_Punc, S0B1POSLemma: Adj_;, S0B1Token: istedikleri_;, S0Lemma: _, S0POS: Adj, S0Token: istedikleri, __isGouvernedBy_iş: true, __isGouvernedBy_iş_MODIFIER: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

18- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [iş, ;, bütün ,.. ]

B0Lemma: iş, B0POS: Noun, B0Token: iş, B1Lemma: ;, B1POS: Punc, B1Token: ;, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [iş]   B= [;, bütün, ülkeleri ,.. ]

B0Lemma: ;, B0POS: Punc, B0Token: ;, B1Lemma: bütün, B1POS: Adj, B1Token: bütün, S0B0Distance: 1, S0B0Lemma: iş_;, S0B0LemmaPOS: iş_Punc, S0B0POS: Noun_Punc, S0B0POSLemma: Noun_;, S0B0Token: iş_;, S0B1Lemma: iş_bütün, S0B1LemmaPOS: iş_Adj, S0B1POS: Noun_Adj, S0B1POSLemma: Noun_bütün, S0B1Token: iş_bütün, S0Lemma: iş, S0POS: Noun, S0Token: iş, hasRighDep_PUNCTUATION: true, iş_;_hasRighDep_PUNCTUATION: true, iş_hasRighDep_PUNCTUATION: true, iş_isGouvernedBy__: true, iş_isGouvernedBy___COORDINATION: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

20- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [;, bütün, ülkeleri ,.. ]

B0Lemma: ;, B0POS: Punc, B0Token: ;, B1Lemma: bütün, B1POS: Adj, B1Token: bütün, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [;]   B= [bütün, ülkeleri, _ ,.. ]

B0Lemma: bütün, B0POS: Adj, B0Token: bütün, B1Lemma: ülke, B1POS: Noun, B1Token: ülkeleri, S0B0Distance: 1, S0B0Lemma: ;_bütün, S0B0LemmaPOS: ;_Adj, S0B0POS: Punc_Adj, S0B0POSLemma: Punc_bütün, S0B0Token: ;_bütün, S0B1Lemma: ;_ülke, S0B1LemmaPOS: ;_Noun, S0B1POS: Punc_Noun, S0B1POSLemma: Punc_ülke, S0B1Token: ;_ülkeleri, S0Lemma: ;, S0POS: Punc, S0Token: ;, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

22- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [bütün, ülkeleri, _ ,.. ]

B0Lemma: bütün, B0POS: Adj, B0Token: bütün, B1Lemma: ülke, B1POS: Noun, B1Token: ülkeleri, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

23- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [bütün]   B= [ülkeleri, _, kucaklamak ,.. ]

B0Lemma: ülke, B0POS: Noun, B0Token: ülkeleri, B1Lemma: kucakla, B1POS: Verb, B1Token: _, S0B0Distance: 1, S0B0Lemma: bütün_ülke, S0B0LemmaPOS: bütün_Noun, S0B0POS: Adj_Noun, S0B0POSLemma: Adj_ülke, S0B0Token: bütün_ülkeleri, S0B1Lemma: bütün_kucakla, S0B1LemmaPOS: bütün_Verb, S0B1POS: Adj_Verb, S0B1POSLemma: Adj_kucakla, S0B1Token: bütün__, S0Lemma: bütün, S0POS: Adj, S0Token: bütün, bütün_isGouvernedBy_ülke: true, bütün_isGouvernedBy_ülke_MODIFIER: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

24- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ülkeleri, _, kucaklamak ,.. ]

B0Lemma: ülke, B0POS: Noun, B0Token: ülkeleri, B1Lemma: kucakla, B1POS: Verb, B1Token: _, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

25- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ülkeleri]   B= [_, kucaklamak, , ,.. ]

B0Lemma: kucakla, B0POS: Verb, B0Token: _, B1Lemma: _, B1POS: Noun, B1Token: kucaklamak, S0B0Distance: 1, S0B0Lemma: ülke_kucakla, S0B0LemmaPOS: ülke_Verb, S0B0POS: Noun_Verb, S0B0POSLemma: Noun_kucakla, S0B0Token: ülkeleri__, S0B1Lemma: ülke__, S0B1LemmaPOS: ülke_Noun, S0B1POS: Noun_Noun, S0B1POSLemma: Noun__, S0B1Token: ülkeleri_kucaklamak, S0Lemma: ülke, S0POS: Noun, S0Token: ülkeleri, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, ülke_isGouvernedBy_kucakla: true, ülke_isGouvernedBy_kucakla_OBJECT: true, 

26- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [_, kucaklamak, , ,.. ]

B0Lemma: kucakla, B0POS: Verb, B0Token: _, B1Lemma: _, B1POS: Noun, B1Token: kucaklamak, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

27- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [_]   B= [kucaklamak, ,, bütün ,.. ]

B0Lemma: _, B0POS: Noun, B0Token: kucaklamak, B1Lemma: ,, B1POS: Punc, B1Token: ,, S0B0Distance: 1, S0B0Lemma: kucakla__, S0B0LemmaPOS: kucakla_Noun, S0B0POS: Verb_Noun, S0B0POSLemma: Verb__, S0B0Token: __kucaklamak, S0B1Lemma: kucakla_,, S0B1LemmaPOS: kucakla_Punc, S0B1POS: Verb_Punc, S0B1POSLemma: Verb_,, S0B1Token: __,, S0Lemma: kucakla, S0POS: Verb, S0Token: _, kucakla_isGouvernedBy__: true, kucakla_isGouvernedBy___DERIV: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

28- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [kucaklamak, ,, bütün ,.. ]

B0Lemma: _, B0POS: Noun, B0Token: kucaklamak, B1Lemma: ,, B1POS: Punc, B1Token: ,, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

29- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [kucaklamak]   B= [,, bütün, insanlık ,.. ]

B0Lemma: ,, B0POS: Punc, B0Token: ,, B1Lemma: bütün, B1POS: Adj, B1Token: bütün, S0B0Distance: 1, S0B0Lemma: __,, S0B0LemmaPOS: __Punc, S0B0POS: Noun_Punc, S0B0POSLemma: Noun_,, S0B0Token: kucaklamak_,, S0B1Lemma: __bütün, S0B1LemmaPOS: __Adj, S0B1POS: Noun_Adj, S0B1POSLemma: Noun_bütün, S0B1Token: kucaklamak_bütün, S0Lemma: _, S0POS: Noun, S0Token: kucaklamak, __,_hasRighDep_PUNCTUATION: true, __hasRighDep_PUNCTUATION: true, __isGouvernedBy__: true, __isGouvernedBy___SUBJECT: true, hasRighDep_PUNCTUATION: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

30- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, bütün, insanlık ,.. ]

B0Lemma: ,, B0POS: Punc, B0Token: ,, B1Lemma: bütün, B1POS: Adj, B1Token: bütün, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

31- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [bütün, insanlık, için ,.. ]

B0Lemma: bütün, B0POS: Adj, B0Token: bütün, B1Lemma: insanlık, B1POS: Noun, B1Token: insanlık, S0B0Distance: 1, S0B0Lemma: ,_bütün, S0B0LemmaPOS: ,_Adj, S0B0POS: Punc_Adj, S0B0POSLemma: Punc_bütün, S0B0Token: ,_bütün, S0B1Lemma: ,_insanlık, S0B1LemmaPOS: ,_Noun, S0B1POS: Punc_Noun, S0B1POSLemma: Punc_insanlık, S0B1Token: ,_insanlık, S0Lemma: ,, S0POS: Punc, S0Token: ,, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

32- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [bütün, insanlık, için ,.. ]

B0Lemma: bütün, B0POS: Adj, B0Token: bütün, B1Lemma: insanlık, B1POS: Noun, B1Token: insanlık, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

33- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [bütün]   B= [insanlık, için, _ ,.. ]

B0Lemma: insanlık, B0POS: Noun, B0Token: insanlık, B1Lemma: için, B1POS: Postp, B1Token: için, S0B0Distance: 1, S0B0Lemma: bütün_insanlık, S0B0LemmaPOS: bütün_Noun, S0B0POS: Adj_Noun, S0B0POSLemma: Adj_insanlık, S0B0Token: bütün_insanlık, S0B1Lemma: bütün_için, S0B1LemmaPOS: bütün_Postp, S0B1POS: Adj_Postp, S0B1POSLemma: Adj_için, S0B1Token: bütün_için, S0Lemma: bütün, S0POS: Adj, S0Token: bütün, bütün_isGouvernedBy_insanlık: true, bütün_isGouvernedBy_insanlık_MODIFIER: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

34- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [insanlık, için, _ ,.. ]

B0Lemma: insanlık, B0POS: Noun, B0Token: insanlık, B1Lemma: için, B1POS: Postp, B1Token: için, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

35- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [insanlık]   B= [için, _, çalışmalar ,.. ]

B0Lemma: için, B0POS: Postp, B0Token: için, B1Lemma: çalış, B1POS: Verb, B1Token: _, S0B0Distance: 1, S0B0Lemma: insanlık_için, S0B0LemmaPOS: insanlık_Postp, S0B0POS: Noun_Postp, S0B0POSLemma: Noun_için, S0B0Token: insanlık_için, S0B1Lemma: insanlık_çalış, S0B1LemmaPOS: insanlık_Verb, S0B1POS: Noun_Verb, S0B1POSLemma: Noun_çalış, S0B1Token: insanlık__, S0Lemma: insanlık, S0POS: Noun, S0Token: insanlık, insanlık_isGouvernedBy_için: true, insanlık_isGouvernedBy_için_ARGUMENT: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

36- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [için, _, çalışmalar ,.. ]

B0Lemma: için, B0POS: Postp, B0Token: için, B1Lemma: çalış, B1POS: Verb, B1Token: _, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

37- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [için]   B= [_, çalışmalar, _ ,.. ]

B0Lemma: çalış, B0POS: Verb, B0Token: _, B1Lemma: _, B1POS: Noun, B1Token: çalışmalar, S0B0Distance: 1, S0B0Lemma: için_çalış, S0B0LemmaPOS: için_Verb, S0B0POS: Postp_Verb, S0B0POSLemma: Postp_çalış, S0B0Token: için__, S0B1Lemma: için__, S0B1LemmaPOS: için_Noun, S0B1POS: Postp_Noun, S0B1POSLemma: Postp__, S0B1Token: için_çalışmalar, S0Lemma: için, S0POS: Postp, S0Token: için, için_isGouvernedBy_yap: true, için_isGouvernedBy_yap_MODIFIER: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

38- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [_, çalışmalar, _ ,.. ]

B0Lemma: çalış, B0POS: Verb, B0Token: _, B1Lemma: _, B1POS: Noun, B1Token: çalışmalar, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

39- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [_]   B= [çalışmalar, _, _ ,.. ]

B0Lemma: _, B0POS: Noun, B0Token: çalışmalar, B1Lemma: yap, B1POS: Verb, B1Token: _, S0B0Distance: 1, S0B0Lemma: çalış__, S0B0LemmaPOS: çalış_Noun, S0B0POS: Verb_Noun, S0B0POSLemma: Verb__, S0B0Token: __çalışmalar, S0B1Lemma: çalış_yap, S0B1LemmaPOS: çalış_Verb, S0B1POS: Verb_Verb, S0B1POSLemma: Verb_yap, S0B1Token: ___, S0Lemma: çalış, S0POS: Verb, S0Token: _, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, çalış_isGouvernedBy__: true, çalış_isGouvernedBy___DERIV: true, 

40- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [çalışmalar, _, _ ,.. ]

B0Lemma: _, B0POS: Noun, B0Token: çalışmalar, B1Lemma: yap, B1POS: Verb, B1Token: _, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

41- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [çalışmalar]   B= [_, _, yapmaktır ,.. ]

B0Lemma: yap, B0POS: Verb, B0Token: _, B1Lemma: _, B1POS: Noun, B1Token: _, S0B0Distance: 1, S0B0Lemma: __yap, S0B0LemmaPOS: __Verb, S0B0POS: Noun_Verb, S0B0POSLemma: Noun_yap, S0B0Token: çalışmalar__, S0B1Lemma: ___, S0B1LemmaPOS: __Noun, S0B1POS: Noun_Noun, S0B1POSLemma: Noun__, S0B1Token: çalışmalar__, S0Lemma: _, S0POS: Noun, S0Token: çalışmalar, __isGouvernedBy_yap: true, __isGouvernedBy_yap_OBJECT: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

42- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [_, _, yapmaktır ,.. ]

B0Lemma: yap, B0POS: Verb, B0Token: _, B1Lemma: _, B1POS: Noun, B1Token: _, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

43- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [_]   B= [_, yapmaktır, . ,.. ]

B0Lemma: _, B0POS: Noun, B0Token: _, B1Lemma: _, B1POS: Verb, B1Token: yapmaktır, S0B0Distance: 1, S0B0Lemma: yap__, S0B0LemmaPOS: yap_Noun, S0B0POS: Verb_Noun, S0B0POSLemma: Verb__, S0B0Token: ___, S0B1Lemma: yap__, S0B1LemmaPOS: yap_Verb, S0B1POS: Verb_Verb, S0B1POSLemma: Verb__, S0B1Token: __yapmaktır, S0Lemma: yap, S0POS: Verb, S0Token: _, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, yap_isGouvernedBy__: true, yap_isGouvernedBy___DERIV: true, 

44- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [_, yapmaktır, . ,.. ]

B0Lemma: _, B0POS: Noun, B0Token: _, B1Lemma: _, B1POS: Verb, B1Token: yapmaktır, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

45- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [_]   B= [yapmaktır, ., " ,.. ]

B0Lemma: _, B0POS: Verb, B0Token: yapmaktır, B1Lemma: ., B1POS: Punc, B1Token: ., S0B0Distance: 1, S0B0Lemma: ___, S0B0LemmaPOS: __Verb, S0B0POS: Noun_Verb, S0B0POSLemma: Noun__, S0B0Token: __yapmaktır, S0B1Lemma: __., S0B1LemmaPOS: __Punc, S0B1POS: Noun_Punc, S0B1POSLemma: Noun_., S0B1Token: __., S0Lemma: _, S0POS: Noun, S0Token: _, __isGouvernedBy__: true, __isGouvernedBy___DERIV: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

46- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [yapmaktır, ., " ,.. ]

B0Lemma: _, B0POS: Verb, B0Token: yapmaktır, B1Lemma: ., B1POS: Punc, B1Token: ., transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

47- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [yapmaktır]   B= [., ", . ,.. ]

B0Lemma: ., B0POS: Punc, B0Token: ., B1Lemma: ", B1POS: Punc, B1Token: ", S0B0Distance: 1, S0B0Lemma: __., S0B0LemmaPOS: __Punc, S0B0POS: Verb_Punc, S0B0POSLemma: Verb_., S0B0Token: yapmaktır_., S0B1Lemma: __", S0B1LemmaPOS: __Punc, S0B1POS: Verb_Punc, S0B1POSLemma: Verb_", S0B1Token: yapmaktır_", S0Lemma: _, S0POS: Verb, S0Token: yapmaktır, __"_hasRighDep_PUNCTUATION: true, __._hasRighDep_PUNCTUATION: true, __hasRighDep_PUNCTUATION: true, __isGouvernedBy_tartış: true, __isGouvernedBy_tartış_COORDINATION: true, hasRighDep_PUNCTUATION: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

48- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [., ", . ,.. ]

B0Lemma: ., B0POS: Punc, B0Token: ., B1Lemma: ", B1POS: Punc, B1Token: ", transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

49- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [", ., Özellikle ,.. ]

B0Lemma: ", B0POS: Punc, B0Token: ", B1Lemma: ., B1POS: Punc, B1Token: ., S0B0Distance: 1, S0B0Lemma: ._", S0B0LemmaPOS: ._Punc, S0B0POS: Punc_Punc, S0B0POSLemma: Punc_", S0B0Token: ._", S0B1Lemma: ._., S0B1LemmaPOS: ._Punc, S0B1POS: Punc_Punc, S0B1POSLemma: Punc_., S0B1Token: ._., S0Lemma: ., S0POS: Punc, S0Token: ., transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

50- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [", ., Özellikle ,.. ]

B0Lemma: ", B0POS: Punc, B0Token: ", B1Lemma: ., B1POS: Punc, B1Token: ., transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

51- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= ["]   B= [., Özellikle, ticari ,.. ]

B0Lemma: ., B0POS: Punc, B0Token: ., B1Lemma: özellikle, B1POS: Adverb, B1Token: Özellikle, S0B0Distance: 1, S0B0Lemma: "_., S0B0LemmaPOS: "_Punc, S0B0POS: Punc_Punc, S0B0POSLemma: Punc_., S0B0Token: "_., S0B1Lemma: "_özellikle, S0B1LemmaPOS: "_Adverb, S0B1POS: Punc_Adverb, S0B1POSLemma: Punc_özellikle, S0B1Token: "_Özellikle, S0Lemma: ", S0POS: Punc, S0Token: ", transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

52- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [., Özellikle, ticari ,.. ]

B0Lemma: ., B0POS: Punc, B0Token: ., B1Lemma: özellikle, B1POS: Adverb, B1Token: Özellikle, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

53- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [Özellikle, ticari, ve ,.. ]

B0Lemma: özellikle, B0POS: Adverb, B0Token: Özellikle, B1Lemma: ticari, B1POS: Adj, B1Token: ticari, S0B0Distance: 1, S0B0Lemma: ._özellikle, S0B0LemmaPOS: ._Adverb, S0B0POS: Punc_Adverb, S0B0POSLemma: Punc_özellikle, S0B0Token: ._Özellikle, S0B1Lemma: ._ticari, S0B1LemmaPOS: ._Adj, S0B1POS: Punc_Adj, S0B1POSLemma: Punc_ticari, S0B1Token: ._ticari, S0Lemma: ., S0POS: Punc, S0Token: ., transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

54- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Özellikle, ticari, ve ,.. ]

B0Lemma: özellikle, B0POS: Adverb, B0Token: Özellikle, B1Lemma: ticari, B1POS: Adj, B1Token: ticari, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

55- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Özellikle]   B= [ticari, ve, ekonomik ,.. ]

B0Lemma: ticari, B0POS: Adj, B0Token: ticari, B1Lemma: ve, B1POS: Conj, B1Token: ve, S0B0Distance: 1, S0B0Lemma: özellikle_ticari, S0B0LemmaPOS: özellikle_Adj, S0B0POS: Adverb_Adj, S0B0POSLemma: Adverb_ticari, S0B0Token: Özellikle_ticari, S0B1Lemma: özellikle_ve, S0B1LemmaPOS: özellikle_Conj, S0B1POS: Adverb_Conj, S0B1POSLemma: Adverb_ve, S0B1Token: Özellikle_ve, S0Lemma: özellikle, S0POS: Adverb, S0Token: Özellikle, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, özellikle_isGouvernedBy_ticari: true, özellikle_isGouvernedBy_ticari_MODIFIER: true, 

56- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ticari, ve, ekonomik ,.. ]

B0Lemma: ticari, B0POS: Adj, B0Token: ticari, B1Lemma: ve, B1POS: Conj, B1Token: ve, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

57- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ticari]   B= [ve, ekonomik, alanda ,.. ]

B0Lemma: ve, B0POS: Conj, B0Token: ve, B1Lemma: ekonomik, B1POS: Adj, B1Token: ekonomik, S0B0Distance: 1, S0B0Lemma: ticari_ve, S0B0LemmaPOS: ticari_Conj, S0B0POS: Adj_Conj, S0B0POSLemma: Adj_ve, S0B0Token: ticari_ve, S0B1Lemma: ticari_ekonomik, S0B1LemmaPOS: ticari_Adj, S0B1POS: Adj_Adj, S0B1POSLemma: Adj_ekonomik, S0B1Token: ticari_ekonomik, S0Lemma: ticari, S0POS: Adj, S0Token: ticari, hasRighDep_CONJUNCTION: true, ticari_hasRighDep_CONJUNCTION: true, ticari_isGouvernedBy_ekonomik: true, ticari_isGouvernedBy_ekonomik_COORDINATION: true, ticari_ve_hasRighDep_CONJUNCTION: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

58- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ve, ekonomik, alanda ,.. ]

B0Lemma: ve, B0POS: Conj, B0Token: ve, B1Lemma: ekonomik, B1POS: Adj, B1Token: ekonomik, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

59- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ve]   B= [ekonomik, alanda, işbirliği ,.. ]

B0Lemma: ekonomik, B0POS: Adj, B0Token: ekonomik, B1Lemma: alan, B1POS: Noun, B1Token: alanda, S0B0Distance: 1, S0B0Lemma: ve_ekonomik, S0B0LemmaPOS: ve_Adj, S0B0POS: Conj_Adj, S0B0POSLemma: Conj_ekonomik, S0B0Token: ve_ekonomik, S0B1Lemma: ve_alan, S0B1LemmaPOS: ve_Noun, S0B1POS: Conj_Noun, S0B1POSLemma: Conj_alan, S0B1Token: ve_alanda, S0Lemma: ve, S0POS: Conj, S0Token: ve, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

60- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ekonomik, alanda, işbirliği ,.. ]

B0Lemma: ekonomik, B0POS: Adj, B0Token: ekonomik, B1Lemma: alan, B1POS: Noun, B1Token: alanda, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

61- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ekonomik]   B= [alanda, işbirliği, önerilerinin ,.. ]

B0Lemma: alan, B0POS: Noun, B0Token: alanda, B1Lemma: işbirliği, B1POS: Noun, B1Token: işbirliği, S0B0Distance: 1, S0B0Lemma: ekonomik_alan, S0B0LemmaPOS: ekonomik_Noun, S0B0POS: Adj_Noun, S0B0POSLemma: Adj_alan, S0B0Token: ekonomik_alanda, S0B1Lemma: ekonomik_işbirliği, S0B1LemmaPOS: ekonomik_Noun, S0B1POS: Adj_Noun, S0B1POSLemma: Adj_işbirliği, S0B1Token: ekonomik_işbirliği, S0Lemma: ekonomik, S0POS: Adj, S0Token: ekonomik, ekonomik_isGouvernedBy_alan: true, ekonomik_isGouvernedBy_alan_MODIFIER: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

62- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [alanda, işbirliği, önerilerinin ,.. ]

B0Lemma: alan, B0POS: Noun, B0Token: alanda, B1Lemma: işbirliği, B1POS: Noun, B1Token: işbirliği, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

63- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [alanda]   B= [işbirliği, önerilerinin, ön ,.. ]

B0Lemma: işbirliği, B0POS: Noun, B0Token: işbirliği, B1Lemma: öneri, B1POS: Noun, B1Token: önerilerinin, S0B0Distance: 1, S0B0Lemma: alan_işbirliği, S0B0LemmaPOS: alan_Noun, S0B0POS: Noun_Noun, S0B0POSLemma: Noun_işbirliği, S0B0Token: alanda_işbirliği, S0B1Lemma: alan_öneri, S0B1LemmaPOS: alan_Noun, S0B1POS: Noun_Noun, S0B1POSLemma: Noun_öneri, S0B1Token: alanda_önerilerinin, S0Lemma: alan, S0POS: Noun, S0Token: alanda, alan_isGouvernedBy_tartış: true, alan_isGouvernedBy_tartış_MODIFIER: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

64- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [işbirliği, önerilerinin, ön ,.. ]

B0Lemma: işbirliği, B0POS: Noun, B0Token: işbirliği, B1Lemma: öneri, B1POS: Noun, B1Token: önerilerinin, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

65- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [işbirliği]   B= [önerilerinin, ön, plana ,.. ]

B0Lemma: öneri, B0POS: Noun, B0Token: önerilerinin, B1Lemma: ön, B1POS: Adj, B1Token: ön, S0B0Distance: 1, S0B0Lemma: işbirliği_öneri, S0B0LemmaPOS: işbirliği_Noun, S0B0POS: Noun_Noun, S0B0POSLemma: Noun_öneri, S0B0Token: işbirliği_önerilerinin, S0B1Lemma: işbirliği_ön, S0B1LemmaPOS: işbirliği_Adj, S0B1POS: Noun_Adj, S0B1POSLemma: Noun_ön, S0B1Token: işbirliği_ön, S0Lemma: işbirliği, S0POS: Noun, S0Token: işbirliği, işbirliği_isGouvernedBy_öneri: true, işbirliği_isGouvernedBy_öneri_POSSESSOR: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

66- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [önerilerinin, ön, plana ,.. ]

B0Lemma: öneri, B0POS: Noun, B0Token: önerilerinin, B1Lemma: ön, B1POS: Adj, B1Token: ön, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

67- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [önerilerinin]   B= [ön, plana, _ ,.. ]

B0Lemma: ön, B0POS: Adj, B0Token: ön, B1Lemma: plan, B1POS: Noun, B1Token: plana, S0B0Distance: 1, S0B0Lemma: öneri_ön, S0B0LemmaPOS: öneri_Adj, S0B0POS: Noun_Adj, S0B0POSLemma: Noun_ön, S0B0Token: önerilerinin_ön, S0B1Lemma: öneri_plan, S0B1LemmaPOS: öneri_Noun, S0B1POS: Noun_Noun, S0B1POSLemma: Noun_plan, S0B1Token: önerilerinin_plana, S0Lemma: öneri, S0POS: Noun, S0Token: önerilerinin, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, öneri_isGouvernedBy__: true, öneri_isGouvernedBy___POSSESSOR: true, 

68- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ön, plana, _ ,.. ]

B0Lemma: ön, B0POS: Adj, B0Token: ön, B1Lemma: plan, B1POS: Noun, B1Token: plana, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

69- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ön]   B= [plana, _, çıktığı ,.. ]

B0Lemma: plan, B0POS: Noun, B0Token: plana, B1Lemma: çık, B1POS: Verb, B1Token: _, S0B0Distance: 1, S0B0Lemma: ön_plan, S0B0LemmaPOS: ön_Noun, S0B0POS: Adj_Noun, S0B0POSLemma: Adj_plan, S0B0Token: ön_plana, S0B1Lemma: ön_çık, S0B1LemmaPOS: ön_Verb, S0B1POS: Adj_Verb, S0B1POSLemma: Adj_çık, S0B1Token: ön__, S0Lemma: ön, S0POS: Adj, S0Token: ön, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, ön_isGouvernedBy_plan: true, ön_isGouvernedBy_plan_MODIFIER: true, 

70- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ön, plana]   B= [_, çıktığı, toplantıda ,.. ]

B0Lemma: çık, B0POS: Verb, B0Token: _, B1Lemma: _, B1POS: Adj, B1Token: çıktığı, S0B0Distance: 1, S0B0Lemma: plan_çık, S0B0LemmaPOS: plan_Verb, S0B0POS: Noun_Verb, S0B0POSLemma: Noun_çık, S0B0Token: plana__, S0B1Lemma: plan__, S0B1LemmaPOS: plan_Adj, S0B1POS: Noun_Adj, S0B1POSLemma: Noun__, S0B1Token: plana_çıktığı, S0Lemma: plan, S0POS: Noun, S0Token: plana, S1B0Lemma: ön_çık, S1B0LemmaPOS: ön_Verb, S1B0POS: Adj_Verb, S1B0POSLemma: Adj_çık, S1B0Token: ön__, S1Lemma: ön, S1POS: Adj, S1S0Lemma: ön_plan, S1S0LemmaPOS: ön_Noun, S1S0POS: Adj_Noun, S1S0POSLemma: Adj_plan, S1S0Token: ön_plana, S1Token: ön, SyntaxicRelation: -MODIFIER, plan_isGouvernedBy_çık: true, plan_isGouvernedBy_çık_MODIFIER: true, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

71- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ön, plana, _]   B= [çıktığı, toplantıda, , ,.. ]

B0Lemma: _, B0POS: Adj, B0Token: çıktığı, B1Lemma: toplantı, B1POS: Noun, B1Token: toplantıda, S0B0Distance: 1, S0B0Lemma: çık__, S0B0LemmaPOS: çık_Adj, S0B0POS: Verb_Adj, S0B0POSLemma: Verb__, S0B0Token: __çıktığı, S0B1Lemma: çık_toplantı, S0B1LemmaPOS: çık_Noun, S0B1POS: Verb_Noun, S0B1POSLemma: Verb_toplantı, S0B1Token: __toplantıda, S0Lemma: çık, S0POS: Verb, S0Token: _, S1B0Lemma: plan__, S1B0LemmaPOS: plan_Adj, S1B0POS: Noun_Adj, S1B0POSLemma: Noun__, S1B0Token: plana_çıktığı, S1Lemma: plan, S1POS: Noun, S1S0Lemma: plan_çık, S1S0LemmaPOS: plan_Verb, S1S0POS: Noun_Verb, S1S0POSLemma: Noun_çık, S1S0Token: plana__, S1Token: plana, SyntaxicRelation: -MODIFIER, transitionHistoryLength1: 0, transitionHistoryLength2: 00, transitionHistoryLength3: 002, çık_isGouvernedBy__: true, çık_isGouvernedBy___DERIV: true, 

72- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ön, plana]   B= [çıktığı, toplantıda, , ,.. ]

B0Lemma: _, B0POS: Adj, B0Token: çıktığı, B1Lemma: toplantı, B1POS: Noun, B1Token: toplantıda, S0B0Distance: 2, S0B0Lemma: plan__, S0B0LemmaPOS: plan_Adj, S0B0POS: Noun_Adj, S0B0POSLemma: Noun__, S0B0Token: plana_çıktığı, S0B1Lemma: plan_toplantı, S0B1LemmaPOS: plan_Noun, S0B1POS: Noun_Noun, S0B1POSLemma: Noun_toplantı, S0B1Token: plana_toplantıda, S0Lemma: plan, S0POS: Noun, S0Token: plana, S1B0Lemma: ön__, S1B0LemmaPOS: ön_Adj, S1B0POS: Adj_Adj, S1B0POSLemma: Adj__, S1B0Token: ön_çıktığı, S1Lemma: ön, S1POS: Adj, S1S0Lemma: ön_plan, S1S0LemmaPOS: ön_Noun, S1S0POS: Adj_Noun, S1S0POSLemma: Adj_plan, S1S0Token: ön_plana, S1Token: ön, SyntaxicRelation: -MODIFIER, transitionHistoryLength1: 0, transitionHistoryLength2: 00, transitionHistoryLength3: 000, 

73- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ön, plana, çıktığı]   B= [toplantıda, ,, Dışişleri ,.. ]

B0Lemma: toplantı, B0POS: Noun, B0Token: toplantıda, B1Lemma: ,, B1POS: Punc, B1Token: ,, S0B0Distance: 1, S0B0Lemma: __toplantı, S0B0LemmaPOS: __Noun, S0B0POS: Adj_Noun, S0B0POSLemma: Adj_toplantı, S0B0Token: çıktığı_toplantıda, S0B1Lemma: __,, S0B1LemmaPOS: __Punc, S0B1POS: Adj_Punc, S0B1POSLemma: Adj_,, S0B1Token: çıktığı_,, S0Lemma: _, S0POS: Adj, S0Token: çıktığı, S1B0Lemma: plan_toplantı, S1B0LemmaPOS: plan_Noun, S1B0POS: Noun_Noun, S1B0POSLemma: Noun_toplantı, S1B0Token: plana_toplantıda, S1Lemma: plan, S1POS: Noun, S1S0Lemma: plan__, S1S0LemmaPOS: plan_Adj, S1S0POS: Noun_Adj, S1S0POSLemma: Noun__, S1S0Token: plana_çıktığı, S1Token: plana, __isGouvernedBy_toplantı: true, __isGouvernedBy_toplantı_MODIFIER: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 200, 

74- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ön, [plana, çıktığı]]   B= [toplantıda, ,, Dışişleri ,.. ]

B0Lemma: toplantı, B0POS: Noun, B0Token: toplantıda, B1Lemma: ,, B1POS: Punc, B1Token: ,, S0B0Distance: 1, S0B0Lemma: plan___toplantı, S0B0LemmaPOS: plan___Noun, S0B0POS: Noun_Adj_Noun, S0B0POSLemma: Noun_Adj_toplantı, S0B0Token: plana_çıktığı_toplantıda, S0B1Lemma: plan___,, S0B1LemmaPOS: plan___Punc, S0B1POS: Noun_Adj_Punc, S0B1POSLemma: Noun_Adj_,, S0B1Token: plana_çıktığı_,, S0Lemma: plan__, S0POS: Noun_Adj, S0Token: plana_çıktığı, S1B0Lemma: ön_toplantı, S1B0LemmaPOS: ön_Noun, S1B0POS: Adj_Noun, S1B0POSLemma: Adj_toplantı, S1B0Token: ön_toplantıda, S1Lemma: ön, S1POS: Adj, S1S0Lemma: ön_plan__, S1S0LemmaPOS: ön_Noun_Adj, S1S0POS: Adj_Noun_Adj, S1S0POSLemma: Adj_plan__, S1S0Token: ön_plana_çıktığı, S1Token: ön, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

75- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[ön, [plana, çıktığı]]]   B= [toplantıda, ,, Dışişleri ,.. ]

B0Lemma: toplantı, B0POS: Noun, B0Token: toplantıda, B1Lemma: ,, B1POS: Punc, B1Token: ,, S0B0Distance: 1, S0B0Lemma: ön_plan___toplantı, S0B0LemmaPOS: ön_plan___Noun, S0B0POS: Adj_Noun_Adj_Noun, S0B0POSLemma: Adj_Noun_Adj_toplantı, S0B0Token: ön_plana_çıktığı_toplantıda, S0B1Lemma: ön_plan___,, S0B1LemmaPOS: ön_plan___Punc, S0B1POS: Adj_Noun_Adj_Punc, S0B1POSLemma: Adj_Noun_Adj_,, S0B1Token: ön_plana_çıktığı_,, S0Lemma: ön_plan__, S0POS: Adj_Noun_Adj, S0Token: ön_plana_çıktığı, transitionHistoryLength1: 1, transitionHistoryLength2: 10, transitionHistoryLength3: 102, 

76- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [toplantıda, ,, Dışişleri ,.. ]

B0Lemma: toplantı, B0POS: Noun, B0Token: toplantıda, B1Lemma: ,, B1POS: Punc, B1Token: ,, transitionHistoryLength1: 1, transitionHistoryLength2: 11, transitionHistoryLength3: 110, 

77- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [toplantıda]   B= [,, Dışişleri, bakanları ,.. ]

B0Lemma: ,, B0POS: Punc, B0Token: ,, B1Lemma: dışişleri, B1POS: Noun, B1Token: Dışişleri, S0B0Distance: 1, S0B0Lemma: toplantı_,, S0B0LemmaPOS: toplantı_Punc, S0B0POS: Noun_Punc, S0B0POSLemma: Noun_,, S0B0Token: toplantıda_,, S0B1Lemma: toplantı_dışişleri, S0B1LemmaPOS: toplantı_Noun, S0B1POS: Noun_Noun, S0B1POSLemma: Noun_dışişleri, S0B1Token: toplantıda_Dışişleri, S0Lemma: toplantı, S0POS: Noun, S0Token: toplantıda, hasRighDep_PUNCTUATION: true, toplantı_,_hasRighDep_PUNCTUATION: true, toplantı_hasRighDep_PUNCTUATION: true, toplantı_isGouvernedBy_tartış: true, toplantı_isGouvernedBy_tartış_MODIFIER: true, transitionHistoryLength1: 2, transitionHistoryLength2: 21, transitionHistoryLength3: 211, 

78- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, Dışişleri, bakanları ,.. ]

B0Lemma: ,, B0POS: Punc, B0Token: ,, B1Lemma: dışişleri, B1POS: Noun, B1Token: Dışişleri, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 021, 

79- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [Dışişleri, bakanları, 9 ,.. ]

B0Lemma: dışişleri, B0POS: Noun, B0Token: Dışişleri, B1Lemma: bakan, B1POS: Noun, B1Token: bakanları, S0B0Distance: 1, S0B0Lemma: ,_dışişleri, S0B0LemmaPOS: ,_Noun, S0B0POS: Punc_Noun, S0B0POSLemma: Punc_dışişleri, S0B0Token: ,_Dışişleri, S0B1Lemma: ,_bakan, S0B1LemmaPOS: ,_Noun, S0B1POS: Punc_Noun, S0B1POSLemma: Punc_bakan, S0B1Token: ,_bakanları, S0Lemma: ,, S0POS: Punc, S0Token: ,, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

80- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Dışişleri, bakanları, 9 ,.. ]

B0Lemma: dışişleri, B0POS: Noun, B0Token: Dışişleri, B1Lemma: bakan, B1POS: Noun, B1Token: bakanları, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

81- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Dışişleri]   B= [bakanları, 9, Kasım'da ,.. ]

B0Lemma: bakan, B0POS: Noun, B0Token: bakanları, B1Lemma: 9, B1POS: Adj, B1Token: 9, S0B0Distance: 1, S0B0Lemma: dışişleri_bakan, S0B0LemmaPOS: dışişleri_Noun, S0B0POS: Noun_Noun, S0B0POSLemma: Noun_bakan, S0B0Token: Dışişleri_bakanları, S0B1Lemma: dışişleri_9, S0B1LemmaPOS: dışişleri_Adj, S0B1POS: Noun_Adj, S0B1POSLemma: Noun_9, S0B1Token: Dışişleri_9, S0Lemma: dışişleri, S0POS: Noun, S0Token: Dışişleri, dışişleri_isGouvernedBy_tartış: true, dışişleri_isGouvernedBy_tartış_SUBJECT: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

82- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [bakanları, 9, Kasım'da ,.. ]

B0Lemma: bakan, B0POS: Noun, B0Token: bakanları, B1Lemma: 9, B1POS: Adj, B1Token: 9, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

83- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [bakanları]   B= [9, Kasım'da, Ankara'da ,.. ]

B0Lemma: 9, B0POS: Adj, B0Token: 9, B1Lemma: Kasım, B1POS: Noun, B1Token: Kasım'da, S0B0Distance: 1, S0B0Lemma: bakan_9, S0B0LemmaPOS: bakan_Adj, S0B0POS: Noun_Adj, S0B0POSLemma: Noun_9, S0B0Token: bakanları_9, S0B1Lemma: bakan_Kasım, S0B1LemmaPOS: bakan_Noun, S0B1POS: Noun_Noun, S0B1POSLemma: Noun_Kasım, S0B1Token: bakanları_Kasım'da, S0Lemma: bakan, S0POS: Noun, S0Token: bakanları, bakan_isGouvernedBy_tartış: true, bakan_isGouvernedBy_tartış_OBJECT: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

84- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [9, Kasım'da, Ankara'da ,.. ]

B0Lemma: 9, B0POS: Adj, B0Token: 9, B1Lemma: Kasım, B1POS: Noun, B1Token: Kasım'da, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

85- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [9]   B= [Kasım'da, Ankara'da, _ ,.. ]

9_isGouvernedBy_Kasım: true, 9_isGouvernedBy_Kasım_MODIFIER: true, B0Lemma: Kasım, B0POS: Noun, B0Token: Kasım'da, B1Lemma: Ankara, B1POS: Noun, B1Token: Ankara'da, S0B0Distance: 1, S0B0Lemma: 9_Kasım, S0B0LemmaPOS: 9_Noun, S0B0POS: Adj_Noun, S0B0POSLemma: Adj_Kasım, S0B0Token: 9_Kasım'da, S0B1Lemma: 9_Ankara, S0B1LemmaPOS: 9_Noun, S0B1POS: Adj_Noun, S0B1POSLemma: Adj_Ankara, S0B1Token: 9_Ankara'da, S0Lemma: 9, S0POS: Adj, S0Token: 9, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

86- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Kasım'da, Ankara'da, _ ,.. ]

B0Lemma: Kasım, B0POS: Noun, B0Token: Kasım'da, B1Lemma: Ankara, B1POS: Noun, B1Token: Ankara'da, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

87- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Kasım'da]   B= [Ankara'da, _, _ ,.. ]

B0Lemma: Ankara, B0POS: Noun, B0Token: Ankara'da, B1Lemma: şekil, B1POS: Noun, B1Token: _, Kasım_isGouvernedBy_tartış: true, Kasım_isGouvernedBy_tartış_MODIFIER: true, S0B0Distance: 1, S0B0Lemma: Kasım_Ankara, S0B0LemmaPOS: Kasım_Noun, S0B0POS: Noun_Noun, S0B0POSLemma: Noun_Ankara, S0B0Token: Kasım'da_Ankara'da, S0B1Lemma: Kasım_şekil, S0B1LemmaPOS: Kasım_Noun, S0B1POS: Noun_Noun, S0B1POSLemma: Noun_şekil, S0B1Token: Kasım'da__, S0Lemma: Kasım, S0POS: Noun, S0Token: Kasım'da, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

88- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Ankara'da, _, _ ,.. ]

B0Lemma: Ankara, B0POS: Noun, B0Token: Ankara'da, B1Lemma: şekil, B1POS: Noun, B1Token: _, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

89- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Ankara'da]   B= [_, _, şekillenen ,.. ]

Ankara_isGouvernedBy_tartış: true, Ankara_isGouvernedBy_tartış_MODIFIER: true, B0Lemma: şekil, B0POS: Noun, B0Token: _, B1Lemma: _, B1POS: Verb, B1Token: _, S0B0Distance: 1, S0B0Lemma: Ankara_şekil, S0B0LemmaPOS: Ankara_Noun, S0B0POS: Noun_Noun, S0B0POSLemma: Noun_şekil, S0B0Token: Ankara'da__, S0B1Lemma: Ankara__, S0B1LemmaPOS: Ankara_Verb, S0B1POS: Noun_Verb, S0B1POSLemma: Noun__, S0B1Token: Ankara'da__, S0Lemma: Ankara, S0POS: Noun, S0Token: Ankara'da, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

90- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [_, _, şekillenen ,.. ]

B0Lemma: şekil, B0POS: Noun, B0Token: _, B1Lemma: _, B1POS: Verb, B1Token: _, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

91- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [_]   B= [_, şekillenen, raporu ,.. ]

B0Lemma: _, B0POS: Verb, B0Token: _, B1Lemma: _, B1POS: Adj, B1Token: şekillenen, S0B0Distance: 1, S0B0Lemma: şekil__, S0B0LemmaPOS: şekil_Verb, S0B0POS: Noun_Verb, S0B0POSLemma: Noun__, S0B0Token: ___, S0B1Lemma: şekil__, S0B1LemmaPOS: şekil_Adj, S0B1POS: Noun_Adj, S0B1POSLemma: Noun__, S0B1Token: __şekillenen, S0Lemma: şekil, S0POS: Noun, S0Token: _, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, şekil_isGouvernedBy__: true, şekil_isGouvernedBy___DERIV: true, 

92- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [_, şekillenen, raporu ,.. ]

B0Lemma: _, B0POS: Verb, B0Token: _, B1Lemma: _, B1POS: Adj, B1Token: şekillenen, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

93- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [_]   B= [şekillenen, raporu, tartışacak ,.. ]

B0Lemma: _, B0POS: Adj, B0Token: şekillenen, B1Lemma: rapor, B1POS: Noun, B1Token: raporu, S0B0Distance: 1, S0B0Lemma: ___, S0B0LemmaPOS: __Adj, S0B0POS: Verb_Adj, S0B0POSLemma: Verb__, S0B0Token: __şekillenen, S0B1Lemma: __rapor, S0B1LemmaPOS: __Noun, S0B1POS: Verb_Noun, S0B1POSLemma: Verb_rapor, S0B1Token: __raporu, S0Lemma: _, S0POS: Verb, S0Token: _, __isGouvernedBy__: true, __isGouvernedBy___DERIV: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

94- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [şekillenen, raporu, tartışacak ,.. ]

B0Lemma: _, B0POS: Adj, B0Token: şekillenen, B1Lemma: rapor, B1POS: Noun, B1Token: raporu, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

95- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [şekillenen]   B= [raporu, tartışacak, . ,.. ]

B0Lemma: rapor, B0POS: Noun, B0Token: raporu, B1Lemma: tartış, B1POS: Verb, B1Token: tartışacak, S0B0Distance: 1, S0B0Lemma: __rapor, S0B0LemmaPOS: __Noun, S0B0POS: Adj_Noun, S0B0POSLemma: Adj_rapor, S0B0Token: şekillenen_raporu, S0B1Lemma: __tartış, S0B1LemmaPOS: __Verb, S0B1POS: Adj_Verb, S0B1POSLemma: Adj_tartış, S0B1Token: şekillenen_tartışacak, S0Lemma: _, S0POS: Adj, S0Token: şekillenen, __isGouvernedBy_rapor: true, __isGouvernedBy_rapor_MODIFIER: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

96- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [raporu, tartışacak, . ,.. ]

B0Lemma: rapor, B0POS: Noun, B0Token: raporu, B1Lemma: tartış, B1POS: Verb, B1Token: tartışacak, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

97- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [raporu]   B= [tartışacak, ., Merkez ,.. ]

B0Lemma: tartış, B0POS: Verb, B0Token: tartışacak, B1Lemma: ., B1POS: Punc, B1Token: ., S0B0Distance: 1, S0B0Lemma: rapor_tartış, S0B0LemmaPOS: rapor_Verb, S0B0POS: Noun_Verb, S0B0POSLemma: Noun_tartış, S0B0Token: raporu_tartışacak, S0B1Lemma: rapor_., S0B1LemmaPOS: rapor_Punc, S0B1POS: Noun_Punc, S0B1POSLemma: Noun_., S0B1Token: raporu_., S0Lemma: rapor, S0POS: Noun, S0Token: raporu, rapor_isGouvernedBy_tartış: true, rapor_isGouvernedBy_tartış_OBJECT: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

98- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [tartışacak, ., Merkez ,.. ]

B0Lemma: tartış, B0POS: Verb, B0Token: tartışacak, B1Lemma: ., B1POS: Punc, B1Token: ., transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

99- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [tartışacak]   B= [., Merkez, bankalarının ,.. ]

B0Lemma: ., B0POS: Punc, B0Token: ., B1Lemma: merkez, B1POS: Noun, B1Token: Merkez, S0B0Distance: 1, S0B0Lemma: tartış_., S0B0LemmaPOS: tartış_Punc, S0B0POS: Verb_Punc, S0B0POSLemma: Verb_., S0B0Token: tartışacak_., S0B1Lemma: tartış_merkez, S0B1LemmaPOS: tartış_Noun, S0B1POS: Verb_Noun, S0B1POSLemma: Verb_merkez, S0B1Token: tartışacak_Merkez, S0Lemma: tartış, S0POS: Verb, S0Token: tartışacak, hasRighDep_PUNCTUATION: true, tartış_._hasRighDep_PUNCTUATION: true, tartış_hasRighDep_PUNCTUATION: true, tartış_isGouvernedBy_al: true, tartış_isGouvernedBy_al_COORDINATION: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

100- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [., Merkez, bankalarının ,.. ]

B0Lemma: ., B0POS: Punc, B0Token: ., B1Lemma: merkez, B1POS: Noun, B1Token: Merkez, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

101- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [Merkez, bankalarının, arasında ,.. ]

B0Lemma: merkez, B0POS: Noun, B0Token: Merkez, B1Lemma: banka, B1POS: Noun, B1Token: bankalarının, S0B0Distance: 1, S0B0Lemma: ._merkez, S0B0LemmaPOS: ._Noun, S0B0POS: Punc_Noun, S0B0POSLemma: Punc_merkez, S0B0Token: ._Merkez, S0B1Lemma: ._banka, S0B1LemmaPOS: ._Noun, S0B1POS: Punc_Noun, S0B1POSLemma: Punc_banka, S0B1Token: ._bankalarının, S0Lemma: ., S0POS: Punc, S0Token: ., transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

102- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Merkez, bankalarının, arasında ,.. ]

B0Lemma: merkez, B0POS: Noun, B0Token: Merkez, B1Lemma: banka, B1POS: Noun, B1Token: bankalarının, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

103- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Merkez]   B= [bankalarının, arasında, işbirliği ,.. ]

B0Lemma: banka, B0POS: Noun, B0Token: bankalarının, B1Lemma: ara, B1POS: Noun, B1Token: arasında, S0B0Distance: 1, S0B0Lemma: merkez_banka, S0B0LemmaPOS: merkez_Noun, S0B0POS: Noun_Noun, S0B0POSLemma: Noun_banka, S0B0Token: Merkez_bankalarının, S0B1Lemma: merkez_ara, S0B1LemmaPOS: merkez_Noun, S0B1POS: Noun_Noun, S0B1POSLemma: Noun_ara, S0B1Token: Merkez_arasında, S0Lemma: merkez, S0POS: Noun, S0Token: Merkez, merkez_isGouvernedBy_banka: true, merkez_isGouvernedBy_banka_MWE: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

104- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [bankalarının, arasında, işbirliği ,.. ]

B0Lemma: banka, B0POS: Noun, B0Token: bankalarının, B1Lemma: ara, B1POS: Noun, B1Token: arasında, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

105- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [bankalarının]   B= [arasında, işbirliği, , ,.. ]

B0Lemma: ara, B0POS: Noun, B0Token: arasında, B1Lemma: işbirliği, B1POS: Noun, B1Token: işbirliği, S0B0Distance: 1, S0B0Lemma: banka_ara, S0B0LemmaPOS: banka_Noun, S0B0POS: Noun_Noun, S0B0POSLemma: Noun_ara, S0B0Token: bankalarının_arasında, S0B1Lemma: banka_işbirliği, S0B1LemmaPOS: banka_Noun, S0B1POS: Noun_Noun, S0B1POSLemma: Noun_işbirliği, S0B1Token: bankalarının_işbirliği, S0Lemma: banka, S0POS: Noun, S0Token: bankalarının, banka_isGouvernedBy_ara: true, banka_isGouvernedBy_ara_POSSESSOR: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

106- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [arasında, işbirliği, , ,.. ]

B0Lemma: ara, B0POS: Noun, B0Token: arasında, B1Lemma: işbirliği, B1POS: Noun, B1Token: işbirliği, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

107- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [arasında]   B= [işbirliği, ,, ortak ,.. ]

B0Lemma: işbirliği, B0POS: Noun, B0Token: işbirliği, B1Lemma: ,, B1POS: Punc, B1Token: ,, S0B0Distance: 1, S0B0Lemma: ara_işbirliği, S0B0LemmaPOS: ara_Noun, S0B0POS: Noun_Noun, S0B0POSLemma: Noun_işbirliği, S0B0Token: arasında_işbirliği, S0B1Lemma: ara_,, S0B1LemmaPOS: ara_Punc, S0B1POS: Noun_Punc, S0B1POSLemma: Noun_,, S0B1Token: arasında_,, S0Lemma: ara, S0POS: Noun, S0Token: arasında, ara_isGouvernedBy_al: true, ara_isGouvernedBy_al_MODIFIER: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

108- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [işbirliği, ,, ortak ,.. ]

B0Lemma: işbirliği, B0POS: Noun, B0Token: işbirliği, B1Lemma: ,, B1POS: Punc, B1Token: ,, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

109- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [işbirliği]   B= [,, ortak, yatırımları ,.. ]

B0Lemma: ,, B0POS: Punc, B0Token: ,, B1Lemma: ortak, B1POS: Adj, B1Token: ortak, S0B0Distance: 1, S0B0Lemma: işbirliği_,, S0B0LemmaPOS: işbirliği_Punc, S0B0POS: Noun_Punc, S0B0POSLemma: Noun_,, S0B0Token: işbirliği_,, S0B1Lemma: işbirliği_ortak, S0B1LemmaPOS: işbirliği_Adj, S0B1POS: Noun_Adj, S0B1POSLemma: Noun_ortak, S0B1Token: işbirliği_ortak, S0Lemma: işbirliği, S0POS: Noun, S0Token: işbirliği, hasRighDep_PUNCTUATION: true, işbirliği_,_hasRighDep_PUNCTUATION: true, işbirliği_hasRighDep_PUNCTUATION: true, işbirliği_isGouvernedBy_al: true, işbirliği_isGouvernedBy_al_SUBJECT: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

110- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, ortak, yatırımları ,.. ]

B0Lemma: ,, B0POS: Punc, B0Token: ,, B1Lemma: ortak, B1POS: Adj, B1Token: ortak, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

111- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [ortak, yatırımları, teşvik ,.. ]

B0Lemma: ortak, B0POS: Adj, B0Token: ortak, B1Lemma: yatırım, B1POS: Noun, B1Token: yatırımları, S0B0Distance: 1, S0B0Lemma: ,_ortak, S0B0LemmaPOS: ,_Adj, S0B0POS: Punc_Adj, S0B0POSLemma: Punc_ortak, S0B0Token: ,_ortak, S0B1Lemma: ,_yatırım, S0B1LemmaPOS: ,_Noun, S0B1POS: Punc_Noun, S0B1POSLemma: Punc_yatırım, S0B1Token: ,_yatırımları, S0Lemma: ,, S0POS: Punc, S0Token: ,, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

112- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ortak, yatırımları, teşvik ,.. ]

B0Lemma: ortak, B0POS: Adj, B0Token: ortak, B1Lemma: yatırım, B1POS: Noun, B1Token: yatırımları, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

113- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ortak]   B= [yatırımları, teşvik, , ,.. ]

B0Lemma: yatırım, B0POS: Noun, B0Token: yatırımları, B1Lemma: teşvik, B1POS: Noun, B1Token: teşvik, S0B0Distance: 1, S0B0Lemma: ortak_yatırım, S0B0LemmaPOS: ortak_Noun, S0B0POS: Adj_Noun, S0B0POSLemma: Adj_yatırım, S0B0Token: ortak_yatırımları, S0B1Lemma: ortak_teşvik, S0B1LemmaPOS: ortak_Noun, S0B1POS: Adj_Noun, S0B1POSLemma: Adj_teşvik, S0B1Token: ortak_teşvik, S0Lemma: ortak, S0POS: Adj, S0Token: ortak, ortak_isGouvernedBy_yatırım: true, ortak_isGouvernedBy_yatırım_MODIFIER: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

114- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [yatırımları, teşvik, , ,.. ]

B0Lemma: yatırım, B0POS: Noun, B0Token: yatırımları, B1Lemma: teşvik, B1POS: Noun, B1Token: teşvik, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

115- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [yatırımları]   B= [teşvik, ,, ortak ,.. ]

B0Lemma: teşvik, B0POS: Noun, B0Token: teşvik, B1Lemma: ,, B1POS: Punc, B1Token: ,, S0B0Distance: 1, S0B0Lemma: yatırım_teşvik, S0B0LemmaPOS: yatırım_Noun, S0B0POS: Noun_Noun, S0B0POSLemma: Noun_teşvik, S0B0Token: yatırımları_teşvik, S0B1Lemma: yatırım_,, S0B1LemmaPOS: yatırım_Punc, S0B1POS: Noun_Punc, S0B1POSLemma: Noun_,, S0B1Token: yatırımları_,, S0Lemma: yatırım, S0POS: Noun, S0Token: yatırımları, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, yatırım_isGouvernedBy_al: true, yatırım_isGouvernedBy_al_OBJECT: true, 

116- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [teşvik, ,, ortak ,.. ]

B0Lemma: teşvik, B0POS: Noun, B0Token: teşvik, B1Lemma: ,, B1POS: Punc, B1Token: ,, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

117- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [teşvik]   B= [,, ortak, özelleştirmelerin ,.. ]

B0Lemma: ,, B0POS: Punc, B0Token: ,, B1Lemma: ortak, B1POS: Adj, B1Token: ortak, S0B0Distance: 1, S0B0Lemma: teşvik_,, S0B0LemmaPOS: teşvik_Punc, S0B0POS: Noun_Punc, S0B0POSLemma: Noun_,, S0B0Token: teşvik_,, S0B1Lemma: teşvik_ortak, S0B1LemmaPOS: teşvik_Adj, S0B1POS: Noun_Adj, S0B1POSLemma: Noun_ortak, S0B1Token: teşvik_ortak, S0Lemma: teşvik, S0POS: Noun, S0Token: teşvik, hasRighDep_PUNCTUATION: true, teşvik_,_hasRighDep_PUNCTUATION: true, teşvik_hasRighDep_PUNCTUATION: true, teşvik_isGouvernedBy_al: true, teşvik_isGouvernedBy_al_SUBJECT: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

118- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, ortak, özelleştirmelerin ,.. ]

B0Lemma: ,, B0POS: Punc, B0Token: ,, B1Lemma: ortak, B1POS: Adj, B1Token: ortak, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

119- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [ortak, özelleştirmelerin, _ ,.. ]

B0Lemma: ortak, B0POS: Adj, B0Token: ortak, B1Lemma: özelleştirme, B1POS: Noun, B1Token: özelleştirmelerin, S0B0Distance: 1, S0B0Lemma: ,_ortak, S0B0LemmaPOS: ,_Adj, S0B0POS: Punc_Adj, S0B0POSLemma: Punc_ortak, S0B0Token: ,_ortak, S0B1Lemma: ,_özelleştirme, S0B1LemmaPOS: ,_Noun, S0B1POS: Punc_Noun, S0B1POSLemma: Punc_özelleştirme, S0B1Token: ,_özelleştirmelerin, S0Lemma: ,, S0POS: Punc, S0Token: ,, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

120- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ortak, özelleştirmelerin, _ ,.. ]

B0Lemma: ortak, B0POS: Adj, B0Token: ortak, B1Lemma: özelleştirme, B1POS: Noun, B1Token: özelleştirmelerin, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

121- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ortak]   B= [özelleştirmelerin, _, öngörüldüğü ,.. ]

B0Lemma: özelleştirme, B0POS: Noun, B0Token: özelleştirmelerin, B1Lemma: öngör, B1POS: Verb, B1Token: _, S0B0Distance: 1, S0B0Lemma: ortak_özelleştirme, S0B0LemmaPOS: ortak_Noun, S0B0POS: Adj_Noun, S0B0POSLemma: Adj_özelleştirme, S0B0Token: ortak_özelleştirmelerin, S0B1Lemma: ortak_öngör, S0B1LemmaPOS: ortak_Verb, S0B1POS: Adj_Verb, S0B1POSLemma: Adj_öngör, S0B1Token: ortak__, S0Lemma: ortak, S0POS: Adj, S0Token: ortak, ortak_isGouvernedBy_özelleştirme: true, ortak_isGouvernedBy_özelleştirme_MODIFIER: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

122- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [özelleştirmelerin, _, öngörüldüğü ,.. ]

B0Lemma: özelleştirme, B0POS: Noun, B0Token: özelleştirmelerin, B1Lemma: öngör, B1POS: Verb, B1Token: _, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

123- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [özelleştirmelerin]   B= [_, öngörüldüğü, raporda ,.. ]

B0Lemma: öngör, B0POS: Verb, B0Token: _, B1Lemma: _, B1POS: Adj, B1Token: öngörüldüğü, S0B0Distance: 1, S0B0Lemma: özelleştirme_öngör, S0B0LemmaPOS: özelleştirme_Verb, S0B0POS: Noun_Verb, S0B0POSLemma: Noun_öngör, S0B0Token: özelleştirmelerin__, S0B1Lemma: özelleştirme__, S0B1LemmaPOS: özelleştirme_Adj, S0B1POS: Noun_Adj, S0B1POSLemma: Noun__, S0B1Token: özelleştirmelerin_öngörüldüğü, S0Lemma: özelleştirme, S0POS: Noun, S0Token: özelleştirmelerin, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, özelleştirme_isGouvernedBy__: true, özelleştirme_isGouvernedBy___POSSESSOR: true, 

124- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [_, öngörüldüğü, raporda ,.. ]

B0Lemma: öngör, B0POS: Verb, B0Token: _, B1Lemma: _, B1POS: Adj, B1Token: öngörüldüğü, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

125- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [_]   B= [öngörüldüğü, raporda, , ,.. ]

B0Lemma: _, B0POS: Adj, B0Token: öngörüldüğü, B1Lemma: rapor, B1POS: Noun, B1Token: raporda, S0B0Distance: 1, S0B0Lemma: öngör__, S0B0LemmaPOS: öngör_Adj, S0B0POS: Verb_Adj, S0B0POSLemma: Verb__, S0B0Token: __öngörüldüğü, S0B1Lemma: öngör_rapor, S0B1LemmaPOS: öngör_Noun, S0B1POS: Verb_Noun, S0B1POSLemma: Verb_rapor, S0B1Token: __raporda, S0Lemma: öngör, S0POS: Verb, S0Token: _, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, öngör_isGouvernedBy__: true, öngör_isGouvernedBy___DERIV: true, 

126- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [öngörüldüğü, raporda, , ,.. ]

B0Lemma: _, B0POS: Adj, B0Token: öngörüldüğü, B1Lemma: rapor, B1POS: Noun, B1Token: raporda, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

127- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [öngörüldüğü]   B= [raporda, ,, tarafların ,.. ]

B0Lemma: rapor, B0POS: Noun, B0Token: raporda, B1Lemma: ,, B1POS: Punc, B1Token: ,, S0B0Distance: 1, S0B0Lemma: __rapor, S0B0LemmaPOS: __Noun, S0B0POS: Adj_Noun, S0B0POSLemma: Adj_rapor, S0B0Token: öngörüldüğü_raporda, S0B1Lemma: __,, S0B1LemmaPOS: __Punc, S0B1POS: Adj_Punc, S0B1POSLemma: Adj_,, S0B1Token: öngörüldüğü_,, S0Lemma: _, S0POS: Adj, S0Token: öngörüldüğü, __isGouvernedBy_rapor: true, __isGouvernedBy_rapor_MODIFIER: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

128- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [raporda, ,, tarafların ,.. ]

B0Lemma: rapor, B0POS: Noun, B0Token: raporda, B1Lemma: ,, B1POS: Punc, B1Token: ,, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

129- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [raporda]   B= [,, tarafların, serbest ,.. ]

B0Lemma: ,, B0POS: Punc, B0Token: ,, B1Lemma: taraf, B1POS: Noun, B1Token: tarafların, S0B0Distance: 1, S0B0Lemma: rapor_,, S0B0LemmaPOS: rapor_Punc, S0B0POS: Noun_Punc, S0B0POSLemma: Noun_,, S0B0Token: raporda_,, S0B1Lemma: rapor_taraf, S0B1LemmaPOS: rapor_Noun, S0B1POS: Noun_Noun, S0B1POSLemma: Noun_taraf, S0B1Token: raporda_tarafların, S0Lemma: rapor, S0POS: Noun, S0Token: raporda, hasRighDep_PUNCTUATION: true, rapor_,_hasRighDep_PUNCTUATION: true, rapor_hasRighDep_PUNCTUATION: true, rapor_isGouvernedBy_al: true, rapor_isGouvernedBy_al_MODIFIER: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

130- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, tarafların, serbest ,.. ]

B0Lemma: ,, B0POS: Punc, B0Token: ,, B1Lemma: taraf, B1POS: Noun, B1Token: tarafların, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

131- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [tarafların, serbest, ticaret ,.. ]

B0Lemma: taraf, B0POS: Noun, B0Token: tarafların, B1Lemma: serbest, B1POS: Adj, B1Token: serbest, S0B0Distance: 1, S0B0Lemma: ,_taraf, S0B0LemmaPOS: ,_Noun, S0B0POS: Punc_Noun, S0B0POSLemma: Punc_taraf, S0B0Token: ,_tarafların, S0B1Lemma: ,_serbest, S0B1LemmaPOS: ,_Adj, S0B1POS: Punc_Adj, S0B1POSLemma: Punc_serbest, S0B1Token: ,_serbest, S0Lemma: ,, S0POS: Punc, S0Token: ,, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

132- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [tarafların, serbest, ticaret ,.. ]

B0Lemma: taraf, B0POS: Noun, B0Token: tarafların, B1Lemma: serbest, B1POS: Adj, B1Token: serbest, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

133- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [tarafların]   B= [serbest, ticaret, bölgesi ,.. ]

B0Lemma: serbest, B0POS: Adj, B0Token: serbest, B1Lemma: ticaret, B1POS: Noun, B1Token: ticaret, S0B0Distance: 1, S0B0Lemma: taraf_serbest, S0B0LemmaPOS: taraf_Adj, S0B0POS: Noun_Adj, S0B0POSLemma: Noun_serbest, S0B0Token: tarafların_serbest, S0B1Lemma: taraf_ticaret, S0B1LemmaPOS: taraf_Noun, S0B1POS: Noun_Noun, S0B1POSLemma: Noun_ticaret, S0B1Token: tarafların_ticaret, S0Lemma: taraf, S0POS: Noun, S0Token: tarafların, taraf_isGouvernedBy_bölge: true, taraf_isGouvernedBy_bölge_POSSESSOR: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

134- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [serbest, ticaret, bölgesi ,.. ]

B0Lemma: serbest, B0POS: Adj, B0Token: serbest, B1Lemma: ticaret, B1POS: Noun, B1Token: ticaret, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

135- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [serbest]   B= [ticaret, bölgesi, _ ,.. ]

B0Lemma: ticaret, B0POS: Noun, B0Token: ticaret, B1Lemma: bölge, B1POS: Noun, B1Token: bölgesi, S0B0Distance: 1, S0B0Lemma: serbest_ticaret, S0B0LemmaPOS: serbest_Noun, S0B0POS: Adj_Noun, S0B0POSLemma: Adj_ticaret, S0B0Token: serbest_ticaret, S0B1Lemma: serbest_bölge, S0B1LemmaPOS: serbest_Noun, S0B1POS: Adj_Noun, S0B1POSLemma: Adj_bölge, S0B1Token: serbest_bölgesi, S0Lemma: serbest, S0POS: Adj, S0Token: serbest, serbest_isGouvernedBy_ticaret: true, serbest_isGouvernedBy_ticaret_MODIFIER: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

136- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ticaret, bölgesi, _ ,.. ]

B0Lemma: ticaret, B0POS: Noun, B0Token: ticaret, B1Lemma: bölge, B1POS: Noun, B1Token: bölgesi, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

137- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ticaret]   B= [bölgesi, _, kurmaları ,.. ]

B0Lemma: bölge, B0POS: Noun, B0Token: bölgesi, B1Lemma: kur, B1POS: Verb, B1Token: _, S0B0Distance: 1, S0B0Lemma: ticaret_bölge, S0B0LemmaPOS: ticaret_Noun, S0B0POS: Noun_Noun, S0B0POSLemma: Noun_bölge, S0B0Token: ticaret_bölgesi, S0B1Lemma: ticaret_kur, S0B1LemmaPOS: ticaret_Verb, S0B1POS: Noun_Verb, S0B1POSLemma: Noun_kur, S0B1Token: ticaret__, S0Lemma: ticaret, S0POS: Noun, S0Token: ticaret, ticaret_isGouvernedBy_bölge: true, ticaret_isGouvernedBy_bölge_POSSESSOR: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

138- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [bölgesi, _, kurmaları ,.. ]

B0Lemma: bölge, B0POS: Noun, B0Token: bölgesi, B1Lemma: kur, B1POS: Verb, B1Token: _, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

139- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [bölgesi]   B= [_, kurmaları, , ,.. ]

B0Lemma: kur, B0POS: Verb, B0Token: _, B1Lemma: _, B1POS: Noun, B1Token: kurmaları, S0B0Distance: 1, S0B0Lemma: bölge_kur, S0B0LemmaPOS: bölge_Verb, S0B0POS: Noun_Verb, S0B0POSLemma: Noun_kur, S0B0Token: bölgesi__, S0B1Lemma: bölge__, S0B1LemmaPOS: bölge_Noun, S0B1POS: Noun_Noun, S0B1POSLemma: Noun__, S0B1Token: bölgesi_kurmaları, S0Lemma: bölge, S0POS: Noun, S0Token: bölgesi, bölge_isGouvernedBy__: true, bölge_isGouvernedBy___OBJECT: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

140- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [_, kurmaları, , ,.. ]

B0Lemma: kur, B0POS: Verb, B0Token: _, B1Lemma: _, B1POS: Noun, B1Token: kurmaları, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

141- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [_]   B= [kurmaları, ,, ticari ,.. ]

B0Lemma: _, B0POS: Noun, B0Token: kurmaları, B1Lemma: ,, B1POS: Punc, B1Token: ,, S0B0Distance: 1, S0B0Lemma: kur__, S0B0LemmaPOS: kur_Noun, S0B0POS: Verb_Noun, S0B0POSLemma: Verb__, S0B0Token: __kurmaları, S0B1Lemma: kur_,, S0B1LemmaPOS: kur_Punc, S0B1POS: Verb_Punc, S0B1POSLemma: Verb_,, S0B1Token: __,, S0Lemma: kur, S0POS: Verb, S0Token: _, kur_isGouvernedBy__: true, kur_isGouvernedBy___DERIV: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

142- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [kurmaları, ,, ticari ,.. ]

B0Lemma: _, B0POS: Noun, B0Token: kurmaları, B1Lemma: ,, B1POS: Punc, B1Token: ,, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

143- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [kurmaları]   B= [,, ticari, engellerin ,.. ]

B0Lemma: ,, B0POS: Punc, B0Token: ,, B1Lemma: ticari, B1POS: Adj, B1Token: ticari, S0B0Distance: 1, S0B0Lemma: __,, S0B0LemmaPOS: __Punc, S0B0POS: Noun_Punc, S0B0POSLemma: Noun_,, S0B0Token: kurmaları_,, S0B1Lemma: __ticari, S0B1LemmaPOS: __Adj, S0B1POS: Noun_Adj, S0B1POSLemma: Noun_ticari, S0B1Token: kurmaları_ticari, S0Lemma: _, S0POS: Noun, S0Token: kurmaları, __,_hasRighDep_PUNCTUATION: true, __hasRighDep_PUNCTUATION: true, __isGouvernedBy__: true, __isGouvernedBy___COORDINATION: true, hasRighDep_PUNCTUATION: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

144- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, ticari, engellerin ,.. ]

B0Lemma: ,, B0POS: Punc, B0Token: ,, B1Lemma: ticari, B1POS: Adj, B1Token: ticari, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

145- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [ticari, engellerin, _ ,.. ]

B0Lemma: ticari, B0POS: Adj, B0Token: ticari, B1Lemma: engel, B1POS: Noun, B1Token: engellerin, S0B0Distance: 1, S0B0Lemma: ,_ticari, S0B0LemmaPOS: ,_Adj, S0B0POS: Punc_Adj, S0B0POSLemma: Punc_ticari, S0B0Token: ,_ticari, S0B1Lemma: ,_engel, S0B1LemmaPOS: ,_Noun, S0B1POS: Punc_Noun, S0B1POSLemma: Punc_engel, S0B1Token: ,_engellerin, S0Lemma: ,, S0POS: Punc, S0Token: ,, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

146- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ticari, engellerin, _ ,.. ]

B0Lemma: ticari, B0POS: Adj, B0Token: ticari, B1Lemma: engel, B1POS: Noun, B1Token: engellerin, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

147- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ticari]   B= [engellerin, _, kaldırılması ,.. ]

B0Lemma: engel, B0POS: Noun, B0Token: engellerin, B1Lemma: kaldır, B1POS: Verb, B1Token: _, S0B0Distance: 1, S0B0Lemma: ticari_engel, S0B0LemmaPOS: ticari_Noun, S0B0POS: Adj_Noun, S0B0POSLemma: Adj_engel, S0B0Token: ticari_engellerin, S0B1Lemma: ticari_kaldır, S0B1LemmaPOS: ticari_Verb, S0B1POS: Adj_Verb, S0B1POSLemma: Adj_kaldır, S0B1Token: ticari__, S0Lemma: ticari, S0POS: Adj, S0Token: ticari, ticari_isGouvernedBy_engel: true, ticari_isGouvernedBy_engel_MODIFIER: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

148- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [engellerin, _, kaldırılması ,.. ]

B0Lemma: engel, B0POS: Noun, B0Token: engellerin, B1Lemma: kaldır, B1POS: Verb, B1Token: _, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

149- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [engellerin]   B= [_, kaldırılması, gibi ,.. ]

B0Lemma: kaldır, B0POS: Verb, B0Token: _, B1Lemma: _, B1POS: Noun, B1Token: kaldırılması, S0B0Distance: 1, S0B0Lemma: engel_kaldır, S0B0LemmaPOS: engel_Verb, S0B0POS: Noun_Verb, S0B0POSLemma: Noun_kaldır, S0B0Token: engellerin__, S0B1Lemma: engel__, S0B1LemmaPOS: engel_Noun, S0B1POS: Noun_Noun, S0B1POSLemma: Noun__, S0B1Token: engellerin_kaldırılması, S0Lemma: engel, S0POS: Noun, S0Token: engellerin, engel_isGouvernedBy__: true, engel_isGouvernedBy___POSSESSOR: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

150- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [_, kaldırılması, gibi ,.. ]

B0Lemma: kaldır, B0POS: Verb, B0Token: _, B1Lemma: _, B1POS: Noun, B1Token: kaldırılması, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

151- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [_]   B= [kaldırılması, gibi, maddeler ,.. ]

B0Lemma: _, B0POS: Noun, B0Token: kaldırılması, B1Lemma: gibi, B1POS: Postp, B1Token: gibi, S0B0Distance: 1, S0B0Lemma: kaldır__, S0B0LemmaPOS: kaldır_Noun, S0B0POS: Verb_Noun, S0B0POSLemma: Verb__, S0B0Token: __kaldırılması, S0B1Lemma: kaldır_gibi, S0B1LemmaPOS: kaldır_Postp, S0B1POS: Verb_Postp, S0B1POSLemma: Verb_gibi, S0B1Token: __gibi, S0Lemma: kaldır, S0POS: Verb, S0Token: _, kaldır_isGouvernedBy__: true, kaldır_isGouvernedBy___DERIV: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

152- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [kaldırılması, gibi, maddeler ,.. ]

B0Lemma: _, B0POS: Noun, B0Token: kaldırılması, B1Lemma: gibi, B1POS: Postp, B1Token: gibi, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

153- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [kaldırılması]   B= [gibi, maddeler, de ,.. ]

B0Lemma: gibi, B0POS: Postp, B0Token: gibi, B1Lemma: madde, B1POS: Noun, B1Token: maddeler, S0B0Distance: 1, S0B0Lemma: __gibi, S0B0LemmaPOS: __Postp, S0B0POS: Noun_Postp, S0B0POSLemma: Noun_gibi, S0B0Token: kaldırılması_gibi, S0B1Lemma: __madde, S0B1LemmaPOS: __Noun, S0B1POS: Noun_Noun, S0B1POSLemma: Noun_madde, S0B1Token: kaldırılması_maddeler, S0Lemma: _, S0POS: Noun, S0Token: kaldırılması, __isGouvernedBy_gibi: true, __isGouvernedBy_gibi_ARGUMENT: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

154- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [gibi, maddeler, de ,.. ]

B0Lemma: gibi, B0POS: Postp, B0Token: gibi, B1Lemma: madde, B1POS: Noun, B1Token: maddeler, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

155- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [gibi]   B= [maddeler, de, yer ,.. ]

B0Lemma: madde, B0POS: Noun, B0Token: maddeler, B1Lemma: de, B1POS: Conj, B1Token: de, S0B0Distance: 1, S0B0Lemma: gibi_madde, S0B0LemmaPOS: gibi_Noun, S0B0POS: Postp_Noun, S0B0POSLemma: Postp_madde, S0B0Token: gibi_maddeler, S0B1Lemma: gibi_de, S0B1LemmaPOS: gibi_Conj, S0B1POS: Postp_Conj, S0B1POSLemma: Postp_de, S0B1Token: gibi_de, S0Lemma: gibi, S0POS: Postp, S0Token: gibi, gibi_isGouvernedBy_madde: true, gibi_isGouvernedBy_madde_MODIFIER: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

156- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [maddeler, de, yer ,.. ]

B0Lemma: madde, B0POS: Noun, B0Token: maddeler, B1Lemma: de, B1POS: Conj, B1Token: de, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

157- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [maddeler]   B= [de, yer, alıyor ,.. ]

B0Lemma: de, B0POS: Conj, B0Token: de, B1Lemma: yer, B1POS: Noun, B1Token: yer, S0B0Distance: 1, S0B0Lemma: madde_de, S0B0LemmaPOS: madde_Conj, S0B0POS: Noun_Conj, S0B0POSLemma: Noun_de, S0B0Token: maddeler_de, S0B1Lemma: madde_yer, S0B1LemmaPOS: madde_Noun, S0B1POS: Noun_Noun, S0B1POSLemma: Noun_yer, S0B1Token: maddeler_yer, S0Lemma: madde, S0POS: Noun, S0Token: maddeler, hasRighDep_INTENSIFIER: true, madde_de_hasRighDep_INTENSIFIER: true, madde_hasRighDep_INTENSIFIER: true, madde_isGouvernedBy_al: true, madde_isGouvernedBy_al_SUBJECT: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

158- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [de, yer, alıyor ,.. ]

B0Lemma: de, B0POS: Conj, B0Token: de, B1Lemma: yer, B1POS: Noun, B1Token: yer, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

159- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [de]   B= [yer, alıyor, , ,.. ]

B0Lemma: yer, B0POS: Noun, B0Token: yer, B1Lemma: al, B1POS: Verb, B1Token: alıyor, S0B0Distance: 1, S0B0Lemma: de_yer, S0B0LemmaPOS: de_Noun, S0B0POS: Conj_Noun, S0B0POSLemma: Conj_yer, S0B0Token: de_yer, S0B1Lemma: de_al, S0B1LemmaPOS: de_Verb, S0B1POS: Conj_Verb, S0B1POSLemma: Conj_al, S0B1Token: de_alıyor, S0Lemma: de, S0POS: Conj, S0Token: de, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

160- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [yer, alıyor, , ,.. ]

B0Lemma: yer, B0POS: Noun, B0Token: yer, B1Lemma: al, B1POS: Verb, B1Token: alıyor, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

161- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [yer]   B= [alıyor, ,, ancak ,.. ]

B0Lemma: al, B0POS: Verb, B0Token: alıyor, B1Lemma: ,, B1POS: Punc, B1Token: ,, S0B0Distance: 1, S0B0Lemma: yer_al, S0B0LemmaPOS: yer_Verb, S0B0POS: Noun_Verb, S0B0POSLemma: Noun_al, S0B0Token: yer_alıyor, S0B1Lemma: yer_,, S0B1LemmaPOS: yer_Punc, S0B1POS: Noun_Punc, S0B1POSLemma: Noun_,, S0B1Token: yer_,, S0Lemma: yer, S0POS: Noun, S0Token: yer, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, yer_isGouvernedBy_al: true, yer_isGouvernedBy_al_MWE: true, 

162- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [yer, alıyor]   B= [,, ancak, bu ,.. ]

B0Lemma: ,, B0POS: Punc, B0Token: ,, B1Lemma: ancak, B1POS: Conj, B1Token: ancak, S0B0Distance: 1, S0B0Lemma: al_,, S0B0LemmaPOS: al_Punc, S0B0POS: Verb_Punc, S0B0POSLemma: Verb_,, S0B0Token: alıyor_,, S0B1Lemma: al_ancak, S0B1LemmaPOS: al_Conj, S0B1POS: Verb_Conj, S0B1POSLemma: Verb_ancak, S0B1Token: alıyor_ancak, S0Lemma: al, S0POS: Verb, S0Token: alıyor, S1B0Lemma: yer_,, S1B0LemmaPOS: yer_Punc, S1B0POS: Noun_Punc, S1B0POSLemma: Noun_,, S1B0Token: yer_,, S1Lemma: yer, S1POS: Noun, S1S0Lemma: yer_al, S1S0LemmaPOS: yer_Verb, S1S0POS: Noun_Verb, S1S0POSLemma: Noun_al, S1S0Token: yer_alıyor, S1Token: yer, SyntaxicRelation: -MWE, al_,_hasRighDep_PUNCTUATION: true, al_ancak_hasRighDep_CONJUNCTION: true, al_hasRighDep_CONJUNCTION: true, al_hasRighDep_PUNCTUATION: true, al_isGouvernedBy_bul: true, al_isGouvernedBy_bul_COORDINATION: true, hasRighDep_CONJUNCTION: true, hasRighDep_PUNCTUATION: true, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

163- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[yer, alıyor]]   B= [,, ancak, bu ,.. ]

B0Lemma: ,, B0POS: Punc, B0Token: ,, B1Lemma: ancak, B1POS: Conj, B1Token: ancak, S0B0Distance: 1, S0B0Lemma: yer_al_,, S0B0LemmaPOS: yer_al_Punc, S0B0POS: Noun_Verb_Punc, S0B0POSLemma: Noun_Verb_,, S0B0Token: yer_alıyor_,, S0B1Lemma: yer_al_ancak, S0B1LemmaPOS: yer_al_Conj, S0B1POS: Noun_Verb_Conj, S0B1POSLemma: Noun_Verb_ancak, S0B1Token: yer_alıyor_ancak, S0Lemma: yer_al, S0POS: Noun_Verb, S0Token: yer_alıyor, transitionHistoryLength1: 0, transitionHistoryLength2: 00, transitionHistoryLength3: 002, 

164- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, ancak, bu ,.. ]

B0Lemma: ,, B0POS: Punc, B0Token: ,, B1Lemma: ancak, B1POS: Conj, B1Token: ancak, transitionHistoryLength1: 1, transitionHistoryLength2: 10, transitionHistoryLength3: 100, 

165- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [ancak, bu, işbirliği ,.. ]

B0Lemma: ancak, B0POS: Conj, B0Token: ancak, B1Lemma: bu, B1POS: Det, B1Token: bu, S0B0Distance: 1, S0B0Lemma: ,_ancak, S0B0LemmaPOS: ,_Conj, S0B0POS: Punc_Conj, S0B0POSLemma: Punc_ancak, S0B0Token: ,_ancak, S0B1Lemma: ,_bu, S0B1LemmaPOS: ,_Det, S0B1POS: Punc_Det, S0B1POSLemma: Punc_bu, S0B1Token: ,_bu, S0Lemma: ,, S0POS: Punc, S0Token: ,, transitionHistoryLength1: 2, transitionHistoryLength2: 21, transitionHistoryLength3: 210, 

166- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ancak, bu, işbirliği ,.. ]

B0Lemma: ancak, B0POS: Conj, B0Token: ancak, B1Lemma: bu, B1POS: Det, B1Token: bu, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 021, 

167- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ancak]   B= [bu, işbirliği, çerçevesinde ,.. ]

B0Lemma: bu, B0POS: Det, B0Token: bu, B1Lemma: işbirliği, B1POS: Noun, B1Token: işbirliği, S0B0Distance: 1, S0B0Lemma: ancak_bu, S0B0LemmaPOS: ancak_Det, S0B0POS: Conj_Det, S0B0POSLemma: Conj_bu, S0B0Token: ancak_bu, S0B1Lemma: ancak_işbirliği, S0B1LemmaPOS: ancak_Noun, S0B1POS: Conj_Noun, S0B1POSLemma: Conj_işbirliği, S0B1Token: ancak_işbirliği, S0Lemma: ancak, S0POS: Conj, S0Token: ancak, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

168- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [bu, işbirliği, çerçevesinde ,.. ]

B0Lemma: bu, B0POS: Det, B0Token: bu, B1Lemma: işbirliği, B1POS: Noun, B1Token: işbirliği, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

169- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [bu]   B= [işbirliği, çerçevesinde, gümrüklere ,.. ]

B0Lemma: işbirliği, B0POS: Noun, B0Token: işbirliği, B1Lemma: çerçeve, B1POS: Noun, B1Token: çerçevesinde, S0B0Distance: 1, S0B0Lemma: bu_işbirliği, S0B0LemmaPOS: bu_Noun, S0B0POS: Det_Noun, S0B0POSLemma: Det_işbirliği, S0B0Token: bu_işbirliği, S0B1Lemma: bu_çerçeve, S0B1LemmaPOS: bu_Noun, S0B1POS: Det_Noun, S0B1POSLemma: Det_çerçeve, S0B1Token: bu_çerçevesinde, S0Lemma: bu, S0POS: Det, S0Token: bu, bu_isGouvernedBy_işbirliği: true, bu_isGouvernedBy_işbirliği_DETERMINER: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

170- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [işbirliği, çerçevesinde, gümrüklere ,.. ]

B0Lemma: işbirliği, B0POS: Noun, B0Token: işbirliği, B1Lemma: çerçeve, B1POS: Noun, B1Token: çerçevesinde, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

171- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [işbirliği]   B= [çerçevesinde, gümrüklere, ilişkin ,.. ]

B0Lemma: çerçeve, B0POS: Noun, B0Token: çerçevesinde, B1Lemma: gümrük, B1POS: Noun, B1Token: gümrüklere, S0B0Distance: 1, S0B0Lemma: işbirliği_çerçeve, S0B0LemmaPOS: işbirliği_Noun, S0B0POS: Noun_Noun, S0B0POSLemma: Noun_çerçeve, S0B0Token: işbirliği_çerçevesinde, S0B1Lemma: işbirliği_gümrük, S0B1LemmaPOS: işbirliği_Noun, S0B1POS: Noun_Noun, S0B1POSLemma: Noun_gümrük, S0B1Token: işbirliği_gümrüklere, S0Lemma: işbirliği, S0POS: Noun, S0Token: işbirliği, işbirliği_isGouvernedBy_çerçeve: true, işbirliği_isGouvernedBy_çerçeve_POSSESSOR: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

172- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [çerçevesinde, gümrüklere, ilişkin ,.. ]

B0Lemma: çerçeve, B0POS: Noun, B0Token: çerçevesinde, B1Lemma: gümrük, B1POS: Noun, B1Token: gümrüklere, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

173- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [çerçevesinde]   B= [gümrüklere, ilişkin, nasıl ,.. ]

B0Lemma: gümrük, B0POS: Noun, B0Token: gümrüklere, B1Lemma: ilişkin, B1POS: Postp, B1Token: ilişkin, S0B0Distance: 1, S0B0Lemma: çerçeve_gümrük, S0B0LemmaPOS: çerçeve_Noun, S0B0POS: Noun_Noun, S0B0POSLemma: Noun_gümrük, S0B0Token: çerçevesinde_gümrüklere, S0B1Lemma: çerçeve_ilişkin, S0B1LemmaPOS: çerçeve_Postp, S0B1POS: Noun_Postp, S0B1POSLemma: Noun_ilişkin, S0B1Token: çerçevesinde_ilişkin, S0Lemma: çerçeve, S0POS: Noun, S0Token: çerçevesinde, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, çerçeve_isGouvernedBy_at: true, çerçeve_isGouvernedBy_at_MODIFIER: true, 

174- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [gümrüklere, ilişkin, nasıl ,.. ]

B0Lemma: gümrük, B0POS: Noun, B0Token: gümrüklere, B1Lemma: ilişkin, B1POS: Postp, B1Token: ilişkin, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

175- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [gümrüklere]   B= [ilişkin, nasıl, adımlar ,.. ]

B0Lemma: ilişkin, B0POS: Postp, B0Token: ilişkin, B1Lemma: nasıl, B1POS: Adverb, B1Token: nasıl, S0B0Distance: 1, S0B0Lemma: gümrük_ilişkin, S0B0LemmaPOS: gümrük_Postp, S0B0POS: Noun_Postp, S0B0POSLemma: Noun_ilişkin, S0B0Token: gümrüklere_ilişkin, S0B1Lemma: gümrük_nasıl, S0B1LemmaPOS: gümrük_Adverb, S0B1POS: Noun_Adverb, S0B1POSLemma: Noun_nasıl, S0B1Token: gümrüklere_nasıl, S0Lemma: gümrük, S0POS: Noun, S0Token: gümrüklere, gümrük_isGouvernedBy_ilişkin: true, gümrük_isGouvernedBy_ilişkin_ARGUMENT: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

176- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ilişkin, nasıl, adımlar ,.. ]

B0Lemma: ilişkin, B0POS: Postp, B0Token: ilişkin, B1Lemma: nasıl, B1POS: Adverb, B1Token: nasıl, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

177- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ilişkin]   B= [nasıl, adımlar, _ ,.. ]

B0Lemma: nasıl, B0POS: Adverb, B0Token: nasıl, B1Lemma: adım, B1POS: Noun, B1Token: adımlar, S0B0Distance: 1, S0B0Lemma: ilişkin_nasıl, S0B0LemmaPOS: ilişkin_Adverb, S0B0POS: Postp_Adverb, S0B0POSLemma: Postp_nasıl, S0B0Token: ilişkin_nasıl, S0B1Lemma: ilişkin_adım, S0B1LemmaPOS: ilişkin_Noun, S0B1POS: Postp_Noun, S0B1POSLemma: Postp_adım, S0B1Token: ilişkin_adımlar, S0Lemma: ilişkin, S0POS: Postp, S0Token: ilişkin, ilişkin_isGouvernedBy_at: true, ilişkin_isGouvernedBy_at_MODIFIER: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

178- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [nasıl, adımlar, _ ,.. ]

B0Lemma: nasıl, B0POS: Adverb, B0Token: nasıl, B1Lemma: adım, B1POS: Noun, B1Token: adımlar, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

179- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [nasıl]   B= [adımlar, _, atılacağı ,.. ]

B0Lemma: adım, B0POS: Noun, B0Token: adımlar, B1Lemma: at, B1POS: Verb, B1Token: _, S0B0Distance: 1, S0B0Lemma: nasıl_adım, S0B0LemmaPOS: nasıl_Noun, S0B0POS: Adverb_Noun, S0B0POSLemma: Adverb_adım, S0B0Token: nasıl_adımlar, S0B1Lemma: nasıl_at, S0B1LemmaPOS: nasıl_Verb, S0B1POS: Adverb_Verb, S0B1POSLemma: Adverb_at, S0B1Token: nasıl__, S0Lemma: nasıl, S0POS: Adverb, S0Token: nasıl, nasıl_isGouvernedBy_at: true, nasıl_isGouvernedBy_at_MODIFIER: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

180- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [adımlar, _, atılacağı ,.. ]

B0Lemma: adım, B0POS: Noun, B0Token: adımlar, B1Lemma: at, B1POS: Verb, B1Token: _, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

181- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [adımlar]   B= [_, atılacağı, konusunda ,.. ]

B0Lemma: at, B0POS: Verb, B0Token: _, B1Lemma: _, B1POS: Adj, B1Token: atılacağı, S0B0Distance: 1, S0B0Lemma: adım_at, S0B0LemmaPOS: adım_Verb, S0B0POS: Noun_Verb, S0B0POSLemma: Noun_at, S0B0Token: adımlar__, S0B1Lemma: adım__, S0B1LemmaPOS: adım_Adj, S0B1POS: Noun_Adj, S0B1POSLemma: Noun__, S0B1Token: adımlar_atılacağı, S0Lemma: adım, S0POS: Noun, S0Token: adımlar, adım_isGouvernedBy_at: true, adım_isGouvernedBy_at_MWE: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

182- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [_, atılacağı, konusunda ,.. ]

B0Lemma: at, B0POS: Verb, B0Token: _, B1Lemma: _, B1POS: Adj, B1Token: atılacağı, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

183- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [_]   B= [atılacağı, konusunda, somut ,.. ]

B0Lemma: _, B0POS: Adj, B0Token: atılacağı, B1Lemma: konu, B1POS: Noun, B1Token: konusunda, S0B0Distance: 1, S0B0Lemma: at__, S0B0LemmaPOS: at_Adj, S0B0POS: Verb_Adj, S0B0POSLemma: Verb__, S0B0Token: __atılacağı, S0B1Lemma: at_konu, S0B1LemmaPOS: at_Noun, S0B1POS: Verb_Noun, S0B1POSLemma: Verb_konu, S0B1Token: __konusunda, S0Lemma: at, S0POS: Verb, S0Token: _, at_isGouvernedBy__: true, at_isGouvernedBy___DERIV: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

184- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [atılacağı, konusunda, somut ,.. ]

B0Lemma: _, B0POS: Adj, B0Token: atılacağı, B1Lemma: konu, B1POS: Noun, B1Token: konusunda, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

185- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [atılacağı]   B= [konusunda, somut, bir ,.. ]

B0Lemma: konu, B0POS: Noun, B0Token: konusunda, B1Lemma: somut, B1POS: Adj, B1Token: somut, S0B0Distance: 1, S0B0Lemma: __konu, S0B0LemmaPOS: __Noun, S0B0POS: Adj_Noun, S0B0POSLemma: Adj_konu, S0B0Token: atılacağı_konusunda, S0B1Lemma: __somut, S0B1LemmaPOS: __Adj, S0B1POS: Adj_Adj, S0B1POSLemma: Adj_somut, S0B1Token: atılacağı_somut, S0Lemma: _, S0POS: Adj, S0Token: atılacağı, __isGouvernedBy_konu: true, __isGouvernedBy_konu_MODIFIER: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

186- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [konusunda, somut, bir ,.. ]

B0Lemma: konu, B0POS: Noun, B0Token: konusunda, B1Lemma: somut, B1POS: Adj, B1Token: somut, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

187- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [konusunda]   B= [somut, bir, öneri ,.. ]

B0Lemma: somut, B0POS: Adj, B0Token: somut, B1Lemma: bir, B1POS: Adj, B1Token: bir, S0B0Distance: 1, S0B0Lemma: konu_somut, S0B0LemmaPOS: konu_Adj, S0B0POS: Noun_Adj, S0B0POSLemma: Noun_somut, S0B0Token: konusunda_somut, S0B1Lemma: konu_bir, S0B1LemmaPOS: konu_Adj, S0B1POS: Noun_Adj, S0B1POSLemma: Noun_bir, S0B1Token: konusunda_bir, S0Lemma: konu, S0POS: Noun, S0Token: konusunda, konu_isGouvernedBy_bul: true, konu_isGouvernedBy_bul_MODIFIER: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

188- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [somut, bir, öneri ,.. ]

B0Lemma: somut, B0POS: Adj, B0Token: somut, B1Lemma: bir, B1POS: Adj, B1Token: bir, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

189- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [somut]   B= [bir, öneri, bulunuyor ,.. ]

B0Lemma: bir, B0POS: Adj, B0Token: bir, B1Lemma: öneri, B1POS: Noun, B1Token: öneri, S0B0Distance: 1, S0B0Lemma: somut_bir, S0B0LemmaPOS: somut_Adj, S0B0POS: Adj_Adj, S0B0POSLemma: Adj_bir, S0B0Token: somut_bir, S0B1Lemma: somut_öneri, S0B1LemmaPOS: somut_Noun, S0B1POS: Adj_Noun, S0B1POSLemma: Adj_öneri, S0B1Token: somut_öneri, S0Lemma: somut, S0POS: Adj, S0Token: somut, somut_isGouvernedBy_öneri: true, somut_isGouvernedBy_öneri_MODIFIER: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

190- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [bir, öneri, bulunuyor ,.. ]

B0Lemma: bir, B0POS: Adj, B0Token: bir, B1Lemma: öneri, B1POS: Noun, B1Token: öneri, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

191- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [bir]   B= [öneri, bulunuyor, . ,.. ]

B0Lemma: öneri, B0POS: Noun, B0Token: öneri, B1Lemma: bul, B1POS: Verb, B1Token: bulunuyor, S0B0Distance: 1, S0B0Lemma: bir_öneri, S0B0LemmaPOS: bir_Noun, S0B0POS: Adj_Noun, S0B0POSLemma: Adj_öneri, S0B0Token: bir_öneri, S0B1Lemma: bir_bul, S0B1LemmaPOS: bir_Verb, S0B1POS: Adj_Verb, S0B1POSLemma: Adj_bul, S0B1Token: bir_bulunuyor, S0Lemma: bir, S0POS: Adj, S0Token: bir, bir_isGouvernedBy_öneri: true, bir_isGouvernedBy_öneri_DETERMINER: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

192- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [öneri, bulunuyor, . ,.. ]

B0Lemma: öneri, B0POS: Noun, B0Token: öneri, B1Lemma: bul, B1POS: Verb, B1Token: bulunuyor, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

193- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [öneri]   B= [bulunuyor, ., AVRUPA ,.. ]

B0Lemma: bul, B0POS: Verb, B0Token: bulunuyor, B1Lemma: ., B1POS: Punc, B1Token: ., S0B0Distance: 1, S0B0Lemma: öneri_bul, S0B0LemmaPOS: öneri_Verb, S0B0POS: Noun_Verb, S0B0POSLemma: Noun_bul, S0B0Token: öneri_bulunuyor, S0B1Lemma: öneri_., S0B1LemmaPOS: öneri_Punc, S0B1POS: Noun_Punc, S0B1POSLemma: Noun_., S0B1Token: öneri_., S0Lemma: öneri, S0POS: Noun, S0Token: öneri, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, öneri_isGouvernedBy_bul: true, öneri_isGouvernedBy_bul_OBJECT: true, 

194- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [bulunuyor, ., AVRUPA ,.. ]

B0Lemma: bul, B0POS: Verb, B0Token: bulunuyor, B1Lemma: ., B1POS: Punc, B1Token: ., transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

195- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [bulunuyor]   B= [., AVRUPA, ÖRNEĞİ ,.. ]

B0Lemma: ., B0POS: Punc, B0Token: ., B1Lemma: Avrupa, B1POS: Noun, B1Token: AVRUPA, S0B0Distance: 1, S0B0Lemma: bul_., S0B0LemmaPOS: bul_Punc, S0B0POS: Verb_Punc, S0B0POSLemma: Verb_., S0B0Token: bulunuyor_., S0B1Lemma: bul_Avrupa, S0B1LemmaPOS: bul_Noun, S0B1POS: Verb_Noun, S0B1POSLemma: Verb_Avrupa, S0B1Token: bulunuyor_AVRUPA, S0Lemma: bul, S0POS: Verb, S0Token: bulunuyor, bul_._hasRighDep_PUNCTUATION: true, bul_hasRighDep_PUNCTUATION: true, bul_isGouvernedBy_açıkla: true, bul_isGouvernedBy_açıkla_COORDINATION: true, hasRighDep_PUNCTUATION: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

196- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [., AVRUPA, ÖRNEĞİ ,.. ]

B0Lemma: ., B0POS: Punc, B0Token: ., B1Lemma: Avrupa, B1POS: Noun, B1Token: AVRUPA, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

197- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [AVRUPA, ÖRNEĞİ, . ,.. ]

B0Lemma: Avrupa, B0POS: Noun, B0Token: AVRUPA, B1Lemma: ÖRNEĞİ, B1POS: Noun, B1Token: ÖRNEĞİ, S0B0Distance: 1, S0B0Lemma: ._Avrupa, S0B0LemmaPOS: ._Noun, S0B0POS: Punc_Noun, S0B0POSLemma: Punc_Avrupa, S0B0Token: ._AVRUPA, S0B1Lemma: ._ÖRNEĞİ, S0B1LemmaPOS: ._Noun, S0B1POS: Punc_Noun, S0B1POSLemma: Punc_ÖRNEĞİ, S0B1Token: ._ÖRNEĞİ, S0Lemma: ., S0POS: Punc, S0Token: ., transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

198- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [AVRUPA, ÖRNEĞİ, . ,.. ]

B0Lemma: Avrupa, B0POS: Noun, B0Token: AVRUPA, B1Lemma: ÖRNEĞİ, B1POS: Noun, B1Token: ÖRNEĞİ, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

199- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [AVRUPA]   B= [ÖRNEĞİ, ., D ,.. ]

Avrupa_isGouvernedBy_ÖRNEĞİ: true, Avrupa_isGouvernedBy_ÖRNEĞİ_MWE: true, B0Lemma: ÖRNEĞİ, B0POS: Noun, B0Token: ÖRNEĞİ, B1Lemma: ., B1POS: Punc, B1Token: ., S0B0Distance: 1, S0B0Lemma: Avrupa_ÖRNEĞİ, S0B0LemmaPOS: Avrupa_Noun, S0B0POS: Noun_Noun, S0B0POSLemma: Noun_ÖRNEĞİ, S0B0Token: AVRUPA_ÖRNEĞİ, S0B1Lemma: Avrupa_., S0B1LemmaPOS: Avrupa_Punc, S0B1POS: Noun_Punc, S0B1POSLemma: Noun_., S0B1Token: AVRUPA_., S0Lemma: Avrupa, S0POS: Noun, S0Token: AVRUPA, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

200- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ÖRNEĞİ, ., D ,.. ]

B0Lemma: ÖRNEĞİ, B0POS: Noun, B0Token: ÖRNEĞİ, B1Lemma: ., B1POS: Punc, B1Token: ., transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

201- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ÖRNEĞİ]   B= [., D, - ,.. ]

B0Lemma: ., B0POS: Punc, B0Token: ., B1Lemma: d, B1POS: Noun, B1Token: D, S0B0Distance: 1, S0B0Lemma: ÖRNEĞİ_., S0B0LemmaPOS: ÖRNEĞİ_Punc, S0B0POS: Noun_Punc, S0B0POSLemma: Noun_., S0B0Token: ÖRNEĞİ_., S0B1Lemma: ÖRNEĞİ_d, S0B1LemmaPOS: ÖRNEĞİ_Noun, S0B1POS: Noun_Noun, S0B1POSLemma: Noun_d, S0B1Token: ÖRNEĞİ_D, S0Lemma: ÖRNEĞİ, S0POS: Noun, S0Token: ÖRNEĞİ, hasRighDep_PUNCTUATION: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, ÖRNEĞİ_._hasRighDep_PUNCTUATION: true, ÖRNEĞİ_hasRighDep_PUNCTUATION: true, ÖRNEĞİ_isGouvernedBy_açıkla: true, ÖRNEĞİ_isGouvernedBy_açıkla_COORDINATION: true, 

202- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [., D, - ,.. ]

B0Lemma: ., B0POS: Punc, B0Token: ., B1Lemma: d, B1POS: Noun, B1Token: D, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

203- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [D, -, 8 ,.. ]

B0Lemma: d, B0POS: Noun, B0Token: D, B1Lemma: -, B1POS: Punc, B1Token: -, S0B0Distance: 1, S0B0Lemma: ._d, S0B0LemmaPOS: ._Noun, S0B0POS: Punc_Noun, S0B0POSLemma: Punc_d, S0B0Token: ._D, S0B1Lemma: ._-, S0B1LemmaPOS: ._Punc, S0B1POS: Punc_Punc, S0B1POSLemma: Punc_-, S0B1Token: ._-, S0Lemma: ., S0POS: Punc, S0Token: ., transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

204- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [D, -, 8 ,.. ]

B0Lemma: d, B0POS: Noun, B0Token: D, B1Lemma: -, B1POS: Punc, B1Token: -, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

205- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [D]   B= [-, 8, Zirvesi'nin ,.. ]

B0Lemma: -, B0POS: Punc, B0Token: -, B1Lemma: 8, B1POS: Adj, B1Token: 8, S0B0Distance: 1, S0B0Lemma: d_-, S0B0LemmaPOS: d_Punc, S0B0POS: Noun_Punc, S0B0POSLemma: Noun_-, S0B0Token: D_-, S0B1Lemma: d_8, S0B1LemmaPOS: d_Adj, S0B1POS: Noun_Adj, S0B1POSLemma: Noun_8, S0B1Token: D_8, S0Lemma: d, S0POS: Noun, S0Token: D, d_-_hasRighDep_PUNCTUATION: true, d_hasRighDep_PUNCTUATION: true, d_isGouvernedBy_açıkla: true, d_isGouvernedBy_açıkla_SUBJECT: true, hasRighDep_PUNCTUATION: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

206- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [-, 8, Zirvesi'nin ,.. ]

B0Lemma: -, B0POS: Punc, B0Token: -, B1Lemma: 8, B1POS: Adj, B1Token: 8, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

207- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [-]   B= [8, Zirvesi'nin, barışçıl ,.. ]

B0Lemma: 8, B0POS: Adj, B0Token: 8, B1Lemma: zirve, B1POS: Noun, B1Token: Zirvesi'nin, S0B0Distance: 1, S0B0Lemma: -_8, S0B0LemmaPOS: -_Adj, S0B0POS: Punc_Adj, S0B0POSLemma: Punc_8, S0B0Token: -_8, S0B1Lemma: -_zirve, S0B1LemmaPOS: -_Noun, S0B1POS: Punc_Noun, S0B1POSLemma: Punc_zirve, S0B1Token: -_Zirvesi'nin, S0Lemma: -, S0POS: Punc, S0Token: -, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

208- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [8, Zirvesi'nin, barışçıl ,.. ]

B0Lemma: 8, B0POS: Adj, B0Token: 8, B1Lemma: zirve, B1POS: Noun, B1Token: Zirvesi'nin, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

209- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [8]   B= [Zirvesi'nin, barışçıl, amaçlar ,.. ]

8_isGouvernedBy_zirve: true, 8_isGouvernedBy_zirve_MODIFIER: true, B0Lemma: zirve, B0POS: Noun, B0Token: Zirvesi'nin, B1Lemma: barışçıl, B1POS: Adj, B1Token: barışçıl, S0B0Distance: 1, S0B0Lemma: 8_zirve, S0B0LemmaPOS: 8_Noun, S0B0POS: Adj_Noun, S0B0POSLemma: Adj_zirve, S0B0Token: 8_Zirvesi'nin, S0B1Lemma: 8_barışçıl, S0B1LemmaPOS: 8_Adj, S0B1POS: Adj_Adj, S0B1POSLemma: Adj_barışçıl, S0B1Token: 8_barışçıl, S0Lemma: 8, S0POS: Adj, S0Token: 8, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

210- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Zirvesi'nin, barışçıl, amaçlar ,.. ]

B0Lemma: zirve, B0POS: Noun, B0Token: Zirvesi'nin, B1Lemma: barışçıl, B1POS: Adj, B1Token: barışçıl, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

211- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Zirvesi'nin]   B= [barışçıl, amaçlar, _ ,.. ]

B0Lemma: barışçıl, B0POS: Adj, B0Token: barışçıl, B1Lemma: amaç, B1POS: Noun, B1Token: amaçlar, S0B0Distance: 1, S0B0Lemma: zirve_barışçıl, S0B0LemmaPOS: zirve_Adj, S0B0POS: Noun_Adj, S0B0POSLemma: Noun_barışçıl, S0B0Token: Zirvesi'nin_barışçıl, S0B1Lemma: zirve_amaç, S0B1LemmaPOS: zirve_Noun, S0B1POS: Noun_Noun, S0B1POSLemma: Noun_amaç, S0B1Token: Zirvesi'nin_amaçlar, S0Lemma: zirve, S0POS: Noun, S0Token: Zirvesi'nin, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, zirve_isGouvernedBy__: true, zirve_isGouvernedBy___POSSESSOR: true, 

212- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [barışçıl, amaçlar, _ ,.. ]

B0Lemma: barışçıl, B0POS: Adj, B0Token: barışçıl, B1Lemma: amaç, B1POS: Noun, B1Token: amaçlar, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

213- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [barışçıl]   B= [amaçlar, _, taşıdığını ,.. ]

B0Lemma: amaç, B0POS: Noun, B0Token: amaçlar, B1Lemma: taşı, B1POS: Verb, B1Token: _, S0B0Distance: 1, S0B0Lemma: barışçıl_amaç, S0B0LemmaPOS: barışçıl_Noun, S0B0POS: Adj_Noun, S0B0POSLemma: Adj_amaç, S0B0Token: barışçıl_amaçlar, S0B1Lemma: barışçıl_taşı, S0B1LemmaPOS: barışçıl_Verb, S0B1POS: Adj_Verb, S0B1POSLemma: Adj_taşı, S0B1Token: barışçıl__, S0Lemma: barışçıl, S0POS: Adj, S0Token: barışçıl, barışçıl_isGouvernedBy_amaç: true, barışçıl_isGouvernedBy_amaç_MODIFIER: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

214- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [amaçlar, _, taşıdığını ,.. ]

B0Lemma: amaç, B0POS: Noun, B0Token: amaçlar, B1Lemma: taşı, B1POS: Verb, B1Token: _, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

215- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [amaçlar]   B= [_, taşıdığını, _ ,.. ]

B0Lemma: taşı, B0POS: Verb, B0Token: _, B1Lemma: _, B1POS: Noun, B1Token: taşıdığını, S0B0Distance: 1, S0B0Lemma: amaç_taşı, S0B0LemmaPOS: amaç_Verb, S0B0POS: Noun_Verb, S0B0POSLemma: Noun_taşı, S0B0Token: amaçlar__, S0B1Lemma: amaç__, S0B1LemmaPOS: amaç_Noun, S0B1POS: Noun_Noun, S0B1POSLemma: Noun__, S0B1Token: amaçlar_taşıdığını, S0Lemma: amaç, S0POS: Noun, S0Token: amaçlar, amaç_isGouvernedBy_taşı: true, amaç_isGouvernedBy_taşı_OBJECT: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

216- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [_, taşıdığını, _ ,.. ]

B0Lemma: taşı, B0POS: Verb, B0Token: _, B1Lemma: _, B1POS: Noun, B1Token: taşıdığını, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

217- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [_]   B= [taşıdığını, _, vurgulayan ,.. ]

B0Lemma: _, B0POS: Noun, B0Token: taşıdığını, B1Lemma: vurgula, B1POS: Verb, B1Token: _, S0B0Distance: 1, S0B0Lemma: taşı__, S0B0LemmaPOS: taşı_Noun, S0B0POS: Verb_Noun, S0B0POSLemma: Verb__, S0B0Token: __taşıdığını, S0B1Lemma: taşı_vurgula, S0B1LemmaPOS: taşı_Verb, S0B1POS: Verb_Verb, S0B1POSLemma: Verb_vurgula, S0B1Token: ___, S0Lemma: taşı, S0POS: Verb, S0Token: _, taşı_isGouvernedBy__: true, taşı_isGouvernedBy___DERIV: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

218- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [taşıdığını, _, vurgulayan ,.. ]

B0Lemma: _, B0POS: Noun, B0Token: taşıdığını, B1Lemma: vurgula, B1POS: Verb, B1Token: _, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

219- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [taşıdığını]   B= [_, vurgulayan, Çiller ,.. ]

B0Lemma: vurgula, B0POS: Verb, B0Token: _, B1Lemma: _, B1POS: Adj, B1Token: vurgulayan, S0B0Distance: 1, S0B0Lemma: __vurgula, S0B0LemmaPOS: __Verb, S0B0POS: Noun_Verb, S0B0POSLemma: Noun_vurgula, S0B0Token: taşıdığını__, S0B1Lemma: ___, S0B1LemmaPOS: __Adj, S0B1POS: Noun_Adj, S0B1POSLemma: Noun__, S0B1Token: taşıdığını_vurgulayan, S0Lemma: _, S0POS: Noun, S0Token: taşıdığını, __isGouvernedBy_vurgula: true, __isGouvernedBy_vurgula_OBJECT: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

220- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [_, vurgulayan, Çiller ,.. ]

B0Lemma: vurgula, B0POS: Verb, B0Token: _, B1Lemma: _, B1POS: Adj, B1Token: vurgulayan, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

221- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [_]   B= [vurgulayan, Çiller, de ,.. ]

B0Lemma: _, B0POS: Adj, B0Token: vurgulayan, B1Lemma: çil, B1POS: Noun, B1Token: Çiller, S0B0Distance: 1, S0B0Lemma: vurgula__, S0B0LemmaPOS: vurgula_Adj, S0B0POS: Verb_Adj, S0B0POSLemma: Verb__, S0B0Token: __vurgulayan, S0B1Lemma: vurgula_çil, S0B1LemmaPOS: vurgula_Noun, S0B1POS: Verb_Noun, S0B1POSLemma: Verb_çil, S0B1Token: __Çiller, S0Lemma: vurgula, S0POS: Verb, S0Token: _, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, vurgula_isGouvernedBy__: true, vurgula_isGouvernedBy___DERIV: true, 

222- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [vurgulayan, Çiller, de ,.. ]

B0Lemma: _, B0POS: Adj, B0Token: vurgulayan, B1Lemma: çil, B1POS: Noun, B1Token: Çiller, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

223- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [vurgulayan]   B= [Çiller, de, " ,.. ]

B0Lemma: çil, B0POS: Noun, B0Token: Çiller, B1Lemma: de, B1POS: Conj, B1Token: de, S0B0Distance: 1, S0B0Lemma: __çil, S0B0LemmaPOS: __Noun, S0B0POS: Adj_Noun, S0B0POSLemma: Adj_çil, S0B0Token: vurgulayan_Çiller, S0B1Lemma: __de, S0B1LemmaPOS: __Conj, S0B1POS: Adj_Conj, S0B1POSLemma: Adj_de, S0B1Token: vurgulayan_de, S0Lemma: _, S0POS: Adj, S0Token: vurgulayan, __isGouvernedBy_çil: true, __isGouvernedBy_çil_MODIFIER: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

224- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Çiller, de, " ,.. ]

B0Lemma: çil, B0POS: Noun, B0Token: Çiller, B1Lemma: de, B1POS: Conj, B1Token: de, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

225- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Çiller]   B= [de, ", Müslüman ,.. ]

B0Lemma: de, B0POS: Conj, B0Token: de, B1Lemma: ", B1POS: Punc, B1Token: ", S0B0Distance: 1, S0B0Lemma: çil_de, S0B0LemmaPOS: çil_Conj, S0B0POS: Noun_Conj, S0B0POSLemma: Noun_de, S0B0Token: Çiller_de, S0B1Lemma: çil_", S0B1LemmaPOS: çil_Punc, S0B1POS: Noun_Punc, S0B1POSLemma: Noun_", S0B1Token: Çiller_", S0Lemma: çil, S0POS: Noun, S0Token: Çiller, hasRighDep_INTENSIFIER: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, çil_de_hasRighDep_INTENSIFIER: true, çil_hasRighDep_INTENSIFIER: true, çil_isGouvernedBy_müslüman: true, çil_isGouvernedBy_müslüman_SUBJECT: true, 

226- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [de, ", Müslüman ,.. ]

B0Lemma: de, B0POS: Conj, B0Token: de, B1Lemma: ", B1POS: Punc, B1Token: ", transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

227- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [de]   B= [", Müslüman, - ,.. ]

B0Lemma: ", B0POS: Punc, B0Token: ", B1Lemma: müslüman, B1POS: Adj, B1Token: Müslüman, S0B0Distance: 1, S0B0Lemma: de_", S0B0LemmaPOS: de_Punc, S0B0POS: Conj_Punc, S0B0POSLemma: Conj_", S0B0Token: de_", S0B1Lemma: de_müslüman, S0B1LemmaPOS: de_Adj, S0B1POS: Conj_Adj, S0B1POSLemma: Conj_müslüman, S0B1Token: de_Müslüman, S0Lemma: de, S0POS: Conj, S0Token: de, de_"_hasRighDep_PUNCTUATION: true, de_hasRighDep_PUNCTUATION: true, hasRighDep_PUNCTUATION: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

228- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [", Müslüman, - ,.. ]

B0Lemma: ", B0POS: Punc, B0Token: ", B1Lemma: müslüman, B1POS: Adj, B1Token: Müslüman, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

229- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= ["]   B= [Müslüman, -, 8'ler ,.. ]

B0Lemma: müslüman, B0POS: Adj, B0Token: Müslüman, B1Lemma: -, B1POS: Punc, B1Token: -, S0B0Distance: 1, S0B0Lemma: "_müslüman, S0B0LemmaPOS: "_Adj, S0B0POS: Punc_Adj, S0B0POSLemma: Punc_müslüman, S0B0Token: "_Müslüman, S0B1Lemma: "_-, S0B1LemmaPOS: "_Punc, S0B1POS: Punc_Punc, S0B1POSLemma: Punc_-, S0B1Token: "_-, S0Lemma: ", S0POS: Punc, S0Token: ", transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

230- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Müslüman, -, 8'ler ,.. ]

B0Lemma: müslüman, B0POS: Adj, B0Token: Müslüman, B1Lemma: -, B1POS: Punc, B1Token: -, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

231- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Müslüman]   B= [-, 8'ler, " ,.. ]

B0Lemma: -, B0POS: Punc, B0Token: -, B1Lemma: 8, B1POS: Noun, B1Token: 8'ler, S0B0Distance: 1, S0B0Lemma: müslüman_-, S0B0LemmaPOS: müslüman_Punc, S0B0POS: Adj_Punc, S0B0POSLemma: Adj_-, S0B0Token: Müslüman_-, S0B1Lemma: müslüman_8, S0B1LemmaPOS: müslüman_Noun, S0B1POS: Adj_Noun, S0B1POSLemma: Adj_8, S0B1Token: Müslüman_8'ler, S0Lemma: müslüman, S0POS: Adj, S0Token: Müslüman, hasRighDep_PUNCTUATION: true, müslüman_-_hasRighDep_PUNCTUATION: true, müslüman_hasRighDep_PUNCTUATION: true, müslüman_isGouvernedBy_açıkla: true, müslüman_isGouvernedBy_açıkla_MODIFIER: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

232- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [-, 8'ler, " ,.. ]

B0Lemma: -, B0POS: Punc, B0Token: -, B1Lemma: 8, B1POS: Noun, B1Token: 8'ler, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

233- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [-]   B= [8'ler, ", isminin ,.. ]

B0Lemma: 8, B0POS: Noun, B0Token: 8'ler, B1Lemma: ", B1POS: Punc, B1Token: ", S0B0Distance: 1, S0B0Lemma: -_8, S0B0LemmaPOS: -_Noun, S0B0POS: Punc_Noun, S0B0POSLemma: Punc_8, S0B0Token: -_8'ler, S0B1Lemma: -_", S0B1LemmaPOS: -_Punc, S0B1POS: Punc_Punc, S0B1POSLemma: Punc_", S0B1Token: -_", S0Lemma: -, S0POS: Punc, S0Token: -, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

234- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [8'ler, ", isminin ,.. ]

B0Lemma: 8, B0POS: Noun, B0Token: 8'ler, B1Lemma: ", B1POS: Punc, B1Token: ", transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

235- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [8'ler]   B= [", isminin, yanlış ,.. ]

8_"_hasRighDep_PUNCTUATION: true, 8_hasRighDep_PUNCTUATION: true, 8_isGouvernedBy_isim: true, 8_isGouvernedBy_isim_POSSESSOR: true, B0Lemma: ", B0POS: Punc, B0Token: ", B1Lemma: isim, B1POS: Noun, B1Token: isminin, S0B0Distance: 1, S0B0Lemma: 8_", S0B0LemmaPOS: 8_Punc, S0B0POS: Noun_Punc, S0B0POSLemma: Noun_", S0B0Token: 8'ler_", S0B1Lemma: 8_isim, S0B1LemmaPOS: 8_Noun, S0B1POS: Noun_Noun, S0B1POSLemma: Noun_isim, S0B1Token: 8'ler_isminin, S0Lemma: 8, S0POS: Noun, S0Token: 8'ler, hasRighDep_PUNCTUATION: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

236- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [", isminin, yanlış ,.. ]

B0Lemma: ", B0POS: Punc, B0Token: ", B1Lemma: isim, B1POS: Noun, B1Token: isminin, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

237- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= ["]   B= [isminin, yanlış, bir ,.. ]

B0Lemma: isim, B0POS: Noun, B0Token: isminin, B1Lemma: yanlış, B1POS: Adj, B1Token: yanlış, S0B0Distance: 1, S0B0Lemma: "_isim, S0B0LemmaPOS: "_Noun, S0B0POS: Punc_Noun, S0B0POSLemma: Punc_isim, S0B0Token: "_isminin, S0B1Lemma: "_yanlış, S0B1LemmaPOS: "_Adj, S0B1POS: Punc_Adj, S0B1POSLemma: Punc_yanlış, S0B1Token: "_yanlış, S0Lemma: ", S0POS: Punc, S0Token: ", transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

238- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [isminin, yanlış, bir ,.. ]

B0Lemma: isim, B0POS: Noun, B0Token: isminin, B1Lemma: yanlış, B1POS: Adj, B1Token: yanlış, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

239- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [isminin]   B= [yanlış, bir, _ ,.. ]

B0Lemma: yanlış, B0POS: Adj, B0Token: yanlış, B1Lemma: bir, B1POS: Adj, B1Token: bir, S0B0Distance: 1, S0B0Lemma: isim_yanlış, S0B0LemmaPOS: isim_Adj, S0B0POS: Noun_Adj, S0B0POSLemma: Noun_yanlış, S0B0Token: isminin_yanlış, S0B1Lemma: isim_bir, S0B1LemmaPOS: isim_Adj, S0B1POS: Noun_Adj, S0B1POSLemma: Noun_bir, S0B1Token: isminin_bir, S0Lemma: isim, S0POS: Noun, S0Token: isminin, isim_isGouvernedBy__: true, isim_isGouvernedBy___POSSESSOR: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

240- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [yanlış, bir, _ ,.. ]

B0Lemma: yanlış, B0POS: Adj, B0Token: yanlış, B1Lemma: bir, B1POS: Adj, B1Token: bir, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

241- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [yanlış]   B= [bir, _, algılamaya ,.. ]

B0Lemma: bir, B0POS: Adj, B0Token: bir, B1Lemma: algıla, B1POS: Verb, B1Token: _, S0B0Distance: 1, S0B0Lemma: yanlış_bir, S0B0LemmaPOS: yanlış_Adj, S0B0POS: Adj_Adj, S0B0POSLemma: Adj_bir, S0B0Token: yanlış_bir, S0B1Lemma: yanlış_algıla, S0B1LemmaPOS: yanlış_Verb, S0B1POS: Adj_Verb, S0B1POSLemma: Adj_algıla, S0B1Token: yanlış__, S0Lemma: yanlış, S0POS: Adj, S0Token: yanlış, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, yanlış_isGouvernedBy__: true, yanlış_isGouvernedBy___MODIFIER: true, 

242- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [bir, _, algılamaya ,.. ]

B0Lemma: bir, B0POS: Adj, B0Token: bir, B1Lemma: algıla, B1POS: Verb, B1Token: _, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

243- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [bir]   B= [_, algılamaya, yol ,.. ]

B0Lemma: algıla, B0POS: Verb, B0Token: _, B1Lemma: _, B1POS: Noun, B1Token: algılamaya, S0B0Distance: 1, S0B0Lemma: bir_algıla, S0B0LemmaPOS: bir_Verb, S0B0POS: Adj_Verb, S0B0POSLemma: Adj_algıla, S0B0Token: bir__, S0B1Lemma: bir__, S0B1LemmaPOS: bir_Noun, S0B1POS: Adj_Noun, S0B1POSLemma: Adj__, S0B1Token: bir_algılamaya, S0Lemma: bir, S0POS: Adj, S0Token: bir, bir_isGouvernedBy__: true, bir_isGouvernedBy___DETERMINER: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

244- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [_, algılamaya, yol ,.. ]

B0Lemma: algıla, B0POS: Verb, B0Token: _, B1Lemma: _, B1POS: Noun, B1Token: algılamaya, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

245- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [_]   B= [algılamaya, yol, _ ,.. ]

B0Lemma: _, B0POS: Noun, B0Token: algılamaya, B1Lemma: yol, B1POS: Noun, B1Token: yol, S0B0Distance: 1, S0B0Lemma: algıla__, S0B0LemmaPOS: algıla_Noun, S0B0POS: Verb_Noun, S0B0POSLemma: Verb__, S0B0Token: __algılamaya, S0B1Lemma: algıla_yol, S0B1LemmaPOS: algıla_Noun, S0B1POS: Verb_Noun, S0B1POSLemma: Verb_yol, S0B1Token: __yol, S0Lemma: algıla, S0POS: Verb, S0Token: _, algıla_isGouvernedBy__: true, algıla_isGouvernedBy___DERIV: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

246- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [algılamaya, yol, _ ,.. ]

B0Lemma: _, B0POS: Noun, B0Token: algılamaya, B1Lemma: yol, B1POS: Noun, B1Token: yol, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

247- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [algılamaya]   B= [yol, _, açtığını ,.. ]

B0Lemma: yol, B0POS: Noun, B0Token: yol, B1Lemma: aç, B1POS: Verb, B1Token: _, S0B0Distance: 1, S0B0Lemma: __yol, S0B0LemmaPOS: __Noun, S0B0POS: Noun_Noun, S0B0POSLemma: Noun_yol, S0B0Token: algılamaya_yol, S0B1Lemma: __aç, S0B1LemmaPOS: __Verb, S0B1POS: Noun_Verb, S0B1POSLemma: Noun_aç, S0B1Token: algılamaya__, S0Lemma: _, S0POS: Noun, S0Token: algılamaya, __isGouvernedBy__: true, __isGouvernedBy___MODIFIER: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

248- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [yol, _, açtığını ,.. ]

B0Lemma: yol, B0POS: Noun, B0Token: yol, B1Lemma: aç, B1POS: Verb, B1Token: _, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

249- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [yol]   B= [_, açtığını, şu ,.. ]

B0Lemma: aç, B0POS: Verb, B0Token: _, B1Lemma: _, B1POS: Noun, B1Token: açtığını, S0B0Distance: 1, S0B0Lemma: yol_aç, S0B0LemmaPOS: yol_Verb, S0B0POS: Noun_Verb, S0B0POSLemma: Noun_aç, S0B0Token: yol__, S0B1Lemma: yol__, S0B1LemmaPOS: yol_Noun, S0B1POS: Noun_Noun, S0B1POSLemma: Noun__, S0B1Token: yol_açtığını, S0Lemma: yol, S0POS: Noun, S0Token: yol, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, yol_isGouvernedBy__: true, yol_isGouvernedBy___MWE: true, 

250- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [yol, _]   B= [açtığını, şu, sözlerle ,.. ]

B0Lemma: _, B0POS: Noun, B0Token: açtığını, B1Lemma: şu, B1POS: Det, B1Token: şu, S0B0Distance: 1, S0B0Lemma: aç__, S0B0LemmaPOS: aç_Noun, S0B0POS: Verb_Noun, S0B0POSLemma: Verb__, S0B0Token: __açtığını, S0B1Lemma: aç_şu, S0B1LemmaPOS: aç_Det, S0B1POS: Verb_Det, S0B1POSLemma: Verb_şu, S0B1Token: __şu, S0Lemma: aç, S0POS: Verb, S0Token: _, S1B0Lemma: yol__, S1B0LemmaPOS: yol_Noun, S1B0POS: Noun_Noun, S1B0POSLemma: Noun__, S1B0Token: yol_açtığını, S1Lemma: yol, S1POS: Noun, S1S0Lemma: yol_aç, S1S0LemmaPOS: yol_Verb, S1S0POS: Noun_Verb, S1S0POSLemma: Noun_aç, S1S0Token: yol__, S1Token: yol, aç_isGouvernedBy__: true, aç_isGouvernedBy___DERIV: true, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

251- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [yol]   B= [açtığını, şu, sözlerle ,.. ]

B0Lemma: _, B0POS: Noun, B0Token: açtığını, B1Lemma: şu, B1POS: Det, B1Token: şu, S0B0Distance: 2, S0B0Lemma: yol__, S0B0LemmaPOS: yol_Noun, S0B0POS: Noun_Noun, S0B0POSLemma: Noun__, S0B0Token: yol_açtığını, S0B1Lemma: yol_şu, S0B1LemmaPOS: yol_Det, S0B1POS: Noun_Det, S0B1POSLemma: Noun_şu, S0B1Token: yol_şu, S0Lemma: yol, S0POS: Noun, S0Token: yol, transitionHistoryLength1: 0, transitionHistoryLength2: 00, transitionHistoryLength3: 002, yol_isGouvernedBy__: true, yol_isGouvernedBy___MWE: true, 

252- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [yol, açtığını]   B= [şu, sözlerle, açıkladı ,.. ]

B0Lemma: şu, B0POS: Det, B0Token: şu, B1Lemma: söz, B1POS: Noun, B1Token: sözlerle, S0B0Distance: 1, S0B0Lemma: __şu, S0B0LemmaPOS: __Det, S0B0POS: Noun_Det, S0B0POSLemma: Noun_şu, S0B0Token: açtığını_şu, S0B1Lemma: __söz, S0B1LemmaPOS: __Noun, S0B1POS: Noun_Noun, S0B1POSLemma: Noun_söz, S0B1Token: açtığını_sözlerle, S0Lemma: _, S0POS: Noun, S0Token: açtığını, S1B0Lemma: yol_şu, S1B0LemmaPOS: yol_Det, S1B0POS: Noun_Det, S1B0POSLemma: Noun_şu, S1B0Token: yol_şu, S1Lemma: yol, S1POS: Noun, S1S0Lemma: yol__, S1S0LemmaPOS: yol_Noun, S1S0POS: Noun_Noun, S1S0POSLemma: Noun__, S1S0Token: yol_açtığını, S1Token: yol, SyntaxicRelation: -MWE, __isGouvernedBy_açıkla: true, __isGouvernedBy_açıkla_OBJECT: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 200, 

253- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[yol, açtığını]]   B= [şu, sözlerle, açıkladı ,.. ]

B0Lemma: şu, B0POS: Det, B0Token: şu, B1Lemma: söz, B1POS: Noun, B1Token: sözlerle, S0B0Distance: 1, S0B0Lemma: yol___şu, S0B0LemmaPOS: yol___Det, S0B0POS: Noun_Noun_Det, S0B0POSLemma: Noun_Noun_şu, S0B0Token: yol_açtığını_şu, S0B1Lemma: yol___söz, S0B1LemmaPOS: yol___Noun, S0B1POS: Noun_Noun_Noun, S0B1POSLemma: Noun_Noun_söz, S0B1Token: yol_açtığını_sözlerle, S0Lemma: yol__, S0POS: Noun_Noun, S0Token: yol_açtığını, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

254- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [şu, sözlerle, açıkladı ,.. ]

B0Lemma: şu, B0POS: Det, B0Token: şu, B1Lemma: söz, B1POS: Noun, B1Token: sözlerle, transitionHistoryLength1: 1, transitionHistoryLength2: 10, transitionHistoryLength3: 102, 

255- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [şu]   B= [sözlerle, açıkladı, : ,.. ]

B0Lemma: söz, B0POS: Noun, B0Token: sözlerle, B1Lemma: açıkla, B1POS: Verb, B1Token: açıkladı, S0B0Distance: 1, S0B0Lemma: şu_söz, S0B0LemmaPOS: şu_Noun, S0B0POS: Det_Noun, S0B0POSLemma: Det_söz, S0B0Token: şu_sözlerle, S0B1Lemma: şu_açıkla, S0B1LemmaPOS: şu_Verb, S0B1POS: Det_Verb, S0B1POSLemma: Det_açıkla, S0B1Token: şu_açıkladı, S0Lemma: şu, S0POS: Det, S0Token: şu, transitionHistoryLength1: 2, transitionHistoryLength2: 21, transitionHistoryLength3: 210, şu_isGouvernedBy_söz: true, şu_isGouvernedBy_söz_DETERMINER: true, 

256- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [sözlerle, açıkladı, : ,.. ]

B0Lemma: söz, B0POS: Noun, B0Token: sözlerle, B1Lemma: açıkla, B1POS: Verb, B1Token: açıkladı, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 021, 

257- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [sözlerle]   B= [açıkladı, :, " ,.. ]

B0Lemma: açıkla, B0POS: Verb, B0Token: açıkladı, B1Lemma: :, B1POS: Punc, B1Token: :, S0B0Distance: 1, S0B0Lemma: söz_açıkla, S0B0LemmaPOS: söz_Verb, S0B0POS: Noun_Verb, S0B0POSLemma: Noun_açıkla, S0B0Token: sözlerle_açıkladı, S0B1Lemma: söz_:, S0B1LemmaPOS: söz_Punc, S0B1POS: Noun_Punc, S0B1POSLemma: Noun_:, S0B1Token: sözlerle_:, S0Lemma: söz, S0POS: Noun, S0Token: sözlerle, söz_isGouvernedBy_açıkla: true, söz_isGouvernedBy_açıkla_MODIFIER: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

258- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [açıkladı, :, " ,.. ]

B0Lemma: açıkla, B0POS: Verb, B0Token: açıkladı, B1Lemma: :, B1POS: Punc, B1Token: :, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

259- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [açıkladı]   B= [:, ", D ,.. ]

B0Lemma: :, B0POS: Punc, B0Token: :, B1Lemma: ", B1POS: Punc, B1Token: ", S0B0Distance: 1, S0B0Lemma: açıkla_:, S0B0LemmaPOS: açıkla_Punc, S0B0POS: Verb_Punc, S0B0POSLemma: Verb_:, S0B0Token: açıkladı_:, S0B1Lemma: açıkla_", S0B1LemmaPOS: açıkla_Punc, S0B1POS: Verb_Punc, S0B1POSLemma: Verb_", S0B1Token: açıkladı_", S0Lemma: açıkla, S0POS: Verb, S0Token: açıkladı, açıkla_"_hasRighDep_PUNCTUATION: true, açıkla_:_hasRighDep_PUNCTUATION: true, açıkla_hasRighDep_PUNCTUATION: true, açıkla_isGouvernedBy_değil: true, açıkla_isGouvernedBy_değil_COORDINATION: true, hasRighDep_PUNCTUATION: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

260- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [:, ", D ,.. ]

B0Lemma: :, B0POS: Punc, B0Token: :, B1Lemma: ", B1POS: Punc, B1Token: ", transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

261- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [:]   B= [", D, - ,.. ]

B0Lemma: ", B0POS: Punc, B0Token: ", B1Lemma: d, B1POS: Noun, B1Token: D, S0B0Distance: 1, S0B0Lemma: :_", S0B0LemmaPOS: :_Punc, S0B0POS: Punc_Punc, S0B0POSLemma: Punc_", S0B0Token: :_", S0B1Lemma: :_d, S0B1LemmaPOS: :_Noun, S0B1POS: Punc_Noun, S0B1POSLemma: Punc_d, S0B1Token: :_D, S0Lemma: :, S0POS: Punc, S0Token: :, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

262- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [", D, - ,.. ]

B0Lemma: ", B0POS: Punc, B0Token: ", B1Lemma: d, B1POS: Noun, B1Token: D, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

263- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= ["]   B= [D, -, 8'ler ,.. ]

B0Lemma: d, B0POS: Noun, B0Token: D, B1Lemma: -, B1POS: Punc, B1Token: -, S0B0Distance: 1, S0B0Lemma: "_d, S0B0LemmaPOS: "_Noun, S0B0POS: Punc_Noun, S0B0POSLemma: Punc_d, S0B0Token: "_D, S0B1Lemma: "_-, S0B1LemmaPOS: "_Punc, S0B1POS: Punc_Punc, S0B1POSLemma: Punc_-, S0B1Token: "_-, S0Lemma: ", S0POS: Punc, S0Token: ", transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

264- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [D, -, 8'ler ,.. ]

B0Lemma: d, B0POS: Noun, B0Token: D, B1Lemma: -, B1POS: Punc, B1Token: -, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

265- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [D]   B= [-, 8'ler, dine ,.. ]

B0Lemma: -, B0POS: Punc, B0Token: -, B1Lemma: 8, B1POS: Noun, B1Token: 8'ler, S0B0Distance: 1, S0B0Lemma: d_-, S0B0LemmaPOS: d_Punc, S0B0POS: Noun_Punc, S0B0POSLemma: Noun_-, S0B0Token: D_-, S0B1Lemma: d_8, S0B1LemmaPOS: d_Noun, S0B1POS: Noun_Noun, S0B1POSLemma: Noun_8, S0B1Token: D_8'ler, S0Lemma: d, S0POS: Noun, S0Token: D, d_-_hasRighDep_PUNCTUATION: true, d_hasRighDep_PUNCTUATION: true, d_isGouvernedBy_değil: true, d_isGouvernedBy_değil_COORDINATION: true, hasRighDep_PUNCTUATION: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

266- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [-, 8'ler, dine ,.. ]

B0Lemma: -, B0POS: Punc, B0Token: -, B1Lemma: 8, B1POS: Noun, B1Token: 8'ler, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

267- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [-]   B= [8'ler, dine, dayalı ,.. ]

B0Lemma: 8, B0POS: Noun, B0Token: 8'ler, B1Lemma: dine, B1POS: Noun, B1Token: dine, S0B0Distance: 1, S0B0Lemma: -_8, S0B0LemmaPOS: -_Noun, S0B0POS: Punc_Noun, S0B0POSLemma: Punc_8, S0B0Token: -_8'ler, S0B1Lemma: -_dine, S0B1LemmaPOS: -_Noun, S0B1POS: Punc_Noun, S0B1POSLemma: Punc_dine, S0B1Token: -_dine, S0Lemma: -, S0POS: Punc, S0Token: -, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

268- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [8'ler, dine, dayalı ,.. ]

B0Lemma: 8, B0POS: Noun, B0Token: 8'ler, B1Lemma: dine, B1POS: Noun, B1Token: dine, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

269- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [8'ler]   B= [dine, dayalı, bir ,.. ]

8_isGouvernedBy_dine: true, 8_isGouvernedBy_dine_MWE: true, B0Lemma: dine, B0POS: Noun, B0Token: dine, B1Lemma: dayalı, B1POS: Adj, B1Token: dayalı, S0B0Distance: 1, S0B0Lemma: 8_dine, S0B0LemmaPOS: 8_Noun, S0B0POS: Noun_Noun, S0B0POSLemma: Noun_dine, S0B0Token: 8'ler_dine, S0B1Lemma: 8_dayalı, S0B1LemmaPOS: 8_Adj, S0B1POS: Noun_Adj, S0B1POSLemma: Noun_dayalı, S0B1Token: 8'ler_dayalı, S0Lemma: 8, S0POS: Noun, S0Token: 8'ler, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

270- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [dine, dayalı, bir ,.. ]

B0Lemma: dine, B0POS: Noun, B0Token: dine, B1Lemma: dayalı, B1POS: Adj, B1Token: dayalı, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

271- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [dine]   B= [dayalı, bir, _ ,.. ]

B0Lemma: dayalı, B0POS: Adj, B0Token: dayalı, B1Lemma: bir, B1POS: Adj, B1Token: bir, S0B0Distance: 1, S0B0Lemma: dine_dayalı, S0B0LemmaPOS: dine_Adj, S0B0POS: Noun_Adj, S0B0POSLemma: Noun_dayalı, S0B0Token: dine_dayalı, S0B1Lemma: dine_bir, S0B1LemmaPOS: dine_Adj, S0B1POS: Noun_Adj, S0B1POSLemma: Noun_bir, S0B1Token: dine_bir, S0Lemma: dine, S0POS: Noun, S0Token: dine, dine_isGouvernedBy_değil: true, dine_isGouvernedBy_değil_SUBJECT: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

272- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [dayalı, bir, _ ,.. ]

B0Lemma: dayalı, B0POS: Adj, B0Token: dayalı, B1Lemma: bir, B1POS: Adj, B1Token: bir, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

273- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [dayalı]   B= [bir, _, örgütlenme ,.. ]

B0Lemma: bir, B0POS: Adj, B0Token: bir, B1Lemma: örgütle, B1POS: Verb, B1Token: _, S0B0Distance: 1, S0B0Lemma: dayalı_bir, S0B0LemmaPOS: dayalı_Adj, S0B0POS: Adj_Adj, S0B0POSLemma: Adj_bir, S0B0Token: dayalı_bir, S0B1Lemma: dayalı_örgütle, S0B1LemmaPOS: dayalı_Verb, S0B1POS: Adj_Verb, S0B1POSLemma: Adj_örgütle, S0B1Token: dayalı__, S0Lemma: dayalı, S0POS: Adj, S0Token: dayalı, dayalı_isGouvernedBy__: true, dayalı_isGouvernedBy___MODIFIER: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

274- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [bir, _, örgütlenme ,.. ]

B0Lemma: bir, B0POS: Adj, B0Token: bir, B1Lemma: örgütle, B1POS: Verb, B1Token: _, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

275- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [bir]   B= [_, örgütlenme, değildir ,.. ]

B0Lemma: örgütle, B0POS: Verb, B0Token: _, B1Lemma: _, B1POS: Noun, B1Token: örgütlenme, S0B0Distance: 1, S0B0Lemma: bir_örgütle, S0B0LemmaPOS: bir_Verb, S0B0POS: Adj_Verb, S0B0POSLemma: Adj_örgütle, S0B0Token: bir__, S0B1Lemma: bir__, S0B1LemmaPOS: bir_Noun, S0B1POS: Adj_Noun, S0B1POSLemma: Adj__, S0B1Token: bir_örgütlenme, S0Lemma: bir, S0POS: Adj, S0Token: bir, bir_isGouvernedBy__: true, bir_isGouvernedBy___DETERMINER: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

276- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [_, örgütlenme, değildir ,.. ]

B0Lemma: örgütle, B0POS: Verb, B0Token: _, B1Lemma: _, B1POS: Noun, B1Token: örgütlenme, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

277- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [_]   B= [örgütlenme, değildir, . ,.. ]

B0Lemma: _, B0POS: Noun, B0Token: örgütlenme, B1Lemma: değil, B1POS: Postp, B1Token: değildir, S0B0Distance: 1, S0B0Lemma: örgütle__, S0B0LemmaPOS: örgütle_Noun, S0B0POS: Verb_Noun, S0B0POSLemma: Verb__, S0B0Token: __örgütlenme, S0B1Lemma: örgütle_değil, S0B1LemmaPOS: örgütle_Postp, S0B1POS: Verb_Postp, S0B1POSLemma: Verb_değil, S0B1Token: __değildir, S0Lemma: örgütle, S0POS: Verb, S0Token: _, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, örgütle_isGouvernedBy__: true, örgütle_isGouvernedBy___DERIV: true, 

278- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [örgütlenme, değildir, . ,.. ]

B0Lemma: _, B0POS: Noun, B0Token: örgütlenme, B1Lemma: değil, B1POS: Postp, B1Token: değildir, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

279- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [örgütlenme]   B= [değildir, . ,.. ]

B0Lemma: değil, B0POS: Postp, B0Token: değildir, B1Lemma: ., B1POS: Punc, B1Token: ., S0B0Distance: 1, S0B0Lemma: __değil, S0B0LemmaPOS: __Postp, S0B0POS: Noun_Postp, S0B0POSLemma: Noun_değil, S0B0Token: örgütlenme_değildir, S0B1Lemma: __., S0B1LemmaPOS: __Punc, S0B1POS: Noun_Punc, S0B1POSLemma: Noun_., S0B1Token: örgütlenme_., S0Lemma: _, S0POS: Noun, S0Token: örgütlenme, __isGouvernedBy_değil: true, __isGouvernedBy_değil_ARGUMENT: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

280- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [değildir, . ,.. ]

B0Lemma: değil, B0POS: Postp, B0Token: değildir, B1Lemma: ., B1POS: Punc, B1Token: ., transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

281- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [değildir]   B= [.]

B0Lemma: ., B0POS: Punc, B0Token: ., S0B0Distance: 1, S0B0Lemma: değil_., S0B0LemmaPOS: değil_Punc, S0B0POS: Postp_Punc, S0B0POSLemma: Postp_., S0B0Token: değildir_., S0Lemma: değil, S0POS: Postp, S0Token: değildir, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

282- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [.]

B0Lemma: ., B0POS: Punc, B0Token: ., transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

283- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [ ]

S0Lemma: ., S0POS: Punc, S0Token: ., transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

284- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

## Sentence No. 2431 - 
Başbakan Necmettin Erbakan imzasıyla TBMM'ye _ gönderilen yasa tasarısında , MGK'nın " Milli güvenliğe ilişkin devletin bekaası için çok _ önemli görev , yetki ve sorumluluk " _ taşıdığına dikkat _ çekilerek , " Bu görev , yetki ve sorumlulukların yerine _ getirilebilmesi , herşeyden önce konu ve alanlarında uzmanlaşmış , tecrübe ve bilgi birikimine sahip , ehliyet ve liyakatını kanıtlamış , gelişmiş beyin gücü ile bilimsel _ araştırma yetenekleri kazandırılmış , fikir üretebilecek şekilde yetiştirilmiş ve devamlı olarak _ çalışmalarına imkan _ sağlanan genç uzman ve uzman yardımcısı düzeyinde personelin istihdamı ile _ mümkündür " görüşüne yer verildi . 
### Existing MWEs: 
1- **dikkat çekilerek** (ID)
2- **yerine getirilebilmesi** (ID)
3- **yer verildi** (ID)



0- &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Başbakan, Necmettin, Erbakan ,.. ]

B0Lemma: başbakan, B0POS: Noun, B0Token: Başbakan, B1Lemma: Necmettin, B1POS: Noun, B1Token: Necmettin, 

1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Başbakan]   B= [Necmettin, Erbakan, imzasıyla ,.. ]

B0Lemma: Necmettin, B0POS: Noun, B0Token: Necmettin, B1Lemma: Erbakan, B1POS: Noun, B1Token: Erbakan, S0B0Distance: 1, S0B0Lemma: başbakan_Necmettin, S0B0LemmaPOS: başbakan_Noun, S0B0POS: Noun_Noun, S0B0POSLemma: Noun_Necmettin, S0B0Token: Başbakan_Necmettin, S0B1Lemma: başbakan_Erbakan, S0B1LemmaPOS: başbakan_Noun, S0B1POS: Noun_Noun, S0B1POSLemma: Noun_Erbakan, S0B1Token: Başbakan_Erbakan, S0Lemma: başbakan, S0POS: Noun, S0Token: Başbakan, başbakan_isGouvernedBy_Necmettin: true, başbakan_isGouvernedBy_Necmettin_MWE: true, 

2- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Necmettin, Erbakan, imzasıyla ,.. ]

B0Lemma: Necmettin, B0POS: Noun, B0Token: Necmettin, B1Lemma: Erbakan, B1POS: Noun, B1Token: Erbakan, transitionHistoryLength1: 0, 

3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Necmettin]   B= [Erbakan, imzasıyla, TBMM'ye ,.. ]

B0Lemma: Erbakan, B0POS: Noun, B0Token: Erbakan, B1Lemma: imza, B1POS: Noun, B1Token: imzasıyla, Necmettin_isGouvernedBy_Erbakan: true, Necmettin_isGouvernedBy_Erbakan_MWE: true, S0B0Distance: 1, S0B0Lemma: Necmettin_Erbakan, S0B0LemmaPOS: Necmettin_Noun, S0B0POS: Noun_Noun, S0B0POSLemma: Noun_Erbakan, S0B0Token: Necmettin_Erbakan, S0B1Lemma: Necmettin_imza, S0B1LemmaPOS: Necmettin_Noun, S0B1POS: Noun_Noun, S0B1POSLemma: Noun_imza, S0B1Token: Necmettin_imzasıyla, S0Lemma: Necmettin, S0POS: Noun, S0Token: Necmettin, transitionHistoryLength1: 2, transitionHistoryLength2: 20, 

4- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Erbakan, imzasıyla, TBMM'ye ,.. ]

B0Lemma: Erbakan, B0POS: Noun, B0Token: Erbakan, B1Lemma: imza, B1POS: Noun, B1Token: imzasıyla, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Erbakan]   B= [imzasıyla, TBMM'ye, _ ,.. ]

B0Lemma: imza, B0POS: Noun, B0Token: imzasıyla, B1Lemma: TBMM'ye, B1POS: ?, B1Token: TBMM'ye, Erbakan_isGouvernedBy_imza: true, Erbakan_isGouvernedBy_imza_POSSESSOR: true, S0B0Distance: 1, S0B0Lemma: Erbakan_imza, S0B0LemmaPOS: Erbakan_Noun, S0B0POS: Noun_Noun, S0B0POSLemma: Noun_imza, S0B0Token: Erbakan_imzasıyla, S0B1Lemma: Erbakan_TBMM'ye, S0B1LemmaPOS: Erbakan_?, S0B1POS: Noun_?, S0B1POSLemma: Noun_TBMM'ye, S0B1Token: Erbakan_TBMM'ye, S0Lemma: Erbakan, S0POS: Noun, S0Token: Erbakan, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

6- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [imzasıyla, TBMM'ye, _ ,.. ]

B0Lemma: imza, B0POS: Noun, B0Token: imzasıyla, B1Lemma: TBMM'ye, B1POS: ?, B1Token: TBMM'ye, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [imzasıyla]   B= [TBMM'ye, _, gönderilen ,.. ]

B0Lemma: TBMM'ye, B0POS: ?, B0Token: TBMM'ye, B1Lemma: gönder, B1POS: Verb, B1Token: _, S0B0Distance: 1, S0B0Lemma: imza_TBMM'ye, S0B0LemmaPOS: imza_?, S0B0POS: Noun_?, S0B0POSLemma: Noun_TBMM'ye, S0B0Token: imzasıyla_TBMM'ye, S0B1Lemma: imza_gönder, S0B1LemmaPOS: imza_Verb, S0B1POS: Noun_Verb, S0B1POSLemma: Noun_gönder, S0B1Token: imzasıyla__, S0Lemma: imza, S0POS: Noun, S0Token: imzasıyla, imza_isGouvernedBy_gönder: true, imza_isGouvernedBy_gönder_MODIFIER: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

8- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [TBMM'ye, _, gönderilen ,.. ]

B0Lemma: TBMM'ye, B0POS: ?, B0Token: TBMM'ye, B1Lemma: gönder, B1POS: Verb, B1Token: _, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [TBMM'ye]   B= [_, gönderilen, yasa ,.. ]

B0Lemma: gönder, B0POS: Verb, B0Token: _, B1Lemma: _, B1POS: Adj, B1Token: gönderilen, S0B0Distance: 1, S0B0Lemma: TBMM'ye_gönder, S0B0LemmaPOS: TBMM'ye_Verb, S0B0POS: ?_Verb, S0B0POSLemma: ?_gönder, S0B0Token: TBMM'ye__, S0B1Lemma: TBMM'ye__, S0B1LemmaPOS: TBMM'ye_Adj, S0B1POS: ?_Adj, S0B1POSLemma: ?__, S0B1Token: TBMM'ye_gönderilen, S0Lemma: TBMM'ye, S0POS: ?, S0Token: TBMM'ye, TBMM'ye_isGouvernedBy_gönder: true, TBMM'ye_isGouvernedBy_gönder_MODIFIER: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

10- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [_, gönderilen, yasa ,.. ]

B0Lemma: gönder, B0POS: Verb, B0Token: _, B1Lemma: _, B1POS: Adj, B1Token: gönderilen, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [_]   B= [gönderilen, yasa, tasarısında ,.. ]

B0Lemma: _, B0POS: Adj, B0Token: gönderilen, B1Lemma: yasa, B1POS: Noun, B1Token: yasa, S0B0Distance: 1, S0B0Lemma: gönder__, S0B0LemmaPOS: gönder_Adj, S0B0POS: Verb_Adj, S0B0POSLemma: Verb__, S0B0Token: __gönderilen, S0B1Lemma: gönder_yasa, S0B1LemmaPOS: gönder_Noun, S0B1POS: Verb_Noun, S0B1POSLemma: Verb_yasa, S0B1Token: __yasa, S0Lemma: gönder, S0POS: Verb, S0Token: _, gönder_isGouvernedBy__: true, gönder_isGouvernedBy___DERIV: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

12- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [gönderilen, yasa, tasarısında ,.. ]

B0Lemma: _, B0POS: Adj, B0Token: gönderilen, B1Lemma: yasa, B1POS: Noun, B1Token: yasa, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [gönderilen]   B= [yasa, tasarısında, , ,.. ]

B0Lemma: yasa, B0POS: Noun, B0Token: yasa, B1Lemma: tasarı, B1POS: Noun, B1Token: tasarısında, S0B0Distance: 1, S0B0Lemma: __yasa, S0B0LemmaPOS: __Noun, S0B0POS: Adj_Noun, S0B0POSLemma: Adj_yasa, S0B0Token: gönderilen_yasa, S0B1Lemma: __tasarı, S0B1LemmaPOS: __Noun, S0B1POS: Adj_Noun, S0B1POSLemma: Adj_tasarı, S0B1Token: gönderilen_tasarısında, S0Lemma: _, S0POS: Adj, S0Token: gönderilen, __isGouvernedBy_tasarı: true, __isGouvernedBy_tasarı_MODIFIER: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

14- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [yasa, tasarısında, , ,.. ]

B0Lemma: yasa, B0POS: Noun, B0Token: yasa, B1Lemma: tasarı, B1POS: Noun, B1Token: tasarısında, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [yasa]   B= [tasarısında, ,, MGK'nın ,.. ]

B0Lemma: tasarı, B0POS: Noun, B0Token: tasarısında, B1Lemma: ,, B1POS: Punc, B1Token: ,, S0B0Distance: 1, S0B0Lemma: yasa_tasarı, S0B0LemmaPOS: yasa_Noun, S0B0POS: Noun_Noun, S0B0POSLemma: Noun_tasarı, S0B0Token: yasa_tasarısında, S0B1Lemma: yasa_,, S0B1LemmaPOS: yasa_Punc, S0B1POS: Noun_Punc, S0B1POSLemma: Noun_,, S0B1Token: yasa_,, S0Lemma: yasa, S0POS: Noun, S0Token: yasa, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, yasa_isGouvernedBy_tasarı: true, yasa_isGouvernedBy_tasarı_MWE: true, 

16- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [tasarısında, ,, MGK'nın ,.. ]

B0Lemma: tasarı, B0POS: Noun, B0Token: tasarısında, B1Lemma: ,, B1POS: Punc, B1Token: ,, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [tasarısında]   B= [,, MGK'nın, " ,.. ]

B0Lemma: ,, B0POS: Punc, B0Token: ,, B1Lemma: Mgk, B1POS: Noun, B1Token: MGK'nın, S0B0Distance: 1, S0B0Lemma: tasarı_,, S0B0LemmaPOS: tasarı_Punc, S0B0POS: Noun_Punc, S0B0POSLemma: Noun_,, S0B0Token: tasarısında_,, S0B1Lemma: tasarı_Mgk, S0B1LemmaPOS: tasarı_Noun, S0B1POS: Noun_Noun, S0B1POSLemma: Noun_Mgk, S0B1Token: tasarısında_MGK'nın, S0Lemma: tasarı, S0POS: Noun, S0Token: tasarısında, hasRighDep_PUNCTUATION: true, tasarı_,_hasRighDep_PUNCTUATION: true, tasarı_hasRighDep_PUNCTUATION: true, tasarı_isGouvernedBy_ver: true, tasarı_isGouvernedBy_ver_MODIFIER: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

18- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, MGK'nın, " ,.. ]

B0Lemma: ,, B0POS: Punc, B0Token: ,, B1Lemma: Mgk, B1POS: Noun, B1Token: MGK'nın, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [MGK'nın, ", Milli ,.. ]

B0Lemma: Mgk, B0POS: Noun, B0Token: MGK'nın, B1Lemma: ", B1POS: Punc, B1Token: ", S0B0Distance: 1, S0B0Lemma: ,_Mgk, S0B0LemmaPOS: ,_Noun, S0B0POS: Punc_Noun, S0B0POSLemma: Punc_Mgk, S0B0Token: ,_MGK'nın, S0B1Lemma: ,_", S0B1LemmaPOS: ,_Punc, S0B1POS: Punc_Punc, S0B1POSLemma: Punc_", S0B1Token: ,_", S0Lemma: ,, S0POS: Punc, S0Token: ,, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

20- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [MGK'nın, ", Milli ,.. ]

B0Lemma: Mgk, B0POS: Noun, B0Token: MGK'nın, B1Lemma: ", B1POS: Punc, B1Token: ", transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [MGK'nın]   B= [", Milli, güvenliğe ,.. ]

B0Lemma: ", B0POS: Punc, B0Token: ", B1Lemma: milli, B1POS: Adj, B1Token: Milli, Mgk_"_hasRighDep_PUNCTUATION: true, Mgk_hasRighDep_PUNCTUATION: true, Mgk_isGouvernedBy_ver: true, Mgk_isGouvernedBy_ver_SUBJECT: true, S0B0Distance: 1, S0B0Lemma: Mgk_", S0B0LemmaPOS: Mgk_Punc, S0B0POS: Noun_Punc, S0B0POSLemma: Noun_", S0B0Token: MGK'nın_", S0B1Lemma: Mgk_milli, S0B1LemmaPOS: Mgk_Adj, S0B1POS: Noun_Adj, S0B1POSLemma: Noun_milli, S0B1Token: MGK'nın_Milli, S0Lemma: Mgk, S0POS: Noun, S0Token: MGK'nın, hasRighDep_PUNCTUATION: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

22- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [", Milli, güvenliğe ,.. ]

B0Lemma: ", B0POS: Punc, B0Token: ", B1Lemma: milli, B1POS: Adj, B1Token: Milli, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

23- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= ["]   B= [Milli, güvenliğe, ilişkin ,.. ]

B0Lemma: milli, B0POS: Adj, B0Token: Milli, B1Lemma: güvenlik, B1POS: Noun, B1Token: güvenliğe, S0B0Distance: 1, S0B0Lemma: "_milli, S0B0LemmaPOS: "_Adj, S0B0POS: Punc_Adj, S0B0POSLemma: Punc_milli, S0B0Token: "_Milli, S0B1Lemma: "_güvenlik, S0B1LemmaPOS: "_Noun, S0B1POS: Punc_Noun, S0B1POSLemma: Punc_güvenlik, S0B1Token: "_güvenliğe, S0Lemma: ", S0POS: Punc, S0Token: ", transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

24- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Milli, güvenliğe, ilişkin ,.. ]

B0Lemma: milli, B0POS: Adj, B0Token: Milli, B1Lemma: güvenlik, B1POS: Noun, B1Token: güvenliğe, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

25- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Milli]   B= [güvenliğe, ilişkin, devletin ,.. ]

B0Lemma: güvenlik, B0POS: Noun, B0Token: güvenliğe, B1Lemma: ilişkin, B1POS: Postp, B1Token: ilişkin, S0B0Distance: 1, S0B0Lemma: milli_güvenlik, S0B0LemmaPOS: milli_Noun, S0B0POS: Adj_Noun, S0B0POSLemma: Adj_güvenlik, S0B0Token: Milli_güvenliğe, S0B1Lemma: milli_ilişkin, S0B1LemmaPOS: milli_Postp, S0B1POS: Adj_Postp, S0B1POSLemma: Adj_ilişkin, S0B1Token: Milli_ilişkin, S0Lemma: milli, S0POS: Adj, S0Token: Milli, milli_isGouvernedBy_güvenlik: true, milli_isGouvernedBy_güvenlik_MODIFIER: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

26- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [güvenliğe, ilişkin, devletin ,.. ]

B0Lemma: güvenlik, B0POS: Noun, B0Token: güvenliğe, B1Lemma: ilişkin, B1POS: Postp, B1Token: ilişkin, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

27- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [güvenliğe]   B= [ilişkin, devletin, bekaası ,.. ]

B0Lemma: ilişkin, B0POS: Postp, B0Token: ilişkin, B1Lemma: devlet, B1POS: Noun, B1Token: devletin, S0B0Distance: 1, S0B0Lemma: güvenlik_ilişkin, S0B0LemmaPOS: güvenlik_Postp, S0B0POS: Noun_Postp, S0B0POSLemma: Noun_ilişkin, S0B0Token: güvenliğe_ilişkin, S0B1Lemma: güvenlik_devlet, S0B1LemmaPOS: güvenlik_Noun, S0B1POS: Noun_Noun, S0B1POSLemma: Noun_devlet, S0B1Token: güvenliğe_devletin, S0Lemma: güvenlik, S0POS: Noun, S0Token: güvenliğe, güvenlik_isGouvernedBy_ilişkin: true, güvenlik_isGouvernedBy_ilişkin_ARGUMENT: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

28- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ilişkin, devletin, bekaası ,.. ]

B0Lemma: ilişkin, B0POS: Postp, B0Token: ilişkin, B1Lemma: devlet, B1POS: Noun, B1Token: devletin, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

29- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ilişkin]   B= [devletin, bekaası, için ,.. ]

B0Lemma: devlet, B0POS: Noun, B0Token: devletin, B1Lemma: bekaa, B1POS: Noun, B1Token: bekaası, S0B0Distance: 1, S0B0Lemma: ilişkin_devlet, S0B0LemmaPOS: ilişkin_Noun, S0B0POS: Postp_Noun, S0B0POSLemma: Postp_devlet, S0B0Token: ilişkin_devletin, S0B1Lemma: ilişkin_bekaa, S0B1LemmaPOS: ilişkin_Noun, S0B1POS: Postp_Noun, S0B1POSLemma: Postp_bekaa, S0B1Token: ilişkin_bekaası, S0Lemma: ilişkin, S0POS: Postp, S0Token: ilişkin, ilişkin_isGouvernedBy_ver: true, ilişkin_isGouvernedBy_ver_MODIFIER: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

30- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [devletin, bekaası, için ,.. ]

B0Lemma: devlet, B0POS: Noun, B0Token: devletin, B1Lemma: bekaa, B1POS: Noun, B1Token: bekaası, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

31- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [devletin]   B= [bekaası, için, çok ,.. ]

B0Lemma: bekaa, B0POS: Noun, B0Token: bekaası, B1Lemma: için, B1POS: Postp, B1Token: için, S0B0Distance: 1, S0B0Lemma: devlet_bekaa, S0B0LemmaPOS: devlet_Noun, S0B0POS: Noun_Noun, S0B0POSLemma: Noun_bekaa, S0B0Token: devletin_bekaası, S0B1Lemma: devlet_için, S0B1LemmaPOS: devlet_Postp, S0B1POS: Noun_Postp, S0B1POSLemma: Noun_için, S0B1Token: devletin_için, S0Lemma: devlet, S0POS: Noun, S0Token: devletin, devlet_isGouvernedBy_bekaa: true, devlet_isGouvernedBy_bekaa_POSSESSOR: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

32- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [bekaası, için, çok ,.. ]

B0Lemma: bekaa, B0POS: Noun, B0Token: bekaası, B1Lemma: için, B1POS: Postp, B1Token: için, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

33- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [bekaası]   B= [için, çok, _ ,.. ]

B0Lemma: için, B0POS: Postp, B0Token: için, B1Lemma: çok, B1POS: Adverb, B1Token: çok, S0B0Distance: 1, S0B0Lemma: bekaa_için, S0B0LemmaPOS: bekaa_Postp, S0B0POS: Noun_Postp, S0B0POSLemma: Noun_için, S0B0Token: bekaası_için, S0B1Lemma: bekaa_çok, S0B1LemmaPOS: bekaa_Adverb, S0B1POS: Noun_Adverb, S0B1POSLemma: Noun_çok, S0B1Token: bekaası_çok, S0Lemma: bekaa, S0POS: Noun, S0Token: bekaası, bekaa_isGouvernedBy_için: true, bekaa_isGouvernedBy_için_ARGUMENT: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

34- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [için, çok, _ ,.. ]

B0Lemma: için, B0POS: Postp, B0Token: için, B1Lemma: çok, B1POS: Adverb, B1Token: çok, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

35- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [için]   B= [çok, _, önemli ,.. ]

B0Lemma: çok, B0POS: Adverb, B0Token: çok, B1Lemma: önem, B1POS: Noun, B1Token: _, S0B0Distance: 1, S0B0Lemma: için_çok, S0B0LemmaPOS: için_Adverb, S0B0POS: Postp_Adverb, S0B0POSLemma: Postp_çok, S0B0Token: için_çok, S0B1Lemma: için_önem, S0B1LemmaPOS: için_Noun, S0B1POS: Postp_Noun, S0B1POSLemma: Postp_önem, S0B1Token: için__, S0Lemma: için, S0POS: Postp, S0Token: için, için_isGouvernedBy_ver: true, için_isGouvernedBy_ver_MODIFIER: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

36- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [çok, _, önemli ,.. ]

B0Lemma: çok, B0POS: Adverb, B0Token: çok, B1Lemma: önem, B1POS: Noun, B1Token: _, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

37- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [çok]   B= [_, önemli, görev ,.. ]

B0Lemma: önem, B0POS: Noun, B0Token: _, B1Lemma: _, B1POS: Adj, B1Token: önemli, S0B0Distance: 1, S0B0Lemma: çok_önem, S0B0LemmaPOS: çok_Noun, S0B0POS: Adverb_Noun, S0B0POSLemma: Adverb_önem, S0B0Token: çok__, S0B1Lemma: çok__, S0B1LemmaPOS: çok_Adj, S0B1POS: Adverb_Adj, S0B1POSLemma: Adverb__, S0B1Token: çok_önemli, S0Lemma: çok, S0POS: Adverb, S0Token: çok, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, çok_isGouvernedBy__: true, çok_isGouvernedBy___DETERMINER: true, 

38- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [_, önemli, görev ,.. ]

B0Lemma: önem, B0POS: Noun, B0Token: _, B1Lemma: _, B1POS: Adj, B1Token: önemli, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

39- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [_]   B= [önemli, görev, , ,.. ]

B0Lemma: _, B0POS: Adj, B0Token: önemli, B1Lemma: görev, B1POS: Noun, B1Token: görev, S0B0Distance: 1, S0B0Lemma: önem__, S0B0LemmaPOS: önem_Adj, S0B0POS: Noun_Adj, S0B0POSLemma: Noun__, S0B0Token: __önemli, S0B1Lemma: önem_görev, S0B1LemmaPOS: önem_Noun, S0B1POS: Noun_Noun, S0B1POSLemma: Noun_görev, S0B1Token: __görev, S0Lemma: önem, S0POS: Noun, S0Token: _, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, önem_isGouvernedBy__: true, önem_isGouvernedBy___DERIV: true, 

40- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [önemli, görev, , ,.. ]

B0Lemma: _, B0POS: Adj, B0Token: önemli, B1Lemma: görev, B1POS: Noun, B1Token: görev, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

41- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [önemli]   B= [görev, ,, yetki ,.. ]

B0Lemma: görev, B0POS: Noun, B0Token: görev, B1Lemma: ,, B1POS: Punc, B1Token: ,, S0B0Distance: 1, S0B0Lemma: __görev, S0B0LemmaPOS: __Noun, S0B0POS: Adj_Noun, S0B0POSLemma: Adj_görev, S0B0Token: önemli_görev, S0B1Lemma: __,, S0B1LemmaPOS: __Punc, S0B1POS: Adj_Punc, S0B1POSLemma: Adj_,, S0B1Token: önemli_,, S0Lemma: _, S0POS: Adj, S0Token: önemli, __isGouvernedBy_görev: true, __isGouvernedBy_görev_MODIFIER: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

42- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [görev, ,, yetki ,.. ]

B0Lemma: görev, B0POS: Noun, B0Token: görev, B1Lemma: ,, B1POS: Punc, B1Token: ,, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

43- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [görev]   B= [,, yetki, ve ,.. ]

B0Lemma: ,, B0POS: Punc, B0Token: ,, B1Lemma: yetki, B1POS: Noun, B1Token: yetki, S0B0Distance: 1, S0B0Lemma: görev_,, S0B0LemmaPOS: görev_Punc, S0B0POS: Noun_Punc, S0B0POSLemma: Noun_,, S0B0Token: görev_,, S0B1Lemma: görev_yetki, S0B1LemmaPOS: görev_Noun, S0B1POS: Noun_Noun, S0B1POSLemma: Noun_yetki, S0B1Token: görev_yetki, S0Lemma: görev, S0POS: Noun, S0Token: görev, görev_,_hasRighDep_PUNCTUATION: true, görev_hasRighDep_PUNCTUATION: true, görev_isGouvernedBy_yetki: true, görev_isGouvernedBy_yetki_COORDINATION: true, hasRighDep_PUNCTUATION: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

44- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, yetki, ve ,.. ]

B0Lemma: ,, B0POS: Punc, B0Token: ,, B1Lemma: yetki, B1POS: Noun, B1Token: yetki, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

45- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [yetki, ve, sorumluluk ,.. ]

B0Lemma: yetki, B0POS: Noun, B0Token: yetki, B1Lemma: ve, B1POS: Conj, B1Token: ve, S0B0Distance: 1, S0B0Lemma: ,_yetki, S0B0LemmaPOS: ,_Noun, S0B0POS: Punc_Noun, S0B0POSLemma: Punc_yetki, S0B0Token: ,_yetki, S0B1Lemma: ,_ve, S0B1LemmaPOS: ,_Conj, S0B1POS: Punc_Conj, S0B1POSLemma: Punc_ve, S0B1Token: ,_ve, S0Lemma: ,, S0POS: Punc, S0Token: ,, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

46- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [yetki, ve, sorumluluk ,.. ]

B0Lemma: yetki, B0POS: Noun, B0Token: yetki, B1Lemma: ve, B1POS: Conj, B1Token: ve, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

47- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [yetki]   B= [ve, sorumluluk, " ,.. ]

B0Lemma: ve, B0POS: Conj, B0Token: ve, B1Lemma: sorumluluk, B1POS: Noun, B1Token: sorumluluk, S0B0Distance: 1, S0B0Lemma: yetki_ve, S0B0LemmaPOS: yetki_Conj, S0B0POS: Noun_Conj, S0B0POSLemma: Noun_ve, S0B0Token: yetki_ve, S0B1Lemma: yetki_sorumluluk, S0B1LemmaPOS: yetki_Noun, S0B1POS: Noun_Noun, S0B1POSLemma: Noun_sorumluluk, S0B1Token: yetki_sorumluluk, S0Lemma: yetki, S0POS: Noun, S0Token: yetki, hasRighDep_CONJUNCTION: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, yetki_hasRighDep_CONJUNCTION: true, yetki_isGouvernedBy_sorumluluk: true, yetki_isGouvernedBy_sorumluluk_COORDINATION: true, yetki_ve_hasRighDep_CONJUNCTION: true, 

48- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ve, sorumluluk, " ,.. ]

B0Lemma: ve, B0POS: Conj, B0Token: ve, B1Lemma: sorumluluk, B1POS: Noun, B1Token: sorumluluk, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

49- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ve]   B= [sorumluluk, ", _ ,.. ]

B0Lemma: sorumluluk, B0POS: Noun, B0Token: sorumluluk, B1Lemma: ", B1POS: Punc, B1Token: ", S0B0Distance: 1, S0B0Lemma: ve_sorumluluk, S0B0LemmaPOS: ve_Noun, S0B0POS: Conj_Noun, S0B0POSLemma: Conj_sorumluluk, S0B0Token: ve_sorumluluk, S0B1Lemma: ve_", S0B1LemmaPOS: ve_Punc, S0B1POS: Conj_Punc, S0B1POSLemma: Conj_", S0B1Token: ve_", S0Lemma: ve, S0POS: Conj, S0Token: ve, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

50- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [sorumluluk, ", _ ,.. ]

B0Lemma: sorumluluk, B0POS: Noun, B0Token: sorumluluk, B1Lemma: ", B1POS: Punc, B1Token: ", transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

51- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [sorumluluk]   B= [", _, taşıdığına ,.. ]

B0Lemma: ", B0POS: Punc, B0Token: ", B1Lemma: taşı, B1POS: Verb, B1Token: _, S0B0Distance: 1, S0B0Lemma: sorumluluk_", S0B0LemmaPOS: sorumluluk_Punc, S0B0POS: Noun_Punc, S0B0POSLemma: Noun_", S0B0Token: sorumluluk_", S0B1Lemma: sorumluluk_taşı, S0B1LemmaPOS: sorumluluk_Verb, S0B1POS: Noun_Verb, S0B1POSLemma: Noun_taşı, S0B1Token: sorumluluk__, S0Lemma: sorumluluk, S0POS: Noun, S0Token: sorumluluk, hasRighDep_PUNCTUATION: true, sorumluluk_"_hasRighDep_PUNCTUATION: true, sorumluluk_hasRighDep_PUNCTUATION: true, sorumluluk_isGouvernedBy_ver: true, sorumluluk_isGouvernedBy_ver_SUBJECT: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

52- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [", _, taşıdığına ,.. ]

B0Lemma: ", B0POS: Punc, B0Token: ", B1Lemma: taşı, B1POS: Verb, B1Token: _, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

53- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= ["]   B= [_, taşıdığına, dikkat ,.. ]

B0Lemma: taşı, B0POS: Verb, B0Token: _, B1Lemma: _, B1POS: Noun, B1Token: taşıdığına, S0B0Distance: 1, S0B0Lemma: "_taşı, S0B0LemmaPOS: "_Verb, S0B0POS: Punc_Verb, S0B0POSLemma: Punc_taşı, S0B0Token: "__, S0B1Lemma: "__, S0B1LemmaPOS: "_Noun, S0B1POS: Punc_Noun, S0B1POSLemma: Punc__, S0B1Token: "_taşıdığına, S0Lemma: ", S0POS: Punc, S0Token: ", transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

54- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [_, taşıdığına, dikkat ,.. ]

B0Lemma: taşı, B0POS: Verb, B0Token: _, B1Lemma: _, B1POS: Noun, B1Token: taşıdığına, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

55- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [_]   B= [taşıdığına, dikkat, _ ,.. ]

B0Lemma: _, B0POS: Noun, B0Token: taşıdığına, B1Lemma: dikkat, B1POS: Noun, B1Token: dikkat, S0B0Distance: 1, S0B0Lemma: taşı__, S0B0LemmaPOS: taşı_Noun, S0B0POS: Verb_Noun, S0B0POSLemma: Verb__, S0B0Token: __taşıdığına, S0B1Lemma: taşı_dikkat, S0B1LemmaPOS: taşı_Noun, S0B1POS: Verb_Noun, S0B1POSLemma: Verb_dikkat, S0B1Token: __dikkat, S0Lemma: taşı, S0POS: Verb, S0Token: _, taşı_isGouvernedBy__: true, taşı_isGouvernedBy___DERIV: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

56- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [taşıdığına, dikkat, _ ,.. ]

B0Lemma: _, B0POS: Noun, B0Token: taşıdığına, B1Lemma: dikkat, B1POS: Noun, B1Token: dikkat, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

57- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [taşıdığına]   B= [dikkat, _, çekilerek ,.. ]

B0Lemma: dikkat, B0POS: Noun, B0Token: dikkat, B1Lemma: çek, B1POS: Verb, B1Token: _, S0B0Distance: 1, S0B0Lemma: __dikkat, S0B0LemmaPOS: __Noun, S0B0POS: Noun_Noun, S0B0POSLemma: Noun_dikkat, S0B0Token: taşıdığına_dikkat, S0B1Lemma: __çek, S0B1LemmaPOS: __Verb, S0B1POS: Noun_Verb, S0B1POSLemma: Noun_çek, S0B1Token: taşıdığına__, S0Lemma: _, S0POS: Noun, S0Token: taşıdığına, __isGouvernedBy_çek: true, __isGouvernedBy_çek_MODIFIER: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

58- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [dikkat, _, çekilerek ,.. ]

B0Lemma: dikkat, B0POS: Noun, B0Token: dikkat, B1Lemma: çek, B1POS: Verb, B1Token: _, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

59- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [dikkat]   B= [_, çekilerek, , ,.. ]

B0Lemma: çek, B0POS: Verb, B0Token: _, B1Lemma: _, B1POS: Adverb, B1Token: çekilerek, S0B0Distance: 1, S0B0Lemma: dikkat_çek, S0B0LemmaPOS: dikkat_Verb, S0B0POS: Noun_Verb, S0B0POSLemma: Noun_çek, S0B0Token: dikkat__, S0B1Lemma: dikkat__, S0B1LemmaPOS: dikkat_Adverb, S0B1POS: Noun_Adverb, S0B1POSLemma: Noun__, S0B1Token: dikkat_çekilerek, S0Lemma: dikkat, S0POS: Noun, S0Token: dikkat, dikkat_isGouvernedBy_çek: true, dikkat_isGouvernedBy_çek_MWE: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

60- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [dikkat, _]   B= [çekilerek, ,, " ,.. ]

B0Lemma: _, B0POS: Adverb, B0Token: çekilerek, B1Lemma: ,, B1POS: Punc, B1Token: ,, S0B0Distance: 1, S0B0Lemma: çek__, S0B0LemmaPOS: çek_Adverb, S0B0POS: Verb_Adverb, S0B0POSLemma: Verb__, S0B0Token: __çekilerek, S0B1Lemma: çek_,, S0B1LemmaPOS: çek_Punc, S0B1POS: Verb_Punc, S0B1POSLemma: Verb_,, S0B1Token: __,, S0Lemma: çek, S0POS: Verb, S0Token: _, S1B0Lemma: dikkat__, S1B0LemmaPOS: dikkat_Adverb, S1B0POS: Noun_Adverb, S1B0POSLemma: Noun__, S1B0Token: dikkat_çekilerek, S1Lemma: dikkat, S1POS: Noun, S1S0Lemma: dikkat_çek, S1S0LemmaPOS: dikkat_Verb, S1S0POS: Noun_Verb, S1S0POSLemma: Noun_çek, S1S0Token: dikkat__, S1Token: dikkat, SyntaxicRelation: -MWE, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, çek_isGouvernedBy__: true, çek_isGouvernedBy___DERIV: true, 

61- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [dikkat]   B= [çekilerek, ,, " ,.. ]

B0Lemma: _, B0POS: Adverb, B0Token: çekilerek, B1Lemma: ,, B1POS: Punc, B1Token: ,, S0B0Distance: 2, S0B0Lemma: dikkat__, S0B0LemmaPOS: dikkat_Adverb, S0B0POS: Noun_Adverb, S0B0POSLemma: Noun__, S0B0Token: dikkat_çekilerek, S0B1Lemma: dikkat_,, S0B1LemmaPOS: dikkat_Punc, S0B1POS: Noun_Punc, S0B1POSLemma: Noun_,, S0B1Token: dikkat_,, S0Lemma: dikkat, S0POS: Noun, S0Token: dikkat, transitionHistoryLength1: 0, transitionHistoryLength2: 00, transitionHistoryLength3: 002, 

62- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [dikkat, çekilerek]   B= [,, ", Bu ,.. ]

B0Lemma: ,, B0POS: Punc, B0Token: ,, B1Lemma: ", B1POS: Punc, B1Token: ", S0B0Distance: 1, S0B0Lemma: __,, S0B0LemmaPOS: __Punc, S0B0POS: Adverb_Punc, S0B0POSLemma: Adverb_,, S0B0Token: çekilerek_,, S0B1Lemma: __", S0B1LemmaPOS: __Punc, S0B1POS: Adverb_Punc, S0B1POSLemma: Adverb_", S0B1Token: çekilerek_", S0Lemma: _, S0POS: Adverb, S0Token: çekilerek, S1B0Lemma: dikkat_,, S1B0LemmaPOS: dikkat_Punc, S1B0POS: Noun_Punc, S1B0POSLemma: Noun_,, S1B0Token: dikkat_,, S1Lemma: dikkat, S1POS: Noun, S1S0Lemma: dikkat__, S1S0LemmaPOS: dikkat_Adverb, S1S0POS: Noun_Adverb, S1S0POSLemma: Noun__, S1S0Token: dikkat_çekilerek, S1Token: dikkat, __"_hasRighDep_PUNCTUATION: true, __,_hasRighDep_PUNCTUATION: true, __hasRighDep_PUNCTUATION: true, __isGouvernedBy_ver: true, __isGouvernedBy_ver_MODIFIER: true, hasRighDep_PUNCTUATION: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 200, 

63- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[dikkat, çekilerek]]   B= [,, ", Bu ,.. ]

B0Lemma: ,, B0POS: Punc, B0Token: ,, B1Lemma: ", B1POS: Punc, B1Token: ", S0B0Distance: 1, S0B0Lemma: dikkat___,, S0B0LemmaPOS: dikkat___Punc, S0B0POS: Noun_Adverb_Punc, S0B0POSLemma: Noun_Adverb_,, S0B0Token: dikkat_çekilerek_,, S0B1Lemma: dikkat___", S0B1LemmaPOS: dikkat___Punc, S0B1POS: Noun_Adverb_Punc, S0B1POSLemma: Noun_Adverb_", S0B1Token: dikkat_çekilerek_", S0Lemma: dikkat__, S0POS: Noun_Adverb, S0Token: dikkat_çekilerek, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

64- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, ", Bu ,.. ]

B0Lemma: ,, B0POS: Punc, B0Token: ,, B1Lemma: ", B1POS: Punc, B1Token: ", transitionHistoryLength1: 1, transitionHistoryLength2: 10, transitionHistoryLength3: 102, 

65- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [", Bu, görev ,.. ]

B0Lemma: ", B0POS: Punc, B0Token: ", B1Lemma: bu, B1POS: Det, B1Token: Bu, S0B0Distance: 1, S0B0Lemma: ,_", S0B0LemmaPOS: ,_Punc, S0B0POS: Punc_Punc, S0B0POSLemma: Punc_", S0B0Token: ,_", S0B1Lemma: ,_bu, S0B1LemmaPOS: ,_Det, S0B1POS: Punc_Det, S0B1POSLemma: Punc_bu, S0B1Token: ,_Bu, S0Lemma: ,, S0POS: Punc, S0Token: ,, transitionHistoryLength1: 2, transitionHistoryLength2: 21, transitionHistoryLength3: 210, 

66- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [", Bu, görev ,.. ]

B0Lemma: ", B0POS: Punc, B0Token: ", B1Lemma: bu, B1POS: Det, B1Token: Bu, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 021, 

67- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= ["]   B= [Bu, görev, , ,.. ]

B0Lemma: bu, B0POS: Det, B0Token: Bu, B1Lemma: görev, B1POS: Noun, B1Token: görev, S0B0Distance: 1, S0B0Lemma: "_bu, S0B0LemmaPOS: "_Det, S0B0POS: Punc_Det, S0B0POSLemma: Punc_bu, S0B0Token: "_Bu, S0B1Lemma: "_görev, S0B1LemmaPOS: "_Noun, S0B1POS: Punc_Noun, S0B1POSLemma: Punc_görev, S0B1Token: "_görev, S0Lemma: ", S0POS: Punc, S0Token: ", transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

68- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Bu, görev, , ,.. ]

B0Lemma: bu, B0POS: Det, B0Token: Bu, B1Lemma: görev, B1POS: Noun, B1Token: görev, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

69- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Bu]   B= [görev, ,, yetki ,.. ]

B0Lemma: görev, B0POS: Noun, B0Token: görev, B1Lemma: ,, B1POS: Punc, B1Token: ,, S0B0Distance: 1, S0B0Lemma: bu_görev, S0B0LemmaPOS: bu_Noun, S0B0POS: Det_Noun, S0B0POSLemma: Det_görev, S0B0Token: Bu_görev, S0B1Lemma: bu_,, S0B1LemmaPOS: bu_Punc, S0B1POS: Det_Punc, S0B1POSLemma: Det_,, S0B1Token: Bu_,, S0Lemma: bu, S0POS: Det, S0Token: Bu, bu_isGouvernedBy_görev: true, bu_isGouvernedBy_görev_DETERMINER: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

70- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [görev, ,, yetki ,.. ]

B0Lemma: görev, B0POS: Noun, B0Token: görev, B1Lemma: ,, B1POS: Punc, B1Token: ,, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

71- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [görev]   B= [,, yetki, ve ,.. ]

B0Lemma: ,, B0POS: Punc, B0Token: ,, B1Lemma: yetki, B1POS: Noun, B1Token: yetki, S0B0Distance: 1, S0B0Lemma: görev_,, S0B0LemmaPOS: görev_Punc, S0B0POS: Noun_Punc, S0B0POSLemma: Noun_,, S0B0Token: görev_,, S0B1Lemma: görev_yetki, S0B1LemmaPOS: görev_Noun, S0B1POS: Noun_Noun, S0B1POSLemma: Noun_yetki, S0B1Token: görev_yetki, S0Lemma: görev, S0POS: Noun, S0Token: görev, görev_,_hasRighDep_PUNCTUATION: true, görev_hasRighDep_PUNCTUATION: true, görev_isGouvernedBy_yetki: true, görev_isGouvernedBy_yetki_COORDINATION: true, hasRighDep_PUNCTUATION: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

72- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, yetki, ve ,.. ]

B0Lemma: ,, B0POS: Punc, B0Token: ,, B1Lemma: yetki, B1POS: Noun, B1Token: yetki, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

73- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [yetki, ve, sorumlulukların ,.. ]

B0Lemma: yetki, B0POS: Noun, B0Token: yetki, B1Lemma: ve, B1POS: Conj, B1Token: ve, S0B0Distance: 1, S0B0Lemma: ,_yetki, S0B0LemmaPOS: ,_Noun, S0B0POS: Punc_Noun, S0B0POSLemma: Punc_yetki, S0B0Token: ,_yetki, S0B1Lemma: ,_ve, S0B1LemmaPOS: ,_Conj, S0B1POS: Punc_Conj, S0B1POSLemma: Punc_ve, S0B1Token: ,_ve, S0Lemma: ,, S0POS: Punc, S0Token: ,, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

74- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [yetki, ve, sorumlulukların ,.. ]

B0Lemma: yetki, B0POS: Noun, B0Token: yetki, B1Lemma: ve, B1POS: Conj, B1Token: ve, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

75- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [yetki]   B= [ve, sorumlulukların, yerine ,.. ]

B0Lemma: ve, B0POS: Conj, B0Token: ve, B1Lemma: sorumluluk, B1POS: Noun, B1Token: sorumlulukların, S0B0Distance: 1, S0B0Lemma: yetki_ve, S0B0LemmaPOS: yetki_Conj, S0B0POS: Noun_Conj, S0B0POSLemma: Noun_ve, S0B0Token: yetki_ve, S0B1Lemma: yetki_sorumluluk, S0B1LemmaPOS: yetki_Noun, S0B1POS: Noun_Noun, S0B1POSLemma: Noun_sorumluluk, S0B1Token: yetki_sorumlulukların, S0Lemma: yetki, S0POS: Noun, S0Token: yetki, hasRighDep_CONJUNCTION: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, yetki_hasRighDep_CONJUNCTION: true, yetki_isGouvernedBy_sorumluluk: true, yetki_isGouvernedBy_sorumluluk_COORDINATION: true, yetki_ve_hasRighDep_CONJUNCTION: true, 

76- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ve, sorumlulukların, yerine ,.. ]

B0Lemma: ve, B0POS: Conj, B0Token: ve, B1Lemma: sorumluluk, B1POS: Noun, B1Token: sorumlulukların, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

77- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ve]   B= [sorumlulukların, yerine, _ ,.. ]

B0Lemma: sorumluluk, B0POS: Noun, B0Token: sorumlulukların, B1Lemma: yer, B1POS: Noun, B1Token: yerine, S0B0Distance: 1, S0B0Lemma: ve_sorumluluk, S0B0LemmaPOS: ve_Noun, S0B0POS: Conj_Noun, S0B0POSLemma: Conj_sorumluluk, S0B0Token: ve_sorumlulukların, S0B1Lemma: ve_yer, S0B1LemmaPOS: ve_Noun, S0B1POS: Conj_Noun, S0B1POSLemma: Conj_yer, S0B1Token: ve_yerine, S0Lemma: ve, S0POS: Conj, S0Token: ve, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

78- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [sorumlulukların, yerine, _ ,.. ]

B0Lemma: sorumluluk, B0POS: Noun, B0Token: sorumlulukların, B1Lemma: yer, B1POS: Noun, B1Token: yerine, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

79- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [sorumlulukların]   B= [yerine, _, getirilebilmesi ,.. ]

B0Lemma: yer, B0POS: Noun, B0Token: yerine, B1Lemma: getir, B1POS: Verb, B1Token: _, S0B0Distance: 1, S0B0Lemma: sorumluluk_yer, S0B0LemmaPOS: sorumluluk_Noun, S0B0POS: Noun_Noun, S0B0POSLemma: Noun_yer, S0B0Token: sorumlulukların_yerine, S0B1Lemma: sorumluluk_getir, S0B1LemmaPOS: sorumluluk_Verb, S0B1POS: Noun_Verb, S0B1POSLemma: Noun_getir, S0B1Token: sorumlulukların__, S0Lemma: sorumluluk, S0POS: Noun, S0Token: sorumlulukların, sorumluluk_isGouvernedBy_yer: true, sorumluluk_isGouvernedBy_yer_POSSESSOR: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

80- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [yerine, _, getirilebilmesi ,.. ]

B0Lemma: yer, B0POS: Noun, B0Token: yerine, B1Lemma: getir, B1POS: Verb, B1Token: _, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

81- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [yerine]   B= [_, getirilebilmesi, , ,.. ]

B0Lemma: getir, B0POS: Verb, B0Token: _, B1Lemma: _, B1POS: Noun, B1Token: getirilebilmesi, S0B0Distance: 1, S0B0Lemma: yer_getir, S0B0LemmaPOS: yer_Verb, S0B0POS: Noun_Verb, S0B0POSLemma: Noun_getir, S0B0Token: yerine__, S0B1Lemma: yer__, S0B1LemmaPOS: yer_Noun, S0B1POS: Noun_Noun, S0B1POSLemma: Noun__, S0B1Token: yerine_getirilebilmesi, S0Lemma: yer, S0POS: Noun, S0Token: yerine, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, yer_isGouvernedBy_getir: true, yer_isGouvernedBy_getir_MODIFIER: true, 

82- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [yerine, _]   B= [getirilebilmesi, ,, herşeyden ,.. ]

B0Lemma: _, B0POS: Noun, B0Token: getirilebilmesi, B1Lemma: ,, B1POS: Punc, B1Token: ,, S0B0Distance: 1, S0B0Lemma: getir__, S0B0LemmaPOS: getir_Noun, S0B0POS: Verb_Noun, S0B0POSLemma: Verb__, S0B0Token: __getirilebilmesi, S0B1Lemma: getir_,, S0B1LemmaPOS: getir_Punc, S0B1POS: Verb_Punc, S0B1POSLemma: Verb_,, S0B1Token: __,, S0Lemma: getir, S0POS: Verb, S0Token: _, S1B0Lemma: yer__, S1B0LemmaPOS: yer_Noun, S1B0POS: Noun_Noun, S1B0POSLemma: Noun__, S1B0Token: yerine_getirilebilmesi, S1Lemma: yer, S1POS: Noun, S1S0Lemma: yer_getir, S1S0LemmaPOS: yer_Verb, S1S0POS: Noun_Verb, S1S0POSLemma: Noun_getir, S1S0Token: yerine__, S1Token: yerine, SyntaxicRelation: -MODIFIER, getir_isGouvernedBy__: true, getir_isGouvernedBy___DERIV: true, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

83- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [yerine]   B= [getirilebilmesi, ,, herşeyden ,.. ]

B0Lemma: _, B0POS: Noun, B0Token: getirilebilmesi, B1Lemma: ,, B1POS: Punc, B1Token: ,, S0B0Distance: 2, S0B0Lemma: yer__, S0B0LemmaPOS: yer_Noun, S0B0POS: Noun_Noun, S0B0POSLemma: Noun__, S0B0Token: yerine_getirilebilmesi, S0B1Lemma: yer_,, S0B1LemmaPOS: yer_Punc, S0B1POS: Noun_Punc, S0B1POSLemma: Noun_,, S0B1Token: yerine_,, S0Lemma: yer, S0POS: Noun, S0Token: yerine, transitionHistoryLength1: 0, transitionHistoryLength2: 00, transitionHistoryLength3: 002, 

84- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [yerine, getirilebilmesi]   B= [,, herşeyden, önce ,.. ]

B0Lemma: ,, B0POS: Punc, B0Token: ,, B1Lemma: herşey, B1POS: Noun, B1Token: herşeyden, S0B0Distance: 1, S0B0Lemma: __,, S0B0LemmaPOS: __Punc, S0B0POS: Noun_Punc, S0B0POSLemma: Noun_,, S0B0Token: getirilebilmesi_,, S0B1Lemma: __herşey, S0B1LemmaPOS: __Noun, S0B1POS: Noun_Noun, S0B1POSLemma: Noun_herşey, S0B1Token: getirilebilmesi_herşeyden, S0Lemma: _, S0POS: Noun, S0Token: getirilebilmesi, S1B0Lemma: yer_,, S1B0LemmaPOS: yer_Punc, S1B0POS: Noun_Punc, S1B0POSLemma: Noun_,, S1B0Token: yerine_,, S1Lemma: yer, S1POS: Noun, S1S0Lemma: yer__, S1S0LemmaPOS: yer_Noun, S1S0POS: Noun_Noun, S1S0POSLemma: Noun__, S1S0Token: yerine_getirilebilmesi, S1Token: yerine, __,_hasRighDep_PUNCTUATION: true, __hasRighDep_PUNCTUATION: true, __isGouvernedBy__: true, __isGouvernedBy___SUBJECT: true, hasRighDep_PUNCTUATION: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 200, 

85- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[yerine, getirilebilmesi]]   B= [,, herşeyden, önce ,.. ]

B0Lemma: ,, B0POS: Punc, B0Token: ,, B1Lemma: herşey, B1POS: Noun, B1Token: herşeyden, S0B0Distance: 1, S0B0Lemma: yer___,, S0B0LemmaPOS: yer___Punc, S0B0POS: Noun_Noun_Punc, S0B0POSLemma: Noun_Noun_,, S0B0Token: yerine_getirilebilmesi_,, S0B1Lemma: yer___herşey, S0B1LemmaPOS: yer___Noun, S0B1POS: Noun_Noun_Noun, S0B1POSLemma: Noun_Noun_herşey, S0B1Token: yerine_getirilebilmesi_herşeyden, S0Lemma: yer__, S0POS: Noun_Noun, S0Token: yerine_getirilebilmesi, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

86- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, herşeyden, önce ,.. ]

B0Lemma: ,, B0POS: Punc, B0Token: ,, B1Lemma: herşey, B1POS: Noun, B1Token: herşeyden, transitionHistoryLength1: 1, transitionHistoryLength2: 10, transitionHistoryLength3: 102, 

87- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [herşeyden, önce, konu ,.. ]

B0Lemma: herşey, B0POS: Noun, B0Token: herşeyden, B1Lemma: önce, B1POS: Postp, B1Token: önce, S0B0Distance: 1, S0B0Lemma: ,_herşey, S0B0LemmaPOS: ,_Noun, S0B0POS: Punc_Noun, S0B0POSLemma: Punc_herşey, S0B0Token: ,_herşeyden, S0B1Lemma: ,_önce, S0B1LemmaPOS: ,_Postp, S0B1POS: Punc_Postp, S0B1POSLemma: Punc_önce, S0B1Token: ,_önce, S0Lemma: ,, S0POS: Punc, S0Token: ,, transitionHistoryLength1: 2, transitionHistoryLength2: 21, transitionHistoryLength3: 210, 

88- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [herşeyden, önce, konu ,.. ]

B0Lemma: herşey, B0POS: Noun, B0Token: herşeyden, B1Lemma: önce, B1POS: Postp, B1Token: önce, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 021, 

89- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [herşeyden]   B= [önce, konu, ve ,.. ]

B0Lemma: önce, B0POS: Postp, B0Token: önce, B1Lemma: konu, B1POS: Noun, B1Token: konu, S0B0Distance: 1, S0B0Lemma: herşey_önce, S0B0LemmaPOS: herşey_Postp, S0B0POS: Noun_Postp, S0B0POSLemma: Noun_önce, S0B0Token: herşeyden_önce, S0B1Lemma: herşey_konu, S0B1LemmaPOS: herşey_Noun, S0B1POS: Noun_Noun, S0B1POSLemma: Noun_konu, S0B1Token: herşeyden_konu, S0Lemma: herşey, S0POS: Noun, S0Token: herşeyden, herşey_isGouvernedBy_önce: true, herşey_isGouvernedBy_önce_ARGUMENT: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

90- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [önce, konu, ve ,.. ]

B0Lemma: önce, B0POS: Postp, B0Token: önce, B1Lemma: konu, B1POS: Noun, B1Token: konu, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

91- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [önce]   B= [konu, ve, alanlarında ,.. ]

B0Lemma: konu, B0POS: Noun, B0Token: konu, B1Lemma: ve, B1POS: Conj, B1Token: ve, S0B0Distance: 1, S0B0Lemma: önce_konu, S0B0LemmaPOS: önce_Noun, S0B0POS: Postp_Noun, S0B0POSLemma: Postp_konu, S0B0Token: önce_konu, S0B1Lemma: önce_ve, S0B1LemmaPOS: önce_Conj, S0B1POS: Postp_Conj, S0B1POSLemma: Postp_ve, S0B1Token: önce_ve, S0Lemma: önce, S0POS: Postp, S0Token: önce, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, önce_isGouvernedBy_uzmanlaş: true, önce_isGouvernedBy_uzmanlaş_MODIFIER: true, 

92- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [konu, ve, alanlarında ,.. ]

B0Lemma: konu, B0POS: Noun, B0Token: konu, B1Lemma: ve, B1POS: Conj, B1Token: ve, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

93- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [konu]   B= [ve, alanlarında, uzmanlaşmış ,.. ]

B0Lemma: ve, B0POS: Conj, B0Token: ve, B1Lemma: alan, B1POS: Noun, B1Token: alanlarında, S0B0Distance: 1, S0B0Lemma: konu_ve, S0B0LemmaPOS: konu_Conj, S0B0POS: Noun_Conj, S0B0POSLemma: Noun_ve, S0B0Token: konu_ve, S0B1Lemma: konu_alan, S0B1LemmaPOS: konu_Noun, S0B1POS: Noun_Noun, S0B1POSLemma: Noun_alan, S0B1Token: konu_alanlarında, S0Lemma: konu, S0POS: Noun, S0Token: konu, hasRighDep_CONJUNCTION: true, konu_hasRighDep_CONJUNCTION: true, konu_isGouvernedBy_alan: true, konu_isGouvernedBy_alan_COORDINATION: true, konu_ve_hasRighDep_CONJUNCTION: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

94- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ve, alanlarında, uzmanlaşmış ,.. ]

B0Lemma: ve, B0POS: Conj, B0Token: ve, B1Lemma: alan, B1POS: Noun, B1Token: alanlarında, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

95- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ve]   B= [alanlarında, uzmanlaşmış, , ,.. ]

B0Lemma: alan, B0POS: Noun, B0Token: alanlarında, B1Lemma: uzmanlaş, B1POS: Verb, B1Token: uzmanlaşmış, S0B0Distance: 1, S0B0Lemma: ve_alan, S0B0LemmaPOS: ve_Noun, S0B0POS: Conj_Noun, S0B0POSLemma: Conj_alan, S0B0Token: ve_alanlarında, S0B1Lemma: ve_uzmanlaş, S0B1LemmaPOS: ve_Verb, S0B1POS: Conj_Verb, S0B1POSLemma: Conj_uzmanlaş, S0B1Token: ve_uzmanlaşmış, S0Lemma: ve, S0POS: Conj, S0Token: ve, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

96- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [alanlarında, uzmanlaşmış, , ,.. ]

B0Lemma: alan, B0POS: Noun, B0Token: alanlarında, B1Lemma: uzmanlaş, B1POS: Verb, B1Token: uzmanlaşmış, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

97- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [alanlarında]   B= [uzmanlaşmış, ,, tecrübe ,.. ]

B0Lemma: uzmanlaş, B0POS: Verb, B0Token: uzmanlaşmış, B1Lemma: ,, B1POS: Punc, B1Token: ,, S0B0Distance: 1, S0B0Lemma: alan_uzmanlaş, S0B0LemmaPOS: alan_Verb, S0B0POS: Noun_Verb, S0B0POSLemma: Noun_uzmanlaş, S0B0Token: alanlarında_uzmanlaşmış, S0B1Lemma: alan_,, S0B1LemmaPOS: alan_Punc, S0B1POS: Noun_Punc, S0B1POSLemma: Noun_,, S0B1Token: alanlarında_,, S0Lemma: alan, S0POS: Noun, S0Token: alanlarında, alan_isGouvernedBy_uzmanlaş: true, alan_isGouvernedBy_uzmanlaş_MODIFIER: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

98- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [uzmanlaşmış, ,, tecrübe ,.. ]

B0Lemma: uzmanlaş, B0POS: Verb, B0Token: uzmanlaşmış, B1Lemma: ,, B1POS: Punc, B1Token: ,, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

99- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [uzmanlaşmış]   B= [,, tecrübe, ve ,.. ]

B0Lemma: ,, B0POS: Punc, B0Token: ,, B1Lemma: tecrübe, B1POS: Noun, B1Token: tecrübe, S0B0Distance: 1, S0B0Lemma: uzmanlaş_,, S0B0LemmaPOS: uzmanlaş_Punc, S0B0POS: Verb_Punc, S0B0POSLemma: Verb_,, S0B0Token: uzmanlaşmış_,, S0B1Lemma: uzmanlaş_tecrübe, S0B1LemmaPOS: uzmanlaş_Noun, S0B1POS: Verb_Noun, S0B1POSLemma: Verb_tecrübe, S0B1Token: uzmanlaşmış_tecrübe, S0Lemma: uzmanlaş, S0POS: Verb, S0Token: uzmanlaşmış, hasRighDep_PUNCTUATION: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, uzmanlaş_,_hasRighDep_PUNCTUATION: true, uzmanlaş_hasRighDep_PUNCTUATION: true, uzmanlaş_isGouvernedBy_kanıtla: true, uzmanlaş_isGouvernedBy_kanıtla_COORDINATION: true, 

100- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, tecrübe, ve ,.. ]

B0Lemma: ,, B0POS: Punc, B0Token: ,, B1Lemma: tecrübe, B1POS: Noun, B1Token: tecrübe, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

101- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [tecrübe, ve, bilgi ,.. ]

B0Lemma: tecrübe, B0POS: Noun, B0Token: tecrübe, B1Lemma: ve, B1POS: Conj, B1Token: ve, S0B0Distance: 1, S0B0Lemma: ,_tecrübe, S0B0LemmaPOS: ,_Noun, S0B0POS: Punc_Noun, S0B0POSLemma: Punc_tecrübe, S0B0Token: ,_tecrübe, S0B1Lemma: ,_ve, S0B1LemmaPOS: ,_Conj, S0B1POS: Punc_Conj, S0B1POSLemma: Punc_ve, S0B1Token: ,_ve, S0Lemma: ,, S0POS: Punc, S0Token: ,, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

102- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [tecrübe, ve, bilgi ,.. ]

B0Lemma: tecrübe, B0POS: Noun, B0Token: tecrübe, B1Lemma: ve, B1POS: Conj, B1Token: ve, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

103- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [tecrübe]   B= [ve, bilgi, birikimine ,.. ]

B0Lemma: ve, B0POS: Conj, B0Token: ve, B1Lemma: bilgi, B1POS: Noun, B1Token: bilgi, S0B0Distance: 1, S0B0Lemma: tecrübe_ve, S0B0LemmaPOS: tecrübe_Conj, S0B0POS: Noun_Conj, S0B0POSLemma: Noun_ve, S0B0Token: tecrübe_ve, S0B1Lemma: tecrübe_bilgi, S0B1LemmaPOS: tecrübe_Noun, S0B1POS: Noun_Noun, S0B1POSLemma: Noun_bilgi, S0B1Token: tecrübe_bilgi, S0Lemma: tecrübe, S0POS: Noun, S0Token: tecrübe, hasRighDep_CONJUNCTION: true, tecrübe_hasRighDep_CONJUNCTION: true, tecrübe_isGouvernedBy_bilgi: true, tecrübe_isGouvernedBy_bilgi_COORDINATION: true, tecrübe_ve_hasRighDep_CONJUNCTION: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

104- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ve, bilgi, birikimine ,.. ]

B0Lemma: ve, B0POS: Conj, B0Token: ve, B1Lemma: bilgi, B1POS: Noun, B1Token: bilgi, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

105- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ve]   B= [bilgi, birikimine, sahip ,.. ]

B0Lemma: bilgi, B0POS: Noun, B0Token: bilgi, B1Lemma: birikim, B1POS: Noun, B1Token: birikimine, S0B0Distance: 1, S0B0Lemma: ve_bilgi, S0B0LemmaPOS: ve_Noun, S0B0POS: Conj_Noun, S0B0POSLemma: Conj_bilgi, S0B0Token: ve_bilgi, S0B1Lemma: ve_birikim, S0B1LemmaPOS: ve_Noun, S0B1POS: Conj_Noun, S0B1POSLemma: Conj_birikim, S0B1Token: ve_birikimine, S0Lemma: ve, S0POS: Conj, S0Token: ve, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

106- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [bilgi, birikimine, sahip ,.. ]

B0Lemma: bilgi, B0POS: Noun, B0Token: bilgi, B1Lemma: birikim, B1POS: Noun, B1Token: birikimine, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

107- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [bilgi]   B= [birikimine, sahip, , ,.. ]

B0Lemma: birikim, B0POS: Noun, B0Token: birikimine, B1Lemma: sahip, B1POS: Noun, B1Token: sahip, S0B0Distance: 1, S0B0Lemma: bilgi_birikim, S0B0LemmaPOS: bilgi_Noun, S0B0POS: Noun_Noun, S0B0POSLemma: Noun_birikim, S0B0Token: bilgi_birikimine, S0B1Lemma: bilgi_sahip, S0B1LemmaPOS: bilgi_Noun, S0B1POS: Noun_Noun, S0B1POSLemma: Noun_sahip, S0B1Token: bilgi_sahip, S0Lemma: bilgi, S0POS: Noun, S0Token: bilgi, bilgi_isGouvernedBy_birikim: true, bilgi_isGouvernedBy_birikim_POSSESSOR: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

108- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [birikimine, sahip, , ,.. ]

B0Lemma: birikim, B0POS: Noun, B0Token: birikimine, B1Lemma: sahip, B1POS: Noun, B1Token: sahip, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

109- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [birikimine]   B= [sahip, ,, ehliyet ,.. ]

B0Lemma: sahip, B0POS: Noun, B0Token: sahip, B1Lemma: ,, B1POS: Punc, B1Token: ,, S0B0Distance: 1, S0B0Lemma: birikim_sahip, S0B0LemmaPOS: birikim_Noun, S0B0POS: Noun_Noun, S0B0POSLemma: Noun_sahip, S0B0Token: birikimine_sahip, S0B1Lemma: birikim_,, S0B1LemmaPOS: birikim_Punc, S0B1POS: Noun_Punc, S0B1POSLemma: Noun_,, S0B1Token: birikimine_,, S0Lemma: birikim, S0POS: Noun, S0Token: birikimine, birikim_isGouvernedBy_kanıtla: true, birikim_isGouvernedBy_kanıtla_MODIFIER: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

110- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [sahip, ,, ehliyet ,.. ]

B0Lemma: sahip, B0POS: Noun, B0Token: sahip, B1Lemma: ,, B1POS: Punc, B1Token: ,, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

111- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [sahip]   B= [,, ehliyet, ve ,.. ]

B0Lemma: ,, B0POS: Punc, B0Token: ,, B1Lemma: ehliyet, B1POS: Noun, B1Token: ehliyet, S0B0Distance: 1, S0B0Lemma: sahip_,, S0B0LemmaPOS: sahip_Punc, S0B0POS: Noun_Punc, S0B0POSLemma: Noun_,, S0B0Token: sahip_,, S0B1Lemma: sahip_ehliyet, S0B1LemmaPOS: sahip_Noun, S0B1POS: Noun_Noun, S0B1POSLemma: Noun_ehliyet, S0B1Token: sahip_ehliyet, S0Lemma: sahip, S0POS: Noun, S0Token: sahip, hasRighDep_PUNCTUATION: true, sahip_,_hasRighDep_PUNCTUATION: true, sahip_hasRighDep_PUNCTUATION: true, sahip_isGouvernedBy_ehliyet: true, sahip_isGouvernedBy_ehliyet_COORDINATION: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

112- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, ehliyet, ve ,.. ]

B0Lemma: ,, B0POS: Punc, B0Token: ,, B1Lemma: ehliyet, B1POS: Noun, B1Token: ehliyet, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

113- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [ehliyet, ve, liyakatını ,.. ]

B0Lemma: ehliyet, B0POS: Noun, B0Token: ehliyet, B1Lemma: ve, B1POS: Conj, B1Token: ve, S0B0Distance: 1, S0B0Lemma: ,_ehliyet, S0B0LemmaPOS: ,_Noun, S0B0POS: Punc_Noun, S0B0POSLemma: Punc_ehliyet, S0B0Token: ,_ehliyet, S0B1Lemma: ,_ve, S0B1LemmaPOS: ,_Conj, S0B1POS: Punc_Conj, S0B1POSLemma: Punc_ve, S0B1Token: ,_ve, S0Lemma: ,, S0POS: Punc, S0Token: ,, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

114- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ehliyet, ve, liyakatını ,.. ]

B0Lemma: ehliyet, B0POS: Noun, B0Token: ehliyet, B1Lemma: ve, B1POS: Conj, B1Token: ve, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

115- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ehliyet]   B= [ve, liyakatını, kanıtlamış ,.. ]

B0Lemma: ve, B0POS: Conj, B0Token: ve, B1Lemma: liyakat, B1POS: Noun, B1Token: liyakatını, S0B0Distance: 1, S0B0Lemma: ehliyet_ve, S0B0LemmaPOS: ehliyet_Conj, S0B0POS: Noun_Conj, S0B0POSLemma: Noun_ve, S0B0Token: ehliyet_ve, S0B1Lemma: ehliyet_liyakat, S0B1LemmaPOS: ehliyet_Noun, S0B1POS: Noun_Noun, S0B1POSLemma: Noun_liyakat, S0B1Token: ehliyet_liyakatını, S0Lemma: ehliyet, S0POS: Noun, S0Token: ehliyet, ehliyet_hasRighDep_CONJUNCTION: true, ehliyet_isGouvernedBy_liyakat: true, ehliyet_isGouvernedBy_liyakat_COORDINATION: true, ehliyet_ve_hasRighDep_CONJUNCTION: true, hasRighDep_CONJUNCTION: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

116- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ve, liyakatını, kanıtlamış ,.. ]

B0Lemma: ve, B0POS: Conj, B0Token: ve, B1Lemma: liyakat, B1POS: Noun, B1Token: liyakatını, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

117- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ve]   B= [liyakatını, kanıtlamış, , ,.. ]

B0Lemma: liyakat, B0POS: Noun, B0Token: liyakatını, B1Lemma: kanıtla, B1POS: Verb, B1Token: kanıtlamış, S0B0Distance: 1, S0B0Lemma: ve_liyakat, S0B0LemmaPOS: ve_Noun, S0B0POS: Conj_Noun, S0B0POSLemma: Conj_liyakat, S0B0Token: ve_liyakatını, S0B1Lemma: ve_kanıtla, S0B1LemmaPOS: ve_Verb, S0B1POS: Conj_Verb, S0B1POSLemma: Conj_kanıtla, S0B1Token: ve_kanıtlamış, S0Lemma: ve, S0POS: Conj, S0Token: ve, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

118- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [liyakatını, kanıtlamış, , ,.. ]

B0Lemma: liyakat, B0POS: Noun, B0Token: liyakatını, B1Lemma: kanıtla, B1POS: Verb, B1Token: kanıtlamış, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

119- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [liyakatını]   B= [kanıtlamış, ,, gelişmiş ,.. ]

B0Lemma: kanıtla, B0POS: Verb, B0Token: kanıtlamış, B1Lemma: ,, B1POS: Punc, B1Token: ,, S0B0Distance: 1, S0B0Lemma: liyakat_kanıtla, S0B0LemmaPOS: liyakat_Verb, S0B0POS: Noun_Verb, S0B0POSLemma: Noun_kanıtla, S0B0Token: liyakatını_kanıtlamış, S0B1Lemma: liyakat_,, S0B1LemmaPOS: liyakat_Punc, S0B1POS: Noun_Punc, S0B1POSLemma: Noun_,, S0B1Token: liyakatını_,, S0Lemma: liyakat, S0POS: Noun, S0Token: liyakatını, liyakat_isGouvernedBy_kanıtla: true, liyakat_isGouvernedBy_kanıtla_OBJECT: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

120- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [kanıtlamış, ,, gelişmiş ,.. ]

B0Lemma: kanıtla, B0POS: Verb, B0Token: kanıtlamış, B1Lemma: ,, B1POS: Punc, B1Token: ,, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

121- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [kanıtlamış]   B= [,, gelişmiş, beyin ,.. ]

B0Lemma: ,, B0POS: Punc, B0Token: ,, B1Lemma: geliş, B1POS: Verb, B1Token: gelişmiş, S0B0Distance: 1, S0B0Lemma: kanıtla_,, S0B0LemmaPOS: kanıtla_Punc, S0B0POS: Verb_Punc, S0B0POSLemma: Verb_,, S0B0Token: kanıtlamış_,, S0B1Lemma: kanıtla_geliş, S0B1LemmaPOS: kanıtla_Verb, S0B1POS: Verb_Verb, S0B1POSLemma: Verb_geliş, S0B1Token: kanıtlamış_gelişmiş, S0Lemma: kanıtla, S0POS: Verb, S0Token: kanıtlamış, hasRighDep_PUNCTUATION: true, kanıtla_,_hasRighDep_PUNCTUATION: true, kanıtla_hasRighDep_PUNCTUATION: true, kanıtla_isGouvernedBy_geliş: true, kanıtla_isGouvernedBy_geliş_COORDINATION: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

122- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, gelişmiş, beyin ,.. ]

B0Lemma: ,, B0POS: Punc, B0Token: ,, B1Lemma: geliş, B1POS: Verb, B1Token: gelişmiş, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

123- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [gelişmiş, beyin, gücü ,.. ]

B0Lemma: geliş, B0POS: Verb, B0Token: gelişmiş, B1Lemma: beyin, B1POS: Noun, B1Token: beyin, S0B0Distance: 1, S0B0Lemma: ,_geliş, S0B0LemmaPOS: ,_Verb, S0B0POS: Punc_Verb, S0B0POSLemma: Punc_geliş, S0B0Token: ,_gelişmiş, S0B1Lemma: ,_beyin, S0B1LemmaPOS: ,_Noun, S0B1POS: Punc_Noun, S0B1POSLemma: Punc_beyin, S0B1Token: ,_beyin, S0Lemma: ,, S0POS: Punc, S0Token: ,, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

124- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [gelişmiş, beyin, gücü ,.. ]

B0Lemma: geliş, B0POS: Verb, B0Token: gelişmiş, B1Lemma: beyin, B1POS: Noun, B1Token: beyin, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

125- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [gelişmiş]   B= [beyin, gücü, ile ,.. ]

B0Lemma: beyin, B0POS: Noun, B0Token: beyin, B1Lemma: güç, B1POS: Noun, B1Token: gücü, S0B0Distance: 1, S0B0Lemma: geliş_beyin, S0B0LemmaPOS: geliş_Noun, S0B0POS: Verb_Noun, S0B0POSLemma: Verb_beyin, S0B0Token: gelişmiş_beyin, S0B1Lemma: geliş_güç, S0B1LemmaPOS: geliş_Noun, S0B1POS: Verb_Noun, S0B1POSLemma: Verb_güç, S0B1Token: gelişmiş_gücü, S0Lemma: geliş, S0POS: Verb, S0Token: gelişmiş, geliş_isGouvernedBy__: true, geliş_isGouvernedBy___MODIFIER: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

126- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [beyin, gücü, ile ,.. ]

B0Lemma: beyin, B0POS: Noun, B0Token: beyin, B1Lemma: güç, B1POS: Noun, B1Token: gücü, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

127- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [beyin]   B= [gücü, ile, bilimsel ,.. ]

B0Lemma: güç, B0POS: Noun, B0Token: gücü, B1Lemma: ile, B1POS: Conj, B1Token: ile, S0B0Distance: 1, S0B0Lemma: beyin_güç, S0B0LemmaPOS: beyin_Noun, S0B0POS: Noun_Noun, S0B0POSLemma: Noun_güç, S0B0Token: beyin_gücü, S0B1Lemma: beyin_ile, S0B1LemmaPOS: beyin_Conj, S0B1POS: Noun_Conj, S0B1POSLemma: Noun_ile, S0B1Token: beyin_ile, S0Lemma: beyin, S0POS: Noun, S0Token: beyin, beyin_isGouvernedBy_güç: true, beyin_isGouvernedBy_güç_POSSESSOR: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

128- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [gücü, ile, bilimsel ,.. ]

B0Lemma: güç, B0POS: Noun, B0Token: gücü, B1Lemma: ile, B1POS: Conj, B1Token: ile, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

129- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [gücü]   B= [ile, bilimsel, _ ,.. ]

B0Lemma: ile, B0POS: Conj, B0Token: ile, B1Lemma: bilimsel, B1POS: Adj, B1Token: bilimsel, S0B0Distance: 1, S0B0Lemma: güç_ile, S0B0LemmaPOS: güç_Conj, S0B0POS: Noun_Conj, S0B0POSLemma: Noun_ile, S0B0Token: gücü_ile, S0B1Lemma: güç_bilimsel, S0B1LemmaPOS: güç_Adj, S0B1POS: Noun_Adj, S0B1POSLemma: Noun_bilimsel, S0B1Token: gücü_bilimsel, S0Lemma: güç, S0POS: Noun, S0Token: gücü, güç_hasRighDep_CONJUNCTION: true, güç_ile_hasRighDep_CONJUNCTION: true, güç_isGouvernedBy__: true, güç_isGouvernedBy___SUBJECT: true, hasRighDep_CONJUNCTION: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

130- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ile, bilimsel, _ ,.. ]

B0Lemma: ile, B0POS: Conj, B0Token: ile, B1Lemma: bilimsel, B1POS: Adj, B1Token: bilimsel, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

131- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ile]   B= [bilimsel, _, araştırma ,.. ]

B0Lemma: bilimsel, B0POS: Adj, B0Token: bilimsel, B1Lemma: araştır, B1POS: Verb, B1Token: _, S0B0Distance: 1, S0B0Lemma: ile_bilimsel, S0B0LemmaPOS: ile_Adj, S0B0POS: Conj_Adj, S0B0POSLemma: Conj_bilimsel, S0B0Token: ile_bilimsel, S0B1Lemma: ile_araştır, S0B1LemmaPOS: ile_Verb, S0B1POS: Conj_Verb, S0B1POSLemma: Conj_araştır, S0B1Token: ile__, S0Lemma: ile, S0POS: Conj, S0Token: ile, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

132- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [bilimsel, _, araştırma ,.. ]

B0Lemma: bilimsel, B0POS: Adj, B0Token: bilimsel, B1Lemma: araştır, B1POS: Verb, B1Token: _, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

133- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [bilimsel]   B= [_, araştırma, yetenekleri ,.. ]

B0Lemma: araştır, B0POS: Verb, B0Token: _, B1Lemma: _, B1POS: Noun, B1Token: araştırma, S0B0Distance: 1, S0B0Lemma: bilimsel_araştır, S0B0LemmaPOS: bilimsel_Verb, S0B0POS: Adj_Verb, S0B0POSLemma: Adj_araştır, S0B0Token: bilimsel__, S0B1Lemma: bilimsel__, S0B1LemmaPOS: bilimsel_Noun, S0B1POS: Adj_Noun, S0B1POSLemma: Adj__, S0B1Token: bilimsel_araştırma, S0Lemma: bilimsel, S0POS: Adj, S0Token: bilimsel, bilimsel_isGouvernedBy__: true, bilimsel_isGouvernedBy___MWE: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

134- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [_, araştırma, yetenekleri ,.. ]

B0Lemma: araştır, B0POS: Verb, B0Token: _, B1Lemma: _, B1POS: Noun, B1Token: araştırma, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

135- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [_]   B= [araştırma, yetenekleri, kazandırılmış ,.. ]

B0Lemma: _, B0POS: Noun, B0Token: araştırma, B1Lemma: yetenek, B1POS: Noun, B1Token: yetenekleri, S0B0Distance: 1, S0B0Lemma: araştır__, S0B0LemmaPOS: araştır_Noun, S0B0POS: Verb_Noun, S0B0POSLemma: Verb__, S0B0Token: __araştırma, S0B1Lemma: araştır_yetenek, S0B1LemmaPOS: araştır_Noun, S0B1POS: Verb_Noun, S0B1POSLemma: Verb_yetenek, S0B1Token: __yetenekleri, S0Lemma: araştır, S0POS: Verb, S0Token: _, araştır_isGouvernedBy__: true, araştır_isGouvernedBy___DERIV: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

136- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [araştırma, yetenekleri, kazandırılmış ,.. ]

B0Lemma: _, B0POS: Noun, B0Token: araştırma, B1Lemma: yetenek, B1POS: Noun, B1Token: yetenekleri, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

137- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [araştırma]   B= [yetenekleri, kazandırılmış, , ,.. ]

B0Lemma: yetenek, B0POS: Noun, B0Token: yetenekleri, B1Lemma: kazan, B1POS: Verb, B1Token: kazandırılmış, S0B0Distance: 1, S0B0Lemma: __yetenek, S0B0LemmaPOS: __Noun, S0B0POS: Noun_Noun, S0B0POSLemma: Noun_yetenek, S0B0Token: araştırma_yetenekleri, S0B1Lemma: __kazan, S0B1LemmaPOS: __Verb, S0B1POS: Noun_Verb, S0B1POSLemma: Noun_kazan, S0B1Token: araştırma_kazandırılmış, S0Lemma: _, S0POS: Noun, S0Token: araştırma, __isGouvernedBy_yetenek: true, __isGouvernedBy_yetenek_MWE: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

138- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [yetenekleri, kazandırılmış, , ,.. ]

B0Lemma: yetenek, B0POS: Noun, B0Token: yetenekleri, B1Lemma: kazan, B1POS: Verb, B1Token: kazandırılmış, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

139- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [yetenekleri]   B= [kazandırılmış, ,, fikir ,.. ]

B0Lemma: kazan, B0POS: Verb, B0Token: kazandırılmış, B1Lemma: ,, B1POS: Punc, B1Token: ,, S0B0Distance: 1, S0B0Lemma: yetenek_kazan, S0B0LemmaPOS: yetenek_Verb, S0B0POS: Noun_Verb, S0B0POSLemma: Noun_kazan, S0B0Token: yetenekleri_kazandırılmış, S0B1Lemma: yetenek_,, S0B1LemmaPOS: yetenek_Punc, S0B1POS: Noun_Punc, S0B1POSLemma: Noun_,, S0B1Token: yetenekleri_,, S0Lemma: yetenek, S0POS: Noun, S0Token: yetenekleri, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, yetenek_isGouvernedBy_kazan: true, yetenek_isGouvernedBy_kazan_OBJECT: true, 

140- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [kazandırılmış, ,, fikir ,.. ]

B0Lemma: kazan, B0POS: Verb, B0Token: kazandırılmış, B1Lemma: ,, B1POS: Punc, B1Token: ,, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

141- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [kazandırılmış]   B= [,, fikir, üretebilecek ,.. ]

B0Lemma: ,, B0POS: Punc, B0Token: ,, B1Lemma: fikir, B1POS: Noun, B1Token: fikir, S0B0Distance: 1, S0B0Lemma: kazan_,, S0B0LemmaPOS: kazan_Punc, S0B0POS: Verb_Punc, S0B0POSLemma: Verb_,, S0B0Token: kazandırılmış_,, S0B1Lemma: kazan_fikir, S0B1LemmaPOS: kazan_Noun, S0B1POS: Verb_Noun, S0B1POSLemma: Verb_fikir, S0B1Token: kazandırılmış_fikir, S0Lemma: kazan, S0POS: Verb, S0Token: kazandırılmış, hasRighDep_PUNCTUATION: true, kazan_,_hasRighDep_PUNCTUATION: true, kazan_hasRighDep_PUNCTUATION: true, kazan_isGouvernedBy_yetiş: true, kazan_isGouvernedBy_yetiş_COORDINATION: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

142- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, fikir, üretebilecek ,.. ]

B0Lemma: ,, B0POS: Punc, B0Token: ,, B1Lemma: fikir, B1POS: Noun, B1Token: fikir, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

143- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [fikir, üretebilecek, şekilde ,.. ]

B0Lemma: fikir, B0POS: Noun, B0Token: fikir, B1Lemma: üre, B1POS: Verb, B1Token: üretebilecek, S0B0Distance: 1, S0B0Lemma: ,_fikir, S0B0LemmaPOS: ,_Noun, S0B0POS: Punc_Noun, S0B0POSLemma: Punc_fikir, S0B0Token: ,_fikir, S0B1Lemma: ,_üre, S0B1LemmaPOS: ,_Verb, S0B1POS: Punc_Verb, S0B1POSLemma: Punc_üre, S0B1Token: ,_üretebilecek, S0Lemma: ,, S0POS: Punc, S0Token: ,, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

144- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [fikir, üretebilecek, şekilde ,.. ]

B0Lemma: fikir, B0POS: Noun, B0Token: fikir, B1Lemma: üre, B1POS: Verb, B1Token: üretebilecek, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

145- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [fikir]   B= [üretebilecek, şekilde, yetiştirilmiş ,.. ]

B0Lemma: üre, B0POS: Verb, B0Token: üretebilecek, B1Lemma: şekil, B1POS: Noun, B1Token: şekilde, S0B0Distance: 1, S0B0Lemma: fikir_üre, S0B0LemmaPOS: fikir_Verb, S0B0POS: Noun_Verb, S0B0POSLemma: Noun_üre, S0B0Token: fikir_üretebilecek, S0B1Lemma: fikir_şekil, S0B1LemmaPOS: fikir_Noun, S0B1POS: Noun_Noun, S0B1POSLemma: Noun_şekil, S0B1Token: fikir_şekilde, S0Lemma: fikir, S0POS: Noun, S0Token: fikir, fikir_isGouvernedBy_üre: true, fikir_isGouvernedBy_üre_OBJECT: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

146- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [üretebilecek, şekilde, yetiştirilmiş ,.. ]

B0Lemma: üre, B0POS: Verb, B0Token: üretebilecek, B1Lemma: şekil, B1POS: Noun, B1Token: şekilde, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

147- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [üretebilecek]   B= [şekilde, yetiştirilmiş, ve ,.. ]

B0Lemma: şekil, B0POS: Noun, B0Token: şekilde, B1Lemma: yetiş, B1POS: Verb, B1Token: yetiştirilmiş, S0B0Distance: 1, S0B0Lemma: üre_şekil, S0B0LemmaPOS: üre_Noun, S0B0POS: Verb_Noun, S0B0POSLemma: Verb_şekil, S0B0Token: üretebilecek_şekilde, S0B1Lemma: üre_yetiş, S0B1LemmaPOS: üre_Verb, S0B1POS: Verb_Verb, S0B1POSLemma: Verb_yetiş, S0B1Token: üretebilecek_yetiştirilmiş, S0Lemma: üre, S0POS: Verb, S0Token: üretebilecek, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, üre_isGouvernedBy_yetiş: true, üre_isGouvernedBy_yetiş_COORDINATION: true, 

148- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [şekilde, yetiştirilmiş, ve ,.. ]

B0Lemma: şekil, B0POS: Noun, B0Token: şekilde, B1Lemma: yetiş, B1POS: Verb, B1Token: yetiştirilmiş, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

149- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [şekilde]   B= [yetiştirilmiş, ve, devamlı ,.. ]

B0Lemma: yetiş, B0POS: Verb, B0Token: yetiştirilmiş, B1Lemma: ve, B1POS: Conj, B1Token: ve, S0B0Distance: 1, S0B0Lemma: şekil_yetiş, S0B0LemmaPOS: şekil_Verb, S0B0POS: Noun_Verb, S0B0POSLemma: Noun_yetiş, S0B0Token: şekilde_yetiştirilmiş, S0B1Lemma: şekil_ve, S0B1LemmaPOS: şekil_Conj, S0B1POS: Noun_Conj, S0B1POSLemma: Noun_ve, S0B1Token: şekilde_ve, S0Lemma: şekil, S0POS: Noun, S0Token: şekilde, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, şekil_isGouvernedBy_yetiş: true, şekil_isGouvernedBy_yetiş_MODIFIER: true, 

150- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [yetiştirilmiş, ve, devamlı ,.. ]

B0Lemma: yetiş, B0POS: Verb, B0Token: yetiştirilmiş, B1Lemma: ve, B1POS: Conj, B1Token: ve, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

151- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [yetiştirilmiş]   B= [ve, devamlı, olarak ,.. ]

B0Lemma: ve, B0POS: Conj, B0Token: ve, B1Lemma: devamlı, B1POS: Adj, B1Token: devamlı, S0B0Distance: 1, S0B0Lemma: yetiş_ve, S0B0LemmaPOS: yetiş_Conj, S0B0POS: Verb_Conj, S0B0POSLemma: Verb_ve, S0B0Token: yetiştirilmiş_ve, S0B1Lemma: yetiş_devamlı, S0B1LemmaPOS: yetiş_Adj, S0B1POS: Verb_Adj, S0B1POSLemma: Verb_devamlı, S0B1Token: yetiştirilmiş_devamlı, S0Lemma: yetiş, S0POS: Verb, S0Token: yetiştirilmiş, hasRighDep_CONJUNCTION: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, yetiş_hasRighDep_CONJUNCTION: true, yetiş_isGouvernedBy__: true, yetiş_isGouvernedBy___COORDINATION: true, yetiş_ve_hasRighDep_CONJUNCTION: true, 

152- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ve, devamlı, olarak ,.. ]

B0Lemma: ve, B0POS: Conj, B0Token: ve, B1Lemma: devamlı, B1POS: Adj, B1Token: devamlı, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

153- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ve]   B= [devamlı, olarak, _ ,.. ]

B0Lemma: devamlı, B0POS: Adj, B0Token: devamlı, B1Lemma: olarak, B1POS: Postp, B1Token: olarak, S0B0Distance: 1, S0B0Lemma: ve_devamlı, S0B0LemmaPOS: ve_Adj, S0B0POS: Conj_Adj, S0B0POSLemma: Conj_devamlı, S0B0Token: ve_devamlı, S0B1Lemma: ve_olarak, S0B1LemmaPOS: ve_Postp, S0B1POS: Conj_Postp, S0B1POSLemma: Conj_olarak, S0B1Token: ve_olarak, S0Lemma: ve, S0POS: Conj, S0Token: ve, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

154- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [devamlı, olarak, _ ,.. ]

B0Lemma: devamlı, B0POS: Adj, B0Token: devamlı, B1Lemma: olarak, B1POS: Postp, B1Token: olarak, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

155- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [devamlı]   B= [olarak, _, çalışmalarına ,.. ]

B0Lemma: olarak, B0POS: Postp, B0Token: olarak, B1Lemma: çalış, B1POS: Verb, B1Token: _, S0B0Distance: 1, S0B0Lemma: devamlı_olarak, S0B0LemmaPOS: devamlı_Postp, S0B0POS: Adj_Postp, S0B0POSLemma: Adj_olarak, S0B0Token: devamlı_olarak, S0B1Lemma: devamlı_çalış, S0B1LemmaPOS: devamlı_Verb, S0B1POS: Adj_Verb, S0B1POSLemma: Adj_çalış, S0B1Token: devamlı__, S0Lemma: devamlı, S0POS: Adj, S0Token: devamlı, devamlı_isGouvernedBy_olarak: true, devamlı_isGouvernedBy_olarak_ARGUMENT: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

156- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [olarak, _, çalışmalarına ,.. ]

B0Lemma: olarak, B0POS: Postp, B0Token: olarak, B1Lemma: çalış, B1POS: Verb, B1Token: _, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

157- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [olarak]   B= [_, çalışmalarına, imkan ,.. ]

B0Lemma: çalış, B0POS: Verb, B0Token: _, B1Lemma: _, B1POS: Noun, B1Token: çalışmalarına, S0B0Distance: 1, S0B0Lemma: olarak_çalış, S0B0LemmaPOS: olarak_Verb, S0B0POS: Postp_Verb, S0B0POSLemma: Postp_çalış, S0B0Token: olarak__, S0B1Lemma: olarak__, S0B1LemmaPOS: olarak_Noun, S0B1POS: Postp_Noun, S0B1POSLemma: Postp__, S0B1Token: olarak_çalışmalarına, S0Lemma: olarak, S0POS: Postp, S0Token: olarak, olarak_isGouvernedBy_çalış: true, olarak_isGouvernedBy_çalış_MODIFIER: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

158- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [_, çalışmalarına, imkan ,.. ]

B0Lemma: çalış, B0POS: Verb, B0Token: _, B1Lemma: _, B1POS: Noun, B1Token: çalışmalarına, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

159- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [_]   B= [çalışmalarına, imkan, _ ,.. ]

B0Lemma: _, B0POS: Noun, B0Token: çalışmalarına, B1Lemma: imkan, B1POS: Noun, B1Token: imkan, S0B0Distance: 1, S0B0Lemma: çalış__, S0B0LemmaPOS: çalış_Noun, S0B0POS: Verb_Noun, S0B0POSLemma: Verb__, S0B0Token: __çalışmalarına, S0B1Lemma: çalış_imkan, S0B1LemmaPOS: çalış_Noun, S0B1POS: Verb_Noun, S0B1POSLemma: Verb_imkan, S0B1Token: __imkan, S0Lemma: çalış, S0POS: Verb, S0Token: _, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, çalış_isGouvernedBy__: true, çalış_isGouvernedBy___DERIV: true, 

160- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [çalışmalarına, imkan, _ ,.. ]

B0Lemma: _, B0POS: Noun, B0Token: çalışmalarına, B1Lemma: imkan, B1POS: Noun, B1Token: imkan, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

161- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [çalışmalarına]   B= [imkan, _, sağlanan ,.. ]

B0Lemma: imkan, B0POS: Noun, B0Token: imkan, B1Lemma: sağla, B1POS: Verb, B1Token: _, S0B0Distance: 1, S0B0Lemma: __imkan, S0B0LemmaPOS: __Noun, S0B0POS: Noun_Noun, S0B0POSLemma: Noun_imkan, S0B0Token: çalışmalarına_imkan, S0B1Lemma: __sağla, S0B1LemmaPOS: __Verb, S0B1POS: Noun_Verb, S0B1POSLemma: Noun_sağla, S0B1Token: çalışmalarına__, S0Lemma: _, S0POS: Noun, S0Token: çalışmalarına, __isGouvernedBy_sağla: true, __isGouvernedBy_sağla_MODIFIER: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

162- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [imkan, _, sağlanan ,.. ]

B0Lemma: imkan, B0POS: Noun, B0Token: imkan, B1Lemma: sağla, B1POS: Verb, B1Token: _, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

163- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [imkan]   B= [_, sağlanan, genç ,.. ]

B0Lemma: sağla, B0POS: Verb, B0Token: _, B1Lemma: _, B1POS: Adj, B1Token: sağlanan, S0B0Distance: 1, S0B0Lemma: imkan_sağla, S0B0LemmaPOS: imkan_Verb, S0B0POS: Noun_Verb, S0B0POSLemma: Noun_sağla, S0B0Token: imkan__, S0B1Lemma: imkan__, S0B1LemmaPOS: imkan_Adj, S0B1POS: Noun_Adj, S0B1POSLemma: Noun__, S0B1Token: imkan_sağlanan, S0Lemma: imkan, S0POS: Noun, S0Token: imkan, imkan_isGouvernedBy_sağla: true, imkan_isGouvernedBy_sağla_MWE: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

164- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [_, sağlanan, genç ,.. ]

B0Lemma: sağla, B0POS: Verb, B0Token: _, B1Lemma: _, B1POS: Adj, B1Token: sağlanan, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

165- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [_]   B= [sağlanan, genç, uzman ,.. ]

B0Lemma: _, B0POS: Adj, B0Token: sağlanan, B1Lemma: genç, B1POS: Adj, B1Token: genç, S0B0Distance: 1, S0B0Lemma: sağla__, S0B0LemmaPOS: sağla_Adj, S0B0POS: Verb_Adj, S0B0POSLemma: Verb__, S0B0Token: __sağlanan, S0B1Lemma: sağla_genç, S0B1LemmaPOS: sağla_Adj, S0B1POS: Verb_Adj, S0B1POSLemma: Verb_genç, S0B1Token: __genç, S0Lemma: sağla, S0POS: Verb, S0Token: _, sağla_isGouvernedBy__: true, sağla_isGouvernedBy___DERIV: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

166- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [sağlanan, genç, uzman ,.. ]

B0Lemma: _, B0POS: Adj, B0Token: sağlanan, B1Lemma: genç, B1POS: Adj, B1Token: genç, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

167- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [sağlanan]   B= [genç, uzman, ve ,.. ]

B0Lemma: genç, B0POS: Adj, B0Token: genç, B1Lemma: uzman, B1POS: Adj, B1Token: uzman, S0B0Distance: 1, S0B0Lemma: __genç, S0B0LemmaPOS: __Adj, S0B0POS: Adj_Adj, S0B0POSLemma: Adj_genç, S0B0Token: sağlanan_genç, S0B1Lemma: __uzman, S0B1LemmaPOS: __Adj, S0B1POS: Adj_Adj, S0B1POSLemma: Adj_uzman, S0B1Token: sağlanan_uzman, S0Lemma: _, S0POS: Adj, S0Token: sağlanan, __isGouvernedBy_düzey: true, __isGouvernedBy_düzey_MODIFIER: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

168- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [genç, uzman, ve ,.. ]

B0Lemma: genç, B0POS: Adj, B0Token: genç, B1Lemma: uzman, B1POS: Adj, B1Token: uzman, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

169- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [genç]   B= [uzman, ve, uzman ,.. ]

B0Lemma: uzman, B0POS: Adj, B0Token: uzman, B1Lemma: ve, B1POS: Conj, B1Token: ve, S0B0Distance: 1, S0B0Lemma: genç_uzman, S0B0LemmaPOS: genç_Adj, S0B0POS: Adj_Adj, S0B0POSLemma: Adj_uzman, S0B0Token: genç_uzman, S0B1Lemma: genç_ve, S0B1LemmaPOS: genç_Conj, S0B1POS: Adj_Conj, S0B1POSLemma: Adj_ve, S0B1Token: genç_ve, S0Lemma: genç, S0POS: Adj, S0Token: genç, genç_isGouvernedBy_düzey: true, genç_isGouvernedBy_düzey_MODIFIER: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

170- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [uzman, ve, uzman ,.. ]

B0Lemma: uzman, B0POS: Adj, B0Token: uzman, B1Lemma: ve, B1POS: Conj, B1Token: ve, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

171- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [uzman]   B= [ve, uzman, yardımcısı ,.. ]

B0Lemma: ve, B0POS: Conj, B0Token: ve, B1Lemma: uzman, B1POS: Adj, B1Token: uzman, S0B0Distance: 1, S0B0Lemma: uzman_ve, S0B0LemmaPOS: uzman_Conj, S0B0POS: Adj_Conj, S0B0POSLemma: Adj_ve, S0B0Token: uzman_ve, S0B1Lemma: uzman_uzman, S0B1LemmaPOS: uzman_Adj, S0B1POS: Adj_Adj, S0B1POSLemma: Adj_uzman, S0B1Token: uzman_uzman, S0Lemma: uzman, S0POS: Adj, S0Token: uzman, hasRighDep_CONJUNCTION: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, uzman_hasRighDep_CONJUNCTION: true, uzman_isGouvernedBy_uzman: true, uzman_isGouvernedBy_uzman_COORDINATION: true, uzman_ve_hasRighDep_CONJUNCTION: true, 

172- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ve, uzman, yardımcısı ,.. ]

B0Lemma: ve, B0POS: Conj, B0Token: ve, B1Lemma: uzman, B1POS: Adj, B1Token: uzman, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

173- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ve]   B= [uzman, yardımcısı, düzeyinde ,.. ]

B0Lemma: uzman, B0POS: Adj, B0Token: uzman, B1Lemma: yardımcı, B1POS: Noun, B1Token: yardımcısı, S0B0Distance: 1, S0B0Lemma: ve_uzman, S0B0LemmaPOS: ve_Adj, S0B0POS: Conj_Adj, S0B0POSLemma: Conj_uzman, S0B0Token: ve_uzman, S0B1Lemma: ve_yardımcı, S0B1LemmaPOS: ve_Noun, S0B1POS: Conj_Noun, S0B1POSLemma: Conj_yardımcı, S0B1Token: ve_yardımcısı, S0Lemma: ve, S0POS: Conj, S0Token: ve, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

174- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [uzman, yardımcısı, düzeyinde ,.. ]

B0Lemma: uzman, B0POS: Adj, B0Token: uzman, B1Lemma: yardımcı, B1POS: Noun, B1Token: yardımcısı, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

175- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [uzman]   B= [yardımcısı, düzeyinde, personelin ,.. ]

B0Lemma: yardımcı, B0POS: Noun, B0Token: yardımcısı, B1Lemma: düzey, B1POS: Noun, B1Token: düzeyinde, S0B0Distance: 1, S0B0Lemma: uzman_yardımcı, S0B0LemmaPOS: uzman_Noun, S0B0POS: Adj_Noun, S0B0POSLemma: Adj_yardımcı, S0B0Token: uzman_yardımcısı, S0B1Lemma: uzman_düzey, S0B1LemmaPOS: uzman_Noun, S0B1POS: Adj_Noun, S0B1POSLemma: Adj_düzey, S0B1Token: uzman_düzeyinde, S0Lemma: uzman, S0POS: Adj, S0Token: uzman, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, uzman_isGouvernedBy_yardımcı: true, uzman_isGouvernedBy_yardımcı_MODIFIER: true, 

176- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [yardımcısı, düzeyinde, personelin ,.. ]

B0Lemma: yardımcı, B0POS: Noun, B0Token: yardımcısı, B1Lemma: düzey, B1POS: Noun, B1Token: düzeyinde, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

177- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [yardımcısı]   B= [düzeyinde, personelin, istihdamı ,.. ]

B0Lemma: düzey, B0POS: Noun, B0Token: düzeyinde, B1Lemma: personel, B1POS: Noun, B1Token: personelin, S0B0Distance: 1, S0B0Lemma: yardımcı_düzey, S0B0LemmaPOS: yardımcı_Noun, S0B0POS: Noun_Noun, S0B0POSLemma: Noun_düzey, S0B0Token: yardımcısı_düzeyinde, S0B1Lemma: yardımcı_personel, S0B1LemmaPOS: yardımcı_Noun, S0B1POS: Noun_Noun, S0B1POSLemma: Noun_personel, S0B1Token: yardımcısı_personelin, S0Lemma: yardımcı, S0POS: Noun, S0Token: yardımcısı, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, yardımcı_isGouvernedBy_düzey: true, yardımcı_isGouvernedBy_düzey_POSSESSOR: true, 

178- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [düzeyinde, personelin, istihdamı ,.. ]

B0Lemma: düzey, B0POS: Noun, B0Token: düzeyinde, B1Lemma: personel, B1POS: Noun, B1Token: personelin, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

179- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [düzeyinde]   B= [personelin, istihdamı, ile ,.. ]

B0Lemma: personel, B0POS: Noun, B0Token: personelin, B1Lemma: istihdam, B1POS: Noun, B1Token: istihdamı, S0B0Distance: 1, S0B0Lemma: düzey_personel, S0B0LemmaPOS: düzey_Noun, S0B0POS: Noun_Noun, S0B0POSLemma: Noun_personel, S0B0Token: düzeyinde_personelin, S0B1Lemma: düzey_istihdam, S0B1LemmaPOS: düzey_Noun, S0B1POS: Noun_Noun, S0B1POSLemma: Noun_istihdam, S0B1Token: düzeyinde_istihdamı, S0Lemma: düzey, S0POS: Noun, S0Token: düzeyinde, düzey_isGouvernedBy__: true, düzey_isGouvernedBy___MODIFIER: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

180- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [personelin, istihdamı, ile ,.. ]

B0Lemma: personel, B0POS: Noun, B0Token: personelin, B1Lemma: istihdam, B1POS: Noun, B1Token: istihdamı, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

181- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [personelin]   B= [istihdamı, ile, _ ,.. ]

B0Lemma: istihdam, B0POS: Noun, B0Token: istihdamı, B1Lemma: ile, B1POS: Conj, B1Token: ile, S0B0Distance: 1, S0B0Lemma: personel_istihdam, S0B0LemmaPOS: personel_Noun, S0B0POS: Noun_Noun, S0B0POSLemma: Noun_istihdam, S0B0Token: personelin_istihdamı, S0B1Lemma: personel_ile, S0B1LemmaPOS: personel_Conj, S0B1POS: Noun_Conj, S0B1POSLemma: Noun_ile, S0B1Token: personelin_ile, S0Lemma: personel, S0POS: Noun, S0Token: personelin, personel_isGouvernedBy_istihdam: true, personel_isGouvernedBy_istihdam_POSSESSOR: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

182- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [istihdamı, ile, _ ,.. ]

B0Lemma: istihdam, B0POS: Noun, B0Token: istihdamı, B1Lemma: ile, B1POS: Conj, B1Token: ile, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

183- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [istihdamı]   B= [ile, _, mümkündür ,.. ]

B0Lemma: ile, B0POS: Conj, B0Token: ile, B1Lemma: mümkün, B1POS: Noun, B1Token: _, S0B0Distance: 1, S0B0Lemma: istihdam_ile, S0B0LemmaPOS: istihdam_Conj, S0B0POS: Noun_Conj, S0B0POSLemma: Noun_ile, S0B0Token: istihdamı_ile, S0B1Lemma: istihdam_mümkün, S0B1LemmaPOS: istihdam_Noun, S0B1POS: Noun_Noun, S0B1POSLemma: Noun_mümkün, S0B1Token: istihdamı__, S0Lemma: istihdam, S0POS: Noun, S0Token: istihdamı, istihdam_isGouvernedBy_ile: true, istihdam_isGouvernedBy_ile_ARGUMENT: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

184- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ile, _, mümkündür ,.. ]

B0Lemma: ile, B0POS: Conj, B0Token: ile, B1Lemma: mümkün, B1POS: Noun, B1Token: _, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

185- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ile]   B= [_, mümkündür, " ,.. ]

B0Lemma: mümkün, B0POS: Noun, B0Token: _, B1Lemma: _, B1POS: Verb, B1Token: mümkündür, S0B0Distance: 1, S0B0Lemma: ile_mümkün, S0B0LemmaPOS: ile_Noun, S0B0POS: Conj_Noun, S0B0POSLemma: Conj_mümkün, S0B0Token: ile__, S0B1Lemma: ile__, S0B1LemmaPOS: ile_Verb, S0B1POS: Conj_Verb, S0B1POSLemma: Conj__, S0B1Token: ile_mümkündür, S0Lemma: ile, S0POS: Conj, S0Token: ile, ile_isGouvernedBy__: true, ile_isGouvernedBy___MODIFIER: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

186- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [_, mümkündür, " ,.. ]

B0Lemma: mümkün, B0POS: Noun, B0Token: _, B1Lemma: _, B1POS: Verb, B1Token: mümkündür, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

187- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [_]   B= [mümkündür, ", görüşüne ,.. ]

B0Lemma: _, B0POS: Verb, B0Token: mümkündür, B1Lemma: ", B1POS: Punc, B1Token: ", S0B0Distance: 1, S0B0Lemma: mümkün__, S0B0LemmaPOS: mümkün_Verb, S0B0POS: Noun_Verb, S0B0POSLemma: Noun__, S0B0Token: __mümkündür, S0B1Lemma: mümkün_", S0B1LemmaPOS: mümkün_Punc, S0B1POS: Noun_Punc, S0B1POSLemma: Noun_", S0B1Token: __", S0Lemma: mümkün, S0POS: Noun, S0Token: _, mümkün_isGouvernedBy__: true, mümkün_isGouvernedBy___DERIV: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

188- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [mümkündür, ", görüşüne ,.. ]

B0Lemma: _, B0POS: Verb, B0Token: mümkündür, B1Lemma: ", B1POS: Punc, B1Token: ", transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

189- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [mümkündür]   B= [", görüşüne, yer ,.. ]

B0Lemma: ", B0POS: Punc, B0Token: ", B1Lemma: görüş, B1POS: Noun, B1Token: görüşüne, S0B0Distance: 1, S0B0Lemma: __", S0B0LemmaPOS: __Punc, S0B0POS: Verb_Punc, S0B0POSLemma: Verb_", S0B0Token: mümkündür_", S0B1Lemma: __görüş, S0B1LemmaPOS: __Noun, S0B1POS: Verb_Noun, S0B1POSLemma: Verb_görüş, S0B1Token: mümkündür_görüşüne, S0Lemma: _, S0POS: Verb, S0Token: mümkündür, __"_hasRighDep_PUNCTUATION: true, __hasRighDep_PUNCTUATION: true, __isGouvernedBy_görüş: true, __isGouvernedBy_görüş_POSSESSOR: true, hasRighDep_PUNCTUATION: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

190- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [", görüşüne, yer ,.. ]

B0Lemma: ", B0POS: Punc, B0Token: ", B1Lemma: görüş, B1POS: Noun, B1Token: görüşüne, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

191- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= ["]   B= [görüşüne, yer, verildi ,.. ]

B0Lemma: görüş, B0POS: Noun, B0Token: görüşüne, B1Lemma: yer, B1POS: Noun, B1Token: yer, S0B0Distance: 1, S0B0Lemma: "_görüş, S0B0LemmaPOS: "_Noun, S0B0POS: Punc_Noun, S0B0POSLemma: Punc_görüş, S0B0Token: "_görüşüne, S0B1Lemma: "_yer, S0B1LemmaPOS: "_Noun, S0B1POS: Punc_Noun, S0B1POSLemma: Punc_yer, S0B1Token: "_yer, S0Lemma: ", S0POS: Punc, S0Token: ", transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

192- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [görüşüne, yer, verildi ,.. ]

B0Lemma: görüş, B0POS: Noun, B0Token: görüşüne, B1Lemma: yer, B1POS: Noun, B1Token: yer, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

193- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [görüşüne]   B= [yer, verildi, . ,.. ]

B0Lemma: yer, B0POS: Noun, B0Token: yer, B1Lemma: ver, B1POS: Verb, B1Token: verildi, S0B0Distance: 1, S0B0Lemma: görüş_yer, S0B0LemmaPOS: görüş_Noun, S0B0POS: Noun_Noun, S0B0POSLemma: Noun_yer, S0B0Token: görüşüne_yer, S0B1Lemma: görüş_ver, S0B1LemmaPOS: görüş_Verb, S0B1POS: Noun_Verb, S0B1POSLemma: Noun_ver, S0B1Token: görüşüne_verildi, S0Lemma: görüş, S0POS: Noun, S0Token: görüşüne, görüş_isGouvernedBy_ver: true, görüş_isGouvernedBy_ver_MODIFIER: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

194- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [yer, verildi, . ,.. ]

B0Lemma: yer, B0POS: Noun, B0Token: yer, B1Lemma: ver, B1POS: Verb, B1Token: verildi, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

195- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [yer]   B= [verildi, . ,.. ]

B0Lemma: ver, B0POS: Verb, B0Token: verildi, B1Lemma: ., B1POS: Punc, B1Token: ., S0B0Distance: 1, S0B0Lemma: yer_ver, S0B0LemmaPOS: yer_Verb, S0B0POS: Noun_Verb, S0B0POSLemma: Noun_ver, S0B0Token: yer_verildi, S0B1Lemma: yer_., S0B1LemmaPOS: yer_Punc, S0B1POS: Noun_Punc, S0B1POSLemma: Noun_., S0B1Token: yer_., S0Lemma: yer, S0POS: Noun, S0Token: yer, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, yer_isGouvernedBy_ver: true, yer_isGouvernedBy_ver_MWE: true, 

196- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [yer, verildi]   B= [.]

B0Lemma: ., B0POS: Punc, B0Token: ., S0B0Distance: 1, S0B0Lemma: ver_., S0B0LemmaPOS: ver_Punc, S0B0POS: Verb_Punc, S0B0POSLemma: Verb_., S0B0Token: verildi_., S0Lemma: ver, S0POS: Verb, S0Token: verildi, S1B0Lemma: yer_., S1B0LemmaPOS: yer_Punc, S1B0POS: Noun_Punc, S1B0POSLemma: Noun_., S1B0Token: yer_., S1Lemma: yer, S1POS: Noun, S1S0Lemma: yer_ver, S1S0LemmaPOS: yer_Verb, S1S0POS: Noun_Verb, S1S0POSLemma: Noun_ver, S1S0Token: yer_verildi, S1Token: yer, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

197- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[yer, verildi]]   B= [.]

B0Lemma: ., B0POS: Punc, B0Token: ., S0B0Distance: 1, S0B0Lemma: yer_ver_., S0B0LemmaPOS: yer_ver_Punc, S0B0POS: Noun_Verb_Punc, S0B0POSLemma: Noun_Verb_., S0B0Token: yer_verildi_., S0Lemma: yer_ver, S0POS: Noun_Verb, S0Token: yer_verildi, transitionHistoryLength1: 0, transitionHistoryLength2: 00, transitionHistoryLength3: 002, 

198- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [.]

B0Lemma: ., B0POS: Punc, B0Token: ., transitionHistoryLength1: 1, transitionHistoryLength2: 10, transitionHistoryLength3: 100, 

199- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [ ]

S0Lemma: ., S0POS: Punc, S0Token: ., transitionHistoryLength1: 2, transitionHistoryLength2: 21, transitionHistoryLength3: 210, 

200- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

## Sentence No. 2479 - 
Gündüz'e ara sıra telefon _ ederek bazı sorular _ sorduğunu ifade _ eden Şahin , " Ona ` RP hakkında ne düşünüyorsun . ' diye sordum . ` Onlar şaşırmışlar , onların _ düzelmesi için Allah'a dua ediyorum . Erbakan bukalemun gibi yön değiştiriyor ' yanıtını verdi . Erbakan'ı yalancı ve iktidar _ olmak için dini alet _ eden bir insan olarak görüyordu " diye konuştu . 
### Existing MWEs: 
1- **telefon ederek** (LVC)
2- **ifade eden** (LVC)
3- **dua ediyorum** (LVC)



0- &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Gündüz'e, ara, sıra ,.. ]

B0Lemma: Gündüz, B0POS: Noun, B0Token: Gündüz'e, B1Lemma: ara, B1POS: Noun, B1Token: ara, 

1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Gündüz'e]   B= [ara, sıra, telefon ,.. ]

B0Lemma: ara, B0POS: Noun, B0Token: ara, B1Lemma: sıra, B1POS: Noun, B1Token: sıra, Gündüz_isGouvernedBy_et: true, Gündüz_isGouvernedBy_et_MODIFIER: true, S0B0Distance: 1, S0B0Lemma: Gündüz_ara, S0B0LemmaPOS: Gündüz_Noun, S0B0POS: Noun_Noun, S0B0POSLemma: Noun_ara, S0B0Token: Gündüz'e_ara, S0B1Lemma: Gündüz_sıra, S0B1LemmaPOS: Gündüz_Noun, S0B1POS: Noun_Noun, S0B1POSLemma: Noun_sıra, S0B1Token: Gündüz'e_sıra, S0Lemma: Gündüz, S0POS: Noun, S0Token: Gündüz'e, 

2- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ara, sıra, telefon ,.. ]

B0Lemma: ara, B0POS: Noun, B0Token: ara, B1Lemma: sıra, B1POS: Noun, B1Token: sıra, transitionHistoryLength1: 0, 

3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ara]   B= [sıra, telefon, _ ,.. ]

B0Lemma: sıra, B0POS: Noun, B0Token: sıra, B1Lemma: telefon, B1POS: Noun, B1Token: telefon, S0B0Distance: 1, S0B0Lemma: ara_sıra, S0B0LemmaPOS: ara_Noun, S0B0POS: Noun_Noun, S0B0POSLemma: Noun_sıra, S0B0Token: ara_sıra, S0B1Lemma: ara_telefon, S0B1LemmaPOS: ara_Noun, S0B1POS: Noun_Noun, S0B1POSLemma: Noun_telefon, S0B1Token: ara_telefon, S0Lemma: ara, S0POS: Noun, S0Token: ara, ara_isGouvernedBy_sıra: true, ara_isGouvernedBy_sıra_MWE: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, 

4- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [sıra, telefon, _ ,.. ]

B0Lemma: sıra, B0POS: Noun, B0Token: sıra, B1Lemma: telefon, B1POS: Noun, B1Token: telefon, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [sıra]   B= [telefon, _, ederek ,.. ]

B0Lemma: telefon, B0POS: Noun, B0Token: telefon, B1Lemma: et, B1POS: Verb, B1Token: _, S0B0Distance: 1, S0B0Lemma: sıra_telefon, S0B0LemmaPOS: sıra_Noun, S0B0POS: Noun_Noun, S0B0POSLemma: Noun_telefon, S0B0Token: sıra_telefon, S0B1Lemma: sıra_et, S0B1LemmaPOS: sıra_Verb, S0B1POS: Noun_Verb, S0B1POSLemma: Noun_et, S0B1Token: sıra__, S0Lemma: sıra, S0POS: Noun, S0Token: sıra, sıra_isGouvernedBy_et: true, sıra_isGouvernedBy_et_MODIFIER: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

6- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [telefon, _, ederek ,.. ]

B0Lemma: telefon, B0POS: Noun, B0Token: telefon, B1Lemma: et, B1POS: Verb, B1Token: _, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [telefon]   B= [_, ederek, bazı ,.. ]

B0Lemma: et, B0POS: Verb, B0Token: _, B1Lemma: _, B1POS: Adverb, B1Token: ederek, S0B0Distance: 1, S0B0Lemma: telefon_et, S0B0LemmaPOS: telefon_Verb, S0B0POS: Noun_Verb, S0B0POSLemma: Noun_et, S0B0Token: telefon__, S0B1Lemma: telefon__, S0B1LemmaPOS: telefon_Adverb, S0B1POS: Noun_Adverb, S0B1POSLemma: Noun__, S0B1Token: telefon_ederek, S0Lemma: telefon, S0POS: Noun, S0Token: telefon, telefon_isGouvernedBy_et: true, telefon_isGouvernedBy_et_MWE: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

8- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [telefon, _]   B= [ederek, bazı, sorular ,.. ]

B0Lemma: _, B0POS: Adverb, B0Token: ederek, B1Lemma: bazı, B1POS: Det, B1Token: bazı, S0B0Distance: 1, S0B0Lemma: et__, S0B0LemmaPOS: et_Adverb, S0B0POS: Verb_Adverb, S0B0POSLemma: Verb__, S0B0Token: __ederek, S0B1Lemma: et_bazı, S0B1LemmaPOS: et_Det, S0B1POS: Verb_Det, S0B1POSLemma: Verb_bazı, S0B1Token: __bazı, S0Lemma: et, S0POS: Verb, S0Token: _, S1B0Lemma: telefon__, S1B0LemmaPOS: telefon_Adverb, S1B0POS: Noun_Adverb, S1B0POSLemma: Noun__, S1B0Token: telefon_ederek, S1Lemma: telefon, S1POS: Noun, S1S0Lemma: telefon_et, S1S0LemmaPOS: telefon_Verb, S1S0POS: Noun_Verb, S1S0POSLemma: Noun_et, S1S0Token: telefon__, S1Token: telefon, SyntaxicRelation: -MWE, et_isGouvernedBy__: true, et_isGouvernedBy___DERIV: true, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

9- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [telefon]   B= [ederek, bazı, sorular ,.. ]

B0Lemma: _, B0POS: Adverb, B0Token: ederek, B1Lemma: bazı, B1POS: Det, B1Token: bazı, S0B0Distance: 2, S0B0Lemma: telefon__, S0B0LemmaPOS: telefon_Adverb, S0B0POS: Noun_Adverb, S0B0POSLemma: Noun__, S0B0Token: telefon_ederek, S0B1Lemma: telefon_bazı, S0B1LemmaPOS: telefon_Det, S0B1POS: Noun_Det, S0B1POSLemma: Noun_bazı, S0B1Token: telefon_bazı, S0Lemma: telefon, S0POS: Noun, S0Token: telefon, transitionHistoryLength1: 0, transitionHistoryLength2: 00, transitionHistoryLength3: 002, 

10- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [telefon, ederek]   B= [bazı, sorular, _ ,.. ]

B0Lemma: bazı, B0POS: Det, B0Token: bazı, B1Lemma: soru, B1POS: Noun, B1Token: sorular, S0B0Distance: 1, S0B0Lemma: __bazı, S0B0LemmaPOS: __Det, S0B0POS: Adverb_Det, S0B0POSLemma: Adverb_bazı, S0B0Token: ederek_bazı, S0B1Lemma: __soru, S0B1LemmaPOS: __Noun, S0B1POS: Adverb_Noun, S0B1POSLemma: Adverb_soru, S0B1Token: ederek_sorular, S0Lemma: _, S0POS: Adverb, S0Token: ederek, S1B0Lemma: telefon_bazı, S1B0LemmaPOS: telefon_Det, S1B0POS: Noun_Det, S1B0POSLemma: Noun_bazı, S1B0Token: telefon_bazı, S1Lemma: telefon, S1POS: Noun, S1S0Lemma: telefon__, S1S0LemmaPOS: telefon_Adverb, S1S0POS: Noun_Adverb, S1S0POSLemma: Noun__, S1S0Token: telefon_ederek, S1Token: telefon, __isGouvernedBy_sor: true, __isGouvernedBy_sor_MODIFIER: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 200, 

11- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[telefon, ederek]]   B= [bazı, sorular, _ ,.. ]

B0Lemma: bazı, B0POS: Det, B0Token: bazı, B1Lemma: soru, B1POS: Noun, B1Token: sorular, S0B0Distance: 1, S0B0Lemma: telefon___bazı, S0B0LemmaPOS: telefon___Det, S0B0POS: Noun_Adverb_Det, S0B0POSLemma: Noun_Adverb_bazı, S0B0Token: telefon_ederek_bazı, S0B1Lemma: telefon___soru, S0B1LemmaPOS: telefon___Noun, S0B1POS: Noun_Adverb_Noun, S0B1POSLemma: Noun_Adverb_soru, S0B1Token: telefon_ederek_sorular, S0Lemma: telefon__, S0POS: Noun_Adverb, S0Token: telefon_ederek, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

12- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [bazı, sorular, _ ,.. ]

B0Lemma: bazı, B0POS: Det, B0Token: bazı, B1Lemma: soru, B1POS: Noun, B1Token: sorular, transitionHistoryLength1: 1, transitionHistoryLength2: 10, transitionHistoryLength3: 102, 

13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [bazı]   B= [sorular, _, sorduğunu ,.. ]

B0Lemma: soru, B0POS: Noun, B0Token: sorular, B1Lemma: sor, B1POS: Verb, B1Token: _, S0B0Distance: 1, S0B0Lemma: bazı_soru, S0B0LemmaPOS: bazı_Noun, S0B0POS: Det_Noun, S0B0POSLemma: Det_soru, S0B0Token: bazı_sorular, S0B1Lemma: bazı_sor, S0B1LemmaPOS: bazı_Verb, S0B1POS: Det_Verb, S0B1POSLemma: Det_sor, S0B1Token: bazı__, S0Lemma: bazı, S0POS: Det, S0Token: bazı, bazı_isGouvernedBy_soru: true, bazı_isGouvernedBy_soru_DETERMINER: true, transitionHistoryLength1: 2, transitionHistoryLength2: 21, transitionHistoryLength3: 210, 

14- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [sorular, _, sorduğunu ,.. ]

B0Lemma: soru, B0POS: Noun, B0Token: sorular, B1Lemma: sor, B1POS: Verb, B1Token: _, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 021, 

15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [sorular]   B= [_, sorduğunu, ifade ,.. ]

B0Lemma: sor, B0POS: Verb, B0Token: _, B1Lemma: _, B1POS: Noun, B1Token: sorduğunu, S0B0Distance: 1, S0B0Lemma: soru_sor, S0B0LemmaPOS: soru_Verb, S0B0POS: Noun_Verb, S0B0POSLemma: Noun_sor, S0B0Token: sorular__, S0B1Lemma: soru__, S0B1LemmaPOS: soru_Noun, S0B1POS: Noun_Noun, S0B1POSLemma: Noun__, S0B1Token: sorular_sorduğunu, S0Lemma: soru, S0POS: Noun, S0Token: sorular, soru_isGouvernedBy_sor: true, soru_isGouvernedBy_sor_OBJECT: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

16- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [_, sorduğunu, ifade ,.. ]

B0Lemma: sor, B0POS: Verb, B0Token: _, B1Lemma: _, B1POS: Noun, B1Token: sorduğunu, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [_]   B= [sorduğunu, ifade, _ ,.. ]

B0Lemma: _, B0POS: Noun, B0Token: sorduğunu, B1Lemma: ifade, B1POS: Noun, B1Token: ifade, S0B0Distance: 1, S0B0Lemma: sor__, S0B0LemmaPOS: sor_Noun, S0B0POS: Verb_Noun, S0B0POSLemma: Verb__, S0B0Token: __sorduğunu, S0B1Lemma: sor_ifade, S0B1LemmaPOS: sor_Noun, S0B1POS: Verb_Noun, S0B1POSLemma: Verb_ifade, S0B1Token: __ifade, S0Lemma: sor, S0POS: Verb, S0Token: _, sor_isGouvernedBy__: true, sor_isGouvernedBy___DERIV: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

18- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [sorduğunu, ifade, _ ,.. ]

B0Lemma: _, B0POS: Noun, B0Token: sorduğunu, B1Lemma: ifade, B1POS: Noun, B1Token: ifade, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [sorduğunu]   B= [ifade, _, eden ,.. ]

B0Lemma: ifade, B0POS: Noun, B0Token: ifade, B1Lemma: et, B1POS: Verb, B1Token: _, S0B0Distance: 1, S0B0Lemma: __ifade, S0B0LemmaPOS: __Noun, S0B0POS: Noun_Noun, S0B0POSLemma: Noun_ifade, S0B0Token: sorduğunu_ifade, S0B1Lemma: __et, S0B1LemmaPOS: __Verb, S0B1POS: Noun_Verb, S0B1POSLemma: Noun_et, S0B1Token: sorduğunu__, S0Lemma: _, S0POS: Noun, S0Token: sorduğunu, __isGouvernedBy_et: true, __isGouvernedBy_et_OBJECT: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

20- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ifade, _, eden ,.. ]

B0Lemma: ifade, B0POS: Noun, B0Token: ifade, B1Lemma: et, B1POS: Verb, B1Token: _, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ifade]   B= [_, eden, Şahin ,.. ]

B0Lemma: et, B0POS: Verb, B0Token: _, B1Lemma: _, B1POS: Adj, B1Token: eden, S0B0Distance: 1, S0B0Lemma: ifade_et, S0B0LemmaPOS: ifade_Verb, S0B0POS: Noun_Verb, S0B0POSLemma: Noun_et, S0B0Token: ifade__, S0B1Lemma: ifade__, S0B1LemmaPOS: ifade_Adj, S0B1POS: Noun_Adj, S0B1POSLemma: Noun__, S0B1Token: ifade_eden, S0Lemma: ifade, S0POS: Noun, S0Token: ifade, ifade_isGouvernedBy_et: true, ifade_isGouvernedBy_et_MWE: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

22- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ifade, _]   B= [eden, Şahin, , ,.. ]

B0Lemma: _, B0POS: Adj, B0Token: eden, B1Lemma: Şahin, B1POS: Noun, B1Token: Şahin, S0B0Distance: 1, S0B0Lemma: et__, S0B0LemmaPOS: et_Adj, S0B0POS: Verb_Adj, S0B0POSLemma: Verb__, S0B0Token: __eden, S0B1Lemma: et_Şahin, S0B1LemmaPOS: et_Noun, S0B1POS: Verb_Noun, S0B1POSLemma: Verb_Şahin, S0B1Token: __Şahin, S0Lemma: et, S0POS: Verb, S0Token: _, S1B0Lemma: ifade__, S1B0LemmaPOS: ifade_Adj, S1B0POS: Noun_Adj, S1B0POSLemma: Noun__, S1B0Token: ifade_eden, S1Lemma: ifade, S1POS: Noun, S1S0Lemma: ifade_et, S1S0LemmaPOS: ifade_Verb, S1S0POS: Noun_Verb, S1S0POSLemma: Noun_et, S1S0Token: ifade__, S1Token: ifade, SyntaxicRelation: -MWE, et_isGouvernedBy__: true, et_isGouvernedBy___DERIV: true, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

23- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ifade]   B= [eden, Şahin, , ,.. ]

B0Lemma: _, B0POS: Adj, B0Token: eden, B1Lemma: Şahin, B1POS: Noun, B1Token: Şahin, S0B0Distance: 2, S0B0Lemma: ifade__, S0B0LemmaPOS: ifade_Adj, S0B0POS: Noun_Adj, S0B0POSLemma: Noun__, S0B0Token: ifade_eden, S0B1Lemma: ifade_Şahin, S0B1LemmaPOS: ifade_Noun, S0B1POS: Noun_Noun, S0B1POSLemma: Noun_Şahin, S0B1Token: ifade_Şahin, S0Lemma: ifade, S0POS: Noun, S0Token: ifade, transitionHistoryLength1: 0, transitionHistoryLength2: 00, transitionHistoryLength3: 002, 

24- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ifade, eden]   B= [Şahin, ,, " ,.. ]

B0Lemma: Şahin, B0POS: Noun, B0Token: Şahin, B1Lemma: ,, B1POS: Punc, B1Token: ,, S0B0Distance: 1, S0B0Lemma: __Şahin, S0B0LemmaPOS: __Noun, S0B0POS: Adj_Noun, S0B0POSLemma: Adj_Şahin, S0B0Token: eden_Şahin, S0B1Lemma: __,, S0B1LemmaPOS: __Punc, S0B1POS: Adj_Punc, S0B1POSLemma: Adj_,, S0B1Token: eden_,, S0Lemma: _, S0POS: Adj, S0Token: eden, S1B0Lemma: ifade_Şahin, S1B0LemmaPOS: ifade_Noun, S1B0POS: Noun_Noun, S1B0POSLemma: Noun_Şahin, S1B0Token: ifade_Şahin, S1Lemma: ifade, S1POS: Noun, S1S0Lemma: ifade__, S1S0LemmaPOS: ifade_Adj, S1S0POS: Noun_Adj, S1S0POSLemma: Noun__, S1S0Token: ifade_eden, S1Token: ifade, __isGouvernedBy_Şahin: true, __isGouvernedBy_Şahin_MODIFIER: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 200, 

25- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[ifade, eden]]   B= [Şahin, ,, " ,.. ]

B0Lemma: Şahin, B0POS: Noun, B0Token: Şahin, B1Lemma: ,, B1POS: Punc, B1Token: ,, S0B0Distance: 1, S0B0Lemma: ifade___Şahin, S0B0LemmaPOS: ifade___Noun, S0B0POS: Noun_Adj_Noun, S0B0POSLemma: Noun_Adj_Şahin, S0B0Token: ifade_eden_Şahin, S0B1Lemma: ifade___,, S0B1LemmaPOS: ifade___Punc, S0B1POS: Noun_Adj_Punc, S0B1POSLemma: Noun_Adj_,, S0B1Token: ifade_eden_,, S0Lemma: ifade__, S0POS: Noun_Adj, S0Token: ifade_eden, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

26- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Şahin, ,, " ,.. ]

B0Lemma: Şahin, B0POS: Noun, B0Token: Şahin, B1Lemma: ,, B1POS: Punc, B1Token: ,, transitionHistoryLength1: 1, transitionHistoryLength2: 10, transitionHistoryLength3: 102, 

27- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Şahin]   B= [,, ", Ona ,.. ]

B0Lemma: ,, B0POS: Punc, B0Token: ,, B1Lemma: ", B1POS: Punc, B1Token: ", S0B0Distance: 1, S0B0Lemma: Şahin_,, S0B0LemmaPOS: Şahin_Punc, S0B0POS: Noun_Punc, S0B0POSLemma: Noun_,, S0B0Token: Şahin_,, S0B1Lemma: Şahin_", S0B1LemmaPOS: Şahin_Punc, S0B1POS: Noun_Punc, S0B1POSLemma: Noun_", S0B1Token: Şahin_", S0Lemma: Şahin, S0POS: Noun, S0Token: Şahin, hasRighDep_PUNCTUATION: true, transitionHistoryLength1: 2, transitionHistoryLength2: 21, transitionHistoryLength3: 210, Şahin_"_hasRighDep_PUNCTUATION: true, Şahin_,_hasRighDep_PUNCTUATION: true, Şahin_hasRighDep_PUNCTUATION: true, Şahin_isGouvernedBy_düşün: true, Şahin_isGouvernedBy_düşün_SUBJECT: true, 

28- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, ", Ona ,.. ]

B0Lemma: ,, B0POS: Punc, B0Token: ,, B1Lemma: ", B1POS: Punc, B1Token: ", transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 021, 

29- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [", Ona, ` ,.. ]

B0Lemma: ", B0POS: Punc, B0Token: ", B1Lemma: o, B1POS: Pron, B1Token: Ona, S0B0Distance: 1, S0B0Lemma: ,_", S0B0LemmaPOS: ,_Punc, S0B0POS: Punc_Punc, S0B0POSLemma: Punc_", S0B0Token: ,_", S0B1Lemma: ,_o, S0B1LemmaPOS: ,_Pron, S0B1POS: Punc_Pron, S0B1POSLemma: Punc_o, S0B1Token: ,_Ona, S0Lemma: ,, S0POS: Punc, S0Token: ,, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

30- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [", Ona, ` ,.. ]

B0Lemma: ", B0POS: Punc, B0Token: ", B1Lemma: o, B1POS: Pron, B1Token: Ona, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

31- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= ["]   B= [Ona, `, RP ,.. ]

B0Lemma: o, B0POS: Pron, B0Token: Ona, B1Lemma: `, B1POS: Punc, B1Token: `, S0B0Distance: 1, S0B0Lemma: "_o, S0B0LemmaPOS: "_Pron, S0B0POS: Punc_Pron, S0B0POSLemma: Punc_o, S0B0Token: "_Ona, S0B1Lemma: "_`, S0B1LemmaPOS: "_Punc, S0B1POS: Punc_Punc, S0B1POSLemma: Punc_`, S0B1Token: "_`, S0Lemma: ", S0POS: Punc, S0Token: ", transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

32- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Ona, `, RP ,.. ]

B0Lemma: o, B0POS: Pron, B0Token: Ona, B1Lemma: `, B1POS: Punc, B1Token: `, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

33- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Ona]   B= [`, RP, hakkında ,.. ]

B0Lemma: `, B0POS: Punc, B0Token: `, B1Lemma: Rp, B1POS: Noun, B1Token: RP, S0B0Distance: 1, S0B0Lemma: o_`, S0B0LemmaPOS: o_Punc, S0B0POS: Pron_Punc, S0B0POSLemma: Pron_`, S0B0Token: Ona_`, S0B1Lemma: o_Rp, S0B1LemmaPOS: o_Noun, S0B1POS: Pron_Noun, S0B1POSLemma: Pron_Rp, S0B1Token: Ona_RP, S0Lemma: o, S0POS: Pron, S0Token: Ona, hasRighDep_PUNCTUATION: true, o_`_hasRighDep_PUNCTUATION: true, o_hasRighDep_PUNCTUATION: true, o_isGouvernedBy_düşün: true, o_isGouvernedBy_düşün_MODIFIER: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

34- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [`, RP, hakkında ,.. ]

B0Lemma: `, B0POS: Punc, B0Token: `, B1Lemma: Rp, B1POS: Noun, B1Token: RP, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

35- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [`]   B= [RP, hakkında, ne ,.. ]

B0Lemma: Rp, B0POS: Noun, B0Token: RP, B1Lemma: hak, B1POS: Noun, B1Token: hakkında, S0B0Distance: 1, S0B0Lemma: `_Rp, S0B0LemmaPOS: `_Noun, S0B0POS: Punc_Noun, S0B0POSLemma: Punc_Rp, S0B0Token: `_RP, S0B1Lemma: `_hak, S0B1LemmaPOS: `_Noun, S0B1POS: Punc_Noun, S0B1POSLemma: Punc_hak, S0B1Token: `_hakkında, S0Lemma: `, S0POS: Punc, S0Token: `, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

36- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [RP, hakkında, ne ,.. ]

B0Lemma: Rp, B0POS: Noun, B0Token: RP, B1Lemma: hak, B1POS: Noun, B1Token: hakkında, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

37- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [RP]   B= [hakkında, ne, düşünüyorsun ,.. ]

B0Lemma: hak, B0POS: Noun, B0Token: hakkında, B1Lemma: ne, B1POS: Pron, B1Token: ne, Rp_isGouvernedBy_hak: true, Rp_isGouvernedBy_hak_POSSESSOR: true, S0B0Distance: 1, S0B0Lemma: Rp_hak, S0B0LemmaPOS: Rp_Noun, S0B0POS: Noun_Noun, S0B0POSLemma: Noun_hak, S0B0Token: RP_hakkında, S0B1Lemma: Rp_ne, S0B1LemmaPOS: Rp_Pron, S0B1POS: Noun_Pron, S0B1POSLemma: Noun_ne, S0B1Token: RP_ne, S0Lemma: Rp, S0POS: Noun, S0Token: RP, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

38- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [hakkında, ne, düşünüyorsun ,.. ]

B0Lemma: hak, B0POS: Noun, B0Token: hakkında, B1Lemma: ne, B1POS: Pron, B1Token: ne, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

39- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [hakkında]   B= [ne, düşünüyorsun, . ,.. ]

B0Lemma: ne, B0POS: Pron, B0Token: ne, B1Lemma: düşün, B1POS: Verb, B1Token: düşünüyorsun, S0B0Distance: 1, S0B0Lemma: hak_ne, S0B0LemmaPOS: hak_Pron, S0B0POS: Noun_Pron, S0B0POSLemma: Noun_ne, S0B0Token: hakkında_ne, S0B1Lemma: hak_düşün, S0B1LemmaPOS: hak_Verb, S0B1POS: Noun_Verb, S0B1POSLemma: Noun_düşün, S0B1Token: hakkında_düşünüyorsun, S0Lemma: hak, S0POS: Noun, S0Token: hakkında, hak_isGouvernedBy_düşün: true, hak_isGouvernedBy_düşün_MODIFIER: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

40- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ne, düşünüyorsun, . ,.. ]

B0Lemma: ne, B0POS: Pron, B0Token: ne, B1Lemma: düşün, B1POS: Verb, B1Token: düşünüyorsun, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

41- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ne]   B= [düşünüyorsun, ., ' ,.. ]

B0Lemma: düşün, B0POS: Verb, B0Token: düşünüyorsun, B1Lemma: ., B1POS: Punc, B1Token: ., S0B0Distance: 1, S0B0Lemma: ne_düşün, S0B0LemmaPOS: ne_Verb, S0B0POS: Pron_Verb, S0B0POSLemma: Pron_düşün, S0B0Token: ne_düşünüyorsun, S0B1Lemma: ne_., S0B1LemmaPOS: ne_Punc, S0B1POS: Pron_Punc, S0B1POSLemma: Pron_., S0B1Token: ne_., S0Lemma: ne, S0POS: Pron, S0Token: ne, ne_isGouvernedBy_düşün: true, ne_isGouvernedBy_düşün_OBJECT: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

42- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [düşünüyorsun, ., ' ,.. ]

B0Lemma: düşün, B0POS: Verb, B0Token: düşünüyorsun, B1Lemma: ., B1POS: Punc, B1Token: ., transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

43- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [düşünüyorsun]   B= [., ', diye ,.. ]

B0Lemma: ., B0POS: Punc, B0Token: ., B1Lemma: ', B1POS: Punc, B1Token: ', S0B0Distance: 1, S0B0Lemma: düşün_., S0B0LemmaPOS: düşün_Punc, S0B0POS: Verb_Punc, S0B0POSLemma: Verb_., S0B0Token: düşünüyorsun_., S0B1Lemma: düşün_', S0B1LemmaPOS: düşün_Punc, S0B1POS: Verb_Punc, S0B1POSLemma: Verb_', S0B1Token: düşünüyorsun_', S0Lemma: düşün, S0POS: Verb, S0Token: düşünüyorsun, düşün_'_hasRighDep_PUNCTUATION: true, düşün_._hasRighDep_PUNCTUATION: true, düşün_hasRighDep_PUNCTUATION: true, düşün_isGouvernedBy_diye: true, düşün_isGouvernedBy_diye_ARGUMENT: true, hasRighDep_PUNCTUATION: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

44- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [., ', diye ,.. ]

B0Lemma: ., B0POS: Punc, B0Token: ., B1Lemma: ', B1POS: Punc, B1Token: ', transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

45- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [', diye, sordum ,.. ]

B0Lemma: ', B0POS: Punc, B0Token: ', B1Lemma: diye, B1POS: Postp, B1Token: diye, S0B0Distance: 1, S0B0Lemma: ._', S0B0LemmaPOS: ._Punc, S0B0POS: Punc_Punc, S0B0POSLemma: Punc_', S0B0Token: ._', S0B1Lemma: ._diye, S0B1LemmaPOS: ._Postp, S0B1POS: Punc_Postp, S0B1POSLemma: Punc_diye, S0B1Token: ._diye, S0Lemma: ., S0POS: Punc, S0Token: ., transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

46- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [', diye, sordum ,.. ]

B0Lemma: ', B0POS: Punc, B0Token: ', B1Lemma: diye, B1POS: Postp, B1Token: diye, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

47- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [']   B= [diye, sordum, . ,.. ]

B0Lemma: diye, B0POS: Postp, B0Token: diye, B1Lemma: sor, B1POS: Verb, B1Token: sordum, S0B0Distance: 1, S0B0Lemma: '_diye, S0B0LemmaPOS: '_Postp, S0B0POS: Punc_Postp, S0B0POSLemma: Punc_diye, S0B0Token: '_diye, S0B1Lemma: '_sor, S0B1LemmaPOS: '_Verb, S0B1POS: Punc_Verb, S0B1POSLemma: Punc_sor, S0B1Token: '_sordum, S0Lemma: ', S0POS: Punc, S0Token: ', transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

48- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [diye, sordum, . ,.. ]

B0Lemma: diye, B0POS: Postp, B0Token: diye, B1Lemma: sor, B1POS: Verb, B1Token: sordum, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

49- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [diye]   B= [sordum, ., ` ,.. ]

B0Lemma: sor, B0POS: Verb, B0Token: sordum, B1Lemma: ., B1POS: Punc, B1Token: ., S0B0Distance: 1, S0B0Lemma: diye_sor, S0B0LemmaPOS: diye_Verb, S0B0POS: Postp_Verb, S0B0POSLemma: Postp_sor, S0B0Token: diye_sordum, S0B1Lemma: diye_., S0B1LemmaPOS: diye_Punc, S0B1POS: Postp_Punc, S0B1POSLemma: Postp_., S0B1Token: diye_., S0Lemma: diye, S0POS: Postp, S0Token: diye, diye_isGouvernedBy_sor: true, diye_isGouvernedBy_sor_MODIFIER: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

50- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [sordum, ., ` ,.. ]

B0Lemma: sor, B0POS: Verb, B0Token: sordum, B1Lemma: ., B1POS: Punc, B1Token: ., transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

51- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [sordum]   B= [., `, Onlar ,.. ]

B0Lemma: ., B0POS: Punc, B0Token: ., B1Lemma: `, B1POS: Punc, B1Token: `, S0B0Distance: 1, S0B0Lemma: sor_., S0B0LemmaPOS: sor_Punc, S0B0POS: Verb_Punc, S0B0POSLemma: Verb_., S0B0Token: sordum_., S0B1Lemma: sor_`, S0B1LemmaPOS: sor_Punc, S0B1POS: Verb_Punc, S0B1POSLemma: Verb_`, S0B1Token: sordum_`, S0Lemma: sor, S0POS: Verb, S0Token: sordum, hasRighDep_PUNCTUATION: true, sor_._hasRighDep_PUNCTUATION: true, sor_`_hasRighDep_PUNCTUATION: true, sor_hasRighDep_PUNCTUATION: true, sor_isGouvernedBy_şaşır: true, sor_isGouvernedBy_şaşır_COORDINATION: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

52- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [., `, Onlar ,.. ]

B0Lemma: ., B0POS: Punc, B0Token: ., B1Lemma: `, B1POS: Punc, B1Token: `, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

53- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [`, Onlar, şaşırmışlar ,.. ]

B0Lemma: `, B0POS: Punc, B0Token: `, B1Lemma: o, B1POS: Pron, B1Token: Onlar, S0B0Distance: 1, S0B0Lemma: ._`, S0B0LemmaPOS: ._Punc, S0B0POS: Punc_Punc, S0B0POSLemma: Punc_`, S0B0Token: ._`, S0B1Lemma: ._o, S0B1LemmaPOS: ._Pron, S0B1POS: Punc_Pron, S0B1POSLemma: Punc_o, S0B1Token: ._Onlar, S0Lemma: ., S0POS: Punc, S0Token: ., transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

54- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [`, Onlar, şaşırmışlar ,.. ]

B0Lemma: `, B0POS: Punc, B0Token: `, B1Lemma: o, B1POS: Pron, B1Token: Onlar, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

55- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [`]   B= [Onlar, şaşırmışlar, , ,.. ]

B0Lemma: o, B0POS: Pron, B0Token: Onlar, B1Lemma: şaşır, B1POS: Verb, B1Token: şaşırmışlar, S0B0Distance: 1, S0B0Lemma: `_o, S0B0LemmaPOS: `_Pron, S0B0POS: Punc_Pron, S0B0POSLemma: Punc_o, S0B0Token: `_Onlar, S0B1Lemma: `_şaşır, S0B1LemmaPOS: `_Verb, S0B1POS: Punc_Verb, S0B1POSLemma: Punc_şaşır, S0B1Token: `_şaşırmışlar, S0Lemma: `, S0POS: Punc, S0Token: `, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

56- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Onlar, şaşırmışlar, , ,.. ]

B0Lemma: o, B0POS: Pron, B0Token: Onlar, B1Lemma: şaşır, B1POS: Verb, B1Token: şaşırmışlar, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

57- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Onlar]   B= [şaşırmışlar, ,, onların ,.. ]

B0Lemma: şaşır, B0POS: Verb, B0Token: şaşırmışlar, B1Lemma: ,, B1POS: Punc, B1Token: ,, S0B0Distance: 1, S0B0Lemma: o_şaşır, S0B0LemmaPOS: o_Verb, S0B0POS: Pron_Verb, S0B0POSLemma: Pron_şaşır, S0B0Token: Onlar_şaşırmışlar, S0B1Lemma: o_,, S0B1LemmaPOS: o_Punc, S0B1POS: Pron_Punc, S0B1POSLemma: Pron_,, S0B1Token: Onlar_,, S0Lemma: o, S0POS: Pron, S0Token: Onlar, o_isGouvernedBy_şaşır: true, o_isGouvernedBy_şaşır_SUBJECT: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

58- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [şaşırmışlar, ,, onların ,.. ]

B0Lemma: şaşır, B0POS: Verb, B0Token: şaşırmışlar, B1Lemma: ,, B1POS: Punc, B1Token: ,, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

59- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [şaşırmışlar]   B= [,, onların, _ ,.. ]

B0Lemma: ,, B0POS: Punc, B0Token: ,, B1Lemma: o, B1POS: Pron, B1Token: onların, S0B0Distance: 1, S0B0Lemma: şaşır_,, S0B0LemmaPOS: şaşır_Punc, S0B0POS: Verb_Punc, S0B0POSLemma: Verb_,, S0B0Token: şaşırmışlar_,, S0B1Lemma: şaşır_o, S0B1LemmaPOS: şaşır_Pron, S0B1POS: Verb_Pron, S0B1POSLemma: Verb_o, S0B1Token: şaşırmışlar_onların, S0Lemma: şaşır, S0POS: Verb, S0Token: şaşırmışlar, hasRighDep_PUNCTUATION: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, şaşır_,_hasRighDep_PUNCTUATION: true, şaşır_hasRighDep_PUNCTUATION: true, şaşır_isGouvernedBy_et: true, şaşır_isGouvernedBy_et_COORDINATION: true, 

60- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, onların, _ ,.. ]

B0Lemma: ,, B0POS: Punc, B0Token: ,, B1Lemma: o, B1POS: Pron, B1Token: onların, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

61- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [onların, _, düzelmesi ,.. ]

B0Lemma: o, B0POS: Pron, B0Token: onların, B1Lemma: düzel, B1POS: Verb, B1Token: _, S0B0Distance: 1, S0B0Lemma: ,_o, S0B0LemmaPOS: ,_Pron, S0B0POS: Punc_Pron, S0B0POSLemma: Punc_o, S0B0Token: ,_onların, S0B1Lemma: ,_düzel, S0B1LemmaPOS: ,_Verb, S0B1POS: Punc_Verb, S0B1POSLemma: Punc_düzel, S0B1Token: ,__, S0Lemma: ,, S0POS: Punc, S0Token: ,, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

62- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [onların, _, düzelmesi ,.. ]

B0Lemma: o, B0POS: Pron, B0Token: onların, B1Lemma: düzel, B1POS: Verb, B1Token: _, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

63- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [onların]   B= [_, düzelmesi, için ,.. ]

B0Lemma: düzel, B0POS: Verb, B0Token: _, B1Lemma: _, B1POS: Noun, B1Token: düzelmesi, S0B0Distance: 1, S0B0Lemma: o_düzel, S0B0LemmaPOS: o_Verb, S0B0POS: Pron_Verb, S0B0POSLemma: Pron_düzel, S0B0Token: onların__, S0B1Lemma: o__, S0B1LemmaPOS: o_Noun, S0B1POS: Pron_Noun, S0B1POSLemma: Pron__, S0B1Token: onların_düzelmesi, S0Lemma: o, S0POS: Pron, S0Token: onların, o_isGouvernedBy__: true, o_isGouvernedBy___POSSESSOR: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

64- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [_, düzelmesi, için ,.. ]

B0Lemma: düzel, B0POS: Verb, B0Token: _, B1Lemma: _, B1POS: Noun, B1Token: düzelmesi, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

65- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [_]   B= [düzelmesi, için, Allah'a ,.. ]

B0Lemma: _, B0POS: Noun, B0Token: düzelmesi, B1Lemma: için, B1POS: Postp, B1Token: için, S0B0Distance: 1, S0B0Lemma: düzel__, S0B0LemmaPOS: düzel_Noun, S0B0POS: Verb_Noun, S0B0POSLemma: Verb__, S0B0Token: __düzelmesi, S0B1Lemma: düzel_için, S0B1LemmaPOS: düzel_Postp, S0B1POS: Verb_Postp, S0B1POSLemma: Verb_için, S0B1Token: __için, S0Lemma: düzel, S0POS: Verb, S0Token: _, düzel_isGouvernedBy__: true, düzel_isGouvernedBy___DERIV: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

66- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [düzelmesi, için, Allah'a ,.. ]

B0Lemma: _, B0POS: Noun, B0Token: düzelmesi, B1Lemma: için, B1POS: Postp, B1Token: için, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

67- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [düzelmesi]   B= [için, Allah'a, dua ,.. ]

B0Lemma: için, B0POS: Postp, B0Token: için, B1Lemma: Allah, B1POS: Noun, B1Token: Allah'a, S0B0Distance: 1, S0B0Lemma: __için, S0B0LemmaPOS: __Postp, S0B0POS: Noun_Postp, S0B0POSLemma: Noun_için, S0B0Token: düzelmesi_için, S0B1Lemma: __Allah, S0B1LemmaPOS: __Noun, S0B1POS: Noun_Noun, S0B1POSLemma: Noun_Allah, S0B1Token: düzelmesi_Allah'a, S0Lemma: _, S0POS: Noun, S0Token: düzelmesi, __isGouvernedBy_için: true, __isGouvernedBy_için_ARGUMENT: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

68- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [için, Allah'a, dua ,.. ]

B0Lemma: için, B0POS: Postp, B0Token: için, B1Lemma: Allah, B1POS: Noun, B1Token: Allah'a, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

69- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [için]   B= [Allah'a, dua, ediyorum ,.. ]

B0Lemma: Allah, B0POS: Noun, B0Token: Allah'a, B1Lemma: dua, B1POS: Noun, B1Token: dua, S0B0Distance: 1, S0B0Lemma: için_Allah, S0B0LemmaPOS: için_Noun, S0B0POS: Postp_Noun, S0B0POSLemma: Postp_Allah, S0B0Token: için_Allah'a, S0B1Lemma: için_dua, S0B1LemmaPOS: için_Noun, S0B1POS: Postp_Noun, S0B1POSLemma: Postp_dua, S0B1Token: için_dua, S0Lemma: için, S0POS: Postp, S0Token: için, için_isGouvernedBy_et: true, için_isGouvernedBy_et_MODIFIER: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

70- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Allah'a, dua, ediyorum ,.. ]

B0Lemma: Allah, B0POS: Noun, B0Token: Allah'a, B1Lemma: dua, B1POS: Noun, B1Token: dua, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

71- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Allah'a]   B= [dua, ediyorum, . ,.. ]

Allah_isGouvernedBy_et: true, Allah_isGouvernedBy_et_MODIFIER: true, B0Lemma: dua, B0POS: Noun, B0Token: dua, B1Lemma: et, B1POS: Verb, B1Token: ediyorum, S0B0Distance: 1, S0B0Lemma: Allah_dua, S0B0LemmaPOS: Allah_Noun, S0B0POS: Noun_Noun, S0B0POSLemma: Noun_dua, S0B0Token: Allah'a_dua, S0B1Lemma: Allah_et, S0B1LemmaPOS: Allah_Verb, S0B1POS: Noun_Verb, S0B1POSLemma: Noun_et, S0B1Token: Allah'a_ediyorum, S0Lemma: Allah, S0POS: Noun, S0Token: Allah'a, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

72- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [dua, ediyorum, . ,.. ]

B0Lemma: dua, B0POS: Noun, B0Token: dua, B1Lemma: et, B1POS: Verb, B1Token: ediyorum, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

73- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [dua]   B= [ediyorum, ., Erbakan ,.. ]

B0Lemma: et, B0POS: Verb, B0Token: ediyorum, B1Lemma: ., B1POS: Punc, B1Token: ., S0B0Distance: 1, S0B0Lemma: dua_et, S0B0LemmaPOS: dua_Verb, S0B0POS: Noun_Verb, S0B0POSLemma: Noun_et, S0B0Token: dua_ediyorum, S0B1Lemma: dua_., S0B1LemmaPOS: dua_Punc, S0B1POS: Noun_Punc, S0B1POSLemma: Noun_., S0B1Token: dua_., S0Lemma: dua, S0POS: Noun, S0Token: dua, dua_isGouvernedBy_et: true, dua_isGouvernedBy_et_MWE: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

74- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [dua, ediyorum]   B= [., Erbakan, bukalemun ,.. ]

B0Lemma: ., B0POS: Punc, B0Token: ., B1Lemma: Erbakan, B1POS: Noun, B1Token: Erbakan, S0B0Distance: 1, S0B0Lemma: et_., S0B0LemmaPOS: et_Punc, S0B0POS: Verb_Punc, S0B0POSLemma: Verb_., S0B0Token: ediyorum_., S0B1Lemma: et_Erbakan, S0B1LemmaPOS: et_Noun, S0B1POS: Verb_Noun, S0B1POSLemma: Verb_Erbakan, S0B1Token: ediyorum_Erbakan, S0Lemma: et, S0POS: Verb, S0Token: ediyorum, S1B0Lemma: dua_., S1B0LemmaPOS: dua_Punc, S1B0POS: Noun_Punc, S1B0POSLemma: Noun_., S1B0Token: dua_., S1Lemma: dua, S1POS: Noun, S1S0Lemma: dua_et, S1S0LemmaPOS: dua_Verb, S1S0POS: Noun_Verb, S1S0POSLemma: Noun_et, S1S0Token: dua_ediyorum, S1Token: dua, SyntaxicRelation: -MWE, et_._hasRighDep_PUNCTUATION: true, et_hasRighDep_PUNCTUATION: true, et_isGouvernedBy_değiş: true, et_isGouvernedBy_değiş_COORDINATION: true, hasRighDep_PUNCTUATION: true, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

75- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[dua, ediyorum]]   B= [., Erbakan, bukalemun ,.. ]

B0Lemma: ., B0POS: Punc, B0Token: ., B1Lemma: Erbakan, B1POS: Noun, B1Token: Erbakan, S0B0Distance: 1, S0B0Lemma: dua_et_., S0B0LemmaPOS: dua_et_Punc, S0B0POS: Noun_Verb_Punc, S0B0POSLemma: Noun_Verb_., S0B0Token: dua_ediyorum_., S0B1Lemma: dua_et_Erbakan, S0B1LemmaPOS: dua_et_Noun, S0B1POS: Noun_Verb_Noun, S0B1POSLemma: Noun_Verb_Erbakan, S0B1Token: dua_ediyorum_Erbakan, S0Lemma: dua_et, S0POS: Noun_Verb, S0Token: dua_ediyorum, transitionHistoryLength1: 0, transitionHistoryLength2: 00, transitionHistoryLength3: 002, 

76- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [., Erbakan, bukalemun ,.. ]

B0Lemma: ., B0POS: Punc, B0Token: ., B1Lemma: Erbakan, B1POS: Noun, B1Token: Erbakan, transitionHistoryLength1: 1, transitionHistoryLength2: 10, transitionHistoryLength3: 100, 

77- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [Erbakan, bukalemun, gibi ,.. ]

B0Lemma: Erbakan, B0POS: Noun, B0Token: Erbakan, B1Lemma: bukalemun, B1POS: Noun, B1Token: bukalemun, S0B0Distance: 1, S0B0Lemma: ._Erbakan, S0B0LemmaPOS: ._Noun, S0B0POS: Punc_Noun, S0B0POSLemma: Punc_Erbakan, S0B0Token: ._Erbakan, S0B1Lemma: ._bukalemun, S0B1LemmaPOS: ._Noun, S0B1POS: Punc_Noun, S0B1POSLemma: Punc_bukalemun, S0B1Token: ._bukalemun, S0Lemma: ., S0POS: Punc, S0Token: ., transitionHistoryLength1: 2, transitionHistoryLength2: 21, transitionHistoryLength3: 210, 

78- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Erbakan, bukalemun, gibi ,.. ]

B0Lemma: Erbakan, B0POS: Noun, B0Token: Erbakan, B1Lemma: bukalemun, B1POS: Noun, B1Token: bukalemun, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 021, 

79- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Erbakan]   B= [bukalemun, gibi, yön ,.. ]

B0Lemma: bukalemun, B0POS: Noun, B0Token: bukalemun, B1Lemma: gibi, B1POS: Postp, B1Token: gibi, Erbakan_isGouvernedBy_değiş: true, Erbakan_isGouvernedBy_değiş_SUBJECT: true, S0B0Distance: 1, S0B0Lemma: Erbakan_bukalemun, S0B0LemmaPOS: Erbakan_Noun, S0B0POS: Noun_Noun, S0B0POSLemma: Noun_bukalemun, S0B0Token: Erbakan_bukalemun, S0B1Lemma: Erbakan_gibi, S0B1LemmaPOS: Erbakan_Postp, S0B1POS: Noun_Postp, S0B1POSLemma: Noun_gibi, S0B1Token: Erbakan_gibi, S0Lemma: Erbakan, S0POS: Noun, S0Token: Erbakan, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

80- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [bukalemun, gibi, yön ,.. ]

B0Lemma: bukalemun, B0POS: Noun, B0Token: bukalemun, B1Lemma: gibi, B1POS: Postp, B1Token: gibi, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

81- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [bukalemun]   B= [gibi, yön, değiştiriyor ,.. ]

B0Lemma: gibi, B0POS: Postp, B0Token: gibi, B1Lemma: yön, B1POS: Noun, B1Token: yön, S0B0Distance: 1, S0B0Lemma: bukalemun_gibi, S0B0LemmaPOS: bukalemun_Postp, S0B0POS: Noun_Postp, S0B0POSLemma: Noun_gibi, S0B0Token: bukalemun_gibi, S0B1Lemma: bukalemun_yön, S0B1LemmaPOS: bukalemun_Noun, S0B1POS: Noun_Noun, S0B1POSLemma: Noun_yön, S0B1Token: bukalemun_yön, S0Lemma: bukalemun, S0POS: Noun, S0Token: bukalemun, bukalemun_isGouvernedBy_gibi: true, bukalemun_isGouvernedBy_gibi_ARGUMENT: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

82- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [gibi, yön, değiştiriyor ,.. ]

B0Lemma: gibi, B0POS: Postp, B0Token: gibi, B1Lemma: yön, B1POS: Noun, B1Token: yön, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

83- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [gibi]   B= [yön, değiştiriyor, ' ,.. ]

B0Lemma: yön, B0POS: Noun, B0Token: yön, B1Lemma: değiş, B1POS: Verb, B1Token: değiştiriyor, S0B0Distance: 1, S0B0Lemma: gibi_yön, S0B0LemmaPOS: gibi_Noun, S0B0POS: Postp_Noun, S0B0POSLemma: Postp_yön, S0B0Token: gibi_yön, S0B1Lemma: gibi_değiş, S0B1LemmaPOS: gibi_Verb, S0B1POS: Postp_Verb, S0B1POSLemma: Postp_değiş, S0B1Token: gibi_değiştiriyor, S0Lemma: gibi, S0POS: Postp, S0Token: gibi, gibi_isGouvernedBy_değiş: true, gibi_isGouvernedBy_değiş_MODIFIER: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

84- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [yön, değiştiriyor, ' ,.. ]

B0Lemma: yön, B0POS: Noun, B0Token: yön, B1Lemma: değiş, B1POS: Verb, B1Token: değiştiriyor, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

85- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [yön]   B= [değiştiriyor, ', yanıtını ,.. ]

B0Lemma: değiş, B0POS: Verb, B0Token: değiştiriyor, B1Lemma: ', B1POS: Punc, B1Token: ', S0B0Distance: 1, S0B0Lemma: yön_değiş, S0B0LemmaPOS: yön_Verb, S0B0POS: Noun_Verb, S0B0POSLemma: Noun_değiş, S0B0Token: yön_değiştiriyor, S0B1Lemma: yön_', S0B1LemmaPOS: yön_Punc, S0B1POS: Noun_Punc, S0B1POSLemma: Noun_', S0B1Token: yön_', S0Lemma: yön, S0POS: Noun, S0Token: yön, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, yön_isGouvernedBy_değiş: true, yön_isGouvernedBy_değiş_OBJECT: true, 

86- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [değiştiriyor, ', yanıtını ,.. ]

B0Lemma: değiş, B0POS: Verb, B0Token: değiştiriyor, B1Lemma: ', B1POS: Punc, B1Token: ', transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

87- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [değiştiriyor]   B= [', yanıtını, verdi ,.. ]

B0Lemma: ', B0POS: Punc, B0Token: ', B1Lemma: yanıt, B1POS: Noun, B1Token: yanıtını, S0B0Distance: 1, S0B0Lemma: değiş_', S0B0LemmaPOS: değiş_Punc, S0B0POS: Verb_Punc, S0B0POSLemma: Verb_', S0B0Token: değiştiriyor_', S0B1Lemma: değiş_yanıt, S0B1LemmaPOS: değiş_Noun, S0B1POS: Verb_Noun, S0B1POSLemma: Verb_yanıt, S0B1Token: değiştiriyor_yanıtını, S0Lemma: değiş, S0POS: Verb, S0Token: değiştiriyor, değiş_'_hasRighDep_PUNCTUATION: true, değiş_hasRighDep_PUNCTUATION: true, değiş_isGouvernedBy_ver: true, değiş_isGouvernedBy_ver_COORDINATION: true, hasRighDep_PUNCTUATION: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

88- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [', yanıtını, verdi ,.. ]

B0Lemma: ', B0POS: Punc, B0Token: ', B1Lemma: yanıt, B1POS: Noun, B1Token: yanıtını, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

89- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [']   B= [yanıtını, verdi, . ,.. ]

B0Lemma: yanıt, B0POS: Noun, B0Token: yanıtını, B1Lemma: ver, B1POS: Verb, B1Token: verdi, S0B0Distance: 1, S0B0Lemma: '_yanıt, S0B0LemmaPOS: '_Noun, S0B0POS: Punc_Noun, S0B0POSLemma: Punc_yanıt, S0B0Token: '_yanıtını, S0B1Lemma: '_ver, S0B1LemmaPOS: '_Verb, S0B1POS: Punc_Verb, S0B1POSLemma: Punc_ver, S0B1Token: '_verdi, S0Lemma: ', S0POS: Punc, S0Token: ', transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

90- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [yanıtını, verdi, . ,.. ]

B0Lemma: yanıt, B0POS: Noun, B0Token: yanıtını, B1Lemma: ver, B1POS: Verb, B1Token: verdi, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

91- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [yanıtını]   B= [verdi, ., Erbakan'ı ,.. ]

B0Lemma: ver, B0POS: Verb, B0Token: verdi, B1Lemma: ., B1POS: Punc, B1Token: ., S0B0Distance: 1, S0B0Lemma: yanıt_ver, S0B0LemmaPOS: yanıt_Verb, S0B0POS: Noun_Verb, S0B0POSLemma: Noun_ver, S0B0Token: yanıtını_verdi, S0B1Lemma: yanıt_., S0B1LemmaPOS: yanıt_Punc, S0B1POS: Noun_Punc, S0B1POSLemma: Noun_., S0B1Token: yanıtını_., S0Lemma: yanıt, S0POS: Noun, S0Token: yanıtını, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, yanıt_isGouvernedBy_ver: true, yanıt_isGouvernedBy_ver_MWE: true, 

92- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [verdi, ., Erbakan'ı ,.. ]

B0Lemma: ver, B0POS: Verb, B0Token: verdi, B1Lemma: ., B1POS: Punc, B1Token: ., transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

93- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [verdi]   B= [., Erbakan'ı, yalancı ,.. ]

B0Lemma: ., B0POS: Punc, B0Token: ., B1Lemma: Erbakan, B1POS: Noun, B1Token: Erbakan'ı, S0B0Distance: 1, S0B0Lemma: ver_., S0B0LemmaPOS: ver_Punc, S0B0POS: Verb_Punc, S0B0POSLemma: Verb_., S0B0Token: verdi_., S0B1Lemma: ver_Erbakan, S0B1LemmaPOS: ver_Noun, S0B1POS: Verb_Noun, S0B1POSLemma: Verb_Erbakan, S0B1Token: verdi_Erbakan'ı, S0Lemma: ver, S0POS: Verb, S0Token: verdi, hasRighDep_PUNCTUATION: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, ver_._hasRighDep_PUNCTUATION: true, ver_hasRighDep_PUNCTUATION: true, ver_isGouvernedBy_gör: true, ver_isGouvernedBy_gör_COORDINATION: true, 

94- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [., Erbakan'ı, yalancı ,.. ]

B0Lemma: ., B0POS: Punc, B0Token: ., B1Lemma: Erbakan, B1POS: Noun, B1Token: Erbakan'ı, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

95- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [Erbakan'ı, yalancı, ve ,.. ]

B0Lemma: Erbakan, B0POS: Noun, B0Token: Erbakan'ı, B1Lemma: yalancı, B1POS: Noun, B1Token: yalancı, S0B0Distance: 1, S0B0Lemma: ._Erbakan, S0B0LemmaPOS: ._Noun, S0B0POS: Punc_Noun, S0B0POSLemma: Punc_Erbakan, S0B0Token: ._Erbakan'ı, S0B1Lemma: ._yalancı, S0B1LemmaPOS: ._Noun, S0B1POS: Punc_Noun, S0B1POSLemma: Punc_yalancı, S0B1Token: ._yalancı, S0Lemma: ., S0POS: Punc, S0Token: ., transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

96- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Erbakan'ı, yalancı, ve ,.. ]

B0Lemma: Erbakan, B0POS: Noun, B0Token: Erbakan'ı, B1Lemma: yalancı, B1POS: Noun, B1Token: yalancı, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

97- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Erbakan'ı]   B= [yalancı, ve, iktidar ,.. ]

B0Lemma: yalancı, B0POS: Noun, B0Token: yalancı, B1Lemma: ve, B1POS: Conj, B1Token: ve, Erbakan_isGouvernedBy_ol: true, Erbakan_isGouvernedBy_ol_OBJECT: true, S0B0Distance: 1, S0B0Lemma: Erbakan_yalancı, S0B0LemmaPOS: Erbakan_Noun, S0B0POS: Noun_Noun, S0B0POSLemma: Noun_yalancı, S0B0Token: Erbakan'ı_yalancı, S0B1Lemma: Erbakan_ve, S0B1LemmaPOS: Erbakan_Conj, S0B1POS: Noun_Conj, S0B1POSLemma: Noun_ve, S0B1Token: Erbakan'ı_ve, S0Lemma: Erbakan, S0POS: Noun, S0Token: Erbakan'ı, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

98- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [yalancı, ve, iktidar ,.. ]

B0Lemma: yalancı, B0POS: Noun, B0Token: yalancı, B1Lemma: ve, B1POS: Conj, B1Token: ve, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

99- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [yalancı]   B= [ve, iktidar, _ ,.. ]

B0Lemma: ve, B0POS: Conj, B0Token: ve, B1Lemma: iktidar, B1POS: Noun, B1Token: iktidar, S0B0Distance: 1, S0B0Lemma: yalancı_ve, S0B0LemmaPOS: yalancı_Conj, S0B0POS: Noun_Conj, S0B0POSLemma: Noun_ve, S0B0Token: yalancı_ve, S0B1Lemma: yalancı_iktidar, S0B1LemmaPOS: yalancı_Noun, S0B1POS: Noun_Noun, S0B1POSLemma: Noun_iktidar, S0B1Token: yalancı_iktidar, S0Lemma: yalancı, S0POS: Noun, S0Token: yalancı, hasRighDep_CONJUNCTION: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, yalancı_hasRighDep_CONJUNCTION: true, yalancı_isGouvernedBy_iktidar: true, yalancı_isGouvernedBy_iktidar_COORDINATION: true, yalancı_ve_hasRighDep_CONJUNCTION: true, 

100- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ve, iktidar, _ ,.. ]

B0Lemma: ve, B0POS: Conj, B0Token: ve, B1Lemma: iktidar, B1POS: Noun, B1Token: iktidar, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

101- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ve]   B= [iktidar, _, olmak ,.. ]

B0Lemma: iktidar, B0POS: Noun, B0Token: iktidar, B1Lemma: ol, B1POS: Verb, B1Token: _, S0B0Distance: 1, S0B0Lemma: ve_iktidar, S0B0LemmaPOS: ve_Noun, S0B0POS: Conj_Noun, S0B0POSLemma: Conj_iktidar, S0B0Token: ve_iktidar, S0B1Lemma: ve_ol, S0B1LemmaPOS: ve_Verb, S0B1POS: Conj_Verb, S0B1POSLemma: Conj_ol, S0B1Token: ve__, S0Lemma: ve, S0POS: Conj, S0Token: ve, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

102- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [iktidar, _, olmak ,.. ]

B0Lemma: iktidar, B0POS: Noun, B0Token: iktidar, B1Lemma: ol, B1POS: Verb, B1Token: _, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

103- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [iktidar]   B= [_, olmak, için ,.. ]

B0Lemma: ol, B0POS: Verb, B0Token: _, B1Lemma: _, B1POS: Noun, B1Token: olmak, S0B0Distance: 1, S0B0Lemma: iktidar_ol, S0B0LemmaPOS: iktidar_Verb, S0B0POS: Noun_Verb, S0B0POSLemma: Noun_ol, S0B0Token: iktidar__, S0B1Lemma: iktidar__, S0B1LemmaPOS: iktidar_Noun, S0B1POS: Noun_Noun, S0B1POSLemma: Noun__, S0B1Token: iktidar_olmak, S0Lemma: iktidar, S0POS: Noun, S0Token: iktidar, iktidar_isGouvernedBy_ol: true, iktidar_isGouvernedBy_ol_OBJECT: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

104- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [_, olmak, için ,.. ]

B0Lemma: ol, B0POS: Verb, B0Token: _, B1Lemma: _, B1POS: Noun, B1Token: olmak, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

105- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [_]   B= [olmak, için, dini ,.. ]

B0Lemma: _, B0POS: Noun, B0Token: olmak, B1Lemma: için, B1POS: Postp, B1Token: için, S0B0Distance: 1, S0B0Lemma: ol__, S0B0LemmaPOS: ol_Noun, S0B0POS: Verb_Noun, S0B0POSLemma: Verb__, S0B0Token: __olmak, S0B1Lemma: ol_için, S0B1LemmaPOS: ol_Postp, S0B1POS: Verb_Postp, S0B1POSLemma: Verb_için, S0B1Token: __için, S0Lemma: ol, S0POS: Verb, S0Token: _, ol_isGouvernedBy__: true, ol_isGouvernedBy___DERIV: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

106- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [olmak, için, dini ,.. ]

B0Lemma: _, B0POS: Noun, B0Token: olmak, B1Lemma: için, B1POS: Postp, B1Token: için, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

107- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [olmak]   B= [için, dini, alet ,.. ]

B0Lemma: için, B0POS: Postp, B0Token: için, B1Lemma: dini, B1POS: Adj, B1Token: dini, S0B0Distance: 1, S0B0Lemma: __için, S0B0LemmaPOS: __Postp, S0B0POS: Noun_Postp, S0B0POSLemma: Noun_için, S0B0Token: olmak_için, S0B1Lemma: __dini, S0B1LemmaPOS: __Adj, S0B1POS: Noun_Adj, S0B1POSLemma: Noun_dini, S0B1Token: olmak_dini, S0Lemma: _, S0POS: Noun, S0Token: olmak, __isGouvernedBy_için: true, __isGouvernedBy_için_ARGUMENT: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

108- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [için, dini, alet ,.. ]

B0Lemma: için, B0POS: Postp, B0Token: için, B1Lemma: dini, B1POS: Adj, B1Token: dini, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

109- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [için]   B= [dini, alet, _ ,.. ]

B0Lemma: dini, B0POS: Adj, B0Token: dini, B1Lemma: alet, B1POS: Noun, B1Token: alet, S0B0Distance: 1, S0B0Lemma: için_dini, S0B0LemmaPOS: için_Adj, S0B0POS: Postp_Adj, S0B0POSLemma: Postp_dini, S0B0Token: için_dini, S0B1Lemma: için_alet, S0B1LemmaPOS: için_Noun, S0B1POS: Postp_Noun, S0B1POSLemma: Postp_alet, S0B1Token: için_alet, S0Lemma: için, S0POS: Postp, S0Token: için, için_isGouvernedBy_et: true, için_isGouvernedBy_et_MODIFIER: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

110- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [dini, alet, _ ,.. ]

B0Lemma: dini, B0POS: Adj, B0Token: dini, B1Lemma: alet, B1POS: Noun, B1Token: alet, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

111- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [dini]   B= [alet, _, eden ,.. ]

B0Lemma: alet, B0POS: Noun, B0Token: alet, B1Lemma: et, B1POS: Verb, B1Token: _, S0B0Distance: 1, S0B0Lemma: dini_alet, S0B0LemmaPOS: dini_Noun, S0B0POS: Adj_Noun, S0B0POSLemma: Adj_alet, S0B0Token: dini_alet, S0B1Lemma: dini_et, S0B1LemmaPOS: dini_Verb, S0B1POS: Adj_Verb, S0B1POSLemma: Adj_et, S0B1Token: dini__, S0Lemma: dini, S0POS: Adj, S0Token: dini, dini_isGouvernedBy_et: true, dini_isGouvernedBy_et_MODIFIER: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

112- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [alet, _, eden ,.. ]

B0Lemma: alet, B0POS: Noun, B0Token: alet, B1Lemma: et, B1POS: Verb, B1Token: _, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

113- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [alet]   B= [_, eden, bir ,.. ]

B0Lemma: et, B0POS: Verb, B0Token: _, B1Lemma: _, B1POS: Adj, B1Token: eden, S0B0Distance: 1, S0B0Lemma: alet_et, S0B0LemmaPOS: alet_Verb, S0B0POS: Noun_Verb, S0B0POSLemma: Noun_et, S0B0Token: alet__, S0B1Lemma: alet__, S0B1LemmaPOS: alet_Adj, S0B1POS: Noun_Adj, S0B1POSLemma: Noun__, S0B1Token: alet_eden, S0Lemma: alet, S0POS: Noun, S0Token: alet, alet_isGouvernedBy_et: true, alet_isGouvernedBy_et_MWE: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

114- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [_, eden, bir ,.. ]

B0Lemma: et, B0POS: Verb, B0Token: _, B1Lemma: _, B1POS: Adj, B1Token: eden, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

115- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [_]   B= [eden, bir, insan ,.. ]

B0Lemma: _, B0POS: Adj, B0Token: eden, B1Lemma: bir, B1POS: Adj, B1Token: bir, S0B0Distance: 1, S0B0Lemma: et__, S0B0LemmaPOS: et_Adj, S0B0POS: Verb_Adj, S0B0POSLemma: Verb__, S0B0Token: __eden, S0B1Lemma: et_bir, S0B1LemmaPOS: et_Adj, S0B1POS: Verb_Adj, S0B1POSLemma: Verb_bir, S0B1Token: __bir, S0Lemma: et, S0POS: Verb, S0Token: _, et_isGouvernedBy__: true, et_isGouvernedBy___DERIV: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

116- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [eden, bir, insan ,.. ]

B0Lemma: _, B0POS: Adj, B0Token: eden, B1Lemma: bir, B1POS: Adj, B1Token: bir, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

117- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [eden]   B= [bir, insan, olarak ,.. ]

B0Lemma: bir, B0POS: Adj, B0Token: bir, B1Lemma: insan, B1POS: Noun, B1Token: insan, S0B0Distance: 1, S0B0Lemma: __bir, S0B0LemmaPOS: __Adj, S0B0POS: Adj_Adj, S0B0POSLemma: Adj_bir, S0B0Token: eden_bir, S0B1Lemma: __insan, S0B1LemmaPOS: __Noun, S0B1POS: Adj_Noun, S0B1POSLemma: Adj_insan, S0B1Token: eden_insan, S0Lemma: _, S0POS: Adj, S0Token: eden, __isGouvernedBy_insan: true, __isGouvernedBy_insan_MODIFIER: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

118- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [bir, insan, olarak ,.. ]

B0Lemma: bir, B0POS: Adj, B0Token: bir, B1Lemma: insan, B1POS: Noun, B1Token: insan, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

119- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [bir]   B= [insan, olarak, görüyordu ,.. ]

B0Lemma: insan, B0POS: Noun, B0Token: insan, B1Lemma: olarak, B1POS: Postp, B1Token: olarak, S0B0Distance: 1, S0B0Lemma: bir_insan, S0B0LemmaPOS: bir_Noun, S0B0POS: Adj_Noun, S0B0POSLemma: Adj_insan, S0B0Token: bir_insan, S0B1Lemma: bir_olarak, S0B1LemmaPOS: bir_Postp, S0B1POS: Adj_Postp, S0B1POSLemma: Adj_olarak, S0B1Token: bir_olarak, S0Lemma: bir, S0POS: Adj, S0Token: bir, bir_isGouvernedBy_insan: true, bir_isGouvernedBy_insan_DETERMINER: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

120- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [insan, olarak, görüyordu ,.. ]

B0Lemma: insan, B0POS: Noun, B0Token: insan, B1Lemma: olarak, B1POS: Postp, B1Token: olarak, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

121- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [insan]   B= [olarak, görüyordu, " ,.. ]

B0Lemma: olarak, B0POS: Postp, B0Token: olarak, B1Lemma: gör, B1POS: Verb, B1Token: görüyordu, S0B0Distance: 1, S0B0Lemma: insan_olarak, S0B0LemmaPOS: insan_Postp, S0B0POS: Noun_Postp, S0B0POSLemma: Noun_olarak, S0B0Token: insan_olarak, S0B1Lemma: insan_gör, S0B1LemmaPOS: insan_Verb, S0B1POS: Noun_Verb, S0B1POSLemma: Noun_gör, S0B1Token: insan_görüyordu, S0Lemma: insan, S0POS: Noun, S0Token: insan, insan_isGouvernedBy_olarak: true, insan_isGouvernedBy_olarak_ARGUMENT: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

122- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [olarak, görüyordu, " ,.. ]

B0Lemma: olarak, B0POS: Postp, B0Token: olarak, B1Lemma: gör, B1POS: Verb, B1Token: görüyordu, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

123- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [olarak]   B= [görüyordu, ", diye ,.. ]

B0Lemma: gör, B0POS: Verb, B0Token: görüyordu, B1Lemma: ", B1POS: Punc, B1Token: ", S0B0Distance: 1, S0B0Lemma: olarak_gör, S0B0LemmaPOS: olarak_Verb, S0B0POS: Postp_Verb, S0B0POSLemma: Postp_gör, S0B0Token: olarak_görüyordu, S0B1Lemma: olarak_", S0B1LemmaPOS: olarak_Punc, S0B1POS: Postp_Punc, S0B1POSLemma: Postp_", S0B1Token: olarak_", S0Lemma: olarak, S0POS: Postp, S0Token: olarak, olarak_isGouvernedBy_gör: true, olarak_isGouvernedBy_gör_MODIFIER: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

124- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [görüyordu, ", diye ,.. ]

B0Lemma: gör, B0POS: Verb, B0Token: görüyordu, B1Lemma: ", B1POS: Punc, B1Token: ", transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

125- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [görüyordu]   B= [", diye, konuştu ,.. ]

B0Lemma: ", B0POS: Punc, B0Token: ", B1Lemma: diye, B1POS: Postp, B1Token: diye, S0B0Distance: 1, S0B0Lemma: gör_", S0B0LemmaPOS: gör_Punc, S0B0POS: Verb_Punc, S0B0POSLemma: Verb_", S0B0Token: görüyordu_", S0B1Lemma: gör_diye, S0B1LemmaPOS: gör_Postp, S0B1POS: Verb_Postp, S0B1POSLemma: Verb_diye, S0B1Token: görüyordu_diye, S0Lemma: gör, S0POS: Verb, S0Token: görüyordu, gör_"_hasRighDep_PUNCTUATION: true, gör_hasRighDep_PUNCTUATION: true, gör_isGouvernedBy_diye: true, gör_isGouvernedBy_diye_ARGUMENT: true, hasRighDep_PUNCTUATION: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

126- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [", diye, konuştu ,.. ]

B0Lemma: ", B0POS: Punc, B0Token: ", B1Lemma: diye, B1POS: Postp, B1Token: diye, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

127- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= ["]   B= [diye, konuştu, . ,.. ]

B0Lemma: diye, B0POS: Postp, B0Token: diye, B1Lemma: konuş, B1POS: Verb, B1Token: konuştu, S0B0Distance: 1, S0B0Lemma: "_diye, S0B0LemmaPOS: "_Postp, S0B0POS: Punc_Postp, S0B0POSLemma: Punc_diye, S0B0Token: "_diye, S0B1Lemma: "_konuş, S0B1LemmaPOS: "_Verb, S0B1POS: Punc_Verb, S0B1POSLemma: Punc_konuş, S0B1Token: "_konuştu, S0Lemma: ", S0POS: Punc, S0Token: ", transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

128- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [diye, konuştu, . ,.. ]

B0Lemma: diye, B0POS: Postp, B0Token: diye, B1Lemma: konuş, B1POS: Verb, B1Token: konuştu, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

129- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [diye]   B= [konuştu, . ,.. ]

B0Lemma: konuş, B0POS: Verb, B0Token: konuştu, B1Lemma: ., B1POS: Punc, B1Token: ., S0B0Distance: 1, S0B0Lemma: diye_konuş, S0B0LemmaPOS: diye_Verb, S0B0POS: Postp_Verb, S0B0POSLemma: Postp_konuş, S0B0Token: diye_konuştu, S0B1Lemma: diye_., S0B1LemmaPOS: diye_Punc, S0B1POS: Postp_Punc, S0B1POSLemma: Postp_., S0B1Token: diye_., S0Lemma: diye, S0POS: Postp, S0Token: diye, diye_isGouvernedBy_konuş: true, diye_isGouvernedBy_konuş_MODIFIER: true, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

130- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [konuştu, . ,.. ]

B0Lemma: konuş, B0POS: Verb, B0Token: konuştu, B1Lemma: ., B1POS: Punc, B1Token: ., transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

131- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [konuştu]   B= [.]

B0Lemma: ., B0POS: Punc, B0Token: ., S0B0Distance: 1, S0B0Lemma: konuş_., S0B0LemmaPOS: konuş_Punc, S0B0POS: Verb_Punc, S0B0POSLemma: Verb_., S0B0Token: konuştu_., S0Lemma: konuş, S0POS: Verb, S0Token: konuştu, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

132- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [.]

B0Lemma: ., B0POS: Punc, B0Token: ., transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

133- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [ ]

S0Lemma: ., S0POS: Punc, S0Token: ., transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

134- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

