## Sentence No. 1777 - 
Във вторник Ердоган направи изявление , в което призова двете страни в Кипър да направят отстъпки и да постигнат споразумение . ( АФП , Анадолска агенция , ТРТ - 28 / 1 / 3 )
### Existing MWEs: 
1- **направи изявление** (LVC)
2- **направят отстъпки** (LVC)
3- **постигнат споразумение** (LVC)
### Identified MWEs: 
1- **направи изявление** 

2- **направят отстъпки** 

3- **постигнат споразумение** 




0- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Във, вторник, Ердоган ,.. ]

B0Token: Във, B0_LastThreeLetters: �в, B0_LastTwoLetters: в, 

1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Във]   B= [вторник, Ердоган, направи ,.. ]

B0Token: вторник, B0_LastThreeLetters: �к, B0_LastTwoLetters: к, S0B0Distance: 1, S0B0Token: Във_вторник, S0B1Token: Във_Ердоган, S0Token: Във, S0_LastThreeLetters: �в, S0_LastTwoLetters: в, TransHistory1: 0, 

2- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [вторник, Ердоган, направи ,.. ]

B0Token: вторник, B0_LastThreeLetters: �к, B0_LastTwoLetters: к, TransHistory1: 0, TransHistory2: 00, 

3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [вторник]   B= [Ердоган, направи, изявление ,.. ]

B0Token: Ердоган, B0_LastThreeLetters: �н, B0_LastTwoLetters: н, S0B0Distance: 1, S0B0Token: вторник_Ердоган, S0B1Token: вторник_направи, S0Token: вторник, S0_LastThreeLetters: �к, S0_LastTwoLetters: к, TransHistory1: 2, TransHistory2: 20, 

4- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Ердоган, направи, изявление ,.. ]

B0Token: Ердоган, B0_LastThreeLetters: �н, B0_LastTwoLetters: н, TransHistory1: 0, TransHistory2: 02, 

5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Ердоган]   B= [направи, изявление, , ,.. ]

B0Token: направи, B0_LastThreeLetters: �и, B0_LastTwoLetters: и, S0B0Distance: 1, S0B0Token: Ердоган_направи, S0B1Token: Ердоган_изявление, S0Token: Ердоган, S0_LastThreeLetters: �н, S0_LastTwoLetters: н, TransHistory1: 2, TransHistory2: 20, 

6- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [направи, изявление, , ,.. ]

B0Token: направи, B0_LastThreeLetters: �и, B0_LastTwoLetters: и, TransHistory1: 0, TransHistory2: 02, 

7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [направи]   B= [изявление, ,, в ,.. ]

B0Token: изявление, B0_LastThreeLetters: �е, B0_LastTwoLetters: е, S0B0Distance: 1, S0B0Token: направи_изявление, S0B1Token: направи_,, S0Token: направи, S0_LastThreeLetters: �и, S0_LastTwoLetters: и, TransHistory1: 2, TransHistory2: 20, 

8- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [направи, изявление]   B= [,, в, което ,.. ]

B0Token: ,, B0_LastThreeLetters: ,, B0_LastTwoLetters: ,, S0B0Distance: 1, S0B0Token: изявление_,, S0B1Token: изявление_в, S0Token: изявление, S0_LastThreeLetters: �е, S0_LastTwoLetters: е, S1B0Token: направи_,, S1S0B0Token: направи_изявление_,, S1S0Token: направи_изявление, S1Token: направи, S1_LastThreeLetters: �и, S1_LastTwoLetters: и, TransHistory1: 0, TransHistory2: 02, 

9- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[направи, изявление]]   B= [,, в, което ,.. ]

B0Token: ,, B0_LastThreeLetters: ,, B0_LastTwoLetters: ,, S0B0Distance: 1, S0B0Token: направи_изявление_,, S0B1Token: направи_изявление_в, S0Token: направи_изявление, S0_LastThreeLetters: �е, S0_LastTwoLetters: е, TransHistory1: 0, TransHistory2: 00, 

10- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, в, което ,.. ]

B0Token: ,, B0_LastThreeLetters: ,, B0_LastTwoLetters: ,, TransHistory1: 1, TransHistory2: 10, 

11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [в, което, призова ,.. ]

B0Token: в, B0_LastThreeLetters: в, B0_LastTwoLetters: в, S0B0Distance: 1, S0B0Token: ,_в, S0B1Token: ,_което, S0Token: ,, S0_LastThreeLetters: ,, S0_LastTwoLetters: ,, TransHistory1: 2, TransHistory2: 21, 

12- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [в, което, призова ,.. ]

B0Token: в, B0_LastThreeLetters: в, B0_LastTwoLetters: в, TransHistory1: 0, TransHistory2: 02, 

13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [в]   B= [което, призова, двете ,.. ]

B0Token: което, B0_LastThreeLetters: �о, B0_LastTwoLetters: о, S0B0Distance: 1, S0B0Token: в_което, S0B1Token: в_призова, S0Token: в, S0_LastThreeLetters: в, S0_LastTwoLetters: в, TransHistory1: 2, TransHistory2: 20, 

14- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [което, призова, двете ,.. ]

B0Token: което, B0_LastThreeLetters: �о, B0_LastTwoLetters: о, TransHistory1: 0, TransHistory2: 02, 

15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [което]   B= [призова, двете, страни ,.. ]

B0Token: призова, B0_LastThreeLetters: �а, B0_LastTwoLetters: а, S0B0Distance: 1, S0B0Token: което_призова, S0B1Token: което_двете, S0Token: което, S0_LastThreeLetters: �о, S0_LastTwoLetters: о, TransHistory1: 2, TransHistory2: 20, 

16- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [призова, двете, страни ,.. ]

B0Token: призова, B0_LastThreeLetters: �а, B0_LastTwoLetters: а, TransHistory1: 0, TransHistory2: 02, 

17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [призова]   B= [двете, страни, в ,.. ]

B0Token: двете, B0_LastThreeLetters: �е, B0_LastTwoLetters: е, S0B0Distance: 1, S0B0Token: призова_двете, S0B1Token: призова_страни, S0Token: призова, S0_LastThreeLetters: �а, S0_LastTwoLetters: а, TransHistory1: 2, TransHistory2: 20, 

18- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [двете, страни, в ,.. ]

B0Token: двете, B0_LastThreeLetters: �е, B0_LastTwoLetters: е, TransHistory1: 0, TransHistory2: 02, 

19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [двете]   B= [страни, в, Кипър ,.. ]

B0Token: страни, B0_LastThreeLetters: �и, B0_LastTwoLetters: и, S0B0Distance: 1, S0B0Token: двете_страни, S0B1Token: двете_в, S0Token: двете, S0_LastThreeLetters: �е, S0_LastTwoLetters: е, TransHistory1: 2, TransHistory2: 20, 

20- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [страни, в, Кипър ,.. ]

B0Token: страни, B0_LastThreeLetters: �и, B0_LastTwoLetters: и, TransHistory1: 0, TransHistory2: 02, 

21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [страни]   B= [в, Кипър, да ,.. ]

B0Token: в, B0_LastThreeLetters: в, B0_LastTwoLetters: в, S0B0Distance: 1, S0B0Token: страни_в, S0B1Token: страни_Кипър, S0Token: страни, S0_LastThreeLetters: �и, S0_LastTwoLetters: и, TransHistory1: 2, TransHistory2: 20, 

22- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [в, Кипър, да ,.. ]

B0Token: в, B0_LastThreeLetters: в, B0_LastTwoLetters: в, TransHistory1: 0, TransHistory2: 02, 

23- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [в]   B= [Кипър, да, направят ,.. ]

B0Token: Кипър, B0_LastThreeLetters: �р, B0_LastTwoLetters: р, S0B0Distance: 1, S0B0Token: в_Кипър, S0B1Token: в_да, S0Token: в, S0_LastThreeLetters: в, S0_LastTwoLetters: в, TransHistory1: 2, TransHistory2: 20, 

24- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Кипър, да, направят ,.. ]

B0Token: Кипър, B0_LastThreeLetters: �р, B0_LastTwoLetters: р, TransHistory1: 0, TransHistory2: 02, 

25- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Кипър]   B= [да, направят, отстъпки ,.. ]

B0Token: да, B0_LastThreeLetters: �а, B0_LastTwoLetters: а, S0B0Distance: 1, S0B0Token: Кипър_да, S0B1Token: Кипър_направят, S0Token: Кипър, S0_LastThreeLetters: �р, S0_LastTwoLetters: р, TransHistory1: 2, TransHistory2: 20, 

26- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [да, направят, отстъпки ,.. ]

B0Token: да, B0_LastThreeLetters: �а, B0_LastTwoLetters: а, TransHistory1: 0, TransHistory2: 02, 

27- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [да]   B= [направят, отстъпки, и ,.. ]

B0Token: направят, B0_LastThreeLetters: �т, B0_LastTwoLetters: т, S0B0Distance: 1, S0B0Token: да_направят, S0B1Token: да_отстъпки, S0Token: да, S0_LastThreeLetters: �а, S0_LastTwoLetters: а, TransHistory1: 2, TransHistory2: 20, 

28- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [направят, отстъпки, и ,.. ]

B0Token: направят, B0_LastThreeLetters: �т, B0_LastTwoLetters: т, TransHistory1: 0, TransHistory2: 02, 

29- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [направят]   B= [отстъпки, и, да ,.. ]

B0Token: отстъпки, B0_LastThreeLetters: �и, B0_LastTwoLetters: и, S0B0Distance: 1, S0B0Token: направят_отстъпки, S0B1Token: направят_и, S0Token: направят, S0_LastThreeLetters: �т, S0_LastTwoLetters: т, TransHistory1: 2, TransHistory2: 20, 

30- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [направят, отстъпки]   B= [и, да, постигнат ,.. ]

B0Token: и, B0_LastThreeLetters: и, B0_LastTwoLetters: и, S0B0Distance: 1, S0B0Token: отстъпки_и, S0B1Token: отстъпки_да, S0Token: отстъпки, S0_LastThreeLetters: �и, S0_LastTwoLetters: и, S1B0Token: направят_и, S1S0B0Token: направят_отстъпки_и, S1S0Token: направят_отстъпки, S1Token: направят, S1_LastThreeLetters: �т, S1_LastTwoLetters: т, TransHistory1: 0, TransHistory2: 02, 

31- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[направят, отстъпки]]   B= [и, да, постигнат ,.. ]

B0Token: и, B0_LastThreeLetters: и, B0_LastTwoLetters: и, S0B0Distance: 1, S0B0Token: направят_отстъпки_и, S0B1Token: направят_отстъпки_да, S0Token: направят_отстъпки, S0_LastThreeLetters: �и, S0_LastTwoLetters: и, TransHistory1: 0, TransHistory2: 00, 

32- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [и, да, постигнат ,.. ]

B0Token: и, B0_LastThreeLetters: и, B0_LastTwoLetters: и, TransHistory1: 1, TransHistory2: 10, 

33- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [и]   B= [да, постигнат, споразумение ,.. ]

B0Token: да, B0_LastThreeLetters: �а, B0_LastTwoLetters: а, S0B0Distance: 1, S0B0Token: и_да, S0B1Token: и_постигнат, S0Token: и, S0_LastThreeLetters: и, S0_LastTwoLetters: и, TransHistory1: 2, TransHistory2: 21, 

34- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [да, постигнат, споразумение ,.. ]

B0Token: да, B0_LastThreeLetters: �а, B0_LastTwoLetters: а, TransHistory1: 0, TransHistory2: 02, 

35- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [да]   B= [постигнат, споразумение, . ,.. ]

B0Token: постигнат, B0_LastThreeLetters: �т, B0_LastTwoLetters: т, S0B0Distance: 1, S0B0Token: да_постигнат, S0B1Token: да_споразумение, S0Token: да, S0_LastThreeLetters: �а, S0_LastTwoLetters: а, TransHistory1: 2, TransHistory2: 20, 

36- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [постигнат, споразумение, . ,.. ]

B0Token: постигнат, B0_LastThreeLetters: �т, B0_LastTwoLetters: т, TransHistory1: 0, TransHistory2: 02, 

37- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [постигнат]   B= [споразумение, ., ( ,.. ]

B0Token: споразумение, B0_LastThreeLetters: �е, B0_LastTwoLetters: е, S0B0Distance: 1, S0B0Token: постигнат_споразумение, S0B1Token: постигнат_., S0Token: постигнат, S0_LastThreeLetters: �т, S0_LastTwoLetters: т, TransHistory1: 2, TransHistory2: 20, 

38- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [постигнат, споразумение]   B= [., (, АФП ,.. ]

B0Token: ., B0_LastThreeLetters: ., B0_LastTwoLetters: ., S0B0Distance: 1, S0B0Token: споразумение_., S0B1Token: споразумение_(, S0Token: споразумение, S0_LastThreeLetters: �е, S0_LastTwoLetters: е, S1B0Token: постигнат_., S1S0B0Token: постигнат_споразумение_., S1S0Token: постигнат_споразумение, S1Token: постигнат, S1_LastThreeLetters: �т, S1_LastTwoLetters: т, TransHistory1: 0, TransHistory2: 02, 

39- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[постигнат, споразумение]]   B= [., (, АФП ,.. ]

B0Token: ., B0_LastThreeLetters: ., B0_LastTwoLetters: ., S0B0Distance: 1, S0B0Token: постигнат_споразумение_., S0B1Token: постигнат_споразумение_(, S0Token: постигнат_споразумение, S0_LastThreeLetters: �е, S0_LastTwoLetters: е, TransHistory1: 0, TransHistory2: 00, 

40- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [., (, АФП ,.. ]

B0Token: ., B0_LastThreeLetters: ., B0_LastTwoLetters: ., TransHistory1: 1, TransHistory2: 10, 

41- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [(, АФП, , ,.. ]

B0Token: (, B0_LastThreeLetters: (, B0_LastTwoLetters: (, S0B0Distance: 1, S0B0Token: ._(, S0B1Token: ._АФП, S0Token: ., S0_LastThreeLetters: ., S0_LastTwoLetters: ., TransHistory1: 2, TransHistory2: 21, 

42- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [(, АФП, , ,.. ]

B0Token: (, B0_LastThreeLetters: (, B0_LastTwoLetters: (, TransHistory1: 0, TransHistory2: 02, 

43- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [(]   B= [АФП, ,, Анадолска ,.. ]

B0Token: АФП, B0_LastThreeLetters: �П, B0_LastTwoLetters: П, S0B0Distance: 1, S0B0Token: (_АФП, S0B1Token: (_,, S0Token: (, S0_LastThreeLetters: (, S0_LastTwoLetters: (, TransHistory1: 2, TransHistory2: 20, 

44- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [АФП, ,, Анадолска ,.. ]

B0Token: АФП, B0_LastThreeLetters: �П, B0_LastTwoLetters: П, TransHistory1: 0, TransHistory2: 02, 

45- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [АФП]   B= [,, Анадолска, агенция ,.. ]

B0Token: ,, B0_LastThreeLetters: ,, B0_LastTwoLetters: ,, S0B0Distance: 1, S0B0Token: АФП_,, S0B1Token: АФП_Анадолска, S0Token: АФП, S0_LastThreeLetters: �П, S0_LastTwoLetters: П, TransHistory1: 2, TransHistory2: 20, 

46- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, Анадолска, агенция ,.. ]

B0Token: ,, B0_LastThreeLetters: ,, B0_LastTwoLetters: ,, TransHistory1: 0, TransHistory2: 02, 

47- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [Анадолска, агенция, , ,.. ]

B0Token: Анадолска, B0_LastThreeLetters: �а, B0_LastTwoLetters: а, S0B0Distance: 1, S0B0Token: ,_Анадолска, S0B1Token: ,_агенция, S0Token: ,, S0_LastThreeLetters: ,, S0_LastTwoLetters: ,, TransHistory1: 2, TransHistory2: 20, 

48- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Анадолска, агенция, , ,.. ]

B0Token: Анадолска, B0_LastThreeLetters: �а, B0_LastTwoLetters: а, TransHistory1: 0, TransHistory2: 02, 

49- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Анадолска]   B= [агенция, ,, ТРТ ,.. ]

B0Token: агенция, B0_LastThreeLetters: �я, B0_LastTwoLetters: я, S0B0Distance: 1, S0B0Token: Анадолска_агенция, S0B1Token: Анадолска_,, S0Token: Анадолска, S0_LastThreeLetters: �а, S0_LastTwoLetters: а, TransHistory1: 2, TransHistory2: 20, 

50- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [агенция, ,, ТРТ ,.. ]

B0Token: агенция, B0_LastThreeLetters: �я, B0_LastTwoLetters: я, TransHistory1: 0, TransHistory2: 02, 

51- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [агенция]   B= [,, ТРТ, - ,.. ]

B0Token: ,, B0_LastThreeLetters: ,, B0_LastTwoLetters: ,, S0B0Distance: 1, S0B0Token: агенция_,, S0B1Token: агенция_ТРТ, S0Token: агенция, S0_LastThreeLetters: �я, S0_LastTwoLetters: я, TransHistory1: 2, TransHistory2: 20, 

52- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, ТРТ, - ,.. ]

B0Token: ,, B0_LastThreeLetters: ,, B0_LastTwoLetters: ,, TransHistory1: 0, TransHistory2: 02, 

53- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [ТРТ, -, 28 ,.. ]

B0Token: ТРТ, B0_LastThreeLetters: �Т, B0_LastTwoLetters: Т, S0B0Distance: 1, S0B0Token: ,_ТРТ, S0B1Token: ,_-, S0Token: ,, S0_LastThreeLetters: ,, S0_LastTwoLetters: ,, TransHistory1: 2, TransHistory2: 20, 

54- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ТРТ, -, 28 ,.. ]

B0Token: ТРТ, B0_LastThreeLetters: �Т, B0_LastTwoLetters: Т, TransHistory1: 0, TransHistory2: 02, 

55- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ТРТ]   B= [-, 28, / ,.. ]

B0Token: -, B0_LastThreeLetters: -, B0_LastTwoLetters: -, S0B0Distance: 1, S0B0Token: ТРТ_-, S0B1Token: ТРТ_28, S0Token: ТРТ, S0_LastThreeLetters: �Т, S0_LastTwoLetters: Т, TransHistory1: 2, TransHistory2: 20, 

56- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [-, 28, / ,.. ]

B0Token: -, B0_LastThreeLetters: -, B0_LastTwoLetters: -, TransHistory1: 0, TransHistory2: 02, 

57- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [-]   B= [28, /, 1 ,.. ]

B0Token: 28, B0_LastThreeLetters: 28, B0_LastTwoLetters: 28, S0B0Distance: 1, S0B0Token: -_28, S0B1Token: -_/, S0Token: -, S0_LastThreeLetters: -, S0_LastTwoLetters: -, TransHistory1: 2, TransHistory2: 20, 

58- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [28, /, 1 ,.. ]

B0Token: 28, B0_LastThreeLetters: 28, B0_LastTwoLetters: 28, TransHistory1: 0, TransHistory2: 02, 

59- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [28]   B= [/, 1, / ,.. ]

B0Token: /, B0_LastThreeLetters: /, B0_LastTwoLetters: /, S0B0Distance: 1, S0B0Token: 28_/, S0B1Token: 28_1, S0Token: 28, S0_LastThreeLetters: 28, S0_LastTwoLetters: 28, TransHistory1: 2, TransHistory2: 20, 

60- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [/, 1, / ,.. ]

B0Token: /, B0_LastThreeLetters: /, B0_LastTwoLetters: /, TransHistory1: 0, TransHistory2: 02, 

61- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [/]   B= [1, /, 3 ,.. ]

B0Token: 1, B0_LastThreeLetters: 1, B0_LastTwoLetters: 1, S0B0Distance: 1, S0B0Token: /_1, S0B1Token: /_/, S0Token: /, S0_LastThreeLetters: /, S0_LastTwoLetters: /, TransHistory1: 2, TransHistory2: 20, 

62- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [1, /, 3 ,.. ]

B0Token: 1, B0_LastThreeLetters: 1, B0_LastTwoLetters: 1, TransHistory1: 0, TransHistory2: 02, 

63- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [1]   B= [/, 3, ) ,.. ]

B0Token: /, B0_LastThreeLetters: /, B0_LastTwoLetters: /, S0B0Distance: 1, S0B0Token: 1_/, S0B1Token: 1_3, S0Token: 1, S0_LastThreeLetters: 1, S0_LastTwoLetters: 1, TransHistory1: 2, TransHistory2: 20, 

64- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [/, 3, ) ,.. ]

B0Token: /, B0_LastThreeLetters: /, B0_LastTwoLetters: /, TransHistory1: 0, TransHistory2: 02, 

65- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [/]   B= [3, ) ,.. ]

B0Token: 3, B0_LastThreeLetters: 3, B0_LastTwoLetters: 3, S0B0Distance: 1, S0B0Token: /_3, S0B1Token: /_), S0Token: /, S0_LastThreeLetters: /, S0_LastTwoLetters: /, TransHistory1: 2, TransHistory2: 20, 

66- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [3, ) ,.. ]

B0Token: 3, B0_LastThreeLetters: 3, B0_LastTwoLetters: 3, TransHistory1: 0, TransHistory2: 02, 

67- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [3]   B= [)]

B0Token: ), B0_LastThreeLetters: ), B0_LastTwoLetters: ), S0B0Distance: 1, S0B0Token: 3_), S0Token: 3, S0_LastThreeLetters: 3, S0_LastTwoLetters: 3, TransHistory1: 2, TransHistory2: 20, 

68- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [)]

B0Token: ), B0_LastThreeLetters: ), B0_LastTwoLetters: ), TransHistory1: 0, TransHistory2: 02, 

69- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [)]   B= [ ]

S0Token: ), S0_LastThreeLetters: ), S0_LastTwoLetters: ), TransHistory1: 2, TransHistory2: 20, 

70- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

## Sentence No. 2188 - 
Той пое обещание правителството да направи всичко възможно , за да се справи с проблема .
### Existing MWEs: 
1- **пое обещание** (LVC)
2- **направи всичко възможно** (ID)
3- **се справи** (IReflV)
### Identified MWEs: 
1- **пое обещание** 

2- **направи всичко възможно** 

3- **се справи** 




0- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Той, пое, обещание ,.. ]

B0Token: Той, B0_LastThreeLetters: �й, B0_LastTwoLetters: й, 

1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Той]   B= [пое, обещание, правителството ,.. ]

B0Token: пое, B0_LastThreeLetters: �е, B0_LastTwoLetters: е, S0B0Distance: 1, S0B0Token: Той_пое, S0B1Token: Той_обещание, S0Token: Той, S0_LastThreeLetters: �й, S0_LastTwoLetters: й, TransHistory1: 0, 

2- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [пое, обещание, правителството ,.. ]

B0Token: пое, B0_LastThreeLetters: �е, B0_LastTwoLetters: е, TransHistory1: 0, TransHistory2: 00, 

3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [пое]   B= [обещание, правителството, да ,.. ]

B0Token: обещание, B0_LastThreeLetters: �е, B0_LastTwoLetters: е, S0B0Distance: 1, S0B0Token: пое_обещание, S0B1Token: пое_правителството, S0Token: пое, S0_LastThreeLetters: �е, S0_LastTwoLetters: е, TransHistory1: 2, TransHistory2: 20, 

4- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [пое, обещание]   B= [правителството, да, направи ,.. ]

B0Token: правителството, B0_LastThreeLetters: �о, B0_LastTwoLetters: о, S0B0Distance: 1, S0B0Token: обещание_правителството, S0B1Token: обещание_да, S0Token: обещание, S0_LastThreeLetters: �е, S0_LastTwoLetters: е, S1B0Token: пое_правителството, S1S0B0Token: пое_обещание_правителството, S1S0Token: пое_обещание, S1Token: пое, S1_LastThreeLetters: �е, S1_LastTwoLetters: е, TransHistory1: 0, TransHistory2: 02, 

5- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[пое, обещание]]   B= [правителството, да, направи ,.. ]

B0Token: правителството, B0_LastThreeLetters: �о, B0_LastTwoLetters: о, S0B0Distance: 1, S0B0Token: пое_обещание_правителството, S0B1Token: пое_обещание_да, S0Token: пое_обещание, S0_LastThreeLetters: �е, S0_LastTwoLetters: е, TransHistory1: 0, TransHistory2: 00, 

6- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [правителството, да, направи ,.. ]

B0Token: правителството, B0_LastThreeLetters: �о, B0_LastTwoLetters: о, TransHistory1: 1, TransHistory2: 10, 

7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [правителството]   B= [да, направи, всичко ,.. ]

B0Token: да, B0_LastThreeLetters: �а, B0_LastTwoLetters: а, S0B0Distance: 1, S0B0Token: правителството_да, S0B1Token: правителството_направи, S0Token: правителството, S0_LastThreeLetters: �о, S0_LastTwoLetters: о, TransHistory1: 2, TransHistory2: 21, 

8- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [да, направи, всичко ,.. ]

B0Token: да, B0_LastThreeLetters: �а, B0_LastTwoLetters: а, TransHistory1: 0, TransHistory2: 02, 

9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [да]   B= [направи, всичко, възможно ,.. ]

B0Token: направи, B0_LastThreeLetters: �и, B0_LastTwoLetters: и, S0B0Distance: 1, S0B0Token: да_направи, S0B1Token: да_всичко, S0Token: да, S0_LastThreeLetters: �а, S0_LastTwoLetters: а, TransHistory1: 2, TransHistory2: 20, 

10- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [направи, всичко, възможно ,.. ]

B0Token: направи, B0_LastThreeLetters: �и, B0_LastTwoLetters: и, TransHistory1: 0, TransHistory2: 02, 

11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [направи]   B= [всичко, възможно, , ,.. ]

B0Token: всичко, B0_LastThreeLetters: �о, B0_LastTwoLetters: о, S0B0Distance: 1, S0B0Token: направи_всичко, S0B1Token: направи_възможно, S0Token: направи, S0_LastThreeLetters: �и, S0_LastTwoLetters: и, TransHistory1: 2, TransHistory2: 20, 

12- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [направи, всичко]   B= [възможно, ,, за ,.. ]

B0Token: възможно, B0_LastThreeLetters: �о, B0_LastTwoLetters: о, S0B0Distance: 1, S0B0Token: всичко_възможно, S0B1Token: всичко_,, S0Token: всичко, S0_LastThreeLetters: �о, S0_LastTwoLetters: о, S1B0Token: направи_възможно, S1S0B0Token: направи_всичко_възможно, S1S0Token: направи_всичко, S1Token: направи, S1_LastThreeLetters: �и, S1_LastTwoLetters: и, TransHistory1: 0, TransHistory2: 02, 

13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [направи, всичко, възможно]   B= [,, за, да ,.. ]

B0Token: ,, B0_LastThreeLetters: ,, B0_LastTwoLetters: ,, S0B0Distance: 1, S0B0Token: възможно_,, S0B1Token: възможно_за, S0Token: възможно, S0_LastThreeLetters: �о, S0_LastTwoLetters: о, S1B0Token: всичко_,, S1S0B0Token: всичко_възможно_,, S1S0Token: всичко_възможно, S1Token: всичко, S1_LastThreeLetters: �о, S1_LastTwoLetters: о, TransHistory1: 0, TransHistory2: 00, 

14- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [направи, [всичко, възможно]]   B= [,, за, да ,.. ]

B0Token: ,, B0_LastThreeLetters: ,, B0_LastTwoLetters: ,, S0B0Distance: 1, S0B0Token: всичко_възможно_,, S0B1Token: всичко_възможно_за, S0Token: всичко_възможно, S0_LastThreeLetters: �о, S0_LastTwoLetters: о, S1B0Token: направи_,, S1S0B0Token: направи_всичко_възможно_,, S1S0Token: направи_всичко_възможно, S1Token: направи, S1_LastThreeLetters: �и, S1_LastTwoLetters: и, TransHistory1: 0, TransHistory2: 00, 

15- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[направи, [всичко, възможно]]]   B= [,, за, да ,.. ]

B0Token: ,, B0_LastThreeLetters: ,, B0_LastTwoLetters: ,, S0B0Distance: 1, S0B0Token: направи_всичко_възможно_,, S0B1Token: направи_всичко_възможно_за, S0Token: направи_всичко_възможно, S0_LastThreeLetters: �о, S0_LastTwoLetters: о, TransHistory1: 1, TransHistory2: 10, 

16- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, за, да ,.. ]

B0Token: ,, B0_LastThreeLetters: ,, B0_LastTwoLetters: ,, TransHistory1: 1, TransHistory2: 11, 

17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [за, да, се ,.. ]

B0Token: за, B0_LastThreeLetters: �а, B0_LastTwoLetters: а, S0B0Distance: 1, S0B0Token: ,_за, S0B1Token: ,_да, S0Token: ,, S0_LastThreeLetters: ,, S0_LastTwoLetters: ,, TransHistory1: 2, TransHistory2: 21, 

18- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [за, да, се ,.. ]

B0Token: за, B0_LastThreeLetters: �а, B0_LastTwoLetters: а, TransHistory1: 0, TransHistory2: 02, 

19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [за]   B= [да, се, справи ,.. ]

B0Token: да, B0_LastThreeLetters: �а, B0_LastTwoLetters: а, S0B0Distance: 1, S0B0Token: за_да, S0B1Token: за_се, S0Token: за, S0_LastThreeLetters: �а, S0_LastTwoLetters: а, TransHistory1: 2, TransHistory2: 20, 

20- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [да, се, справи ,.. ]

B0Token: да, B0_LastThreeLetters: �а, B0_LastTwoLetters: а, TransHistory1: 0, TransHistory2: 02, 

