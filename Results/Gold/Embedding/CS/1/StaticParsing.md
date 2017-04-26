## Sentence No. 30834 - 
**dejte** **si** **pozor** , aby **se** z vás **nestali** cizinci : mezi nimi **se** též **nalézá** mnoho ubožáků , kteří **se** **chovají** zpupně jenom proto , že **se** tu **cítí** bohatí ! 
### Existing MWEs: 
1- **dejte si pozor** (ID)Tokens : 
dejte
si
pozor


2- **dejte si** (IReflV), EmbeddedTokens : 
dejte
si


3- **se nestali** (IReflV)Tokens : 
se
nestali


4- **se nalézá** (IReflV)Tokens : 
se
nalézá


5- **se chovají** (IReflV)Tokens : 
se
chovají


6- **se cítí** (IReflV)Tokens : 
se
cítí





0- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [dejte, si, pozor ,.. ]



1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [dejte]   B= [si, pozor, , ,.. ]



2- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [dejte, si]   B= [pozor, ,, aby ,.. ]



3- **MERGE_AS_IReflV**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[dejte, si]]   B= [pozor, ,, aby ,.. ]



4- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[dejte, si]  pozor]   B= [,, aby, se ,.. ]



5- **MERGE_AS_ID**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[[dejte, si]  pozor]]   B= [,, aby, se ,.. ]



6- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, aby, se ,.. ]



7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [aby, se, z ,.. ]



8- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [aby, se, z ,.. ]



9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [aby]   B= [se, z, vás ,.. ]



10- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [se, z, vás ,.. ]



11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [se]   B= [z, vás, nestali ,.. ]



12- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [se, z]   B= [vás, nestali, cizinci ,.. ]



13- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [se]   B= [vás, nestali, cizinci ,.. ]



14- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [se, vás]   B= [nestali, cizinci, : ,.. ]



15- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [se]   B= [nestali, cizinci, : ,.. ]



16- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [se, nestali]   B= [cizinci, :, mezi ,.. ]



17- **MERGE_AS_IReflV**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[se, nestali]]   B= [cizinci, :, mezi ,.. ]



18- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [cizinci, :, mezi ,.. ]



19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [cizinci]   B= [:, mezi, nimi ,.. ]



20- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [:, mezi, nimi ,.. ]



21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [:]   B= [mezi, nimi, se ,.. ]



22- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [mezi, nimi, se ,.. ]



23- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [mezi]   B= [nimi, se, též ,.. ]



24- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [nimi, se, též ,.. ]



25- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [nimi]   B= [se, též, nalézá ,.. ]



26- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [se, též, nalézá ,.. ]



27- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [se]   B= [též, nalézá, mnoho ,.. ]



28- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [se, též]   B= [nalézá, mnoho, ubožáků ,.. ]



29- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [se]   B= [nalézá, mnoho, ubožáků ,.. ]



30- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [se, nalézá]   B= [mnoho, ubožáků, , ,.. ]



31- **MERGE_AS_IReflV**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[se, nalézá]]   B= [mnoho, ubožáků, , ,.. ]



32- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [mnoho, ubožáků, , ,.. ]



33- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [mnoho]   B= [ubožáků, ,, kteří ,.. ]



34- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ubožáků, ,, kteří ,.. ]



35- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ubožáků]   B= [,, kteří, se ,.. ]



36- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, kteří, se ,.. ]



37- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [kteří, se, chovají ,.. ]



38- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [kteří, se, chovají ,.. ]



39- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [kteří]   B= [se, chovají, zpupně ,.. ]



40- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [se, chovají, zpupně ,.. ]



41- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [se]   B= [chovají, zpupně, jenom ,.. ]



42- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [se, chovají]   B= [zpupně, jenom, proto ,.. ]



43- **MERGE_AS_IReflV**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[se, chovají]]   B= [zpupně, jenom, proto ,.. ]



44- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [zpupně, jenom, proto ,.. ]



45- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [zpupně]   B= [jenom, proto, , ,.. ]



46- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [jenom, proto, , ,.. ]



47- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [jenom]   B= [proto, ,, že ,.. ]



48- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [proto, ,, že ,.. ]



49- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [proto]   B= [,, že, se ,.. ]



50- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, že, se ,.. ]



51- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [že, se, tu ,.. ]



52- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [že, se, tu ,.. ]



53- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [že]   B= [se, tu, cítí ,.. ]



54- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [se, tu, cítí ,.. ]



55- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [se]   B= [tu, cítí, bohatí ,.. ]



56- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [se, tu]   B= [cítí, bohatí, ! ,.. ]



57- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [se]   B= [cítí, bohatí, ! ,.. ]



58- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [se, cítí]   B= [bohatí, ! ,.. ]



59- **MERGE_AS_IReflV**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[se, cítí]]   B= [bohatí, ! ,.. ]



60- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [bohatí, ! ,.. ]



61- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [bohatí]   B= [!]



62- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [!]



63- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [!]   B= [ ]



64- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

## Sentence No. 31111 - 
i lehkomyslný novinář **to** **má** **těžké** : každý den **se** na něj **hrnou** nová témata , v nichž **se** **musí** nějak **vyznat** , aniž **by** **se** kdo **ptal** , zda **má** na seznámení **čas** a **sílu** . 
### Existing MWEs: 
1- **to má těžké** (ID)Tokens : 
to
má
těžké


2- **se hrnou** (IReflV)Tokens : 
se
hrnou


3- **se musí vyznat** (IReflV)Tokens : 
se
musí
vyznat


4- **by se ptal** (IReflV)Tokens : 
by
se
ptal


5- **má čas** (LVC)Tokens : 
má
čas


6- **má sílu** (LVC), Interleaving Tokens : 
má
sílu





0- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [i, lehkomyslný, novinář ,.. ]



1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [i]   B= [lehkomyslný, novinář, to ,.. ]



2- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [lehkomyslný, novinář, to ,.. ]



3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [lehkomyslný]   B= [novinář, to, má ,.. ]



4- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [novinář, to, má ,.. ]



5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [novinář]   B= [to, má, těžké ,.. ]



6- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [to, má, těžké ,.. ]



7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [to]   B= [má, těžké, : ,.. ]



8- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [to, má]   B= [těžké, :, každý ,.. ]



9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [to, má, těžké]   B= [:, každý, den ,.. ]



10- WHITE_MERGE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [to, [má, těžké]]   B= [:, každý, den ,.. ]



11- **MERGE_AS_ID**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[to, [má, těžké]]]   B= [:, každý, den ,.. ]



12- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [:, každý, den ,.. ]



13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [:]   B= [každý, den, se ,.. ]



14- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [každý, den, se ,.. ]



15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [každý]   B= [den, se, na ,.. ]



16- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [den, se, na ,.. ]



17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [den]   B= [se, na, něj ,.. ]



18- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [se, na, něj ,.. ]



19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [se]   B= [na, něj, hrnou ,.. ]



20- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [se, na]   B= [něj, hrnou, nová ,.. ]



21- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [se]   B= [něj, hrnou, nová ,.. ]



22- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [se, něj]   B= [hrnou, nová, témata ,.. ]



23- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [se]   B= [hrnou, nová, témata ,.. ]



24- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [se, hrnou]   B= [nová, témata, , ,.. ]



25- **MERGE_AS_IReflV**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[se, hrnou]]   B= [nová, témata, , ,.. ]



26- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [nová, témata, , ,.. ]



27- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [nová]   B= [témata, ,, v ,.. ]



28- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [témata, ,, v ,.. ]



29- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [témata]   B= [,, v, nichž ,.. ]



30- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, v, nichž ,.. ]



31- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [v, nichž, se ,.. ]



32- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [v, nichž, se ,.. ]



33- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [v]   B= [nichž, se, musí ,.. ]



34- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [nichž, se, musí ,.. ]



35- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [nichž]   B= [se, musí, nějak ,.. ]



36- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [se, musí, nějak ,.. ]



37- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [se]   B= [musí, nějak, vyznat ,.. ]



38- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [se, musí]   B= [nějak, vyznat, , ,.. ]



39- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [se, musí, nějak]   B= [vyznat, ,, aniž ,.. ]



40- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [se, musí]   B= [vyznat, ,, aniž ,.. ]



41- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [se, musí, vyznat]   B= [,, aniž, by ,.. ]



42- WHITE_MERGE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [se, [musí, vyznat]]   B= [,, aniž, by ,.. ]



43- **MERGE_AS_IReflV**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[se, [musí, vyznat]]]   B= [,, aniž, by ,.. ]



44- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, aniž, by ,.. ]



45- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [aniž, by, se ,.. ]



46- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [aniž, by, se ,.. ]



47- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [aniž]   B= [by, se, kdo ,.. ]



48- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [by, se, kdo ,.. ]



49- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [by]   B= [se, kdo, ptal ,.. ]



50- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [by, se]   B= [kdo, ptal, , ,.. ]



51- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [by, se, kdo]   B= [ptal, ,, zda ,.. ]



52- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [by, se]   B= [ptal, ,, zda ,.. ]



53- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [by, se, ptal]   B= [,, zda, má ,.. ]



54- WHITE_MERGE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [by, [se, ptal]]   B= [,, zda, má ,.. ]



55- **MERGE_AS_IReflV**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[by, [se, ptal]]]   B= [,, zda, má ,.. ]



56- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, zda, má ,.. ]



57- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [zda, má, na ,.. ]



58- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [zda, má, na ,.. ]



59- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [zda]   B= [má, na, seznámení ,.. ]



60- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [má, na, seznámení ,.. ]



61- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [má]   B= [na, seznámení, čas ,.. ]



62- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [má, na]   B= [seznámení, čas, a ,.. ]



63- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [má]   B= [seznámení, čas, a ,.. ]



64- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [má, seznámení]   B= [čas, a, sílu ,.. ]



65- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [má]   B= [čas, a, sílu ,.. ]



66- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [má, čas]   B= [a, sílu, . ,.. ]



67- **MERGE_AS_LVC**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[má, čas]]   B= [a, sílu, . ,.. ]



68- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [a, sílu, . ,.. ]



69- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [a]   B= [sílu, . ,.. ]



70- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [sílu, . ,.. ]



71- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [sílu]   B= [.]



72- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [.]



73- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [ ]



74- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

## Sentence No. 9212 - 
tam je podle mého kámen úrazu : hlava je při podobném nárazu jedinou částí těla , která není pevně fixována a musí pohltit obrovské množství energie , " **přidal** **se** lauda a **zamyslel** **se** nad touto motoristickou disciplínou : " formule 1 je extrémně nebezpečný sport a člověk si **musí** neustále **klást** **otázku** , jestli to **má** vůbec nějaký **smysl** . 
### Existing MWEs: 
1- **přidal se** (IReflV)Tokens : 
přidal
se


2- **zamyslel se** (IReflV)Tokens : 
zamyslel
se


3- **musí klást otázku** (LVC)Tokens : 
musí
klást
otázku


4- **má smysl** (LVC)Tokens : 
má
smysl





0- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [tam, je, podle ,.. ]



1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [tam]   B= [je, podle, mého ,.. ]



2- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [je, podle, mého ,.. ]



3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [je]   B= [podle, mého, kámen ,.. ]



4- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [podle, mého, kámen ,.. ]



5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [podle]   B= [mého, kámen, úrazu ,.. ]



6- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [mého, kámen, úrazu ,.. ]



7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [mého]   B= [kámen, úrazu, : ,.. ]



8- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [kámen, úrazu, : ,.. ]



9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [kámen]   B= [úrazu, :, hlava ,.. ]



10- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [úrazu, :, hlava ,.. ]



11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [úrazu]   B= [:, hlava, je ,.. ]



12- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [:, hlava, je ,.. ]



13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [:]   B= [hlava, je, při ,.. ]



14- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [hlava, je, při ,.. ]



15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [hlava]   B= [je, při, podobném ,.. ]



16- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [je, při, podobném ,.. ]



