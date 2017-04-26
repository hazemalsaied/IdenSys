## Sentence No. 1676 - 
אדיר זיק ציטט מכתב מהרב צבי יהודה קוק האומר כי על ארץ ישראל יש **למסור** **את** **הנפש** ואם תהיה כפיה הן מצד גוים או אפילו חלילה מצד יהודים יש **למסור** **את** **הנפש** 
### Existing MWEs: 
2- **למסור הנפש** (LVC, 1)Tokens : 
למסור
הנפש


3- **למסור את הנפש** (LVC, 1), Interleaving Tokens : 
למסור
את
הנפש


1- **למסור הנפש** (LVC, 1)Tokens : 
למסור
הנפש


4- **למסור את הנפש** (LVC, 1), Interleaving Tokens : 
למסור
את
הנפש


### Identified MWEs: 
1- **למסור את הנפש** (LVC)Tokens : 
למסור
את
הנפש


2- **למסור את הנפש** (LVC)Tokens : 
למסור
את
הנפש





0- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [אדיר, זיק, ציטט ,.. ]



1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [אדיר]   B= [זיק, ציטט, מכתב ,.. ]



2- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [זיק, ציטט, מכתב ,.. ]



3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [זיק]   B= [ציטט, מכתב, מהרב ,.. ]



4- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ציטט, מכתב, מהרב ,.. ]



5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ציטט]   B= [מכתב, מהרב, צבי ,.. ]



6- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [מכתב, מהרב, צבי ,.. ]



7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [מכתב]   B= [מהרב, צבי, יהודה ,.. ]



8- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [מהרב, צבי, יהודה ,.. ]



9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [מהרב]   B= [צבי, יהודה, קוק ,.. ]



10- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [צבי, יהודה, קוק ,.. ]



11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [צבי]   B= [יהודה, קוק, האומר ,.. ]



12- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [יהודה, קוק, האומר ,.. ]



13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [יהודה]   B= [קוק, האומר, כי ,.. ]



14- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [קוק, האומר, כי ,.. ]



15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [קוק]   B= [האומר, כי, על ,.. ]



16- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [האומר, כי, על ,.. ]



17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [האומר]   B= [כי, על, ארץ ,.. ]



18- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [כי, על, ארץ ,.. ]



19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [כי]   B= [על, ארץ, ישראל ,.. ]



20- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [על, ארץ, ישראל ,.. ]



21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [על]   B= [ארץ, ישראל, יש ,.. ]



22- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ארץ, ישראל, יש ,.. ]



23- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ארץ]   B= [ישראל, יש, למסור ,.. ]



24- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ישראל, יש, למסור ,.. ]



25- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ישראל]   B= [יש, למסור, את ,.. ]



26- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [יש, למסור, את ,.. ]



27- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [יש]   B= [למסור, את, הנפש ,.. ]



28- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [למסור, את, הנפש ,.. ]



29- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [למסור]   B= [את, הנפש, ואם ,.. ]



30- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [למסור, את]   B= [הנפש, ואם, תהיה ,.. ]



31- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [למסור, את, הנפש]   B= [ואם, תהיה, כפיה ,.. ]



32- WHITE_MERGE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [למסור, [את, הנפש]]   B= [ואם, תהיה, כפיה ,.. ]



33- **MERGE_AS_LVC**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[למסור, [את, הנפש]]]   B= [ואם, תהיה, כפיה ,.. ]



34- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ואם, תהיה, כפיה ,.. ]



35- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ואם]   B= [תהיה, כפיה, הן ,.. ]



36- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [תהיה, כפיה, הן ,.. ]



37- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [תהיה]   B= [כפיה, הן, מצד ,.. ]



38- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [כפיה, הן, מצד ,.. ]



39- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [כפיה]   B= [הן, מצד, גוים ,.. ]



40- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [הן, מצד, גוים ,.. ]



41- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [הן]   B= [מצד, גוים, או ,.. ]



42- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [מצד, גוים, או ,.. ]



43- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [מצד]   B= [גוים, או, אפילו ,.. ]



44- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [גוים, או, אפילו ,.. ]



45- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [גוים]   B= [או, אפילו, חלילה ,.. ]



46- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [או, אפילו, חלילה ,.. ]



47- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [או]   B= [אפילו, חלילה, מצד ,.. ]



48- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [אפילו, חלילה, מצד ,.. ]



49- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [אפילו]   B= [חלילה, מצד, יהודים ,.. ]



50- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [חלילה, מצד, יהודים ,.. ]



51- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [חלילה]   B= [מצד, יהודים, יש ,.. ]



52- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [מצד, יהודים, יש ,.. ]



53- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [מצד]   B= [יהודים, יש, למסור ,.. ]



54- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [יהודים, יש, למסור ,.. ]



55- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [יהודים]   B= [יש, למסור, את ,.. ]



56- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [יש, למסור, את ,.. ]



57- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [יש]   B= [למסור, את, הנפש ,.. ]



58- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [למסור, את, הנפש ,.. ]



59- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [למסור]   B= [את, הנפש ,.. ]



60- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [למסור, את]   B= [הנפש]



61- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [למסור, את, הנפש]   B= [ ]



62- WHITE_MERGE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [למסור, [את, הנפש]]   B= [ ]



63- **MERGE_AS_LVC**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[למסור, [את, הנפש]]]   B= [ ]



64- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

## Sentence No. 1244 - 
הסיור במקום הוא סיור כדי **להכיר** **ולו** **במעט** **את** **העבר** וכן לראות שעדיין קיימות ברחבי הארץ שמורות טבע **רחוקות** **מהעין** **נסתרות** **מעין** **כל** והליכה בשביל היא 
### Existing MWEs: 
1- **להכיר ולו במעט את העבר** (OTH)Tokens : 
להכיר
ולו
במעט
את
העבר


2- **רחוקות מהעין** (VPC)Tokens : 
רחוקות
מהעין


3- **נסתרות מעין כל** (VPC)Tokens : 
נסתרות
מעין
כל





0- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [הסיור, במקום, הוא ,.. ]



1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [הסיור]   B= [במקום, הוא, סיור ,.. ]



2- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [במקום, הוא, סיור ,.. ]



3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [במקום]   B= [הוא, סיור, כדי ,.. ]



4- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [הוא, סיור, כדי ,.. ]



5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [הוא]   B= [סיור, כדי, להכיר ,.. ]



6- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [סיור, כדי, להכיר ,.. ]



7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [סיור]   B= [כדי, להכיר, ולו ,.. ]



8- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [כדי, להכיר, ולו ,.. ]



9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [כדי]   B= [להכיר, ולו, במעט ,.. ]



10- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [להכיר, ולו, במעט ,.. ]



11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [להכיר]   B= [ולו, במעט, את ,.. ]



12- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ולו, במעט, את ,.. ]



13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ולו]   B= [במעט, את, העבר ,.. ]



14- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [במעט, את, העבר ,.. ]



15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [במעט]   B= [את, העבר, וכן ,.. ]



16- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [את, העבר, וכן ,.. ]



17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [את]   B= [העבר, וכן, לראות ,.. ]



18- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [העבר, וכן, לראות ,.. ]



19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [העבר]   B= [וכן, לראות, שעדיין ,.. ]



20- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [וכן, לראות, שעדיין ,.. ]



21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [וכן]   B= [לראות, שעדיין, קיימות ,.. ]



22- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [לראות, שעדיין, קיימות ,.. ]



23- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [לראות]   B= [שעדיין, קיימות, ברחבי ,.. ]



24- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [שעדיין, קיימות, ברחבי ,.. ]



25- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [שעדיין]   B= [קיימות, ברחבי, הארץ ,.. ]



26- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [קיימות, ברחבי, הארץ ,.. ]



27- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [קיימות]   B= [ברחבי, הארץ, שמורות ,.. ]



28- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ברחבי, הארץ, שמורות ,.. ]



29- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ברחבי]   B= [הארץ, שמורות, טבע ,.. ]



30- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [הארץ, שמורות, טבע ,.. ]



31- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [הארץ]   B= [שמורות, טבע, רחוקות ,.. ]



32- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [שמורות, טבע, רחוקות ,.. ]



33- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [שמורות]   B= [טבע, רחוקות, מהעין ,.. ]



34- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [טבע, רחוקות, מהעין ,.. ]



35- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [טבע]   B= [רחוקות, מהעין, נסתרות ,.. ]



36- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [רחוקות, מהעין, נסתרות ,.. ]



37- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [רחוקות]   B= [מהעין, נסתרות, מעין ,.. ]



38- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [מהעין, נסתרות, מעין ,.. ]



39- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [מהעין]   B= [נסתרות, מעין, כל ,.. ]



40- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [נסתרות, מעין, כל ,.. ]



41- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [נסתרות]   B= [מעין, כל, והליכה ,.. ]



42- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [מעין, כל, והליכה ,.. ]



43- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [מעין]   B= [כל, והליכה, בשביל ,.. ]



44- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [כל, והליכה, בשביל ,.. ]



45- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [כל]   B= [והליכה, בשביל, היא ,.. ]



46- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [והליכה, בשביל, היא ,.. ]



47- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [והליכה]   B= [בשביל, היא ,.. ]



48- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [בשביל, היא ,.. ]



49- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [בשביל]   B= [היא]



50- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [היא]



51- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [היא]   B= [ ]



52- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

## Sentence No. 1298 - 
מטילי החרמות **ועושי** **דברם** **לוקחים** **את** **החוק** **לידיהם** **וחורצים** **דינם** של חפים מפשע מחוץ לכותלי בית המשפט 
### Existing MWEs: 
1- **ועושי דברם** (OTH)Tokens : 
ועושי
דברם


2- **לוקחים את החוק לידיהם** (OTH)Tokens : 
לוקחים
את
החוק
לידיהם


3- **וחורצים דינם** (LVC)Tokens : 
וחורצים
דינם


### Identified MWEs: 
1- **לוקחים את החוק** (VPC)Tokens : 
לוקחים
את
החוק





0- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [מטילי, החרמות, ועושי ,.. ]



1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [מטילי]   B= [החרמות, ועושי, דברם ,.. ]



2- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [החרמות, ועושי, דברם ,.. ]



3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [החרמות]   B= [ועושי, דברם, לוקחים ,.. ]



4- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ועושי, דברם, לוקחים ,.. ]



5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ועושי]   B= [דברם, לוקחים, את ,.. ]



6- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [דברם, לוקחים, את ,.. ]



7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [דברם]   B= [לוקחים, את, החוק ,.. ]



8- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [לוקחים, את, החוק ,.. ]



9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [לוקחים]   B= [את, החוק, לידיהם ,.. ]



10- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [לוקחים, את]   B= [החוק, לידיהם, וחורצים ,.. ]



11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [לוקחים, את, החוק]   B= [לידיהם, וחורצים, דינם ,.. ]



12- WHITE_MERGE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [לוקחים, [את, החוק]]   B= [לידיהם, וחורצים, דינם ,.. ]



13- **MERGE_AS_VPC**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[לוקחים, [את, החוק]]]   B= [לידיהם, וחורצים, דינם ,.. ]



14- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [לידיהם, וחורצים, דינם ,.. ]



15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [לידיהם]   B= [וחורצים, דינם, של ,.. ]



16- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [וחורצים, דינם, של ,.. ]



17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [וחורצים]   B= [דינם, של, חפים ,.. ]



18- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [דינם, של, חפים ,.. ]



19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [דינם]   B= [של, חפים, מפשע ,.. ]



20- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [של, חפים, מפשע ,.. ]



21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [של]   B= [חפים, מפשע, מחוץ ,.. ]



22- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [חפים, מפשע, מחוץ ,.. ]



23- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [חפים]   B= [מפשע, מחוץ, לכותלי ,.. ]



24- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [מפשע, מחוץ, לכותלי ,.. ]



25- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [מפשע]   B= [מחוץ, לכותלי, בית ,.. ]



26- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [מחוץ, לכותלי, בית ,.. ]



27- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [מחוץ]   B= [לכותלי, בית, המשפט ,.. ]



28- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [לכותלי, בית, המשפט ,.. ]



29- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [לכותלי]   B= [בית, המשפט ,.. ]



30- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [בית, המשפט ,.. ]



31- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [בית]   B= [המשפט]



32- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [המשפט]



33- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [המשפט]   B= [ ]



34- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

## Sentence No. 1370 - 
מול כוחות רשע אטומים מול אנשים חסרי ערכים ציוניים מול דיקטטור מטורף **הגורר** **את** **המדינה** למלחמת אזרחים אנו **נציב** **מחדש** את **סולם** **הערכים** הציוני התיישבותי שהקים **את** מדינת ישראל ביתו הלאומי של העם היהודי אומרים מארגני האירוע 
### Existing MWEs: 
2- **הגורר את המדינה** (VPC, 1)Tokens : 
הגורר
את
המדינה


1- **נציב מחדש סולם הערכים** (OTH, 1)Tokens : 
נציב
מחדש
סולם
הערכים


3- **נציב מחדש סולם הערכים את** (OTH, 1), Interleaving Tokens : 
נציב
מחדש
סולם
הערכים
את


### Identified MWEs: 
1- **הגורר את המדינה** (VPC)Tokens : 
הגורר
את
המדינה


