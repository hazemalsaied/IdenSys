#Oracle problem
## Sentence No. 897 - 
vesela bodi , da **imaš** **glavo** **na** **ramenih** in da jo znaš **uporabljati** . « 
### Existing MWEs: 
1- **imaš na ramenih** (ID)

2- **glavo uporabljati** (ID)

black Merge Num : 1 Interleaving Num: 0


0- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [vesela, bodi, , ,.. ]



1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [vesela]   B= [bodi, ,, da ,.. ]



2- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [bodi, ,, da ,.. ]



3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [bodi]   B= [,, da, imaš ,.. ]



4- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, da, imaš ,.. ]



5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [da, imaš, glavo ,.. ]



6- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [da, imaš, glavo ,.. ]



7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [da]   B= [imaš, glavo, na ,.. ]



8- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [imaš, glavo, na ,.. ]



9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [imaš]   B= [glavo, na, ramenih ,.. ]



10- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [imaš, glavo]   B= [na, ramenih, in ,.. ]



11- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [imaš]   B= [na, ramenih, in ,.. ]



12- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [imaš, na]   B= [ramenih, in, da ,.. ]



13- **WHITE_MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[imaš, na]]   B= [ramenih, in, da ,.. ]



14- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[imaš, na]  ramenih]   B= [in, da, jo ,.. ]



15- **MERGE_AS_OTH**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[[imaš, na]  ramenih]]   B= [in, da, jo ,.. ]



16- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [in, da, jo ,.. ]



17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [in]   B= [da, jo, znaš ,.. ]



18- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [da, jo, znaš ,.. ]



19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [da]   B= [jo, znaš, uporabljati ,.. ]



20- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [jo, znaš, uporabljati ,.. ]



21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [jo]   B= [znaš, uporabljati, . ,.. ]



22- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [znaš, uporabljati, . ,.. ]



23- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [znaš]   B= [uporabljati, ., « ,.. ]



24- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [uporabljati, ., « ,.. ]



25- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [uporabljati]   B= [., « ,.. ]



26- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [., « ,.. ]



27- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [«]



28- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [«]



29- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [«]   B= [ ]



30- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

