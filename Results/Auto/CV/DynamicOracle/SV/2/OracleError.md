#Oracle problem
## Sentence No. 81 - 
låt oss **ta** det **på** **allvar** . 
### Existing MWEs: 
1- **ta på allvar** (ID)

black Merge Num : 2 Interleaving Num: 0


0- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [låt, oss, ta ,.. ]



1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [låt]   B= [oss, ta, det ,.. ]



2- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [oss, ta, det ,.. ]



3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [oss]   B= [ta, det, på ,.. ]



4- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ta, det, på ,.. ]



5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ta]   B= [det, på, allvar ,.. ]



6- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ta, det]   B= [på, allvar, . ,.. ]



7- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ta]   B= [på, allvar, . ,.. ]



8- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ta, på]   B= [allvar, . ,.. ]



9- **WHITE_MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[ta, på]]   B= [allvar, . ,.. ]



10- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[ta, på]  allvar]   B= [.]



11- **MERGE_AS_OTH**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[[ta, på]  allvar]]   B= [.]



12- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [.]



13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [ ]



14- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

#Oracle problem
## Sentence No. 85 - 
vem kan väl **ha** något **emot** det positiva ordet ” öppna ” ? 
### Existing MWEs: 
1- **ha emot** (VPC)

black Merge Num : 2 Interleaving Num: 0


0- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [vem, kan, väl ,.. ]



1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [vem]   B= [kan, väl, ha ,.. ]



2- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [kan, väl, ha ,.. ]



3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [kan]   B= [väl, ha, något ,.. ]



4- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [väl, ha, något ,.. ]



5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [väl]   B= [ha, något, emot ,.. ]



6- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ha, något, emot ,.. ]



7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ha]   B= [något, emot, det ,.. ]



8- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ha, något]   B= [emot, det, positiva ,.. ]



9- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ha]   B= [emot, det, positiva ,.. ]



10- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ha, emot]   B= [det, positiva, ordet ,.. ]



11- **MERGE_AS_OTH**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[ha, emot]]   B= [det, positiva, ordet ,.. ]



12- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [det, positiva, ordet ,.. ]



13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [det]   B= [positiva, ordet, ” ,.. ]



14- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [positiva, ordet, ” ,.. ]



15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [positiva]   B= [ordet, ”, öppna ,.. ]



16- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ordet, ”, öppna ,.. ]



17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ordet]   B= [”, öppna, ” ,.. ]



18- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [”, öppna, ” ,.. ]



19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [”]   B= [öppna, ”, ? ,.. ]



20- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [öppna, ”, ? ,.. ]



21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [öppna]   B= [”, ? ,.. ]



22- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [”, ? ,.. ]



23- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [”]   B= [?]



24- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [?]



25- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [?]   B= [ ]



26- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

#Oracle problem
## Sentence No. 86 - 
polisen **träffade** **på** honom utanför hans hem tidigare i veckan och tyckte han verkade påverkad av narkotika . 
### Existing MWEs: 
1- **träffade på** (VPC)

black Merge Num : 2 Interleaving Num: 0


0- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [polisen, träffade, på ,.. ]



1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [polisen]   B= [träffade, på, honom ,.. ]



2- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [träffade, på, honom ,.. ]



3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [träffade]   B= [på, honom, utanför ,.. ]



4- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [träffade, på]   B= [honom, utanför, hans ,.. ]



5- **MERGE_AS_OTH**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[träffade, på]]   B= [honom, utanför, hans ,.. ]



6- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [honom, utanför, hans ,.. ]



7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [honom]   B= [utanför, hans, hem ,.. ]



8- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [utanför, hans, hem ,.. ]



9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [utanför]   B= [hans, hem, tidigare ,.. ]



10- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [hans, hem, tidigare ,.. ]



11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [hans]   B= [hem, tidigare, i ,.. ]



12- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [hem, tidigare, i ,.. ]



13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [hem]   B= [tidigare, i, veckan ,.. ]



14- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [tidigare, i, veckan ,.. ]



15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [tidigare]   B= [i, veckan, och ,.. ]



16- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [i, veckan, och ,.. ]



17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [i]   B= [veckan, och, tyckte ,.. ]



18- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [veckan, och, tyckte ,.. ]



19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [veckan]   B= [och, tyckte, han ,.. ]



20- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [och, tyckte, han ,.. ]



21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [och]   B= [tyckte, han, verkade ,.. ]



22- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [tyckte, han, verkade ,.. ]



23- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [tyckte]   B= [han, verkade, påverkad ,.. ]



24- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [han, verkade, påverkad ,.. ]



25- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [han]   B= [verkade, påverkad, av ,.. ]



26- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [verkade, påverkad, av ,.. ]



27- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [verkade]   B= [påverkad, av, narkotika ,.. ]



28- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [påverkad, av, narkotika ,.. ]



29- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [påverkad]   B= [av, narkotika, . ,.. ]



30- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [av, narkotika, . ,.. ]



31- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [av]   B= [narkotika, . ,.. ]



32- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [narkotika, . ,.. ]



33- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [narkotika]   B= [.]



34- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [.]



35- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [ ]



36- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

#Oracle problem
## Sentence No. 94 - 
skene : ledningen på badhuset kaskad i skene ska **se** **över** rutiner och information till föräldrar efter incidenten på fredagen , då en femårig pojke hittades livlös i en av bassängerna . 
### Existing MWEs: 
1- **se över** (VPC)