2- **נציב מחדש את סולם הערכים** (OTH)Tokens : 
נציב
מחדש
את
סולם
הערכים





0- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [מול, כוחות, רשע ,.. ]



1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [מול]   B= [כוחות, רשע, אטומים ,.. ]



2- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [כוחות, רשע, אטומים ,.. ]



3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [כוחות]   B= [רשע, אטומים, מול ,.. ]



4- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [רשע, אטומים, מול ,.. ]



5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [רשע]   B= [אטומים, מול, אנשים ,.. ]



6- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [אטומים, מול, אנשים ,.. ]



7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [אטומים]   B= [מול, אנשים, חסרי ,.. ]



8- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [מול, אנשים, חסרי ,.. ]



9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [מול]   B= [אנשים, חסרי, ערכים ,.. ]



10- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [אנשים, חסרי, ערכים ,.. ]



11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [אנשים]   B= [חסרי, ערכים, ציוניים ,.. ]



12- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [חסרי, ערכים, ציוניים ,.. ]



13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [חסרי]   B= [ערכים, ציוניים, מול ,.. ]



14- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ערכים, ציוניים, מול ,.. ]



15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ערכים]   B= [ציוניים, מול, דיקטטור ,.. ]



16- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ציוניים, מול, דיקטטור ,.. ]



17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ציוניים]   B= [מול, דיקטטור, מטורף ,.. ]



18- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [מול, דיקטטור, מטורף ,.. ]



19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [מול]   B= [דיקטטור, מטורף, הגורר ,.. ]



20- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [דיקטטור, מטורף, הגורר ,.. ]



21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [דיקטטור]   B= [מטורף, הגורר, את ,.. ]



22- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [מטורף, הגורר, את ,.. ]



23- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [מטורף]   B= [הגורר, את, המדינה ,.. ]



24- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [הגורר, את, המדינה ,.. ]



25- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [הגורר]   B= [את, המדינה, למלחמת ,.. ]



26- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [הגורר, את]   B= [המדינה, למלחמת, אזרחים ,.. ]



27- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [הגורר, את, המדינה]   B= [למלחמת, אזרחים, אנו ,.. ]



28- WHITE_MERGE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [הגורר, [את, המדינה]]   B= [למלחמת, אזרחים, אנו ,.. ]



29- **MERGE_AS_VPC**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[הגורר, [את, המדינה]]]   B= [למלחמת, אזרחים, אנו ,.. ]



30- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [למלחמת, אזרחים, אנו ,.. ]



31- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [למלחמת]   B= [אזרחים, אנו, נציב ,.. ]



32- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [אזרחים, אנו, נציב ,.. ]



33- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [אזרחים]   B= [אנו, נציב, מחדש ,.. ]



34- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [אנו, נציב, מחדש ,.. ]



35- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [אנו]   B= [נציב, מחדש, את ,.. ]



36- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [נציב, מחדש, את ,.. ]



37- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [נציב]   B= [מחדש, את, סולם ,.. ]



38- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [נציב, מחדש]   B= [את, סולם, הערכים ,.. ]



39- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [נציב, מחדש, את]   B= [סולם, הערכים, הציוני ,.. ]



40- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [נציב, מחדש, את, סולם]   B= [הערכים, הציוני, התיישבותי ,.. ]



41- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [נציב, מחדש, את, סולם, הערכים]   B= [הציוני, התיישבותי, שהקים ,.. ]



42- WHITE_MERGE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [נציב, מחדש, את, [סולם, הערכים]]   B= [הציוני, התיישבותי, שהקים ,.. ]



43- WHITE_MERGE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [נציב, מחדש, [את, [סולם, הערכים]]]   B= [הציוני, התיישבותי, שהקים ,.. ]



44- WHITE_MERGE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [נציב, [מחדש, [את, [סולם, הערכים]]]]   B= [הציוני, התיישבותי, שהקים ,.. ]



45- **MERGE_AS_OTH**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[נציב, [מחדש, [את, [סולם, הערכים]]]]]   B= [הציוני, התיישבותי, שהקים ,.. ]



46- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [הציוני, התיישבותי, שהקים ,.. ]



47- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [הציוני]   B= [התיישבותי, שהקים, את ,.. ]



48- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [התיישבותי, שהקים, את ,.. ]



49- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [התיישבותי]   B= [שהקים, את, מדינת ,.. ]



50- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [שהקים, את, מדינת ,.. ]



51- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [שהקים]   B= [את, מדינת, ישראל ,.. ]



52- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [את, מדינת, ישראל ,.. ]



53- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [את]   B= [מדינת, ישראל, ביתו ,.. ]



54- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [מדינת, ישראל, ביתו ,.. ]



55- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [מדינת]   B= [ישראל, ביתו, הלאומי ,.. ]



56- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ישראל, ביתו, הלאומי ,.. ]



57- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ישראל]   B= [ביתו, הלאומי, של ,.. ]



58- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ביתו, הלאומי, של ,.. ]



59- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ביתו]   B= [הלאומי, של, העם ,.. ]



60- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [הלאומי, של, העם ,.. ]



61- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [הלאומי]   B= [של, העם, היהודי ,.. ]



62- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [של, העם, היהודי ,.. ]



63- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [של]   B= [העם, היהודי, אומרים ,.. ]



64- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [העם, היהודי, אומרים ,.. ]



65- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [העם]   B= [היהודי, אומרים, מארגני ,.. ]



66- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [היהודי, אומרים, מארגני ,.. ]



67- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [היהודי]   B= [אומרים, מארגני, האירוע ,.. ]



68- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [אומרים, מארגני, האירוע ,.. ]



69- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [אומרים]   B= [מארגני, האירוע ,.. ]



70- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [מארגני, האירוע ,.. ]



71- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [מארגני]   B= [האירוע]



72- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [האירוע]



73- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [האירוע]   B= [ ]



74- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

## Sentence No. 1391 - 
לדברי אריאל ממילא כולם **שמעו** **את** **המוסיקה** **שהם** **רוצים** ובכך רק **ניתנה** שוב **במה** לאותם אמנים **שמהווים** **דוגמא** **שלילית** 
### Existing MWEs: 
1- **שמעו את המוסיקה שהם רוצים** (ID)Tokens : 
שמעו
את
המוסיקה
שהם
רוצים


2- **ניתנה במה** (OTH)Tokens : 
ניתנה
במה


3- **שמהווים דוגמא שלילית** (OTH)Tokens : 
שמהווים
דוגמא
שלילית





0- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [לדברי, אריאל, ממילא ,.. ]



1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [לדברי]   B= [אריאל, ממילא, כולם ,.. ]



2- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [אריאל, ממילא, כולם ,.. ]



3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [אריאל]   B= [ממילא, כולם, שמעו ,.. ]



4- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ממילא, כולם, שמעו ,.. ]



5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ממילא]   B= [כולם, שמעו, את ,.. ]



6- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [כולם, שמעו, את ,.. ]



7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [כולם]   B= [שמעו, את, המוסיקה ,.. ]



8- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [שמעו, את, המוסיקה ,.. ]



9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [שמעו]   B= [את, המוסיקה, שהם ,.. ]



10- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [את, המוסיקה, שהם ,.. ]



11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [את]   B= [המוסיקה, שהם, רוצים ,.. ]



12- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [המוסיקה, שהם, רוצים ,.. ]



13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [המוסיקה]   B= [שהם, רוצים, ובכך ,.. ]



14- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [שהם, רוצים, ובכך ,.. ]



15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [שהם]   B= [רוצים, ובכך, רק ,.. ]



16- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [רוצים, ובכך, רק ,.. ]



17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [רוצים]   B= [ובכך, רק, ניתנה ,.. ]



18- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ובכך, רק, ניתנה ,.. ]



19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ובכך]   B= [רק, ניתנה, שוב ,.. ]



20- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [רק, ניתנה, שוב ,.. ]



21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [רק]   B= [ניתנה, שוב, במה ,.. ]



22- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ניתנה, שוב, במה ,.. ]



23- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ניתנה]   B= [שוב, במה, לאותם ,.. ]



24- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [שוב, במה, לאותם ,.. ]



25- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [שוב]   B= [במה, לאותם, אמנים ,.. ]



26- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [במה, לאותם, אמנים ,.. ]



27- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [במה]   B= [לאותם, אמנים, שמהווים ,.. ]



28- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [לאותם, אמנים, שמהווים ,.. ]



29- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [לאותם]   B= [אמנים, שמהווים, דוגמא ,.. ]



30- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [אמנים, שמהווים, דוגמא ,.. ]



31- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [אמנים]   B= [שמהווים, דוגמא, שלילית ,.. ]



32- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [שמהווים, דוגמא, שלילית ,.. ]



33- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [שמהווים]   B= [דוגמא, שלילית ,.. ]



34- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [דוגמא, שלילית ,.. ]



35- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [דוגמא]   B= [שלילית]



36- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [שלילית]



37- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [שלילית]   B= [ ]



38- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

