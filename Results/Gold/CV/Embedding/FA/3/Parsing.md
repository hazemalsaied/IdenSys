## Sentence No. 1408 - 
**حس** **مي‌کرد** دقيقاً مي‌داند نشستن رويِ چنين صندليِ راحتي نزديکِ آتش چه احساسي دارد ، درحالي‌که پاها را به حفاظِ آتش **تکيه** **داده** اي و کتري بررويِ آتش **غلغل** **مي‌کند** و تيک‌تاکِ ساعت در اتاق مي‌پيچد و کسي **مراقبِ** تو **نيست** و صدايي **به** **گوش** **نمي‌رسد** . 
### Existing MWEs: 
1- **حس مي‌کرد** (OTH, 5)Tokens : 
حس
مي‌کرد


2- **تکيه داده** (OTH, 5)Tokens : 
تکيه
داده


3- **غلغل مي‌کند** (OTH)Tokens : 
غلغل
مي‌کند


4- **مراقبِ نيست** (OTH, 2)Tokens : 
مراقبِ
نيست


5- **به گوش نمي‌رسد** (OTH)Tokens : 
به
گوش
نمي‌رسد


### Identified MWEs: 
1- **حس مي‌کرد** (OTH)Tokens : 
حس
مي‌کرد


2- **احساسي دارد** (OTH)Tokens : 
احساسي
دارد


3- **غلغل مي‌کند** (OTH)Tokens : 
غلغل
مي‌کند


4- **در اتاق مي‌پيچد** (OTH)Tokens : 
در
اتاق
مي‌پيچد


5- **مراقبِ نيست** (OTH)Tokens : 
مراقبِ
نيست





0- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [حس, مي‌کرد, دقيقاً ,.. ]



1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [حس]   B= [مي‌کرد, دقيقاً, مي‌داند ,.. ]



2- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [حس, مي‌کرد]   B= [دقيقاً, مي‌داند, نشستن ,.. ]



3- **MERGE_AS_OTH**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[حس, مي‌کرد]]   B= [دقيقاً, مي‌داند, نشستن ,.. ]



4- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [دقيقاً, مي‌داند, نشستن ,.. ]



5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [دقيقاً]   B= [مي‌داند, نشستن, رويِ ,.. ]



6- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [مي‌داند, نشستن, رويِ ,.. ]



7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [مي‌داند]   B= [نشستن, رويِ, چنين ,.. ]



8- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [نشستن, رويِ, چنين ,.. ]



9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [نشستن]   B= [رويِ, چنين, صندليِ ,.. ]



10- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [رويِ, چنين, صندليِ ,.. ]



11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [رويِ]   B= [چنين, صندليِ, راحتي ,.. ]



12- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [چنين, صندليِ, راحتي ,.. ]



13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [چنين]   B= [صندليِ, راحتي, نزديکِ ,.. ]



14- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [صندليِ, راحتي, نزديکِ ,.. ]



15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [صندليِ]   B= [راحتي, نزديکِ, آتش ,.. ]



16- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [راحتي, نزديکِ, آتش ,.. ]



17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [راحتي]   B= [نزديکِ, آتش, چه ,.. ]



18- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [نزديکِ, آتش, چه ,.. ]



19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [نزديکِ]   B= [آتش, چه, احساسي ,.. ]



20- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [آتش, چه, احساسي ,.. ]



21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [آتش]   B= [چه, احساسي, دارد ,.. ]



22- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [چه, احساسي, دارد ,.. ]



23- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [چه]   B= [احساسي, دارد, ، ,.. ]



24- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [احساسي, دارد, ، ,.. ]



25- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [احساسي]   B= [دارد, ،, درحالي‌که ,.. ]



26- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [احساسي, دارد]   B= [،, درحالي‌که, پاها ,.. ]



27- **MERGE_AS_OTH**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[احساسي, دارد]]   B= [،, درحالي‌که, پاها ,.. ]



28- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [،, درحالي‌که, پاها ,.. ]



29- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [،]   B= [درحالي‌که, پاها, را ,.. ]



30- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [درحالي‌که, پاها, را ,.. ]



31- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [درحالي‌که]   B= [پاها, را, به ,.. ]



32- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [پاها, را, به ,.. ]



33- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [پاها]   B= [را, به, حفاظِ ,.. ]



34- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [را, به, حفاظِ ,.. ]



35- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [را]   B= [به, حفاظِ, آتش ,.. ]



36- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [به, حفاظِ, آتش ,.. ]



37- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [به]   B= [حفاظِ, آتش, تکيه ,.. ]



38- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [حفاظِ, آتش, تکيه ,.. ]



39- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [حفاظِ]   B= [آتش, تکيه, داده ,.. ]



40- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [آتش, تکيه, داده ,.. ]



41- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [آتش]   B= [تکيه, داده, اي ,.. ]



42- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [تکيه, داده, اي ,.. ]



43- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [تکيه]   B= [داده, اي, و ,.. ]



44- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [تکيه, داده]   B= [اي, و, کتري ,.. ]



45- WHITE_MERGE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[تکيه, داده]]   B= [اي, و, کتري ,.. ]



46- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [اي, و, کتري ,.. ]



47- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [اي]   B= [و, کتري, بررويِ ,.. ]



48- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [و, کتري, بررويِ ,.. ]



49- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [و]   B= [کتري, بررويِ, آتش ,.. ]



50- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [کتري, بررويِ, آتش ,.. ]



51- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [کتري]   B= [بررويِ, آتش, غلغل ,.. ]



52- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [بررويِ, آتش, غلغل ,.. ]



53- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [بررويِ]   B= [آتش, غلغل, مي‌کند ,.. ]



54- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [آتش, غلغل, مي‌کند ,.. ]



55- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [آتش]   B= [غلغل, مي‌کند, و ,.. ]



56- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [غلغل, مي‌کند, و ,.. ]



57- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [غلغل]   B= [مي‌کند, و, تيک‌تاکِ ,.. ]



58- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [غلغل, مي‌کند]   B= [و, تيک‌تاکِ, ساعت ,.. ]



59- **MERGE_AS_OTH**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[غلغل, مي‌کند]]   B= [و, تيک‌تاکِ, ساعت ,.. ]



60- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [و, تيک‌تاکِ, ساعت ,.. ]



61- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [و]   B= [تيک‌تاکِ, ساعت, در ,.. ]



62- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [تيک‌تاکِ, ساعت, در ,.. ]



63- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [تيک‌تاکِ]   B= [ساعت, در, اتاق ,.. ]



64- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ساعت, در, اتاق ,.. ]



65- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ساعت]   B= [در, اتاق, مي‌پيچد ,.. ]



66- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [در, اتاق, مي‌پيچد ,.. ]



67- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [در]   B= [اتاق, مي‌پيچد, و ,.. ]



68- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [در, اتاق]   B= [مي‌پيچد, و, کسي ,.. ]



69- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [در, اتاق, مي‌پيچد]   B= [و, کسي, مراقبِ ,.. ]



70- WHITE_MERGE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [در, [اتاق, مي‌پيچد]]   B= [و, کسي, مراقبِ ,.. ]



71- **MERGE_AS_OTH**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[در, [اتاق, مي‌پيچد]]]   B= [و, کسي, مراقبِ ,.. ]



72- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [و, کسي, مراقبِ ,.. ]



73- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [و]   B= [کسي, مراقبِ, تو ,.. ]



74- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [کسي, مراقبِ, تو ,.. ]



75- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [کسي]   B= [مراقبِ, تو, نيست ,.. ]



76- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [مراقبِ, تو, نيست ,.. ]



77- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [مراقبِ]   B= [تو, نيست, و ,.. ]



78- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [مراقبِ, تو]   B= [نيست, و, صدايي ,.. ]



79- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [مراقبِ]   B= [نيست, و, صدايي ,.. ]



80- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [مراقبِ, نيست]   B= [و, صدايي, به ,.. ]



81- **MERGE_AS_OTH**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[مراقبِ, نيست]]   B= [و, صدايي, به ,.. ]



82- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [و, صدايي, به ,.. ]



83- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [و]   B= [صدايي, به, گوش ,.. ]



84- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [صدايي, به, گوش ,.. ]



85- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [صدايي]   B= [به, گوش, نمي‌رسد ,.. ]



86- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [به, گوش, نمي‌رسد ,.. ]



87- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [به]   B= [گوش, نمي‌رسد, . ,.. ]



88- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [گوش, نمي‌رسد, . ,.. ]



89- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [گوش]   B= [نمي‌رسد, . ,.. ]



90- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [نمي‌رسد, . ,.. ]



91- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [نمي‌رسد]   B= [.]



92- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [.]



93- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [ ]



94- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

## Sentence No. 1542 - 
در ميدانِ جنگ ، در سلولِ شکنجه ، يا کشتيِ در حالِ غرق‌شدن ، مسئله‌اي که فرد به‌خاطرِ آن **در** **حالِ** جنگ **بود** معمولاً **فراموش** **مي‌شد** ، زيرا بدن آن‌قدر **باد** **مي‌کرد** که همهٔ فضا را **پر** **مي‌کرد** و يا وقتي کسي از ترس در حالِ فلج‌شدن است و يا از درد **جيغ** **مي‌کشد** ، زندگي مبارزه‌اي لحظه‌به‌لحظه برعليهِ گرسنگي ، سرما ، بي‌خوابي ، زخمِ معده و يا دندان‌درد است . 
### Existing MWEs: 
1- **در حالِ بود** (OTH, 16)Tokens : 
در
حالِ
بود


2- **فراموش مي‌شد** (OTH)Tokens : 
فراموش
مي‌شد


3- **باد مي‌کرد** (OTH, 1)Tokens : 
باد
مي‌کرد


4- **پر مي‌کرد** (OTH, 6)Tokens : 
پر
مي‌کرد


5- **جيغ مي‌کشد** (OTH, 1)Tokens : 
جيغ
مي‌کشد


### Identified MWEs: 
1- **در حالِ بود** (OTH)Tokens : 
در
حالِ
بود


2- **فراموش مي‌شد** (OTH)Tokens : 
فراموش
مي‌شد