17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [je]   B= [při, podobném, nárazu ,.. ]



18- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [při, podobném, nárazu ,.. ]



19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [při]   B= [podobném, nárazu, jedinou ,.. ]



20- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [podobném, nárazu, jedinou ,.. ]



21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [podobném]   B= [nárazu, jedinou, částí ,.. ]



22- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [nárazu, jedinou, částí ,.. ]



23- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [nárazu]   B= [jedinou, částí, těla ,.. ]



24- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [jedinou, částí, těla ,.. ]



25- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [jedinou]   B= [částí, těla, , ,.. ]



26- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [částí, těla, , ,.. ]



27- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [částí]   B= [těla, ,, která ,.. ]



28- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [těla, ,, která ,.. ]



29- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [těla]   B= [,, která, není ,.. ]



30- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, která, není ,.. ]



31- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [která, není, pevně ,.. ]



32- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [která, není, pevně ,.. ]



33- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [která]   B= [není, pevně, fixována ,.. ]



34- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [není, pevně, fixována ,.. ]



35- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [není]   B= [pevně, fixována, a ,.. ]



36- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [pevně, fixována, a ,.. ]



37- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [pevně]   B= [fixována, a, musí ,.. ]



38- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [fixována, a, musí ,.. ]



39- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [fixována]   B= [a, musí, pohltit ,.. ]



40- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [a, musí, pohltit ,.. ]



41- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [a]   B= [musí, pohltit, obrovské ,.. ]



42- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [musí, pohltit, obrovské ,.. ]



43- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [musí]   B= [pohltit, obrovské, množství ,.. ]



44- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [pohltit, obrovské, množství ,.. ]



45- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [pohltit]   B= [obrovské, množství, energie ,.. ]



46- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [obrovské, množství, energie ,.. ]



47- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [obrovské]   B= [množství, energie, , ,.. ]



48- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [množství, energie, , ,.. ]



49- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [množství]   B= [energie, ,, " ,.. ]



50- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [energie, ,, " ,.. ]



51- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [energie]   B= [,, ", přidal ,.. ]



52- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, ", přidal ,.. ]



53- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [", přidal, se ,.. ]



54- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [", přidal, se ,.. ]



55- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= ["]   B= [přidal, se, lauda ,.. ]



56- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [přidal, se, lauda ,.. ]



57- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [přidal]   B= [se, lauda, a ,.. ]



58- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [přidal, se]   B= [lauda, a, zamyslel ,.. ]



59- **MERGE_AS_IReflV**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[přidal, se]]   B= [lauda, a, zamyslel ,.. ]



60- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [lauda, a, zamyslel ,.. ]



61- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [lauda]   B= [a, zamyslel, se ,.. ]



62- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [a, zamyslel, se ,.. ]



63- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [a]   B= [zamyslel, se, nad ,.. ]



64- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [zamyslel, se, nad ,.. ]



65- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [zamyslel]   B= [se, nad, touto ,.. ]



66- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [zamyslel, se]   B= [nad, touto, motoristickou ,.. ]



67- **MERGE_AS_IReflV**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[zamyslel, se]]   B= [nad, touto, motoristickou ,.. ]



68- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [nad, touto, motoristickou ,.. ]



69- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [nad]   B= [touto, motoristickou, disciplínou ,.. ]



70- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [touto, motoristickou, disciplínou ,.. ]



71- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [touto]   B= [motoristickou, disciplínou, : ,.. ]



72- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [motoristickou, disciplínou, : ,.. ]



73- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [motoristickou]   B= [disciplínou, :, " ,.. ]



74- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [disciplínou, :, " ,.. ]



75- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [disciplínou]   B= [:, ", formule ,.. ]



76- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [:, ", formule ,.. ]



77- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [:]   B= [", formule, 1 ,.. ]



78- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [", formule, 1 ,.. ]



79- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= ["]   B= [formule, 1, je ,.. ]



80- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [formule, 1, je ,.. ]



81- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [formule]   B= [1, je, extrémně ,.. ]



82- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [1, je, extrémně ,.. ]



83- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [1]   B= [je, extrémně, nebezpečný ,.. ]



84- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [je, extrémně, nebezpečný ,.. ]



85- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [je]   B= [extrémně, nebezpečný, sport ,.. ]



86- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [extrémně, nebezpečný, sport ,.. ]



87- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [extrémně]   B= [nebezpečný, sport, a ,.. ]



88- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [nebezpečný, sport, a ,.. ]



89- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [nebezpečný]   B= [sport, a, člověk ,.. ]



90- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [sport, a, člověk ,.. ]



91- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [sport]   B= [a, člověk, si ,.. ]



92- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [a, člověk, si ,.. ]



93- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [a]   B= [člověk, si, musí ,.. ]



94- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [člověk, si, musí ,.. ]



95- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [člověk]   B= [si, musí, neustále ,.. ]



96- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [si, musí, neustále ,.. ]



97- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [si]   B= [musí, neustále, klást ,.. ]



98- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [musí, neustále, klást ,.. ]



99- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [musí]   B= [neustále, klást, otázku ,.. ]



100- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [musí, neustále]   B= [klást, otázku, , ,.. ]



101- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [musí]   B= [klást, otázku, , ,.. ]



102- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [musí, klást]   B= [otázku, ,, jestli ,.. ]



103- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [musí, klást, otázku]   B= [,, jestli, to ,.. ]



104- WHITE_MERGE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [musí, [klást, otázku]]   B= [,, jestli, to ,.. ]



105- **MERGE_AS_LVC**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[musí, [klást, otázku]]]   B= [,, jestli, to ,.. ]



106- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, jestli, to ,.. ]



107- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [jestli, to, má ,.. ]



108- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [jestli, to, má ,.. ]



109- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [jestli]   B= [to, má, vůbec ,.. ]



110- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [to, má, vůbec ,.. ]



111- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [to]   B= [má, vůbec, nějaký ,.. ]



112- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [má, vůbec, nějaký ,.. ]



113- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [má]   B= [vůbec, nějaký, smysl ,.. ]



114- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [má, vůbec]   B= [nějaký, smysl, . ,.. ]



115- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [má]   B= [nějaký, smysl, . ,.. ]



116- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [má, nějaký]   B= [smysl, . ,.. ]



117- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [má]   B= [smysl, . ,.. ]



118- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [má, smysl]   B= [.]



119- **MERGE_AS_LVC**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[má, smysl]]   B= [.]



120- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [.]



121- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [ ]



122- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

## Sentence No. 11782 - 
neméně důležitým **se** mi **jeví** i určitá spontánní symbolická gesta a události , které vyjadřují úctu k lidem , již **měli** **odvahu** **postavit** **se** komunistickému příkoří a dokonce za obhajobu pravdy **položit** i svůj **život** . 
### Existing MWEs: 
1- **se jeví** (IReflV)Tokens : 
se
jeví


2- **měli odvahu** (LVC)Tokens : 
měli
odvahu


3- **postavit se** (IReflV)Tokens : 
postavit
se


4- **položit život** (ID)Tokens : 
položit
život





0- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [neméně, důležitým, se ,.. ]



1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [neméně]   B= [důležitým, se, mi ,.. ]



2- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [důležitým, se, mi ,.. ]



3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [důležitým]   B= [se, mi, jeví ,.. ]



4- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [se, mi, jeví ,.. ]



5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [se]   B= [mi, jeví, i ,.. ]



6- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [se, mi]   B= [jeví, i, určitá ,.. ]



7- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [se]   B= [jeví, i, určitá ,.. ]



8- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [se, jeví]   B= [i, určitá, spontánní ,.. ]



9- **MERGE_AS_IReflV**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[se, jeví]]   B= [i, určitá, spontánní ,.. ]



10- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [i, určitá, spontánní ,.. ]



11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [i]   B= [určitá, spontánní, symbolická ,.. ]



12- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [určitá, spontánní, symbolická ,.. ]



13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [určitá]   B= [spontánní, symbolická, gesta ,.. ]



14- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [spontánní, symbolická, gesta ,.. ]



15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [spontánní]   B= [symbolická, gesta, a ,.. ]



16- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [symbolická, gesta, a ,.. ]



17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [symbolická]   B= [gesta, a, události ,.. ]



18- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [gesta, a, události ,.. ]



19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [gesta]   B= [a, události, , ,.. ]



20- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [a, události, , ,.. ]



21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [a]   B= [události, ,, které ,.. ]



22- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [události, ,, které ,.. ]



23- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [události]   B= [,, které, vyjadřují ,.. ]



24- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, které, vyjadřují ,.. ]



25- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [které, vyjadřují, úctu ,.. ]



26- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [které, vyjadřují, úctu ,.. ]



27- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [které]   B= [vyjadřují, úctu, k ,.. ]



28- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [vyjadřují, úctu, k ,.. ]



29- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [vyjadřují]   B= [úctu, k, lidem ,.. ]



30- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [úctu, k, lidem ,.. ]



31- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [úctu]   B= [k, lidem, , ,.. ]



32- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [k, lidem, , ,.. ]



33- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [k]   B= [lidem, ,, již ,.. ]



34- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [lidem, ,, již ,.. ]



35- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [lidem]   B= [,, již, měli ,.. ]



36- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, již, měli ,.. ]



37- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [již, měli, odvahu ,.. ]



38- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [již, měli, odvahu ,.. ]



39- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [již]   B= [měli, odvahu, postavit ,.. ]



40- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [měli, odvahu, postavit ,.. ]



41- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [měli]   B= [odvahu, postavit, se ,.. ]



42- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [měli, odvahu]   B= [postavit, se, komunistickému ,.. ]



43- **MERGE_AS_LVC**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[měli, odvahu]]   B= [postavit, se, komunistickému ,.. ]



44- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [postavit, se, komunistickému ,.. ]



45- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [postavit]   B= [se, komunistickému, příkoří ,.. ]



46- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [postavit, se]   B= [komunistickému, příkoří, a ,.. ]



47- **MERGE_AS_IReflV**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[postavit, se]]   B= [komunistickému, příkoří, a ,.. ]



48- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [komunistickému, příkoří, a ,.. ]



49- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [komunistickému]   B= [příkoří, a, dokonce ,.. ]



50- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [příkoří, a, dokonce ,.. ]



51- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [příkoří]   B= [a, dokonce, za ,.. ]



52- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [a, dokonce, za ,.. ]



53- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [a]   B= [dokonce, za, obhajobu ,.. ]



54- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [dokonce, za, obhajobu ,.. ]



55- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [dokonce]   B= [za, obhajobu, pravdy ,.. ]



56- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [za, obhajobu, pravdy ,.. ]



57- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [za]   B= [obhajobu, pravdy, položit ,.. ]



58- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [obhajobu, pravdy, položit ,.. ]



59- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [obhajobu]   B= [pravdy, položit, i ,.. ]



60- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [pravdy, položit, i ,.. ]



61- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [pravdy]   B= [položit, i, svůj ,.. ]



62- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [položit, i, svůj ,.. ]



63- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [položit]   B= [i, svůj, život ,.. ]



64- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [položit, i]   B= [svůj, život, . ,.. ]



65- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [položit]   B= [svůj, život, . ,.. ]



66- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [položit, svůj]   B= [život, . ,.. ]



67- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [položit]   B= [život, . ,.. ]



68- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [položit, život]   B= [.]



69- **MERGE_AS_ID**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[položit, život]]   B= [.]



70- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [.]



71- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [ ]



72- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

## Sentence No. 11815 - 
peres oznámil , že izraelské úřady návštěvu samozřejmě povolí , vždyť proti ní **nemají** žádné **námitky** , a když **si** paní bhuttová **nepřeje** **setkat** **se** s izraelci - **nemusí** ; 
### Existing MWEs: 
1- **nemají námitky** (LVC)Tokens : 
nemají
námitky


2- **si nepřeje** (IReflV)Tokens : 
si
nepřeje


3- **setkat se nemusí** (IReflV)Tokens : 
setkat
se
nemusí


4- **setkat se** (IReflV), EmbeddedTokens : 
setkat
se





0- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [peres, oznámil, , ,.. ]



1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [peres]   B= [oznámil, ,, že ,.. ]



2- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [oznámil, ,, že ,.. ]



3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [oznámil]   B= [,, že, izraelské ,.. ]



4- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, že, izraelské ,.. ]



5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [že, izraelské, úřady ,.. ]



6- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [že, izraelské, úřady ,.. ]



7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [že]   B= [izraelské, úřady, návštěvu ,.. ]



8- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [izraelské, úřady, návštěvu ,.. ]



9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [izraelské]   B= [úřady, návštěvu, samozřejmě ,.. ]



10- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [úřady, návštěvu, samozřejmě ,.. ]



11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [úřady]   B= [návštěvu, samozřejmě, povolí ,.. ]



12- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [návštěvu, samozřejmě, povolí ,.. ]



13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [návštěvu]   B= [samozřejmě, povolí, , ,.. ]



14- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [samozřejmě, povolí, , ,.. ]



15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [samozřejmě]   B= [povolí, ,, vždyť ,.. ]



16- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [povolí, ,, vždyť ,.. ]



17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [povolí]   B= [,, vždyť, proti ,.. ]



18- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, vždyť, proti ,.. ]



