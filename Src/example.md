## Sentence No. 543 - 
dá se předpokládat , že firma , která **si** **dá** **záležet** na kvalitním zpracování prospektu , **bude** také **věnovat** dobrou **péči** vám . 
### Existing MWEs: 
1- **si dá záležet** (ID)

2- **si dá** (IReflV), Embedded

3- **bude věnovat péči** (LVC)




0- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [dá, se, předpokládat ,.. ]



1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [dá]   B= [se, předpokládat, , ,.. ]



2- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [se, předpokládat, , ,.. ]



3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [se]   B= [předpokládat, ,, že ,.. ]



4- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [předpokládat, ,, že ,.. ]



5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [předpokládat]   B= [,, že, firma ,.. ]



6- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, že, firma ,.. ]



7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [že, firma, , ,.. ]



8- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [že, firma, , ,.. ]



9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [že]   B= [firma, ,, která ,.. ]



10- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [firma, ,, která ,.. ]



11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [firma]   B= [,, která, si ,.. ]



12- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, která, si ,.. ]



13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [která, si, dá ,.. ]



14- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [která, si, dá ,.. ]



15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [která]   B= [si, dá, záležet ,.. ]



16- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [si, dá, záležet ,.. ]



17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [si]   B= [dá, záležet, na ,.. ]



18- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [si, dá]   B= [záležet, na, kvalitním ,.. ]



19- **MERGE_AS_IReflV**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[si, dá]]   B= [záležet, na, kvalitním ,.. ]



20- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[si, dá]  záležet]   B= [na, kvalitním, zpracování ,.. ]



21- **MERGE_AS_ID**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[[si, dá]  záležet]]   B= [na, kvalitním, zpracování ,.. ]



22- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [na, kvalitním, zpracování ,.. ]



23- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [na]   B= [kvalitním, zpracování, prospektu ,.. ]



24- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [kvalitním, zpracování, prospektu ,.. ]



25- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [kvalitním]   B= [zpracování, prospektu, , ,.. ]



26- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [zpracování, prospektu, , ,.. ]



27- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [zpracování]   B= [prospektu, ,, bude ,.. ]



28- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [prospektu, ,, bude ,.. ]



29- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [prospektu]   B= [,, bude, také ,.. ]



30- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, bude, také ,.. ]



31- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [bude, také, věnovat ,.. ]



32- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [bude, také, věnovat ,.. ]



33- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [bude]   B= [také, věnovat, dobrou ,.. ]



34- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [bude, také]   B= [věnovat, dobrou, péči ,.. ]



35- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [bude]   B= [věnovat, dobrou, péči ,.. ]



36- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [bude, věnovat]   B= [dobrou, péči, vám ,.. ]



37- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [bude, věnovat, dobrou]   B= [péči, vám, . ,.. ]



38- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [bude, věnovat]   B= [péči, vám, . ,.. ]



39- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [bude, věnovat, péči]   B= [vám, . ,.. ]



40- WHITE_MERGE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [bude, [věnovat, péči]]   B= [vám, . ,.. ]



41- **MERGE_AS_LVC**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[bude, [věnovat, péči]]]   B= [vám, . ,.. ]



42- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [vám, . ,.. ]



43- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [vám]   B= [.]



44- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [.]



45- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [ ]



46- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]


## Sentence No. 1148 - 
není nic logičtějšího , než použít osobní atestace jednotlivých vědců k tomu , aby jim na následující období do další atestace byly přiděleny osobní operační granty ve výši , která **by** **se** stejně jako **zvýšení** či **snížení** **platu** **řídila** zhodnocením jejich práce za uplynulé období . 
### Existing MWEs: 
1- **by se řídila** (IReflV)

2- **se řídila** (IReflV), Embedded

3- **zvýšení platu** (LVC)

4- **snížení platu** (LVC), Interleaving 




0- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [není, nic, logičtějšího ,.. ]



1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [není]   B= [nic, logičtějšího, , ,.. ]



2- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [nic, logičtějšího, , ,.. ]



3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [nic]   B= [logičtějšího, ,, než ,.. ]



4- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [logičtějšího, ,, než ,.. ]



5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [logičtějšího]   B= [,, než, použít ,.. ]



6- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, než, použít ,.. ]



7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [než, použít, osobní ,.. ]



8- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [než, použít, osobní ,.. ]



9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [než]   B= [použít, osobní, atestace ,.. ]



10- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [použít, osobní, atestace ,.. ]



