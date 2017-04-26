## Sentence No. 67 - 
parkeringsplatserna ska vara trygga , av god kvalitet , ha väderskydd och det ska **finnas** **möjligheter** att **låsa** **in** eller **fast** cykeln . 
### Existing MWEs: 
1- **finnas möjligheter** (LVC)Tokens : 
finnas
möjligheter


2- **låsa in** (VPC)Tokens : 
låsa
in


3- **låsa fast** (VPC), Interleaving Tokens : 
låsa
fast





0- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [parkeringsplatserna, ska, vara ,.. ]



1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [parkeringsplatserna]   B= [ska, vara, trygga ,.. ]



2- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ska, vara, trygga ,.. ]



3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ska]   B= [vara, trygga, , ,.. ]



4- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [vara, trygga, , ,.. ]



5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [vara]   B= [trygga, ,, av ,.. ]



6- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [trygga, ,, av ,.. ]



7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [trygga]   B= [,, av, god ,.. ]



8- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, av, god ,.. ]



9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [av, god, kvalitet ,.. ]



10- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [av, god, kvalitet ,.. ]



11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [av]   B= [god, kvalitet, , ,.. ]



12- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [god, kvalitet, , ,.. ]



13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [god]   B= [kvalitet, ,, ha ,.. ]



14- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [kvalitet, ,, ha ,.. ]



15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [kvalitet]   B= [,, ha, väderskydd ,.. ]



16- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, ha, väderskydd ,.. ]



17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [ha, väderskydd, och ,.. ]



18- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ha, väderskydd, och ,.. ]



19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ha]   B= [väderskydd, och, det ,.. ]



20- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [väderskydd, och, det ,.. ]



21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [väderskydd]   B= [och, det, ska ,.. ]



22- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [och, det, ska ,.. ]



23- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [och]   B= [det, ska, finnas ,.. ]



24- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [det, ska, finnas ,.. ]



25- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [det]   B= [ska, finnas, möjligheter ,.. ]



26- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ska, finnas, möjligheter ,.. ]



27- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ska]   B= [finnas, möjligheter, att ,.. ]



28- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [finnas, möjligheter, att ,.. ]



29- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [finnas]   B= [möjligheter, att, låsa ,.. ]



30- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [finnas, möjligheter]   B= [att, låsa, in ,.. ]



31- **MERGE_AS_LVC**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[finnas, möjligheter]]   B= [att, låsa, in ,.. ]



32- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [att, låsa, in ,.. ]



33- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [att]   B= [låsa, in, eller ,.. ]



34- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [låsa, in, eller ,.. ]



35- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [låsa]   B= [in, eller, fast ,.. ]



36- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [låsa, in]   B= [eller, fast, cykeln ,.. ]



37- **MERGE_AS_VPC**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[låsa, in]]   B= [eller, fast, cykeln ,.. ]



38- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [eller, fast, cykeln ,.. ]



39- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [eller]   B= [fast, cykeln, . ,.. ]



40- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [fast, cykeln, . ,.. ]



41- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [fast]   B= [cykeln, . ,.. ]



42- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [cykeln, . ,.. ]



43- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [cykeln]   B= [.]



44- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [.]



45- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [ ]



46- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

## Sentence No. 12 - 
det går inte att **komma** **igång** med appen utan att först skapa ett konto och **lägga** **till** bilen i datorn . 
### Existing MWEs: 
1- **komma igång** (VPC)Tokens : 
komma
igång


2- **lägga till** (VPC)Tokens : 
lägga
till





0- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [det, går, inte ,.. ]



1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [det]   B= [går, inte, att ,.. ]



2- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [går, inte, att ,.. ]



3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [går]   B= [inte, att, komma ,.. ]



4- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [inte, att, komma ,.. ]



5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [inte]   B= [att, komma, igång ,.. ]



6- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [att, komma, igång ,.. ]



7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [att]   B= [komma, igång, med ,.. ]



8- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [komma, igång, med ,.. ]



9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [komma]   B= [igång, med, appen ,.. ]



10- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [komma, igång]   B= [med, appen, utan ,.. ]



11- **MERGE_AS_VPC**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[komma, igång]]   B= [med, appen, utan ,.. ]



12- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [med, appen, utan ,.. ]



13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [med]   B= [appen, utan, att ,.. ]



14- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [appen, utan, att ,.. ]



15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [appen]   B= [utan, att, först ,.. ]



16- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [utan, att, först ,.. ]



17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [utan]   B= [att, först, skapa ,.. ]



18- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [att, först, skapa ,.. ]



19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [att]   B= [först, skapa, ett ,.. ]



20- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [först, skapa, ett ,.. ]



21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [först]   B= [skapa, ett, konto ,.. ]



22- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [skapa, ett, konto ,.. ]



23- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [skapa]   B= [ett, konto, och ,.. ]



24- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ett, konto, och ,.. ]



25- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ett]   B= [konto, och, lägga ,.. ]



26- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [konto, och, lägga ,.. ]



27- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [konto]   B= [och, lägga, till ,.. ]



28- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [och, lägga, till ,.. ]



29- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [och]   B= [lägga, till, bilen ,.. ]



30- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [lägga, till, bilen ,.. ]



31- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [lägga]   B= [till, bilen, i ,.. ]



32- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [lägga, till]   B= [bilen, i, datorn ,.. ]



33- **MERGE_AS_VPC**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[lägga, till]]   B= [bilen, i, datorn ,.. ]



34- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [bilen, i, datorn ,.. ]



35- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [bilen]   B= [i, datorn, . ,.. ]



36- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [i, datorn, . ,.. ]



37- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [i]   B= [datorn, . ,.. ]



38- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [datorn, . ,.. ]



39- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [datorn]   B= [.]



40- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [.]



41- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [ ]



42- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

## Sentence No. 22 - 
mats grauers och anderz larqvist , ordförande och klubbdirektör , **säger** **sig** inte ha **tagit** ett slutgiltigt **beslut** . 
### Existing MWEs: 
1- **säger sig** (IReflV)Tokens : 
säger
sig


2- **tagit beslut** (LVC)Tokens : 
tagit
beslut





0- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [mats, grauers, och ,.. ]



1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [mats]   B= [grauers, och, anderz ,.. ]



2- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [grauers, och, anderz ,.. ]



3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [grauers]   B= [och, anderz, larqvist ,.. ]



4- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [och, anderz, larqvist ,.. ]



5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [och]   B= [anderz, larqvist, , ,.. ]



6- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [anderz, larqvist, , ,.. ]



7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [anderz]   B= [larqvist, ,, ordförande ,.. ]



8- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [larqvist, ,, ordförande ,.. ]



9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [larqvist]   B= [,, ordförande, och ,.. ]



10- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, ordförande, och ,.. ]



11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [ordförande, och, klubbdirektör ,.. ]



12- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ordförande, och, klubbdirektör ,.. ]



13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ordförande]   B= [och, klubbdirektör, , ,.. ]



14- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [och, klubbdirektör, , ,.. ]



15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [och]   B= [klubbdirektör, ,, säger ,.. ]



16- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [klubbdirektör, ,, säger ,.. ]



17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [klubbdirektör]   B= [,, säger, sig ,.. ]



18- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, säger, sig ,.. ]



19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [säger, sig, inte ,.. ]



20- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [säger, sig, inte ,.. ]



21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [säger]   B= [sig, inte, ha ,.. ]



22- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [säger, sig]   B= [inte, ha, tagit ,.. ]



23- **MERGE_AS_IReflV**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[säger, sig]]   B= [inte, ha, tagit ,.. ]



24- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [inte, ha, tagit ,.. ]



25- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [inte]   B= [ha, tagit, ett ,.. ]



26- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ha, tagit, ett ,.. ]



27- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ha]   B= [tagit, ett, slutgiltigt ,.. ]



28- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [tagit, ett, slutgiltigt ,.. ]



29- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [tagit]   B= [ett, slutgiltigt, beslut ,.. ]



30- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [tagit, ett]   B= [slutgiltigt, beslut, . ,.. ]



31- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [tagit]   B= [slutgiltigt, beslut, . ,.. ]



32- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [tagit, slutgiltigt]   B= [beslut, . ,.. ]



33- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [tagit]   B= [beslut, . ,.. ]



34- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [tagit, beslut]   B= [.]



35- **MERGE_AS_LVC**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[tagit, beslut]]   B= [.]



36- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [.]



37- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [ ]



38- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

## Sentence No. 34 - 
exempelvis **erbjöd** **sig** ryssland , som ofta bromsat västmakternas planer på militära ingripanden , i går att **hjälpa** **till** med att transportera franska soldater till mali . 
### Existing MWEs: 
1- **erbjöd sig** (IReflV)Tokens : 
erbjöd
sig


2- **hjälpa till** (VPC)Tokens : 
hjälpa
till





0- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [exempelvis, erbjöd, sig ,.. ]



1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [exempelvis]   B= [erbjöd, sig, ryssland ,.. ]



2- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [erbjöd, sig, ryssland ,.. ]



3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [erbjöd]   B= [sig, ryssland, , ,.. ]



4- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [erbjöd, sig]   B= [ryssland, ,, som ,.. ]



5- **MERGE_AS_IReflV**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[erbjöd, sig]]   B= [ryssland, ,, som ,.. ]



6- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ryssland, ,, som ,.. ]



7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ryssland]   B= [,, som, ofta ,.. ]



8- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, som, ofta ,.. ]



9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [som, ofta, bromsat ,.. ]



10- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [som, ofta, bromsat ,.. ]



11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [som]   B= [ofta, bromsat, västmakternas ,.. ]



12- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ofta, bromsat, västmakternas ,.. ]



13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ofta]   B= [bromsat, västmakternas, planer ,.. ]



14- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [bromsat, västmakternas, planer ,.. ]



15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [bromsat]   B= [västmakternas, planer, på ,.. ]



16- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [västmakternas, planer, på ,.. ]



17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [västmakternas]   B= [planer, på, militära ,.. ]



18- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [planer, på, militära ,.. ]



19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [planer]   B= [på, militära, ingripanden ,.. ]



20- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [på, militära, ingripanden ,.. ]



21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [på]   B= [militära, ingripanden, , ,.. ]



22- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [militära, ingripanden, , ,.. ]



23- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [militära]   B= [ingripanden, ,, i ,.. ]



24- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ingripanden, ,, i ,.. ]



25- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ingripanden]   B= [,, i, går ,.. ]



26- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, i, går ,.. ]



27- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [i, går, att ,.. ]



28- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [i, går, att ,.. ]



29- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [i]   B= [går, att, hjälpa ,.. ]



30- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [går, att, hjälpa ,.. ]



31- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [går]   B= [att, hjälpa, till ,.. ]



32- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [att, hjälpa, till ,.. ]



33- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [att]   B= [hjälpa, till, med ,.. ]



34- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [hjälpa, till, med ,.. ]



35- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [hjälpa]   B= [till, med, att ,.. ]



36- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [hjälpa, till]   B= [med, att, transportera ,.. ]



37- **MERGE_AS_VPC**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[hjälpa, till]]   B= [med, att, transportera ,.. ]



38- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [med, att, transportera ,.. ]



39- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [med]   B= [att, transportera, franska ,.. ]



40- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [att, transportera, franska ,.. ]



41- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [att]   B= [transportera, franska, soldater ,.. ]



42- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [transportera, franska, soldater ,.. ]



43- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [transportera]   B= [franska, soldater, till ,.. ]



44- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [franska, soldater, till ,.. ]



45- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [franska]   B= [soldater, till, mali ,.. ]



46- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [soldater, till, mali ,.. ]



47- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [soldater]   B= [till, mali, . ,.. ]



48- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [till, mali, . ,.. ]



49- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [till]   B= [mali, . ,.. ]



50- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [mali, . ,.. ]



51- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [mali]   B= [.]



52- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [.]



53- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [ ]



54- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

## Sentence No. 61 - 
det **avspeglar** **sig** också i den säsongsbetonade menyn som vi **borrade** **oss** **ner** i medan vi smååt av den goda brödkorgen med malt- , surdegs- och knäckebröd , och ett rört smör därtill . 
### Existing MWEs: 
1- **avspeglar sig** (IReflV)Tokens : 
avspeglar
sig