21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [да]   B= [се, справи, с ,.. ]

B0Token: се, B0_LastThreeLetters: �е, B0_LastTwoLetters: е, S0B0Distance: 1, S0B0Token: да_се, S0B1Token: да_справи, S0Token: да, S0_LastThreeLetters: �а, S0_LastTwoLetters: а, TransHistory1: 2, TransHistory2: 20, 

22- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [се, справи, с ,.. ]

B0Token: се, B0_LastThreeLetters: �е, B0_LastTwoLetters: е, TransHistory1: 0, TransHistory2: 02, 

23- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [се]   B= [справи, с, проблема ,.. ]

B0Token: справи, B0_LastThreeLetters: �и, B0_LastTwoLetters: и, S0B0Distance: 1, S0B0Token: се_справи, S0B1Token: се_с, S0Token: се, S0_LastThreeLetters: �е, S0_LastTwoLetters: е, TransHistory1: 2, TransHistory2: 20, 

24- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [се, справи]   B= [с, проблема, . ,.. ]

B0Token: с, B0_LastThreeLetters: с, B0_LastTwoLetters: с, S0B0Distance: 1, S0B0Token: справи_с, S0B1Token: справи_проблема, S0Token: справи, S0_LastThreeLetters: �и, S0_LastTwoLetters: и, S1B0Token: се_с, S1S0B0Token: се_справи_с, S1S0Token: се_справи, S1Token: се, S1_LastThreeLetters: �е, S1_LastTwoLetters: е, TransHistory1: 0, TransHistory2: 02, 

25- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[се, справи]]   B= [с, проблема, . ,.. ]

B0Token: с, B0_LastThreeLetters: с, B0_LastTwoLetters: с, S0B0Distance: 1, S0B0Token: се_справи_с, S0B1Token: се_справи_проблема, S0Token: се_справи, S0_LastThreeLetters: �и, S0_LastTwoLetters: и, TransHistory1: 0, TransHistory2: 00, 

26- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [с, проблема, . ,.. ]

B0Token: с, B0_LastThreeLetters: с, B0_LastTwoLetters: с, TransHistory1: 1, TransHistory2: 10, 

27- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [с]   B= [проблема, . ,.. ]

B0Token: проблема, B0_LastThreeLetters: �а, B0_LastTwoLetters: а, S0B0Distance: 1, S0B0Token: с_проблема, S0B1Token: с_., S0Token: с, S0_LastThreeLetters: с, S0_LastTwoLetters: с, TransHistory1: 2, TransHistory2: 21, 

28- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [проблема, . ,.. ]

B0Token: проблема, B0_LastThreeLetters: �а, B0_LastTwoLetters: а, TransHistory1: 0, TransHistory2: 02, 

29- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [проблема]   B= [.]

B0Token: ., B0_LastThreeLetters: ., B0_LastTwoLetters: ., S0B0Distance: 1, S0B0Token: проблема_., S0Token: проблема, S0_LastThreeLetters: �а, S0_LastTwoLetters: а, TransHistory1: 2, TransHistory2: 20, 

30- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [.]

B0Token: ., B0_LastThreeLetters: ., B0_LastTwoLetters: ., TransHistory1: 0, TransHistory2: 02, 

31- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [ ]

S0Token: ., S0_LastThreeLetters: ., S0_LastTwoLetters: ., TransHistory1: 2, TransHistory2: 20, 

32- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

## Sentence No. 2518 - 
Междувременно , говорителят на гръцкото правителство Христос Протопапас заяви в четвъртък , че ако Турция иска да се присъедини към съюза , трябва да започне да работи за уреждането на кипърския въпрос и да се примири с факта , че гръцката част на острова вече е подписала договора за присъединяване .
### Existing MWEs: 
1- **се присъедини** (IReflV)
2- **се примири** (IReflV)
3- **подписала договора** (LVC)
### Identified MWEs: 
1- **се присъедини** 

2- **се примири** 

3- **подписала договора** 




0- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Междувременно, ,, говорителят ,.. ]

B0Token: Междувременно, B0_LastThreeLetters: �о, B0_LastTwoLetters: о, 

1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Междувременно]   B= [,, говорителят, на ,.. ]

B0Token: ,, B0_LastThreeLetters: ,, B0_LastTwoLetters: ,, S0B0Distance: 1, S0B0Token: Междувременно_,, S0B1Token: Междувременно_говорителят, S0Token: Междувременно, S0_LastThreeLetters: �о, S0_LastTwoLetters: о, TransHistory1: 0, 

2- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, говорителят, на ,.. ]

B0Token: ,, B0_LastThreeLetters: ,, B0_LastTwoLetters: ,, TransHistory1: 0, TransHistory2: 00, 

3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [говорителят, на, гръцкото ,.. ]

B0Token: говорителят, B0_LastThreeLetters: �т, B0_LastTwoLetters: т, S0B0Distance: 1, S0B0Token: ,_говорителят, S0B1Token: ,_на, S0Token: ,, S0_LastThreeLetters: ,, S0_LastTwoLetters: ,, TransHistory1: 2, TransHistory2: 20, 

4- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [говорителят, на, гръцкото ,.. ]

B0Token: говорителят, B0_LastThreeLetters: �т, B0_LastTwoLetters: т, TransHistory1: 0, TransHistory2: 02, 

5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [говорителят]   B= [на, гръцкото, правителство ,.. ]

B0Token: на, B0_LastThreeLetters: �а, B0_LastTwoLetters: а, S0B0Distance: 1, S0B0Token: говорителят_на, S0B1Token: говорителят_гръцкото, S0Token: говорителят, S0_LastThreeLetters: �т, S0_LastTwoLetters: т, TransHistory1: 2, TransHistory2: 20, 

6- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [на, гръцкото, правителство ,.. ]

B0Token: на, B0_LastThreeLetters: �а, B0_LastTwoLetters: а, TransHistory1: 0, TransHistory2: 02, 

7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [на]   B= [гръцкото, правителство, Христос ,.. ]

B0Token: гръцкото, B0_LastThreeLetters: �о, B0_LastTwoLetters: о, S0B0Distance: 1, S0B0Token: на_гръцкото, S0B1Token: на_правителство, S0Token: на, S0_LastThreeLetters: �а, S0_LastTwoLetters: а, TransHistory1: 2, TransHistory2: 20, 

8- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [гръцкото, правителство, Христос ,.. ]

B0Token: гръцкото, B0_LastThreeLetters: �о, B0_LastTwoLetters: о, TransHistory1: 0, TransHistory2: 02, 

9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [гръцкото]   B= [правителство, Христос, Протопапас ,.. ]

B0Token: правителство, B0_LastThreeLetters: �о, B0_LastTwoLetters: о, S0B0Distance: 1, S0B0Token: гръцкото_правителство, S0B1Token: гръцкото_Христос, S0Token: гръцкото, S0_LastThreeLetters: �о, S0_LastTwoLetters: о, TransHistory1: 2, TransHistory2: 20, 

10- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [правителство, Христос, Протопапас ,.. ]

B0Token: правителство, B0_LastThreeLetters: �о, B0_LastTwoLetters: о, TransHistory1: 0, TransHistory2: 02, 

11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [правителство]   B= [Христос, Протопапас, заяви ,.. ]

B0Token: Христос, B0_LastThreeLetters: �с, B0_LastTwoLetters: с, S0B0Distance: 1, S0B0Token: правителство_Христос, S0B1Token: правителство_Протопапас, S0Token: правителство, S0_LastThreeLetters: �о, S0_LastTwoLetters: о, TransHistory1: 2, TransHistory2: 20, 

12- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Христос, Протопапас, заяви ,.. ]

B0Token: Христос, B0_LastThreeLetters: �с, B0_LastTwoLetters: с, TransHistory1: 0, TransHistory2: 02, 

13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Христос]   B= [Протопапас, заяви, в ,.. ]

B0Token: Протопапас, B0_LastThreeLetters: �с, B0_LastTwoLetters: с, S0B0Distance: 1, S0B0Token: Христос_Протопапас, S0B1Token: Христос_заяви, S0Token: Христос, S0_LastThreeLetters: �с, S0_LastTwoLetters: с, TransHistory1: 2, TransHistory2: 20, 

14- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Протопапас, заяви, в ,.. ]

B0Token: Протопапас, B0_LastThreeLetters: �с, B0_LastTwoLetters: с, TransHistory1: 0, TransHistory2: 02, 

15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Протопапас]   B= [заяви, в, четвъртък ,.. ]

B0Token: заяви, B0_LastThreeLetters: �и, B0_LastTwoLetters: и, S0B0Distance: 1, S0B0Token: Протопапас_заяви, S0B1Token: Протопапас_в, S0Token: Протопапас, S0_LastThreeLetters: �с, S0_LastTwoLetters: с, TransHistory1: 2, TransHistory2: 20, 

16- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [заяви, в, четвъртък ,.. ]

B0Token: заяви, B0_LastThreeLetters: �и, B0_LastTwoLetters: и, TransHistory1: 0, TransHistory2: 02, 

17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [заяви]   B= [в, четвъртък, , ,.. ]

B0Token: в, B0_LastThreeLetters: в, B0_LastTwoLetters: в, S0B0Distance: 1, S0B0Token: заяви_в, S0B1Token: заяви_четвъртък, S0Token: заяви, S0_LastThreeLetters: �и, S0_LastTwoLetters: и, TransHistory1: 2, TransHistory2: 20, 

18- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [в, четвъртък, , ,.. ]

B0Token: в, B0_LastThreeLetters: в, B0_LastTwoLetters: в, TransHistory1: 0, TransHistory2: 02, 

19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [в]   B= [четвъртък, ,, че ,.. ]

B0Token: четвъртък, B0_LastThreeLetters: �к, B0_LastTwoLetters: к, S0B0Distance: 1, S0B0Token: в_четвъртък, S0B1Token: в_,, S0Token: в, S0_LastThreeLetters: в, S0_LastTwoLetters: в, TransHistory1: 2, TransHistory2: 20, 

20- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [четвъртък, ,, че ,.. ]

B0Token: четвъртък, B0_LastThreeLetters: �к, B0_LastTwoLetters: к, TransHistory1: 0, TransHistory2: 02, 

21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [четвъртък]   B= [,, че, ако ,.. ]

B0Token: ,, B0_LastThreeLetters: ,, B0_LastTwoLetters: ,, S0B0Distance: 1, S0B0Token: четвъртък_,, S0B1Token: четвъртък_че, S0Token: четвъртък, S0_LastThreeLetters: �к, S0_LastTwoLetters: к, TransHistory1: 2, TransHistory2: 20, 

22- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, че, ако ,.. ]

B0Token: ,, B0_LastThreeLetters: ,, B0_LastTwoLetters: ,, TransHistory1: 0, TransHistory2: 02, 

23- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [че, ако, Турция ,.. ]

B0Token: че, B0_LastThreeLetters: �е, B0_LastTwoLetters: е, S0B0Distance: 1, S0B0Token: ,_че, S0B1Token: ,_ако, S0Token: ,, S0_LastThreeLetters: ,, S0_LastTwoLetters: ,, TransHistory1: 2, TransHistory2: 20, 

24- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [че, ако, Турция ,.. ]

B0Token: че, B0_LastThreeLetters: �е, B0_LastTwoLetters: е, TransHistory1: 0, TransHistory2: 02, 

25- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [че]   B= [ако, Турция, иска ,.. ]

B0Token: ако, B0_LastThreeLetters: �о, B0_LastTwoLetters: о, S0B0Distance: 1, S0B0Token: че_ако, S0B1Token: че_Турция, S0Token: че, S0_LastThreeLetters: �е, S0_LastTwoLetters: е, TransHistory1: 2, TransHistory2: 20, 

26- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ако, Турция, иска ,.. ]

B0Token: ако, B0_LastThreeLetters: �о, B0_LastTwoLetters: о, TransHistory1: 0, TransHistory2: 02, 

27- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ако]   B= [Турция, иска, да ,.. ]

B0Token: Турция, B0_LastThreeLetters: �я, B0_LastTwoLetters: я, S0B0Distance: 1, S0B0Token: ако_Турция, S0B1Token: ако_иска, S0Token: ако, S0_LastThreeLetters: �о, S0_LastTwoLetters: о, TransHistory1: 2, TransHistory2: 20, 

28- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Турция, иска, да ,.. ]

B0Token: Турция, B0_LastThreeLetters: �я, B0_LastTwoLetters: я, TransHistory1: 0, TransHistory2: 02, 

29- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Турция]   B= [иска, да, се ,.. ]

B0Token: иска, B0_LastThreeLetters: �а, B0_LastTwoLetters: а, S0B0Distance: 1, S0B0Token: Турция_иска, S0B1Token: Турция_да, S0Token: Турция, S0_LastThreeLetters: �я, S0_LastTwoLetters: я, TransHistory1: 2, TransHistory2: 20, 

30- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [иска, да, се ,.. ]

B0Token: иска, B0_LastThreeLetters: �а, B0_LastTwoLetters: а, TransHistory1: 0, TransHistory2: 02, 

31- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [иска]   B= [да, се, присъедини ,.. ]

B0Token: да, B0_LastThreeLetters: �а, B0_LastTwoLetters: а, S0B0Distance: 1, S0B0Token: иска_да, S0B1Token: иска_се, S0Token: иска, S0_LastThreeLetters: �а, S0_LastTwoLetters: а, TransHistory1: 2, TransHistory2: 20, 

32- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [да, се, присъедини ,.. ]

B0Token: да, B0_LastThreeLetters: �а, B0_LastTwoLetters: а, TransHistory1: 0, TransHistory2: 02, 

33- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [да]   B= [се, присъедини, към ,.. ]

B0Token: се, B0_LastThreeLetters: �е, B0_LastTwoLetters: е, S0B0Distance: 1, S0B0Token: да_се, S0B1Token: да_присъедини, S0Token: да, S0_LastThreeLetters: �а, S0_LastTwoLetters: а, TransHistory1: 2, TransHistory2: 20, 

34- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [се, присъедини, към ,.. ]

B0Token: се, B0_LastThreeLetters: �е, B0_LastTwoLetters: е, TransHistory1: 0, TransHistory2: 02, 

35- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [се]   B= [присъедини, към, съюза ,.. ]

B0Token: присъедини, B0_LastThreeLetters: �и, B0_LastTwoLetters: и, S0B0Distance: 1, S0B0Token: се_присъедини, S0B1Token: се_към, S0Token: се, S0_LastThreeLetters: �е, S0_LastTwoLetters: е, TransHistory1: 2, TransHistory2: 20, 

36- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [се, присъедини]   B= [към, съюза, , ,.. ]

B0Token: към, B0_LastThreeLetters: �м, B0_LastTwoLetters: м, S0B0Distance: 1, S0B0Token: присъедини_към, S0B1Token: присъедини_съюза, S0Token: присъедини, S0_LastThreeLetters: �и, S0_LastTwoLetters: и, S1B0Token: се_към, S1S0B0Token: се_присъедини_към, S1S0Token: се_присъедини, S1Token: се, S1_LastThreeLetters: �е, S1_LastTwoLetters: е, TransHistory1: 0, TransHistory2: 02, 

37- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[се, присъедини]]   B= [към, съюза, , ,.. ]

B0Token: към, B0_LastThreeLetters: �м, B0_LastTwoLetters: м, S0B0Distance: 1, S0B0Token: се_присъедини_към, S0B1Token: се_присъедини_съюза, S0Token: се_присъедини, S0_LastThreeLetters: �и, S0_LastTwoLetters: и, TransHistory1: 0, TransHistory2: 00, 

38- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [към, съюза, , ,.. ]

B0Token: към, B0_LastThreeLetters: �м, B0_LastTwoLetters: м, TransHistory1: 1, TransHistory2: 10, 

39- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [към]   B= [съюза, ,, трябва ,.. ]

B0Token: съюза, B0_LastThreeLetters: �а, B0_LastTwoLetters: а, S0B0Distance: 1, S0B0Token: към_съюза, S0B1Token: към_,, S0Token: към, S0_LastThreeLetters: �м, S0_LastTwoLetters: м, TransHistory1: 2, TransHistory2: 21, 

40- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [съюза, ,, трябва ,.. ]

B0Token: съюза, B0_LastThreeLetters: �а, B0_LastTwoLetters: а, TransHistory1: 0, TransHistory2: 02, 

41- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [съюза]   B= [,, трябва, да ,.. ]

B0Token: ,, B0_LastThreeLetters: ,, B0_LastTwoLetters: ,, S0B0Distance: 1, S0B0Token: съюза_,, S0B1Token: съюза_трябва, S0Token: съюза, S0_LastThreeLetters: �а, S0_LastTwoLetters: а, TransHistory1: 2, TransHistory2: 20, 

42- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, трябва, да ,.. ]

B0Token: ,, B0_LastThreeLetters: ,, B0_LastTwoLetters: ,, TransHistory1: 0, TransHistory2: 02, 

43- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [трябва, да, започне ,.. ]

B0Token: трябва, B0_LastThreeLetters: �а, B0_LastTwoLetters: а, S0B0Distance: 1, S0B0Token: ,_трябва, S0B1Token: ,_да, S0Token: ,, S0_LastThreeLetters: ,, S0_LastTwoLetters: ,, TransHistory1: 2, TransHistory2: 20, 

44- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [трябва, да, започне ,.. ]

B0Token: трябва, B0_LastThreeLetters: �а, B0_LastTwoLetters: а, TransHistory1: 0, TransHistory2: 02, 

45- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [трябва]   B= [да, започне, да ,.. ]

B0Token: да, B0_LastThreeLetters: �а, B0_LastTwoLetters: а, S0B0Distance: 1, S0B0Token: трябва_да, S0B1Token: трябва_започне, S0Token: трябва, S0_LastThreeLetters: �а, S0_LastTwoLetters: а, TransHistory1: 2, TransHistory2: 20, 

46- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [да, започне, да ,.. ]

B0Token: да, B0_LastThreeLetters: �а, B0_LastTwoLetters: а, TransHistory1: 0, TransHistory2: 02, 

47- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [да]   B= [започне, да, работи ,.. ]

B0Token: започне, B0_LastThreeLetters: �е, B0_LastTwoLetters: е, S0B0Distance: 1, S0B0Token: да_започне, S0B1Token: да_да, S0Token: да, S0_LastThreeLetters: �а, S0_LastTwoLetters: а, TransHistory1: 2, TransHistory2: 20, 

48- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [започне, да, работи ,.. ]

B0Token: започне, B0_LastThreeLetters: �е, B0_LastTwoLetters: е, TransHistory1: 0, TransHistory2: 02, 

49- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [започне]   B= [да, работи, за ,.. ]

B0Token: да, B0_LastThreeLetters: �а, B0_LastTwoLetters: а, S0B0Distance: 1, S0B0Token: започне_да, S0B1Token: започне_работи, S0Token: започне, S0_LastThreeLetters: �е, S0_LastTwoLetters: е, TransHistory1: 2, TransHistory2: 20, 

50- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [да, работи, за ,.. ]

B0Token: да, B0_LastThreeLetters: �а, B0_LastTwoLetters: а, TransHistory1: 0, TransHistory2: 02, 

51- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [да]   B= [работи, за, уреждането ,.. ]

B0Token: работи, B0_LastThreeLetters: �и, B0_LastTwoLetters: и, S0B0Distance: 1, S0B0Token: да_работи, S0B1Token: да_за, S0Token: да, S0_LastThreeLetters: �а, S0_LastTwoLetters: а, TransHistory1: 2, TransHistory2: 20, 

52- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [работи, за, уреждането ,.. ]

B0Token: работи, B0_LastThreeLetters: �и, B0_LastTwoLetters: и, TransHistory1: 0, TransHistory2: 02, 

53- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [работи]   B= [за, уреждането, на ,.. ]

B0Token: за, B0_LastThreeLetters: �а, B0_LastTwoLetters: а, S0B0Distance: 1, S0B0Token: работи_за, S0B1Token: работи_уреждането, S0Token: работи, S0_LastThreeLetters: �и, S0_LastTwoLetters: и, TransHistory1: 2, TransHistory2: 20, 

54- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [за, уреждането, на ,.. ]

B0Token: за, B0_LastThreeLetters: �а, B0_LastTwoLetters: а, TransHistory1: 0, TransHistory2: 02, 

55- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [за]   B= [уреждането, на, кипърския ,.. ]

B0Token: уреждането, B0_LastThreeLetters: �о, B0_LastTwoLetters: о, S0B0Distance: 1, S0B0Token: за_уреждането, S0B1Token: за_на, S0Token: за, S0_LastThreeLetters: �а, S0_LastTwoLetters: а, TransHistory1: 2, TransHistory2: 20, 

56- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [уреждането, на, кипърския ,.. ]

B0Token: уреждането, B0_LastThreeLetters: �о, B0_LastTwoLetters: о, TransHistory1: 0, TransHistory2: 02, 

57- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [уреждането]   B= [на, кипърския, въпрос ,.. ]

B0Token: на, B0_LastThreeLetters: �а, B0_LastTwoLetters: а, S0B0Distance: 1, S0B0Token: уреждането_на, S0B1Token: уреждането_кипърския, S0Token: уреждането, S0_LastThreeLetters: �о, S0_LastTwoLetters: о, TransHistory1: 2, TransHistory2: 20, 

58- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [на, кипърския, въпрос ,.. ]

B0Token: на, B0_LastThreeLetters: �а, B0_LastTwoLetters: а, TransHistory1: 0, TransHistory2: 02, 

59- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [на]   B= [кипърския, въпрос, и ,.. ]

B0Token: кипърския, B0_LastThreeLetters: �я, B0_LastTwoLetters: я, S0B0Distance: 1, S0B0Token: на_кипърския, S0B1Token: на_въпрос, S0Token: на, S0_LastThreeLetters: �а, S0_LastTwoLetters: а, TransHistory1: 2, TransHistory2: 20, 

60- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [кипърския, въпрос, и ,.. ]

B0Token: кипърския, B0_LastThreeLetters: �я, B0_LastTwoLetters: я, TransHistory1: 0, TransHistory2: 02, 

61- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [кипърския]   B= [въпрос, и, да ,.. ]

B0Token: въпрос, B0_LastThreeLetters: �с, B0_LastTwoLetters: с, S0B0Distance: 1, S0B0Token: кипърския_въпрос, S0B1Token: кипърския_и, S0Token: кипърския, S0_LastThreeLetters: �я, S0_LastTwoLetters: я, TransHistory1: 2, TransHistory2: 20, 

62- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [въпрос, и, да ,.. ]

B0Token: въпрос, B0_LastThreeLetters: �с, B0_LastTwoLetters: с, TransHistory1: 0, TransHistory2: 02, 

63- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [въпрос]   B= [и, да, се ,.. ]

B0Token: и, B0_LastThreeLetters: и, B0_LastTwoLetters: и, S0B0Distance: 1, S0B0Token: въпрос_и, S0B1Token: въпрос_да, S0Token: въпрос, S0_LastThreeLetters: �с, S0_LastTwoLetters: с, TransHistory1: 2, TransHistory2: 20, 

64- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [и, да, се ,.. ]

B0Token: и, B0_LastThreeLetters: и, B0_LastTwoLetters: и, TransHistory1: 0, TransHistory2: 02, 

65- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [и]   B= [да, се, примири ,.. ]

B0Token: да, B0_LastThreeLetters: �а, B0_LastTwoLetters: а, S0B0Distance: 1, S0B0Token: и_да, S0B1Token: и_се, S0Token: и, S0_LastThreeLetters: и, S0_LastTwoLetters: и, TransHistory1: 2, TransHistory2: 20, 

66- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [да, се, примири ,.. ]

B0Token: да, B0_LastThreeLetters: �а, B0_LastTwoLetters: а, TransHistory1: 0, TransHistory2: 02, 

67- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [да]   B= [се, примири, с ,.. ]

B0Token: се, B0_LastThreeLetters: �е, B0_LastTwoLetters: е, S0B0Distance: 1, S0B0Token: да_се, S0B1Token: да_примири, S0Token: да, S0_LastThreeLetters: �а, S0_LastTwoLetters: а, TransHistory1: 2, TransHistory2: 20, 

68- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [се, примири, с ,.. ]

B0Token: се, B0_LastThreeLetters: �е, B0_LastTwoLetters: е, TransHistory1: 0, TransHistory2: 02, 

69- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [се]   B= [примири, с, факта ,.. ]

B0Token: примири, B0_LastThreeLetters: �и, B0_LastTwoLetters: и, S0B0Distance: 1, S0B0Token: се_примири, S0B1Token: се_с, S0Token: се, S0_LastThreeLetters: �е, S0_LastTwoLetters: е, TransHistory1: 2, TransHistory2: 20, 

70- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [се, примири]   B= [с, факта, , ,.. ]

B0Token: с, B0_LastThreeLetters: с, B0_LastTwoLetters: с, S0B0Distance: 1, S0B0Token: примири_с, S0B1Token: примири_факта, S0Token: примири, S0_LastThreeLetters: �и, S0_LastTwoLetters: и, S1B0Token: се_с, S1S0B0Token: се_примири_с, S1S0Token: се_примири, S1Token: се, S1_LastThreeLetters: �е, S1_LastTwoLetters: е, TransHistory1: 0, TransHistory2: 02, 

71- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[се, примири]]   B= [с, факта, , ,.. ]

B0Token: с, B0_LastThreeLetters: с, B0_LastTwoLetters: с, S0B0Distance: 1, S0B0Token: се_примири_с, S0B1Token: се_примири_факта, S0Token: се_примири, S0_LastThreeLetters: �и, S0_LastTwoLetters: и, TransHistory1: 0, TransHistory2: 00, 

72- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [с, факта, , ,.. ]

B0Token: с, B0_LastThreeLetters: с, B0_LastTwoLetters: с, TransHistory1: 1, TransHistory2: 10, 

73- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [с]   B= [факта, ,, че ,.. ]

B0Token: факта, B0_LastThreeLetters: �а, B0_LastTwoLetters: а, S0B0Distance: 1, S0B0Token: с_факта, S0B1Token: с_,, S0Token: с, S0_LastThreeLetters: с, S0_LastTwoLetters: с, TransHistory1: 2, TransHistory2: 21, 

74- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [факта, ,, че ,.. ]

B0Token: факта, B0_LastThreeLetters: �а, B0_LastTwoLetters: а, TransHistory1: 0, TransHistory2: 02, 

75- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [факта]   B= [,, че, гръцката ,.. ]

B0Token: ,, B0_LastThreeLetters: ,, B0_LastTwoLetters: ,, S0B0Distance: 1, S0B0Token: факта_,, S0B1Token: факта_че, S0Token: факта, S0_LastThreeLetters: �а, S0_LastTwoLetters: а, TransHistory1: 2, TransHistory2: 20, 

76- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, че, гръцката ,.. ]

B0Token: ,, B0_LastThreeLetters: ,, B0_LastTwoLetters: ,, TransHistory1: 0, TransHistory2: 02, 

77- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [че, гръцката, част ,.. ]

B0Token: че, B0_LastThreeLetters: �е, B0_LastTwoLetters: е, S0B0Distance: 1, S0B0Token: ,_че, S0B1Token: ,_гръцката, S0Token: ,, S0_LastThreeLetters: ,, S0_LastTwoLetters: ,, TransHistory1: 2, TransHistory2: 20, 

78- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [че, гръцката, част ,.. ]

B0Token: че, B0_LastThreeLetters: �е, B0_LastTwoLetters: е, TransHistory1: 0, TransHistory2: 02, 

79- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [че]   B= [гръцката, част, на ,.. ]

B0Token: гръцката, B0_LastThreeLetters: �а, B0_LastTwoLetters: а, S0B0Distance: 1, S0B0Token: че_гръцката, S0B1Token: че_част, S0Token: че, S0_LastThreeLetters: �е, S0_LastTwoLetters: е, TransHistory1: 2, TransHistory2: 20, 

80- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [гръцката, част, на ,.. ]

B0Token: гръцката, B0_LastThreeLetters: �а, B0_LastTwoLetters: а, TransHistory1: 0, TransHistory2: 02, 

81- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [гръцката]   B= [част, на, острова ,.. ]

B0Token: част, B0_LastThreeLetters: �т, B0_LastTwoLetters: т, S0B0Distance: 1, S0B0Token: гръцката_част, S0B1Token: гръцката_на, S0Token: гръцката, S0_LastThreeLetters: �а, S0_LastTwoLetters: а, TransHistory1: 2, TransHistory2: 20, 

82- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [част, на, острова ,.. ]

B0Token: част, B0_LastThreeLetters: �т, B0_LastTwoLetters: т, TransHistory1: 0, TransHistory2: 02, 

83- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [част]   B= [на, острова, вече ,.. ]

B0Token: на, B0_LastThreeLetters: �а, B0_LastTwoLetters: а, S0B0Distance: 1, S0B0Token: част_на, S0B1Token: част_острова, S0Token: част, S0_LastThreeLetters: �т, S0_LastTwoLetters: т, TransHistory1: 2, TransHistory2: 20, 

84- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [на, острова, вече ,.. ]

B0Token: на, B0_LastThreeLetters: �а, B0_LastTwoLetters: а, TransHistory1: 0, TransHistory2: 02, 

85- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [на]   B= [острова, вече, е ,.. ]

B0Token: острова, B0_LastThreeLetters: �а, B0_LastTwoLetters: а, S0B0Distance: 1, S0B0Token: на_острова, S0B1Token: на_вече, S0Token: на, S0_LastThreeLetters: �а, S0_LastTwoLetters: а, TransHistory1: 2, TransHistory2: 20, 

86- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [острова, вече, е ,.. ]

B0Token: острова, B0_LastThreeLetters: �а, B0_LastTwoLetters: а, TransHistory1: 0, TransHistory2: 02, 

87- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [острова]   B= [вече, е, подписала ,.. ]

B0Token: вече, B0_LastThreeLetters: �е, B0_LastTwoLetters: е, S0B0Distance: 1, S0B0Token: острова_вече, S0B1Token: острова_е, S0Token: острова, S0_LastThreeLetters: �а, S0_LastTwoLetters: а, TransHistory1: 2, TransHistory2: 20, 

88- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [вече, е, подписала ,.. ]

B0Token: вече, B0_LastThreeLetters: �е, B0_LastTwoLetters: е, TransHistory1: 0, TransHistory2: 02, 

89- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [вече]   B= [е, подписала, договора ,.. ]

B0Token: е, B0_LastThreeLetters: е, B0_LastTwoLetters: е, S0B0Distance: 1, S0B0Token: вече_е, S0B1Token: вече_подписала, S0Token: вече, S0_LastThreeLetters: �е, S0_LastTwoLetters: е, TransHistory1: 2, TransHistory2: 20, 

90- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [е, подписала, договора ,.. ]

B0Token: е, B0_LastThreeLetters: е, B0_LastTwoLetters: е, TransHistory1: 0, TransHistory2: 02, 

91- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [е]   B= [подписала, договора, за ,.. ]

B0Token: подписала, B0_LastThreeLetters: �а, B0_LastTwoLetters: а, S0B0Distance: 1, S0B0Token: е_подписала, S0B1Token: е_договора, S0Token: е, S0_LastThreeLetters: е, S0_LastTwoLetters: е, TransHistory1: 2, TransHistory2: 20, 

92- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [подписала, договора, за ,.. ]

B0Token: подписала, B0_LastThreeLetters: �а, B0_LastTwoLetters: а, TransHistory1: 0, TransHistory2: 02, 

93- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [подписала]   B= [договора, за, присъединяване ,.. ]

B0Token: договора, B0_LastThreeLetters: �а, B0_LastTwoLetters: а, S0B0Distance: 1, S0B0Token: подписала_договора, S0B1Token: подписала_за, S0Token: подписала, S0_LastThreeLetters: �а, S0_LastTwoLetters: а, TransHistory1: 2, TransHistory2: 20, 

94- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [подписала, договора]   B= [за, присъединяване, . ,.. ]

B0Token: за, B0_LastThreeLetters: �а, B0_LastTwoLetters: а, S0B0Distance: 1, S0B0Token: договора_за, S0B1Token: договора_присъединяване, S0Token: договора, S0_LastThreeLetters: �а, S0_LastTwoLetters: а, S1B0Token: подписала_за, S1S0B0Token: подписала_договора_за, S1S0Token: подписала_договора, S1Token: подписала, S1_LastThreeLetters: �а, S1_LastTwoLetters: а, TransHistory1: 0, TransHistory2: 02, 

95- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[подписала, договора]]   B= [за, присъединяване, . ,.. ]

B0Token: за, B0_LastThreeLetters: �а, B0_LastTwoLetters: а, S0B0Distance: 1, S0B0Token: подписала_договора_за, S0B1Token: подписала_договора_присъединяване, S0Token: подписала_договора, S0_LastThreeLetters: �а, S0_LastTwoLetters: а, TransHistory1: 0, TransHistory2: 00, 

96- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [за, присъединяване, . ,.. ]

B0Token: за, B0_LastThreeLetters: �а, B0_LastTwoLetters: а, TransHistory1: 1, TransHistory2: 10, 

97- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [за]   B= [присъединяване, . ,.. ]

B0Token: присъединяване, B0_LastThreeLetters: �е, B0_LastTwoLetters: е, S0B0Distance: 1, S0B0Token: за_присъединяване, S0B1Token: за_., S0Token: за, S0_LastThreeLetters: �а, S0_LastTwoLetters: а, TransHistory1: 2, TransHistory2: 21, 

98- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [присъединяване, . ,.. ]

B0Token: присъединяване, B0_LastThreeLetters: �е, B0_LastTwoLetters: е, TransHistory1: 0, TransHistory2: 02, 

99- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [присъединяване]   B= [.]

B0Token: ., B0_LastThreeLetters: ., B0_LastTwoLetters: ., S0B0Distance: 1, S0B0Token: присъединяване_., S0Token: присъединяване, S0_LastThreeLetters: �е, S0_LastTwoLetters: е, TransHistory1: 2, TransHistory2: 20, 

100- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [.]

B0Token: ., B0_LastThreeLetters: ., B0_LastTwoLetters: ., TransHistory1: 0, TransHistory2: 02, 

101- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [ ]

S0Token: ., S0_LastThreeLetters: ., S0_LastTwoLetters: ., TransHistory1: 2, TransHistory2: 20, 

102- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

## Sentence No. 2648 - 
Те постигнаха съгласие , че представителите на областните правителства ще се срещнат в рамките на 15 дни , за да се договорят по останалите проектоизменения , препоръчани от Комитета &quot; Булдозер &quot; към Службата на Върховния представител .
### Existing MWEs: 
1- **постигнаха съгласие** (LVC)
2- **ще се срещнат** (IReflV)
3- **се договорят** (IReflV)
### Identified MWEs: 
1- **постигнаха съгласие** 

2- **ще се срещнат** 

3- **се договорят** 




0- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Те, постигнаха, съгласие ,.. ]

B0Token: Те, B0_LastThreeLetters: �е, B0_LastTwoLetters: е, 

1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Те]   B= [постигнаха, съгласие, , ,.. ]

B0Token: постигнаха, B0_LastThreeLetters: �а, B0_LastTwoLetters: а, S0B0Distance: 1, S0B0Token: Те_постигнаха, S0B1Token: Те_съгласие, S0Token: Те, S0_LastThreeLetters: �е, S0_LastTwoLetters: е, TransHistory1: 0, 

2- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [постигнаха, съгласие, , ,.. ]

B0Token: постигнаха, B0_LastThreeLetters: �а, B0_LastTwoLetters: а, TransHistory1: 0, TransHistory2: 00, 

3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [постигнаха]   B= [съгласие, ,, че ,.. ]

B0Token: съгласие, B0_LastThreeLetters: �е, B0_LastTwoLetters: е, S0B0Distance: 1, S0B0Token: постигнаха_съгласие, S0B1Token: постигнаха_,, S0Token: постигнаха, S0_LastThreeLetters: �а, S0_LastTwoLetters: а, TransHistory1: 2, TransHistory2: 20, 

4- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [постигнаха, съгласие]   B= [,, че, представителите ,.. ]

B0Token: ,, B0_LastThreeLetters: ,, B0_LastTwoLetters: ,, S0B0Distance: 1, S0B0Token: съгласие_,, S0B1Token: съгласие_че, S0Token: съгласие, S0_LastThreeLetters: �е, S0_LastTwoLetters: е, S1B0Token: постигнаха_,, S1S0B0Token: постигнаха_съгласие_,, S1S0Token: постигнаха_съгласие, S1Token: постигнаха, S1_LastThreeLetters: �а, S1_LastTwoLetters: а, TransHistory1: 0, TransHistory2: 02, 

5- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[постигнаха, съгласие]]   B= [,, че, представителите ,.. ]

B0Token: ,, B0_LastThreeLetters: ,, B0_LastTwoLetters: ,, S0B0Distance: 1, S0B0Token: постигнаха_съгласие_,, S0B1Token: постигнаха_съгласие_че, S0Token: постигнаха_съгласие, S0_LastThreeLetters: �е, S0_LastTwoLetters: е, TransHistory1: 0, TransHistory2: 00, 

6- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, че, представителите ,.. ]

B0Token: ,, B0_LastThreeLetters: ,, B0_LastTwoLetters: ,, TransHistory1: 1, TransHistory2: 10, 

7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [че, представителите, на ,.. ]

B0Token: че, B0_LastThreeLetters: �е, B0_LastTwoLetters: е, S0B0Distance: 1, S0B0Token: ,_че, S0B1Token: ,_представителите, S0Token: ,, S0_LastThreeLetters: ,, S0_LastTwoLetters: ,, TransHistory1: 2, TransHistory2: 21, 

8- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [че, представителите, на ,.. ]

B0Token: че, B0_LastThreeLetters: �е, B0_LastTwoLetters: е, TransHistory1: 0, TransHistory2: 02, 

9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [че]   B= [представителите, на, областните ,.. ]

B0Token: представителите, B0_LastThreeLetters: �е, B0_LastTwoLetters: е, S0B0Distance: 1, S0B0Token: че_представителите, S0B1Token: че_на, S0Token: че, S0_LastThreeLetters: �е, S0_LastTwoLetters: е, TransHistory1: 2, TransHistory2: 20, 

10- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [представителите, на, областните ,.. ]

B0Token: представителите, B0_LastThreeLetters: �е, B0_LastTwoLetters: е, TransHistory1: 0, TransHistory2: 02, 

11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [представителите]   B= [на, областните, правителства ,.. ]

B0Token: на, B0_LastThreeLetters: �а, B0_LastTwoLetters: а, S0B0Distance: 1, S0B0Token: представителите_на, S0B1Token: представителите_областните, S0Token: представителите, S0_LastThreeLetters: �е, S0_LastTwoLetters: е, TransHistory1: 2, TransHistory2: 20, 

12- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [на, областните, правителства ,.. ]

B0Token: на, B0_LastThreeLetters: �а, B0_LastTwoLetters: а, TransHistory1: 0, TransHistory2: 02, 

13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [на]   B= [областните, правителства, ще ,.. ]

B0Token: областните, B0_LastThreeLetters: �е, B0_LastTwoLetters: е, S0B0Distance: 1, S0B0Token: на_областните, S0B1Token: на_правителства, S0Token: на, S0_LastThreeLetters: �а, S0_LastTwoLetters: а, TransHistory1: 2, TransHistory2: 20, 

14- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [областните, правителства, ще ,.. ]

B0Token: областните, B0_LastThreeLetters: �е, B0_LastTwoLetters: е, TransHistory1: 0, TransHistory2: 02, 

15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [областните]   B= [правителства, ще, се ,.. ]

B0Token: правителства, B0_LastThreeLetters: �а, B0_LastTwoLetters: а, S0B0Distance: 1, S0B0Token: областните_правителства, S0B1Token: областните_ще, S0Token: областните, S0_LastThreeLetters: �е, S0_LastTwoLetters: е, TransHistory1: 2, TransHistory2: 20, 

16- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [правителства, ще, се ,.. ]

B0Token: правителства, B0_LastThreeLetters: �а, B0_LastTwoLetters: а, TransHistory1: 0, TransHistory2: 02, 

17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [правителства]   B= [ще, се, срещнат ,.. ]

B0Token: ще, B0_LastThreeLetters: �е, B0_LastTwoLetters: е, S0B0Distance: 1, S0B0Token: правителства_ще, S0B1Token: правителства_се, S0Token: правителства, S0_LastThreeLetters: �а, S0_LastTwoLetters: а, TransHistory1: 2, TransHistory2: 20, 

18- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ще, се, срещнат ,.. ]

B0Token: ще, B0_LastThreeLetters: �е, B0_LastTwoLetters: е, TransHistory1: 0, TransHistory2: 02, 

19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ще]   B= [се, срещнат, в ,.. ]

B0Token: се, B0_LastThreeLetters: �е, B0_LastTwoLetters: е, S0B0Distance: 1, S0B0Token: ще_се, S0B1Token: ще_срещнат, S0Token: ще, S0_LastThreeLetters: �е, S0_LastTwoLetters: е, TransHistory1: 2, TransHistory2: 20, 

20- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ще, се]   B= [срещнат, в, рамките ,.. ]

B0Token: срещнат, B0_LastThreeLetters: �т, B0_LastTwoLetters: т, S0B0Distance: 1, S0B0Token: се_срещнат, S0B1Token: се_в, S0Token: се, S0_LastThreeLetters: �е, S0_LastTwoLetters: е, S1B0Token: ще_срещнат, S1S0B0Token: ще_се_срещнат, S1S0Token: ще_се, S1Token: ще, S1_LastThreeLetters: �е, S1_LastTwoLetters: е, TransHistory1: 0, TransHistory2: 02, 

21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ще, се, срещнат]   B= [в, рамките, на ,.. ]

B0Token: в, B0_LastThreeLetters: в, B0_LastTwoLetters: в, S0B0Distance: 1, S0B0Token: срещнат_в, S0B1Token: срещнат_рамките, S0Token: срещнат, S0_LastThreeLetters: �т, S0_LastTwoLetters: т, S1B0Token: се_в, S1S0B0Token: се_срещнат_в, S1S0Token: се_срещнат, S1Token: се, S1_LastThreeLetters: �е, S1_LastTwoLetters: е, TransHistory1: 0, TransHistory2: 00, 

22- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ще, [се, срещнат]]   B= [в, рамките, на ,.. ]

B0Token: в, B0_LastThreeLetters: в, B0_LastTwoLetters: в, S0B0Distance: 1, S0B0Token: се_срещнат_в, S0B1Token: се_срещнат_рамките, S0Token: се_срещнат, S0_LastThreeLetters: �т, S0_LastTwoLetters: т, S1B0Token: ще_в, S1S0B0Token: ще_се_срещнат_в, S1S0Token: ще_се_срещнат, S1Token: ще, S1_LastThreeLetters: �е, S1_LastTwoLetters: е, TransHistory1: 0, TransHistory2: 00, 

23- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[ще, [се, срещнат]]]   B= [в, рамките, на ,.. ]

B0Token: в, B0_LastThreeLetters: в, B0_LastTwoLetters: в, S0B0Distance: 1, S0B0Token: ще_се_срещнат_в, S0B1Token: ще_се_срещнат_рамките, S0Token: ще_се_срещнат, S0_LastThreeLetters: �т, S0_LastTwoLetters: т, TransHistory1: 1, TransHistory2: 10, 

24- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [в, рамките, на ,.. ]

B0Token: в, B0_LastThreeLetters: в, B0_LastTwoLetters: в, TransHistory1: 1, TransHistory2: 11, 

25- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [в]   B= [рамките, на, 15 ,.. ]

B0Token: рамките, B0_LastThreeLetters: �е, B0_LastTwoLetters: е, S0B0Distance: 1, S0B0Token: в_рамките, S0B1Token: в_на, S0Token: в, S0_LastThreeLetters: в, S0_LastTwoLetters: в, TransHistory1: 2, TransHistory2: 21, 

26- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [рамките, на, 15 ,.. ]

B0Token: рамките, B0_LastThreeLetters: �е, B0_LastTwoLetters: е, TransHistory1: 0, TransHistory2: 02, 

27- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [рамките]   B= [на, 15, дни ,.. ]

