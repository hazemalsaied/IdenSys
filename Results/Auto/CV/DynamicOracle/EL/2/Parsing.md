## Sentence No. 1644 - 
Εκείνο το οποίο μου **έδωσε** την **ώθηση** είναι το γεγονός ότι είμαι σίγουρη ότι **έλαβα** την **απόφαση** **έχοντας** πλήρη **επίγνωση** και **συνείδηση** της απόφασής μου ” , πρόσθεσε η Γερμανίδα καγκελάριος . 
### Existing MWEs: 
1- **έδωσε ώθηση** (LVC, 2)

2- **έλαβα απόφαση** (LVC, 7)

3- **έχοντας επίγνωση** (LVC)

4- **έχοντας συνείδηση** (LVC), Interleaving 

### Identified MWEs: 
1- **έδωσε ώθηση** (OTH)

black Merge Num : 3 Interleaving Num: 1


0- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Εκείνο, το, οποίο ,.. ]



1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Εκείνο]   B= [το, οποίο, μου ,.. ]



2- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [το, οποίο, μου ,.. ]



3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [το]   B= [οποίο, μου, έδωσε ,.. ]



4- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [οποίο, μου, έδωσε ,.. ]



5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [οποίο]   B= [μου, έδωσε, την ,.. ]



6- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [μου, έδωσε, την ,.. ]



7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [μου]   B= [έδωσε, την, ώθηση ,.. ]



8- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [έδωσε, την, ώθηση ,.. ]



9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [έδωσε]   B= [την, ώθηση, είναι ,.. ]



10- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [έδωσε, την]   B= [ώθηση, είναι, το ,.. ]



11- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [έδωσε]   B= [ώθηση, είναι, το ,.. ]



12- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [έδωσε, ώθηση]   B= [είναι, το, γεγονός ,.. ]



13- **MERGE_AS_OTH**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[έδωσε, ώθηση]]   B= [είναι, το, γεγονός ,.. ]



14- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [είναι, το, γεγονός ,.. ]



15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [είναι]   B= [το, γεγονός, ότι ,.. ]



16- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [το, γεγονός, ότι ,.. ]



17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [το]   B= [γεγονός, ότι, είμαι ,.. ]



18- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [γεγονός, ότι, είμαι ,.. ]



19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [γεγονός]   B= [ότι, είμαι, σίγουρη ,.. ]



20- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ότι, είμαι, σίγουρη ,.. ]



21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ότι]   B= [είμαι, σίγουρη, ότι ,.. ]



22- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [είμαι, σίγουρη, ότι ,.. ]



23- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [είμαι]   B= [σίγουρη, ότι, έλαβα ,.. ]



24- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [σίγουρη, ότι, έλαβα ,.. ]



25- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [σίγουρη]   B= [ότι, έλαβα, την ,.. ]



26- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ότι, έλαβα, την ,.. ]



27- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ότι]   B= [έλαβα, την, απόφαση ,.. ]



28- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [έλαβα, την, απόφαση ,.. ]



29- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [έλαβα]   B= [την, απόφαση, έχοντας ,.. ]



30- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [την, απόφαση, έχοντας ,.. ]



31- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [την]   B= [απόφαση, έχοντας, πλήρη ,.. ]



32- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [απόφαση, έχοντας, πλήρη ,.. ]



33- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [απόφαση]   B= [έχοντας, πλήρη, επίγνωση ,.. ]



34- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [έχοντας, πλήρη, επίγνωση ,.. ]



35- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [έχοντας]   B= [πλήρη, επίγνωση, και ,.. ]



36- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [πλήρη, επίγνωση, και ,.. ]



37- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [πλήρη]   B= [επίγνωση, και, συνείδηση ,.. ]



38- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [επίγνωση, και, συνείδηση ,.. ]



39- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [επίγνωση]   B= [και, συνείδηση, της ,.. ]



40- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [και, συνείδηση, της ,.. ]



41- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [και]   B= [συνείδηση, της, απόφασής ,.. ]



42- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [συνείδηση, της, απόφασής ,.. ]



43- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [συνείδηση]   B= [της, απόφασής, μου ,.. ]



44- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [της, απόφασής, μου ,.. ]



45- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [της]   B= [απόφασής, μου, ” ,.. ]



46- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [απόφασής, μου, ” ,.. ]



47- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [απόφασής]   B= [μου, ”, , ,.. ]



48- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [μου, ”, , ,.. ]



49- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [μου]   B= [”, ,, πρόσθεσε ,.. ]



50- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [”, ,, πρόσθεσε ,.. ]



51- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [”]   B= [,, πρόσθεσε, η ,.. ]



52- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, πρόσθεσε, η ,.. ]



53- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [πρόσθεσε, η, Γερμανίδα ,.. ]



54- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [πρόσθεσε, η, Γερμανίδα ,.. ]



55- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [πρόσθεσε]   B= [η, Γερμανίδα, καγκελάριος ,.. ]



56- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [η, Γερμανίδα, καγκελάριος ,.. ]



57- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [η]   B= [Γερμανίδα, καγκελάριος, . ,.. ]



58- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Γερμανίδα, καγκελάριος, . ,.. ]



59- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Γερμανίδα]   B= [καγκελάριος, . ,.. ]



60- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [καγκελάριος, . ,.. ]



61- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [καγκελάριος]   B= [.]



62- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [.]



63- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [ ]



64- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

## Sentence No. 1060 - 
Ο νεαρός άνδρας σύντομα εκφράζει συμπάθεια προς την Πιλάρ , ερωτεύεται τη Μαρία και **έρχεται** **σε** **σύγκρουση** με τον Πάμπλο , ο οποίος **φέρνει** **αντιρρήσεις** πάνω στην ανατίναξη της γέφυρας . 
### Existing MWEs: 
1- **έρχεται σε σύγκρουση** (LVC, 1)

2- **φέρνει αντιρρήσεις** (LVC)

### Identified MWEs: 
1- **έρχεται σε σύγκρουση** (OTH)

black Merge Num : 2 Interleaving Num: 0


0- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Ο, νεαρός, άνδρας ,.. ]



1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Ο]   B= [νεαρός, άνδρας, σύντομα ,.. ]



2- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [νεαρός, άνδρας, σύντομα ,.. ]



3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [νεαρός]   B= [άνδρας, σύντομα, εκφράζει ,.. ]



4- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [άνδρας, σύντομα, εκφράζει ,.. ]



5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [άνδρας]   B= [σύντομα, εκφράζει, συμπάθεια ,.. ]



6- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [σύντομα, εκφράζει, συμπάθεια ,.. ]



7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [σύντομα]   B= [εκφράζει, συμπάθεια, προς ,.. ]



8- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [εκφράζει, συμπάθεια, προς ,.. ]



9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [εκφράζει]   B= [συμπάθεια, προς, την ,.. ]



10- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [συμπάθεια, προς, την ,.. ]



11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [συμπάθεια]   B= [προς, την, Πιλάρ ,.. ]



12- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [προς, την, Πιλάρ ,.. ]



13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [προς]   B= [την, Πιλάρ, , ,.. ]



14- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [την, Πιλάρ, , ,.. ]



15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [την]   B= [Πιλάρ, ,, ερωτεύεται ,.. ]



16- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Πιλάρ, ,, ερωτεύεται ,.. ]



17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Πιλάρ]   B= [,, ερωτεύεται, τη ,.. ]



18- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, ερωτεύεται, τη ,.. ]



19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [ερωτεύεται, τη, Μαρία ,.. ]



20- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ερωτεύεται, τη, Μαρία ,.. ]



21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ερωτεύεται]   B= [τη, Μαρία, και ,.. ]



22- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [τη, Μαρία, και ,.. ]



23- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [τη]   B= [Μαρία, και, έρχεται ,.. ]



24- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Μαρία, και, έρχεται ,.. ]



25- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Μαρία]   B= [και, έρχεται, σε ,.. ]



26- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [και, έρχεται, σε ,.. ]



27- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [και]   B= [έρχεται, σε, σύγκρουση ,.. ]



28- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [έρχεται, σε, σύγκρουση ,.. ]



29- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [έρχεται]   B= [σε, σύγκρουση, με ,.. ]



30- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [έρχεται, σε]   B= [σύγκρουση, με, τον ,.. ]



31- **WHITE_MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[έρχεται, σε]]   B= [σύγκρουση, με, τον ,.. ]



32- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[έρχεται, σε]  σύγκρουση]   B= [με, τον, Πάμπλο ,.. ]



33- **MERGE_AS_OTH**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[[έρχεται, σε]  σύγκρουση]]   B= [με, τον, Πάμπλο ,.. ]



34- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [με, τον, Πάμπλο ,.. ]



35- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [με]   B= [τον, Πάμπλο, , ,.. ]



36- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [τον, Πάμπλο, , ,.. ]



37- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [τον]   B= [Πάμπλο, ,, ο ,.. ]



38- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Πάμπλο, ,, ο ,.. ]



39- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Πάμπλο]   B= [,, ο, οποίος ,.. ]



40- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, ο, οποίος ,.. ]



41- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [ο, οποίος, φέρνει ,.. ]



42- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ο, οποίος, φέρνει ,.. ]



43- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ο]   B= [οποίος, φέρνει, αντιρρήσεις ,.. ]



44- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [οποίος, φέρνει, αντιρρήσεις ,.. ]



45- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [οποίος]   B= [φέρνει, αντιρρήσεις, πάνω ,.. ]



46- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [φέρνει, αντιρρήσεις, πάνω ,.. ]



47- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [φέρνει]   B= [αντιρρήσεις, πάνω, στην ,.. ]



48- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [αντιρρήσεις, πάνω, στην ,.. ]



49- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [αντιρρήσεις]   B= [πάνω, στην, ανατίναξη ,.. ]



50- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [πάνω, στην, ανατίναξη ,.. ]



51- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [πάνω]   B= [στην, ανατίναξη, της ,.. ]



52- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [στην, ανατίναξη, της ,.. ]



53- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [στην]   B= [ανατίναξη, της, γέφυρας ,.. ]



54- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ανατίναξη, της, γέφυρας ,.. ]



55- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ανατίναξη]   B= [της, γέφυρας, . ,.. ]



56- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [της, γέφυρας, . ,.. ]



57- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [της]   B= [γέφυρας, . ,.. ]



58- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [γέφυρας, . ,.. ]



59- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [γέφυρας]   B= [.]



60- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [.]



61- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [ ]



62- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

## Sentence No. 1130 - 
**Έχοντας** **σκοπό** να βρει τα χρήματα ώστε να βοηθήσει τον φίλο του Τζεφ ( Μπιλ Μάρεϊ ) να ανεβάσει το θεατρικό του έργο , μεταμφιέζεται σε γυναίκα με το όνομα Ντόροθι Μάικλς και **πιάνει** **δουλειά** σε μια σαπουνόπερα , χωρίς κανείς να ξέρει ότι είναι άνδρας . 
### Existing MWEs: 
1- **Έχοντας σκοπό** (LVC, 3)

2- **πιάνει δουλειά** (ID, 1)

### Identified MWEs: 
1- **Έχοντας σκοπό** (OTH)

2- **πιάνει δουλειά** (OTH)

black Merge Num : 2 Interleaving Num: 0


0- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Έχοντας, σκοπό, να ,.. ]



1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Έχοντας]   B= [σκοπό, να, βρει ,.. ]



2- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Έχοντας, σκοπό]   B= [να, βρει, τα ,.. ]



3- **MERGE_AS_OTH**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[Έχοντας, σκοπό]]   B= [να, βρει, τα ,.. ]



4- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [να, βρει, τα ,.. ]



5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [να]   B= [βρει, τα, χρήματα ,.. ]



6- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [βρει, τα, χρήματα ,.. ]



7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [βρει]   B= [τα, χρήματα, ώστε ,.. ]



8- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [τα, χρήματα, ώστε ,.. ]



9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [τα]   B= [χρήματα, ώστε, να ,.. ]



10- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [χρήματα, ώστε, να ,.. ]



11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [χρήματα]   B= [ώστε, να, βοηθήσει ,.. ]



12- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ώστε, να, βοηθήσει ,.. ]



13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ώστε]   B= [να, βοηθήσει, τον ,.. ]



14- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [να, βοηθήσει, τον ,.. ]



15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [να]   B= [βοηθήσει, τον, φίλο ,.. ]



16- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [βοηθήσει, τον, φίλο ,.. ]



