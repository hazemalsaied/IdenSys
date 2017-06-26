#Oracle problem
## Sentence No. 3 - 
Ägarna säger : flera klubbar **går** så mycket **minus** att vi sparar pengar på att inte spela alls . 
### Existing MWEs: 
1- **går minus** (ID)

black Merge Num : 3 Interleaving Num: 0


0- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Ägarna, säger, : ,.. ]



1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Ägarna]   B= [säger, :, flera ,.. ]



2- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [säger, :, flera ,.. ]



3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [säger]   B= [:, flera, klubbar ,.. ]



4- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [:, flera, klubbar ,.. ]



5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [:]   B= [flera, klubbar, går ,.. ]



6- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [flera, klubbar, går ,.. ]



7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [flera]   B= [klubbar, går, så ,.. ]



8- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [klubbar, går, så ,.. ]



9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [klubbar]   B= [går, så, mycket ,.. ]



10- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [går, så, mycket ,.. ]



11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [går]   B= [så, mycket, minus ,.. ]



12- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [går, så]   B= [mycket, minus, att ,.. ]



13- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [går]   B= [mycket, minus, att ,.. ]



14- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [går, mycket]   B= [minus, att, vi ,.. ]



15- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [går]   B= [minus, att, vi ,.. ]



16- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [går, minus]   B= [att, vi, sparar ,.. ]



17- **MERGE_AS_OTH**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[går, minus]]   B= [att, vi, sparar ,.. ]



18- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [att, vi, sparar ,.. ]



19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [att]   B= [vi, sparar, pengar ,.. ]



20- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [vi, sparar, pengar ,.. ]



21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [vi]   B= [sparar, pengar, på ,.. ]



22- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [sparar, pengar, på ,.. ]



23- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [sparar]   B= [pengar, på, att ,.. ]



24- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [pengar, på, att ,.. ]



25- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [pengar]   B= [på, att, inte ,.. ]



26- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [på, att, inte ,.. ]



27- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [på]   B= [att, inte, spela ,.. ]



28- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [att, inte, spela ,.. ]



29- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [att]   B= [inte, spela, alls ,.. ]



30- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [inte, spela, alls ,.. ]



31- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [inte]   B= [spela, alls, . ,.. ]



32- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [spela, alls, . ,.. ]



33- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [spela]   B= [alls, . ,.. ]



34- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [alls, . ,.. ]



35- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [alls]   B= [.]



36- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [.]



37- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [ ]



38- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

#Oracle problem
## Sentence No. 4 - 
dela resterande clementiner genom att **skära** **av** toppen . 
### Existing MWEs: 
1- **skära av** (VPC)

black Merge Num : 3 Interleaving Num: 0


0- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [dela, resterande, clementiner ,.. ]



1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [dela]   B= [resterande, clementiner, genom ,.. ]



2- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [resterande, clementiner, genom ,.. ]



3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [resterande]   B= [clementiner, genom, att ,.. ]



4- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [clementiner, genom, att ,.. ]



5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [clementiner]   B= [genom, att, skära ,.. ]



6- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [genom, att, skära ,.. ]



7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [genom]   B= [att, skära, av ,.. ]



8- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [att, skära, av ,.. ]



9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [att]   B= [skära, av, toppen ,.. ]



10- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [skära, av, toppen ,.. ]



11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [skära]   B= [av, toppen, . ,.. ]



12- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [skära, av]   B= [toppen, . ,.. ]



13- **MERGE_AS_OTH**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[skära, av]]   B= [toppen, . ,.. ]



14- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [toppen, . ,.. ]



15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [toppen]   B= [.]



16- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [.]



17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [ ]



18- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

#Oracle problem
## Sentence No. 6 - 
vi väljare **har** **möjligheten** att skicka centern dit de **hör** **hemma** , nämligen ut ur riksdagen år 2014 . 
### Existing MWEs: 
1- **har möjligheten hör hemma** (VPC)

black Merge Num : 3 Interleaving Num: 0


0- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [vi, väljare, har ,.. ]



1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [vi]   B= [väljare, har, möjligheten ,.. ]



2- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [väljare, har, möjligheten ,.. ]



3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [väljare]   B= [har, möjligheten, att ,.. ]



4- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [har, möjligheten, att ,.. ]



5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [har]   B= [möjligheten, att, skicka ,.. ]



6- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [har, möjligheten]   B= [att, skicka, centern ,.. ]



7- **WHITE_MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[har, möjligheten]]   B= [att, skicka, centern ,.. ]



8- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[har, möjligheten]  att]   B= [skicka, centern, dit ,.. ]



9- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[har, möjligheten]]   B= [skicka, centern, dit ,.. ]



10- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[har, möjligheten]  skicka]   B= [centern, dit, de ,.. ]



11- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[har, möjligheten]]   B= [centern, dit, de ,.. ]



12- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[har, möjligheten]  centern]   B= [dit, de, hör ,.. ]



13- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[har, möjligheten]]   B= [dit, de, hör ,.. ]



14- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[har, möjligheten]  dit]   B= [de, hör, hemma ,.. ]



15- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[har, möjligheten]]   B= [de, hör, hemma ,.. ]



16- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[har, möjligheten]  de]   B= [hör, hemma, , ,.. ]



17- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[har, möjligheten]]   B= [hör, hemma, , ,.. ]



18- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[har, möjligheten]  hör]   B= [hemma, ,, nämligen ,.. ]



19- **WHITE_MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[[har, möjligheten]  hör]]   B= [hemma, ,, nämligen ,.. ]



20- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[[har, möjligheten]  hör]  hemma]   B= [,, nämligen, ut ,.. ]



21- **MERGE_AS_OTH**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[[[har, möjligheten]  hör]  hemma]]   B= [,, nämligen, ut ,.. ]



22- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, nämligen, ut ,.. ]



23- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [nämligen, ut, ur ,.. ]



24- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [nämligen, ut, ur ,.. ]



25- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [nämligen]   B= [ut, ur, riksdagen ,.. ]



26- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ut, ur, riksdagen ,.. ]



27- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ut]   B= [ur, riksdagen, år ,.. ]



28- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ur, riksdagen, år ,.. ]



29- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ur]   B= [riksdagen, år, 2014 ,.. ]



30- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [riksdagen, år, 2014 ,.. ]



31- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [riksdagen]   B= [år, 2014, . ,.. ]



32- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [år, 2014, . ,.. ]



33- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [år]   B= [2014, . ,.. ]



34- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [2014, . ,.. ]



35- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [2014]   B= [.]



36- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [.]



37- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [ ]



38- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

#Oracle problem
## Sentence No. 12 - 
det går inte att **komma** **igång** med appen utan att först skapa ett konto och **lägga** **till** bilen i datorn . 
### Existing MWEs: 
1- **komma igång** (VPC)

2- **lägga till** (VPC)

black Merge Num : 6 Interleaving Num: 0


0- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [det, går, inte ,.. ]



1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [det]   B= [går, inte, att ,.. ]



2- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [går, inte, att ,.. ]



3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [går]   B= [inte, att, komma ,.. ]



4- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [inte, att, komma ,.. ]



5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [inte]   B= [att, komma, igång ,.. ]



6- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [att, komma, igång ,.. ]



7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [att]   B= [komma, igång, med ,.. ]



8- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [komma, igång, med ,.. ]



9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [komma]   B= [igång, med, appen ,.. ]



10- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [komma, igång]   B= [med, appen, utan ,.. ]



11- **MERGE_AS_OTH**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[komma, igång]]   B= [med, appen, utan ,.. ]



12- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [med, appen, utan ,.. ]



13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [med]   B= [appen, utan, att ,.. ]



14- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [appen, utan, att ,.. ]



15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [appen]   B= [utan, att, först ,.. ]



16- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [utan, att, först ,.. ]



17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [utan]   B= [att, först, skapa ,.. ]



18- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [att, först, skapa ,.. ]



19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [att]   B= [först, skapa, ett ,.. ]



20- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [först, skapa, ett ,.. ]



21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [först]   B= [skapa, ett, konto ,.. ]



22- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [skapa, ett, konto ,.. ]



23- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [skapa]   B= [ett, konto, och ,.. ]



24- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ett, konto, och ,.. ]



25- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ett]   B= [konto, och, lägga ,.. ]



26- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [konto, och, lägga ,.. ]



27- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [konto]   B= [och, lägga, till ,.. ]



28- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [och, lägga, till ,.. ]



29- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [och]   B= [lägga, till, bilen ,.. ]



30- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [lägga, till, bilen ,.. ]



31- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [lägga]   B= [till, bilen, i ,.. ]



32- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [lägga, till]   B= [bilen, i, datorn ,.. ]



33- **MERGE_AS_OTH**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[lägga, till]]   B= [bilen, i, datorn ,.. ]



34- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [bilen, i, datorn ,.. ]



35- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [bilen]   B= [i, datorn, . ,.. ]



36- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [i, datorn, . ,.. ]



37- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [i]   B= [datorn, . ,.. ]



38- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [datorn, . ,.. ]



39- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [datorn]   B= [.]



40- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [.]



41- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [ ]



42- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

#Oracle problem
## Sentence No. 20 - 
att **lära** **ut** miljökunskap och sopsortering med hjälp av en hund har många fördelar enligt anders lundberg . 
### Existing MWEs: 
1- **lära ut** (VPC)

black Merge Num : 3 Interleaving Num: 0


0- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [att, lära, ut ,.. ]



1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [att]   B= [lära, ut, miljökunskap ,.. ]



2- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [lära, ut, miljökunskap ,.. ]



3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [lära]   B= [ut, miljökunskap, och ,.. ]



4- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [lära, ut]   B= [miljökunskap, och, sopsortering ,.. ]



5- **MERGE_AS_OTH**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[lära, ut]]   B= [miljökunskap, och, sopsortering ,.. ]



6- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [miljökunskap, och, sopsortering ,.. ]



7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [miljökunskap]   B= [och, sopsortering, med ,.. ]



8- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [och, sopsortering, med ,.. ]



9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [och]   B= [sopsortering, med, hjälp ,.. ]



10- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [sopsortering, med, hjälp ,.. ]



11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [sopsortering]   B= [med, hjälp, av ,.. ]



12- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [med, hjälp, av ,.. ]



13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [med]   B= [hjälp, av, en ,.. ]



14- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [hjälp, av, en ,.. ]



15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [hjälp]   B= [av, en, hund ,.. ]



16- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [av, en, hund ,.. ]



17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [av]   B= [en, hund, har ,.. ]



18- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [en, hund, har ,.. ]



19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [en]   B= [hund, har, många ,.. ]



20- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [hund, har, många ,.. ]



21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [hund]   B= [har, många, fördelar ,.. ]



22- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [har, många, fördelar ,.. ]



23- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [har]   B= [många, fördelar, enligt ,.. ]



24- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [många, fördelar, enligt ,.. ]



25- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [många]   B= [fördelar, enligt, anders ,.. ]



26- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [fördelar, enligt, anders ,.. ]



27- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [fördelar]   B= [enligt, anders, lundberg ,.. ]



28- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [enligt, anders, lundberg ,.. ]



29- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [enligt]   B= [anders, lundberg, . ,.. ]



30- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [anders, lundberg, . ,.. ]



31- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [anders]   B= [lundberg, . ,.. ]



32- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [lundberg, . ,.. ]



33- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [lundberg]   B= [.]



34- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [.]



35- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [ ]



36- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

#Oracle problem
## Sentence No. 22 - 
mats grauers och anderz larqvist , ordförande och klubbdirektör , **säger** **sig** inte ha **tagit** ett slutgiltigt **beslut** . 
### Existing MWEs: 
1- **säger sig** (IReflV)

2- **tagit beslut** (LVC)

black Merge Num : 6 Interleaving Num: 0


0- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [mats, grauers, och ,.. ]



1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [mats]   B= [grauers, och, anderz ,.. ]



2- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [grauers, och, anderz ,.. ]



3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [grauers]   B= [och, anderz, larqvist ,.. ]



4- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [och, anderz, larqvist ,.. ]



5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [och]   B= [anderz, larqvist, , ,.. ]



6- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [anderz, larqvist, , ,.. ]



7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [anderz]   B= [larqvist, ,, ordförande ,.. ]



8- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [larqvist, ,, ordförande ,.. ]



9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [larqvist]   B= [,, ordförande, och ,.. ]



10- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, ordförande, och ,.. ]



11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [ordförande, och, klubbdirektör ,.. ]



12- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ordförande, och, klubbdirektör ,.. ]



13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ordförande]   B= [och, klubbdirektör, , ,.. ]



14- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [och, klubbdirektör, , ,.. ]



15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [och]   B= [klubbdirektör, ,, säger ,.. ]



16- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [klubbdirektör, ,, säger ,.. ]



17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [klubbdirektör]   B= [,, säger, sig ,.. ]



18- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, säger, sig ,.. ]



19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [säger, sig, inte ,.. ]



20- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [säger, sig, inte ,.. ]



21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [säger]   B= [sig, inte, ha ,.. ]



22- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [säger, sig]   B= [inte, ha, tagit ,.. ]



23- **MERGE_AS_OTH**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[säger, sig]]   B= [inte, ha, tagit ,.. ]



24- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [inte, ha, tagit ,.. ]



25- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [inte]   B= [ha, tagit, ett ,.. ]



26- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ha, tagit, ett ,.. ]



27- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ha]   B= [tagit, ett, slutgiltigt ,.. ]



28- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [tagit, ett, slutgiltigt ,.. ]



29- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [tagit]   B= [ett, slutgiltigt, beslut ,.. ]



30- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [tagit, ett]   B= [slutgiltigt, beslut, . ,.. ]



31- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [tagit]   B= [slutgiltigt, beslut, . ,.. ]



32- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [tagit, slutgiltigt]   B= [beslut, . ,.. ]



33- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [tagit]   B= [beslut, . ,.. ]



34- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [tagit, beslut]   B= [.]



35- **MERGE_AS_OTH**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[tagit, beslut]]   B= [.]



36- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [.]



37- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [ ]



38- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

#Oracle problem
## Sentence No. 28 - 
i slutet av 1970-talet bildade han punkbandet bad boo band , som **spelade** **in** den egenhändigt skrivna låten knulla i bangkok . 
### Existing MWEs: 
1- **spelade in** (VPC)

black Merge Num : 3 Interleaving Num: 0


0- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [i, slutet, av ,.. ]



1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [i]   B= [slutet, av, 1970-talet ,.. ]



2- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [slutet, av, 1970-talet ,.. ]



3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [slutet]   B= [av, 1970-talet, bildade ,.. ]



4- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [av, 1970-talet, bildade ,.. ]



5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [av]   B= [1970-talet, bildade, han ,.. ]



6- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [1970-talet, bildade, han ,.. ]



7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [1970-talet]   B= [bildade, han, punkbandet ,.. ]



8- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [bildade, han, punkbandet ,.. ]



9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [bildade]   B= [han, punkbandet, bad ,.. ]



10- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [han, punkbandet, bad ,.. ]



11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [han]   B= [punkbandet, bad, boo ,.. ]



12- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [punkbandet, bad, boo ,.. ]



13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [punkbandet]   B= [bad, boo, band ,.. ]



14- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [bad, boo, band ,.. ]



15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [bad]   B= [boo, band, , ,.. ]



16- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [boo, band, , ,.. ]



17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [boo]   B= [band, ,, som ,.. ]



18- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [band, ,, som ,.. ]



19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [band]   B= [,, som, spelade ,.. ]



20- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, som, spelade ,.. ]



21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [som, spelade, in ,.. ]



22- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [som, spelade, in ,.. ]



23- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [som]   B= [spelade, in, den ,.. ]



24- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [spelade, in, den ,.. ]



25- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [spelade]   B= [in, den, egenhändigt ,.. ]



26- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [spelade, in]   B= [den, egenhändigt, skrivna ,.. ]



27- **MERGE_AS_OTH**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[spelade, in]]   B= [den, egenhändigt, skrivna ,.. ]



28- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [den, egenhändigt, skrivna ,.. ]



29- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [den]   B= [egenhändigt, skrivna, låten ,.. ]



30- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [egenhändigt, skrivna, låten ,.. ]



31- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [egenhändigt]   B= [skrivna, låten, knulla ,.. ]



32- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [skrivna, låten, knulla ,.. ]



33- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [skrivna]   B= [låten, knulla, i ,.. ]



34- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [låten, knulla, i ,.. ]



35- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [låten]   B= [knulla, i, bangkok ,.. ]



36- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [knulla, i, bangkok ,.. ]



37- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [knulla]   B= [i, bangkok, . ,.. ]



38- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [i, bangkok, . ,.. ]



39- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [i]   B= [bangkok, . ,.. ]



40- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [bangkok, . ,.. ]



41- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [bangkok]   B= [.]



42- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [.]



43- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [ ]



44- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

#Oracle problem
## Sentence No. 32 - 
en präst som **spelar** **med** , en annan som så småningom avslöjar att allt är en enda manipulation iscensatt av maktens hantlangare för att avleda en växande kritik mot pinochet . 
### Existing MWEs: 
1- **spelar med** (VPC)

black Merge Num : 3 Interleaving Num: 0


0- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [en, präst, som ,.. ]



1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [en]   B= [präst, som, spelar ,.. ]



2- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [präst, som, spelar ,.. ]



3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [präst]   B= [som, spelar, med ,.. ]



4- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [som, spelar, med ,.. ]



5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [som]   B= [spelar, med, , ,.. ]



6- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [spelar, med, , ,.. ]



7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [spelar]   B= [med, ,, en ,.. ]



8- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [spelar, med]   B= [,, en, annan ,.. ]



9- **MERGE_AS_OTH**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[spelar, med]]   B= [,, en, annan ,.. ]



10- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, en, annan ,.. ]



11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [en, annan, som ,.. ]



12- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [en, annan, som ,.. ]



13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [en]   B= [annan, som, så ,.. ]



14- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [annan, som, så ,.. ]



15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [annan]   B= [som, så, småningom ,.. ]



16- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [som, så, småningom ,.. ]



17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [som]   B= [så, småningom, avslöjar ,.. ]



18- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [så, småningom, avslöjar ,.. ]



19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [så]   B= [småningom, avslöjar, att ,.. ]



20- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [småningom, avslöjar, att ,.. ]



21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [småningom]   B= [avslöjar, att, allt ,.. ]



22- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [avslöjar, att, allt ,.. ]



23- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [avslöjar]   B= [att, allt, är ,.. ]



24- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [att, allt, är ,.. ]



25- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [att]   B= [allt, är, en ,.. ]



26- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [allt, är, en ,.. ]



27- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [allt]   B= [är, en, enda ,.. ]



28- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [är, en, enda ,.. ]



29- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [är]   B= [en, enda, manipulation ,.. ]



30- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [en, enda, manipulation ,.. ]



31- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [en]   B= [enda, manipulation, iscensatt ,.. ]



32- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [enda, manipulation, iscensatt ,.. ]



33- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [enda]   B= [manipulation, iscensatt, av ,.. ]



34- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [manipulation, iscensatt, av ,.. ]



35- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [manipulation]   B= [iscensatt, av, maktens ,.. ]



36- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [iscensatt, av, maktens ,.. ]



37- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [iscensatt]   B= [av, maktens, hantlangare ,.. ]



38- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [av, maktens, hantlangare ,.. ]



39- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [av]   B= [maktens, hantlangare, för ,.. ]



40- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [maktens, hantlangare, för ,.. ]



41- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [maktens]   B= [hantlangare, för, att ,.. ]



42- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [hantlangare, för, att ,.. ]



43- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [hantlangare]   B= [för, att, avleda ,.. ]



44- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [för, att, avleda ,.. ]



45- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [för]   B= [att, avleda, en ,.. ]



46- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [att, avleda, en ,.. ]



47- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [att]   B= [avleda, en, växande ,.. ]



48- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [avleda, en, växande ,.. ]



49- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [avleda]   B= [en, växande, kritik ,.. ]



50- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [en, växande, kritik ,.. ]



51- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [en]   B= [växande, kritik, mot ,.. ]



52- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [växande, kritik, mot ,.. ]



53- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [växande]   B= [kritik, mot, pinochet ,.. ]



54- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [kritik, mot, pinochet ,.. ]



55- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [kritik]   B= [mot, pinochet, . ,.. ]



56- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [mot, pinochet, . ,.. ]



57- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [mot]   B= [pinochet, . ,.. ]



58- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [pinochet, . ,.. ]



59- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [pinochet]   B= [.]



60- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [.]



61- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [ ]



62- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

#Oracle problem
## Sentence No. 34 - 
exempelvis **erbjöd** **sig** ryssland , som ofta bromsat västmakternas planer på militära ingripanden , i går att **hjälpa** **till** med att transportera franska soldater till mali . 
### Existing MWEs: 
1- **erbjöd sig** (IReflV)

2- **hjälpa till** (VPC)

black Merge Num : 6 Interleaving Num: 0


0- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [exempelvis, erbjöd, sig ,.. ]



1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [exempelvis]   B= [erbjöd, sig, ryssland ,.. ]



2- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [erbjöd, sig, ryssland ,.. ]



3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [erbjöd]   B= [sig, ryssland, , ,.. ]



4- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [erbjöd, sig]   B= [ryssland, ,, som ,.. ]



5- **MERGE_AS_OTH**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[erbjöd, sig]]   B= [ryssland, ,, som ,.. ]



6- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ryssland, ,, som ,.. ]



7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ryssland]   B= [,, som, ofta ,.. ]



8- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, som, ofta ,.. ]



9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [som, ofta, bromsat ,.. ]



10- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [som, ofta, bromsat ,.. ]



11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [som]   B= [ofta, bromsat, västmakternas ,.. ]



12- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ofta, bromsat, västmakternas ,.. ]



13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ofta]   B= [bromsat, västmakternas, planer ,.. ]



14- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [bromsat, västmakternas, planer ,.. ]



15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [bromsat]   B= [västmakternas, planer, på ,.. ]



16- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [västmakternas, planer, på ,.. ]



17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [västmakternas]   B= [planer, på, militära ,.. ]



18- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [planer, på, militära ,.. ]



19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [planer]   B= [på, militära, ingripanden ,.. ]



20- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [på, militära, ingripanden ,.. ]



21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [på]   B= [militära, ingripanden, , ,.. ]



22- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [militära, ingripanden, , ,.. ]



23- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [militära]   B= [ingripanden, ,, i ,.. ]



24- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ingripanden, ,, i ,.. ]



25- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ingripanden]   B= [,, i, går ,.. ]



26- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, i, går ,.. ]



27- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [i, går, att ,.. ]



28- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [i, går, att ,.. ]



29- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [i]   B= [går, att, hjälpa ,.. ]



30- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [går, att, hjälpa ,.. ]



31- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [går]   B= [att, hjälpa, till ,.. ]



32- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [att, hjälpa, till ,.. ]



33- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [att]   B= [hjälpa, till, med ,.. ]



34- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [hjälpa, till, med ,.. ]



35- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [hjälpa]   B= [till, med, att ,.. ]



36- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [hjälpa, till]   B= [med, att, transportera ,.. ]



37- **MERGE_AS_OTH**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[hjälpa, till]]   B= [med, att, transportera ,.. ]



38- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [med, att, transportera ,.. ]



39- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [med]   B= [att, transportera, franska ,.. ]



40- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [att, transportera, franska ,.. ]



41- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [att]   B= [transportera, franska, soldater ,.. ]



42- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [transportera, franska, soldater ,.. ]



43- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [transportera]   B= [franska, soldater, till ,.. ]



44- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [franska, soldater, till ,.. ]



45- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [franska]   B= [soldater, till, mali ,.. ]



46- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [soldater, till, mali ,.. ]



47- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [soldater]   B= [till, mali, . ,.. ]



48- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [till, mali, . ,.. ]



49- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [till]   B= [mali, . ,.. ]



50- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [mali, . ,.. ]



51- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [mali]   B= [.]



52- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [.]



53- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [ ]



54- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

#Oracle problem
## Sentence No. 35 - 
**stänga** **av** en endaste minut – varför det ? 
### Existing MWEs: 
1- **stänga av** (VPC)

black Merge Num : 3 Interleaving Num: 0


0- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [stänga, av, en ,.. ]



1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [stänga]   B= [av, en, endaste ,.. ]



2- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [stänga, av]   B= [en, endaste, minut ,.. ]



3- **MERGE_AS_OTH**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[stänga, av]]   B= [en, endaste, minut ,.. ]



4- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [en, endaste, minut ,.. ]



5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [en]   B= [endaste, minut, – ,.. ]



6- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [endaste, minut, – ,.. ]



7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [endaste]   B= [minut, –, varför ,.. ]



8- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [minut, –, varför ,.. ]



9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [minut]   B= [–, varför, det ,.. ]



10- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [–, varför, det ,.. ]



11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [–]   B= [varför, det, ? ,.. ]



12- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [varför, det, ? ,.. ]



13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [varför]   B= [det, ? ,.. ]



14- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [det, ? ,.. ]



15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [det]   B= [?]



16- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [?]



17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [?]   B= [ ]



18- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

#Oracle problem
## Sentence No. 39 - 
de ska **ta** **reda** på hur man åkte hästdroska , hur man klädde sig till kalas , hur man beställde ett stop öl . 
### Existing MWEs: 
1- **ta reda** (VPC)

black Merge Num : 3 Interleaving Num: 0


0- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [de, ska, ta ,.. ]



1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [de]   B= [ska, ta, reda ,.. ]



2- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ska, ta, reda ,.. ]



3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ska]   B= [ta, reda, på ,.. ]



4- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ta, reda, på ,.. ]



5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ta]   B= [reda, på, hur ,.. ]



6- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ta, reda]   B= [på, hur, man ,.. ]



7- **MERGE_AS_OTH**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[ta, reda]]   B= [på, hur, man ,.. ]



8- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [på, hur, man ,.. ]



9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [på]   B= [hur, man, åkte ,.. ]



10- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [hur, man, åkte ,.. ]



11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [hur]   B= [man, åkte, hästdroska ,.. ]



12- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [man, åkte, hästdroska ,.. ]



13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [man]   B= [åkte, hästdroska, , ,.. ]



14- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [åkte, hästdroska, , ,.. ]



15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [åkte]   B= [hästdroska, ,, hur ,.. ]



16- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [hästdroska, ,, hur ,.. ]



17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [hästdroska]   B= [,, hur, man ,.. ]



18- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, hur, man ,.. ]



19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [hur, man, klädde ,.. ]



20- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [hur, man, klädde ,.. ]



21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [hur]   B= [man, klädde, sig ,.. ]



22- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [man, klädde, sig ,.. ]



23- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [man]   B= [klädde, sig, till ,.. ]



24- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [klädde, sig, till ,.. ]



25- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [klädde]   B= [sig, till, kalas ,.. ]



26- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [sig, till, kalas ,.. ]



27- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [sig]   B= [till, kalas, , ,.. ]



28- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [till, kalas, , ,.. ]



29- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [till]   B= [kalas, ,, hur ,.. ]



30- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [kalas, ,, hur ,.. ]



31- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [kalas]   B= [,, hur, man ,.. ]



32- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, hur, man ,.. ]



33- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [hur, man, beställde ,.. ]



34- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [hur, man, beställde ,.. ]



35- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [hur]   B= [man, beställde, ett ,.. ]



36- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [man, beställde, ett ,.. ]



37- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [man]   B= [beställde, ett, stop ,.. ]



38- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [beställde, ett, stop ,.. ]



39- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [beställde]   B= [ett, stop, öl ,.. ]



40- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ett, stop, öl ,.. ]



41- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ett]   B= [stop, öl, . ,.. ]



42- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [stop, öl, . ,.. ]



43- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [stop]   B= [öl, . ,.. ]



44- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [öl, . ,.. ]



45- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [öl]   B= [.]



46- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [.]



47- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [ ]



48- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

#Oracle problem
## Sentence No. 44 - 
eila **växte** **upp** i gullspång och mariestad . 
### Existing MWEs: 
1- **växte upp** (VPC)

black Merge Num : 3 Interleaving Num: 0


0- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [eila, växte, upp ,.. ]



1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [eila]   B= [växte, upp, i ,.. ]



2- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [växte, upp, i ,.. ]



3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [växte]   B= [upp, i, gullspång ,.. ]



4- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [växte, upp]   B= [i, gullspång, och ,.. ]



5- **MERGE_AS_OTH**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[växte, upp]]   B= [i, gullspång, och ,.. ]



6- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [i, gullspång, och ,.. ]



7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [i]   B= [gullspång, och, mariestad ,.. ]



8- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [gullspång, och, mariestad ,.. ]



9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [gullspång]   B= [och, mariestad, . ,.. ]



10- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [och, mariestad, . ,.. ]



11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [och]   B= [mariestad, . ,.. ]



12- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [mariestad, . ,.. ]



13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [mariestad]   B= [.]



14- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [.]



15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [ ]



16- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

#Oracle problem
## Sentence No. 45 - 
när du **kom** **med** på samma bussresa som jag förändrades mitt liv . 
### Existing MWEs: 
1- **kom med** (VPC)

black Merge Num : 3 Interleaving Num: 0


0- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [när, du, kom ,.. ]



1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [när]   B= [du, kom, med ,.. ]



2- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [du, kom, med ,.. ]



3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [du]   B= [kom, med, på ,.. ]



4- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [kom, med, på ,.. ]



5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [kom]   B= [med, på, samma ,.. ]



6- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [kom, med]   B= [på, samma, bussresa ,.. ]



7- **MERGE_AS_OTH**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[kom, med]]   B= [på, samma, bussresa ,.. ]



8- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [på, samma, bussresa ,.. ]



9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [på]   B= [samma, bussresa, som ,.. ]



10- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [samma, bussresa, som ,.. ]



11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [samma]   B= [bussresa, som, jag ,.. ]



12- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [bussresa, som, jag ,.. ]



13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [bussresa]   B= [som, jag, förändrades ,.. ]



14- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [som, jag, förändrades ,.. ]



15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [som]   B= [jag, förändrades, mitt ,.. ]



16- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [jag, förändrades, mitt ,.. ]



17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [jag]   B= [förändrades, mitt, liv ,.. ]



18- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [förändrades, mitt, liv ,.. ]



19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [förändrades]   B= [mitt, liv, . ,.. ]



20- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [mitt, liv, . ,.. ]



21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [mitt]   B= [liv, . ,.. ]



22- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [liv, . ,.. ]



23- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [liv]   B= [.]



24- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [.]



25- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [ ]



26- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

#Oracle problem
## Sentence No. 47 - 
teater : komedin ladykillers med bland andra ulla skoog och claes malmberg **ger** **sig** nu **ut** på riksteaterturné med start i varberg den 22 januari . 
### Existing MWEs: 
1- **ger sig ut** (ID)

black Merge Num : 3 Interleaving Num: 0


0- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [teater, :, komedin ,.. ]



1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [teater]   B= [:, komedin, ladykillers ,.. ]



2- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [:, komedin, ladykillers ,.. ]



3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [:]   B= [komedin, ladykillers, med ,.. ]



4- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [komedin, ladykillers, med ,.. ]



5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [komedin]   B= [ladykillers, med, bland ,.. ]



6- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ladykillers, med, bland ,.. ]



7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ladykillers]   B= [med, bland, andra ,.. ]



8- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [med, bland, andra ,.. ]



9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [med]   B= [bland, andra, ulla ,.. ]



10- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [bland, andra, ulla ,.. ]



11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [bland]   B= [andra, ulla, skoog ,.. ]



12- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [andra, ulla, skoog ,.. ]



13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [andra]   B= [ulla, skoog, och ,.. ]



14- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ulla, skoog, och ,.. ]



15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ulla]   B= [skoog, och, claes ,.. ]



16- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [skoog, och, claes ,.. ]