B0Token: на, B0_LastThreeLetters: �а, B0_LastTwoLetters: а, S0B0Distance: 1, S0B0Token: рамките_на, S0B1Token: рамките_15, S0Token: рамките, S0_LastThreeLetters: �е, S0_LastTwoLetters: е, TransHistory1: 2, TransHistory2: 20, 

28- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [на, 15, дни ,.. ]

B0Token: на, B0_LastThreeLetters: �а, B0_LastTwoLetters: а, TransHistory1: 0, TransHistory2: 02, 

29- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [на]   B= [15, дни, , ,.. ]

B0Token: 15, B0_LastThreeLetters: 15, B0_LastTwoLetters: 15, S0B0Distance: 1, S0B0Token: на_15, S0B1Token: на_дни, S0Token: на, S0_LastThreeLetters: �а, S0_LastTwoLetters: а, TransHistory1: 2, TransHistory2: 20, 

30- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [15, дни, , ,.. ]

B0Token: 15, B0_LastThreeLetters: 15, B0_LastTwoLetters: 15, TransHistory1: 0, TransHistory2: 02, 

31- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [15]   B= [дни, ,, за ,.. ]

B0Token: дни, B0_LastThreeLetters: �и, B0_LastTwoLetters: и, S0B0Distance: 1, S0B0Token: 15_дни, S0B1Token: 15_,, S0Token: 15, S0_LastThreeLetters: 15, S0_LastTwoLetters: 15, TransHistory1: 2, TransHistory2: 20, 

32- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [дни, ,, за ,.. ]

B0Token: дни, B0_LastThreeLetters: �и, B0_LastTwoLetters: и, TransHistory1: 0, TransHistory2: 02, 

33- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [дни]   B= [,, за, да ,.. ]

B0Token: ,, B0_LastThreeLetters: ,, B0_LastTwoLetters: ,, S0B0Distance: 1, S0B0Token: дни_,, S0B1Token: дни_за, S0Token: дни, S0_LastThreeLetters: �и, S0_LastTwoLetters: и, TransHistory1: 2, TransHistory2: 20, 

34- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, за, да ,.. ]

B0Token: ,, B0_LastThreeLetters: ,, B0_LastTwoLetters: ,, TransHistory1: 0, TransHistory2: 02, 

35- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [за, да, се ,.. ]

B0Token: за, B0_LastThreeLetters: �а, B0_LastTwoLetters: а, S0B0Distance: 1, S0B0Token: ,_за, S0B1Token: ,_да, S0Token: ,, S0_LastThreeLetters: ,, S0_LastTwoLetters: ,, TransHistory1: 2, TransHistory2: 20, 

36- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [за, да, се ,.. ]

B0Token: за, B0_LastThreeLetters: �а, B0_LastTwoLetters: а, TransHistory1: 0, TransHistory2: 02, 

37- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [за]   B= [да, се, договорят ,.. ]

B0Token: да, B0_LastThreeLetters: �а, B0_LastTwoLetters: а, S0B0Distance: 1, S0B0Token: за_да, S0B1Token: за_се, S0Token: за, S0_LastThreeLetters: �а, S0_LastTwoLetters: а, TransHistory1: 2, TransHistory2: 20, 

38- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [да, се, договорят ,.. ]

B0Token: да, B0_LastThreeLetters: �а, B0_LastTwoLetters: а, TransHistory1: 0, TransHistory2: 02, 

39- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [да]   B= [се, договорят, по ,.. ]

B0Token: се, B0_LastThreeLetters: �е, B0_LastTwoLetters: е, S0B0Distance: 1, S0B0Token: да_се, S0B1Token: да_договорят, S0Token: да, S0_LastThreeLetters: �а, S0_LastTwoLetters: а, TransHistory1: 2, TransHistory2: 20, 

40- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [се, договорят, по ,.. ]

B0Token: се, B0_LastThreeLetters: �е, B0_LastTwoLetters: е, TransHistory1: 0, TransHistory2: 02, 

41- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [се]   B= [договорят, по, останалите ,.. ]

B0Token: договорят, B0_LastThreeLetters: �т, B0_LastTwoLetters: т, S0B0Distance: 1, S0B0Token: се_договорят, S0B1Token: се_по, S0Token: се, S0_LastThreeLetters: �е, S0_LastTwoLetters: е, TransHistory1: 2, TransHistory2: 20, 

42- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [се, договорят]   B= [по, останалите, проектоизменения ,.. ]

B0Token: по, B0_LastThreeLetters: �о, B0_LastTwoLetters: о, S0B0Distance: 1, S0B0Token: договорят_по, S0B1Token: договорят_останалите, S0Token: договорят, S0_LastThreeLetters: �т, S0_LastTwoLetters: т, S1B0Token: се_по, S1S0B0Token: се_договорят_по, S1S0Token: се_договорят, S1Token: се, S1_LastThreeLetters: �е, S1_LastTwoLetters: е, TransHistory1: 0, TransHistory2: 02, 

43- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[се, договорят]]   B= [по, останалите, проектоизменения ,.. ]

B0Token: по, B0_LastThreeLetters: �о, B0_LastTwoLetters: о, S0B0Distance: 1, S0B0Token: се_договорят_по, S0B1Token: се_договорят_останалите, S0Token: се_договорят, S0_LastThreeLetters: �т, S0_LastTwoLetters: т, TransHistory1: 0, TransHistory2: 00, 

44- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [по, останалите, проектоизменения ,.. ]

B0Token: по, B0_LastThreeLetters: �о, B0_LastTwoLetters: о, TransHistory1: 1, TransHistory2: 10, 

45- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [по]   B= [останалите, проектоизменения, , ,.. ]

B0Token: останалите, B0_LastThreeLetters: �е, B0_LastTwoLetters: е, S0B0Distance: 1, S0B0Token: по_останалите, S0B1Token: по_проектоизменения, S0Token: по, S0_LastThreeLetters: �о, S0_LastTwoLetters: о, TransHistory1: 2, TransHistory2: 21, 

46- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [останалите, проектоизменения, , ,.. ]

B0Token: останалите, B0_LastThreeLetters: �е, B0_LastTwoLetters: е, TransHistory1: 0, TransHistory2: 02, 

47- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [останалите]   B= [проектоизменения, ,, препоръчани ,.. ]

B0Token: проектоизменения, B0_LastThreeLetters: �я, B0_LastTwoLetters: я, S0B0Distance: 1, S0B0Token: останалите_проектоизменения, S0B1Token: останалите_,, S0Token: останалите, S0_LastThreeLetters: �е, S0_LastTwoLetters: е, TransHistory1: 2, TransHistory2: 20, 

48- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [проектоизменения, ,, препоръчани ,.. ]

B0Token: проектоизменения, B0_LastThreeLetters: �я, B0_LastTwoLetters: я, TransHistory1: 0, TransHistory2: 02, 

49- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [проектоизменения]   B= [,, препоръчани, от ,.. ]

B0Token: ,, B0_LastThreeLetters: ,, B0_LastTwoLetters: ,, S0B0Distance: 1, S0B0Token: проектоизменения_,, S0B1Token: проектоизменения_препоръчани, S0Token: проектоизменения, S0_LastThreeLetters: �я, S0_LastTwoLetters: я, TransHistory1: 2, TransHistory2: 20, 

50- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, препоръчани, от ,.. ]

B0Token: ,, B0_LastThreeLetters: ,, B0_LastTwoLetters: ,, TransHistory1: 0, TransHistory2: 02, 

51- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [препоръчани, от, Комитета ,.. ]

B0Token: препоръчани, B0_LastThreeLetters: �и, B0_LastTwoLetters: и, S0B0Distance: 1, S0B0Token: ,_препоръчани, S0B1Token: ,_от, S0Token: ,, S0_LastThreeLetters: ,, S0_LastTwoLetters: ,, TransHistory1: 2, TransHistory2: 20, 

52- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [препоръчани, от, Комитета ,.. ]

B0Token: препоръчани, B0_LastThreeLetters: �и, B0_LastTwoLetters: и, TransHistory1: 0, TransHistory2: 02, 

53- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [препоръчани]   B= [от, Комитета, &quot; ,.. ]

B0Token: от, B0_LastThreeLetters: �т, B0_LastTwoLetters: т, S0B0Distance: 1, S0B0Token: препоръчани_от, S0B1Token: препоръчани_Комитета, S0Token: препоръчани, S0_LastThreeLetters: �и, S0_LastTwoLetters: и, TransHistory1: 2, TransHistory2: 20, 

54- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [от, Комитета, &quot; ,.. ]

B0Token: от, B0_LastThreeLetters: �т, B0_LastTwoLetters: т, TransHistory1: 0, TransHistory2: 02, 

55- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [от]   B= [Комитета, &quot;, Булдозер ,.. ]

B0Token: Комитета, B0_LastThreeLetters: �а, B0_LastTwoLetters: а, S0B0Distance: 1, S0B0Token: от_Комитета, S0B1Token: от_&quot;, S0Token: от, S0_LastThreeLetters: �т, S0_LastTwoLetters: т, TransHistory1: 2, TransHistory2: 20, 

56- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Комитета, &quot;, Булдозер ,.. ]

B0Token: Комитета, B0_LastThreeLetters: �а, B0_LastTwoLetters: а, TransHistory1: 0, TransHistory2: 02, 

57- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Комитета]   B= [&quot;, Булдозер, &quot; ,.. ]

B0Token: &quot;, B0_LastThreeLetters: ot;, B0_LastTwoLetters: t;, S0B0Distance: 1, S0B0Token: Комитета_&quot;, S0B1Token: Комитета_Булдозер, S0Token: Комитета, S0_LastThreeLetters: �а, S0_LastTwoLetters: а, TransHistory1: 2, TransHistory2: 20, 

58- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [&quot;, Булдозер, &quot; ,.. ]

B0Token: &quot;, B0_LastThreeLetters: ot;, B0_LastTwoLetters: t;, TransHistory1: 0, TransHistory2: 02, 

59- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [&quot;]   B= [Булдозер, &quot;, към ,.. ]

B0Token: Булдозер, B0_LastThreeLetters: �р, B0_LastTwoLetters: р, S0B0Distance: 1, S0B0Token: &quot;_Булдозер, S0B1Token: &quot;_&quot;, S0Token: &quot;, S0_LastThreeLetters: ot;, S0_LastTwoLetters: t;, TransHistory1: 2, TransHistory2: 20, 

60- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Булдозер, &quot;, към ,.. ]

B0Token: Булдозер, B0_LastThreeLetters: �р, B0_LastTwoLetters: р, TransHistory1: 0, TransHistory2: 02, 

61- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Булдозер]   B= [&quot;, към, Службата ,.. ]

B0Token: &quot;, B0_LastThreeLetters: ot;, B0_LastTwoLetters: t;, S0B0Distance: 1, S0B0Token: Булдозер_&quot;, S0B1Token: Булдозер_към, S0Token: Булдозер, S0_LastThreeLetters: �р, S0_LastTwoLetters: р, TransHistory1: 2, TransHistory2: 20, 

62- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [&quot;, към, Службата ,.. ]

B0Token: &quot;, B0_LastThreeLetters: ot;, B0_LastTwoLetters: t;, TransHistory1: 0, TransHistory2: 02, 

63- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [&quot;]   B= [към, Службата, на ,.. ]

B0Token: към, B0_LastThreeLetters: �м, B0_LastTwoLetters: м, S0B0Distance: 1, S0B0Token: &quot;_към, S0B1Token: &quot;_Службата, S0Token: &quot;, S0_LastThreeLetters: ot;, S0_LastTwoLetters: t;, TransHistory1: 2, TransHistory2: 20, 

64- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [към, Службата, на ,.. ]

B0Token: към, B0_LastThreeLetters: �м, B0_LastTwoLetters: м, TransHistory1: 0, TransHistory2: 02, 

65- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [към]   B= [Службата, на, Върховния ,.. ]

B0Token: Службата, B0_LastThreeLetters: �а, B0_LastTwoLetters: а, S0B0Distance: 1, S0B0Token: към_Службата, S0B1Token: към_на, S0Token: към, S0_LastThreeLetters: �м, S0_LastTwoLetters: м, TransHistory1: 2, TransHistory2: 20, 

66- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Службата, на, Върховния ,.. ]

B0Token: Службата, B0_LastThreeLetters: �а, B0_LastTwoLetters: а, TransHistory1: 0, TransHistory2: 02, 

67- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Службата]   B= [на, Върховния, представител ,.. ]

B0Token: на, B0_LastThreeLetters: �а, B0_LastTwoLetters: а, S0B0Distance: 1, S0B0Token: Службата_на, S0B1Token: Службата_Върховния, S0Token: Службата, S0_LastThreeLetters: �а, S0_LastTwoLetters: а, TransHistory1: 2, TransHistory2: 20, 

68- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [на, Върховния, представител ,.. ]

B0Token: на, B0_LastThreeLetters: �а, B0_LastTwoLetters: а, TransHistory1: 0, TransHistory2: 02, 

69- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [на]   B= [Върховния, представител, . ,.. ]

B0Token: Върховния, B0_LastThreeLetters: �я, B0_LastTwoLetters: я, S0B0Distance: 1, S0B0Token: на_Върховния, S0B1Token: на_представител, S0Token: на, S0_LastThreeLetters: �а, S0_LastTwoLetters: а, TransHistory1: 2, TransHistory2: 20, 

70- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Върховния, представител, . ,.. ]

B0Token: Върховния, B0_LastThreeLetters: �я, B0_LastTwoLetters: я, TransHistory1: 0, TransHistory2: 02, 

71- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Върховния]   B= [представител, . ,.. ]

B0Token: представител, B0_LastThreeLetters: �л, B0_LastTwoLetters: л, S0B0Distance: 1, S0B0Token: Върховния_представител, S0B1Token: Върховния_., S0Token: Върховния, S0_LastThreeLetters: �я, S0_LastTwoLetters: я, TransHistory1: 2, TransHistory2: 20, 

72- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [представител, . ,.. ]

B0Token: представител, B0_LastThreeLetters: �л, B0_LastTwoLetters: л, TransHistory1: 0, TransHistory2: 02, 

73- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [представител]   B= [.]

B0Token: ., B0_LastThreeLetters: ., B0_LastTwoLetters: ., S0B0Distance: 1, S0B0Token: представител_., S0Token: представител, S0_LastThreeLetters: �л, S0_LastTwoLetters: л, TransHistory1: 2, TransHistory2: 20, 

74- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [.]

B0Token: ., B0_LastThreeLetters: ., B0_LastTwoLetters: ., TransHistory1: 0, TransHistory2: 02, 

75- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [ ]

S0Token: ., S0_LastThreeLetters: ., S0_LastTwoLetters: ., TransHistory1: 2, TransHistory2: 20, 

76- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

## Sentence No. 2725 - 
В понеделник сръбското правителство призова Сливанчанин и други двама сред най-търсените заподозрени във военни престъпления , Радован Караджич и Ратко Младич , също да се предадат , поемайки ангажимент , че страната ще продължи да изпълнява своите задължения към Трибунала на ООН и други международни организации .
### Existing MWEs: 
1- **се предадат** (IReflV)
2- **поемайки ангажимент** (LVC)
3- **изпълнява задължения** (LVC)
### Identified MWEs: 
1- **се предадат** 