11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [použít]   B= [osobní, atestace, jednotlivých ,.. ]



12- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [osobní, atestace, jednotlivých ,.. ]



13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [osobní]   B= [atestace, jednotlivých, vědců ,.. ]



14- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [atestace, jednotlivých, vědců ,.. ]



15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [atestace]   B= [jednotlivých, vědců, k ,.. ]



16- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [jednotlivých, vědců, k ,.. ]



17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [jednotlivých]   B= [vědců, k, tomu ,.. ]



18- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [vědců, k, tomu ,.. ]



19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [vědců]   B= [k, tomu, , ,.. ]



20- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [k, tomu, , ,.. ]



21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [k]   B= [tomu, ,, aby ,.. ]



22- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [tomu, ,, aby ,.. ]



23- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [tomu]   B= [,, aby, jim ,.. ]



24- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, aby, jim ,.. ]



25- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [aby, jim, na ,.. ]



26- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [aby, jim, na ,.. ]



27- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [aby]   B= [jim, na, následující ,.. ]



28- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [jim, na, následující ,.. ]



29- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [jim]   B= [na, následující, období ,.. ]



30- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [na, následující, období ,.. ]



31- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [na]   B= [následující, období, do ,.. ]



32- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [následující, období, do ,.. ]



33- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [následující]   B= [období, do, další ,.. ]



34- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [období, do, další ,.. ]



35- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [období]   B= [do, další, atestace ,.. ]



36- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [do, další, atestace ,.. ]



37- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [do]   B= [další, atestace, byly ,.. ]



38- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [další, atestace, byly ,.. ]



39- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [další]   B= [atestace, byly, přiděleny ,.. ]



40- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [atestace, byly, přiděleny ,.. ]



41- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [atestace]   B= [byly, přiděleny, osobní ,.. ]



42- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [byly, přiděleny, osobní ,.. ]



43- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [byly]   B= [přiděleny, osobní, operační ,.. ]



44- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [přiděleny, osobní, operační ,.. ]



45- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [přiděleny]   B= [osobní, operační, granty ,.. ]



46- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [osobní, operační, granty ,.. ]



47- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [osobní]   B= [operační, granty, ve ,.. ]



48- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [operační, granty, ve ,.. ]



49- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [operační]   B= [granty, ve, výši ,.. ]



50- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [granty, ve, výši ,.. ]



51- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [granty]   B= [ve, výši, , ,.. ]



52- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ve, výši, , ,.. ]



53- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ve]   B= [výši, ,, která ,.. ]



54- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [výši, ,, která ,.. ]



55- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [výši]   B= [,, která, by ,.. ]



56- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, která, by ,.. ]



57- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [která, by, se ,.. ]



58- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [která, by, se ,.. ]



59- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [která]   B= [by, se, stejně ,.. ]



60- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [by, se, stejně ,.. ]



61- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [by]   B= [se, stejně, jako ,.. ]



62- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [by, se]   B= [stejně, jako, zvýšení ,.. ]



63- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [by, se, stejně]   B= [jako, zvýšení, či ,.. ]



64- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [by, se]   B= [jako, zvýšení, či ,.. ]



65- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [by, se, jako]   B= [zvýšení, či, snížení ,.. ]



66- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [by, se]   B= [zvýšení, či, snížení ,.. ]



67- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [by, se, zvýšení]   B= [či, snížení, platu ,.. ]



68- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [by, se, zvýšení, či]   B= [snížení, platu, řídila ,.. ]



69- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [by, se, zvýšení]   B= [snížení, platu, řídila ,.. ]



70- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [by, se, zvýšení, snížení]   B= [platu, řídila, zhodnocením ,.. ]



71- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [by, se, zvýšení]   B= [platu, řídila, zhodnocením ,.. ]



72- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [by, se, zvýšení, platu]   B= [řídila, zhodnocením, jejich ,.. ]



73- **MERGE_AS_LVC**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [by, se, [zvýšení, platu]]   B= [řídila, zhodnocením, jejich ,.. ]



74- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [by, se]   B= [řídila, zhodnocením, jejich ,.. ]



75- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [by, se, řídila]   B= [zhodnocením, jejich, práce ,.. ]



76- **MERGE_AS_IReflV**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [by, [se, řídila]]   B= [zhodnocením, jejich, práce ,.. ]



77- **MERGE_AS_IReflV**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[by, [se, řídila]]]   B= [zhodnocením, jejich, práce ,.. ]



78- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [zhodnocením, jejich, práce ,.. ]



79- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [zhodnocením]   B= [jejich, práce, za ,.. ]



80- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [jejich, práce, za ,.. ]



81- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [jejich]   B= [práce, za, uplynulé ,.. ]



82- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [práce, za, uplynulé ,.. ]



83- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [práce]   B= [za, uplynulé, období ,.. ]



84- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [za, uplynulé, období ,.. ]



85- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [za]   B= [uplynulé, období, . ,.. ]



86- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [uplynulé, období, . ,.. ]



87- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [uplynulé]   B= [období, . ,.. ]



88- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [období, . ,.. ]



89- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [období]   B= [.]



90- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [.]



91- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [ ]



92- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]


Error
Error
Error
Error
Error
Error
Error
Error
Error
## Sentence No. 1697 - 
stejně jako maďarsku **by** **se** nám **mohlo** **stát** , že většina obchodů **se** **nebude** **dít** v praze , ale třeba ve vídni nebo v londýně . 
### Existing MWEs: 
1- **by se mohlo stát** (IReflV)

2- **se stát** (IReflV), Embedded

3- **se nebude dít** (IReflV)




0- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [stejně, jako, maďarsku ,.. ]



1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [stejně]   B= [jako, maďarsku, by ,.. ]



2- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [jako, maďarsku, by ,.. ]



3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [jako]   B= [maďarsku, by, se ,.. ]



4- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [maďarsku, by, se ,.. ]



5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [maďarsku]   B= [by, se, nám ,.. ]



6- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [by, se, nám ,.. ]



7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [by]   B= [se, nám, mohlo ,.. ]



8- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [by, se]   B= [nám, mohlo, stát ,.. ]



9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [by, se, nám]   B= [mohlo, stát, , ,.. ]



10- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [by, se]   B= [mohlo, stát, , ,.. ]



11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [by, se, mohlo]   B= [stát, ,, že ,.. ]



12- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [by, se, mohlo, stát]   B= [,, že, většina ,.. ]



13- WHITE_MERGE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [by, se, [mohlo, stát]]   B= [,, že, většina ,.. ]



14- WHITE_MERGE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [by, [se, [mohlo, stát]]]   B= [,, že, většina ,.. ]



15- **MERGE_AS_IReflV**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[by, [se, [mohlo, stát]]]]   B= [,, že, většina ,.. ]



16- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, že, většina ,.. ]



17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [že, většina, obchodů ,.. ]



18- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [že, většina, obchodů ,.. ]



19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [že]   B= [většina, obchodů, se ,.. ]



20- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [většina, obchodů, se ,.. ]



21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [většina]   B= [obchodů, se, nebude ,.. ]



22- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [obchodů, se, nebude ,.. ]



23- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [obchodů]   B= [se, nebude, dít ,.. ]



24- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [se, nebude, dít ,.. ]



25- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [se]   B= [nebude, dít, v ,.. ]



26- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [se, nebude]   B= [dít, v, praze ,.. ]



27- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [se, nebude, dít]   B= [v, praze, , ,.. ]



28- WHITE_MERGE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [se, [nebude, dít]]   B= [v, praze, , ,.. ]



29- **MERGE_AS_IReflV**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[se, [nebude, dít]]]   B= [v, praze, , ,.. ]



30- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [v, praze, , ,.. ]



31- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [v]   B= [praze, ,, ale ,.. ]



32- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [praze, ,, ale ,.. ]



33- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [praze]   B= [,, ale, třeba ,.. ]



34- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, ale, třeba ,.. ]



35- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [ale, třeba, ve ,.. ]



36- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ale, třeba, ve ,.. ]



37- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ale]   B= [třeba, ve, vídni ,.. ]



38- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [třeba, ve, vídni ,.. ]



39- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [třeba]   B= [ve, vídni, nebo ,.. ]



40- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ve, vídni, nebo ,.. ]



41- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ve]   B= [vídni, nebo, v ,.. ]



42- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [vídni, nebo, v ,.. ]



43- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [vídni]   B= [nebo, v, londýně ,.. ]



44- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [nebo, v, londýně ,.. ]



45- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [nebo]   B= [v, londýně, . ,.. ]



46- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [v, londýně, . ,.. ]



47- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [v]   B= [londýně, . ,.. ]



48- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [londýně, . ,.. ]



49- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [londýně]   B= [.]



50- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [.]



51- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [ ]



52- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]