17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [skoog]   B= [och, claes, malmberg ,.. ]



18- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [och, claes, malmberg ,.. ]



19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [och]   B= [claes, malmberg, ger ,.. ]



20- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [claes, malmberg, ger ,.. ]



21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [claes]   B= [malmberg, ger, sig ,.. ]



22- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [malmberg, ger, sig ,.. ]



23- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [malmberg]   B= [ger, sig, nu ,.. ]



24- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ger, sig, nu ,.. ]



25- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ger]   B= [sig, nu, ut ,.. ]



26- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ger, sig]   B= [nu, ut, på ,.. ]



27- **WHITE_MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[ger, sig]]   B= [nu, ut, på ,.. ]



28- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[ger, sig]  nu]   B= [ut, på, riksteaterturné ,.. ]



29- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[ger, sig]]   B= [ut, på, riksteaterturné ,.. ]



30- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[ger, sig]  ut]   B= [på, riksteaterturné, med ,.. ]



31- **MERGE_AS_OTH**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[[ger, sig]  ut]]   B= [på, riksteaterturné, med ,.. ]



32- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [på, riksteaterturné, med ,.. ]



33- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [på]   B= [riksteaterturné, med, start ,.. ]



34- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [riksteaterturné, med, start ,.. ]



35- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [riksteaterturné]   B= [med, start, i ,.. ]



36- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [med, start, i ,.. ]



37- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [med]   B= [start, i, varberg ,.. ]



38- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [start, i, varberg ,.. ]



39- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [start]   B= [i, varberg, den ,.. ]



40- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [i, varberg, den ,.. ]



41- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [i]   B= [varberg, den, 22 ,.. ]



42- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [varberg, den, 22 ,.. ]



43- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [varberg]   B= [den, 22, januari ,.. ]



44- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [den, 22, januari ,.. ]



45- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [den]   B= [22, januari, . ,.. ]



46- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [22, januari, . ,.. ]



47- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [22]   B= [januari, . ,.. ]



48- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [januari, . ,.. ]



49- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [januari]   B= [.]



50- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [.]



51- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [ ]



52- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

#Oracle problem
## Sentence No. 49 - 
momentet **koppla** **ihop** och synka behövs inte längre . 
### Existing MWEs: 
1- **koppla ihop** (VPC)

black Merge Num : 3 Interleaving Num: 0


0- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [momentet, koppla, ihop ,.. ]



1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [momentet]   B= [koppla, ihop, och ,.. ]



2- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [koppla, ihop, och ,.. ]



3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [koppla]   B= [ihop, och, synka ,.. ]



4- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [koppla, ihop]   B= [och, synka, behövs ,.. ]



5- **MERGE_AS_OTH**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[koppla, ihop]]   B= [och, synka, behövs ,.. ]



6- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [och, synka, behövs ,.. ]



7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [och]   B= [synka, behövs, inte ,.. ]



8- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [synka, behövs, inte ,.. ]



9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [synka]   B= [behövs, inte, längre ,.. ]



10- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [behövs, inte, längre ,.. ]



11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [behövs]   B= [inte, längre, . ,.. ]



12- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [inte, längre, . ,.. ]



13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [inte]   B= [längre, . ,.. ]



14- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [längre, . ,.. ]



15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [längre]   B= [.]



16- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [.]



17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [ ]



18- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

#Oracle problem
## Sentence No. 54 - 
men oppositionen vädjar till regeringen att inte **ta** imf:s **lån** . 
### Existing MWEs: 
1- **ta lån** (LVC)

black Merge Num : 3 Interleaving Num: 0


0- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [men, oppositionen, vädjar ,.. ]



1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [men]   B= [oppositionen, vädjar, till ,.. ]



2- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [oppositionen, vädjar, till ,.. ]



3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [oppositionen]   B= [vädjar, till, regeringen ,.. ]



4- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [vädjar, till, regeringen ,.. ]



5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [vädjar]   B= [till, regeringen, att ,.. ]



6- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [till, regeringen, att ,.. ]



7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [till]   B= [regeringen, att, inte ,.. ]



8- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [regeringen, att, inte ,.. ]



9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [regeringen]   B= [att, inte, ta ,.. ]



10- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [att, inte, ta ,.. ]



11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [att]   B= [inte, ta, imf:s ,.. ]



12- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [inte, ta, imf:s ,.. ]



13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [inte]   B= [ta, imf:s, lån ,.. ]



14- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ta, imf:s, lån ,.. ]



15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ta]   B= [imf:s, lån, . ,.. ]



16- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ta, imf:s]   B= [lån, . ,.. ]



17- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ta]   B= [lån, . ,.. ]



18- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ta, lån]   B= [.]



19- **MERGE_AS_OTH**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[ta, lån]]   B= [.]



20- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [.]



21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [ ]



22- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

#Oracle problem
## Sentence No. 56 - 
då crashdiet redan hunnit med att **bocka** **av** stora poster på att göra-listan som att agera förband åt motley crue och spela på legendariska whisky a go go i los angeles är självförtroendet kanske inte helt ogrundat . 
### Existing MWEs: 
1- **bocka av** (VPC)

black Merge Num : 3 Interleaving Num: 0


0- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [då, crashdiet, redan ,.. ]



1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [då]   B= [crashdiet, redan, hunnit ,.. ]



2- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [crashdiet, redan, hunnit ,.. ]



3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [crashdiet]   B= [redan, hunnit, med ,.. ]



4- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [redan, hunnit, med ,.. ]



5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [redan]   B= [hunnit, med, att ,.. ]



6- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [hunnit, med, att ,.. ]



7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [hunnit]   B= [med, att, bocka ,.. ]



8- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [med, att, bocka ,.. ]



9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [med]   B= [att, bocka, av ,.. ]



10- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [att, bocka, av ,.. ]



11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [att]   B= [bocka, av, stora ,.. ]



12- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [bocka, av, stora ,.. ]



13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [bocka]   B= [av, stora, poster ,.. ]



14- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [bocka, av]   B= [stora, poster, på ,.. ]



15- **MERGE_AS_OTH**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[bocka, av]]   B= [stora, poster, på ,.. ]



16- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [stora, poster, på ,.. ]



17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [stora]   B= [poster, på, att ,.. ]



18- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [poster, på, att ,.. ]



19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [poster]   B= [på, att, göra-listan ,.. ]



20- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [på, att, göra-listan ,.. ]



21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [på]   B= [att, göra-listan, som ,.. ]



22- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [att, göra-listan, som ,.. ]



23- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [att]   B= [göra-listan, som, att ,.. ]



24- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [göra-listan, som, att ,.. ]



25- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [göra-listan]   B= [som, att, agera ,.. ]



26- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [som, att, agera ,.. ]



27- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [som]   B= [att, agera, förband ,.. ]



28- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [att, agera, förband ,.. ]



29- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [att]   B= [agera, förband, åt ,.. ]



30- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [agera, förband, åt ,.. ]



31- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [agera]   B= [förband, åt, motley ,.. ]



32- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [förband, åt, motley ,.. ]



33- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [förband]   B= [åt, motley, crue ,.. ]



34- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [åt, motley, crue ,.. ]



35- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [åt]   B= [motley, crue, och ,.. ]



36- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [motley, crue, och ,.. ]



37- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [motley]   B= [crue, och, spela ,.. ]



38- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [crue, och, spela ,.. ]



39- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [crue]   B= [och, spela, på ,.. ]



40- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [och, spela, på ,.. ]



41- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [och]   B= [spela, på, legendariska ,.. ]



42- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [spela, på, legendariska ,.. ]



43- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [spela]   B= [på, legendariska, whisky ,.. ]



44- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [på, legendariska, whisky ,.. ]



45- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [på]   B= [legendariska, whisky, a ,.. ]



46- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [legendariska, whisky, a ,.. ]



47- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [legendariska]   B= [whisky, a, go ,.. ]



48- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [whisky, a, go ,.. ]



49- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [whisky]   B= [a, go, go ,.. ]



50- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [a, go, go ,.. ]



51- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [a]   B= [go, go, i ,.. ]



52- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [go, go, i ,.. ]



53- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [go]   B= [go, i, los ,.. ]



54- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [go, i, los ,.. ]



55- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [go]   B= [i, los, angeles ,.. ]



56- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [i, los, angeles ,.. ]



57- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [i]   B= [los, angeles, är ,.. ]



58- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [los, angeles, är ,.. ]



59- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [los]   B= [angeles, är, självförtroendet ,.. ]



60- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [angeles, är, självförtroendet ,.. ]



61- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [angeles]   B= [är, självförtroendet, kanske ,.. ]



62- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [är, självförtroendet, kanske ,.. ]



63- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [är]   B= [självförtroendet, kanske, inte ,.. ]



64- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [självförtroendet, kanske, inte ,.. ]



65- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [självförtroendet]   B= [kanske, inte, helt ,.. ]



66- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [kanske, inte, helt ,.. ]



67- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [kanske]   B= [inte, helt, ogrundat ,.. ]



68- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [inte, helt, ogrundat ,.. ]



69- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [inte]   B= [helt, ogrundat, . ,.. ]



70- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [helt, ogrundat, . ,.. ]



71- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [helt]   B= [ogrundat, . ,.. ]



72- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ogrundat, . ,.. ]



73- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ogrundat]   B= [.]



74- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [.]



75- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [ ]



76- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

#Oracle problem
## Sentence No. 61 - 
det **avspeglar** **sig** också i den säsongsbetonade menyn som vi **borrade** **oss** **ner** i medan vi smååt av den goda brödkorgen med malt- , surdegs- och knäckebröd , och ett rört smör därtill . 
### Existing MWEs: 
1- **avspeglar sig** (IReflV)

2- **borrade oss ner** (ID)

black Merge Num : 6 Interleaving Num: 0


0- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [det, avspeglar, sig ,.. ]



1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [det]   B= [avspeglar, sig, också ,.. ]



2- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [avspeglar, sig, också ,.. ]



3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [avspeglar]   B= [sig, också, i ,.. ]



4- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [avspeglar, sig]   B= [också, i, den ,.. ]



5- **MERGE_AS_OTH**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[avspeglar, sig]]   B= [också, i, den ,.. ]



6- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [också, i, den ,.. ]



7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [också]   B= [i, den, säsongsbetonade ,.. ]



8- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [i, den, säsongsbetonade ,.. ]



9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [i]   B= [den, säsongsbetonade, menyn ,.. ]



10- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [den, säsongsbetonade, menyn ,.. ]



11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [den]   B= [säsongsbetonade, menyn, som ,.. ]



12- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [säsongsbetonade, menyn, som ,.. ]



13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [säsongsbetonade]   B= [menyn, som, vi ,.. ]



14- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [menyn, som, vi ,.. ]



15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [menyn]   B= [som, vi, borrade ,.. ]



16- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [som, vi, borrade ,.. ]



17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [som]   B= [vi, borrade, oss ,.. ]



18- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [vi, borrade, oss ,.. ]



19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [vi]   B= [borrade, oss, ner ,.. ]



20- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [borrade, oss, ner ,.. ]



21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [borrade]   B= [oss, ner, i ,.. ]



22- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [borrade, oss]   B= [ner, i, medan ,.. ]



23- **WHITE_MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[borrade, oss]]   B= [ner, i, medan ,.. ]



24- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[borrade, oss]  ner]   B= [i, medan, vi ,.. ]



25- **MERGE_AS_OTH**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[[borrade, oss]  ner]]   B= [i, medan, vi ,.. ]



26- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [i, medan, vi ,.. ]



27- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [i]   B= [medan, vi, smååt ,.. ]



28- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [medan, vi, smååt ,.. ]



29- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [medan]   B= [vi, smååt, av ,.. ]



30- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [vi, smååt, av ,.. ]



31- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [vi]   B= [smååt, av, den ,.. ]



32- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [smååt, av, den ,.. ]



33- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [smååt]   B= [av, den, goda ,.. ]



34- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [av, den, goda ,.. ]



35- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [av]   B= [den, goda, brödkorgen ,.. ]



36- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [den, goda, brödkorgen ,.. ]



37- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [den]   B= [goda, brödkorgen, med ,.. ]



38- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [goda, brödkorgen, med ,.. ]



39- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [goda]   B= [brödkorgen, med, malt- ,.. ]



40- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [brödkorgen, med, malt- ,.. ]



41- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [brödkorgen]   B= [med, malt-, , ,.. ]



42- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [med, malt-, , ,.. ]



43- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [med]   B= [malt-, ,, surdegs- ,.. ]



44- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [malt-, ,, surdegs- ,.. ]



45- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [malt-]   B= [,, surdegs-, och ,.. ]



46- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, surdegs-, och ,.. ]



47- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [surdegs-, och, knäckebröd ,.. ]



48- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [surdegs-, och, knäckebröd ,.. ]



49- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [surdegs-]   B= [och, knäckebröd, , ,.. ]



50- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [och, knäckebröd, , ,.. ]



51- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [och]   B= [knäckebröd, ,, och ,.. ]



52- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [knäckebröd, ,, och ,.. ]



53- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [knäckebröd]   B= [,, och, ett ,.. ]



54- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, och, ett ,.. ]



55- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [och, ett, rört ,.. ]



56- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [och, ett, rört ,.. ]



57- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [och]   B= [ett, rört, smör ,.. ]



58- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ett, rört, smör ,.. ]



59- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ett]   B= [rört, smör, därtill ,.. ]



60- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [rört, smör, därtill ,.. ]



61- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [rört]   B= [smör, därtill, . ,.. ]



62- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [smör, därtill, . ,.. ]



63- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [smör]   B= [därtill, . ,.. ]



64- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [därtill, . ,.. ]



65- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [därtill]   B= [.]



66- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [.]



67- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [ ]



68- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

#Oracle problem
## Sentence No. 67 - 
parkeringsplatserna ska vara trygga , av god kvalitet , ha väderskydd och det ska **finnas** **möjligheter** att **låsa** **in** eller **fast** cykeln . 
### Existing MWEs: 
1- **finnas möjligheter** (LVC)

2- **låsa in** (VPC)

3- **låsa fast** (VPC), Interleaving 

black Merge Num : 6 Interleaving Num: 1


0- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [parkeringsplatserna, ska, vara ,.. ]



1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [parkeringsplatserna]   B= [ska, vara, trygga ,.. ]



2- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ska, vara, trygga ,.. ]



3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ska]   B= [vara, trygga, , ,.. ]



4- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [vara, trygga, , ,.. ]



5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [vara]   B= [trygga, ,, av ,.. ]



6- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [trygga, ,, av ,.. ]



7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [trygga]   B= [,, av, god ,.. ]



8- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, av, god ,.. ]



9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [av, god, kvalitet ,.. ]



10- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [av, god, kvalitet ,.. ]



11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [av]   B= [god, kvalitet, , ,.. ]



12- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [god, kvalitet, , ,.. ]



13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [god]   B= [kvalitet, ,, ha ,.. ]



14- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [kvalitet, ,, ha ,.. ]



15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [kvalitet]   B= [,, ha, väderskydd ,.. ]



16- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, ha, väderskydd ,.. ]



17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [ha, väderskydd, och ,.. ]



18- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ha, väderskydd, och ,.. ]



19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ha]   B= [väderskydd, och, det ,.. ]



20- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [väderskydd, och, det ,.. ]



21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [väderskydd]   B= [och, det, ska ,.. ]



22- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [och, det, ska ,.. ]



23- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [och]   B= [det, ska, finnas ,.. ]



24- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [det, ska, finnas ,.. ]



25- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [det]   B= [ska, finnas, möjligheter ,.. ]



26- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ska, finnas, möjligheter ,.. ]



27- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ska]   B= [finnas, möjligheter, att ,.. ]



28- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [finnas, möjligheter, att ,.. ]



29- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [finnas]   B= [möjligheter, att, låsa ,.. ]



30- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [finnas, möjligheter]   B= [att, låsa, in ,.. ]



31- **MERGE_AS_OTH**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[finnas, möjligheter]]   B= [att, låsa, in ,.. ]



32- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [att, låsa, in ,.. ]



33- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [att]   B= [låsa, in, eller ,.. ]



34- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [låsa, in, eller ,.. ]



35- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [låsa]   B= [in, eller, fast ,.. ]



36- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [låsa, in]   B= [eller, fast, cykeln ,.. ]



37- **MERGE_AS_OTH**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[låsa, in]]   B= [eller, fast, cykeln ,.. ]



38- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [eller, fast, cykeln ,.. ]



39- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [eller]   B= [fast, cykeln, . ,.. ]



40- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [fast, cykeln, . ,.. ]



41- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [fast]   B= [cykeln, . ,.. ]



42- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [cykeln, . ,.. ]



43- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [cykeln]   B= [.]



44- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [.]



45- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [ ]



46- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

#Oracle problem
## Sentence No. 69 - 
först och främst måste man se det allmänna pensionssystemet som ett generationskontrakt där den yrkesverksamma generationen betalar de äldres pension och samtidigt **tar** **ansvar** för att **skapa** **förutsättning** för sin egen pension . 
### Existing MWEs: 
1- **tar ansvar** (LVC)

2- **skapa förutsättning** (LVC)

black Merge Num : 6 Interleaving Num: 0


0- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [först, och, främst ,.. ]



1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [först]   B= [och, främst, måste ,.. ]



2- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [och, främst, måste ,.. ]



3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [och]   B= [främst, måste, man ,.. ]



4- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [främst, måste, man ,.. ]



5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [främst]   B= [måste, man, se ,.. ]



6- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [måste, man, se ,.. ]



7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [måste]   B= [man, se, det ,.. ]



8- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [man, se, det ,.. ]



9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [man]   B= [se, det, allmänna ,.. ]



10- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [se, det, allmänna ,.. ]



11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [se]   B= [det, allmänna, pensionssystemet ,.. ]



12- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [det, allmänna, pensionssystemet ,.. ]



13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [det]   B= [allmänna, pensionssystemet, som ,.. ]



14- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [allmänna, pensionssystemet, som ,.. ]



15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [allmänna]   B= [pensionssystemet, som, ett ,.. ]



16- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [pensionssystemet, som, ett ,.. ]



17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [pensionssystemet]   B= [som, ett, generationskontrakt ,.. ]



18- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [som, ett, generationskontrakt ,.. ]



19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [som]   B= [ett, generationskontrakt, där ,.. ]



20- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ett, generationskontrakt, där ,.. ]



21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ett]   B= [generationskontrakt, där, den ,.. ]



22- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [generationskontrakt, där, den ,.. ]



23- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [generationskontrakt]   B= [där, den, yrkesverksamma ,.. ]



24- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [där, den, yrkesverksamma ,.. ]



25- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [där]   B= [den, yrkesverksamma, generationen ,.. ]



26- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [den, yrkesverksamma, generationen ,.. ]



27- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [den]   B= [yrkesverksamma, generationen, betalar ,.. ]



28- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [yrkesverksamma, generationen, betalar ,.. ]



29- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [yrkesverksamma]   B= [generationen, betalar, de ,.. ]



30- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [generationen, betalar, de ,.. ]



31- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [generationen]   B= [betalar, de, äldres ,.. ]



32- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [betalar, de, äldres ,.. ]



33- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [betalar]   B= [de, äldres, pension ,.. ]



34- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [de, äldres, pension ,.. ]



35- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [de]   B= [äldres, pension, och ,.. ]



36- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [äldres, pension, och ,.. ]



37- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [äldres]   B= [pension, och, samtidigt ,.. ]



38- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [pension, och, samtidigt ,.. ]



39- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [pension]   B= [och, samtidigt, tar ,.. ]



40- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [och, samtidigt, tar ,.. ]



41- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [och]   B= [samtidigt, tar, ansvar ,.. ]



42- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [samtidigt, tar, ansvar ,.. ]



43- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [samtidigt]   B= [tar, ansvar, för ,.. ]



44- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [tar, ansvar, för ,.. ]



45- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [tar]   B= [ansvar, för, att ,.. ]



46- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [tar, ansvar]   B= [för, att, skapa ,.. ]



47- **MERGE_AS_OTH**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[tar, ansvar]]   B= [för, att, skapa ,.. ]



48- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [för, att, skapa ,.. ]



49- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [för]   B= [att, skapa, förutsättning ,.. ]



50- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [att, skapa, förutsättning ,.. ]



51- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [att]   B= [skapa, förutsättning, för ,.. ]



52- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [skapa, förutsättning, för ,.. ]



53- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [skapa]   B= [förutsättning, för, sin ,.. ]



54- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [skapa, förutsättning]   B= [för, sin, egen ,.. ]



55- **MERGE_AS_OTH**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[skapa, förutsättning]]   B= [för, sin, egen ,.. ]



56- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [för, sin, egen ,.. ]



57- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [för]   B= [sin, egen, pension ,.. ]



58- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [sin, egen, pension ,.. ]



59- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [sin]   B= [egen, pension, . ,.. ]



60- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [egen, pension, . ,.. ]



61- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [egen]   B= [pension, . ,.. ]



62- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [pension, . ,.. ]



63- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [pension]   B= [.]



64- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [.]



65- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [ ]



66- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

#Oracle problem
## Sentence No. 70 - 
jag är en av dem som tyckt att mathias ranégie aldrig **fick** **chansen** på kamratgården , samtidigt ska man **komma** **ihåg** att det var när han blev knäskadad som marcus berg stod för det största genombrottet i allsvenskan på många år . 
### Existing MWEs: 
1- **fick chansen** (LVC)

2- **komma ihåg** (VPC)

black Merge Num : 6 Interleaving Num: 0


0- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [jag, är, en ,.. ]



1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [jag]   B= [är, en, av ,.. ]



2- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [är, en, av ,.. ]



3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [är]   B= [en, av, dem ,.. ]



4- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [en, av, dem ,.. ]



5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [en]   B= [av, dem, som ,.. ]



6- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [av, dem, som ,.. ]



7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [av]   B= [dem, som, tyckt ,.. ]



8- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [dem, som, tyckt ,.. ]



9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [dem]   B= [som, tyckt, att ,.. ]



10- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [som, tyckt, att ,.. ]



11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [som]   B= [tyckt, att, mathias ,.. ]



12- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [tyckt, att, mathias ,.. ]



13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [tyckt]   B= [att, mathias, ranégie ,.. ]



14- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [att, mathias, ranégie ,.. ]



15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [att]   B= [mathias, ranégie, aldrig ,.. ]



16- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [mathias, ranégie, aldrig ,.. ]



17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [mathias]   B= [ranégie, aldrig, fick ,.. ]



18- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ranégie, aldrig, fick ,.. ]



19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ranégie]   B= [aldrig, fick, chansen ,.. ]



20- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [aldrig, fick, chansen ,.. ]



21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [aldrig]   B= [fick, chansen, på ,.. ]



22- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [fick, chansen, på ,.. ]



23- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [fick]   B= [chansen, på, kamratgården ,.. ]



24- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [fick, chansen]   B= [på, kamratgården, , ,.. ]



25- **MERGE_AS_OTH**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[fick, chansen]]   B= [på, kamratgården, , ,.. ]



26- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [på, kamratgården, , ,.. ]



27- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [på]   B= [kamratgården, ,, samtidigt ,.. ]



28- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [kamratgården, ,, samtidigt ,.. ]



29- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [kamratgården]   B= [,, samtidigt, ska ,.. ]



30- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, samtidigt, ska ,.. ]



31- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [samtidigt, ska, man ,.. ]



32- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [samtidigt, ska, man ,.. ]



33- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [samtidigt]   B= [ska, man, komma ,.. ]



34- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ska, man, komma ,.. ]



35- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ska]   B= [man, komma, ihåg ,.. ]



36- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [man, komma, ihåg ,.. ]



37- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [man]   B= [komma, ihåg, att ,.. ]



38- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [komma, ihåg, att ,.. ]



39- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [komma]   B= [ihåg, att, det ,.. ]



40- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [komma, ihåg]   B= [att, det, var ,.. ]