black Merge Num : 2 Interleaving Num: 0


0- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [skene, :, ledningen ,.. ]



1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [skene]   B= [:, ledningen, på ,.. ]



2- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [:, ledningen, på ,.. ]



3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [:]   B= [ledningen, på, badhuset ,.. ]



4- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ledningen, på, badhuset ,.. ]



5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ledningen]   B= [på, badhuset, kaskad ,.. ]



6- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [på, badhuset, kaskad ,.. ]



7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [på]   B= [badhuset, kaskad, i ,.. ]



8- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [badhuset, kaskad, i ,.. ]



9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [badhuset]   B= [kaskad, i, skene ,.. ]



10- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [kaskad, i, skene ,.. ]



11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [kaskad]   B= [i, skene, ska ,.. ]



12- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [i, skene, ska ,.. ]



13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [i]   B= [skene, ska, se ,.. ]



14- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [skene, ska, se ,.. ]



15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [skene]   B= [ska, se, över ,.. ]



16- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ska, se, över ,.. ]



17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ska]   B= [se, över, rutiner ,.. ]



18- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [se, över, rutiner ,.. ]



19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [se]   B= [över, rutiner, och ,.. ]



20- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [se, över]   B= [rutiner, och, information ,.. ]



21- **MERGE_AS_OTH**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[se, över]]   B= [rutiner, och, information ,.. ]



22- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [rutiner, och, information ,.. ]



23- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [rutiner]   B= [och, information, till ,.. ]



24- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [och, information, till ,.. ]



25- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [och]   B= [information, till, föräldrar ,.. ]



26- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [information, till, föräldrar ,.. ]



27- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [information]   B= [till, föräldrar, efter ,.. ]



28- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [till, föräldrar, efter ,.. ]



29- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [till]   B= [föräldrar, efter, incidenten ,.. ]



30- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [föräldrar, efter, incidenten ,.. ]



31- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [föräldrar]   B= [efter, incidenten, på ,.. ]



32- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [efter, incidenten, på ,.. ]



33- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [efter]   B= [incidenten, på, fredagen ,.. ]



34- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [incidenten, på, fredagen ,.. ]



35- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [incidenten]   B= [på, fredagen, , ,.. ]



36- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [på, fredagen, , ,.. ]



37- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [på]   B= [fredagen, ,, då ,.. ]



38- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [fredagen, ,, då ,.. ]



39- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [fredagen]   B= [,, då, en ,.. ]



40- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, då, en ,.. ]



41- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [då, en, femårig ,.. ]



42- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [då, en, femårig ,.. ]



43- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [då]   B= [en, femårig, pojke ,.. ]



44- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [en, femårig, pojke ,.. ]



45- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [en]   B= [femårig, pojke, hittades ,.. ]



46- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [femårig, pojke, hittades ,.. ]



47- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [femårig]   B= [pojke, hittades, livlös ,.. ]



48- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [pojke, hittades, livlös ,.. ]



49- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [pojke]   B= [hittades, livlös, i ,.. ]



50- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [hittades, livlös, i ,.. ]



51- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [hittades]   B= [livlös, i, en ,.. ]



52- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [livlös, i, en ,.. ]



53- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [livlös]   B= [i, en, av ,.. ]



54- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [i, en, av ,.. ]



55- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [i]   B= [en, av, bassängerna ,.. ]



56- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [en, av, bassängerna ,.. ]



57- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [en]   B= [av, bassängerna, . ,.. ]



58- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [av, bassängerna, . ,.. ]



59- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [av]   B= [bassängerna, . ,.. ]



60- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [bassängerna, . ,.. ]



61- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [bassängerna]   B= [.]



62- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [.]



63- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [ ]



64- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

#Oracle problem
## Sentence No. 98 - 
fysisk humor **går** alltid **hem** och jag har alltid älskat det . 
### Existing MWEs: 
1- **går hem** (VPC)

black Merge Num : 2 Interleaving Num: 0


0- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [fysisk, humor, går ,.. ]



1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [fysisk]   B= [humor, går, alltid ,.. ]



2- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [humor, går, alltid ,.. ]



3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [humor]   B= [går, alltid, hem ,.. ]



4- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [går, alltid, hem ,.. ]



5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [går]   B= [alltid, hem, och ,.. ]



6- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [går, alltid]   B= [hem, och, jag ,.. ]



7- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [går]   B= [hem, och, jag ,.. ]



8- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [går, hem]   B= [och, jag, har ,.. ]



9- **MERGE_AS_OTH**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[går, hem]]   B= [och, jag, har ,.. ]



10- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [och, jag, har ,.. ]



11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [och]   B= [jag, har, alltid ,.. ]



12- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [jag, har, alltid ,.. ]



13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [jag]   B= [har, alltid, älskat ,.. ]



14- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [har, alltid, älskat ,.. ]



15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [har]   B= [alltid, älskat, det ,.. ]



16- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [alltid, älskat, det ,.. ]



17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [alltid]   B= [älskat, det, . ,.. ]



18- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [älskat, det, . ,.. ]



19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [älskat]   B= [det, . ,.. ]



20- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [det, . ,.. ]



21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [det]   B= [.]



22- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [.]



23- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [ ]



24- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