2- **поемайки ангажимент** 

3- **изпълнява задължения** 




0- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [В, понеделник, сръбското ,.. ]

B0Token: В, B0_LastThreeLetters: В, B0_LastTwoLetters: В, 

1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [В]   B= [понеделник, сръбското, правителство ,.. ]

B0Token: понеделник, B0_LastThreeLetters: �к, B0_LastTwoLetters: к, S0B0Distance: 1, S0B0Token: В_понеделник, S0B1Token: В_сръбското, S0Token: В, S0_LastThreeLetters: В, S0_LastTwoLetters: В, TransHistory1: 0, 

2- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [понеделник, сръбското, правителство ,.. ]

B0Token: понеделник, B0_LastThreeLetters: �к, B0_LastTwoLetters: к, TransHistory1: 0, TransHistory2: 00, 

3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [понеделник]   B= [сръбското, правителство, призова ,.. ]

B0Token: сръбското, B0_LastThreeLetters: �о, B0_LastTwoLetters: о, S0B0Distance: 1, S0B0Token: понеделник_сръбското, S0B1Token: понеделник_правителство, S0Token: понеделник, S0_LastThreeLetters: �к, S0_LastTwoLetters: к, TransHistory1: 2, TransHistory2: 20, 

4- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [сръбското, правителство, призова ,.. ]

B0Token: сръбското, B0_LastThreeLetters: �о, B0_LastTwoLetters: о, TransHistory1: 0, TransHistory2: 02, 

5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [сръбското]   B= [правителство, призова, Сливанчанин ,.. ]

B0Token: правителство, B0_LastThreeLetters: �о, B0_LastTwoLetters: о, S0B0Distance: 1, S0B0Token: сръбското_правителство, S0B1Token: сръбското_призова, S0Token: сръбското, S0_LastThreeLetters: �о, S0_LastTwoLetters: о, TransHistory1: 2, TransHistory2: 20, 

6- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [правителство, призова, Сливанчанин ,.. ]

B0Token: правителство, B0_LastThreeLetters: �о, B0_LastTwoLetters: о, TransHistory1: 0, TransHistory2: 02, 

7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [правителство]   B= [призова, Сливанчанин, и ,.. ]

B0Token: призова, B0_LastThreeLetters: �а, B0_LastTwoLetters: а, S0B0Distance: 1, S0B0Token: правителство_призова, S0B1Token: правителство_Сливанчанин, S0Token: правителство, S0_LastThreeLetters: �о, S0_LastTwoLetters: о, TransHistory1: 2, TransHistory2: 20, 

8- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [призова, Сливанчанин, и ,.. ]

B0Token: призова, B0_LastThreeLetters: �а, B0_LastTwoLetters: а, TransHistory1: 0, TransHistory2: 02, 

9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [призова]   B= [Сливанчанин, и, други ,.. ]

B0Token: Сливанчанин, B0_LastThreeLetters: �н, B0_LastTwoLetters: н, S0B0Distance: 1, S0B0Token: призова_Сливанчанин, S0B1Token: призова_и, S0Token: призова, S0_LastThreeLetters: �а, S0_LastTwoLetters: а, TransHistory1: 2, TransHistory2: 20, 

10- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Сливанчанин, и, други ,.. ]

B0Token: Сливанчанин, B0_LastThreeLetters: �н, B0_LastTwoLetters: н, TransHistory1: 0, TransHistory2: 02, 

11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Сливанчанин]   B= [и, други, двама ,.. ]

B0Token: и, B0_LastThreeLetters: и, B0_LastTwoLetters: и, S0B0Distance: 1, S0B0Token: Сливанчанин_и, S0B1Token: Сливанчанин_други, S0Token: Сливанчанин, S0_LastThreeLetters: �н, S0_LastTwoLetters: н, TransHistory1: 2, TransHistory2: 20, 

12- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [и, други, двама ,.. ]

B0Token: и, B0_LastThreeLetters: и, B0_LastTwoLetters: и, TransHistory1: 0, TransHistory2: 02, 

13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [и]   B= [други, двама, сред ,.. ]

B0Token: други, B0_LastThreeLetters: �и, B0_LastTwoLetters: и, S0B0Distance: 1, S0B0Token: и_други, S0B1Token: и_двама, S0Token: и, S0_LastThreeLetters: и, S0_LastTwoLetters: и, TransHistory1: 2, TransHistory2: 20, 

14- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [други, двама, сред ,.. ]

B0Token: други, B0_LastThreeLetters: �и, B0_LastTwoLetters: и, TransHistory1: 0, TransHistory2: 02, 

15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [други]   B= [двама, сред, най-търсените ,.. ]

B0Token: двама, B0_LastThreeLetters: �а, B0_LastTwoLetters: а, S0B0Distance: 1, S0B0Token: други_двама, S0B1Token: други_сред, S0Token: други, S0_LastThreeLetters: �и, S0_LastTwoLetters: и, TransHistory1: 2, TransHistory2: 20, 

16- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [двама, сред, най-търсените ,.. ]

B0Token: двама, B0_LastThreeLetters: �а, B0_LastTwoLetters: а, TransHistory1: 0, TransHistory2: 02, 

17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [двама]   B= [сред, най-търсените, заподозрени ,.. ]

B0Token: сред, B0_LastThreeLetters: �д, B0_LastTwoLetters: д, S0B0Distance: 1, S0B0Token: двама_сред, S0B1Token: двама_най-търсените, S0Token: двама, S0_LastThreeLetters: �а, S0_LastTwoLetters: а, TransHistory1: 2, TransHistory2: 20, 

18- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [сред, най-търсените, заподозрени ,.. ]

B0Token: сред, B0_LastThreeLetters: �д, B0_LastTwoLetters: д, TransHistory1: 0, TransHistory2: 02, 

19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [сред]   B= [най-търсените, заподозрени, във ,.. ]

B0Token: най-търсените, B0_LastThreeLetters: �е, B0_LastTwoLetters: е, S0B0Distance: 1, S0B0Token: сред_най-търсените, S0B1Token: сред_заподозрени, S0Token: сред, S0_LastThreeLetters: �д, S0_LastTwoLetters: д, TransHistory1: 2, TransHistory2: 20, 

20- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [най-търсените, заподозрени, във ,.. ]

B0Token: най-търсените, B0_LastThreeLetters: �е, B0_LastTwoLetters: е, TransHistory1: 0, TransHistory2: 02, 

21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [най-търсените]   B= [заподозрени, във, военни ,.. ]

B0Token: заподозрени, B0_LastThreeLetters: �и, B0_LastTwoLetters: и, S0B0Distance: 1, S0B0Token: най-търсените_заподозрени, S0B1Token: най-търсените_във, S0Token: най-търсените, S0_LastThreeLetters: �е, S0_LastTwoLetters: е, TransHistory1: 2, TransHistory2: 20, 

22- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [заподозрени, във, военни ,.. ]

B0Token: заподозрени, B0_LastThreeLetters: �и, B0_LastTwoLetters: и, TransHistory1: 0, TransHistory2: 02, 

23- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [заподозрени]   B= [във, военни, престъпления ,.. ]

B0Token: във, B0_LastThreeLetters: �в, B0_LastTwoLetters: в, S0B0Distance: 1, S0B0Token: заподозрени_във, S0B1Token: заподозрени_военни, S0Token: заподозрени, S0_LastThreeLetters: �и, S0_LastTwoLetters: и, TransHistory1: 2, TransHistory2: 20, 

24- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [във, военни, престъпления ,.. ]

B0Token: във, B0_LastThreeLetters: �в, B0_LastTwoLetters: в, TransHistory1: 0, TransHistory2: 02, 

25- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [във]   B= [военни, престъпления, , ,.. ]

B0Token: военни, B0_LastThreeLetters: �и, B0_LastTwoLetters: и, S0B0Distance: 1, S0B0Token: във_военни, S0B1Token: във_престъпления, S0Token: във, S0_LastThreeLetters: �в, S0_LastTwoLetters: в, TransHistory1: 2, TransHistory2: 20, 

26- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [военни, престъпления, , ,.. ]

B0Token: военни, B0_LastThreeLetters: �и, B0_LastTwoLetters: и, TransHistory1: 0, TransHistory2: 02, 

27- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [военни]   B= [престъпления, ,, Радован ,.. ]

B0Token: престъпления, B0_LastThreeLetters: �я, B0_LastTwoLetters: я, S0B0Distance: 1, S0B0Token: военни_престъпления, S0B1Token: военни_,, S0Token: военни, S0_LastThreeLetters: �и, S0_LastTwoLetters: и, TransHistory1: 2, TransHistory2: 20, 

28- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [престъпления, ,, Радован ,.. ]

B0Token: престъпления, B0_LastThreeLetters: �я, B0_LastTwoLetters: я, TransHistory1: 0, TransHistory2: 02, 

29- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [престъпления]   B= [,, Радован, Караджич ,.. ]

B0Token: ,, B0_LastThreeLetters: ,, B0_LastTwoLetters: ,, S0B0Distance: 1, S0B0Token: престъпления_,, S0B1Token: престъпления_Радован, S0Token: престъпления, S0_LastThreeLetters: �я, S0_LastTwoLetters: я, TransHistory1: 2, TransHistory2: 20, 

30- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, Радован, Караджич ,.. ]

B0Token: ,, B0_LastThreeLetters: ,, B0_LastTwoLetters: ,, TransHistory1: 0, TransHistory2: 02, 

31- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [Радован, Караджич, и ,.. ]

B0Token: Радован, B0_LastThreeLetters: �н, B0_LastTwoLetters: н, S0B0Distance: 1, S0B0Token: ,_Радован, S0B1Token: ,_Караджич, S0Token: ,, S0_LastThreeLetters: ,, S0_LastTwoLetters: ,, TransHistory1: 2, TransHistory2: 20, 

32- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Радован, Караджич, и ,.. ]

B0Token: Радован, B0_LastThreeLetters: �н, B0_LastTwoLetters: н, TransHistory1: 0, TransHistory2: 02, 

33- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Радован]   B= [Караджич, и, Ратко ,.. ]

B0Token: Караджич, B0_LastThreeLetters: �ч, B0_LastTwoLetters: ч, S0B0Distance: 1, S0B0Token: Радован_Караджич, S0B1Token: Радован_и, S0Token: Радован, S0_LastThreeLetters: �н, S0_LastTwoLetters: н, TransHistory1: 2, TransHistory2: 20, 

34- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Караджич, и, Ратко ,.. ]

B0Token: Караджич, B0_LastThreeLetters: �ч, B0_LastTwoLetters: ч, TransHistory1: 0, TransHistory2: 02, 

35- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Караджич]   B= [и, Ратко, Младич ,.. ]

B0Token: и, B0_LastThreeLetters: и, B0_LastTwoLetters: и, S0B0Distance: 1, S0B0Token: Караджич_и, S0B1Token: Караджич_Ратко, S0Token: Караджич, S0_LastThreeLetters: �ч, S0_LastTwoLetters: ч, TransHistory1: 2, TransHistory2: 20, 

36- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [и, Ратко, Младич ,.. ]

B0Token: и, B0_LastThreeLetters: и, B0_LastTwoLetters: и, TransHistory1: 0, TransHistory2: 02, 

37- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [и]   B= [Ратко, Младич, , ,.. ]

B0Token: Ратко, B0_LastThreeLetters: �о, B0_LastTwoLetters: о, S0B0Distance: 1, S0B0Token: и_Ратко, S0B1Token: и_Младич, S0Token: и, S0_LastThreeLetters: и, S0_LastTwoLetters: и, TransHistory1: 2, TransHistory2: 20, 

38- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Ратко, Младич, , ,.. ]

B0Token: Ратко, B0_LastThreeLetters: �о, B0_LastTwoLetters: о, TransHistory1: 0, TransHistory2: 02, 

39- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Ратко]   B= [Младич, ,, също ,.. ]

B0Token: Младич, B0_LastThreeLetters: �ч, B0_LastTwoLetters: ч, S0B0Distance: 1, S0B0Token: Ратко_Младич, S0B1Token: Ратко_,, S0Token: Ратко, S0_LastThreeLetters: �о, S0_LastTwoLetters: о, TransHistory1: 2, TransHistory2: 20, 

40- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Младич, ,, също ,.. ]

B0Token: Младич, B0_LastThreeLetters: �ч, B0_LastTwoLetters: ч, TransHistory1: 0, TransHistory2: 02, 

41- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Младич]   B= [,, също, да ,.. ]

B0Token: ,, B0_LastThreeLetters: ,, B0_LastTwoLetters: ,, S0B0Distance: 1, S0B0Token: Младич_,, S0B1Token: Младич_също, S0Token: Младич, S0_LastThreeLetters: �ч, S0_LastTwoLetters: ч, TransHistory1: 2, TransHistory2: 20, 

42- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, също, да ,.. ]

B0Token: ,, B0_LastThreeLetters: ,, B0_LastTwoLetters: ,, TransHistory1: 0, TransHistory2: 02, 

43- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [също, да, се ,.. ]

B0Token: също, B0_LastThreeLetters: �о, B0_LastTwoLetters: о, S0B0Distance: 1, S0B0Token: ,_също, S0B1Token: ,_да, S0Token: ,, S0_LastThreeLetters: ,, S0_LastTwoLetters: ,, TransHistory1: 2, TransHistory2: 20, 

44- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [също, да, се ,.. ]

B0Token: също, B0_LastThreeLetters: �о, B0_LastTwoLetters: о, TransHistory1: 0, TransHistory2: 02, 

45- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [също]   B= [да, се, предадат ,.. ]

B0Token: да, B0_LastThreeLetters: �а, B0_LastTwoLetters: а, S0B0Distance: 1, S0B0Token: също_да, S0B1Token: също_се, S0Token: също, S0_LastThreeLetters: �о, S0_LastTwoLetters: о, TransHistory1: 2, TransHistory2: 20, 

46- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [да, се, предадат ,.. ]

B0Token: да, B0_LastThreeLetters: �а, B0_LastTwoLetters: а, TransHistory1: 0, TransHistory2: 02, 

47- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [да]   B= [се, предадат, , ,.. ]

B0Token: се, B0_LastThreeLetters: �е, B0_LastTwoLetters: е, S0B0Distance: 1, S0B0Token: да_се, S0B1Token: да_предадат, S0Token: да, S0_LastThreeLetters: �а, S0_LastTwoLetters: а, TransHistory1: 2, TransHistory2: 20, 

48- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [се, предадат, , ,.. ]

B0Token: се, B0_LastThreeLetters: �е, B0_LastTwoLetters: е, TransHistory1: 0, TransHistory2: 02, 

49- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [се]   B= [предадат, ,, поемайки ,.. ]

