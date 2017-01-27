## Sentence No. 1292 - 
לא יקרא אדם להטלת חרם על איש ציבור או אדם פרטי לא יקח אדם חלק בביצוע חרם שהוטל על ידי כל גורם שהוא כך קובעת הצעת חוק שהונחה על שולחן הכנסת ועיקרה מאבק בחרמות
### Existing MWEs: 
1- **להטלת חרם** (LVC)
2- **שהונחה על שולחן** (VPC)



0- &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [לא, יקרא, אדם ,.. ]

B0Token: לא, B0_LastThreeLetters: �א, B0_LastTwoLetters: א, B1Token: יקרא, B1_LastThreeLetters: �א, B1_LastTwoLetters: א, 

1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [לא]   B= [יקרא, אדם, להטלת ,.. ]

B0Token: יקרא, B0_LastThreeLetters: �א, B0_LastTwoLetters: א, B1Token: אדם, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, S0B0Token: לא_יקרא, S0B1Token: לא_אדם, S0B2Token: לא_להטלת, S0Token: לא, S0_LastThreeLetters: �א, S0_LastTwoLetters: א, 

2- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [יקרא, אדם, להטלת ,.. ]

B0Token: יקרא, B0_LastThreeLetters: �א, B0_LastTwoLetters: א, B1Token: אדם, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, transitionHistoryLength1: 0, 

3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [יקרא]   B= [אדם, להטלת, חרם ,.. ]

B0Token: אדם, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, B1Token: להטלת, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, S0B0Token: יקרא_אדם, S0B1Token: יקרא_להטלת, S0B2Token: יקרא_חרם, S0Token: יקרא, S0_LastThreeLetters: �א, S0_LastTwoLetters: א, transitionHistoryLength1: 2, transitionHistoryLength2: 20, 

4- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [אדם, להטלת, חרם ,.. ]

B0Token: אדם, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, B1Token: להטלת, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [אדם]   B= [להטלת, חרם, על ,.. ]

B0Token: להטלת, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: חרם, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, S0B0Token: אדם_להטלת, S0B1Token: אדם_חרם, S0B2Token: אדם_על, S0Token: אדם, S0_LastThreeLetters: �ם, S0_LastTwoLetters: ם, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

6- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [להטלת, חרם, על ,.. ]

B0Token: להטלת, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: חרם, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [להטלת]   B= [חרם, על, איש ,.. ]

B0Token: חרם, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, B1Token: על, B1_LastThreeLetters: �ל, B1_LastTwoLetters: ל, S0B0Token: להטלת_חרם, S0B1Token: להטלת_על, S0B2Token: להטלת_איש, S0Token: להטלת, S0_LastThreeLetters: �ת, S0_LastTwoLetters: ת, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

8- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [להטלת, חרם]   B= [על, איש, ציבור ,.. ]

B0Token: על, B0_LastThreeLetters: �ל, B0_LastTwoLetters: ל, B1Token: איש, B1_LastThreeLetters: �ש, B1_LastTwoLetters: ש, S0B0Token: חרם_על, S0B1Token: חרם_איש, S0B2Token: חרם_ציבור, S0Token: חרם, S0_LastThreeLetters: �ם, S0_LastTwoLetters: ם, S1B0Token: להטלת_על, S1S0Token: להטלת_חרם, S1Token: להטלת, S1_LastThreeLetters: �ת, S1_LastTwoLetters: ת, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

9- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[להטלת, חרם]]   B= [על, איש, ציבור ,.. ]

B0Token: על, B0_LastThreeLetters: �ל, B0_LastTwoLetters: ל, B1Token: איש, B1_LastThreeLetters: �ש, B1_LastTwoLetters: ש, S0B0Token: להטלת_חרם_על, S0B1Token: להטלת_חרם_איש, S0B2Token: להטלת_חרם_ציבור, S0Token: להטלת_חרם, transitionHistoryLength1: 0, transitionHistoryLength2: 00, transitionHistoryLength3: 002, 

10- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [על, איש, ציבור ,.. ]

B0Token: על, B0_LastThreeLetters: �ל, B0_LastTwoLetters: ל, B1Token: איש, B1_LastThreeLetters: �ש, B1_LastTwoLetters: ש, transitionHistoryLength1: 1, transitionHistoryLength2: 10, transitionHistoryLength3: 100, 

11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [על]   B= [איש, ציבור, או ,.. ]

B0Token: איש, B0_LastThreeLetters: �ש, B0_LastTwoLetters: ש, B1Token: ציבור, B1_LastThreeLetters: �ר, B1_LastTwoLetters: ר, S0B0Token: על_איש, S0B1Token: על_ציבור, S0B2Token: על_או, S0Token: על, S0_LastThreeLetters: �ל, S0_LastTwoLetters: ל, transitionHistoryLength1: 2, transitionHistoryLength2: 21, transitionHistoryLength3: 210, 

12- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [איש, ציבור, או ,.. ]

B0Token: איש, B0_LastThreeLetters: �ש, B0_LastTwoLetters: ש, B1Token: ציבור, B1_LastThreeLetters: �ר, B1_LastTwoLetters: ר, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 021, 

13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [איש]   B= [ציבור, או, אדם ,.. ]

B0Token: ציבור, B0_LastThreeLetters: �ר, B0_LastTwoLetters: ר, B1Token: או, B1_LastThreeLetters: �ו, B1_LastTwoLetters: ו, S0B0Token: איש_ציבור, S0B1Token: איש_או, S0B2Token: איש_אדם, S0Token: איש, S0_LastThreeLetters: �ש, S0_LastTwoLetters: ש, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

14- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ציבור, או, אדם ,.. ]

B0Token: ציבור, B0_LastThreeLetters: �ר, B0_LastTwoLetters: ר, B1Token: או, B1_LastThreeLetters: �ו, B1_LastTwoLetters: ו, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ציבור]   B= [או, אדם, פרטי ,.. ]

B0Token: או, B0_LastThreeLetters: �ו, B0_LastTwoLetters: ו, B1Token: אדם, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, S0B0Token: ציבור_או, S0B1Token: ציבור_אדם, S0B2Token: ציבור_פרטי, S0Token: ציבור, S0_LastThreeLetters: �ר, S0_LastTwoLetters: ר, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

16- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [או, אדם, פרטי ,.. ]

B0Token: או, B0_LastThreeLetters: �ו, B0_LastTwoLetters: ו, B1Token: אדם, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [או]   B= [אדם, פרטי, לא ,.. ]

B0Token: אדם, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, B1Token: פרטי, B1_LastThreeLetters: �י, B1_LastTwoLetters: י, S0B0Token: או_אדם, S0B1Token: או_פרטי, S0B2Token: או_לא, S0Token: או, S0_LastThreeLetters: �ו, S0_LastTwoLetters: ו, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

18- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [אדם, פרטי, לא ,.. ]

B0Token: אדם, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, B1Token: פרטי, B1_LastThreeLetters: �י, B1_LastTwoLetters: י, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [אדם]   B= [פרטי, לא, יקח ,.. ]

B0Token: פרטי, B0_LastThreeLetters: �י, B0_LastTwoLetters: י, B1Token: לא, B1_LastThreeLetters: �א, B1_LastTwoLetters: א, S0B0Token: אדם_פרטי, S0B1Token: אדם_לא, S0B2Token: אדם_יקח, S0Token: אדם, S0_LastThreeLetters: �ם, S0_LastTwoLetters: ם, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

20- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [פרטי, לא, יקח ,.. ]

B0Token: פרטי, B0_LastThreeLetters: �י, B0_LastTwoLetters: י, B1Token: לא, B1_LastThreeLetters: �א, B1_LastTwoLetters: א, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [פרטי]   B= [לא, יקח, אדם ,.. ]

B0Token: לא, B0_LastThreeLetters: �א, B0_LastTwoLetters: א, B1Token: יקח, B1_LastThreeLetters: �ח, B1_LastTwoLetters: ח, S0B0Token: פרטי_לא, S0B1Token: פרטי_יקח, S0B2Token: פרטי_אדם, S0Token: פרטי, S0_LastThreeLetters: �י, S0_LastTwoLetters: י, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

22- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [לא, יקח, אדם ,.. ]

B0Token: לא, B0_LastThreeLetters: �א, B0_LastTwoLetters: א, B1Token: יקח, B1_LastThreeLetters: �ח, B1_LastTwoLetters: ח, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

23- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [לא]   B= [יקח, אדם, חלק ,.. ]

B0Token: יקח, B0_LastThreeLetters: �ח, B0_LastTwoLetters: ח, B1Token: אדם, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, S0B0Token: לא_יקח, S0B1Token: לא_אדם, S0B2Token: לא_חלק, S0Token: לא, S0_LastThreeLetters: �א, S0_LastTwoLetters: א, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

24- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [יקח, אדם, חלק ,.. ]

B0Token: יקח, B0_LastThreeLetters: �ח, B0_LastTwoLetters: ח, B1Token: אדם, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

25- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [יקח]   B= [אדם, חלק, בביצוע ,.. ]

B0Token: אדם, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, B1Token: חלק, B1_LastThreeLetters: �ק, B1_LastTwoLetters: ק, S0B0Token: יקח_אדם, S0B1Token: יקח_חלק, S0B2Token: יקח_בביצוע, S0Token: יקח, S0_LastThreeLetters: �ח, S0_LastTwoLetters: ח, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

26- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [אדם, חלק, בביצוע ,.. ]

B0Token: אדם, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, B1Token: חלק, B1_LastThreeLetters: �ק, B1_LastTwoLetters: ק, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

27- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [אדם]   B= [חלק, בביצוע, חרם ,.. ]

B0Token: חלק, B0_LastThreeLetters: �ק, B0_LastTwoLetters: ק, B1Token: בביצוע, B1_LastThreeLetters: �ע, B1_LastTwoLetters: ע, S0B0Token: אדם_חלק, S0B1Token: אדם_בביצוע, S0B2Token: אדם_חרם, S0Token: אדם, S0_LastThreeLetters: �ם, S0_LastTwoLetters: ם, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

28- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [חלק, בביצוע, חרם ,.. ]

B0Token: חלק, B0_LastThreeLetters: �ק, B0_LastTwoLetters: ק, B1Token: בביצוע, B1_LastThreeLetters: �ע, B1_LastTwoLetters: ע, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

29- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [חלק]   B= [בביצוע, חרם, שהוטל ,.. ]

B0Token: בביצוע, B0_LastThreeLetters: �ע, B0_LastTwoLetters: ע, B1Token: חרם, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, S0B0Token: חלק_בביצוע, S0B1Token: חלק_חרם, S0B2Token: חלק_שהוטל, S0Token: חלק, S0_LastThreeLetters: �ק, S0_LastTwoLetters: ק, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

30- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [בביצוע, חרם, שהוטל ,.. ]

B0Token: בביצוע, B0_LastThreeLetters: �ע, B0_LastTwoLetters: ע, B1Token: חרם, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

31- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [בביצוע]   B= [חרם, שהוטל, על ,.. ]

B0Token: חרם, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, B1Token: שהוטל, B1_LastThreeLetters: �ל, B1_LastTwoLetters: ל, S0B0Token: בביצוע_חרם, S0B1Token: בביצוע_שהוטל, S0B2Token: בביצוע_על, S0Token: בביצוע, S0_LastThreeLetters: �ע, S0_LastTwoLetters: ע, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

32- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [חרם, שהוטל, על ,.. ]

B0Token: חרם, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, B1Token: שהוטל, B1_LastThreeLetters: �ל, B1_LastTwoLetters: ל, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

33- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [חרם]   B= [שהוטל, על, ידי ,.. ]

B0Token: שהוטל, B0_LastThreeLetters: �ל, B0_LastTwoLetters: ל, B1Token: על, B1_LastThreeLetters: �ל, B1_LastTwoLetters: ל, S0B0Token: חרם_שהוטל, S0B1Token: חרם_על, S0B2Token: חרם_ידי, S0Token: חרם, S0_LastThreeLetters: �ם, S0_LastTwoLetters: ם, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

34- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [שהוטל, על, ידי ,.. ]

B0Token: שהוטל, B0_LastThreeLetters: �ל, B0_LastTwoLetters: ל, B1Token: על, B1_LastThreeLetters: �ל, B1_LastTwoLetters: ל, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

35- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [שהוטל]   B= [על, ידי, כל ,.. ]

B0Token: על, B0_LastThreeLetters: �ל, B0_LastTwoLetters: ל, B1Token: ידי, B1_LastThreeLetters: �י, B1_LastTwoLetters: י, S0B0Token: שהוטל_על, S0B1Token: שהוטל_ידי, S0B2Token: שהוטל_כל, S0Token: שהוטל, S0_LastThreeLetters: �ל, S0_LastTwoLetters: ל, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

36- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [על, ידי, כל ,.. ]

B0Token: על, B0_LastThreeLetters: �ל, B0_LastTwoLetters: ל, B1Token: ידי, B1_LastThreeLetters: �י, B1_LastTwoLetters: י, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

37- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [על]   B= [ידי, כל, גורם ,.. ]

B0Token: ידי, B0_LastThreeLetters: �י, B0_LastTwoLetters: י, B1Token: כל, B1_LastThreeLetters: �ל, B1_LastTwoLetters: ל, S0B0Token: על_ידי, S0B1Token: על_כל, S0B2Token: על_גורם, S0Token: על, S0_LastThreeLetters: �ל, S0_LastTwoLetters: ל, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

38- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ידי, כל, גורם ,.. ]

B0Token: ידי, B0_LastThreeLetters: �י, B0_LastTwoLetters: י, B1Token: כל, B1_LastThreeLetters: �ל, B1_LastTwoLetters: ל, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

39- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ידי]   B= [כל, גורם, שהוא ,.. ]

B0Token: כל, B0_LastThreeLetters: �ל, B0_LastTwoLetters: ל, B1Token: גורם, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, S0B0Token: ידי_כל, S0B1Token: ידי_גורם, S0B2Token: ידי_שהוא, S0Token: ידי, S0_LastThreeLetters: �י, S0_LastTwoLetters: י, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

40- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [כל, גורם, שהוא ,.. ]

B0Token: כל, B0_LastThreeLetters: �ל, B0_LastTwoLetters: ל, B1Token: גורם, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

41- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [כל]   B= [גורם, שהוא, כך ,.. ]

B0Token: גורם, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, B1Token: שהוא, B1_LastThreeLetters: �א, B1_LastTwoLetters: א, S0B0Token: כל_גורם, S0B1Token: כל_שהוא, S0B2Token: כל_כך, S0Token: כל, S0_LastThreeLetters: �ל, S0_LastTwoLetters: ל, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

42- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [גורם, שהוא, כך ,.. ]

B0Token: גורם, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, B1Token: שהוא, B1_LastThreeLetters: �א, B1_LastTwoLetters: א, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

43- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [גורם]   B= [שהוא, כך, קובעת ,.. ]

B0Token: שהוא, B0_LastThreeLetters: �א, B0_LastTwoLetters: א, B1Token: כך, B1_LastThreeLetters: �ך, B1_LastTwoLetters: ך, S0B0Token: גורם_שהוא, S0B1Token: גורם_כך, S0B2Token: גורם_קובעת, S0Token: גורם, S0_LastThreeLetters: �ם, S0_LastTwoLetters: ם, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

44- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [שהוא, כך, קובעת ,.. ]

B0Token: שהוא, B0_LastThreeLetters: �א, B0_LastTwoLetters: א, B1Token: כך, B1_LastThreeLetters: �ך, B1_LastTwoLetters: ך, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

45- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [שהוא]   B= [כך, קובעת, הצעת ,.. ]

B0Token: כך, B0_LastThreeLetters: �ך, B0_LastTwoLetters: ך, B1Token: קובעת, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, S0B0Token: שהוא_כך, S0B1Token: שהוא_קובעת, S0B2Token: שהוא_הצעת, S0Token: שהוא, S0_LastThreeLetters: �א, S0_LastTwoLetters: א, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

46- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [כך, קובעת, הצעת ,.. ]

B0Token: כך, B0_LastThreeLetters: �ך, B0_LastTwoLetters: ך, B1Token: קובעת, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

47- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [כך]   B= [קובעת, הצעת, חוק ,.. ]

B0Token: קובעת, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: הצעת, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, S0B0Token: כך_קובעת, S0B1Token: כך_הצעת, S0B2Token: כך_חוק, S0Token: כך, S0_LastThreeLetters: �ך, S0_LastTwoLetters: ך, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

48- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [קובעת, הצעת, חוק ,.. ]

B0Token: קובעת, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: הצעת, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

49- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [קובעת]   B= [הצעת, חוק, שהונחה ,.. ]

B0Token: הצעת, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: חוק, B1_LastThreeLetters: �ק, B1_LastTwoLetters: ק, S0B0Token: קובעת_הצעת, S0B1Token: קובעת_חוק, S0B2Token: קובעת_שהונחה, S0Token: קובעת, S0_LastThreeLetters: �ת, S0_LastTwoLetters: ת, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

50- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [הצעת, חוק, שהונחה ,.. ]

B0Token: הצעת, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: חוק, B1_LastThreeLetters: �ק, B1_LastTwoLetters: ק, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

51- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [הצעת]   B= [חוק, שהונחה, על ,.. ]

B0Token: חוק, B0_LastThreeLetters: �ק, B0_LastTwoLetters: ק, B1Token: שהונחה, B1_LastThreeLetters: �ה, B1_LastTwoLetters: ה, S0B0Token: הצעת_חוק, S0B1Token: הצעת_שהונחה, S0B2Token: הצעת_על, S0Token: הצעת, S0_LastThreeLetters: �ת, S0_LastTwoLetters: ת, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

52- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [חוק, שהונחה, על ,.. ]

B0Token: חוק, B0_LastThreeLetters: �ק, B0_LastTwoLetters: ק, B1Token: שהונחה, B1_LastThreeLetters: �ה, B1_LastTwoLetters: ה, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

53- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [חוק]   B= [שהונחה, על, שולחן ,.. ]

B0Token: שהונחה, B0_LastThreeLetters: �ה, B0_LastTwoLetters: ה, B1Token: על, B1_LastThreeLetters: �ל, B1_LastTwoLetters: ל, S0B0Token: חוק_שהונחה, S0B1Token: חוק_על, S0B2Token: חוק_שולחן, S0Token: חוק, S0_LastThreeLetters: �ק, S0_LastTwoLetters: ק, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

54- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [שהונחה, על, שולחן ,.. ]

B0Token: שהונחה, B0_LastThreeLetters: �ה, B0_LastTwoLetters: ה, B1Token: על, B1_LastThreeLetters: �ל, B1_LastTwoLetters: ל, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

55- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [שהונחה]   B= [על, שולחן, הכנסת ,.. ]

B0Token: על, B0_LastThreeLetters: �ל, B0_LastTwoLetters: ל, B1Token: שולחן, B1_LastThreeLetters: �ן, B1_LastTwoLetters: ן, S0B0Token: שהונחה_על, S0B1Token: שהונחה_שולחן, S0B2Token: שהונחה_הכנסת, S0Token: שהונחה, S0_LastThreeLetters: �ה, S0_LastTwoLetters: ה, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

56- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [שהונחה, על]   B= [שולחן, הכנסת, ועיקרה ,.. ]

B0Token: שולחן, B0_LastThreeLetters: �ן, B0_LastTwoLetters: ן, B1Token: הכנסת, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, S0B0Token: על_שולחן, S0B1Token: על_הכנסת, S0B2Token: על_ועיקרה, S0Token: על, S0_LastThreeLetters: �ל, S0_LastTwoLetters: ל, S1B0Token: שהונחה_שולחן, S1S0Token: שהונחה_על, S1Token: שהונחה, S1_LastThreeLetters: �ה, S1_LastTwoLetters: ה, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

57- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [שהונחה, על, שולחן]   B= [הכנסת, ועיקרה, מאבק ,.. ]

B0Token: הכנסת, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: ועיקרה, B1_LastThreeLetters: �ה, B1_LastTwoLetters: ה, S0B0Token: שולחן_הכנסת, S0B1Token: שולחן_ועיקרה, S0B2Token: שולחן_מאבק, S0Token: שולחן, S0_LastThreeLetters: �ן, S0_LastTwoLetters: ן, S1B0Token: על_הכנסת, S1S0Token: על_שולחן, S1Token: על, S1_LastThreeLetters: �ל, S1_LastTwoLetters: ל, transitionHistoryLength1: 0, transitionHistoryLength2: 00, transitionHistoryLength3: 002, 

58- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [שהונחה, [על, שולחן]]   B= [הכנסת, ועיקרה, מאבק ,.. ]

B0Token: הכנסת, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: ועיקרה, B1_LastThreeLetters: �ה, B1_LastTwoLetters: ה, S0B0Token: על_שולחן_הכנסת, S0B1Token: על_שולחן_ועיקרה, S0B2Token: על_שולחן_מאבק, S0Token: על_שולחן, S1B0Token: שהונחה_הכנסת, S1S0Token: שהונחה_על_שולחן, S1Token: שהונחה, S1_LastThreeLetters: �ה, S1_LastTwoLetters: ה, transitionHistoryLength1: 0, transitionHistoryLength2: 00, transitionHistoryLength3: 000, 

59- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[שהונחה, [על, שולחן]]]   B= [הכנסת, ועיקרה, מאבק ,.. ]

B0Token: הכנסת, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: ועיקרה, B1_LastThreeLetters: �ה, B1_LastTwoLetters: ה, S0B0Token: שהונחה_על_שולחן_הכנסת, S0B1Token: שהונחה_על_שולחן_ועיקרה, S0B2Token: שהונחה_על_שולחן_מאבק, S0Token: שהונחה_על_שולחן, transitionHistoryLength1: 1, transitionHistoryLength2: 10, transitionHistoryLength3: 100, 

60- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [הכנסת, ועיקרה, מאבק ,.. ]

B0Token: הכנסת, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: ועיקרה, B1_LastThreeLetters: �ה, B1_LastTwoLetters: ה, transitionHistoryLength1: 1, transitionHistoryLength2: 11, transitionHistoryLength3: 110, 

61- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [הכנסת]   B= [ועיקרה, מאבק, בחרמות ,.. ]

B0Token: ועיקרה, B0_LastThreeLetters: �ה, B0_LastTwoLetters: ה, B1Token: מאבק, B1_LastThreeLetters: �ק, B1_LastTwoLetters: ק, S0B0Token: הכנסת_ועיקרה, S0B1Token: הכנסת_מאבק, S0B2Token: הכנסת_בחרמות, S0Token: הכנסת, S0_LastThreeLetters: �ת, S0_LastTwoLetters: ת, transitionHistoryLength1: 2, transitionHistoryLength2: 21, transitionHistoryLength3: 211, 

62- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ועיקרה, מאבק, בחרמות ,.. ]

B0Token: ועיקרה, B0_LastThreeLetters: �ה, B0_LastTwoLetters: ה, B1Token: מאבק, B1_LastThreeLetters: �ק, B1_LastTwoLetters: ק, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 021, 

63- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ועיקרה]   B= [מאבק, בחרמות ,.. ]

B0Token: מאבק, B0_LastThreeLetters: �ק, B0_LastTwoLetters: ק, B1Token: בחרמות, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, S0B0Token: ועיקרה_מאבק, S0B1Token: ועיקרה_בחרמות, S0Token: ועיקרה, S0_LastThreeLetters: �ה, S0_LastTwoLetters: ה, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

64- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [מאבק, בחרמות ,.. ]

B0Token: מאבק, B0_LastThreeLetters: �ק, B0_LastTwoLetters: ק, B1Token: בחרמות, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

65- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [מאבק]   B= [בחרמות]

B0Token: בחרמות, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, S0B0Token: מאבק_בחרמות, S0Token: מאבק, S0_LastThreeLetters: �ק, S0_LastTwoLetters: ק, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

66- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [בחרמות]

B0Token: בחרמות, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

67- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [בחרמות]   B= [ ]

S0Token: בחרמות, S0_LastThreeLetters: �ת, S0_LastTwoLetters: ת, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

68- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

## Sentence No. 1303 - 
עתה מתקרבים לשעת הכרעה שבה רק מסירות של ציבור גדול תוכל לחולל את השינוי כך אומר ראש מועצת הר חברון וחבר הנהלת מועצת יש " ע בר חי בראיון לערוץ 7 ביום שאחרי ההפגנה
### Existing MWEs: 
1- **מתקרבים לשעת הכרעה** (VPC)
2- **לחולל השינוי** (LVC)



0- &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [עתה, מתקרבים, לשעת ,.. ]

B0Token: עתה, B0_LastThreeLetters: �ה, B0_LastTwoLetters: ה, B1Token: מתקרבים, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, 

1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [עתה]   B= [מתקרבים, לשעת, הכרעה ,.. ]

B0Token: מתקרבים, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, B1Token: לשעת, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, S0B0Token: עתה_מתקרבים, S0B1Token: עתה_לשעת, S0B2Token: עתה_הכרעה, S0Token: עתה, S0_LastThreeLetters: �ה, S0_LastTwoLetters: ה, 

2- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [מתקרבים, לשעת, הכרעה ,.. ]

B0Token: מתקרבים, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, B1Token: לשעת, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, transitionHistoryLength1: 0, 

3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [מתקרבים]   B= [לשעת, הכרעה, שבה ,.. ]

B0Token: לשעת, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: הכרעה, B1_LastThreeLetters: �ה, B1_LastTwoLetters: ה, S0B0Token: מתקרבים_לשעת, S0B1Token: מתקרבים_הכרעה, S0B2Token: מתקרבים_שבה, S0Token: מתקרבים, S0_LastThreeLetters: �ם, S0_LastTwoLetters: ם, transitionHistoryLength1: 2, transitionHistoryLength2: 20, 

4- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [מתקרבים, לשעת]   B= [הכרעה, שבה, רק ,.. ]

B0Token: הכרעה, B0_LastThreeLetters: �ה, B0_LastTwoLetters: ה, B1Token: שבה, B1_LastThreeLetters: �ה, B1_LastTwoLetters: ה, S0B0Token: לשעת_הכרעה, S0B1Token: לשעת_שבה, S0B2Token: לשעת_רק, S0Token: לשעת, S0_LastThreeLetters: �ת, S0_LastTwoLetters: ת, S1B0Token: מתקרבים_הכרעה, S1S0Token: מתקרבים_לשעת, S1Token: מתקרבים, S1_LastThreeLetters: �ם, S1_LastTwoLetters: ם, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [מתקרבים, לשעת, הכרעה]   B= [שבה, רק, מסירות ,.. ]

B0Token: שבה, B0_LastThreeLetters: �ה, B0_LastTwoLetters: ה, B1Token: רק, B1_LastThreeLetters: �ק, B1_LastTwoLetters: ק, S0B0Token: הכרעה_שבה, S0B1Token: הכרעה_רק, S0B2Token: הכרעה_מסירות, S0Token: הכרעה, S0_LastThreeLetters: �ה, S0_LastTwoLetters: ה, S1B0Token: לשעת_שבה, S1S0Token: לשעת_הכרעה, S1Token: לשעת, S1_LastThreeLetters: �ת, S1_LastTwoLetters: ת, transitionHistoryLength1: 0, transitionHistoryLength2: 00, transitionHistoryLength3: 002, 

6- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [מתקרבים, [לשעת, הכרעה]]   B= [שבה, רק, מסירות ,.. ]

B0Token: שבה, B0_LastThreeLetters: �ה, B0_LastTwoLetters: ה, B1Token: רק, B1_LastThreeLetters: �ק, B1_LastTwoLetters: ק, S0B0Token: לשעת_הכרעה_שבה, S0B1Token: לשעת_הכרעה_רק, S0B2Token: לשעת_הכרעה_מסירות, S0Token: לשעת_הכרעה, S1B0Token: מתקרבים_שבה, S1S0Token: מתקרבים_לשעת_הכרעה, S1Token: מתקרבים, S1_LastThreeLetters: �ם, S1_LastTwoLetters: ם, transitionHistoryLength1: 0, transitionHistoryLength2: 00, transitionHistoryLength3: 000, 

7- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[מתקרבים, [לשעת, הכרעה]]]   B= [שבה, רק, מסירות ,.. ]

B0Token: שבה, B0_LastThreeLetters: �ה, B0_LastTwoLetters: ה, B1Token: רק, B1_LastThreeLetters: �ק, B1_LastTwoLetters: ק, S0B0Token: מתקרבים_לשעת_הכרעה_שבה, S0B1Token: מתקרבים_לשעת_הכרעה_רק, S0B2Token: מתקרבים_לשעת_הכרעה_מסירות, S0Token: מתקרבים_לשעת_הכרעה, transitionHistoryLength1: 1, transitionHistoryLength2: 10, transitionHistoryLength3: 100, 

8- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [שבה, רק, מסירות ,.. ]

B0Token: שבה, B0_LastThreeLetters: �ה, B0_LastTwoLetters: ה, B1Token: רק, B1_LastThreeLetters: �ק, B1_LastTwoLetters: ק, transitionHistoryLength1: 1, transitionHistoryLength2: 11, transitionHistoryLength3: 110, 

9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [שבה]   B= [רק, מסירות, של ,.. ]

B0Token: רק, B0_LastThreeLetters: �ק, B0_LastTwoLetters: ק, B1Token: מסירות, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, S0B0Token: שבה_רק, S0B1Token: שבה_מסירות, S0B2Token: שבה_של, S0Token: שבה, S0_LastThreeLetters: �ה, S0_LastTwoLetters: ה, transitionHistoryLength1: 2, transitionHistoryLength2: 21, transitionHistoryLength3: 211, 

10- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [רק, מסירות, של ,.. ]

B0Token: רק, B0_LastThreeLetters: �ק, B0_LastTwoLetters: ק, B1Token: מסירות, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 021, 

11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [רק]   B= [מסירות, של, ציבור ,.. ]

B0Token: מסירות, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: של, B1_LastThreeLetters: �ל, B1_LastTwoLetters: ל, S0B0Token: רק_מסירות, S0B1Token: רק_של, S0B2Token: רק_ציבור, S0Token: רק, S0_LastThreeLetters: �ק, S0_LastTwoLetters: ק, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

12- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [מסירות, של, ציבור ,.. ]

B0Token: מסירות, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: של, B1_LastThreeLetters: �ל, B1_LastTwoLetters: ל, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [מסירות]   B= [של, ציבור, גדול ,.. ]

B0Token: של, B0_LastThreeLetters: �ל, B0_LastTwoLetters: ל, B1Token: ציבור, B1_LastThreeLetters: �ר, B1_LastTwoLetters: ר, S0B0Token: מסירות_של, S0B1Token: מסירות_ציבור, S0B2Token: מסירות_גדול, S0Token: מסירות, S0_LastThreeLetters: �ת, S0_LastTwoLetters: ת, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

14- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [של, ציבור, גדול ,.. ]

B0Token: של, B0_LastThreeLetters: �ל, B0_LastTwoLetters: ל, B1Token: ציבור, B1_LastThreeLetters: �ר, B1_LastTwoLetters: ר, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [של]   B= [ציבור, גדול, תוכל ,.. ]

B0Token: ציבור, B0_LastThreeLetters: �ר, B0_LastTwoLetters: ר, B1Token: גדול, B1_LastThreeLetters: �ל, B1_LastTwoLetters: ל, S0B0Token: של_ציבור, S0B1Token: של_גדול, S0B2Token: של_תוכל, S0Token: של, S0_LastThreeLetters: �ל, S0_LastTwoLetters: ל, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

16- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ציבור, גדול, תוכל ,.. ]

B0Token: ציבור, B0_LastThreeLetters: �ר, B0_LastTwoLetters: ר, B1Token: גדול, B1_LastThreeLetters: �ל, B1_LastTwoLetters: ל, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ציבור]   B= [גדול, תוכל, לחולל ,.. ]

B0Token: גדול, B0_LastThreeLetters: �ל, B0_LastTwoLetters: ל, B1Token: תוכל, B1_LastThreeLetters: �ל, B1_LastTwoLetters: ל, S0B0Token: ציבור_גדול, S0B1Token: ציבור_תוכל, S0B2Token: ציבור_לחולל, S0Token: ציבור, S0_LastThreeLetters: �ר, S0_LastTwoLetters: ר, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

18- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [גדול, תוכל, לחולל ,.. ]

B0Token: גדול, B0_LastThreeLetters: �ל, B0_LastTwoLetters: ל, B1Token: תוכל, B1_LastThreeLetters: �ל, B1_LastTwoLetters: ל, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [גדול]   B= [תוכל, לחולל, את ,.. ]

B0Token: תוכל, B0_LastThreeLetters: �ל, B0_LastTwoLetters: ל, B1Token: לחולל, B1_LastThreeLetters: �ל, B1_LastTwoLetters: ל, S0B0Token: גדול_תוכל, S0B1Token: גדול_לחולל, S0B2Token: גדול_את, S0Token: גדול, S0_LastThreeLetters: �ל, S0_LastTwoLetters: ל, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

20- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [תוכל, לחולל, את ,.. ]

B0Token: תוכל, B0_LastThreeLetters: �ל, B0_LastTwoLetters: ל, B1Token: לחולל, B1_LastThreeLetters: �ל, B1_LastTwoLetters: ל, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [תוכל]   B= [לחולל, את, השינוי ,.. ]

B0Token: לחולל, B0_LastThreeLetters: �ל, B0_LastTwoLetters: ל, B1Token: את, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, S0B0Token: תוכל_לחולל, S0B1Token: תוכל_את, S0B2Token: תוכל_השינוי, S0Token: תוכל, S0_LastThreeLetters: �ל, S0_LastTwoLetters: ל, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

22- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [לחולל, את, השינוי ,.. ]

B0Token: לחולל, B0_LastThreeLetters: �ל, B0_LastTwoLetters: ל, B1Token: את, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

23- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [לחולל]   B= [את, השינוי, כך ,.. ]

B0Token: את, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: השינוי, B1_LastThreeLetters: �י, B1_LastTwoLetters: י, S0B0Token: לחולל_את, S0B1Token: לחולל_השינוי, S0B2Token: לחולל_כך, S0Token: לחולל, S0_LastThreeLetters: �ל, S0_LastTwoLetters: ל, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

24- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [לחולל, את]   B= [השינוי, כך, אומר ,.. ]

B0Token: השינוי, B0_LastThreeLetters: �י, B0_LastTwoLetters: י, B1Token: כך, B1_LastThreeLetters: �ך, B1_LastTwoLetters: ך, S0B0Token: את_השינוי, S0B1Token: את_כך, S0B2Token: את_אומר, S0Token: את, S0_LastThreeLetters: �ת, S0_LastTwoLetters: ת, S1B0Token: לחולל_השינוי, S1S0Token: לחולל_את, S1Token: לחולל, S1_LastThreeLetters: �ל, S1_LastTwoLetters: ל, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

25- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [לחולל]   B= [השינוי, כך, אומר ,.. ]

B0Token: השינוי, B0_LastThreeLetters: �י, B0_LastTwoLetters: י, B1Token: כך, B1_LastThreeLetters: �ך, B1_LastTwoLetters: ך, S0B0Token: לחולל_השינוי, S0B1Token: לחולל_כך, S0B2Token: לחולל_אומר, S0Token: לחולל, S0_LastThreeLetters: �ל, S0_LastTwoLetters: ל, transitionHistoryLength1: 0, transitionHistoryLength2: 00, transitionHistoryLength3: 002, 

26- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [לחולל, השינוי]   B= [כך, אומר, ראש ,.. ]

B0Token: כך, B0_LastThreeLetters: �ך, B0_LastTwoLetters: ך, B1Token: אומר, B1_LastThreeLetters: �ר, B1_LastTwoLetters: ר, S0B0Token: השינוי_כך, S0B1Token: השינוי_אומר, S0B2Token: השינוי_ראש, S0Token: השינוי, S0_LastThreeLetters: �י, S0_LastTwoLetters: י, S1B0Token: לחולל_כך, S1S0Token: לחולל_השינוי, S1Token: לחולל, S1_LastThreeLetters: �ל, S1_LastTwoLetters: ל, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 200, 

27- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[לחולל, השינוי]]   B= [כך, אומר, ראש ,.. ]

B0Token: כך, B0_LastThreeLetters: �ך, B0_LastTwoLetters: ך, B1Token: אומר, B1_LastThreeLetters: �ר, B1_LastTwoLetters: ר, S0B0Token: לחולל_השינוי_כך, S0B1Token: לחולל_השינוי_אומר, S0B2Token: לחולל_השינוי_ראש, S0Token: לחולל_השינוי, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

28- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [כך, אומר, ראש ,.. ]

B0Token: כך, B0_LastThreeLetters: �ך, B0_LastTwoLetters: ך, B1Token: אומר, B1_LastThreeLetters: �ר, B1_LastTwoLetters: ר, transitionHistoryLength1: 1, transitionHistoryLength2: 10, transitionHistoryLength3: 102, 

29- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [כך]   B= [אומר, ראש, מועצת ,.. ]

B0Token: אומר, B0_LastThreeLetters: �ר, B0_LastTwoLetters: ר, B1Token: ראש, B1_LastThreeLetters: �ש, B1_LastTwoLetters: ש, S0B0Token: כך_אומר, S0B1Token: כך_ראש, S0B2Token: כך_מועצת, S0Token: כך, S0_LastThreeLetters: �ך, S0_LastTwoLetters: ך, transitionHistoryLength1: 2, transitionHistoryLength2: 21, transitionHistoryLength3: 210, 

30- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [אומר, ראש, מועצת ,.. ]

B0Token: אומר, B0_LastThreeLetters: �ר, B0_LastTwoLetters: ר, B1Token: ראש, B1_LastThreeLetters: �ש, B1_LastTwoLetters: ש, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 021, 

31- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [אומר]   B= [ראש, מועצת, הר ,.. ]

B0Token: ראש, B0_LastThreeLetters: �ש, B0_LastTwoLetters: ש, B1Token: מועצת, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, S0B0Token: אומר_ראש, S0B1Token: אומר_מועצת, S0B2Token: אומר_הר, S0Token: אומר, S0_LastThreeLetters: �ר, S0_LastTwoLetters: ר, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

32- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ראש, מועצת, הר ,.. ]

B0Token: ראש, B0_LastThreeLetters: �ש, B0_LastTwoLetters: ש, B1Token: מועצת, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

33- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ראש]   B= [מועצת, הר, חברון ,.. ]

B0Token: מועצת, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: הר, B1_LastThreeLetters: �ר, B1_LastTwoLetters: ר, S0B0Token: ראש_מועצת, S0B1Token: ראש_הר, S0B2Token: ראש_חברון, S0Token: ראש, S0_LastThreeLetters: �ש, S0_LastTwoLetters: ש, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

34- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [מועצת, הר, חברון ,.. ]

B0Token: מועצת, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: הר, B1_LastThreeLetters: �ר, B1_LastTwoLetters: ר, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

35- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [מועצת]   B= [הר, חברון, וחבר ,.. ]

B0Token: הר, B0_LastThreeLetters: �ר, B0_LastTwoLetters: ר, B1Token: חברון, B1_LastThreeLetters: �ן, B1_LastTwoLetters: ן, S0B0Token: מועצת_הר, S0B1Token: מועצת_חברון, S0B2Token: מועצת_וחבר, S0Token: מועצת, S0_LastThreeLetters: �ת, S0_LastTwoLetters: ת, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

36- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [הר, חברון, וחבר ,.. ]

B0Token: הר, B0_LastThreeLetters: �ר, B0_LastTwoLetters: ר, B1Token: חברון, B1_LastThreeLetters: �ן, B1_LastTwoLetters: ן, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

37- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [הר]   B= [חברון, וחבר, הנהלת ,.. ]

B0Token: חברון, B0_LastThreeLetters: �ן, B0_LastTwoLetters: ן, B1Token: וחבר, B1_LastThreeLetters: �ר, B1_LastTwoLetters: ר, S0B0Token: הר_חברון, S0B1Token: הר_וחבר, S0B2Token: הר_הנהלת, S0Token: הר, S0_LastThreeLetters: �ר, S0_LastTwoLetters: ר, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

38- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [חברון, וחבר, הנהלת ,.. ]

B0Token: חברון, B0_LastThreeLetters: �ן, B0_LastTwoLetters: ן, B1Token: וחבר, B1_LastThreeLetters: �ר, B1_LastTwoLetters: ר, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

39- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [חברון]   B= [וחבר, הנהלת, מועצת ,.. ]

B0Token: וחבר, B0_LastThreeLetters: �ר, B0_LastTwoLetters: ר, B1Token: הנהלת, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, S0B0Token: חברון_וחבר, S0B1Token: חברון_הנהלת, S0B2Token: חברון_מועצת, S0Token: חברון, S0_LastThreeLetters: �ן, S0_LastTwoLetters: ן, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

40- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [וחבר, הנהלת, מועצת ,.. ]

B0Token: וחבר, B0_LastThreeLetters: �ר, B0_LastTwoLetters: ר, B1Token: הנהלת, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

41- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [וחבר]   B= [הנהלת, מועצת, יש ,.. ]

B0Token: הנהלת, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: מועצת, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, S0B0Token: וחבר_הנהלת, S0B1Token: וחבר_מועצת, S0B2Token: וחבר_יש, S0Token: וחבר, S0_LastThreeLetters: �ר, S0_LastTwoLetters: ר, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

42- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [הנהלת, מועצת, יש ,.. ]

B0Token: הנהלת, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: מועצת, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

43- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [הנהלת]   B= [מועצת, יש, " ,.. ]

B0Token: מועצת, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: יש, B1_LastThreeLetters: �ש, B1_LastTwoLetters: ש, S0B0Token: הנהלת_מועצת, S0B1Token: הנהלת_יש, S0B2Token: הנהלת_", S0Token: הנהלת, S0_LastThreeLetters: �ת, S0_LastTwoLetters: ת, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

44- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [מועצת, יש, " ,.. ]

B0Token: מועצת, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: יש, B1_LastThreeLetters: �ש, B1_LastTwoLetters: ש, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

45- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [מועצת]   B= [יש, ", ע ,.. ]

B0Token: יש, B0_LastThreeLetters: �ש, B0_LastTwoLetters: ש, B1Token: ", B1_LastThreeLetters: ", B1_LastTwoLetters: ", S0B0Token: מועצת_יש, S0B1Token: מועצת_", S0B2Token: מועצת_ע, S0Token: מועצת, S0_LastThreeLetters: �ת, S0_LastTwoLetters: ת, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

46- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [יש, ", ע ,.. ]

B0Token: יש, B0_LastThreeLetters: �ש, B0_LastTwoLetters: ש, B1Token: ", B1_LastThreeLetters: ", B1_LastTwoLetters: ", transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

47- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [יש]   B= [", ע, בר ,.. ]

B0Token: ", B0_LastThreeLetters: ", B0_LastTwoLetters: ", B1Token: ע, B1_LastThreeLetters: ע, B1_LastTwoLetters: ע, S0B0Token: יש_", S0B1Token: יש_ע, S0B2Token: יש_בר, S0Token: יש, S0_LastThreeLetters: �ש, S0_LastTwoLetters: ש, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

48- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [", ע, בר ,.. ]

B0Token: ", B0_LastThreeLetters: ", B0_LastTwoLetters: ", B1Token: ע, B1_LastThreeLetters: ע, B1_LastTwoLetters: ע, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

49- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= ["]   B= [ע, בר, חי ,.. ]

B0Token: ע, B0_LastThreeLetters: ע, B0_LastTwoLetters: ע, B1Token: בר, B1_LastThreeLetters: �ר, B1_LastTwoLetters: ר, S0B0Token: "_ע, S0B1Token: "_בר, S0B2Token: "_חי, S0Token: ", S0_LastThreeLetters: ", S0_LastTwoLetters: ", transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

50- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ע, בר, חי ,.. ]

B0Token: ע, B0_LastThreeLetters: ע, B0_LastTwoLetters: ע, B1Token: בר, B1_LastThreeLetters: �ר, B1_LastTwoLetters: ר, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

51- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ע]   B= [בר, חי, בראיון ,.. ]

B0Token: בר, B0_LastThreeLetters: �ר, B0_LastTwoLetters: ר, B1Token: חי, B1_LastThreeLetters: �י, B1_LastTwoLetters: י, S0B0Token: ע_בר, S0B1Token: ע_חי, S0B2Token: ע_בראיון, S0Token: ע, S0_LastThreeLetters: ע, S0_LastTwoLetters: ע, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

52- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [בר, חי, בראיון ,.. ]

B0Token: בר, B0_LastThreeLetters: �ר, B0_LastTwoLetters: ר, B1Token: חי, B1_LastThreeLetters: �י, B1_LastTwoLetters: י, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

53- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [בר]   B= [חי, בראיון, לערוץ ,.. ]

B0Token: חי, B0_LastThreeLetters: �י, B0_LastTwoLetters: י, B1Token: בראיון, B1_LastThreeLetters: �ן, B1_LastTwoLetters: ן, S0B0Token: בר_חי, S0B1Token: בר_בראיון, S0B2Token: בר_לערוץ, S0Token: בר, S0_LastThreeLetters: �ר, S0_LastTwoLetters: ר, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

54- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [חי, בראיון, לערוץ ,.. ]

B0Token: חי, B0_LastThreeLetters: �י, B0_LastTwoLetters: י, B1Token: בראיון, B1_LastThreeLetters: �ן, B1_LastTwoLetters: ן, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

55- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [חי]   B= [בראיון, לערוץ, 7 ,.. ]

B0Token: בראיון, B0_LastThreeLetters: �ן, B0_LastTwoLetters: ן, B1Token: לערוץ, B1_LastThreeLetters: �ץ, B1_LastTwoLetters: ץ, S0B0Token: חי_בראיון, S0B1Token: חי_לערוץ, S0B2Token: חי_7, S0Token: חי, S0_LastThreeLetters: �י, S0_LastTwoLetters: י, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

56- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [בראיון, לערוץ, 7 ,.. ]

B0Token: בראיון, B0_LastThreeLetters: �ן, B0_LastTwoLetters: ן, B1Token: לערוץ, B1_LastThreeLetters: �ץ, B1_LastTwoLetters: ץ, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

57- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [בראיון]   B= [לערוץ, 7, ביום ,.. ]

B0Token: לערוץ, B0_LastThreeLetters: �ץ, B0_LastTwoLetters: ץ, B1Token: 7, B1_LastThreeLetters: 7, B1_LastTwoLetters: 7, S0B0Token: בראיון_לערוץ, S0B1Token: בראיון_7, S0B2Token: בראיון_ביום, S0Token: בראיון, S0_LastThreeLetters: �ן, S0_LastTwoLetters: ן, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

58- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [לערוץ, 7, ביום ,.. ]

B0Token: לערוץ, B0_LastThreeLetters: �ץ, B0_LastTwoLetters: ץ, B1Token: 7, B1_LastThreeLetters: 7, B1_LastTwoLetters: 7, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

59- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [לערוץ]   B= [7, ביום, שאחרי ,.. ]

B0Token: 7, B0_LastThreeLetters: 7, B0_LastTwoLetters: 7, B1Token: ביום, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, S0B0Token: לערוץ_7, S0B1Token: לערוץ_ביום, S0B2Token: לערוץ_שאחרי, S0Token: לערוץ, S0_LastThreeLetters: �ץ, S0_LastTwoLetters: ץ, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

60- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [7, ביום, שאחרי ,.. ]

B0Token: 7, B0_LastThreeLetters: 7, B0_LastTwoLetters: 7, B1Token: ביום, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

61- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [7]   B= [ביום, שאחרי, ההפגנה ,.. ]

B0Token: ביום, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, B1Token: שאחרי, B1_LastThreeLetters: �י, B1_LastTwoLetters: י, S0B0Token: 7_ביום, S0B1Token: 7_שאחרי, S0B2Token: 7_ההפגנה, S0Token: 7, S0_LastThreeLetters: 7, S0_LastTwoLetters: 7, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

62- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ביום, שאחרי, ההפגנה ,.. ]

B0Token: ביום, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, B1Token: שאחרי, B1_LastThreeLetters: �י, B1_LastTwoLetters: י, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

63- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ביום]   B= [שאחרי, ההפגנה ,.. ]

B0Token: שאחרי, B0_LastThreeLetters: �י, B0_LastTwoLetters: י, B1Token: ההפגנה, B1_LastThreeLetters: �ה, B1_LastTwoLetters: ה, S0B0Token: ביום_שאחרי, S0B1Token: ביום_ההפגנה, S0Token: ביום, S0_LastThreeLetters: �ם, S0_LastTwoLetters: ם, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

64- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [שאחרי, ההפגנה ,.. ]

B0Token: שאחרי, B0_LastThreeLetters: �י, B0_LastTwoLetters: י, B1Token: ההפגנה, B1_LastThreeLetters: �ה, B1_LastTwoLetters: ה, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

65- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [שאחרי]   B= [ההפגנה]

B0Token: ההפגנה, B0_LastThreeLetters: �ה, B0_LastTwoLetters: ה, S0B0Token: שאחרי_ההפגנה, S0Token: שאחרי, S0_LastThreeLetters: �י, S0_LastTwoLetters: י, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

66- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ההפגנה]

B0Token: ההפגנה, B0_LastThreeLetters: �ה, B0_LastTwoLetters: ה, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

67- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ההפגנה]   B= [ ]

S0Token: ההפגנה, S0_LastThreeLetters: �ה, S0_LastTwoLetters: ה, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

68- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

## Sentence No. 1338 - 
פינס אמר כי האופן החד צדדי בו התקבלו ההחלטות ללא מעורבות הציבור מהווה כישלון חרוץ שאין לו אח ורע בשום מקום בעולם
### Existing MWEs: 
1- **מהווה כישלון חרוץ** (OTH)
2- **מהווה כישלון חרוץ שאין לו אח ורע** (OTH), Interleaving 



0- &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [פינס, אמר, כי ,.. ]

B0Token: פינס, B0_LastThreeLetters: �ס, B0_LastTwoLetters: ס, B1Token: אמר, B1_LastThreeLetters: �ר, B1_LastTwoLetters: ר, 

1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [פינס]   B= [אמר, כי, האופן ,.. ]

B0Token: אמר, B0_LastThreeLetters: �ר, B0_LastTwoLetters: ר, B1Token: כי, B1_LastThreeLetters: �י, B1_LastTwoLetters: י, S0B0Token: פינס_אמר, S0B1Token: פינס_כי, S0B2Token: פינס_האופן, S0Token: פינס, S0_LastThreeLetters: �ס, S0_LastTwoLetters: ס, 

2- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [אמר, כי, האופן ,.. ]

B0Token: אמר, B0_LastThreeLetters: �ר, B0_LastTwoLetters: ר, B1Token: כי, B1_LastThreeLetters: �י, B1_LastTwoLetters: י, transitionHistoryLength1: 0, 

3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [אמר]   B= [כי, האופן, החד ,.. ]

B0Token: כי, B0_LastThreeLetters: �י, B0_LastTwoLetters: י, B1Token: האופן, B1_LastThreeLetters: �ן, B1_LastTwoLetters: ן, S0B0Token: אמר_כי, S0B1Token: אמר_האופן, S0B2Token: אמר_החד, S0Token: אמר, S0_LastThreeLetters: �ר, S0_LastTwoLetters: ר, transitionHistoryLength1: 2, transitionHistoryLength2: 20, 

4- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [כי, האופן, החד ,.. ]

B0Token: כי, B0_LastThreeLetters: �י, B0_LastTwoLetters: י, B1Token: האופן, B1_LastThreeLetters: �ן, B1_LastTwoLetters: ן, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [כי]   B= [האופן, החד, צדדי ,.. ]

B0Token: האופן, B0_LastThreeLetters: �ן, B0_LastTwoLetters: ן, B1Token: החד, B1_LastThreeLetters: �ד, B1_LastTwoLetters: ד, S0B0Token: כי_האופן, S0B1Token: כי_החד, S0B2Token: כי_צדדי, S0Token: כי, S0_LastThreeLetters: �י, S0_LastTwoLetters: י, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

6- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [האופן, החד, צדדי ,.. ]

B0Token: האופן, B0_LastThreeLetters: �ן, B0_LastTwoLetters: ן, B1Token: החד, B1_LastThreeLetters: �ד, B1_LastTwoLetters: ד, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [האופן]   B= [החד, צדדי, בו ,.. ]

B0Token: החד, B0_LastThreeLetters: �ד, B0_LastTwoLetters: ד, B1Token: צדדי, B1_LastThreeLetters: �י, B1_LastTwoLetters: י, S0B0Token: האופן_החד, S0B1Token: האופן_צדדי, S0B2Token: האופן_בו, S0Token: האופן, S0_LastThreeLetters: �ן, S0_LastTwoLetters: ן, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

8- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [החד, צדדי, בו ,.. ]

B0Token: החד, B0_LastThreeLetters: �ד, B0_LastTwoLetters: ד, B1Token: צדדי, B1_LastThreeLetters: �י, B1_LastTwoLetters: י, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [החד]   B= [צדדי, בו, התקבלו ,.. ]

B0Token: צדדי, B0_LastThreeLetters: �י, B0_LastTwoLetters: י, B1Token: בו, B1_LastThreeLetters: �ו, B1_LastTwoLetters: ו, S0B0Token: החד_צדדי, S0B1Token: החד_בו, S0B2Token: החד_התקבלו, S0Token: החד, S0_LastThreeLetters: �ד, S0_LastTwoLetters: ד, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

10- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [צדדי, בו, התקבלו ,.. ]

B0Token: צדדי, B0_LastThreeLetters: �י, B0_LastTwoLetters: י, B1Token: בו, B1_LastThreeLetters: �ו, B1_LastTwoLetters: ו, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [צדדי]   B= [בו, התקבלו, ההחלטות ,.. ]

B0Token: בו, B0_LastThreeLetters: �ו, B0_LastTwoLetters: ו, B1Token: התקבלו, B1_LastThreeLetters: �ו, B1_LastTwoLetters: ו, S0B0Token: צדדי_בו, S0B1Token: צדדי_התקבלו, S0B2Token: צדדי_ההחלטות, S0Token: צדדי, S0_LastThreeLetters: �י, S0_LastTwoLetters: י, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

12- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [בו, התקבלו, ההחלטות ,.. ]

B0Token: בו, B0_LastThreeLetters: �ו, B0_LastTwoLetters: ו, B1Token: התקבלו, B1_LastThreeLetters: �ו, B1_LastTwoLetters: ו, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [בו]   B= [התקבלו, ההחלטות, ללא ,.. ]

B0Token: התקבלו, B0_LastThreeLetters: �ו, B0_LastTwoLetters: ו, B1Token: ההחלטות, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, S0B0Token: בו_התקבלו, S0B1Token: בו_ההחלטות, S0B2Token: בו_ללא, S0Token: בו, S0_LastThreeLetters: �ו, S0_LastTwoLetters: ו, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

14- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [התקבלו, ההחלטות, ללא ,.. ]

B0Token: התקבלו, B0_LastThreeLetters: �ו, B0_LastTwoLetters: ו, B1Token: ההחלטות, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [התקבלו]   B= [ההחלטות, ללא, מעורבות ,.. ]

B0Token: ההחלטות, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: ללא, B1_LastThreeLetters: �א, B1_LastTwoLetters: א, S0B0Token: התקבלו_ההחלטות, S0B1Token: התקבלו_ללא, S0B2Token: התקבלו_מעורבות, S0Token: התקבלו, S0_LastThreeLetters: �ו, S0_LastTwoLetters: ו, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

16- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ההחלטות, ללא, מעורבות ,.. ]