2- **borrade oss ner** (ID)Tokens : 
borrade
oss
ner





0- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [det, avspeglar, sig ,.. ]



1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [det]   B= [avspeglar, sig, också ,.. ]



2- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [avspeglar, sig, också ,.. ]



3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [avspeglar]   B= [sig, också, i ,.. ]



4- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [avspeglar, sig]   B= [också, i, den ,.. ]



5- **MERGE_AS_IReflV**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[avspeglar, sig]]   B= [också, i, den ,.. ]



6- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [också, i, den ,.. ]



7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [också]   B= [i, den, säsongsbetonade ,.. ]



8- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [i, den, säsongsbetonade ,.. ]



9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [i]   B= [den, säsongsbetonade, menyn ,.. ]



10- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [den, säsongsbetonade, menyn ,.. ]



11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [den]   B= [säsongsbetonade, menyn, som ,.. ]



12- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [säsongsbetonade, menyn, som ,.. ]



13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [säsongsbetonade]   B= [menyn, som, vi ,.. ]



14- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [menyn, som, vi ,.. ]



15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [menyn]   B= [som, vi, borrade ,.. ]



16- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [som, vi, borrade ,.. ]



17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [som]   B= [vi, borrade, oss ,.. ]



18- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [vi, borrade, oss ,.. ]



19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [vi]   B= [borrade, oss, ner ,.. ]



20- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [borrade, oss, ner ,.. ]



21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [borrade]   B= [oss, ner, i ,.. ]



22- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [borrade, oss]   B= [ner, i, medan ,.. ]



23- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [borrade, oss, ner]   B= [i, medan, vi ,.. ]



24- WHITE_MERGE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [borrade, [oss, ner]]   B= [i, medan, vi ,.. ]



25- **MERGE_AS_ID**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[borrade, [oss, ner]]]   B= [i, medan, vi ,.. ]



26- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [i, medan, vi ,.. ]



27- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [i]   B= [medan, vi, smååt ,.. ]



28- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [medan, vi, smååt ,.. ]



29- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [medan]   B= [vi, smååt, av ,.. ]



30- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [vi, smååt, av ,.. ]



31- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [vi]   B= [smååt, av, den ,.. ]



32- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [smååt, av, den ,.. ]



33- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [smååt]   B= [av, den, goda ,.. ]



34- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [av, den, goda ,.. ]



35- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [av]   B= [den, goda, brödkorgen ,.. ]



36- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [den, goda, brödkorgen ,.. ]



37- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [den]   B= [goda, brödkorgen, med ,.. ]



38- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [goda, brödkorgen, med ,.. ]



39- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [goda]   B= [brödkorgen, med, malt- ,.. ]



40- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [brödkorgen, med, malt- ,.. ]



41- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [brödkorgen]   B= [med, malt-, , ,.. ]



42- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [med, malt-, , ,.. ]



43- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [med]   B= [malt-, ,, surdegs- ,.. ]



44- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [malt-, ,, surdegs- ,.. ]



45- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [malt-]   B= [,, surdegs-, och ,.. ]



46- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, surdegs-, och ,.. ]



47- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [surdegs-, och, knäckebröd ,.. ]



48- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [surdegs-, och, knäckebröd ,.. ]



49- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [surdegs-]   B= [och, knäckebröd, , ,.. ]



50- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [och, knäckebröd, , ,.. ]



51- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [och]   B= [knäckebröd, ,, och ,.. ]



52- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [knäckebröd, ,, och ,.. ]



53- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [knäckebröd]   B= [,, och, ett ,.. ]



54- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, och, ett ,.. ]



55- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [och, ett, rört ,.. ]



56- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [och, ett, rört ,.. ]



57- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [och]   B= [ett, rört, smör ,.. ]



58- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ett, rört, smör ,.. ]



59- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ett]   B= [rört, smör, därtill ,.. ]



60- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [rört, smör, därtill ,.. ]



61- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [rört]   B= [smör, därtill, . ,.. ]



62- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [smör, därtill, . ,.. ]



63- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [smör]   B= [därtill, . ,.. ]



64- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [därtill, . ,.. ]



65- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [därtill]   B= [.]



66- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [.]



67- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [ ]



68- Reduce&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