3- **باد مي‌کرد** (OTH)Tokens : 
باد
مي‌کرد


4- **پر مي‌کرد** (OTH)Tokens : 
پر
مي‌کرد


5- **در حالِ است** (OTH)Tokens : 
در
حالِ
است


6- **جيغ مي‌کشد** (OTH)Tokens : 
جيغ
مي‌کشد





0- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [در, ميدانِ, جنگ ,.. ]



1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [در]   B= [ميدانِ, جنگ, ، ,.. ]



2- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ميدانِ, جنگ, ، ,.. ]



3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ميدانِ]   B= [جنگ, ،, در ,.. ]



4- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [جنگ, ،, در ,.. ]



5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [جنگ]   B= [،, در, سلولِ ,.. ]



6- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [،, در, سلولِ ,.. ]



7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [،]   B= [در, سلولِ, شکنجه ,.. ]



8- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [در, سلولِ, شکنجه ,.. ]



9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [در]   B= [سلولِ, شکنجه, ، ,.. ]



10- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [سلولِ, شکنجه, ، ,.. ]



11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [سلولِ]   B= [شکنجه, ،, يا ,.. ]



12- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [شکنجه, ،, يا ,.. ]



13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [شکنجه]   B= [،, يا, کشتيِ ,.. ]



14- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [،, يا, کشتيِ ,.. ]



15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [،]   B= [يا, کشتيِ, در ,.. ]



16- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [يا, کشتيِ, در ,.. ]



17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [يا]   B= [کشتيِ, در, حالِ ,.. ]



18- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [کشتيِ, در, حالِ ,.. ]



19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [کشتيِ]   B= [در, حالِ, غرق‌شدن ,.. ]



20- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [در, حالِ, غرق‌شدن ,.. ]



21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [در]   B= [حالِ, غرق‌شدن, ، ,.. ]



22- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [حالِ, غرق‌شدن, ، ,.. ]



23- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [حالِ]   B= [غرق‌شدن, ،, مسئله‌اي ,.. ]



24- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [غرق‌شدن, ،, مسئله‌اي ,.. ]



25- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [غرق‌شدن]   B= [،, مسئله‌اي, که ,.. ]



26- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [،, مسئله‌اي, که ,.. ]



27- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [،]   B= [مسئله‌اي, که, فرد ,.. ]



28- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [مسئله‌اي, که, فرد ,.. ]



29- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [مسئله‌اي]   B= [که, فرد, به‌خاطرِ ,.. ]



30- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [که, فرد, به‌خاطرِ ,.. ]



31- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [که]   B= [فرد, به‌خاطرِ, آن ,.. ]



32- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [فرد, به‌خاطرِ, آن ,.. ]



33- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [فرد]   B= [به‌خاطرِ, آن, در ,.. ]



34- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [به‌خاطرِ, آن, در ,.. ]



35- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [به‌خاطرِ]   B= [آن, در, حالِ ,.. ]



36- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [آن, در, حالِ ,.. ]



37- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [آن]   B= [در, حالِ, جنگ ,.. ]



38- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [در, حالِ, جنگ ,.. ]



39- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [در]   B= [حالِ, جنگ, بود ,.. ]



40- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [در, حالِ]   B= [جنگ, بود, معمولاً ,.. ]



41- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [در, حالِ, جنگ]   B= [بود, معمولاً, فراموش ,.. ]



42- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [در, حالِ]   B= [بود, معمولاً, فراموش ,.. ]



43- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [در, حالِ, بود]   B= [معمولاً, فراموش, مي‌شد ,.. ]



44- WHITE_MERGE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [در, [حالِ, بود]]   B= [معمولاً, فراموش, مي‌شد ,.. ]



45- **MERGE_AS_OTH**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[در, [حالِ, بود]]]   B= [معمولاً, فراموش, مي‌شد ,.. ]



46- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [معمولاً, فراموش, مي‌شد ,.. ]



47- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [معمولاً]   B= [فراموش, مي‌شد, ، ,.. ]



48- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [فراموش, مي‌شد, ، ,.. ]



49- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [فراموش]   B= [مي‌شد, ،, زيرا ,.. ]



50- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [فراموش, مي‌شد]   B= [،, زيرا, بدن ,.. ]



51- **MERGE_AS_OTH**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[فراموش, مي‌شد]]   B= [،, زيرا, بدن ,.. ]



52- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [،, زيرا, بدن ,.. ]



53- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [،]   B= [زيرا, بدن, آن‌قدر ,.. ]



54- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [زيرا, بدن, آن‌قدر ,.. ]



55- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [زيرا]   B= [بدن, آن‌قدر, باد ,.. ]



56- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [بدن, آن‌قدر, باد ,.. ]



57- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [بدن]   B= [آن‌قدر, باد, مي‌کرد ,.. ]



58- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [آن‌قدر, باد, مي‌کرد ,.. ]



59- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [آن‌قدر]   B= [باد, مي‌کرد, که ,.. ]



60- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [باد, مي‌کرد, که ,.. ]



61- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [باد]   B= [مي‌کرد, که, همهٔ ,.. ]



62- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [باد, مي‌کرد]   B= [که, همهٔ, فضا ,.. ]



63- **MERGE_AS_OTH**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[باد, مي‌کرد]]   B= [که, همهٔ, فضا ,.. ]



64- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [که, همهٔ, فضا ,.. ]



65- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [که]   B= [همهٔ, فضا, را ,.. ]



66- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [همهٔ, فضا, را ,.. ]



67- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [همهٔ]   B= [فضا, را, پر ,.. ]



68- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [فضا, را, پر ,.. ]



69- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [فضا]   B= [را, پر, مي‌کرد ,.. ]



70- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [را, پر, مي‌کرد ,.. ]



71- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [را]   B= [پر, مي‌کرد, و ,.. ]



72- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [پر, مي‌کرد, و ,.. ]



73- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [پر]   B= [مي‌کرد, و, يا ,.. ]



74- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [پر, مي‌کرد]   B= [و, يا, وقتي ,.. ]



75- **MERGE_AS_OTH**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[پر, مي‌کرد]]   B= [و, يا, وقتي ,.. ]



76- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [و, يا, وقتي ,.. ]



77- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [و]   B= [يا, وقتي, کسي ,.. ]



78- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [يا, وقتي, کسي ,.. ]



79- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [يا]   B= [وقتي, کسي, از ,.. ]



80- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [وقتي, کسي, از ,.. ]



81- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [وقتي]   B= [کسي, از, ترس ,.. ]



82- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [کسي, از, ترس ,.. ]



83- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [کسي]   B= [از, ترس, در ,.. ]



84- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [از, ترس, در ,.. ]



85- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [از]   B= [ترس, در, حالِ ,.. ]



86- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ترس, در, حالِ ,.. ]



87- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ترس]   B= [در, حالِ, فلج‌شدن ,.. ]



88- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [در, حالِ, فلج‌شدن ,.. ]



89- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [در]   B= [حالِ, فلج‌شدن, است ,.. ]



90- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [در, حالِ]   B= [فلج‌شدن, است, و ,.. ]



91- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [در, حالِ, فلج‌شدن]   B= [است, و, يا ,.. ]



92- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [در, حالِ]   B= [است, و, يا ,.. ]



93- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [در, حالِ, است]   B= [و, يا, از ,.. ]



94- WHITE_MERGE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [در, [حالِ, است]]   B= [و, يا, از ,.. ]



95- **MERGE_AS_OTH**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[در, [حالِ, است]]]   B= [و, يا, از ,.. ]



96- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [و, يا, از ,.. ]



97- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [و]   B= [يا, از, درد ,.. ]



98- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [يا, از, درد ,.. ]



99- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [يا]   B= [از, درد, جيغ ,.. ]



100- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [از, درد, جيغ ,.. ]



101- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [از]   B= [درد, جيغ, مي‌کشد ,.. ]



102- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [درد, جيغ, مي‌کشد ,.. ]



103- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [درد]   B= [جيغ, مي‌کشد, ، ,.. ]



104- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [جيغ, مي‌کشد, ، ,.. ]



105- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [جيغ]   B= [مي‌کشد, ،, زندگي ,.. ]



106- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [جيغ, مي‌کشد]   B= [،, زندگي, مبارزه‌اي ,.. ]



107- **MERGE_AS_OTH**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[جيغ, مي‌کشد]]   B= [،, زندگي, مبارزه‌اي ,.. ]



108- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [،, زندگي, مبارزه‌اي ,.. ]



109- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [،]   B= [زندگي, مبارزه‌اي, لحظه‌به‌لحظه ,.. ]



110- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [زندگي, مبارزه‌اي, لحظه‌به‌لحظه ,.. ]



111- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [زندگي]   B= [مبارزه‌اي, لحظه‌به‌لحظه, برعليهِ ,.. ]



112- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [مبارزه‌اي, لحظه‌به‌لحظه, برعليهِ ,.. ]



113- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [مبارزه‌اي]   B= [لحظه‌به‌لحظه, برعليهِ, گرسنگي ,.. ]



114- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [لحظه‌به‌لحظه, برعليهِ, گرسنگي ,.. ]



115- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [لحظه‌به‌لحظه]   B= [برعليهِ, گرسنگي, ، ,.. ]



116- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [برعليهِ, گرسنگي, ، ,.. ]



117- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [برعليهِ]   B= [گرسنگي, ،, سرما ,.. ]



118- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [گرسنگي, ،, سرما ,.. ]



119- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [گرسنگي]   B= [،, سرما, ، ,.. ]



120- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [،, سرما, ، ,.. ]



121- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [،]   B= [سرما, ،, بي‌خوابي ,.. ]



122- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [سرما, ،, بي‌خوابي ,.. ]



123- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [سرما]   B= [،, بي‌خوابي, ، ,.. ]



124- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [،, بي‌خوابي, ، ,.. ]



125- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [،]   B= [بي‌خوابي, ،, زخمِ ,.. ]



126- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [بي‌خوابي, ،, زخمِ ,.. ]



127- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [بي‌خوابي]   B= [،, زخمِ, معده ,.. ]



128- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [،, زخمِ, معده ,.. ]



129- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [،]   B= [زخمِ, معده, و ,.. ]



130- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [زخمِ, معده, و ,.. ]



131- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [زخمِ]   B= [معده, و, يا ,.. ]



132- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [معده, و, يا ,.. ]



133- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [معده]   B= [و, يا, دندان‌درد ,.. ]



134- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [و, يا, دندان‌درد ,.. ]



135- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [و]   B= [يا, دندان‌درد, است ,.. ]



136- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [يا, دندان‌درد, است ,.. ]



137- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [يا]   B= [دندان‌درد, است, . ,.. ]



138- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [دندان‌درد, است, . ,.. ]



139- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [دندان‌درد]   B= [است, . ,.. ]



140- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [است, . ,.. ]



141- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [است]   B= [.]



142- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [.]



143- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [ ]



144- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

## Sentence No. 1137 - 
وقتي آن را **به** **زبان** **مي‌آوردي** منطقي **به** **نظر** **مي‌رسيد** ؛ وقتي به آدم‌هايي که در پياده‌رو از کنار َت مي‌گذشتند **نگاه** **مي‌کردي** به اين حرف **ايمان** **مي‌آوردي** . 
### Existing MWEs: 
1- **به زبان مي‌آوردي** (OTH)Tokens : 
به
زبان
مي‌آوردي


2- **به نظر مي‌رسيد** (OTH, 18)Tokens : 
به
نظر
مي‌رسيد


3- **نگاه مي‌کردي** (OTH, 25)Tokens : 
نگاه
مي‌کردي


4- **ايمان مي‌آوردي** (OTH)Tokens : 
ايمان
مي‌آوردي


### Identified MWEs: 
1- **به نظر مي‌رسيد** (OTH)Tokens : 
به
نظر
مي‌رسيد


2- **نگاه مي‌کردي** (OTH)Tokens : 
نگاه
مي‌کردي





0- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [وقتي, آن, را ,.. ]



1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [وقتي]   B= [آن, را, به ,.. ]



2- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [آن, را, به ,.. ]



3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [آن]   B= [را, به, زبان ,.. ]



4- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [را, به, زبان ,.. ]



5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [را]   B= [به, زبان, مي‌آوردي ,.. ]



6- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [به, زبان, مي‌آوردي ,.. ]



7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [به]   B= [زبان, مي‌آوردي, منطقي ,.. ]



8- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [زبان, مي‌آوردي, منطقي ,.. ]



9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [زبان]   B= [مي‌آوردي, منطقي, به ,.. ]



10- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [مي‌آوردي, منطقي, به ,.. ]



11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [مي‌آوردي]   B= [منطقي, به, نظر ,.. ]



12- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [منطقي, به, نظر ,.. ]



13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [منطقي]   B= [به, نظر, مي‌رسيد ,.. ]



14- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [به, نظر, مي‌رسيد ,.. ]



15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [به]   B= [نظر, مي‌رسيد, ؛ ,.. ]



16- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [به, نظر]   B= [مي‌رسيد, ؛, وقتي ,.. ]



17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [به, نظر, مي‌رسيد]   B= [؛, وقتي, به ,.. ]



18- WHITE_MERGE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [به, [نظر, مي‌رسيد]]   B= [؛, وقتي, به ,.. ]



19- **MERGE_AS_OTH**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[به, [نظر, مي‌رسيد]]]   B= [؛, وقتي, به ,.. ]



20- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [؛, وقتي, به ,.. ]



21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [؛]   B= [وقتي, به, آدم‌هايي ,.. ]



22- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [وقتي, به, آدم‌هايي ,.. ]



23- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [وقتي]   B= [به, آدم‌هايي, که ,.. ]



24- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [به, آدم‌هايي, که ,.. ]



25- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [به]   B= [آدم‌هايي, که, در ,.. ]



26- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [آدم‌هايي, که, در ,.. ]



27- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [آدم‌هايي]   B= [که, در, پياده‌رو ,.. ]



28- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [که, در, پياده‌رو ,.. ]



29- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [که]   B= [در, پياده‌رو, از ,.. ]



30- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [در, پياده‌رو, از ,.. ]



31- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [در]   B= [پياده‌رو, از, کنار ,.. ]



32- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [پياده‌رو, از, کنار ,.. ]



33- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [پياده‌رو]   B= [از, کنار, َت ,.. ]



34- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [از, کنار, َت ,.. ]



35- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [از]   B= [کنار, َت, مي‌گذشتند ,.. ]



36- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [کنار, َت, مي‌گذشتند ,.. ]



37- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [کنار]   B= [َت, مي‌گذشتند, نگاه ,.. ]



38- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [َت, مي‌گذشتند, نگاه ,.. ]



39- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [َت]   B= [مي‌گذشتند, نگاه, مي‌کردي ,.. ]



40- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [مي‌گذشتند, نگاه, مي‌کردي ,.. ]



41- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [مي‌گذشتند]   B= [نگاه, مي‌کردي, به ,.. ]



42- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [نگاه, مي‌کردي, به ,.. ]



43- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [نگاه]   B= [مي‌کردي, به, اين ,.. ]



44- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [نگاه, مي‌کردي]   B= [به, اين, حرف ,.. ]



45- **MERGE_AS_OTH**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[نگاه, مي‌کردي]]   B= [به, اين, حرف ,.. ]



46- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [به, اين, حرف ,.. ]



47- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [به]   B= [اين, حرف, ايمان ,.. ]



48- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [اين, حرف, ايمان ,.. ]



49- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [اين]   B= [حرف, ايمان, مي‌آوردي ,.. ]



50- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [حرف, ايمان, مي‌آوردي ,.. ]



51- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [حرف]   B= [ايمان, مي‌آوردي, . ,.. ]



52- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ايمان, مي‌آوردي, . ,.. ]



53- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ايمان]   B= [مي‌آوردي, . ,.. ]



54- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [مي‌آوردي, . ,.. ]



55- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [مي‌آوردي]   B= [.]



56- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [.]



57- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [ ]



58- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

## Sentence No. 1325 - 
و هنگامي‌که حافظه ضعيف بود و شواهدِ نوشتاري نيز **تحريف** **شده** بود – همه **مجبور** به قبولِ اين ادعايِ حزب **بودند** که شرايطِ زندگيِ افراد بعداز انقلاب بهتر شده است ، زيرا هيچ معياري برايِ آزمودنِ درستيِ آن **وجود** **نداشت** و بعدها هم نمي‌توانست **به** **وجود** **بيايد** . 
### Existing MWEs: 
1- **تحريف شده** (OTH)Tokens : 
تحريف
شده


2- **مجبور بودند** (OTH, 5)Tokens : 
مجبور
بودند


3- **وجود نداشت** (OTH, 51)Tokens : 
وجود
نداشت


4- **به وجود بيايد** (OTH)Tokens : 
به
وجود
بيايد


### Identified MWEs: 
1- **تحريف شده** (OTH)Tokens : 
تحريف
شده


2- **مجبور بودند** (OTH)Tokens : 
مجبور
بودند


3- **وجود نداشت** (OTH)Tokens : 
وجود
نداشت


4- **به وجود بيايد** (OTH)Tokens : 
به
وجود
بيايد





0- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [و, هنگامي‌که, حافظه ,.. ]



1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [و]   B= [هنگامي‌که, حافظه, ضعيف ,.. ]



2- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [هنگامي‌که, حافظه, ضعيف ,.. ]



3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [هنگامي‌که]   B= [حافظه, ضعيف, بود ,.. ]



4- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [حافظه, ضعيف, بود ,.. ]



5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [حافظه]   B= [ضعيف, بود, و ,.. ]



6- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ضعيف, بود, و ,.. ]



7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ضعيف]   B= [بود, و, شواهدِ ,.. ]



8- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [بود, و, شواهدِ ,.. ]



9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [بود]   B= [و, شواهدِ, نوشتاري ,.. ]



10- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [و, شواهدِ, نوشتاري ,.. ]



11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [و]   B= [شواهدِ, نوشتاري, نيز ,.. ]



12- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [شواهدِ, نوشتاري, نيز ,.. ]



13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [شواهدِ]   B= [نوشتاري, نيز, تحريف ,.. ]



14- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [نوشتاري, نيز, تحريف ,.. ]



15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [نوشتاري]   B= [نيز, تحريف, شده ,.. ]



16- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [نيز, تحريف, شده ,.. ]



17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [نيز]   B= [تحريف, شده, بود ,.. ]



18- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [تحريف, شده, بود ,.. ]



19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [تحريف]   B= [شده, بود, – ,.. ]



20- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [تحريف, شده]   B= [بود, –, همه ,.. ]



21- **MERGE_AS_OTH**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[تحريف, شده]]   B= [بود, –, همه ,.. ]



22- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [بود, –, همه ,.. ]



23- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [بود]   B= [–, همه, مجبور ,.. ]



24- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [–, همه, مجبور ,.. ]



25- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [–]   B= [همه, مجبور, به ,.. ]



26- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [همه, مجبور, به ,.. ]



27- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [همه]   B= [مجبور, به, قبولِ ,.. ]



28- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [مجبور, به, قبولِ ,.. ]



29- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [مجبور]   B= [به, قبولِ, اين ,.. ]



30- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [مجبور, به]   B= [قبولِ, اين, ادعايِ ,.. ]



31- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [مجبور]   B= [قبولِ, اين, ادعايِ ,.. ]



32- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [مجبور, قبولِ]   B= [اين, ادعايِ, حزب ,.. ]



33- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [مجبور]   B= [اين, ادعايِ, حزب ,.. ]



34- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [مجبور, اين]   B= [ادعايِ, حزب, بودند ,.. ]



35- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [مجبور]   B= [ادعايِ, حزب, بودند ,.. ]



36- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [مجبور, ادعايِ]   B= [حزب, بودند, که ,.. ]



37- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [مجبور]   B= [حزب, بودند, که ,.. ]



38- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [مجبور, حزب]   B= [بودند, که, شرايطِ ,.. ]



39- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [مجبور]   B= [بودند, که, شرايطِ ,.. ]



40- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [مجبور, بودند]   B= [که, شرايطِ, زندگيِ ,.. ]



41- **MERGE_AS_OTH**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[مجبور, بودند]]   B= [که, شرايطِ, زندگيِ ,.. ]



42- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [که, شرايطِ, زندگيِ ,.. ]



43- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [که]   B= [شرايطِ, زندگيِ, افراد ,.. ]



44- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [شرايطِ, زندگيِ, افراد ,.. ]



45- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [شرايطِ]   B= [زندگيِ, افراد, بعداز ,.. ]



46- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [زندگيِ, افراد, بعداز ,.. ]



47- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [زندگيِ]   B= [افراد, بعداز, انقلاب ,.. ]



48- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [افراد, بعداز, انقلاب ,.. ]



49- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [افراد]   B= [بعداز, انقلاب, بهتر ,.. ]



50- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [بعداز, انقلاب, بهتر ,.. ]



51- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [بعداز]   B= [انقلاب, بهتر, شده ,.. ]



52- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [انقلاب, بهتر, شده ,.. ]



53- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [انقلاب]   B= [بهتر, شده, است ,.. ]



54- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [بهتر, شده, است ,.. ]



55- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [بهتر]   B= [شده, است, ، ,.. ]



56- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [شده, است, ، ,.. ]



57- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [شده]   B= [است, ،, زيرا ,.. ]



58- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [است, ،, زيرا ,.. ]



59- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [است]   B= [،, زيرا, هيچ ,.. ]



60- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [،, زيرا, هيچ ,.. ]



61- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [،]   B= [زيرا, هيچ, معياري ,.. ]



62- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [زيرا, هيچ, معياري ,.. ]



63- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [زيرا]   B= [هيچ, معياري, برايِ ,.. ]



64- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [هيچ, معياري, برايِ ,.. ]



65- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [هيچ]   B= [معياري, برايِ, آزمودنِ ,.. ]



66- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [معياري, برايِ, آزمودنِ ,.. ]



67- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [معياري]   B= [برايِ, آزمودنِ, درستيِ ,.. ]



68- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [برايِ, آزمودنِ, درستيِ ,.. ]



69- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [برايِ]   B= [آزمودنِ, درستيِ, آن ,.. ]



70- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [آزمودنِ, درستيِ, آن ,.. ]



71- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [آزمودنِ]   B= [درستيِ, آن, وجود ,.. ]



72- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [درستيِ, آن, وجود ,.. ]



73- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [درستيِ]   B= [آن, وجود, نداشت ,.. ]



74- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [آن, وجود, نداشت ,.. ]



75- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [آن]   B= [وجود, نداشت, و ,.. ]



76- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [وجود, نداشت, و ,.. ]



77- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [وجود]   B= [نداشت, و, بعدها ,.. ]



78- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [وجود, نداشت]   B= [و, بعدها, هم ,.. ]



79- **MERGE_AS_OTH**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[وجود, نداشت]]   B= [و, بعدها, هم ,.. ]



80- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [و, بعدها, هم ,.. ]



81- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [و]   B= [بعدها, هم, نمي‌توانست ,.. ]



82- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [بعدها, هم, نمي‌توانست ,.. ]



83- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [بعدها]   B= [هم, نمي‌توانست, به ,.. ]



84- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [هم, نمي‌توانست, به ,.. ]



85- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [هم]   B= [نمي‌توانست, به, وجود ,.. ]



86- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [نمي‌توانست, به, وجود ,.. ]



87- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [نمي‌توانست]   B= [به, وجود, بيايد ,.. ]



88- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [به, وجود, بيايد ,.. ]



89- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [به]   B= [وجود, بيايد, . ,.. ]



90- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [به, وجود]   B= [بيايد, . ,.. ]



91- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [به, وجود, بيايد]   B= [.]



92- WHITE_MERGE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [به, [وجود, بيايد]]   B= [.]



93- **MERGE_AS_OTH**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[به, [وجود, بيايد]]]   B= [.]



94- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [.]



95- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [ ]



96- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

## Sentence No. 1439 - 
**ياد** م **نيست** بقيه اش چه‌طور بود ، ولي آخر اش اين‌جوري **تموم** **مي‌شد** : اين هم شمعي که راه ِت و به‌سويِ تخت **روشن** **مي‌کنه** ، اين هم ساطوري که سر ِت و **قطع** **مي‌کنه** . 
### Existing MWEs: 
1- **ياد نيست** (OTH, 2)Tokens : 
ياد
نيست


2- **تموم مي‌شد** (OTH, 2)Tokens : 
تموم
مي‌شد


3- **روشن مي‌کنه** (OTH, 1)Tokens : 
روشن
مي‌کنه


4- **قطع مي‌کنه** (OTH, 1)Tokens : 
قطع
مي‌کنه


### Identified MWEs: 
1- **ياد نيست** (OTH)Tokens : 
ياد
نيست


2- **تموم مي‌شد** (OTH)Tokens : 
تموم
مي‌شد


3- **روشن مي‌کنه** (OTH)Tokens : 
روشن
مي‌کنه