## Sentence No. 2707 - 
doktorand je studentem , **jak** **se** **sluší** **a** **patří** . 
### Existing MWEs: 
1- **jak se sluší a patří** (OTH)

2- **se sluší** (IReflV), Embedded

3- **se patří** (IReflV), Interleaving 




0- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [doktorand, je, studentem ,.. ]



1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [doktorand]   B= [je, studentem, , ,.. ]



2- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [je, studentem, , ,.. ]



3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [je]   B= [studentem, ,, jak ,.. ]



4- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [studentem, ,, jak ,.. ]



5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [studentem]   B= [,, jak, se ,.. ]



6- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, jak, se ,.. ]



7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [jak, se, sluší ,.. ]



8- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [jak, se, sluší ,.. ]



9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [jak]   B= [se, sluší, a ,.. ]



10- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [jak, se]   B= [sluší, a, patří ,.. ]



11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [jak, se, sluší]   B= [a, patří, . ,.. ]



12- **MERGE_AS_IReflV**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [jak, [se, sluší]]   B= [a, patří, . ,.. ]



13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [jak, [se, sluší]  a]   B= [patří, . ,.. ]



14- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [jak, [se, sluší]  a, patří]   B= [.]



15- WHITE_MERGE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [jak, [se, sluší]  [a, patří]]   B= [.]



16- WHITE_MERGE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [jak, [[se, sluší]  [a, patří]]]   B= [.]



17- **MERGE_AS_OTH**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[jak, [[se, sluší]  [a, patří]]]]   B= [.]



18- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [.]



19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [ ]



20- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]


## Sentence No. 2864 - 
**bojím** **se** , že pokud inscenování oper opustí tradiční podobu , **dostane** **se** opera **do** **úzkých** a spíš bude vyhledávat koncertní provedení . 
### Existing MWEs: 
1- **bojím se** (IReflV)

2- **dostane se do úzkých** (ID)

3- **dostane se** (IReflV), Embedded




0- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [bojím, se, , ,.. ]



1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [bojím]   B= [se, ,, že ,.. ]



2- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [bojím, se]   B= [,, že, pokud ,.. ]



3- **MERGE_AS_IReflV**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[bojím, se]]   B= [,, že, pokud ,.. ]



4- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, že, pokud ,.. ]



5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [že, pokud, inscenování ,.. ]



6- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [že, pokud, inscenování ,.. ]



7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [že]   B= [pokud, inscenování, oper ,.. ]



8- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [pokud, inscenování, oper ,.. ]



9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [pokud]   B= [inscenování, oper, opustí ,.. ]



10- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [inscenování, oper, opustí ,.. ]



11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [inscenování]   B= [oper, opustí, tradiční ,.. ]



12- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [oper, opustí, tradiční ,.. ]



13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [oper]   B= [opustí, tradiční, podobu ,.. ]



14- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [opustí, tradiční, podobu ,.. ]



15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [opustí]   B= [tradiční, podobu, , ,.. ]



16- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [tradiční, podobu, , ,.. ]



17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [tradiční]   B= [podobu, ,, dostane ,.. ]



18- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [podobu, ,, dostane ,.. ]



19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [podobu]   B= [,, dostane, se ,.. ]



20- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, dostane, se ,.. ]



21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [dostane, se, opera ,.. ]



22- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [dostane, se, opera ,.. ]



23- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [dostane]   B= [se, opera, do ,.. ]



24- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [dostane, se]   B= [opera, do, úzkých ,.. ]



25- **MERGE_AS_IReflV**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[dostane, se]]   B= [opera, do, úzkých ,.. ]



26- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[dostane, se]  opera]   B= [do, úzkých, a ,.. ]



27- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[dostane, se]]   B= [do, úzkých, a ,.. ]



28- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[dostane, se]  do]   B= [úzkých, a, spíš ,.. ]



29- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[dostane, se]  do, úzkých]   B= [a, spíš, bude ,.. ]



30- WHITE_MERGE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[dostane, se]  [do, úzkých]]   B= [a, spíš, bude ,.. ]



31- **MERGE_AS_ID**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[[dostane, se]  [do, úzkých]]]   B= [a, spíš, bude ,.. ]



32- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [a, spíš, bude ,.. ]



33- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [a]   B= [spíš, bude, vyhledávat ,.. ]



34- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [spíš, bude, vyhledávat ,.. ]



35- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [spíš]   B= [bude, vyhledávat, koncertní ,.. ]



36- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [bude, vyhledávat, koncertní ,.. ]



37- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [bude]   B= [vyhledávat, koncertní, provedení ,.. ]



38- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [vyhledávat, koncertní, provedení ,.. ]



39- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [vyhledávat]   B= [koncertní, provedení, . ,.. ]



40- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [koncertní, provedení, . ,.. ]



41- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [koncertní]   B= [provedení, . ,.. ]



42- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [provedení, . ,.. ]



43- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [provedení]   B= [.]



44- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [.]



45- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [ ]



46- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]


Error
Error
Error
Error
Error
Error
Error
Error
Error
Error
Error
Error
Error
Error
Error
Error
Error
Error
Error
Error
Error
Error
Error
Error
Error
Error
Error
## Sentence No. 4204 - 
potom přišli noví trenéři , začal jsem **dostávat** **příležitost** a pomalu **jsem** **se** **dostával** **do** **tempa** . 
### Existing MWEs: 
1- **dostávat příležitost** (LVC)

2- **jsem se dostával do tempa** (ID)

3- **jsem se dostával** (IReflV), Embedded




0- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [potom, přišli, noví ,.. ]



1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [potom]   B= [přišli, noví, trenéři ,.. ]



2- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [přišli, noví, trenéři ,.. ]



3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [přišli]   B= [noví, trenéři, , ,.. ]



4- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [noví, trenéři, , ,.. ]



5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [noví]   B= [trenéři, ,, začal ,.. ]



6- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [trenéři, ,, začal ,.. ]



7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [trenéři]   B= [,, začal, jsem ,.. ]



8- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, začal, jsem ,.. ]



9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [začal, jsem, dostávat ,.. ]



10- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [začal, jsem, dostávat ,.. ]



11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [začal]   B= [jsem, dostávat, příležitost ,.. ]



12- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [jsem, dostávat, příležitost ,.. ]



13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [jsem]   B= [dostávat, příležitost, a ,.. ]



14- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [dostávat, příležitost, a ,.. ]



15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [dostávat]   B= [příležitost, a, pomalu ,.. ]



16- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [dostávat, příležitost]   B= [a, pomalu, jsem ,.. ]



17- **MERGE_AS_LVC**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[dostávat, příležitost]]   B= [a, pomalu, jsem ,.. ]



18- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [a, pomalu, jsem ,.. ]



19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [a]   B= [pomalu, jsem, se ,.. ]



20- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [pomalu, jsem, se ,.. ]



21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [pomalu]   B= [jsem, se, dostával ,.. ]



22- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [jsem, se, dostával ,.. ]



23- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [jsem]   B= [se, dostával, do ,.. ]



24- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [jsem, se]   B= [dostával, do, tempa ,.. ]



25- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [jsem, se, dostával]   B= [do, tempa, . ,.. ]



26- WHITE_MERGE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [jsem, [se, dostával]]   B= [do, tempa, . ,.. ]



27- **MERGE_AS_IReflV**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[jsem, [se, dostával]]]   B= [do, tempa, . ,.. ]



28- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[jsem, [se, dostával]]  do]   B= [tempa, . ,.. ]



29- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[jsem, [se, dostával]]  do, tempa]   B= [.]



30- WHITE_MERGE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[jsem, [se, dostával]]  [do, tempa]]   B= [.]



31- **MERGE_AS_ID**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[[jsem, [se, dostával]]  [do, tempa]]]   B= [.]



32- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [.]



33- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [ ]



34- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]


## Sentence No. 5074 - 
naposledy **jsme** **se** **zabývali** některými otázkami spojenými s výpovědí z nájmu , a to nikoliv z hlediska výkladu ustanovení občanského zákoníku , ale z hlediska pomalu **se** **tvořící** soudní judikatury . 
### Existing MWEs: 
1- **jsme se zabývali** (IReflV)

2- **se zabývali** (IReflV), Embedded

3- **se tvořící** (IReflV)




0- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [naposledy, jsme, se ,.. ]



1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [naposledy]   B= [jsme, se, zabývali ,.. ]



2- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [jsme, se, zabývali ,.. ]



3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [jsme]   B= [se, zabývali, některými ,.. ]



4- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [jsme, se]   B= [zabývali, některými, otázkami ,.. ]



5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [jsme, se, zabývali]   B= [některými, otázkami, spojenými ,.. ]



6- **MERGE_AS_IReflV**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [jsme, [se, zabývali]]   B= [některými, otázkami, spojenými ,.. ]



7- **MERGE_AS_IReflV**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[jsme, [se, zabývali]]]   B= [některými, otázkami, spojenými ,.. ]



8- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [některými, otázkami, spojenými ,.. ]



9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [některými]   B= [otázkami, spojenými, s ,.. ]



10- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [otázkami, spojenými, s ,.. ]



11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [otázkami]   B= [spojenými, s, výpovědí ,.. ]



12- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [spojenými, s, výpovědí ,.. ]



13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [spojenými]   B= [s, výpovědí, z ,.. ]



14- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [s, výpovědí, z ,.. ]



15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [s]   B= [výpovědí, z, nájmu ,.. ]



16- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [výpovědí, z, nájmu ,.. ]



17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [výpovědí]   B= [z, nájmu, , ,.. ]



18- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [z, nájmu, , ,.. ]



19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [z]   B= [nájmu, ,, a ,.. ]



20- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [nájmu, ,, a ,.. ]



21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [nájmu]   B= [,, a, to ,.. ]



22- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, a, to ,.. ]



23- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [a, to, nikoliv ,.. ]



24- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [a, to, nikoliv ,.. ]



25- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [a]   B= [to, nikoliv, z ,.. ]



26- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [to, nikoliv, z ,.. ]



27- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [to]   B= [nikoliv, z, hlediska ,.. ]



28- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [nikoliv, z, hlediska ,.. ]



29- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [nikoliv]   B= [z, hlediska, výkladu ,.. ]



30- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [z, hlediska, výkladu ,.. ]



31- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [z]   B= [hlediska, výkladu, ustanovení ,.. ]



32- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [hlediska, výkladu, ustanovení ,.. ]



33- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [hlediska]   B= [výkladu, ustanovení, občanského ,.. ]



34- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [výkladu, ustanovení, občanského ,.. ]



35- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [výkladu]   B= [ustanovení, občanského, zákoníku ,.. ]



36- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ustanovení, občanského, zákoníku ,.. ]



37- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ustanovení]   B= [občanského, zákoníku, , ,.. ]



38- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [občanského, zákoníku, , ,.. ]



39- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [občanského]   B= [zákoníku, ,, ale ,.. ]



40- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [zákoníku, ,, ale ,.. ]



41- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [zákoníku]   B= [,, ale, z ,.. ]



42- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, ale, z ,.. ]



43- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [ale, z, hlediska ,.. ]



44- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ale, z, hlediska ,.. ]



45- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ale]   B= [z, hlediska, pomalu ,.. ]



46- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [z, hlediska, pomalu ,.. ]



47- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [z]   B= [hlediska, pomalu, se ,.. ]



48- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [hlediska, pomalu, se ,.. ]



49- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [hlediska]   B= [pomalu, se, tvořící ,.. ]



50- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [pomalu, se, tvořící ,.. ]



51- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [pomalu]   B= [se, tvořící, soudní ,.. ]



52- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [se, tvořící, soudní ,.. ]



53- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [se]   B= [tvořící, soudní, judikatury ,.. ]



54- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [se, tvořící]   B= [soudní, judikatury, . ,.. ]



55- **MERGE_AS_IReflV**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[se, tvořící]]   B= [soudní, judikatury, . ,.. ]



56- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [soudní, judikatury, . ,.. ]



57- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [soudní]   B= [judikatury, . ,.. ]



58- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [judikatury, . ,.. ]



59- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [judikatury]   B= [.]



60- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [.]



61- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [ ]



62- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]


Error
Error
Error
Error
Error
Error
## Sentence No. 7916 - 
Česká republika , která je toho času nestálým členem rady bezpečnosti , **má** **možnost** **zaujmout** ke vzniklé realitě jednoznačné **stanovisko** , neboť je třeba **podívat** **se** **pravdě** **do** **očí** . 
### Existing MWEs: 
1- **má možnost** (LVC)

2- **zaujmout stanovisko** (LVC)

3- **podívat se pravdě do očí** (ID)

4- **podívat se** (IReflV), Embedded




0- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Česká, republika, , ,.. ]



1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Česká]   B= [republika, ,, která ,.. ]



2- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [republika, ,, která ,.. ]



3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [republika]   B= [,, která, je ,.. ]



4- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, která, je ,.. ]



5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [která, je, toho ,.. ]



6- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [která, je, toho ,.. ]



7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [která]   B= [je, toho, času ,.. ]



8- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [je, toho, času ,.. ]



9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [je]   B= [toho, času, nestálým ,.. ]



10- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [toho, času, nestálým ,.. ]