41- **MERGE_AS_OTH**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[komma, ihåg]]   B= [att, det, var ,.. ]



42- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [att, det, var ,.. ]



43- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [att]   B= [det, var, när ,.. ]



44- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [det, var, när ,.. ]



45- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [det]   B= [var, när, han ,.. ]



46- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [var, när, han ,.. ]



47- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [var]   B= [när, han, blev ,.. ]



48- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [när, han, blev ,.. ]



49- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [när]   B= [han, blev, knäskadad ,.. ]



50- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [han, blev, knäskadad ,.. ]



51- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [han]   B= [blev, knäskadad, som ,.. ]



52- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [blev, knäskadad, som ,.. ]



53- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [blev]   B= [knäskadad, som, marcus ,.. ]



54- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [knäskadad, som, marcus ,.. ]



55- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [knäskadad]   B= [som, marcus, berg ,.. ]



56- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [som, marcus, berg ,.. ]



57- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [som]   B= [marcus, berg, stod ,.. ]



58- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [marcus, berg, stod ,.. ]



59- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [marcus]   B= [berg, stod, för ,.. ]



60- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [berg, stod, för ,.. ]



61- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [berg]   B= [stod, för, det ,.. ]



62- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [stod, för, det ,.. ]



63- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [stod]   B= [för, det, största ,.. ]



64- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [för, det, största ,.. ]



65- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [för]   B= [det, största, genombrottet ,.. ]



66- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [det, största, genombrottet ,.. ]



67- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [det]   B= [största, genombrottet, i ,.. ]



68- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [största, genombrottet, i ,.. ]



69- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [största]   B= [genombrottet, i, allsvenskan ,.. ]



70- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [genombrottet, i, allsvenskan ,.. ]



71- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [genombrottet]   B= [i, allsvenskan, på ,.. ]



72- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [i, allsvenskan, på ,.. ]



73- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [i]   B= [allsvenskan, på, många ,.. ]



74- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [allsvenskan, på, många ,.. ]



75- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [allsvenskan]   B= [på, många, år ,.. ]



76- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [på, många, år ,.. ]



77- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [på]   B= [många, år, . ,.. ]



78- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [många, år, . ,.. ]



79- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [många]   B= [år, . ,.. ]



80- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [år, . ,.. ]



81- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [år]   B= [.]



82- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [.]



83- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [ ]



84- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

#Oracle problem
## Sentence No. 75 - 
domaren , som kandiderar till högsta domstolen , fällde kommentaren sedan parlamentet **ställt** en **fråga** om lämpligheten att införa dödsstraff mot våldtäktsmän . 
### Existing MWEs: 
1- **ställt fråga** (LVC)

black Merge Num : 3 Interleaving Num: 0


0- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [domaren, ,, som ,.. ]



1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [domaren]   B= [,, som, kandiderar ,.. ]



2- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, som, kandiderar ,.. ]



3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [som, kandiderar, till ,.. ]



4- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [som, kandiderar, till ,.. ]



5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [som]   B= [kandiderar, till, högsta ,.. ]



6- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [kandiderar, till, högsta ,.. ]



7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [kandiderar]   B= [till, högsta, domstolen ,.. ]



8- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [till, högsta, domstolen ,.. ]



9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [till]   B= [högsta, domstolen, , ,.. ]



10- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [högsta, domstolen, , ,.. ]



11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [högsta]   B= [domstolen, ,, fällde ,.. ]



12- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [domstolen, ,, fällde ,.. ]



13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [domstolen]   B= [,, fällde, kommentaren ,.. ]



14- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, fällde, kommentaren ,.. ]



15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [fällde, kommentaren, sedan ,.. ]



16- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [fällde, kommentaren, sedan ,.. ]



17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [fällde]   B= [kommentaren, sedan, parlamentet ,.. ]



18- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [kommentaren, sedan, parlamentet ,.. ]



19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [kommentaren]   B= [sedan, parlamentet, ställt ,.. ]



20- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [sedan, parlamentet, ställt ,.. ]



21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [sedan]   B= [parlamentet, ställt, en ,.. ]



22- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [parlamentet, ställt, en ,.. ]



23- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [parlamentet]   B= [ställt, en, fråga ,.. ]



24- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ställt, en, fråga ,.. ]



25- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ställt]   B= [en, fråga, om ,.. ]



26- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ställt, en]   B= [fråga, om, lämpligheten ,.. ]



27- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ställt]   B= [fråga, om, lämpligheten ,.. ]



28- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ställt, fråga]   B= [om, lämpligheten, att ,.. ]



29- **MERGE_AS_OTH**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[ställt, fråga]]   B= [om, lämpligheten, att ,.. ]



30- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [om, lämpligheten, att ,.. ]



31- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [om]   B= [lämpligheten, att, införa ,.. ]



32- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [lämpligheten, att, införa ,.. ]



33- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [lämpligheten]   B= [att, införa, dödsstraff ,.. ]



34- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [att, införa, dödsstraff ,.. ]



35- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [att]   B= [införa, dödsstraff, mot ,.. ]



36- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [införa, dödsstraff, mot ,.. ]



37- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [införa]   B= [dödsstraff, mot, våldtäktsmän ,.. ]



38- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [dödsstraff, mot, våldtäktsmän ,.. ]



39- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [dödsstraff]   B= [mot, våldtäktsmän, . ,.. ]



40- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [mot, våldtäktsmän, . ,.. ]



41- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [mot]   B= [våldtäktsmän, . ,.. ]



42- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [våldtäktsmän, . ,.. ]



43- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [våldtäktsmän]   B= [.]



44- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [.]



45- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [ ]



46- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

#Oracle problem
## Sentence No. 78 - 
varningen om en försämrad julprognos är inte något som nk **märkt** **av** . 
### Existing MWEs: 
1- **märkt av** (VPC)

black Merge Num : 3 Interleaving Num: 0


0- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [varningen, om, en ,.. ]



1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [varningen]   B= [om, en, försämrad ,.. ]



2- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [om, en, försämrad ,.. ]



3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [om]   B= [en, försämrad, julprognos ,.. ]



4- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [en, försämrad, julprognos ,.. ]



5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [en]   B= [försämrad, julprognos, är ,.. ]



6- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [försämrad, julprognos, är ,.. ]



7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [försämrad]   B= [julprognos, är, inte ,.. ]



8- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [julprognos, är, inte ,.. ]



9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [julprognos]   B= [är, inte, något ,.. ]



10- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [är, inte, något ,.. ]



11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [är]   B= [inte, något, som ,.. ]



12- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [inte, något, som ,.. ]



13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [inte]   B= [något, som, nk ,.. ]



14- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [något, som, nk ,.. ]



15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [något]   B= [som, nk, märkt ,.. ]



16- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [som, nk, märkt ,.. ]



17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [som]   B= [nk, märkt, av ,.. ]



18- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [nk, märkt, av ,.. ]



19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [nk]   B= [märkt, av, . ,.. ]



20- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [märkt, av, . ,.. ]



21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [märkt]   B= [av, . ,.. ]



22- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [märkt, av]   B= [.]



23- **MERGE_AS_OTH**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[märkt, av]]   B= [.]



24- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [.]



25- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [ ]



26- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

#Oracle problem
## Sentence No. 81 - 
låt oss **ta** det **på** **allvar** . 
### Existing MWEs: 
1- **ta på allvar** (ID)

black Merge Num : 3 Interleaving Num: 0


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

black Merge Num : 3 Interleaving Num: 0


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

black Merge Num : 3 Interleaving Num: 0


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

black Merge Num : 3 Interleaving Num: 0


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

black Merge Num : 3 Interleaving Num: 0


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

black Merge Num : 3 Interleaving Num: 0


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

black Merge Num : 3 Interleaving Num: 0


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
## Sentence No. 165 - 
och har i så fall kenneth gustafsson och jesper florén **tagit** **över** den rollen i gais ? 
### Existing MWEs: 
1- **tagit över** (VPC)

black Merge Num : 4 Interleaving Num: 0


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

black Merge Num : 4 Interleaving Num: 0


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

black Merge Num : 8 Interleaving Num: 0


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