#Oracle problem
## Sentence No. 110 - 
– … Är det nog fortfarande viktoria som **drar** **längsta** **strået** – åtminstone i det korta programmet , säger joshi helgesson och fortsätter : 
### Existing MWEs: 
1- **drar längsta strået** (ID)

black Merge Num : 2 Interleaving Num: 0


0- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [–, …, Är ,.. ]



1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [–]   B= […, Är, det ,.. ]



2- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= […, Är, det ,.. ]



3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= […]   B= [Är, det, nog ,.. ]



4- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Är, det, nog ,.. ]



5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Är]   B= [det, nog, fortfarande ,.. ]



6- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [det, nog, fortfarande ,.. ]



7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [det]   B= [nog, fortfarande, viktoria ,.. ]



8- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [nog, fortfarande, viktoria ,.. ]



9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [nog]   B= [fortfarande, viktoria, som ,.. ]



10- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [fortfarande, viktoria, som ,.. ]



11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [fortfarande]   B= [viktoria, som, drar ,.. ]



12- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [viktoria, som, drar ,.. ]



13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [viktoria]   B= [som, drar, längsta ,.. ]



14- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [som, drar, längsta ,.. ]



15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [som]   B= [drar, längsta, strået ,.. ]



16- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [drar, längsta, strået ,.. ]



17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [drar]   B= [längsta, strået, – ,.. ]



18- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [drar, längsta]   B= [strået, –, åtminstone ,.. ]



19- **WHITE_MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[drar, längsta]]   B= [strået, –, åtminstone ,.. ]



20- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[drar, längsta]  strået]   B= [–, åtminstone, i ,.. ]



21- **MERGE_AS_OTH**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[[drar, längsta]  strået]]   B= [–, åtminstone, i ,.. ]



22- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [–, åtminstone, i ,.. ]



23- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [–]   B= [åtminstone, i, det ,.. ]



24- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [åtminstone, i, det ,.. ]



25- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [åtminstone]   B= [i, det, korta ,.. ]



26- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [i, det, korta ,.. ]



27- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [i]   B= [det, korta, programmet ,.. ]



28- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [det, korta, programmet ,.. ]



29- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [det]   B= [korta, programmet, , ,.. ]



30- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [korta, programmet, , ,.. ]



31- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [korta]   B= [programmet, ,, säger ,.. ]



32- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [programmet, ,, säger ,.. ]



33- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [programmet]   B= [,, säger, joshi ,.. ]



34- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, säger, joshi ,.. ]



35- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [säger, joshi, helgesson ,.. ]



36- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [säger, joshi, helgesson ,.. ]



37- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [säger]   B= [joshi, helgesson, och ,.. ]



38- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [joshi, helgesson, och ,.. ]



39- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [joshi]   B= [helgesson, och, fortsätter ,.. ]



40- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [helgesson, och, fortsätter ,.. ]



41- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [helgesson]   B= [och, fortsätter, : ,.. ]



42- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [och, fortsätter, : ,.. ]



43- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [och]   B= [fortsätter, : ,.. ]



44- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [fortsätter, : ,.. ]



45- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [fortsätter]   B= [:]



46- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [:]



47- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [:]   B= [ ]



48- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

#Oracle problem
## Sentence No. 118 - 
fördelen med röstmeddelanden som **spelas** **in** och skickas är att de funkar även om man har dålig mobiltäckning . 
### Existing MWEs: 
1- **spelas in** (VPC)

black Merge Num : 2 Interleaving Num: 0


0- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [fördelen, med, röstmeddelanden ,.. ]



1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [fördelen]   B= [med, röstmeddelanden, som ,.. ]



2- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [med, röstmeddelanden, som ,.. ]



3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [med]   B= [röstmeddelanden, som, spelas ,.. ]



4- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [röstmeddelanden, som, spelas ,.. ]



5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [röstmeddelanden]   B= [som, spelas, in ,.. ]



6- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [som, spelas, in ,.. ]



7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [som]   B= [spelas, in, och ,.. ]



8- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [spelas, in, och ,.. ]



9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [spelas]   B= [in, och, skickas ,.. ]



10- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [spelas, in]   B= [och, skickas, är ,.. ]



11- **MERGE_AS_OTH**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[spelas, in]]   B= [och, skickas, är ,.. ]



12- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [och, skickas, är ,.. ]



13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [och]   B= [skickas, är, att ,.. ]



14- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [skickas, är, att ,.. ]



15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [skickas]   B= [är, att, de ,.. ]



16- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [är, att, de ,.. ]



17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [är]   B= [att, de, funkar ,.. ]



18- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [att, de, funkar ,.. ]



19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [att]   B= [de, funkar, även ,.. ]



20- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [de, funkar, även ,.. ]



21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [de]   B= [funkar, även, om ,.. ]



22- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [funkar, även, om ,.. ]



23- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [funkar]   B= [även, om, man ,.. ]



24- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [även, om, man ,.. ]



25- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [även]   B= [om, man, har ,.. ]



26- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [om, man, har ,.. ]



27- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [om]   B= [man, har, dålig ,.. ]



28- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [man, har, dålig ,.. ]



29- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [man]   B= [har, dålig, mobiltäckning ,.. ]



30- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [har, dålig, mobiltäckning ,.. ]



31- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [har]   B= [dålig, mobiltäckning, . ,.. ]



32- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [dålig, mobiltäckning, . ,.. ]



33- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [dålig]   B= [mobiltäckning, . ,.. ]



34- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [mobiltäckning, . ,.. ]



35- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [mobiltäckning]   B= [.]



36- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [.]



37- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [ ]



38- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

#Oracle problem
## Sentence No. 124 - 
annat var det 1976 när after dark tog sina första steg som dragshowgrupp , och 1980 när de **flyttade** **in** på hamburger börs . 
### Existing MWEs: 
1- **flyttade in** (VPC)

black Merge Num : 2 Interleaving Num: 0


0- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [annat, var, det ,.. ]



1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [annat]   B= [var, det, 1976 ,.. ]



2- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [var, det, 1976 ,.. ]



3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [var]   B= [det, 1976, när ,.. ]



4- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [det, 1976, när ,.. ]



5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [det]   B= [1976, när, after ,.. ]



6- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [1976, när, after ,.. ]



7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [1976]   B= [när, after, dark ,.. ]



8- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [när, after, dark ,.. ]



9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [när]   B= [after, dark, tog ,.. ]



10- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [after, dark, tog ,.. ]



11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [after]   B= [dark, tog, sina ,.. ]



12- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [dark, tog, sina ,.. ]



13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [dark]   B= [tog, sina, första ,.. ]



14- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [tog, sina, första ,.. ]



15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [tog]   B= [sina, första, steg ,.. ]



16- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [sina, första, steg ,.. ]



17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [sina]   B= [första, steg, som ,.. ]



18- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [första, steg, som ,.. ]



19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [första]   B= [steg, som, dragshowgrupp ,.. ]



20- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [steg, som, dragshowgrupp ,.. ]



21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [steg]   B= [som, dragshowgrupp, , ,.. ]



22- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [som, dragshowgrupp, , ,.. ]



23- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [som]   B= [dragshowgrupp, ,, och ,.. ]



24- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [dragshowgrupp, ,, och ,.. ]



25- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [dragshowgrupp]   B= [,, och, 1980 ,.. ]



26- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, och, 1980 ,.. ]



27- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [och, 1980, när ,.. ]



28- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [och, 1980, när ,.. ]



29- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [och]   B= [1980, när, de ,.. ]



30- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [1980, när, de ,.. ]



31- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [1980]   B= [när, de, flyttade ,.. ]



32- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [när, de, flyttade ,.. ]



33- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [när]   B= [de, flyttade, in ,.. ]



34- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [de, flyttade, in ,.. ]



35- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [de]   B= [flyttade, in, på ,.. ]



36- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [flyttade, in, på ,.. ]



37- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [flyttade]   B= [in, på, hamburger ,.. ]



38- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [flyttade, in]   B= [på, hamburger, börs ,.. ]



39- **MERGE_AS_OTH**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[flyttade, in]]   B= [på, hamburger, börs ,.. ]



40- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [på, hamburger, börs ,.. ]



41- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [på]   B= [hamburger, börs, . ,.. ]



42- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [hamburger, börs, . ,.. ]



43- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [hamburger]   B= [börs, . ,.. ]



44- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [börs, . ,.. ]



45- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [börs]   B= [.]



46- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [.]



47- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [ ]



48- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

#Oracle problem
## Sentence No. 133 - 
– de berättade att de hade klagat ända sedan verksamheten började utan att **få** **gehör** , säger frida nowotny . 
### Existing MWEs: 
1- **få gehör** (ID)

black Merge Num : 2 Interleaving Num: 0


0- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [–, de, berättade ,.. ]



1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [–]   B= [de, berättade, att ,.. ]



2- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [de, berättade, att ,.. ]



3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [de]   B= [berättade, att, de ,.. ]



4- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [berättade, att, de ,.. ]



5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [berättade]   B= [att, de, hade ,.. ]



6- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [att, de, hade ,.. ]



7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [att]   B= [de, hade, klagat ,.. ]



8- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [de, hade, klagat ,.. ]



9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [de]   B= [hade, klagat, ända ,.. ]



10- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [hade, klagat, ända ,.. ]



11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [hade]   B= [klagat, ända, sedan ,.. ]



12- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [klagat, ända, sedan ,.. ]



13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [klagat]   B= [ända, sedan, verksamheten ,.. ]



14- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ända, sedan, verksamheten ,.. ]



15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ända]   B= [sedan, verksamheten, började ,.. ]



16- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [sedan, verksamheten, började ,.. ]



17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [sedan]   B= [verksamheten, började, utan ,.. ]



18- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [verksamheten, började, utan ,.. ]



19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [verksamheten]   B= [började, utan, att ,.. ]



20- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [började, utan, att ,.. ]



21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [började]   B= [utan, att, få ,.. ]



22- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [utan, att, få ,.. ]



23- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [utan]   B= [att, få, gehör ,.. ]



24- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [att, få, gehör ,.. ]



25- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [att]   B= [få, gehör, , ,.. ]



26- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [få, gehör, , ,.. ]



27- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [få]   B= [gehör, ,, säger ,.. ]



28- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [få, gehör]   B= [,, säger, frida ,.. ]



29- **MERGE_AS_OTH**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[få, gehör]]   B= [,, säger, frida ,.. ]



30- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, säger, frida ,.. ]



31- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [säger, frida, nowotny ,.. ]



32- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [säger, frida, nowotny ,.. ]



33- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [säger]   B= [frida, nowotny, . ,.. ]



34- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [frida, nowotny, . ,.. ]



35- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [frida]   B= [nowotny, . ,.. ]



36- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [nowotny, . ,.. ]



37- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [nowotny]   B= [.]



38- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [.]



39- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [ ]



40- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

#Oracle problem
## Sentence No. 141 - 
inte bara genom det hårda arbete han visar här , utan också som center i frölundas förstakedja , som har **fått** **i** **gång** maskineriet ordentligt . 
### Existing MWEs: 
1- **fått i gång** (VPC)

black Merge Num : 2 Interleaving Num: 0


0- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [inte, bara, genom ,.. ]



1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [inte]   B= [bara, genom, det ,.. ]



2- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [bara, genom, det ,.. ]



3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [bara]   B= [genom, det, hårda ,.. ]



4- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [genom, det, hårda ,.. ]



5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [genom]   B= [det, hårda, arbete ,.. ]



6- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [det, hårda, arbete ,.. ]



7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [det]   B= [hårda, arbete, han ,.. ]



8- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [hårda, arbete, han ,.. ]



9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [hårda]   B= [arbete, han, visar ,.. ]



10- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [arbete, han, visar ,.. ]



11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [arbete]   B= [han, visar, här ,.. ]



12- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [han, visar, här ,.. ]



13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [han]   B= [visar, här, , ,.. ]



14- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [visar, här, , ,.. ]



15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [visar]   B= [här, ,, utan ,.. ]



16- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [här, ,, utan ,.. ]



17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [här]   B= [,, utan, också ,.. ]



18- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, utan, också ,.. ]



19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [utan, också, som ,.. ]



20- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [utan, också, som ,.. ]



21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [utan]   B= [också, som, center ,.. ]



22- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [också, som, center ,.. ]



23- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [också]   B= [som, center, i ,.. ]



24- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [som, center, i ,.. ]



25- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [som]   B= [center, i, frölundas ,.. ]



26- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [center, i, frölundas ,.. ]



27- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [center]   B= [i, frölundas, förstakedja ,.. ]



28- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [i, frölundas, förstakedja ,.. ]



29- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [i]   B= [frölundas, förstakedja, , ,.. ]



30- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [frölundas, förstakedja, , ,.. ]



31- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [frölundas]   B= [förstakedja, ,, som ,.. ]



32- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [förstakedja, ,, som ,.. ]



33- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [förstakedja]   B= [,, som, har ,.. ]



34- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, som, har ,.. ]



35- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [som, har, fått ,.. ]



36- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [som, har, fått ,.. ]



37- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [som]   B= [har, fått, i ,.. ]



38- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [har, fått, i ,.. ]



39- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [har]   B= [fått, i, gång ,.. ]



40- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [fått, i, gång ,.. ]



41- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [fått]   B= [i, gång, maskineriet ,.. ]



42- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [fått, i]   B= [gång, maskineriet, ordentligt ,.. ]



43- **WHITE_MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[fått, i]]   B= [gång, maskineriet, ordentligt ,.. ]



44- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[fått, i]  gång]   B= [maskineriet, ordentligt, . ,.. ]



45- **MERGE_AS_OTH**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[[fått, i]  gång]]   B= [maskineriet, ordentligt, . ,.. ]



46- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [maskineriet, ordentligt, . ,.. ]



47- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [maskineriet]   B= [ordentligt, . ,.. ]



48- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ordentligt, . ,.. ]



49- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ordentligt]   B= [.]



50- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [.]



51- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [ ]



52- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

#Oracle problem
## Sentence No. 144 - 
jag är positivt överraskad av hur skönt det faktiskt är , har inte gillat att **röra** **på** **mig** sedan jag spelade fotboll i tonåren . 
### Existing MWEs: 
1- **röra på mig** (ID)

black Merge Num : 2 Interleaving Num: 0


0- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [jag, är, positivt ,.. ]



1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [jag]   B= [är, positivt, överraskad ,.. ]



2- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [är, positivt, överraskad ,.. ]



3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [är]   B= [positivt, överraskad, av ,.. ]



4- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [positivt, överraskad, av ,.. ]



5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [positivt]   B= [överraskad, av, hur ,.. ]



6- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [överraskad, av, hur ,.. ]



7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [överraskad]   B= [av, hur, skönt ,.. ]



8- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [av, hur, skönt ,.. ]



9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [av]   B= [hur, skönt, det ,.. ]



10- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [hur, skönt, det ,.. ]



11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [hur]   B= [skönt, det, faktiskt ,.. ]



12- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [skönt, det, faktiskt ,.. ]



13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [skönt]   B= [det, faktiskt, är ,.. ]



14- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [det, faktiskt, är ,.. ]



15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [det]   B= [faktiskt, är, , ,.. ]



16- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [faktiskt, är, , ,.. ]



17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [faktiskt]   B= [är, ,, har ,.. ]



18- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [är, ,, har ,.. ]



19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [är]   B= [,, har, inte ,.. ]



20- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, har, inte ,.. ]



21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [har, inte, gillat ,.. ]



22- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [har, inte, gillat ,.. ]



23- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [har]   B= [inte, gillat, att ,.. ]



24- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [inte, gillat, att ,.. ]



25- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [inte]   B= [gillat, att, röra ,.. ]



26- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [gillat, att, röra ,.. ]



27- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [gillat]   B= [att, röra, på ,.. ]



28- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [att, röra, på ,.. ]



29- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [att]   B= [röra, på, mig ,.. ]



30- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [röra, på, mig ,.. ]



31- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [röra]   B= [på, mig, sedan ,.. ]



32- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [röra, på]   B= [mig, sedan, jag ,.. ]



33- **WHITE_MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[röra, på]]   B= [mig, sedan, jag ,.. ]



34- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[röra, på]  mig]   B= [sedan, jag, spelade ,.. ]



35- **MERGE_AS_OTH**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[[röra, på]  mig]]   B= [sedan, jag, spelade ,.. ]



36- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [sedan, jag, spelade ,.. ]



37- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [sedan]   B= [jag, spelade, fotboll ,.. ]



38- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [jag, spelade, fotboll ,.. ]



39- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [jag]   B= [spelade, fotboll, i ,.. ]



40- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [spelade, fotboll, i ,.. ]



41- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [spelade]   B= [fotboll, i, tonåren ,.. ]



42- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [fotboll, i, tonåren ,.. ]



43- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [fotboll]   B= [i, tonåren, . ,.. ]



44- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [i, tonåren, . ,.. ]



45- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [i]   B= [tonåren, . ,.. ]



46- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [tonåren, . ,.. ]



47- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [tonåren]   B= [.]



48- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [.]



49- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [ ]



50- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

#Oracle problem
## Sentence No. 148 - 
det **riktas** ibland **kritik** mot amorteringskrav , som att boendekostnader blir högre och unga köpare drabbas . 
### Existing MWEs: 
1- **riktas kritik** (LVC)

black Merge Num : 2 Interleaving Num: 0


0- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [det, riktas, ibland ,.. ]



1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [det]   B= [riktas, ibland, kritik ,.. ]



2- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [riktas, ibland, kritik ,.. ]



3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [riktas]   B= [ibland, kritik, mot ,.. ]



4- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [riktas, ibland]   B= [kritik, mot, amorteringskrav ,.. ]



5- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [riktas]   B= [kritik, mot, amorteringskrav ,.. ]



6- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [riktas, kritik]   B= [mot, amorteringskrav, , ,.. ]



7- **MERGE_AS_OTH**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[riktas, kritik]]   B= [mot, amorteringskrav, , ,.. ]



8- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [mot, amorteringskrav, , ,.. ]



9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [mot]   B= [amorteringskrav, ,, som ,.. ]



10- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [amorteringskrav, ,, som ,.. ]



11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [amorteringskrav]   B= [,, som, att ,.. ]



12- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, som, att ,.. ]



13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [som, att, boendekostnader ,.. ]



14- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [som, att, boendekostnader ,.. ]



15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [som]   B= [att, boendekostnader, blir ,.. ]



16- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [att, boendekostnader, blir ,.. ]



17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [att]   B= [boendekostnader, blir, högre ,.. ]



18- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [boendekostnader, blir, högre ,.. ]



19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [boendekostnader]   B= [blir, högre, och ,.. ]



20- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [blir, högre, och ,.. ]



21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [blir]   B= [högre, och, unga ,.. ]



22- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [högre, och, unga ,.. ]



23- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [högre]   B= [och, unga, köpare ,.. ]



24- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [och, unga, köpare ,.. ]



25- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [och]   B= [unga, köpare, drabbas ,.. ]



26- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [unga, köpare, drabbas ,.. ]



27- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [unga]   B= [köpare, drabbas, . ,.. ]



28- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [köpare, drabbas, . ,.. ]



29- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [köpare]   B= [drabbas, . ,.. ]



30- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [drabbas, . ,.. ]



31- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [drabbas]   B= [.]



32- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [.]



33- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [ ]



34- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

#Oracle problem
## Sentence No. 155 - 
en takfläkt **skapar** **illusionen** av en lätt bris och det hela känns förvånansvärt verklighetstroget . 
### Existing MWEs: 
1- **skapar illusionen** (LVC)

black Merge Num : 2 Interleaving Num: 0


0- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [en, takfläkt, skapar ,.. ]



1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [en]   B= [takfläkt, skapar, illusionen ,.. ]



2- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [takfläkt, skapar, illusionen ,.. ]



3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [takfläkt]   B= [skapar, illusionen, av ,.. ]



4- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [skapar, illusionen, av ,.. ]



5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [skapar]   B= [illusionen, av, en ,.. ]



6- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [skapar, illusionen]   B= [av, en, lätt ,.. ]



7- **MERGE_AS_OTH**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[skapar, illusionen]]   B= [av, en, lätt ,.. ]



8- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [av, en, lätt ,.. ]



9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [av]   B= [en, lätt, bris ,.. ]



10- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [en, lätt, bris ,.. ]



11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [en]   B= [lätt, bris, och ,.. ]



12- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [lätt, bris, och ,.. ]



13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [lätt]   B= [bris, och, det ,.. ]



14- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [bris, och, det ,.. ]



15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [bris]   B= [och, det, hela ,.. ]



16- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [och, det, hela ,.. ]



17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [och]   B= [det, hela, känns ,.. ]



18- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [det, hela, känns ,.. ]



19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [det]   B= [hela, känns, förvånansvärt ,.. ]



20- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [hela, känns, förvånansvärt ,.. ]



21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [hela]   B= [känns, förvånansvärt, verklighetstroget ,.. ]



22- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [känns, förvånansvärt, verklighetstroget ,.. ]



23- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [känns]   B= [förvånansvärt, verklighetstroget, . ,.. ]



24- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [förvånansvärt, verklighetstroget, . ,.. ]



25- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [förvånansvärt]   B= [verklighetstroget, . ,.. ]



26- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [verklighetstroget, . ,.. ]



27- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [verklighetstroget]   B= [.]



28- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [.]



29- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [ ]



30- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

#Oracle problem
## Sentence No. 165 - 
och har i så fall kenneth gustafsson och jesper florén **tagit** **över** den rollen i gais ? 
### Existing MWEs: 
1- **tagit över** (VPC)

black Merge Num : 2 Interleaving Num: 0


0- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [och, har, i ,.. ]



1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [och]   B= [har, i, så ,.. ]



2- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [har, i, så ,.. ]



3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [har]   B= [i, så, fall ,.. ]



4- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [i, så, fall ,.. ]



5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [i]   B= [så, fall, kenneth ,.. ]



6- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [så, fall, kenneth ,.. ]



7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [så]   B= [fall, kenneth, gustafsson ,.. ]



8- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [fall, kenneth, gustafsson ,.. ]



9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [fall]   B= [kenneth, gustafsson, och ,.. ]



10- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [kenneth, gustafsson, och ,.. ]



11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [kenneth]   B= [gustafsson, och, jesper ,.. ]



12- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [gustafsson, och, jesper ,.. ]



13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [gustafsson]   B= [och, jesper, florén ,.. ]



14- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [och, jesper, florén ,.. ]



15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [och]   B= [jesper, florén, tagit ,.. ]



16- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [jesper, florén, tagit ,.. ]



17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [jesper]   B= [florén, tagit, över ,.. ]



18- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [florén, tagit, över ,.. ]



19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [florén]   B= [tagit, över, den ,.. ]



20- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [tagit, över, den ,.. ]



21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [tagit]   B= [över, den, rollen ,.. ]



22- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [tagit, över]   B= [den, rollen, i ,.. ]



23- **MERGE_AS_OTH**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[tagit, över]]   B= [den, rollen, i ,.. ]



24- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [den, rollen, i ,.. ]



25- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [den]   B= [rollen, i, gais ,.. ]



26- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [rollen, i, gais ,.. ]



27- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [rollen]   B= [i, gais, ? ,.. ]



28- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [i, gais, ? ,.. ]



29- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [i]   B= [gais, ? ,.. ]



30- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [gais, ? ,.. ]



31- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [gais]   B= [?]



32- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [?]



33- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [?]   B= [ ]



34- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

#Oracle problem
## Sentence No. 167 - 
– vårt hopp var att sverige skulle tänka på de viktigare matcherna som kommer , så att vi **fick** **lov** att spela lite och så blev det , konstaterar norske tränaren espen tho . 
### Existing MWEs: 
1- **fick lov** (LVC)

black Merge Num : 2 Interleaving Num: 0


0- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [–, vårt, hopp ,.. ]



1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [–]   B= [vårt, hopp, var ,.. ]



2- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [vårt, hopp, var ,.. ]



3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [vårt]   B= [hopp, var, att ,.. ]



4- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [hopp, var, att ,.. ]



5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [hopp]   B= [var, att, sverige ,.. ]



6- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [var, att, sverige ,.. ]



7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [var]   B= [att, sverige, skulle ,.. ]



8- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [att, sverige, skulle ,.. ]



9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [att]   B= [sverige, skulle, tänka ,.. ]



10- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [sverige, skulle, tänka ,.. ]



11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [sverige]   B= [skulle, tänka, på ,.. ]



12- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [skulle, tänka, på ,.. ]



13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [skulle]   B= [tänka, på, de ,.. ]



14- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [tänka, på, de ,.. ]



15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [tänka]   B= [på, de, viktigare ,.. ]



16- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [på, de, viktigare ,.. ]



17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [på]   B= [de, viktigare, matcherna ,.. ]



18- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [de, viktigare, matcherna ,.. ]



19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [de]   B= [viktigare, matcherna, som ,.. ]



20- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [viktigare, matcherna, som ,.. ]



21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [viktigare]   B= [matcherna, som, kommer ,.. ]



22- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [matcherna, som, kommer ,.. ]



23- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [matcherna]   B= [som, kommer, , ,.. ]



24- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [som, kommer, , ,.. ]



25- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [som]   B= [kommer, ,, så ,.. ]



26- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [kommer, ,, så ,.. ]



27- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [kommer]   B= [,, så, att ,.. ]



28- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, så, att ,.. ]



29- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [så, att, vi ,.. ]



30- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [så, att, vi ,.. ]



31- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [så]   B= [att, vi, fick ,.. ]



32- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [att, vi, fick ,.. ]



33- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [att]   B= [vi, fick, lov ,.. ]



34- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [vi, fick, lov ,.. ]



35- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [vi]   B= [fick, lov, att ,.. ]



36- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [fick, lov, att ,.. ]



37- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [fick]   B= [lov, att, spela ,.. ]



38- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [fick, lov]   B= [att, spela, lite ,.. ]



39- **MERGE_AS_OTH**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[fick, lov]]   B= [att, spela, lite ,.. ]



40- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [att, spela, lite ,.. ]



41- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [att]   B= [spela, lite, och ,.. ]



42- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [spela, lite, och ,.. ]



43- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [spela]   B= [lite, och, så ,.. ]



44- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [lite, och, så ,.. ]



45- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [lite]   B= [och, så, blev ,.. ]



46- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [och, så, blev ,.. ]



47- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [och]   B= [så, blev, det ,.. ]



48- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [så, blev, det ,.. ]



49- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [så]   B= [blev, det, , ,.. ]



50- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [blev, det, , ,.. ]



51- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [blev]   B= [det, ,, konstaterar ,.. ]



52- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [det, ,, konstaterar ,.. ]



53- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [det]   B= [,, konstaterar, norske ,.. ]



54- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, konstaterar, norske ,.. ]



55- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [konstaterar, norske, tränaren ,.. ]



56- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [konstaterar, norske, tränaren ,.. ]



57- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [konstaterar]   B= [norske, tränaren, espen ,.. ]



58- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [norske, tränaren, espen ,.. ]



59- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [norske]   B= [tränaren, espen, tho ,.. ]



60- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [tränaren, espen, tho ,.. ]



61- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [tränaren]   B= [espen, tho, . ,.. ]



62- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [espen, tho, . ,.. ]



63- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [espen]   B= [tho, . ,.. ]



64- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [tho, . ,.. ]



65- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [tho]   B= [.]



66- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [.]



67- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [ ]



68- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

#Oracle problem
## Sentence No. 171 - 
att ge denna intresseorganisation makt över hur stor andel av kostnaderna som ska kunna **vältras** **över** på enskilda , är att **bygga** **in** jäv och risk för godtycke i systemet . 
### Existing MWEs: 
1- **vältras över** (VPC)

2- **bygga in** (VPC)

black Merge Num : 4 Interleaving Num: 0


0- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [att, ge, denna ,.. ]



1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [att]   B= [ge, denna, intresseorganisation ,.. ]



2- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ge, denna, intresseorganisation ,.. ]



3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ge]   B= [denna, intresseorganisation, makt ,.. ]



4- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [denna, intresseorganisation, makt ,.. ]



5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [denna]   B= [intresseorganisation, makt, över ,.. ]



6- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [intresseorganisation, makt, över ,.. ]



7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [intresseorganisation]   B= [makt, över, hur ,.. ]



8- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [makt, över, hur ,.. ]



9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [makt]   B= [över, hur, stor ,.. ]



10- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [över, hur, stor ,.. ]



11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [över]   B= [hur, stor, andel ,.. ]



12- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [hur, stor, andel ,.. ]



13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [hur]   B= [stor, andel, av ,.. ]



14- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [stor, andel, av ,.. ]



15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [stor]   B= [andel, av, kostnaderna ,.. ]



16- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [andel, av, kostnaderna ,.. ]



17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [andel]   B= [av, kostnaderna, som ,.. ]



18- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [av, kostnaderna, som ,.. ]



19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [av]   B= [kostnaderna, som, ska ,.. ]



20- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [kostnaderna, som, ska ,.. ]



21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [kostnaderna]   B= [som, ska, kunna ,.. ]



22- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [som, ska, kunna ,.. ]



23- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [som]   B= [ska, kunna, vältras ,.. ]



24- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ska, kunna, vältras ,.. ]



25- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ska]   B= [kunna, vältras, över ,.. ]



26- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [kunna, vältras, över ,.. ]



27- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [kunna]   B= [vältras, över, på ,.. ]



28- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [vältras, över, på ,.. ]



29- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [vältras]   B= [över, på, enskilda ,.. ]



30- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [vältras, över]   B= [på, enskilda, , ,.. ]



31- **MERGE_AS_OTH**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[vältras, över]]   B= [på, enskilda, , ,.. ]



32- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [på, enskilda, , ,.. ]



33- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [på]   B= [enskilda, ,, är ,.. ]



34- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [enskilda, ,, är ,.. ]



35- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [enskilda]   B= [,, är, att ,.. ]



36- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, är, att ,.. ]



37- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [är, att, bygga ,.. ]



38- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [är, att, bygga ,.. ]



39- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [är]   B= [att, bygga, in ,.. ]



40- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [att, bygga, in ,.. ]



41- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [att]   B= [bygga, in, jäv ,.. ]



42- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [bygga, in, jäv ,.. ]



43- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [bygga]   B= [in, jäv, och ,.. ]



44- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [bygga, in]   B= [jäv, och, risk ,.. ]



45- **MERGE_AS_OTH**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[bygga, in]]   B= [jäv, och, risk ,.. ]



46- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [jäv, och, risk ,.. ]



47- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [jäv]   B= [och, risk, för ,.. ]



48- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [och, risk, för ,.. ]



49- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [och]   B= [risk, för, godtycke ,.. ]



50- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [risk, för, godtycke ,.. ]



51- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [risk]   B= [för, godtycke, i ,.. ]



52- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [för, godtycke, i ,.. ]



53- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [för]   B= [godtycke, i, systemet ,.. ]



54- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [godtycke, i, systemet ,.. ]



55- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [godtycke]   B= [i, systemet, . ,.. ]



56- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [i, systemet, . ,.. ]



57- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [i]   B= [systemet, . ,.. ]



58- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [systemet, . ,.. ]



59- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [systemet]   B= [.]



60- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [.]



61- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [ ]



62- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