B0Token: ההחלטות, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: ללא, B1_LastThreeLetters: �א, B1_LastTwoLetters: א, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ההחלטות]   B= [ללא, מעורבות, הציבור ,.. ]

B0Token: ללא, B0_LastThreeLetters: �א, B0_LastTwoLetters: א, B1Token: מעורבות, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, S0B0Token: ההחלטות_ללא, S0B1Token: ההחלטות_מעורבות, S0B2Token: ההחלטות_הציבור, S0Token: ההחלטות, S0_LastThreeLetters: �ת, S0_LastTwoLetters: ת, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

18- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ללא, מעורבות, הציבור ,.. ]

B0Token: ללא, B0_LastThreeLetters: �א, B0_LastTwoLetters: א, B1Token: מעורבות, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ללא]   B= [מעורבות, הציבור, מהווה ,.. ]

B0Token: מעורבות, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: הציבור, B1_LastThreeLetters: �ר, B1_LastTwoLetters: ר, S0B0Token: ללא_מעורבות, S0B1Token: ללא_הציבור, S0B2Token: ללא_מהווה, S0Token: ללא, S0_LastThreeLetters: �א, S0_LastTwoLetters: א, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

20- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [מעורבות, הציבור, מהווה ,.. ]

B0Token: מעורבות, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: הציבור, B1_LastThreeLetters: �ר, B1_LastTwoLetters: ר, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [מעורבות]   B= [הציבור, מהווה, כישלון ,.. ]

B0Token: הציבור, B0_LastThreeLetters: �ר, B0_LastTwoLetters: ר, B1Token: מהווה, B1_LastThreeLetters: �ה, B1_LastTwoLetters: ה, S0B0Token: מעורבות_הציבור, S0B1Token: מעורבות_מהווה, S0B2Token: מעורבות_כישלון, S0Token: מעורבות, S0_LastThreeLetters: �ת, S0_LastTwoLetters: ת, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

22- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [הציבור, מהווה, כישלון ,.. ]

B0Token: הציבור, B0_LastThreeLetters: �ר, B0_LastTwoLetters: ר, B1Token: מהווה, B1_LastThreeLetters: �ה, B1_LastTwoLetters: ה, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

23- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [הציבור]   B= [מהווה, כישלון, חרוץ ,.. ]

B0Token: מהווה, B0_LastThreeLetters: �ה, B0_LastTwoLetters: ה, B1Token: כישלון, B1_LastThreeLetters: �ן, B1_LastTwoLetters: ן, S0B0Token: הציבור_מהווה, S0B1Token: הציבור_כישלון, S0B2Token: הציבור_חרוץ, S0Token: הציבור, S0_LastThreeLetters: �ר, S0_LastTwoLetters: ר, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

24- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [מהווה, כישלון, חרוץ ,.. ]

B0Token: מהווה, B0_LastThreeLetters: �ה, B0_LastTwoLetters: ה, B1Token: כישלון, B1_LastThreeLetters: �ן, B1_LastTwoLetters: ן, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

25- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [מהווה]   B= [כישלון, חרוץ, שאין ,.. ]

B0Token: כישלון, B0_LastThreeLetters: �ן, B0_LastTwoLetters: ן, B1Token: חרוץ, B1_LastThreeLetters: �ץ, B1_LastTwoLetters: ץ, S0B0Token: מהווה_כישלון, S0B1Token: מהווה_חרוץ, S0B2Token: מהווה_שאין, S0Token: מהווה, S0_LastThreeLetters: �ה, S0_LastTwoLetters: ה, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

26- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [מהווה, כישלון]   B= [חרוץ, שאין, לו ,.. ]

B0Token: חרוץ, B0_LastThreeLetters: �ץ, B0_LastTwoLetters: ץ, B1Token: שאין, B1_LastThreeLetters: �ן, B1_LastTwoLetters: ן, S0B0Token: כישלון_חרוץ, S0B1Token: כישלון_שאין, S0B2Token: כישלון_לו, S0Token: כישלון, S0_LastThreeLetters: �ן, S0_LastTwoLetters: ן, S1B0Token: מהווה_חרוץ, S1S0Token: מהווה_כישלון, S1Token: מהווה, S1_LastThreeLetters: �ה, S1_LastTwoLetters: ה, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

27- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [מהווה, כישלון, חרוץ]   B= [שאין, לו, אח ,.. ]

B0Token: שאין, B0_LastThreeLetters: �ן, B0_LastTwoLetters: ן, B1Token: לו, B1_LastThreeLetters: �ו, B1_LastTwoLetters: ו, S0B0Token: חרוץ_שאין, S0B1Token: חרוץ_לו, S0B2Token: חרוץ_אח, S0Token: חרוץ, S0_LastThreeLetters: �ץ, S0_LastTwoLetters: ץ, S1B0Token: כישלון_שאין, S1S0Token: כישלון_חרוץ, S1Token: כישלון, S1_LastThreeLetters: �ן, S1_LastTwoLetters: ן, transitionHistoryLength1: 0, transitionHistoryLength2: 00, transitionHistoryLength3: 002, 

28- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [מהווה, [כישלון, חרוץ]]   B= [שאין, לו, אח ,.. ]

B0Token: שאין, B0_LastThreeLetters: �ן, B0_LastTwoLetters: ן, B1Token: לו, B1_LastThreeLetters: �ו, B1_LastTwoLetters: ו, S0B0Token: כישלון_חרוץ_שאין, S0B1Token: כישלון_חרוץ_לו, S0B2Token: כישלון_חרוץ_אח, S0Token: כישלון_חרוץ, S1B0Token: מהווה_שאין, S1S0Token: מהווה_כישלון_חרוץ, S1Token: מהווה, S1_LastThreeLetters: �ה, S1_LastTwoLetters: ה, transitionHistoryLength1: 0, transitionHistoryLength2: 00, transitionHistoryLength3: 000, 

29- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[מהווה, [כישלון, חרוץ]]]   B= [שאין, לו, אח ,.. ]

B0Token: שאין, B0_LastThreeLetters: �ן, B0_LastTwoLetters: ן, B1Token: לו, B1_LastThreeLetters: �ו, B1_LastTwoLetters: ו, S0B0Token: מהווה_כישלון_חרוץ_שאין, S0B1Token: מהווה_כישלון_חרוץ_לו, S0B2Token: מהווה_כישלון_חרוץ_אח, S0Token: מהווה_כישלון_חרוץ, transitionHistoryLength1: 1, transitionHistoryLength2: 10, transitionHistoryLength3: 100, 

30- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [שאין, לו, אח ,.. ]

B0Token: שאין, B0_LastThreeLetters: �ן, B0_LastTwoLetters: ן, B1Token: לו, B1_LastThreeLetters: �ו, B1_LastTwoLetters: ו, transitionHistoryLength1: 1, transitionHistoryLength2: 11, transitionHistoryLength3: 110, 

31- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [שאין]   B= [לו, אח, ורע ,.. ]

B0Token: לו, B0_LastThreeLetters: �ו, B0_LastTwoLetters: ו, B1Token: אח, B1_LastThreeLetters: �ח, B1_LastTwoLetters: ח, S0B0Token: שאין_לו, S0B1Token: שאין_אח, S0B2Token: שאין_ורע, S0Token: שאין, S0_LastThreeLetters: �ן, S0_LastTwoLetters: ן, transitionHistoryLength1: 2, transitionHistoryLength2: 21, transitionHistoryLength3: 211, 

32- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [לו, אח, ורע ,.. ]

B0Token: לו, B0_LastThreeLetters: �ו, B0_LastTwoLetters: ו, B1Token: אח, B1_LastThreeLetters: �ח, B1_LastTwoLetters: ח, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 021, 

33- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [לו]   B= [אח, ורע, בשום ,.. ]

B0Token: אח, B0_LastThreeLetters: �ח, B0_LastTwoLetters: ח, B1Token: ורע, B1_LastThreeLetters: �ע, B1_LastTwoLetters: ע, S0B0Token: לו_אח, S0B1Token: לו_ורע, S0B2Token: לו_בשום, S0Token: לו, S0_LastThreeLetters: �ו, S0_LastTwoLetters: ו, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

34- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [אח, ורע, בשום ,.. ]

B0Token: אח, B0_LastThreeLetters: �ח, B0_LastTwoLetters: ח, B1Token: ורע, B1_LastThreeLetters: �ע, B1_LastTwoLetters: ע, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

35- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [אח]   B= [ורע, בשום, מקום ,.. ]

B0Token: ורע, B0_LastThreeLetters: �ע, B0_LastTwoLetters: ע, B1Token: בשום, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, S0B0Token: אח_ורע, S0B1Token: אח_בשום, S0B2Token: אח_מקום, S0Token: אח, S0_LastThreeLetters: �ח, S0_LastTwoLetters: ח, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

36- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ורע, בשום, מקום ,.. ]

B0Token: ורע, B0_LastThreeLetters: �ע, B0_LastTwoLetters: ע, B1Token: בשום, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

37- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ורע]   B= [בשום, מקום, בעולם ,.. ]

B0Token: בשום, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, B1Token: מקום, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, S0B0Token: ורע_בשום, S0B1Token: ורע_מקום, S0B2Token: ורע_בעולם, S0Token: ורע, S0_LastThreeLetters: �ע, S0_LastTwoLetters: ע, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

38- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [בשום, מקום, בעולם ,.. ]

B0Token: בשום, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, B1Token: מקום, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

39- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [בשום]   B= [מקום, בעולם ,.. ]

B0Token: מקום, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, B1Token: בעולם, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, S0B0Token: בשום_מקום, S0B1Token: בשום_בעולם, S0Token: בשום, S0_LastThreeLetters: �ם, S0_LastTwoLetters: ם, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

40- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [מקום, בעולם ,.. ]

B0Token: מקום, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, B1Token: בעולם, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

41- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [מקום]   B= [בעולם]

B0Token: בעולם, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, S0B0Token: מקום_בעולם, S0Token: מקום, S0_LastThreeLetters: �ם, S0_LastTwoLetters: ם, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

42- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [בעולם]

B0Token: בעולם, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

43- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [בעולם]   B= [ ]

S0Token: בעולם, S0_LastThreeLetters: �ם, S0_LastTwoLetters: ם, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

44- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

## Sentence No. 1339 - 
יש לשנות את דרך ההתנהלות ולהגיע לפתרון מערכתי רחב יש לבזר סמכויות ולהרחיב את מעורבות הועדות המקומיות אשר הוצאו למעשה מהתמונה ובכך ניתן יהיה להחיל עליהן את האחריות בקבלת ההחלטות אמר שר הפנים במהלך דיוני ועדה שעסקה בסוגיה
### Existing MWEs: 
1- **הוצאו מהתמונה** (OTH)
2- **שעסקה בסוגיה** (VPC)



0- &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [יש, לשנות, את ,.. ]

B0Token: יש, B0_LastThreeLetters: �ש, B0_LastTwoLetters: ש, B1Token: לשנות, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, 

1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [יש]   B= [לשנות, את, דרך ,.. ]

B0Token: לשנות, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: את, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, S0B0Token: יש_לשנות, S0B1Token: יש_את, S0B2Token: יש_דרך, S0Token: יש, S0_LastThreeLetters: �ש, S0_LastTwoLetters: ש, 

2- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [לשנות, את, דרך ,.. ]

B0Token: לשנות, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: את, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, transitionHistoryLength1: 0, 

3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [לשנות]   B= [את, דרך, ההתנהלות ,.. ]

B0Token: את, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: דרך, B1_LastThreeLetters: �ך, B1_LastTwoLetters: ך, S0B0Token: לשנות_את, S0B1Token: לשנות_דרך, S0B2Token: לשנות_ההתנהלות, S0Token: לשנות, S0_LastThreeLetters: �ת, S0_LastTwoLetters: ת, transitionHistoryLength1: 2, transitionHistoryLength2: 20, 

4- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [את, דרך, ההתנהלות ,.. ]

B0Token: את, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: דרך, B1_LastThreeLetters: �ך, B1_LastTwoLetters: ך, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [את]   B= [דרך, ההתנהלות, ולהגיע ,.. ]

B0Token: דרך, B0_LastThreeLetters: �ך, B0_LastTwoLetters: ך, B1Token: ההתנהלות, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, S0B0Token: את_דרך, S0B1Token: את_ההתנהלות, S0B2Token: את_ולהגיע, S0Token: את, S0_LastThreeLetters: �ת, S0_LastTwoLetters: ת, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

6- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [דרך, ההתנהלות, ולהגיע ,.. ]

B0Token: דרך, B0_LastThreeLetters: �ך, B0_LastTwoLetters: ך, B1Token: ההתנהלות, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [דרך]   B= [ההתנהלות, ולהגיע, לפתרון ,.. ]

B0Token: ההתנהלות, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: ולהגיע, B1_LastThreeLetters: �ע, B1_LastTwoLetters: ע, S0B0Token: דרך_ההתנהלות, S0B1Token: דרך_ולהגיע, S0B2Token: דרך_לפתרון, S0Token: דרך, S0_LastThreeLetters: �ך, S0_LastTwoLetters: ך, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

8- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ההתנהלות, ולהגיע, לפתרון ,.. ]

B0Token: ההתנהלות, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: ולהגיע, B1_LastThreeLetters: �ע, B1_LastTwoLetters: ע, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ההתנהלות]   B= [ולהגיע, לפתרון, מערכתי ,.. ]

B0Token: ולהגיע, B0_LastThreeLetters: �ע, B0_LastTwoLetters: ע, B1Token: לפתרון, B1_LastThreeLetters: �ן, B1_LastTwoLetters: ן, S0B0Token: ההתנהלות_ולהגיע, S0B1Token: ההתנהלות_לפתרון, S0B2Token: ההתנהלות_מערכתי, S0Token: ההתנהלות, S0_LastThreeLetters: �ת, S0_LastTwoLetters: ת, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

10- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ולהגיע, לפתרון, מערכתי ,.. ]