4- **قطع مي‌کنه** (OTH)Tokens : 
قطع
مي‌کنه





0- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ياد, م, نيست ,.. ]



1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ياد]   B= [م, نيست, بقيه ,.. ]



2- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ياد, م]   B= [نيست, بقيه, اش ,.. ]



3- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ياد]   B= [نيست, بقيه, اش ,.. ]



4- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ياد, نيست]   B= [بقيه, اش, چه‌طور ,.. ]



5- **MERGE_AS_OTH**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[ياد, نيست]]   B= [بقيه, اش, چه‌طور ,.. ]



6- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [بقيه, اش, چه‌طور ,.. ]



7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [بقيه]   B= [اش, چه‌طور, بود ,.. ]



8- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [اش, چه‌طور, بود ,.. ]



9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [اش]   B= [چه‌طور, بود, ، ,.. ]



10- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [چه‌طور, بود, ، ,.. ]



11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [چه‌طور]   B= [بود, ،, ولي ,.. ]



12- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [بود, ،, ولي ,.. ]



13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [بود]   B= [،, ولي, آخر ,.. ]



14- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [،, ولي, آخر ,.. ]



15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [،]   B= [ولي, آخر, اش ,.. ]



16- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ولي, آخر, اش ,.. ]



17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ولي]   B= [آخر, اش, اين‌جوري ,.. ]



18- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [آخر, اش, اين‌جوري ,.. ]



19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [آخر]   B= [اش, اين‌جوري, تموم ,.. ]



20- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [اش, اين‌جوري, تموم ,.. ]



21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [اش]   B= [اين‌جوري, تموم, مي‌شد ,.. ]



22- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [اين‌جوري, تموم, مي‌شد ,.. ]



23- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [اين‌جوري]   B= [تموم, مي‌شد, : ,.. ]



24- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [تموم, مي‌شد, : ,.. ]



25- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [تموم]   B= [مي‌شد, :, اين ,.. ]



26- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [تموم, مي‌شد]   B= [:, اين, هم ,.. ]



27- **MERGE_AS_OTH**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[تموم, مي‌شد]]   B= [:, اين, هم ,.. ]



28- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [:, اين, هم ,.. ]



29- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [:]   B= [اين, هم, شمعي ,.. ]



30- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [اين, هم, شمعي ,.. ]



31- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [اين]   B= [هم, شمعي, که ,.. ]



32- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [هم, شمعي, که ,.. ]



33- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [هم]   B= [شمعي, که, راه ,.. ]



34- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [شمعي, که, راه ,.. ]



35- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [شمعي]   B= [که, راه, ِت ,.. ]



36- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [که, راه, ِت ,.. ]



37- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [که]   B= [راه, ِت, و ,.. ]



38- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [راه, ِت, و ,.. ]



39- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [راه]   B= [ِت, و, به‌سويِ ,.. ]



40- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ِت, و, به‌سويِ ,.. ]



41- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ِت]   B= [و, به‌سويِ, تخت ,.. ]



42- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [و, به‌سويِ, تخت ,.. ]



43- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [و]   B= [به‌سويِ, تخت, روشن ,.. ]



44- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [به‌سويِ, تخت, روشن ,.. ]



45- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [به‌سويِ]   B= [تخت, روشن, مي‌کنه ,.. ]



46- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [تخت, روشن, مي‌کنه ,.. ]



47- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [تخت]   B= [روشن, مي‌کنه, ، ,.. ]



48- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [روشن, مي‌کنه, ، ,.. ]



49- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [روشن]   B= [مي‌کنه, ،, اين ,.. ]



50- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [روشن, مي‌کنه]   B= [،, اين, هم ,.. ]



51- **MERGE_AS_OTH**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[روشن, مي‌کنه]]   B= [،, اين, هم ,.. ]



52- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [،, اين, هم ,.. ]



53- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [،]   B= [اين, هم, ساطوري ,.. ]



54- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [اين, هم, ساطوري ,.. ]



55- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [اين]   B= [هم, ساطوري, که ,.. ]



56- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [هم, ساطوري, که ,.. ]



57- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [هم]   B= [ساطوري, که, سر ,.. ]



58- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ساطوري, که, سر ,.. ]



59- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ساطوري]   B= [که, سر, ِت ,.. ]



60- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [که, سر, ِت ,.. ]



61- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [که]   B= [سر, ِت, و ,.. ]



62- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [سر, ِت, و ,.. ]



63- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [سر]   B= [ِت, و, قطع ,.. ]



64- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ِت, و, قطع ,.. ]



65- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ِت]   B= [و, قطع, مي‌کنه ,.. ]



66- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [و, قطع, مي‌کنه ,.. ]



67- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [و]   B= [قطع, مي‌کنه, . ,.. ]



68- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [قطع, مي‌کنه, . ,.. ]



69- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [قطع]   B= [مي‌کنه, . ,.. ]



70- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [قطع, مي‌کنه]   B= [.]



71- **MERGE_AS_OTH**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[قطع, مي‌کنه]]   B= [.]



72- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [.]



73- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [ ]



74- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