B0Token: предадат, B0_LastThreeLetters: �т, B0_LastTwoLetters: т, S0B0Distance: 1, S0B0Token: се_предадат, S0B1Token: се_,, S0Token: се, S0_LastThreeLetters: �е, S0_LastTwoLetters: е, TransHistory1: 2, TransHistory2: 20, 

50- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [се, предадат]   B= [,, поемайки, ангажимент ,.. ]

B0Token: ,, B0_LastThreeLetters: ,, B0_LastTwoLetters: ,, S0B0Distance: 1, S0B0Token: предадат_,, S0B1Token: предадат_поемайки, S0Token: предадат, S0_LastThreeLetters: �т, S0_LastTwoLetters: т, S1B0Token: се_,, S1S0B0Token: се_предадат_,, S1S0Token: се_предадат, S1Token: се, S1_LastThreeLetters: �е, S1_LastTwoLetters: е, TransHistory1: 0, TransHistory2: 02, 

51- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[се, предадат]]   B= [,, поемайки, ангажимент ,.. ]

B0Token: ,, B0_LastThreeLetters: ,, B0_LastTwoLetters: ,, S0B0Distance: 1, S0B0Token: се_предадат_,, S0B1Token: се_предадат_поемайки, S0Token: се_предадат, S0_LastThreeLetters: �т, S0_LastTwoLetters: т, TransHistory1: 0, TransHistory2: 00, 

52- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, поемайки, ангажимент ,.. ]

B0Token: ,, B0_LastThreeLetters: ,, B0_LastTwoLetters: ,, TransHistory1: 1, TransHistory2: 10, 

53- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [поемайки, ангажимент, , ,.. ]

B0Token: поемайки, B0_LastThreeLetters: �и, B0_LastTwoLetters: и, S0B0Distance: 1, S0B0Token: ,_поемайки, S0B1Token: ,_ангажимент, S0Token: ,, S0_LastThreeLetters: ,, S0_LastTwoLetters: ,, TransHistory1: 2, TransHistory2: 21, 

54- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [поемайки, ангажимент, , ,.. ]

B0Token: поемайки, B0_LastThreeLetters: �и, B0_LastTwoLetters: и, TransHistory1: 0, TransHistory2: 02, 

55- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [поемайки]   B= [ангажимент, ,, че ,.. ]

B0Token: ангажимент, B0_LastThreeLetters: �т, B0_LastTwoLetters: т, S0B0Distance: 1, S0B0Token: поемайки_ангажимент, S0B1Token: поемайки_,, S0Token: поемайки, S0_LastThreeLetters: �и, S0_LastTwoLetters: и, TransHistory1: 2, TransHistory2: 20, 

56- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [поемайки, ангажимент]   B= [,, че, страната ,.. ]

B0Token: ,, B0_LastThreeLetters: ,, B0_LastTwoLetters: ,, S0B0Distance: 1, S0B0Token: ангажимент_,, S0B1Token: ангажимент_че, S0Token: ангажимент, S0_LastThreeLetters: �т, S0_LastTwoLetters: т, S1B0Token: поемайки_,, S1S0B0Token: поемайки_ангажимент_,, S1S0Token: поемайки_ангажимент, S1Token: поемайки, S1_LastThreeLetters: �и, S1_LastTwoLetters: и, TransHistory1: 0, TransHistory2: 02, 

57- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[поемайки, ангажимент]]   B= [,, че, страната ,.. ]

B0Token: ,, B0_LastThreeLetters: ,, B0_LastTwoLetters: ,, S0B0Distance: 1, S0B0Token: поемайки_ангажимент_,, S0B1Token: поемайки_ангажимент_че, S0Token: поемайки_ангажимент, S0_LastThreeLetters: �т, S0_LastTwoLetters: т, TransHistory1: 0, TransHistory2: 00, 

58- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [,, че, страната ,.. ]

B0Token: ,, B0_LastThreeLetters: ,, B0_LastTwoLetters: ,, TransHistory1: 1, TransHistory2: 10, 

59- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [,]   B= [че, страната, ще ,.. ]

B0Token: че, B0_LastThreeLetters: �е, B0_LastTwoLetters: е, S0B0Distance: 1, S0B0Token: ,_че, S0B1Token: ,_страната, S0Token: ,, S0_LastThreeLetters: ,, S0_LastTwoLetters: ,, TransHistory1: 2, TransHistory2: 21, 

60- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [че, страната, ще ,.. ]

B0Token: че, B0_LastThreeLetters: �е, B0_LastTwoLetters: е, TransHistory1: 0, TransHistory2: 02, 

61- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [че]   B= [страната, ще, продължи ,.. ]

B0Token: страната, B0_LastThreeLetters: �а, B0_LastTwoLetters: а, S0B0Distance: 1, S0B0Token: че_страната, S0B1Token: че_ще, S0Token: че, S0_LastThreeLetters: �е, S0_LastTwoLetters: е, TransHistory1: 2, TransHistory2: 20, 

62- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [страната, ще, продължи ,.. ]

B0Token: страната, B0_LastThreeLetters: �а, B0_LastTwoLetters: а, TransHistory1: 0, TransHistory2: 02, 

63- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [страната]   B= [ще, продължи, да ,.. ]

B0Token: ще, B0_LastThreeLetters: �е, B0_LastTwoLetters: е, S0B0Distance: 1, S0B0Token: страната_ще, S0B1Token: страната_продължи, S0Token: страната, S0_LastThreeLetters: �а, S0_LastTwoLetters: а, TransHistory1: 2, TransHistory2: 20, 

64- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ще, продължи, да ,.. ]

B0Token: ще, B0_LastThreeLetters: �е, B0_LastTwoLetters: е, TransHistory1: 0, TransHistory2: 02, 

65- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ще]   B= [продължи, да, изпълнява ,.. ]

B0Token: продължи, B0_LastThreeLetters: �и, B0_LastTwoLetters: и, S0B0Distance: 1, S0B0Token: ще_продължи, S0B1Token: ще_да, S0Token: ще, S0_LastThreeLetters: �е, S0_LastTwoLetters: е, TransHistory1: 2, TransHistory2: 20, 

66- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [продължи, да, изпълнява ,.. ]

B0Token: продължи, B0_LastThreeLetters: �и, B0_LastTwoLetters: и, TransHistory1: 0, TransHistory2: 02, 

67- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [продължи]   B= [да, изпълнява, своите ,.. ]

B0Token: да, B0_LastThreeLetters: �а, B0_LastTwoLetters: а, S0B0Distance: 1, S0B0Token: продължи_да, S0B1Token: продължи_изпълнява, S0Token: продължи, S0_LastThreeLetters: �и, S0_LastTwoLetters: и, TransHistory1: 2, TransHistory2: 20, 

68- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [да, изпълнява, своите ,.. ]

B0Token: да, B0_LastThreeLetters: �а, B0_LastTwoLetters: а, TransHistory1: 0, TransHistory2: 02, 

69- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [да]   B= [изпълнява, своите, задължения ,.. ]

B0Token: изпълнява, B0_LastThreeLetters: �а, B0_LastTwoLetters: а, S0B0Distance: 1, S0B0Token: да_изпълнява, S0B1Token: да_своите, S0Token: да, S0_LastThreeLetters: �а, S0_LastTwoLetters: а, TransHistory1: 2, TransHistory2: 20, 

70- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [изпълнява, своите, задължения ,.. ]

B0Token: изпълнява, B0_LastThreeLetters: �а, B0_LastTwoLetters: а, TransHistory1: 0, TransHistory2: 02, 

71- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [изпълнява]   B= [своите, задължения, към ,.. ]

B0Token: своите, B0_LastThreeLetters: �е, B0_LastTwoLetters: е, S0B0Distance: 1, S0B0Token: изпълнява_своите, S0B1Token: изпълнява_задължения, S0Token: изпълнява, S0_LastThreeLetters: �а, S0_LastTwoLetters: а, TransHistory1: 2, TransHistory2: 20, 

72- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [изпълнява, своите]   B= [задължения, към, Трибунала ,.. ]

B0Token: задължения, B0_LastThreeLetters: �я, B0_LastTwoLetters: я, S0B0Distance: 1, S0B0Token: своите_задължения, S0B1Token: своите_към, S0Token: своите, S0_LastThreeLetters: �е, S0_LastTwoLetters: е, S1B0Token: изпълнява_задължения, S1S0B0Token: изпълнява_своите_задължения, S1S0Token: изпълнява_своите, S1Token: изпълнява, S1_LastThreeLetters: �а, S1_LastTwoLetters: а, TransHistory1: 0, TransHistory2: 02, 

73- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [изпълнява]   B= [задължения, към, Трибунала ,.. ]

B0Token: задължения, B0_LastThreeLetters: �я, B0_LastTwoLetters: я, S0B0Distance: 2, S0B0Token: изпълнява_задължения, S0B1Token: изпълнява_към, S0Token: изпълнява, S0_LastThreeLetters: �а, S0_LastTwoLetters: а, TransHistory1: 0, TransHistory2: 00, 

74- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [изпълнява, задължения]   B= [към, Трибунала, на ,.. ]

B0Token: към, B0_LastThreeLetters: �м, B0_LastTwoLetters: м, S0B0Distance: 1, S0B0Token: задължения_към, S0B1Token: задължения_Трибунала, S0Token: задължения, S0_LastThreeLetters: �я, S0_LastTwoLetters: я, S1B0Token: изпълнява_към, S1S0B0Token: изпълнява_задължения_към, S1S0Token: изпълнява_задължения, S1Token: изпълнява, S1_LastThreeLetters: �а, S1_LastTwoLetters: а, TransHistory1: 2, TransHistory2: 20, 

75- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[изпълнява, задължения]]   B= [към, Трибунала, на ,.. ]

B0Token: към, B0_LastThreeLetters: �м, B0_LastTwoLetters: м, S0B0Distance: 1, S0B0Token: изпълнява_задължения_към, S0B1Token: изпълнява_задължения_Трибунала, S0Token: изпълнява_задължения, S0_LastThreeLetters: �я, S0_LastTwoLetters: я, TransHistory1: 0, TransHistory2: 02, 

76- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [към, Трибунала, на ,.. ]

B0Token: към, B0_LastThreeLetters: �м, B0_LastTwoLetters: м, TransHistory1: 1, TransHistory2: 10, 

77- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [към]   B= [Трибунала, на, ООН ,.. ]

B0Token: Трибунала, B0_LastThreeLetters: �а, B0_LastTwoLetters: а, S0B0Distance: 1, S0B0Token: към_Трибунала, S0B1Token: към_на, S0Token: към, S0_LastThreeLetters: �м, S0_LastTwoLetters: м, TransHistory1: 2, TransHistory2: 21, 

78- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [Трибунала, на, ООН ,.. ]

B0Token: Трибунала, B0_LastThreeLetters: �а, B0_LastTwoLetters: а, TransHistory1: 0, TransHistory2: 02, 

79- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [Трибунала]   B= [на, ООН, и ,.. ]

B0Token: на, B0_LastThreeLetters: �а, B0_LastTwoLetters: а, S0B0Distance: 1, S0B0Token: Трибунала_на, S0B1Token: Трибунала_ООН, S0Token: Трибунала, S0_LastThreeLetters: �а, S0_LastTwoLetters: а, TransHistory1: 2, TransHistory2: 20, 

80- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [на, ООН, и ,.. ]

B0Token: на, B0_LastThreeLetters: �а, B0_LastTwoLetters: а, TransHistory1: 0, TransHistory2: 02, 

81- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [на]   B= [ООН, и, други ,.. ]

B0Token: ООН, B0_LastThreeLetters: �Н, B0_LastTwoLetters: Н, S0B0Distance: 1, S0B0Token: на_ООН, S0B1Token: на_и, S0Token: на, S0_LastThreeLetters: �а, S0_LastTwoLetters: а, TransHistory1: 2, TransHistory2: 20, 

82- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ООН, и, други ,.. ]

B0Token: ООН, B0_LastThreeLetters: �Н, B0_LastTwoLetters: Н, TransHistory1: 0, TransHistory2: 02, 

83- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ООН]   B= [и, други, международни ,.. ]

B0Token: и, B0_LastThreeLetters: и, B0_LastTwoLetters: и, S0B0Distance: 1, S0B0Token: ООН_и, S0B1Token: ООН_други, S0Token: ООН, S0_LastThreeLetters: �Н, S0_LastTwoLetters: Н, TransHistory1: 2, TransHistory2: 20, 

84- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [и, други, международни ,.. ]

B0Token: и, B0_LastThreeLetters: и, B0_LastTwoLetters: и, TransHistory1: 0, TransHistory2: 02, 

85- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [и]   B= [други, международни, организации ,.. ]

B0Token: други, B0_LastThreeLetters: �и, B0_LastTwoLetters: и, S0B0Distance: 1, S0B0Token: и_други, S0B1Token: и_международни, S0Token: и, S0_LastThreeLetters: и, S0_LastTwoLetters: и, TransHistory1: 2, TransHistory2: 20, 

86- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [други, международни, организации ,.. ]

B0Token: други, B0_LastThreeLetters: �и, B0_LastTwoLetters: и, TransHistory1: 0, TransHistory2: 02, 

87- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [други]   B= [международни, организации, . ,.. ]

B0Token: международни, B0_LastThreeLetters: �и, B0_LastTwoLetters: и, S0B0Distance: 1, S0B0Token: други_международни, S0B1Token: други_организации, S0Token: други, S0_LastThreeLetters: �и, S0_LastTwoLetters: и, TransHistory1: 2, TransHistory2: 20, 

88- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [международни, организации, . ,.. ]

B0Token: международни, B0_LastThreeLetters: �и, B0_LastTwoLetters: и, TransHistory1: 0, TransHistory2: 02, 

89- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [международни]   B= [организации, . ,.. ]

B0Token: организации, B0_LastThreeLetters: �и, B0_LastTwoLetters: и, S0B0Distance: 1, S0B0Token: международни_организации, S0B1Token: международни_., S0Token: международни, S0_LastThreeLetters: �и, S0_LastTwoLetters: и, TransHistory1: 2, TransHistory2: 20, 

90- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [организации, . ,.. ]

B0Token: организации, B0_LastThreeLetters: �и, B0_LastTwoLetters: и, TransHistory1: 0, TransHistory2: 02, 

91- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [организации]   B= [.]

B0Token: ., B0_LastThreeLetters: ., B0_LastTwoLetters: ., S0B0Distance: 1, S0B0Token: организации_., S0Token: организации, S0_LastThreeLetters: �и, S0_LastTwoLetters: и, TransHistory1: 2, TransHistory2: 20, 

92- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [.]

B0Token: ., B0_LastThreeLetters: ., B0_LastTwoLetters: ., TransHistory1: 0, TransHistory2: 02, 

93- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [.]   B= [ ]

S0Token: ., S0_LastThreeLetters: ., S0_LastTwoLetters: ., TransHistory1: 2, TransHistory2: 20, 

94- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