B0Token: ולהגיע, B0_LastThreeLetters: �ע, B0_LastTwoLetters: ע, B1Token: לפתרון, B1_LastThreeLetters: �ן, B1_LastTwoLetters: ן, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ולהגיע]   B= [לפתרון, מערכתי, רחב ,.. ]

B0Token: לפתרון, B0_LastThreeLetters: �ן, B0_LastTwoLetters: ן, B1Token: מערכתי, B1_LastThreeLetters: �י, B1_LastTwoLetters: י, S0B0Token: ולהגיע_לפתרון, S0B1Token: ולהגיע_מערכתי, S0B2Token: ולהגיע_רחב, S0Token: ולהגיע, S0_LastThreeLetters: �ע, S0_LastTwoLetters: ע, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

12- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [לפתרון, מערכתי, רחב ,.. ]

B0Token: לפתרון, B0_LastThreeLetters: �ן, B0_LastTwoLetters: ן, B1Token: מערכתי, B1_LastThreeLetters: �י, B1_LastTwoLetters: י, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [לפתרון]   B= [מערכתי, רחב, יש ,.. ]

B0Token: מערכתי, B0_LastThreeLetters: �י, B0_LastTwoLetters: י, B1Token: רחב, B1_LastThreeLetters: �ב, B1_LastTwoLetters: ב, S0B0Token: לפתרון_מערכתי, S0B1Token: לפתרון_רחב, S0B2Token: לפתרון_יש, S0Token: לפתרון, S0_LastThreeLetters: �ן, S0_LastTwoLetters: ן, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

14- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [מערכתי, רחב, יש ,.. ]

B0Token: מערכתי, B0_LastThreeLetters: �י, B0_LastTwoLetters: י, B1Token: רחב, B1_LastThreeLetters: �ב, B1_LastTwoLetters: ב, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [מערכתי]   B= [רחב, יש, לבזר ,.. ]

B0Token: רחב, B0_LastThreeLetters: �ב, B0_LastTwoLetters: ב, B1Token: יש, B1_LastThreeLetters: �ש, B1_LastTwoLetters: ש, S0B0Token: מערכתי_רחב, S0B1Token: מערכתי_יש, S0B2Token: מערכתי_לבזר, S0Token: מערכתי, S0_LastThreeLetters: �י, S0_LastTwoLetters: י, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

16- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [רחב, יש, לבזר ,.. ]

B0Token: רחב, B0_LastThreeLetters: �ב, B0_LastTwoLetters: ב, B1Token: יש, B1_LastThreeLetters: �ש, B1_LastTwoLetters: ש, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [רחב]   B= [יש, לבזר, סמכויות ,.. ]

B0Token: יש, B0_LastThreeLetters: �ש, B0_LastTwoLetters: ש, B1Token: לבזר, B1_LastThreeLetters: �ר, B1_LastTwoLetters: ר, S0B0Token: רחב_יש, S0B1Token: רחב_לבזר, S0B2Token: רחב_סמכויות, S0Token: רחב, S0_LastThreeLetters: �ב, S0_LastTwoLetters: ב, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

18- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [יש, לבזר, סמכויות ,.. ]

B0Token: יש, B0_LastThreeLetters: �ש, B0_LastTwoLetters: ש, B1Token: לבזר, B1_LastThreeLetters: �ר, B1_LastTwoLetters: ר, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [יש]   B= [לבזר, סמכויות, ולהרחיב ,.. ]

B0Token: לבזר, B0_LastThreeLetters: �ר, B0_LastTwoLetters: ר, B1Token: סמכויות, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, S0B0Token: יש_לבזר, S0B1Token: יש_סמכויות, S0B2Token: יש_ולהרחיב, S0Token: יש, S0_LastThreeLetters: �ש, S0_LastTwoLetters: ש, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

20- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [לבזר, סמכויות, ולהרחיב ,.. ]

B0Token: לבזר, B0_LastThreeLetters: �ר, B0_LastTwoLetters: ר, B1Token: סמכויות, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [לבזר]   B= [סמכויות, ולהרחיב, את ,.. ]

B0Token: סמכויות, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: ולהרחיב, B1_LastThreeLetters: �ב, B1_LastTwoLetters: ב, S0B0Token: לבזר_סמכויות, S0B1Token: לבזר_ולהרחיב, S0B2Token: לבזר_את, S0Token: לבזר, S0_LastThreeLetters: �ר, S0_LastTwoLetters: ר, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

22- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [סמכויות, ולהרחיב, את ,.. ]

B0Token: סמכויות, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: ולהרחיב, B1_LastThreeLetters: �ב, B1_LastTwoLetters: ב, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

23- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [סמכויות]   B= [ולהרחיב, את, מעורבות ,.. ]

B0Token: ולהרחיב, B0_LastThreeLetters: �ב, B0_LastTwoLetters: ב, B1Token: את, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, S0B0Token: סמכויות_ולהרחיב, S0B1Token: סמכויות_את, S0B2Token: סמכויות_מעורבות, S0Token: סמכויות, S0_LastThreeLetters: �ת, S0_LastTwoLetters: ת, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

24- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ולהרחיב, את, מעורבות ,.. ]

B0Token: ולהרחיב, B0_LastThreeLetters: �ב, B0_LastTwoLetters: ב, B1Token: את, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

25- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ולהרחיב]   B= [את, מעורבות, הועדות ,.. ]

B0Token: את, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: מעורבות, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, S0B0Token: ולהרחיב_את, S0B1Token: ולהרחיב_מעורבות, S0B2Token: ולהרחיב_הועדות, S0Token: ולהרחיב, S0_LastThreeLetters: �ב, S0_LastTwoLetters: ב, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

26- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [את, מעורבות, הועדות ,.. ]

B0Token: את, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: מעורבות, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

27- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [את]   B= [מעורבות, הועדות, המקומיות ,.. ]

B0Token: מעורבות, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: הועדות, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, S0B0Token: את_מעורבות, S0B1Token: את_הועדות, S0B2Token: את_המקומיות, S0Token: את, S0_LastThreeLetters: �ת, S0_LastTwoLetters: ת, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

28- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [מעורבות, הועדות, המקומיות ,.. ]

B0Token: מעורבות, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: הועדות, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

29- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [מעורבות]   B= [הועדות, המקומיות, אשר ,.. ]

B0Token: הועדות, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: המקומיות, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, S0B0Token: מעורבות_הועדות, S0B1Token: מעורבות_המקומיות, S0B2Token: מעורבות_אשר, S0Token: מעורבות, S0_LastThreeLetters: �ת, S0_LastTwoLetters: ת, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

30- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [הועדות, המקומיות, אשר ,.. ]

B0Token: הועדות, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: המקומיות, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

31- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [הועדות]   B= [המקומיות, אשר, הוצאו ,.. ]

B0Token: המקומיות, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: אשר, B1_LastThreeLetters: �ר, B1_LastTwoLetters: ר, S0B0Token: הועדות_המקומיות, S0B1Token: הועדות_אשר, S0B2Token: הועדות_הוצאו, S0Token: הועדות, S0_LastThreeLetters: �ת, S0_LastTwoLetters: ת, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

32- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [המקומיות, אשר, הוצאו ,.. ]

B0Token: המקומיות, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: אשר, B1_LastThreeLetters: �ר, B1_LastTwoLetters: ר, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

33- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [המקומיות]   B= [אשר, הוצאו, למעשה ,.. ]

B0Token: אשר, B0_LastThreeLetters: �ר, B0_LastTwoLetters: ר, B1Token: הוצאו, B1_LastThreeLetters: �ו, B1_LastTwoLetters: ו, S0B0Token: המקומיות_אשר, S0B1Token: המקומיות_הוצאו, S0B2Token: המקומיות_למעשה, S0Token: המקומיות, S0_LastThreeLetters: �ת, S0_LastTwoLetters: ת, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

34- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [אשר, הוצאו, למעשה ,.. ]

B0Token: אשר, B0_LastThreeLetters: �ר, B0_LastTwoLetters: ר, B1Token: הוצאו, B1_LastThreeLetters: �ו, B1_LastTwoLetters: ו, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

35- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [אשר]   B= [הוצאו, למעשה, מהתמונה ,.. ]

B0Token: הוצאו, B0_LastThreeLetters: �ו, B0_LastTwoLetters: ו, B1Token: למעשה, B1_LastThreeLetters: �ה, B1_LastTwoLetters: ה, S0B0Token: אשר_הוצאו, S0B1Token: אשר_למעשה, S0B2Token: אשר_מהתמונה, S0Token: אשר, S0_LastThreeLetters: �ר, S0_LastTwoLetters: ר, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

36- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [הוצאו, למעשה, מהתמונה ,.. ]

B0Token: הוצאו, B0_LastThreeLetters: �ו, B0_LastTwoLetters: ו, B1Token: למעשה, B1_LastThreeLetters: �ה, B1_LastTwoLetters: ה, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

37- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [הוצאו]   B= [למעשה, מהתמונה, ובכך ,.. ]

B0Token: למעשה, B0_LastThreeLetters: �ה, B0_LastTwoLetters: ה, B1Token: מהתמונה, B1_LastThreeLetters: �ה, B1_LastTwoLetters: ה, S0B0Token: הוצאו_למעשה, S0B1Token: הוצאו_מהתמונה, S0B2Token: הוצאו_ובכך, S0Token: הוצאו, S0_LastThreeLetters: �ו, S0_LastTwoLetters: ו, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

38- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [הוצאו, למעשה]   B= [מהתמונה, ובכך, ניתן ,.. ]

B0Token: מהתמונה, B0_LastThreeLetters: �ה, B0_LastTwoLetters: ה, B1Token: ובכך, B1_LastThreeLetters: �ך, B1_LastTwoLetters: ך, S0B0Token: למעשה_מהתמונה, S0B1Token: למעשה_ובכך, S0B2Token: למעשה_ניתן, S0Token: למעשה, S0_LastThreeLetters: �ה, S0_LastTwoLetters: ה, S1B0Token: הוצאו_מהתמונה, S1S0Token: הוצאו_למעשה, S1Token: הוצאו, S1_LastThreeLetters: �ו, S1_LastTwoLetters: ו, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

39- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [הוצאו]   B= [מהתמונה, ובכך, ניתן ,.. ]

B0Token: מהתמונה, B0_LastThreeLetters: �ה, B0_LastTwoLetters: ה, B1Token: ובכך, B1_LastThreeLetters: �ך, B1_LastTwoLetters: ך, S0B0Token: הוצאו_מהתמונה, S0B1Token: הוצאו_ובכך, S0B2Token: הוצאו_ניתן, S0Token: הוצאו, S0_LastThreeLetters: �ו, S0_LastTwoLetters: ו, transitionHistoryLength1: 0, transitionHistoryLength2: 00, transitionHistoryLength3: 002, 

40- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [הוצאו, מהתמונה]   B= [ובכך, ניתן, יהיה ,.. ]

B0Token: ובכך, B0_LastThreeLetters: �ך, B0_LastTwoLetters: ך, B1Token: ניתן, B1_LastThreeLetters: �ן, B1_LastTwoLetters: ן, S0B0Token: מהתמונה_ובכך, S0B1Token: מהתמונה_ניתן, S0B2Token: מהתמונה_יהיה, S0Token: מהתמונה, S0_LastThreeLetters: �ה, S0_LastTwoLetters: ה, S1B0Token: הוצאו_ובכך, S1S0Token: הוצאו_מהתמונה, S1Token: הוצאו, S1_LastThreeLetters: �ו, S1_LastTwoLetters: ו, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 200, 

41- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[הוצאו, מהתמונה]]   B= [ובכך, ניתן, יהיה ,.. ]

B0Token: ובכך, B0_LastThreeLetters: �ך, B0_LastTwoLetters: ך, B1Token: ניתן, B1_LastThreeLetters: �ן, B1_LastTwoLetters: ן, S0B0Token: הוצאו_מהתמונה_ובכך, S0B1Token: הוצאו_מהתמונה_ניתן, S0B2Token: הוצאו_מהתמונה_יהיה, S0Token: הוצאו_מהתמונה, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

42- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ובכך, ניתן, יהיה ,.. ]

B0Token: ובכך, B0_LastThreeLetters: �ך, B0_LastTwoLetters: ך, B1Token: ניתן, B1_LastThreeLetters: �ן, B1_LastTwoLetters: ן, transitionHistoryLength1: 1, transitionHistoryLength2: 10, transitionHistoryLength3: 102, 

43- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ובכך]   B= [ניתן, יהיה, להחיל ,.. ]

B0Token: ניתן, B0_LastThreeLetters: �ן, B0_LastTwoLetters: ן, B1Token: יהיה, B1_LastThreeLetters: �ה, B1_LastTwoLetters: ה, S0B0Token: ובכך_ניתן, S0B1Token: ובכך_יהיה, S0B2Token: ובכך_להחיל, S0Token: ובכך, S0_LastThreeLetters: �ך, S0_LastTwoLetters: ך, transitionHistoryLength1: 2, transitionHistoryLength2: 21, transitionHistoryLength3: 210, 

44- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ניתן, יהיה, להחיל ,.. ]

B0Token: ניתן, B0_LastThreeLetters: �ן, B0_LastTwoLetters: ן, B1Token: יהיה, B1_LastThreeLetters: �ה, B1_LastTwoLetters: ה, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 021, 

45- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ניתן]   B= [יהיה, להחיל, עליהן ,.. ]

B0Token: יהיה, B0_LastThreeLetters: �ה, B0_LastTwoLetters: ה, B1Token: להחיל, B1_LastThreeLetters: �ל, B1_LastTwoLetters: ל, S0B0Token: ניתן_יהיה, S0B1Token: ניתן_להחיל, S0B2Token: ניתן_עליהן, S0Token: ניתן, S0_LastThreeLetters: �ן, S0_LastTwoLetters: ן, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

46- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [יהיה, להחיל, עליהן ,.. ]

B0Token: יהיה, B0_LastThreeLetters: �ה, B0_LastTwoLetters: ה, B1Token: להחיל, B1_LastThreeLetters: �ל, B1_LastTwoLetters: ל, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

47- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [יהיה]   B= [להחיל, עליהן, את ,.. ]

B0Token: להחיל, B0_LastThreeLetters: �ל, B0_LastTwoLetters: ל, B1Token: עליהן, B1_LastThreeLetters: �ן, B1_LastTwoLetters: ן, S0B0Token: יהיה_להחיל, S0B1Token: יהיה_עליהן, S0B2Token: יהיה_את, S0Token: יהיה, S0_LastThreeLetters: �ה, S0_LastTwoLetters: ה, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

48- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [להחיל, עליהן, את ,.. ]

B0Token: להחיל, B0_LastThreeLetters: �ל, B0_LastTwoLetters: ל, B1Token: עליהן, B1_LastThreeLetters: �ן, B1_LastTwoLetters: ן, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

49- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [להחיל]   B= [עליהן, את, האחריות ,.. ]

B0Token: עליהן, B0_LastThreeLetters: �ן, B0_LastTwoLetters: ן, B1Token: את, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, S0B0Token: להחיל_עליהן, S0B1Token: להחיל_את, S0B2Token: להחיל_האחריות, S0Token: להחיל, S0_LastThreeLetters: �ל, S0_LastTwoLetters: ל, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

50- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [עליהן, את, האחריות ,.. ]

B0Token: עליהן, B0_LastThreeLetters: �ן, B0_LastTwoLetters: ן, B1Token: את, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

51- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [עליהן]   B= [את, האחריות, בקבלת ,.. ]

B0Token: את, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: האחריות, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, S0B0Token: עליהן_את, S0B1Token: עליהן_האחריות, S0B2Token: עליהן_בקבלת, S0Token: עליהן, S0_LastThreeLetters: �ן, S0_LastTwoLetters: ן, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

52- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [את, האחריות, בקבלת ,.. ]

B0Token: את, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: האחריות, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

53- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [את]   B= [האחריות, בקבלת, ההחלטות ,.. ]

B0Token: האחריות, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: בקבלת, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, S0B0Token: את_האחריות, S0B1Token: את_בקבלת, S0B2Token: את_ההחלטות, S0Token: את, S0_LastThreeLetters: �ת, S0_LastTwoLetters: ת, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

54- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [האחריות, בקבלת, ההחלטות ,.. ]

B0Token: האחריות, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: בקבלת, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

55- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [האחריות]   B= [בקבלת, ההחלטות, אמר ,.. ]

B0Token: בקבלת, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: ההחלטות, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, S0B0Token: האחריות_בקבלת, S0B1Token: האחריות_ההחלטות, S0B2Token: האחריות_אמר, S0Token: האחריות, S0_LastThreeLetters: �ת, S0_LastTwoLetters: ת, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

56- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [בקבלת, ההחלטות, אמר ,.. ]

B0Token: בקבלת, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: ההחלטות, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

57- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [בקבלת]   B= [ההחלטות, אמר, שר ,.. ]

B0Token: ההחלטות, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: אמר, B1_LastThreeLetters: �ר, B1_LastTwoLetters: ר, S0B0Token: בקבלת_ההחלטות, S0B1Token: בקבלת_אמר, S0B2Token: בקבלת_שר, S0Token: בקבלת, S0_LastThreeLetters: �ת, S0_LastTwoLetters: ת, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

58- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ההחלטות, אמר, שר ,.. ]

B0Token: ההחלטות, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: אמר, B1_LastThreeLetters: �ר, B1_LastTwoLetters: ר, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

59- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ההחלטות]   B= [אמר, שר, הפנים ,.. ]

B0Token: אמר, B0_LastThreeLetters: �ר, B0_LastTwoLetters: ר, B1Token: שר, B1_LastThreeLetters: �ר, B1_LastTwoLetters: ר, S0B0Token: ההחלטות_אמר, S0B1Token: ההחלטות_שר, S0B2Token: ההחלטות_הפנים, S0Token: ההחלטות, S0_LastThreeLetters: �ת, S0_LastTwoLetters: ת, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

60- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [אמר, שר, הפנים ,.. ]

B0Token: אמר, B0_LastThreeLetters: �ר, B0_LastTwoLetters: ר, B1Token: שר, B1_LastThreeLetters: �ר, B1_LastTwoLetters: ר, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

61- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [אמר]   B= [שר, הפנים, במהלך ,.. ]

B0Token: שר, B0_LastThreeLetters: �ר, B0_LastTwoLetters: ר, B1Token: הפנים, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, S0B0Token: אמר_שר, S0B1Token: אמר_הפנים, S0B2Token: אמר_במהלך, S0Token: אמר, S0_LastThreeLetters: �ר, S0_LastTwoLetters: ר, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

62- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [שר, הפנים, במהלך ,.. ]

B0Token: שר, B0_LastThreeLetters: �ר, B0_LastTwoLetters: ר, B1Token: הפנים, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

63- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [שר]   B= [הפנים, במהלך, דיוני ,.. ]

B0Token: הפנים, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, B1Token: במהלך, B1_LastThreeLetters: �ך, B1_LastTwoLetters: ך, S0B0Token: שר_הפנים, S0B1Token: שר_במהלך, S0B2Token: שר_דיוני, S0Token: שר, S0_LastThreeLetters: �ר, S0_LastTwoLetters: ר, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

64- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [הפנים, במהלך, דיוני ,.. ]

B0Token: הפנים, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, B1Token: במהלך, B1_LastThreeLetters: �ך, B1_LastTwoLetters: ך, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

65- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [הפנים]   B= [במהלך, דיוני, ועדה ,.. ]

B0Token: במהלך, B0_LastThreeLetters: �ך, B0_LastTwoLetters: ך, B1Token: דיוני, B1_LastThreeLetters: �י, B1_LastTwoLetters: י, S0B0Token: הפנים_במהלך, S0B1Token: הפנים_דיוני, S0B2Token: הפנים_ועדה, S0Token: הפנים, S0_LastThreeLetters: �ם, S0_LastTwoLetters: ם, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

66- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [במהלך, דיוני, ועדה ,.. ]

B0Token: במהלך, B0_LastThreeLetters: �ך, B0_LastTwoLetters: ך, B1Token: דיוני, B1_LastThreeLetters: �י, B1_LastTwoLetters: י, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

67- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [במהלך]   B= [דיוני, ועדה, שעסקה ,.. ]

B0Token: דיוני, B0_LastThreeLetters: �י, B0_LastTwoLetters: י, B1Token: ועדה, B1_LastThreeLetters: �ה, B1_LastTwoLetters: ה, S0B0Token: במהלך_דיוני, S0B1Token: במהלך_ועדה, S0B2Token: במהלך_שעסקה, S0Token: במהלך, S0_LastThreeLetters: �ך, S0_LastTwoLetters: ך, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

68- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [דיוני, ועדה, שעסקה ,.. ]

B0Token: דיוני, B0_LastThreeLetters: �י, B0_LastTwoLetters: י, B1Token: ועדה, B1_LastThreeLetters: �ה, B1_LastTwoLetters: ה, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

69- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [דיוני]   B= [ועדה, שעסקה, בסוגיה ,.. ]

B0Token: ועדה, B0_LastThreeLetters: �ה, B0_LastTwoLetters: ה, B1Token: שעסקה, B1_LastThreeLetters: �ה, B1_LastTwoLetters: ה, S0B0Token: דיוני_ועדה, S0B1Token: דיוני_שעסקה, S0B2Token: דיוני_בסוגיה, S0Token: דיוני, S0_LastThreeLetters: �י, S0_LastTwoLetters: י, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

70- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ועדה, שעסקה, בסוגיה ,.. ]

B0Token: ועדה, B0_LastThreeLetters: �ה, B0_LastTwoLetters: ה, B1Token: שעסקה, B1_LastThreeLetters: �ה, B1_LastTwoLetters: ה, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

71- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ועדה]   B= [שעסקה, בסוגיה ,.. ]

B0Token: שעסקה, B0_LastThreeLetters: �ה, B0_LastTwoLetters: ה, B1Token: בסוגיה, B1_LastThreeLetters: �ה, B1_LastTwoLetters: ה, S0B0Token: ועדה_שעסקה, S0B1Token: ועדה_בסוגיה, S0Token: ועדה, S0_LastThreeLetters: �ה, S0_LastTwoLetters: ה, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

72- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [שעסקה, בסוגיה ,.. ]

B0Token: שעסקה, B0_LastThreeLetters: �ה, B0_LastTwoLetters: ה, B1Token: בסוגיה, B1_LastThreeLetters: �ה, B1_LastTwoLetters: ה, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

73- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [שעסקה]   B= [בסוגיה]

B0Token: בסוגיה, B0_LastThreeLetters: �ה, B0_LastTwoLetters: ה, S0B0Token: שעסקה_בסוגיה, S0Token: שעסקה, S0_LastThreeLetters: �ה, S0_LastTwoLetters: ה, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

74- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [שעסקה, בסוגיה]   B= [ ]

S0Token: בסוגיה, S0_LastThreeLetters: �ה, S0_LastTwoLetters: ה, S1S0Token: שעסקה_בסוגיה, S1Token: שעסקה, S1_LastThreeLetters: �ה, S1_LastTwoLetters: ה, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

75- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[שעסקה, בסוגיה]]   B= [ ]

S0Token: שעסקה_בסוגיה, transitionHistoryLength1: 0, transitionHistoryLength2: 00, transitionHistoryLength3: 002, 

76- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

## Sentence No. 1368 - 
מארגני האירוע אומרים כי לאירוע יגיעו מכל הארץ ממגוון תנועות ההתיישבות שחוללו את נס התחייה הציונית של עם השב אל ארצו ואדמתו
### Existing MWEs: 
1- **שחוללו את נס התחייה** (OTH)
2- **עם השב אל ארצו ואדמתו** (OTH)



0- &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [מארגני, האירוע, אומרים ,.. ]

B0Token: מארגני, B0_LastThreeLetters: �י, B0_LastTwoLetters: י, B1Token: האירוע, B1_LastThreeLetters: �ע, B1_LastTwoLetters: ע, 

1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [מארגני]   B= [האירוע, אומרים, כי ,.. ]

B0Token: האירוע, B0_LastThreeLetters: �ע, B0_LastTwoLetters: ע, B1Token: אומרים, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, S0B0Token: מארגני_האירוע, S0B1Token: מארגני_אומרים, S0B2Token: מארגני_כי, S0Token: מארגני, S0_LastThreeLetters: �י, S0_LastTwoLetters: י, 

2- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [האירוע, אומרים, כי ,.. ]

B0Token: האירוע, B0_LastThreeLetters: �ע, B0_LastTwoLetters: ע, B1Token: אומרים, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, transitionHistoryLength1: 0, 

3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [האירוע]   B= [אומרים, כי, לאירוע ,.. ]

B0Token: אומרים, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, B1Token: כי, B1_LastThreeLetters: �י, B1_LastTwoLetters: י, S0B0Token: האירוע_אומרים, S0B1Token: האירוע_כי, S0B2Token: האירוע_לאירוע, S0Token: האירוע, S0_LastThreeLetters: �ע, S0_LastTwoLetters: ע, transitionHistoryLength1: 2, transitionHistoryLength2: 20, 

4- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [אומרים, כי, לאירוע ,.. ]

B0Token: אומרים, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, B1Token: כי, B1_LastThreeLetters: �י, B1_LastTwoLetters: י, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [אומרים]   B= [כי, לאירוע, יגיעו ,.. ]

B0Token: כי, B0_LastThreeLetters: �י, B0_LastTwoLetters: י, B1Token: לאירוע, B1_LastThreeLetters: �ע, B1_LastTwoLetters: ע, S0B0Token: אומרים_כי, S0B1Token: אומרים_לאירוע, S0B2Token: אומרים_יגיעו, S0Token: אומרים, S0_LastThreeLetters: �ם, S0_LastTwoLetters: ם, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

6- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [כי, לאירוע, יגיעו ,.. ]

B0Token: כי, B0_LastThreeLetters: �י, B0_LastTwoLetters: י, B1Token: לאירוע, B1_LastThreeLetters: �ע, B1_LastTwoLetters: ע, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [כי]   B= [לאירוע, יגיעו, מכל ,.. ]

B0Token: לאירוע, B0_LastThreeLetters: �ע, B0_LastTwoLetters: ע, B1Token: יגיעו, B1_LastThreeLetters: �ו, B1_LastTwoLetters: ו, S0B0Token: כי_לאירוע, S0B1Token: כי_יגיעו, S0B2Token: כי_מכל, S0Token: כי, S0_LastThreeLetters: �י, S0_LastTwoLetters: י, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

8- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [לאירוע, יגיעו, מכל ,.. ]

B0Token: לאירוע, B0_LastThreeLetters: �ע, B0_LastTwoLetters: ע, B1Token: יגיעו, B1_LastThreeLetters: �ו, B1_LastTwoLetters: ו, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [לאירוע]   B= [יגיעו, מכל, הארץ ,.. ]

B0Token: יגיעו, B0_LastThreeLetters: �ו, B0_LastTwoLetters: ו, B1Token: מכל, B1_LastThreeLetters: �ל, B1_LastTwoLetters: ל, S0B0Token: לאירוע_יגיעו, S0B1Token: לאירוע_מכל, S0B2Token: לאירוע_הארץ, S0Token: לאירוע, S0_LastThreeLetters: �ע, S0_LastTwoLetters: ע, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

10- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [יגיעו, מכל, הארץ ,.. ]

B0Token: יגיעו, B0_LastThreeLetters: �ו, B0_LastTwoLetters: ו, B1Token: מכל, B1_LastThreeLetters: �ל, B1_LastTwoLetters: ל, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [יגיעו]   B= [מכל, הארץ, ממגוון ,.. ]

B0Token: מכל, B0_LastThreeLetters: �ל, B0_LastTwoLetters: ל, B1Token: הארץ, B1_LastThreeLetters: �ץ, B1_LastTwoLetters: ץ, S0B0Token: יגיעו_מכל, S0B1Token: יגיעו_הארץ, S0B2Token: יגיעו_ממגוון, S0Token: יגיעו, S0_LastThreeLetters: �ו, S0_LastTwoLetters: ו, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

12- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [מכל, הארץ, ממגוון ,.. ]

B0Token: מכל, B0_LastThreeLetters: �ל, B0_LastTwoLetters: ל, B1Token: הארץ, B1_LastThreeLetters: �ץ, B1_LastTwoLetters: ץ, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [מכל]   B= [הארץ, ממגוון, תנועות ,.. ]

B0Token: הארץ, B0_LastThreeLetters: �ץ, B0_LastTwoLetters: ץ, B1Token: ממגוון, B1_LastThreeLetters: �ן, B1_LastTwoLetters: ן, S0B0Token: מכל_הארץ, S0B1Token: מכל_ממגוון, S0B2Token: מכל_תנועות, S0Token: מכל, S0_LastThreeLetters: �ל, S0_LastTwoLetters: ל, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

14- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [הארץ, ממגוון, תנועות ,.. ]

B0Token: הארץ, B0_LastThreeLetters: �ץ, B0_LastTwoLetters: ץ, B1Token: ממגוון, B1_LastThreeLetters: �ן, B1_LastTwoLetters: ן, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [הארץ]   B= [ממגוון, תנועות, ההתיישבות ,.. ]

B0Token: ממגוון, B0_LastThreeLetters: �ן, B0_LastTwoLetters: ן, B1Token: תנועות, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, S0B0Token: הארץ_ממגוון, S0B1Token: הארץ_תנועות, S0B2Token: הארץ_ההתיישבות, S0Token: הארץ, S0_LastThreeLetters: �ץ, S0_LastTwoLetters: ץ, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

16- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ממגוון, תנועות, ההתיישבות ,.. ]

B0Token: ממגוון, B0_LastThreeLetters: �ן, B0_LastTwoLetters: ן, B1Token: תנועות, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ממגוון]   B= [תנועות, ההתיישבות, שחוללו ,.. ]

B0Token: תנועות, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: ההתיישבות, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, S0B0Token: ממגוון_תנועות, S0B1Token: ממגוון_ההתיישבות, S0B2Token: ממגוון_שחוללו, S0Token: ממגוון, S0_LastThreeLetters: �ן, S0_LastTwoLetters: ן, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

18- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [תנועות, ההתיישבות, שחוללו ,.. ]

B0Token: תנועות, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: ההתיישבות, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [תנועות]   B= [ההתיישבות, שחוללו, את ,.. ]

B0Token: ההתיישבות, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: שחוללו, B1_LastThreeLetters: �ו, B1_LastTwoLetters: ו, S0B0Token: תנועות_ההתיישבות, S0B1Token: תנועות_שחוללו, S0B2Token: תנועות_את, S0Token: תנועות, S0_LastThreeLetters: �ת, S0_LastTwoLetters: ת, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

20- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ההתיישבות, שחוללו, את ,.. ]

B0Token: ההתיישבות, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: שחוללו, B1_LastThreeLetters: �ו, B1_LastTwoLetters: ו, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ההתיישבות]   B= [שחוללו, את, נס ,.. ]

B0Token: שחוללו, B0_LastThreeLetters: �ו, B0_LastTwoLetters: ו, B1Token: את, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, S0B0Token: ההתיישבות_שחוללו, S0B1Token: ההתיישבות_את, S0B2Token: ההתיישבות_נס, S0Token: ההתיישבות, S0_LastThreeLetters: �ת, S0_LastTwoLetters: ת, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

22- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [שחוללו, את, נס ,.. ]

B0Token: שחוללו, B0_LastThreeLetters: �ו, B0_LastTwoLetters: ו, B1Token: את, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

23- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [שחוללו]   B= [את, נס, התחייה ,.. ]

B0Token: את, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: נס, B1_LastThreeLetters: �ס, B1_LastTwoLetters: ס, S0B0Token: שחוללו_את, S0B1Token: שחוללו_נס, S0B2Token: שחוללו_התחייה, S0Token: שחוללו, S0_LastThreeLetters: �ו, S0_LastTwoLetters: ו, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

24- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [שחוללו, את]   B= [נס, התחייה, הציונית ,.. ]

B0Token: נס, B0_LastThreeLetters: �ס, B0_LastTwoLetters: ס, B1Token: התחייה, B1_LastThreeLetters: �ה, B1_LastTwoLetters: ה, S0B0Token: את_נס, S0B1Token: את_התחייה, S0B2Token: את_הציונית, S0Token: את, S0_LastThreeLetters: �ת, S0_LastTwoLetters: ת, S1B0Token: שחוללו_נס, S1S0Token: שחוללו_את, S1Token: שחוללו, S1_LastThreeLetters: �ו, S1_LastTwoLetters: ו, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

25- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [שחוללו, את, נס]   B= [התחייה, הציונית, של ,.. ]

B0Token: התחייה, B0_LastThreeLetters: �ה, B0_LastTwoLetters: ה, B1Token: הציונית, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, S0B0Token: נס_התחייה, S0B1Token: נס_הציונית, S0B2Token: נס_של, S0Token: נס, S0_LastThreeLetters: �ס, S0_LastTwoLetters: ס, S1B0Token: את_התחייה, S1S0Token: את_נס, S1Token: את, S1_LastThreeLetters: �ת, S1_LastTwoLetters: ת, transitionHistoryLength1: 0, transitionHistoryLength2: 00, transitionHistoryLength3: 002, 

26- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [שחוללו, את, נס, התחייה]   B= [הציונית, של, עם ,.. ]

B0Token: הציונית, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: של, B1_LastThreeLetters: �ל, B1_LastTwoLetters: ל, S0B0Token: התחייה_הציונית, S0B1Token: התחייה_של, S0B2Token: התחייה_עם, S0Token: התחייה, S0_LastThreeLetters: �ה, S0_LastTwoLetters: ה, S1B0Token: נס_הציונית, S1S0Token: נס_התחייה, S1Token: נס, S1_LastThreeLetters: �ס, S1_LastTwoLetters: ס, transitionHistoryLength1: 0, transitionHistoryLength2: 00, transitionHistoryLength3: 000, 

27- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [שחוללו, את, [נס, התחייה]]   B= [הציונית, של, עם ,.. ]

B0Token: הציונית, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: של, B1_LastThreeLetters: �ל, B1_LastTwoLetters: ל, S0B0Token: נס_התחייה_הציונית, S0B1Token: נס_התחייה_של, S0B2Token: נס_התחייה_עם, S0Token: נס_התחייה, S1B0Token: את_הציונית, S1S0Token: את_נס_התחייה, S1Token: את, S1_LastThreeLetters: �ת, S1_LastTwoLetters: ת, transitionHistoryLength1: 0, transitionHistoryLength2: 00, transitionHistoryLength3: 000, 

28- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [שחוללו, [את, [נס, התחייה]]]   B= [הציונית, של, עם ,.. ]

B0Token: הציונית, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: של, B1_LastThreeLetters: �ל, B1_LastTwoLetters: ל, S0B0Token: את_נס_התחייה_הציונית, S0B1Token: את_נס_התחייה_של, S0B2Token: את_נס_התחייה_עם, S0Token: את_נס_התחייה, S1B0Token: שחוללו_הציונית, S1S0Token: שחוללו_את_נס_התחייה, S1Token: שחוללו, S1_LastThreeLetters: �ו, S1_LastTwoLetters: ו, transitionHistoryLength1: 1, transitionHistoryLength2: 10, transitionHistoryLength3: 100, 

29- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[שחוללו, [את, [נס, התחייה]]]]   B= [הציונית, של, עם ,.. ]

B0Token: הציונית, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: של, B1_LastThreeLetters: �ל, B1_LastTwoLetters: ל, S0B0Token: שחוללו_את_נס_התחייה_הציונית, S0B1Token: שחוללו_את_נס_התחייה_של, S0B2Token: שחוללו_את_נס_התחייה_עם, S0Token: שחוללו_את_נס_התחייה, transitionHistoryLength1: 1, transitionHistoryLength2: 11, transitionHistoryLength3: 110, 

30- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [הציונית, של, עם ,.. ]

B0Token: הציונית, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: של, B1_LastThreeLetters: �ל, B1_LastTwoLetters: ל, transitionHistoryLength1: 1, transitionHistoryLength2: 11, transitionHistoryLength3: 111, 

31- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [הציונית]   B= [של, עם, השב ,.. ]

B0Token: של, B0_LastThreeLetters: �ל, B0_LastTwoLetters: ל, B1Token: עם, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, S0B0Token: הציונית_של, S0B1Token: הציונית_עם, S0B2Token: הציונית_השב, S0Token: הציונית, S0_LastThreeLetters: �ת, S0_LastTwoLetters: ת, transitionHistoryLength1: 2, transitionHistoryLength2: 21, transitionHistoryLength3: 211, 

32- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [של, עם, השב ,.. ]

B0Token: של, B0_LastThreeLetters: �ל, B0_LastTwoLetters: ל, B1Token: עם, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 021, 

33- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [של]   B= [עם, השב, אל ,.. ]

B0Token: עם, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, B1Token: השב, B1_LastThreeLetters: �ב, B1_LastTwoLetters: ב, S0B0Token: של_עם, S0B1Token: של_השב, S0B2Token: של_אל, S0Token: של, S0_LastThreeLetters: �ל, S0_LastTwoLetters: ל, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

34- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [עם, השב, אל ,.. ]

B0Token: עם, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, B1Token: השב, B1_LastThreeLetters: �ב, B1_LastTwoLetters: ב, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

35- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [עם]   B= [השב, אל, ארצו ,.. ]

B0Token: השב, B0_LastThreeLetters: �ב, B0_LastTwoLetters: ב, B1Token: אל, B1_LastThreeLetters: �ל, B1_LastTwoLetters: ל, S0B0Token: עם_השב, S0B1Token: עם_אל, S0B2Token: עם_ארצו, S0Token: עם, S0_LastThreeLetters: �ם, S0_LastTwoLetters: ם, transitionHistoryLength1: 2, transitionHistoryLength2: 20, transitionHistoryLength3: 202, 

36- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [עם, השב]   B= [אל, ארצו, ואדמתו ,.. ]

B0Token: אל, B0_LastThreeLetters: �ל, B0_LastTwoLetters: ל, B1Token: ארצו, B1_LastThreeLetters: �ו, B1_LastTwoLetters: ו, S0B0Token: השב_אל, S0B1Token: השב_ארצו, S0B2Token: השב_ואדמתו, S0Token: השב, S0_LastThreeLetters: �ב, S0_LastTwoLetters: ב, S1B0Token: עם_אל, S1S0Token: עם_השב, S1Token: עם, S1_LastThreeLetters: �ם, S1_LastTwoLetters: ם, transitionHistoryLength1: 0, transitionHistoryLength2: 02, transitionHistoryLength3: 020, 

37- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [עם, השב, אל]   B= [ארצו, ואדמתו ,.. ]

B0Token: ארצו, B0_LastThreeLetters: �ו, B0_LastTwoLetters: ו, B1Token: ואדמתו, B1_LastThreeLetters: �ו, B1_LastTwoLetters: ו, S0B0Token: אל_ארצו, S0B1Token: אל_ואדמתו, S0Token: אל, S0_LastThreeLetters: �ל, S0_LastTwoLetters: ל, S1B0Token: השב_ארצו, S1S0Token: השב_אל, S1Token: השב, S1_LastThreeLetters: �ב, S1_LastTwoLetters: ב, transitionHistoryLength1: 0, transitionHistoryLength2: 00, transitionHistoryLength3: 002, 

38- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [עם, השב, אל, ארצו]   B= [ואדמתו]

B0Token: ואדמתו, B0_LastThreeLetters: �ו, B0_LastTwoLetters: ו, S0B0Token: ארצו_ואדמתו, S0Token: ארצו, S0_LastThreeLetters: �ו, S0_LastTwoLetters: ו, S1B0Token: אל_ואדמתו, S1S0Token: אל_ארצו, S1Token: אל, S1_LastThreeLetters: �ל, S1_LastTwoLetters: ל, transitionHistoryLength1: 0, transitionHistoryLength2: 00, transitionHistoryLength3: 000, 

39- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [עם, השב, אל, ארצו, ואדמתו]   B= [ ]

S0Token: ואדמתו, S0_LastThreeLetters: �ו, S0_LastTwoLetters: ו, S1S0Token: ארצו_ואדמתו, S1Token: ארצו, S1_LastThreeLetters: �ו, S1_LastTwoLetters: ו, transitionHistoryLength1: 0, transitionHistoryLength2: 00, transitionHistoryLength3: 000, 

40- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [עם, השב, אל, [ארצו, ואדמתו]]   B= [ ]

S0Token: ארצו_ואדמתו, S1S0Token: אל_ארצו_ואדמתו, S1Token: אל, S1_LastThreeLetters: �ל, S1_LastTwoLetters: ל, transitionHistoryLength1: 0, transitionHistoryLength2: 00, transitionHistoryLength3: 000, 

41- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [עם, השב, [אל, [ארצו, ואדמתו]]]   B= [ ]

S0Token: אל_ארצו_ואדמתו, S1S0Token: השב_אל_ארצו_ואדמתו, S1Token: השב, S1_LastThreeLetters: �ב, S1_LastTwoLetters: ב, transitionHistoryLength1: 1, transitionHistoryLength2: 10, transitionHistoryLength3: 100, 

42- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [עם, [השב, [אל, [ארצו, ואדמתו]]]]   B= [ ]

S0Token: השב_אל_ארצו_ואדמתו, S1S0Token: עם_השב_אל_ארצו_ואדמתו, S1Token: עם, S1_LastThreeLetters: �ם, S1_LastTwoLetters: ם, transitionHistoryLength1: 1, transitionHistoryLength2: 11, transitionHistoryLength3: 110, 

43- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[עם, [השב, [אל, [ארצו, ואדמתו]]]]]   B= [ ]

S0Token: עם_השב_אל_ארצו_ואדמתו, transitionHistoryLength1: 1, transitionHistoryLength2: 11, transitionHistoryLength3: 111, 

44- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