19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [vždyť, proti, ní ,.. ]



20- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [vždyť, proti, ní ,.. ]



21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [vždyť]   B= [proti, ní, nemají ,.. ]



22- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [proti, ní, nemají ,.. ]



23- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [proti]   B= [ní, nemají, žádné ,.. ]



24- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ní, nemají, žádné ,.. ]



25- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ní]   B= [nemají, žádné, námitky ,.. ]



26- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [nemají, žádné, námitky ,.. ]



27- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [nemají]   B= [žádné, námitky, , ,.. ]



28- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [nemají, žádné]   B= [námitky, ,, a ,.. ]



29- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [nemají]   B= [námitky, ,, a ,.. ]



30- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [nemají, námitky]   B= [,, a, když ,.. ]



31- **MERGE_AS_LVC**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[nemají, námitky]]   B= [,, a, když ,.. ]



32- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, a, když ,.. ]



33- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [a, když, si ,.. ]



34- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [a, když, si ,.. ]



35- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [a]   B= [když, si, paní ,.. ]



36- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [když, si, paní ,.. ]



37- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [když]   B= [si, paní, bhuttová ,.. ]



38- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [si, paní, bhuttová ,.. ]



39- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [si]   B= [paní, bhuttová, nepřeje ,.. ]



40- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [si, paní]   B= [bhuttová, nepřeje, setkat ,.. ]



41- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [si]   B= [bhuttová, nepřeje, setkat ,.. ]



42- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [si, bhuttová]   B= [nepřeje, setkat, se ,.. ]



43- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [si]   B= [nepřeje, setkat, se ,.. ]



44- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [si, nepřeje]   B= [setkat, se, s ,.. ]



45- **MERGE_AS_IReflV**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[si, nepřeje]]   B= [setkat, se, s ,.. ]



46- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [setkat, se, s ,.. ]



47- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [setkat]   B= [se, s, izraelci ,.. ]



48- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [setkat, se]   B= [s, izraelci, - ,.. ]



49- **MERGE_AS_IReflV**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[setkat, se]]   B= [s, izraelci, - ,.. ]



50- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[setkat, se]  s]   B= [izraelci, -, nemusí ,.. ]



51- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[setkat, se]]   B= [izraelci, -, nemusí ,.. ]



52- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[setkat, se]  izraelci]   B= [-, nemusí, ; ,.. ]



53- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[setkat, se]]   B= [-, nemusí, ; ,.. ]



54- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[setkat, se]  -]   B= [nemusí, ; ,.. ]



55- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[setkat, se]]   B= [nemusí, ; ,.. ]



56- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[setkat, se]  nemusí]   B= [;]



57- **MERGE_AS_IReflV**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[[setkat, se]  nemusí]]   B= [;]



58- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [;]



59- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [;]   B= [ ]



60- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