17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [βοηθήσει]   B= [τον, φίλο, του ,.. ]



18- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [τον, φίλο, του ,.. ]



19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [τον]   B= [φίλο, του, Τζεφ ,.. ]



20- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [φίλο, του, Τζεφ ,.. ]



21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [φίλο]   B= [του, Τζεφ, ( ,.. ]



22- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [του, Τζεφ, ( ,.. ]



23- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [του]   B= [Τζεφ, (, Μπιλ ,.. ]



24- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Τζεφ, (, Μπιλ ,.. ]



25- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Τζεφ]   B= [(, Μπιλ, Μάρεϊ ,.. ]



26- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [(, Μπιλ, Μάρεϊ ,.. ]



27- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [(]   B= [Μπιλ, Μάρεϊ, ) ,.. ]



28- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Μπιλ, Μάρεϊ, ) ,.. ]



29- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Μπιλ]   B= [Μάρεϊ, ), να ,.. ]



30- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Μάρεϊ, ), να ,.. ]



31- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Μάρεϊ]   B= [), να, ανεβάσει ,.. ]



32- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [), να, ανεβάσει ,.. ]



33- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [)]   B= [να, ανεβάσει, το ,.. ]



34- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [να, ανεβάσει, το ,.. ]



35- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [να]   B= [ανεβάσει, το, θεατρικό ,.. ]



36- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ανεβάσει, το, θεατρικό ,.. ]



37- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ανεβάσει]   B= [το, θεατρικό, του ,.. ]



38- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [το, θεατρικό, του ,.. ]



39- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [το]   B= [θεατρικό, του, έργο ,.. ]



40- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [θεατρικό, του, έργο ,.. ]



41- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [θεατρικό]   B= [του, έργο, , ,.. ]



42- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [του, έργο, , ,.. ]



43- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [του]   B= [έργο, ,, μεταμφιέζεται ,.. ]



44- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [έργο, ,, μεταμφιέζεται ,.. ]



45- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [έργο]   B= [,, μεταμφιέζεται, σε ,.. ]



46- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, μεταμφιέζεται, σε ,.. ]



47- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [μεταμφιέζεται, σε, γυναίκα ,.. ]



48- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [μεταμφιέζεται, σε, γυναίκα ,.. ]



49- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [μεταμφιέζεται]   B= [σε, γυναίκα, με ,.. ]



50- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [σε, γυναίκα, με ,.. ]



51- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [σε]   B= [γυναίκα, με, το ,.. ]



52- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [γυναίκα, με, το ,.. ]



53- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [γυναίκα]   B= [με, το, όνομα ,.. ]



54- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [με, το, όνομα ,.. ]



55- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [με]   B= [το, όνομα, Ντόροθι ,.. ]



56- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [το, όνομα, Ντόροθι ,.. ]



57- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [το]   B= [όνομα, Ντόροθι, Μάικλς ,.. ]



58- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [όνομα, Ντόροθι, Μάικλς ,.. ]



59- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [όνομα]   B= [Ντόροθι, Μάικλς, και ,.. ]



60- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Ντόροθι, Μάικλς, και ,.. ]



61- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Ντόροθι]   B= [Μάικλς, και, πιάνει ,.. ]



62- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Μάικλς, και, πιάνει ,.. ]



63- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Μάικλς]   B= [και, πιάνει, δουλειά ,.. ]



64- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [και, πιάνει, δουλειά ,.. ]



65- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [και]   B= [πιάνει, δουλειά, σε ,.. ]



66- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [πιάνει, δουλειά, σε ,.. ]



67- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [πιάνει]   B= [δουλειά, σε, μια ,.. ]



68- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [πιάνει, δουλειά]   B= [σε, μια, σαπουνόπερα ,.. ]



69- **MERGE_AS_OTH**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[πιάνει, δουλειά]]   B= [σε, μια, σαπουνόπερα ,.. ]



70- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [σε, μια, σαπουνόπερα ,.. ]



71- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [σε]   B= [μια, σαπουνόπερα, , ,.. ]



72- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [μια, σαπουνόπερα, , ,.. ]



73- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [μια]   B= [σαπουνόπερα, ,, χωρίς ,.. ]



74- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [σαπουνόπερα, ,, χωρίς ,.. ]



75- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [σαπουνόπερα]   B= [,, χωρίς, κανείς ,.. ]



76- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, χωρίς, κανείς ,.. ]



77- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [χωρίς, κανείς, να ,.. ]



78- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [χωρίς, κανείς, να ,.. ]



79- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [χωρίς]   B= [κανείς, να, ξέρει ,.. ]



80- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [κανείς, να, ξέρει ,.. ]



81- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [κανείς]   B= [να, ξέρει, ότι ,.. ]



82- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [να, ξέρει, ότι ,.. ]



83- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [να]   B= [ξέρει, ότι, είναι ,.. ]



84- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ξέρει, ότι, είναι ,.. ]



85- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ξέρει]   B= [ότι, είναι, άνδρας ,.. ]



86- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ότι, είναι, άνδρας ,.. ]



87- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ότι]   B= [είναι, άνδρας, . ,.. ]



88- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [είναι, άνδρας, . ,.. ]



89- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [είναι]   B= [άνδρας, . ,.. ]



90- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [άνδρας, . ,.. ]



91- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [άνδρας]   B= [.]



92- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [.]



93- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [ ]



94- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

## Sentence No. 1137 - 
Θα **φέρει** **τα** **πάνω** **κάτω** στις ζωές των φιλενάδων της αλλά και της πόλης της όταν θα αποφασίσει να **πάρει** **συνέντευξη** από μαύρες γυναίκες , οι οποίες έχουν περάσει σχεδόν ολόκληρες τις ζωές τους ως υπηρέτριες σε λευκές οικογένειες πλουσίων . 
### Existing MWEs: 
1- **φέρει τα πάνω κάτω** (ID, 1)

2- **πάρει συνέντευξη** (LVC)

### Identified MWEs: 
1- **φέρει τα πάνω κάτω** (OTH)

black Merge Num : 2 Interleaving Num: 0


0- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Θα, φέρει, τα ,.. ]



1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Θα]   B= [φέρει, τα, πάνω ,.. ]



2- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [φέρει, τα, πάνω ,.. ]



3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [φέρει]   B= [τα, πάνω, κάτω ,.. ]



4- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [φέρει, τα]   B= [πάνω, κάτω, στις ,.. ]



5- **WHITE_MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[φέρει, τα]]   B= [πάνω, κάτω, στις ,.. ]



6- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[φέρει, τα]  πάνω]   B= [κάτω, στις, ζωές ,.. ]



7- **WHITE_MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[[φέρει, τα]  πάνω]]   B= [κάτω, στις, ζωές ,.. ]



8- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[[φέρει, τα]  πάνω]  κάτω]   B= [στις, ζωές, των ,.. ]



9- **MERGE_AS_OTH**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[[[φέρει, τα]  πάνω]  κάτω]]   B= [στις, ζωές, των ,.. ]



10- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[[[φέρει, τα]  πάνω]  κάτω]  στις]   B= [ζωές, των, φιλενάδων ,.. ]



11- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[[[φέρει, τα]  πάνω]  κάτω]]   B= [ζωές, των, φιλενάδων ,.. ]



12- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[[[φέρει, τα]  πάνω]  κάτω]  ζωές]   B= [των, φιλενάδων, της ,.. ]



13- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[[[φέρει, τα]  πάνω]  κάτω]]   B= [των, φιλενάδων, της ,.. ]



14- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[[[φέρει, τα]  πάνω]  κάτω]  των]   B= [φιλενάδων, της, αλλά ,.. ]



15- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[[[φέρει, τα]  πάνω]  κάτω]]   B= [φιλενάδων, της, αλλά ,.. ]



16- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[[[φέρει, τα]  πάνω]  κάτω]  φιλενάδων]   B= [της, αλλά, και ,.. ]



17- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[[[φέρει, τα]  πάνω]  κάτω]]   B= [της, αλλά, και ,.. ]



18- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[[[φέρει, τα]  πάνω]  κάτω]  της]   B= [αλλά, και, της ,.. ]



19- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[[[φέρει, τα]  πάνω]  κάτω]]   B= [αλλά, και, της ,.. ]



20- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[[[φέρει, τα]  πάνω]  κάτω]  αλλά]   B= [και, της, πόλης ,.. ]



21- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[[[φέρει, τα]  πάνω]  κάτω]]   B= [και, της, πόλης ,.. ]



22- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[[[φέρει, τα]  πάνω]  κάτω]  και]   B= [της, πόλης, της ,.. ]



23- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[[[φέρει, τα]  πάνω]  κάτω]]   B= [της, πόλης, της ,.. ]



24- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[[[φέρει, τα]  πάνω]  κάτω]  της]   B= [πόλης, της, όταν ,.. ]



25- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[[[φέρει, τα]  πάνω]  κάτω]]   B= [πόλης, της, όταν ,.. ]



26- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[[[φέρει, τα]  πάνω]  κάτω]  πόλης]   B= [της, όταν, θα ,.. ]



27- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[[[φέρει, τα]  πάνω]  κάτω]]   B= [της, όταν, θα ,.. ]



28- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[[[φέρει, τα]  πάνω]  κάτω]  της]   B= [όταν, θα, αποφασίσει ,.. ]



29- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[[[φέρει, τα]  πάνω]  κάτω]]   B= [όταν, θα, αποφασίσει ,.. ]



30- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[[[φέρει, τα]  πάνω]  κάτω]  όταν]   B= [θα, αποφασίσει, να ,.. ]



31- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[[[φέρει, τα]  πάνω]  κάτω]]   B= [θα, αποφασίσει, να ,.. ]



32- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[[[φέρει, τα]  πάνω]  κάτω]  θα]   B= [αποφασίσει, να, πάρει ,.. ]



33- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[[[φέρει, τα]  πάνω]  κάτω]]   B= [αποφασίσει, να, πάρει ,.. ]



34- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[[[φέρει, τα]  πάνω]  κάτω]  αποφασίσει]   B= [να, πάρει, συνέντευξη ,.. ]



35- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[[[φέρει, τα]  πάνω]  κάτω]]   B= [να, πάρει, συνέντευξη ,.. ]



36- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[[[φέρει, τα]  πάνω]  κάτω]  να]   B= [πάρει, συνέντευξη, από ,.. ]



37- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[[[φέρει, τα]  πάνω]  κάτω]]   B= [πάρει, συνέντευξη, από ,.. ]



38- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[[[φέρει, τα]  πάνω]  κάτω]  πάρει]   B= [συνέντευξη, από, μαύρες ,.. ]



39- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[[[φέρει, τα]  πάνω]  κάτω]]   B= [συνέντευξη, από, μαύρες ,.. ]



40- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[[[φέρει, τα]  πάνω]  κάτω]  συνέντευξη]   B= [από, μαύρες, γυναίκες ,.. ]



41- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[[[φέρει, τα]  πάνω]  κάτω]]   B= [από, μαύρες, γυναίκες ,.. ]



42- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[[[φέρει, τα]  πάνω]  κάτω]  από]   B= [μαύρες, γυναίκες, , ,.. ]



43- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[[[φέρει, τα]  πάνω]  κάτω]]   B= [μαύρες, γυναίκες, , ,.. ]



44- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[[[φέρει, τα]  πάνω]  κάτω]  μαύρες]   B= [γυναίκες, ,, οι ,.. ]



45- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[[[φέρει, τα]  πάνω]  κάτω]]   B= [γυναίκες, ,, οι ,.. ]



46- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[[[φέρει, τα]  πάνω]  κάτω]  γυναίκες]   B= [,, οι, οποίες ,.. ]



47- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[[[φέρει, τα]  πάνω]  κάτω]]   B= [,, οι, οποίες ,.. ]



48- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[[[φέρει, τα]  πάνω]  κάτω]  ,]   B= [οι, οποίες, έχουν ,.. ]



49- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[[[φέρει, τα]  πάνω]  κάτω]]   B= [οι, οποίες, έχουν ,.. ]



50- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[[[φέρει, τα]  πάνω]  κάτω]  οι]   B= [οποίες, έχουν, περάσει ,.. ]



51- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[[[φέρει, τα]  πάνω]  κάτω]]   B= [οποίες, έχουν, περάσει ,.. ]



52- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[[[φέρει, τα]  πάνω]  κάτω]  οποίες]   B= [έχουν, περάσει, σχεδόν ,.. ]



53- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[[[φέρει, τα]  πάνω]  κάτω]]   B= [έχουν, περάσει, σχεδόν ,.. ]



54- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[[[φέρει, τα]  πάνω]  κάτω]  έχουν]   B= [περάσει, σχεδόν, ολόκληρες ,.. ]



55- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[[[φέρει, τα]  πάνω]  κάτω]]   B= [περάσει, σχεδόν, ολόκληρες ,.. ]



56- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[[[φέρει, τα]  πάνω]  κάτω]  περάσει]   B= [σχεδόν, ολόκληρες, τις ,.. ]



57- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[[[φέρει, τα]  πάνω]  κάτω]]   B= [σχεδόν, ολόκληρες, τις ,.. ]



58- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[[[φέρει, τα]  πάνω]  κάτω]  σχεδόν]   B= [ολόκληρες, τις, ζωές ,.. ]



59- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[[[φέρει, τα]  πάνω]  κάτω]]   B= [ολόκληρες, τις, ζωές ,.. ]



60- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[[[φέρει, τα]  πάνω]  κάτω]  ολόκληρες]   B= [τις, ζωές, τους ,.. ]



61- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[[[φέρει, τα]  πάνω]  κάτω]]   B= [τις, ζωές, τους ,.. ]



62- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[[[φέρει, τα]  πάνω]  κάτω]  τις]   B= [ζωές, τους, ως ,.. ]



63- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[[[φέρει, τα]  πάνω]  κάτω]]   B= [ζωές, τους, ως ,.. ]



64- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[[[φέρει, τα]  πάνω]  κάτω]  ζωές]   B= [τους, ως, υπηρέτριες ,.. ]



65- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[[[φέρει, τα]  πάνω]  κάτω]]   B= [τους, ως, υπηρέτριες ,.. ]



66- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[[[φέρει, τα]  πάνω]  κάτω]  τους]   B= [ως, υπηρέτριες, σε ,.. ]



67- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[[[φέρει, τα]  πάνω]  κάτω]]   B= [ως, υπηρέτριες, σε ,.. ]



68- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[[[φέρει, τα]  πάνω]  κάτω]  ως]   B= [υπηρέτριες, σε, λευκές ,.. ]



69- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[[[φέρει, τα]  πάνω]  κάτω]]   B= [υπηρέτριες, σε, λευκές ,.. ]



70- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[[[φέρει, τα]  πάνω]  κάτω]  υπηρέτριες]   B= [σε, λευκές, οικογένειες ,.. ]



71- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[[[φέρει, τα]  πάνω]  κάτω]]   B= [σε, λευκές, οικογένειες ,.. ]



72- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[[[φέρει, τα]  πάνω]  κάτω]  σε]   B= [λευκές, οικογένειες, πλουσίων ,.. ]



73- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[[[φέρει, τα]  πάνω]  κάτω]]   B= [λευκές, οικογένειες, πλουσίων ,.. ]



74- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[[[φέρει, τα]  πάνω]  κάτω]  λευκές]   B= [οικογένειες, πλουσίων, . ,.. ]



75- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[[[φέρει, τα]  πάνω]  κάτω]]   B= [οικογένειες, πλουσίων, . ,.. ]



76- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[[[φέρει, τα]  πάνω]  κάτω]  οικογένειες]   B= [πλουσίων, . ,.. ]



77- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[[[φέρει, τα]  πάνω]  κάτω]]   B= [πλουσίων, . ,.. ]



78- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[[[φέρει, τα]  πάνω]  κάτω]  πλουσίων]   B= [.]



79- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[[[φέρει, τα]  πάνω]  κάτω]]   B= [.]



80- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[[[φέρει, τα]  πάνω]  κάτω]  .]   B= [ ]



81- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[[[φέρει, τα]  πάνω]  κάτω]]   B= [ ]



82- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

## Sentence No. 1203 - 
**Η** **χαριστική** **βολή** **δίνεται** όταν **πιάνουν** **συζήτηση** για το δεκαεξάχρονο γιο του Τζορτζ και της Μάρθας που πρόκειται να γιορτάσει τα γενέθλιά του την επόμενη μέρα . 
### Existing MWEs: 
2- **Η χαριστική βολή δίνεται** (ID)