11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [toho]   B= [času, nestálým, členem ,.. ]



12- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [času, nestálým, členem ,.. ]



13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [času]   B= [nestálým, členem, rady ,.. ]



14- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [nestálým, členem, rady ,.. ]



15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [nestálým]   B= [členem, rady, bezpečnosti ,.. ]



16- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [členem, rady, bezpečnosti ,.. ]



17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [členem]   B= [rady, bezpečnosti, , ,.. ]



18- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [rady, bezpečnosti, , ,.. ]



19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [rady]   B= [bezpečnosti, ,, má ,.. ]



20- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [bezpečnosti, ,, má ,.. ]



21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [bezpečnosti]   B= [,, má, možnost ,.. ]



22- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, má, možnost ,.. ]



23- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [má, možnost, zaujmout ,.. ]



24- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [má, možnost, zaujmout ,.. ]



25- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [má]   B= [možnost, zaujmout, ke ,.. ]



26- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [má, možnost]   B= [zaujmout, ke, vzniklé ,.. ]



27- **MERGE_AS_LVC**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[má, možnost]]   B= [zaujmout, ke, vzniklé ,.. ]



28- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [zaujmout, ke, vzniklé ,.. ]



29- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [zaujmout]   B= [ke, vzniklé, realitě ,.. ]



30- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [zaujmout, ke]   B= [vzniklé, realitě, jednoznačné ,.. ]



31- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [zaujmout]   B= [vzniklé, realitě, jednoznačné ,.. ]



32- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [zaujmout, vzniklé]   B= [realitě, jednoznačné, stanovisko ,.. ]



33- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [zaujmout]   B= [realitě, jednoznačné, stanovisko ,.. ]



34- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [zaujmout, realitě]   B= [jednoznačné, stanovisko, , ,.. ]



35- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [zaujmout]   B= [jednoznačné, stanovisko, , ,.. ]



36- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [zaujmout, jednoznačné]   B= [stanovisko, ,, neboť ,.. ]



37- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [zaujmout]   B= [stanovisko, ,, neboť ,.. ]



38- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [zaujmout, stanovisko]   B= [,, neboť, je ,.. ]



39- **MERGE_AS_LVC**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[zaujmout, stanovisko]]   B= [,, neboť, je ,.. ]



40- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, neboť, je ,.. ]



41- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [neboť, je, třeba ,.. ]



42- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [neboť, je, třeba ,.. ]



43- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [neboť]   B= [je, třeba, podívat ,.. ]



44- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [je, třeba, podívat ,.. ]



45- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [je]   B= [třeba, podívat, se ,.. ]



46- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [třeba, podívat, se ,.. ]



47- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [třeba]   B= [podívat, se, pravdě ,.. ]



48- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [podívat, se, pravdě ,.. ]



49- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [podívat]   B= [se, pravdě, do ,.. ]



50- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [podívat, se]   B= [pravdě, do, očí ,.. ]



51- **MERGE_AS_IReflV**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[podívat, se]]   B= [pravdě, do, očí ,.. ]



52- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[podívat, se]  pravdě]   B= [do, očí, . ,.. ]



53- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[podívat, se]  pravdě, do]   B= [očí, . ,.. ]



54- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[podívat, se]  pravdě, do, očí]   B= [.]



55- WHITE_MERGE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[podívat, se]  pravdě, [do, očí]]   B= [.]



56- WHITE_MERGE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[podívat, se]  [pravdě, [do, očí]]]   B= [.]



57- **MERGE_AS_ID**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[[podívat, se]  [pravdě, [do, očí]]]]   B= [.]



58- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [.]



59- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [ ]



60- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]


Error
Error
Error
Error
## Sentence No. 8549 - 
**dovedu** **si** **představit** , že **bychom** **se** **mohli** během dvou let této úrovni **přiblížit** . 
### Existing MWEs: 
1- **dovedu si představit** (ID)

2- **dovedu si představit** (IReflV), Embedded

3- **bychom se mohli přiblížit** (IReflV)




0- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [dovedu, si, představit ,.. ]



1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [dovedu]   B= [si, představit, , ,.. ]



2- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [dovedu, si]   B= [představit, ,, že ,.. ]



3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [dovedu, si, představit]   B= [,, že, bychom ,.. ]



4- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [dovedu, si, představit, ,]   B= [že, bychom, se ,.. ]



5- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [dovedu, si, představit]   B= [že, bychom, se ,.. ]



6- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [dovedu, si, představit, že]   B= [bychom, se, mohli ,.. ]



7- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [dovedu, si, představit]   B= [bychom, se, mohli ,.. ]



8- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [dovedu, si, představit, bychom]   B= [se, mohli, během ,.. ]



9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [dovedu, si, představit, bychom, se]   B= [mohli, během, dvou ,.. ]



10- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [dovedu, si, představit, bychom, se, mohli]   B= [během, dvou, let ,.. ]



11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [dovedu, si, představit, bychom, se, mohli, během]   B= [dvou, let, této ,.. ]



12- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [dovedu, si, představit, bychom, se, mohli]   B= [dvou, let, této ,.. ]



13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [dovedu, si, představit, bychom, se, mohli, dvou]   B= [let, této, úrovni ,.. ]



14- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [dovedu, si, představit, bychom, se, mohli]   B= [let, této, úrovni ,.. ]



15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [dovedu, si, představit, bychom, se, mohli, let]   B= [této, úrovni, přiblížit ,.. ]



16- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [dovedu, si, představit, bychom, se, mohli]   B= [této, úrovni, přiblížit ,.. ]



17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [dovedu, si, představit, bychom, se, mohli, této]   B= [úrovni, přiblížit, . ,.. ]



18- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [dovedu, si, představit, bychom, se, mohli]   B= [úrovni, přiblížit, . ,.. ]



19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [dovedu, si, představit, bychom, se, mohli, úrovni]   B= [přiblížit, . ,.. ]



20- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [dovedu, si, představit, bychom, se, mohli]   B= [přiblížit, . ,.. ]



21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [dovedu, si, představit, bychom, se, mohli, přiblížit]   B= [.]



22- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [dovedu, si, představit, bychom, se, mohli, přiblížit, .]   B= [ ]



23- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [dovedu, si, představit, bychom, se, mohli, přiblížit]   B= [ ]



24- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [dovedu, si, představit, bychom, se, mohli]   B= [ ]



25- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [dovedu, si, představit, bychom, se]   B= [ ]



26- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [dovedu, si, představit, bychom]   B= [ ]



27- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [dovedu, si, představit]   B= [ ]



28- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [dovedu, si]   B= [ ]



29- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [dovedu]   B= [ ]



30- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]


## Sentence No. 15276 - 
všechno **se** **k** **lepšímu** **obrátilo** s **blížícími** **se** volbami do kocourkovského magistrátu . 
### Existing MWEs: 
1- **se k lepšímu obrátilo** (ID)

2- **se obrátilo** (IReflV), Embedded

3- **blížícími se** (IReflV)




0- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [všechno, se, k ,.. ]



1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [všechno]   B= [se, k, lepšímu ,.. ]



2- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [se, k, lepšímu ,.. ]



3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [se]   B= [k, lepšímu, obrátilo ,.. ]



4- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [se, k]   B= [lepšímu, obrátilo, s ,.. ]



5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [se, k, lepšímu]   B= [obrátilo, s, blížícími ,.. ]



6- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [se, k, lepšímu, obrátilo]   B= [s, blížícími, se ,.. ]



7- WHITE_MERGE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [se, k, [lepšímu, obrátilo]]   B= [s, blížícími, se ,.. ]



8- WHITE_MERGE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [se, [k, [lepšímu, obrátilo]]]   B= [s, blížícími, se ,.. ]



9- **MERGE_AS_ID**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[se, [k, [lepšímu, obrátilo]]]]   B= [s, blížícími, se ,.. ]



10- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [s, blížícími, se ,.. ]



11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [s]   B= [blížícími, se, volbami ,.. ]



12- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [blížícími, se, volbami ,.. ]



13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [blížícími]   B= [se, volbami, do ,.. ]



14- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [blížícími, se]   B= [volbami, do, kocourkovského ,.. ]



15- **MERGE_AS_IReflV**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[blížícími, se]]   B= [volbami, do, kocourkovského ,.. ]



16- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [volbami, do, kocourkovského ,.. ]



17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [volbami]   B= [do, kocourkovského, magistrátu ,.. ]



18- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [do, kocourkovského, magistrátu ,.. ]



19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [do]   B= [kocourkovského, magistrátu, . ,.. ]



20- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [kocourkovského, magistrátu, . ,.. ]



21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [kocourkovského]   B= [magistrátu, . ,.. ]



22- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [magistrátu, . ,.. ]



23- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [magistrátu]   B= [.]



24- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [.]



25- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [ ]



26- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]