1- **πιάνουν συζήτηση** (ID)

### Identified MWEs: 
1- **πιάνουν συζήτηση** (OTH)

black Merge Num : 2 Interleaving Num: 0


0- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Η, χαριστική, βολή ,.. ]



1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Η]   B= [χαριστική, βολή, δίνεται ,.. ]



2- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [χαριστική, βολή, δίνεται ,.. ]



3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [χαριστική]   B= [βολή, δίνεται, όταν ,.. ]



4- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [βολή, δίνεται, όταν ,.. ]



5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [βολή]   B= [δίνεται, όταν, πιάνουν ,.. ]



6- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [δίνεται, όταν, πιάνουν ,.. ]



7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [δίνεται]   B= [όταν, πιάνουν, συζήτηση ,.. ]



8- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [δίνεται, όταν]   B= [πιάνουν, συζήτηση, για ,.. ]



9- **WHITE_MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[δίνεται, όταν]]   B= [πιάνουν, συζήτηση, για ,.. ]



10- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[δίνεται, όταν]  πιάνουν]   B= [συζήτηση, για, το ,.. ]



11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[δίνεται, όταν]  πιάνουν, συζήτηση]   B= [για, το, δεκαεξάχρονο ,.. ]



12- **MERGE_AS_OTH**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[δίνεται, όταν]  [πιάνουν, συζήτηση]]   B= [για, το, δεκαεξάχρονο ,.. ]



13- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[δίνεται, όταν]]   B= [για, το, δεκαεξάχρονο ,.. ]



14- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[δίνεται, όταν]  για]   B= [το, δεκαεξάχρονο, γιο ,.. ]



15- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[δίνεται, όταν]]   B= [το, δεκαεξάχρονο, γιο ,.. ]



16- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [το, δεκαεξάχρονο, γιο ,.. ]



17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [το]   B= [δεκαεξάχρονο, γιο, του ,.. ]



18- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [δεκαεξάχρονο, γιο, του ,.. ]



19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [δεκαεξάχρονο]   B= [γιο, του, Τζορτζ ,.. ]



20- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [γιο, του, Τζορτζ ,.. ]



21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [γιο]   B= [του, Τζορτζ, και ,.. ]



22- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [του, Τζορτζ, και ,.. ]



23- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [του]   B= [Τζορτζ, και, της ,.. ]



24- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Τζορτζ, και, της ,.. ]



25- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Τζορτζ]   B= [και, της, Μάρθας ,.. ]



26- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [και, της, Μάρθας ,.. ]



27- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [και]   B= [της, Μάρθας, που ,.. ]



28- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [της, Μάρθας, που ,.. ]



29- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [της]   B= [Μάρθας, που, πρόκειται ,.. ]



30- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Μάρθας, που, πρόκειται ,.. ]



31- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Μάρθας]   B= [που, πρόκειται, να ,.. ]



32- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [που, πρόκειται, να ,.. ]



33- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [που]   B= [πρόκειται, να, γιορτάσει ,.. ]



34- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [πρόκειται, να, γιορτάσει ,.. ]



35- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [πρόκειται]   B= [να, γιορτάσει, τα ,.. ]



36- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [να, γιορτάσει, τα ,.. ]



37- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [να]   B= [γιορτάσει, τα, γενέθλιά ,.. ]



38- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [γιορτάσει, τα, γενέθλιά ,.. ]



39- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [γιορτάσει]   B= [τα, γενέθλιά, του ,.. ]



40- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [τα, γενέθλιά, του ,.. ]



41- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [τα]   B= [γενέθλιά, του, την ,.. ]



42- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [γενέθλιά, του, την ,.. ]



43- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [γενέθλιά]   B= [του, την, επόμενη ,.. ]



44- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [του, την, επόμενη ,.. ]



45- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [του]   B= [την, επόμενη, μέρα ,.. ]



46- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [την, επόμενη, μέρα ,.. ]



47- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [την]   B= [επόμενη, μέρα, . ,.. ]



48- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [επόμενη, μέρα, . ,.. ]



49- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [επόμενη]   B= [μέρα, . ,.. ]



50- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [μέρα, . ,.. ]



51- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [μέρα]   B= [.]



52- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [.]



53- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [ ]



54- REDUCE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

