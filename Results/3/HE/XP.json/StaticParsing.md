## Sentence No. 72 - 
ועד רבני חב " ד לא הביע עד כה את עמדתו בשאלת הסרבנות בשל העובדה שהרבי זצ " ל לא קרא מעולם לחיילים לסרב להשתתף בפינוי יישובים ובנסיגות אף שזעק והתריע בכל כוחו נגד המהלכים הללו
### Existing MWEs: 
1- **הביע את עמדתו** (VPC)
2- **שזעק והתריע** (OTH)



0- &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ועד, רבני, חב ,.. ]

B0Token: ועד, B0_LastThreeLetters: �ד, B0_LastTwoLetters: ד, B1Token: רבני, B1_LastThreeLetters: �י, B1_LastTwoLetters: י, 

1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ועד]   B= [רבני, חב, " ,.. ]

B0Token: רבני, B0_LastThreeLetters: �י, B0_LastTwoLetters: י, B1Token: חב, B1_LastThreeLetters: �ב, B1_LastTwoLetters: ב, S0B0Token: ועד_רבני, S0B1Token: ועד_חב, S0B2Token: ועד_", S0Token: ועד, S0_LastThreeLetters: �ד, S0_LastTwoLetters: ד, 

2- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [רבני, חב, " ,.. ]

B0Token: רבני, B0_LastThreeLetters: �י, B0_LastTwoLetters: י, B1Token: חב, B1_LastThreeLetters: �ב, B1_LastTwoLetters: ב, TransHistory1: 0, 

3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [רבני]   B= [חב, ", ד ,.. ]

B0Token: חב, B0_LastThreeLetters: �ב, B0_LastTwoLetters: ב, B1Token: ", B1_LastThreeLetters: ", B1_LastTwoLetters: ", S0B0Token: רבני_חב, S0B1Token: רבני_", S0B2Token: רבני_ד, S0Token: רבני, S0_LastThreeLetters: �י, S0_LastTwoLetters: י, TransHistory1: 2, TransHistory2: 20, 

4- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [חב, ", ד ,.. ]

B0Token: חב, B0_LastThreeLetters: �ב, B0_LastTwoLetters: ב, B1Token: ", B1_LastThreeLetters: ", B1_LastTwoLetters: ", TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [חב]   B= [", ד, לא ,.. ]

B0Token: ", B0_LastThreeLetters: ", B0_LastTwoLetters: ", B1Token: ד, B1_LastThreeLetters: ד, B1_LastTwoLetters: ד, S0B0Token: חב_", S0B1Token: חב_ד, S0B2Token: חב_לא, S0Token: חב, S0_LastThreeLetters: �ב, S0_LastTwoLetters: ב, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

6- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [", ד, לא ,.. ]

B0Token: ", B0_LastThreeLetters: ", B0_LastTwoLetters: ", B1Token: ד, B1_LastThreeLetters: ד, B1_LastTwoLetters: ד, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= ["]   B= [ד, לא, הביע ,.. ]

B0Token: ד, B0_LastThreeLetters: ד, B0_LastTwoLetters: ד, B1Token: לא, B1_LastThreeLetters: �א, B1_LastTwoLetters: א, S0B0Token: "_ד, S0B1Token: "_לא, S0B2Token: "_הביע, S0Token: ", S0_LastThreeLetters: ", S0_LastTwoLetters: ", TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

8- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ד, לא, הביע ,.. ]

B0Token: ד, B0_LastThreeLetters: ד, B0_LastTwoLetters: ד, B1Token: לא, B1_LastThreeLetters: �א, B1_LastTwoLetters: א, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ד]   B= [לא, הביע, עד ,.. ]

B0Token: לא, B0_LastThreeLetters: �א, B0_LastTwoLetters: א, B1Token: הביע, B1_LastThreeLetters: �ע, B1_LastTwoLetters: ע, S0B0Token: ד_לא, S0B1Token: ד_הביע, S0B2Token: ד_עד, S0Token: ד, S0_LastThreeLetters: ד, S0_LastTwoLetters: ד, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

10- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [לא, הביע, עד ,.. ]

B0Token: לא, B0_LastThreeLetters: �א, B0_LastTwoLetters: א, B1Token: הביע, B1_LastThreeLetters: �ע, B1_LastTwoLetters: ע, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [לא]   B= [הביע, עד, כה ,.. ]

B0Token: הביע, B0_LastThreeLetters: �ע, B0_LastTwoLetters: ע, B1Token: עד, B1_LastThreeLetters: �ד, B1_LastTwoLetters: ד, S0B0Token: לא_הביע, S0B1Token: לא_עד, S0B2Token: לא_כה, S0Token: לא, S0_LastThreeLetters: �א, S0_LastTwoLetters: א, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

12- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [הביע, עד, כה ,.. ]

B0Token: הביע, B0_LastThreeLetters: �ע, B0_LastTwoLetters: ע, B1Token: עד, B1_LastThreeLetters: �ד, B1_LastTwoLetters: ד, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [הביע]   B= [עד, כה, את ,.. ]

B0Token: עד, B0_LastThreeLetters: �ד, B0_LastTwoLetters: ד, B1Token: כה, B1_LastThreeLetters: �ה, B1_LastTwoLetters: ה, S0B0Token: הביע_עד, S0B1Token: הביע_כה, S0B2Token: הביע_את, S0Token: הביע, S0_LastThreeLetters: �ע, S0_LastTwoLetters: ע, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

14- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [הביע, עד]   B= [כה, את, עמדתו ,.. ]

B0Token: כה, B0_LastThreeLetters: �ה, B0_LastTwoLetters: ה, B1Token: את, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, S0B0Token: עד_כה, S0B1Token: עד_את, S0B2Token: עד_עמדתו, S0Token: עד, S0_LastThreeLetters: �ד, S0_LastTwoLetters: ד, S1B0Token: הביע_כה, S1S0Token: הביע_עד, S1Token: הביע, S1_LastThreeLetters: �ע, S1_LastTwoLetters: ע, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

15- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [הביע]   B= [כה, את, עמדתו ,.. ]

B0Token: כה, B0_LastThreeLetters: �ה, B0_LastTwoLetters: ה, B1Token: את, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, S0B0Token: הביע_כה, S0B1Token: הביע_את, S0B2Token: הביע_עמדתו, S0Token: הביע, S0_LastThreeLetters: �ע, S0_LastTwoLetters: ע, TransHistory1: 0, TransHistory2: 00, TransHistory3: 002, 

16- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [הביע, כה]   B= [את, עמדתו, בשאלת ,.. ]

B0Token: את, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: עמדתו, B1_LastThreeLetters: �ו, B1_LastTwoLetters: ו, S0B0Token: כה_את, S0B1Token: כה_עמדתו, S0B2Token: כה_בשאלת, S0Token: כה, S0_LastThreeLetters: �ה, S0_LastTwoLetters: ה, S1B0Token: הביע_את, S1S0Token: הביע_כה, S1Token: הביע, S1_LastThreeLetters: �ע, S1_LastTwoLetters: ע, TransHistory1: 2, TransHistory2: 20, TransHistory3: 200, 

17- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [הביע]   B= [את, עמדתו, בשאלת ,.. ]

B0Token: את, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: עמדתו, B1_LastThreeLetters: �ו, B1_LastTwoLetters: ו, S0B0Token: הביע_את, S0B1Token: הביע_עמדתו, S0B2Token: הביע_בשאלת, S0Token: הביע, S0_LastThreeLetters: �ע, S0_LastTwoLetters: ע, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

18- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [הביע, את]   B= [עמדתו, בשאלת, הסרבנות ,.. ]

B0Token: עמדתו, B0_LastThreeLetters: �ו, B0_LastTwoLetters: ו, B1Token: בשאלת, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, S0B0Token: את_עמדתו, S0B1Token: את_בשאלת, S0B2Token: את_הסרבנות, S0Token: את, S0_LastThreeLetters: �ת, S0_LastTwoLetters: ת, S1B0Token: הביע_עמדתו, S1S0Token: הביע_את, S1Token: הביע, S1_LastThreeLetters: �ע, S1_LastTwoLetters: ע, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [הביע, את, עמדתו]   B= [בשאלת, הסרבנות, בשל ,.. ]

B0Token: בשאלת, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: הסרבנות, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, S0B0Token: עמדתו_בשאלת, S0B1Token: עמדתו_הסרבנות, S0B2Token: עמדתו_בשל, S0Token: עמדתו, S0_LastThreeLetters: �ו, S0_LastTwoLetters: ו, S1B0Token: את_בשאלת, S1S0Token: את_עמדתו, S1Token: את, S1_LastThreeLetters: �ת, S1_LastTwoLetters: ת, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

20- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [הביע, [את, עמדתו]]   B= [בשאלת, הסרבנות, בשל ,.. ]

B0Token: בשאלת, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: הסרבנות, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, S0B0Token: את_עמדתו_בשאלת, S0B1Token: את_עמדתו_הסרבנות, S0B2Token: את_עמדתו_בשל, S0Token: את_עמדתו, S1B0Token: הביע_בשאלת, S1S0Token: הביע_את_עמדתו, S1Token: הביע, S1_LastThreeLetters: �ע, S1_LastTwoLetters: ע, TransHistory1: 0, TransHistory2: 00, TransHistory3: 002, 

21- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[הביע, [את, עמדתו]]]   B= [בשאלת, הסרבנות, בשל ,.. ]

B0Token: בשאלת, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: הסרבנות, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, S0B0Token: הביע_את_עמדתו_בשאלת, S0B1Token: הביע_את_עמדתו_הסרבנות, S0B2Token: הביע_את_עמדתו_בשל, S0Token: הביע_את_עמדתו, TransHistory1: 1, TransHistory2: 10, TransHistory3: 100, 

22- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [בשאלת, הסרבנות, בשל ,.. ]

B0Token: בשאלת, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: הסרבנות, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, TransHistory1: 1, TransHistory2: 11, TransHistory3: 110, 

23- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [בשאלת]   B= [הסרבנות, בשל, העובדה ,.. ]

B0Token: הסרבנות, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: בשל, B1_LastThreeLetters: �ל, B1_LastTwoLetters: ל, S0B0Token: בשאלת_הסרבנות, S0B1Token: בשאלת_בשל, S0B2Token: בשאלת_העובדה, S0Token: בשאלת, S0_LastThreeLetters: �ת, S0_LastTwoLetters: ת, TransHistory1: 2, TransHistory2: 21, TransHistory3: 211, 

24- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [הסרבנות, בשל, העובדה ,.. ]

B0Token: הסרבנות, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: בשל, B1_LastThreeLetters: �ל, B1_LastTwoLetters: ל, TransHistory1: 0, TransHistory2: 02, TransHistory3: 021, 

25- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [הסרבנות]   B= [בשל, העובדה, שהרבי ,.. ]

B0Token: בשל, B0_LastThreeLetters: �ל, B0_LastTwoLetters: ל, B1Token: העובדה, B1_LastThreeLetters: �ה, B1_LastTwoLetters: ה, S0B0Token: הסרבנות_בשל, S0B1Token: הסרבנות_העובדה, S0B2Token: הסרבנות_שהרבי, S0Token: הסרבנות, S0_LastThreeLetters: �ת, S0_LastTwoLetters: ת, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

26- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [בשל, העובדה, שהרבי ,.. ]

B0Token: בשל, B0_LastThreeLetters: �ל, B0_LastTwoLetters: ל, B1Token: העובדה, B1_LastThreeLetters: �ה, B1_LastTwoLetters: ה, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

27- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [בשל]   B= [העובדה, שהרבי, זצ ,.. ]

B0Token: העובדה, B0_LastThreeLetters: �ה, B0_LastTwoLetters: ה, B1Token: שהרבי, B1_LastThreeLetters: �י, B1_LastTwoLetters: י, S0B0Token: בשל_העובדה, S0B1Token: בשל_שהרבי, S0B2Token: בשל_זצ, S0Token: בשל, S0_LastThreeLetters: �ל, S0_LastTwoLetters: ל, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

28- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [העובדה, שהרבי, זצ ,.. ]

B0Token: העובדה, B0_LastThreeLetters: �ה, B0_LastTwoLetters: ה, B1Token: שהרבי, B1_LastThreeLetters: �י, B1_LastTwoLetters: י, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

29- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [העובדה]   B= [שהרבי, זצ, " ,.. ]

B0Token: שהרבי, B0_LastThreeLetters: �י, B0_LastTwoLetters: י, B1Token: זצ, B1_LastThreeLetters: �צ, B1_LastTwoLetters: צ, S0B0Token: העובדה_שהרבי, S0B1Token: העובדה_זצ, S0B2Token: העובדה_", S0Token: העובדה, S0_LastThreeLetters: �ה, S0_LastTwoLetters: ה, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

30- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [שהרבי, זצ, " ,.. ]

B0Token: שהרבי, B0_LastThreeLetters: �י, B0_LastTwoLetters: י, B1Token: זצ, B1_LastThreeLetters: �צ, B1_LastTwoLetters: צ, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

31- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [שהרבי]   B= [זצ, ", ל ,.. ]

B0Token: זצ, B0_LastThreeLetters: �צ, B0_LastTwoLetters: צ, B1Token: ", B1_LastThreeLetters: ", B1_LastTwoLetters: ", S0B0Token: שהרבי_זצ, S0B1Token: שהרבי_", S0B2Token: שהרבי_ל, S0Token: שהרבי, S0_LastThreeLetters: �י, S0_LastTwoLetters: י, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

32- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [זצ, ", ל ,.. ]

B0Token: זצ, B0_LastThreeLetters: �צ, B0_LastTwoLetters: צ, B1Token: ", B1_LastThreeLetters: ", B1_LastTwoLetters: ", TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

33- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [זצ]   B= [", ל, לא ,.. ]

B0Token: ", B0_LastThreeLetters: ", B0_LastTwoLetters: ", B1Token: ל, B1_LastThreeLetters: ל, B1_LastTwoLetters: ל, S0B0Token: זצ_", S0B1Token: זצ_ל, S0B2Token: זצ_לא, S0Token: זצ, S0_LastThreeLetters: �צ, S0_LastTwoLetters: צ, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

34- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [", ל, לא ,.. ]

B0Token: ", B0_LastThreeLetters: ", B0_LastTwoLetters: ", B1Token: ל, B1_LastThreeLetters: ל, B1_LastTwoLetters: ל, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

35- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= ["]   B= [ל, לא, קרא ,.. ]

B0Token: ל, B0_LastThreeLetters: ל, B0_LastTwoLetters: ל, B1Token: לא, B1_LastThreeLetters: �א, B1_LastTwoLetters: א, S0B0Token: "_ל, S0B1Token: "_לא, S0B2Token: "_קרא, S0Token: ", S0_LastThreeLetters: ", S0_LastTwoLetters: ", TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

36- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ל, לא, קרא ,.. ]

B0Token: ל, B0_LastThreeLetters: ל, B0_LastTwoLetters: ל, B1Token: לא, B1_LastThreeLetters: �א, B1_LastTwoLetters: א, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

37- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ל]   B= [לא, קרא, מעולם ,.. ]

B0Token: לא, B0_LastThreeLetters: �א, B0_LastTwoLetters: א, B1Token: קרא, B1_LastThreeLetters: �א, B1_LastTwoLetters: א, S0B0Token: ל_לא, S0B1Token: ל_קרא, S0B2Token: ל_מעולם, S0Token: ל, S0_LastThreeLetters: ל, S0_LastTwoLetters: ל, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

38- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [לא, קרא, מעולם ,.. ]

B0Token: לא, B0_LastThreeLetters: �א, B0_LastTwoLetters: א, B1Token: קרא, B1_LastThreeLetters: �א, B1_LastTwoLetters: א, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

39- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [לא]   B= [קרא, מעולם, לחיילים ,.. ]

B0Token: קרא, B0_LastThreeLetters: �א, B0_LastTwoLetters: א, B1Token: מעולם, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, S0B0Token: לא_קרא, S0B1Token: לא_מעולם, S0B2Token: לא_לחיילים, S0Token: לא, S0_LastThreeLetters: �א, S0_LastTwoLetters: א, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

40- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [קרא, מעולם, לחיילים ,.. ]

B0Token: קרא, B0_LastThreeLetters: �א, B0_LastTwoLetters: א, B1Token: מעולם, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

41- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [קרא]   B= [מעולם, לחיילים, לסרב ,.. ]

B0Token: מעולם, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, B1Token: לחיילים, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, S0B0Token: קרא_מעולם, S0B1Token: קרא_לחיילים, S0B2Token: קרא_לסרב, S0Token: קרא, S0_LastThreeLetters: �א, S0_LastTwoLetters: א, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

42- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [מעולם, לחיילים, לסרב ,.. ]

B0Token: מעולם, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, B1Token: לחיילים, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

43- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [מעולם]   B= [לחיילים, לסרב, להשתתף ,.. ]

B0Token: לחיילים, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, B1Token: לסרב, B1_LastThreeLetters: �ב, B1_LastTwoLetters: ב, S0B0Token: מעולם_לחיילים, S0B1Token: מעולם_לסרב, S0B2Token: מעולם_להשתתף, S0Token: מעולם, S0_LastThreeLetters: �ם, S0_LastTwoLetters: ם, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

44- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [לחיילים, לסרב, להשתתף ,.. ]

B0Token: לחיילים, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, B1Token: לסרב, B1_LastThreeLetters: �ב, B1_LastTwoLetters: ב, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

45- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [לחיילים]   B= [לסרב, להשתתף, בפינוי ,.. ]

B0Token: לסרב, B0_LastThreeLetters: �ב, B0_LastTwoLetters: ב, B1Token: להשתתף, B1_LastThreeLetters: �ף, B1_LastTwoLetters: ף, S0B0Token: לחיילים_לסרב, S0B1Token: לחיילים_להשתתף, S0B2Token: לחיילים_בפינוי, S0Token: לחיילים, S0_LastThreeLetters: �ם, S0_LastTwoLetters: ם, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

46- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [לסרב, להשתתף, בפינוי ,.. ]

B0Token: לסרב, B0_LastThreeLetters: �ב, B0_LastTwoLetters: ב, B1Token: להשתתף, B1_LastThreeLetters: �ף, B1_LastTwoLetters: ף, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

47- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [לסרב]   B= [להשתתף, בפינוי, יישובים ,.. ]

B0Token: להשתתף, B0_LastThreeLetters: �ף, B0_LastTwoLetters: ף, B1Token: בפינוי, B1_LastThreeLetters: �י, B1_LastTwoLetters: י, S0B0Token: לסרב_להשתתף, S0B1Token: לסרב_בפינוי, S0B2Token: לסרב_יישובים, S0Token: לסרב, S0_LastThreeLetters: �ב, S0_LastTwoLetters: ב, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

48- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [להשתתף, בפינוי, יישובים ,.. ]

B0Token: להשתתף, B0_LastThreeLetters: �ף, B0_LastTwoLetters: ף, B1Token: בפינוי, B1_LastThreeLetters: �י, B1_LastTwoLetters: י, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

49- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [להשתתף]   B= [בפינוי, יישובים, ובנסיגות ,.. ]

B0Token: בפינוי, B0_LastThreeLetters: �י, B0_LastTwoLetters: י, B1Token: יישובים, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, S0B0Token: להשתתף_בפינוי, S0B1Token: להשתתף_יישובים, S0B2Token: להשתתף_ובנסיגות, S0Token: להשתתף, S0_LastThreeLetters: �ף, S0_LastTwoLetters: ף, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

50- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [בפינוי, יישובים, ובנסיגות ,.. ]

B0Token: בפינוי, B0_LastThreeLetters: �י, B0_LastTwoLetters: י, B1Token: יישובים, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

51- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [בפינוי]   B= [יישובים, ובנסיגות, אף ,.. ]

B0Token: יישובים, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, B1Token: ובנסיגות, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, S0B0Token: בפינוי_יישובים, S0B1Token: בפינוי_ובנסיגות, S0B2Token: בפינוי_אף, S0Token: בפינוי, S0_LastThreeLetters: �י, S0_LastTwoLetters: י, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

52- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [יישובים, ובנסיגות, אף ,.. ]

B0Token: יישובים, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, B1Token: ובנסיגות, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

53- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [יישובים]   B= [ובנסיגות, אף, שזעק ,.. ]

B0Token: ובנסיגות, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: אף, B1_LastThreeLetters: �ף, B1_LastTwoLetters: ף, S0B0Token: יישובים_ובנסיגות, S0B1Token: יישובים_אף, S0B2Token: יישובים_שזעק, S0Token: יישובים, S0_LastThreeLetters: �ם, S0_LastTwoLetters: ם, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

54- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ובנסיגות, אף, שזעק ,.. ]

B0Token: ובנסיגות, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: אף, B1_LastThreeLetters: �ף, B1_LastTwoLetters: ף, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

55- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ובנסיגות]   B= [אף, שזעק, והתריע ,.. ]

B0Token: אף, B0_LastThreeLetters: �ף, B0_LastTwoLetters: ף, B1Token: שזעק, B1_LastThreeLetters: �ק, B1_LastTwoLetters: ק, S0B0Token: ובנסיגות_אף, S0B1Token: ובנסיגות_שזעק, S0B2Token: ובנסיגות_והתריע, S0Token: ובנסיגות, S0_LastThreeLetters: �ת, S0_LastTwoLetters: ת, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

56- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [אף, שזעק, והתריע ,.. ]

B0Token: אף, B0_LastThreeLetters: �ף, B0_LastTwoLetters: ף, B1Token: שזעק, B1_LastThreeLetters: �ק, B1_LastTwoLetters: ק, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

57- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [אף]   B= [שזעק, והתריע, בכל ,.. ]

B0Token: שזעק, B0_LastThreeLetters: �ק, B0_LastTwoLetters: ק, B1Token: והתריע, B1_LastThreeLetters: �ע, B1_LastTwoLetters: ע, S0B0Token: אף_שזעק, S0B1Token: אף_והתריע, S0B2Token: אף_בכל, S0Token: אף, S0_LastThreeLetters: �ף, S0_LastTwoLetters: ף, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

58- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [שזעק, והתריע, בכל ,.. ]

B0Token: שזעק, B0_LastThreeLetters: �ק, B0_LastTwoLetters: ק, B1Token: והתריע, B1_LastThreeLetters: �ע, B1_LastTwoLetters: ע, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

59- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [שזעק]   B= [והתריע, בכל, כוחו ,.. ]

B0Token: והתריע, B0_LastThreeLetters: �ע, B0_LastTwoLetters: ע, B1Token: בכל, B1_LastThreeLetters: �ל, B1_LastTwoLetters: ל, S0B0Token: שזעק_והתריע, S0B1Token: שזעק_בכל, S0B2Token: שזעק_כוחו, S0Token: שזעק, S0_LastThreeLetters: �ק, S0_LastTwoLetters: ק, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

60- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [שזעק, והתריע]   B= [בכל, כוחו, נגד ,.. ]

B0Token: בכל, B0_LastThreeLetters: �ל, B0_LastTwoLetters: ל, B1Token: כוחו, B1_LastThreeLetters: �ו, B1_LastTwoLetters: ו, S0B0Token: והתריע_בכל, S0B1Token: והתריע_כוחו, S0B2Token: והתריע_נגד, S0Token: והתריע, S0_LastThreeLetters: �ע, S0_LastTwoLetters: ע, S1B0Token: שזעק_בכל, S1S0Token: שזעק_והתריע, S1Token: שזעק, S1_LastThreeLetters: �ק, S1_LastTwoLetters: ק, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

61- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[שזעק, והתריע]]   B= [בכל, כוחו, נגד ,.. ]

B0Token: בכל, B0_LastThreeLetters: �ל, B0_LastTwoLetters: ל, B1Token: כוחו, B1_LastThreeLetters: �ו, B1_LastTwoLetters: ו, S0B0Token: שזעק_והתריע_בכל, S0B1Token: שזעק_והתריע_כוחו, S0B2Token: שזעק_והתריע_נגד, S0Token: שזעק_והתריע, TransHistory1: 0, TransHistory2: 00, TransHistory3: 002, 

62- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [בכל, כוחו, נגד ,.. ]

B0Token: בכל, B0_LastThreeLetters: �ל, B0_LastTwoLetters: ל, B1Token: כוחו, B1_LastThreeLetters: �ו, B1_LastTwoLetters: ו, TransHistory1: 1, TransHistory2: 10, TransHistory3: 100, 

63- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [בכל]   B= [כוחו, נגד, המהלכים ,.. ]

B0Token: כוחו, B0_LastThreeLetters: �ו, B0_LastTwoLetters: ו, B1Token: נגד, B1_LastThreeLetters: �ד, B1_LastTwoLetters: ד, S0B0Token: בכל_כוחו, S0B1Token: בכל_נגד, S0B2Token: בכל_המהלכים, S0Token: בכל, S0_LastThreeLetters: �ל, S0_LastTwoLetters: ל, TransHistory1: 2, TransHistory2: 21, TransHistory3: 210, 

64- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [כוחו, נגד, המהלכים ,.. ]

B0Token: כוחו, B0_LastThreeLetters: �ו, B0_LastTwoLetters: ו, B1Token: נגד, B1_LastThreeLetters: �ד, B1_LastTwoLetters: ד, TransHistory1: 0, TransHistory2: 02, TransHistory3: 021, 

65- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [כוחו]   B= [נגד, המהלכים, הללו ,.. ]

B0Token: נגד, B0_LastThreeLetters: �ד, B0_LastTwoLetters: ד, B1Token: המהלכים, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, S0B0Token: כוחו_נגד, S0B1Token: כוחו_המהלכים, S0B2Token: כוחו_הללו, S0Token: כוחו, S0_LastThreeLetters: �ו, S0_LastTwoLetters: ו, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

66- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [נגד, המהלכים, הללו ,.. ]

B0Token: נגד, B0_LastThreeLetters: �ד, B0_LastTwoLetters: ד, B1Token: המהלכים, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

67- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [נגד]   B= [המהלכים, הללו ,.. ]

B0Token: המהלכים, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, B1Token: הללו, B1_LastThreeLetters: �ו, B1_LastTwoLetters: ו, S0B0Token: נגד_המהלכים, S0B1Token: נגד_הללו, S0Token: נגד, S0_LastThreeLetters: �ד, S0_LastTwoLetters: ד, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

68- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [המהלכים, הללו ,.. ]

B0Token: המהלכים, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, B1Token: הללו, B1_LastThreeLetters: �ו, B1_LastTwoLetters: ו, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

69- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [המהלכים]   B= [הללו]

B0Token: הללו, B0_LastThreeLetters: �ו, B0_LastTwoLetters: ו, S0B0Token: המהלכים_הללו, S0Token: המהלכים, S0_LastThreeLetters: �ם, S0_LastTwoLetters: ם, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

70- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [הללו]

B0Token: הללו, B0_LastThreeLetters: �ו, B0_LastTwoLetters: ו, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

71- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [הללו]   B= [ ]

S0Token: הללו, S0_LastThreeLetters: �ו, S0_LastTwoLetters: ו, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

72- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

## Sentence No. 92 - 
מחבלים פתחו באש לעבר רכב ישראלי סמוך לכניסה לבית אין נפגעים ולא נגרם נזק
### Existing MWEs: 
1- **פתחו באש** (VPC)
2- **נגרם נזק** (LVC)



0- &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [מחבלים, פתחו, באש ,.. ]

B0Token: מחבלים, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, B1Token: פתחו, B1_LastThreeLetters: �ו, B1_LastTwoLetters: ו, 

1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [מחבלים]   B= [פתחו, באש, לעבר ,.. ]

B0Token: פתחו, B0_LastThreeLetters: �ו, B0_LastTwoLetters: ו, B1Token: באש, B1_LastThreeLetters: �ש, B1_LastTwoLetters: ש, S0B0Token: מחבלים_פתחו, S0B1Token: מחבלים_באש, S0B2Token: מחבלים_לעבר, S0Token: מחבלים, S0_LastThreeLetters: �ם, S0_LastTwoLetters: ם, 

2- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [פתחו, באש, לעבר ,.. ]

B0Token: פתחו, B0_LastThreeLetters: �ו, B0_LastTwoLetters: ו, B1Token: באש, B1_LastThreeLetters: �ש, B1_LastTwoLetters: ש, TransHistory1: 0, 

3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [פתחו]   B= [באש, לעבר, רכב ,.. ]

B0Token: באש, B0_LastThreeLetters: �ש, B0_LastTwoLetters: ש, B1Token: לעבר, B1_LastThreeLetters: �ר, B1_LastTwoLetters: ר, S0B0Token: פתחו_באש, S0B1Token: פתחו_לעבר, S0B2Token: פתחו_רכב, S0Token: פתחו, S0_LastThreeLetters: �ו, S0_LastTwoLetters: ו, TransHistory1: 2, TransHistory2: 20, 

4- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [פתחו, באש]   B= [לעבר, רכב, ישראלי ,.. ]

B0Token: לעבר, B0_LastThreeLetters: �ר, B0_LastTwoLetters: ר, B1Token: רכב, B1_LastThreeLetters: �ב, B1_LastTwoLetters: ב, S0B0Token: באש_לעבר, S0B1Token: באש_רכב, S0B2Token: באש_ישראלי, S0Token: באש, S0_LastThreeLetters: �ש, S0_LastTwoLetters: ש, S1B0Token: פתחו_לעבר, S1S0Token: פתחו_באש, S1Token: פתחו, S1_LastThreeLetters: �ו, S1_LastTwoLetters: ו, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

5- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[פתחו, באש]]   B= [לעבר, רכב, ישראלי ,.. ]

B0Token: לעבר, B0_LastThreeLetters: �ר, B0_LastTwoLetters: ר, B1Token: רכב, B1_LastThreeLetters: �ב, B1_LastTwoLetters: ב, S0B0Token: פתחו_באש_לעבר, S0B1Token: פתחו_באש_רכב, S0B2Token: פתחו_באש_ישראלי, S0Token: פתחו_באש, TransHistory1: 0, TransHistory2: 00, TransHistory3: 002, 

6- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [לעבר, רכב, ישראלי ,.. ]

B0Token: לעבר, B0_LastThreeLetters: �ר, B0_LastTwoLetters: ר, B1Token: רכב, B1_LastThreeLetters: �ב, B1_LastTwoLetters: ב, TransHistory1: 1, TransHistory2: 10, TransHistory3: 100, 

7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [לעבר]   B= [רכב, ישראלי, סמוך ,.. ]

B0Token: רכב, B0_LastThreeLetters: �ב, B0_LastTwoLetters: ב, B1Token: ישראלי, B1_LastThreeLetters: �י, B1_LastTwoLetters: י, S0B0Token: לעבר_רכב, S0B1Token: לעבר_ישראלי, S0B2Token: לעבר_סמוך, S0Token: לעבר, S0_LastThreeLetters: �ר, S0_LastTwoLetters: ר, TransHistory1: 2, TransHistory2: 21, TransHistory3: 210, 

8- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [רכב, ישראלי, סמוך ,.. ]

B0Token: רכב, B0_LastThreeLetters: �ב, B0_LastTwoLetters: ב, B1Token: ישראלי, B1_LastThreeLetters: �י, B1_LastTwoLetters: י, TransHistory1: 0, TransHistory2: 02, TransHistory3: 021, 

9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [רכב]   B= [ישראלי, סמוך, לכניסה ,.. ]

B0Token: ישראלי, B0_LastThreeLetters: �י, B0_LastTwoLetters: י, B1Token: סמוך, B1_LastThreeLetters: �ך, B1_LastTwoLetters: ך, S0B0Token: רכב_ישראלי, S0B1Token: רכב_סמוך, S0B2Token: רכב_לכניסה, S0Token: רכב, S0_LastThreeLetters: �ב, S0_LastTwoLetters: ב, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

10- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ישראלי, סמוך, לכניסה ,.. ]

B0Token: ישראלי, B0_LastThreeLetters: �י, B0_LastTwoLetters: י, B1Token: סמוך, B1_LastThreeLetters: �ך, B1_LastTwoLetters: ך, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ישראלי]   B= [סמוך, לכניסה, לבית ,.. ]

B0Token: סמוך, B0_LastThreeLetters: �ך, B0_LastTwoLetters: ך, B1Token: לכניסה, B1_LastThreeLetters: �ה, B1_LastTwoLetters: ה, S0B0Token: ישראלי_סמוך, S0B1Token: ישראלי_לכניסה, S0B2Token: ישראלי_לבית, S0Token: ישראלי, S0_LastThreeLetters: �י, S0_LastTwoLetters: י, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

12- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [סמוך, לכניסה, לבית ,.. ]

B0Token: סמוך, B0_LastThreeLetters: �ך, B0_LastTwoLetters: ך, B1Token: לכניסה, B1_LastThreeLetters: �ה, B1_LastTwoLetters: ה, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [סמוך]   B= [לכניסה, לבית, אין ,.. ]

B0Token: לכניסה, B0_LastThreeLetters: �ה, B0_LastTwoLetters: ה, B1Token: לבית, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, S0B0Token: סמוך_לכניסה, S0B1Token: סמוך_לבית, S0B2Token: סמוך_אין, S0Token: סמוך, S0_LastThreeLetters: �ך, S0_LastTwoLetters: ך, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

14- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [לכניסה, לבית, אין ,.. ]

B0Token: לכניסה, B0_LastThreeLetters: �ה, B0_LastTwoLetters: ה, B1Token: לבית, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [לכניסה]   B= [לבית, אין, נפגעים ,.. ]

B0Token: לבית, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: אין, B1_LastThreeLetters: �ן, B1_LastTwoLetters: ן, S0B0Token: לכניסה_לבית, S0B1Token: לכניסה_אין, S0B2Token: לכניסה_נפגעים, S0Token: לכניסה, S0_LastThreeLetters: �ה, S0_LastTwoLetters: ה, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

16- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [לבית, אין, נפגעים ,.. ]

B0Token: לבית, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: אין, B1_LastThreeLetters: �ן, B1_LastTwoLetters: ן, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [לבית]   B= [אין, נפגעים, ולא ,.. ]

B0Token: אין, B0_LastThreeLetters: �ן, B0_LastTwoLetters: ן, B1Token: נפגעים, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, S0B0Token: לבית_אין, S0B1Token: לבית_נפגעים, S0B2Token: לבית_ולא, S0Token: לבית, S0_LastThreeLetters: �ת, S0_LastTwoLetters: ת, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

18- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [אין, נפגעים, ולא ,.. ]

B0Token: אין, B0_LastThreeLetters: �ן, B0_LastTwoLetters: ן, B1Token: נפגעים, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [אין]   B= [נפגעים, ולא, נגרם ,.. ]

B0Token: נפגעים, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, B1Token: ולא, B1_LastThreeLetters: �א, B1_LastTwoLetters: א, S0B0Token: אין_נפגעים, S0B1Token: אין_ולא, S0B2Token: אין_נגרם, S0Token: אין, S0_LastThreeLetters: �ן, S0_LastTwoLetters: ן, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

20- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [נפגעים, ולא, נגרם ,.. ]

B0Token: נפגעים, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, B1Token: ולא, B1_LastThreeLetters: �א, B1_LastTwoLetters: א, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [נפגעים]   B= [ולא, נגרם, נזק ,.. ]

B0Token: ולא, B0_LastThreeLetters: �א, B0_LastTwoLetters: א, B1Token: נגרם, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, S0B0Token: נפגעים_ולא, S0B1Token: נפגעים_נגרם, S0B2Token: נפגעים_נזק, S0Token: נפגעים, S0_LastThreeLetters: �ם, S0_LastTwoLetters: ם, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

22- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ולא, נגרם, נזק ,.. ]

B0Token: ולא, B0_LastThreeLetters: �א, B0_LastTwoLetters: א, B1Token: נגרם, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

23- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ולא]   B= [נגרם, נזק ,.. ]

B0Token: נגרם, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, B1Token: נזק, B1_LastThreeLetters: �ק, B1_LastTwoLetters: ק, S0B0Token: ולא_נגרם, S0B1Token: ולא_נזק, S0Token: ולא, S0_LastThreeLetters: �א, S0_LastTwoLetters: א, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

24- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [נגרם, נזק ,.. ]

B0Token: נגרם, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, B1Token: נזק, B1_LastThreeLetters: �ק, B1_LastTwoLetters: ק, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

25- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [נגרם]   B= [נזק]

B0Token: נזק, B0_LastThreeLetters: �ק, B0_LastTwoLetters: ק, S0B0Token: נגרם_נזק, S0Token: נגרם, S0_LastThreeLetters: �ם, S0_LastTwoLetters: ם, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

26- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [נגרם, נזק]   B= [ ]

S0Token: נזק, S0_LastThreeLetters: �ק, S0_LastTwoLetters: ק, S1S0Token: נגרם_נזק, S1Token: נגרם, S1_LastThreeLetters: �ם, S1_LastTwoLetters: ם, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

27- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[נגרם, נזק]]   B= [ ]

S0Token: נגרם_נזק, TransHistory1: 0, TransHistory2: 00, TransHistory3: 002, 

28- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

## Sentence No. 169 - 
ריבלין שב וחזר על טענתו ההולכת ומתבהרת מדברי צמרת ממשלתו של שרון לא מדובר רק בהתנתקות מחבל עזה ולא רק בהרס ובחורבן של גוש קטיף
### Existing MWEs: 
2- **שב על** (VPC)
1- **ההולכת ומתבהרת** (OTH)



0- &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ריבלין, שב, וחזר ,.. ]

B0Token: ריבלין, B0_LastThreeLetters: �ן, B0_LastTwoLetters: ן, B1Token: שב, B1_LastThreeLetters: �ב, B1_LastTwoLetters: ב, 

1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ריבלין]   B= [שב, וחזר, על ,.. ]

B0Token: שב, B0_LastThreeLetters: �ב, B0_LastTwoLetters: ב, B1Token: וחזר, B1_LastThreeLetters: �ר, B1_LastTwoLetters: ר, S0B0Token: ריבלין_שב, S0B1Token: ריבלין_וחזר, S0B2Token: ריבלין_על, S0Token: ריבלין, S0_LastThreeLetters: �ן, S0_LastTwoLetters: ן, 

2- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [שב, וחזר, על ,.. ]

B0Token: שב, B0_LastThreeLetters: �ב, B0_LastTwoLetters: ב, B1Token: וחזר, B1_LastThreeLetters: �ר, B1_LastTwoLetters: ר, TransHistory1: 0, 

3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [שב]   B= [וחזר, על, טענתו ,.. ]

B0Token: וחזר, B0_LastThreeLetters: �ר, B0_LastTwoLetters: ר, B1Token: על, B1_LastThreeLetters: �ל, B1_LastTwoLetters: ל, S0B0Token: שב_וחזר, S0B1Token: שב_על, S0B2Token: שב_טענתו, S0Token: שב, S0_LastThreeLetters: �ב, S0_LastTwoLetters: ב, TransHistory1: 2, TransHistory2: 20, 

4- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [שב, וחזר]   B= [על, טענתו, ההולכת ,.. ]

B0Token: על, B0_LastThreeLetters: �ל, B0_LastTwoLetters: ל, B1Token: טענתו, B1_LastThreeLetters: �ו, B1_LastTwoLetters: ו, S0B0Token: וחזר_על, S0B1Token: וחזר_טענתו, S0B2Token: וחזר_ההולכת, S0Token: וחזר, S0_LastThreeLetters: �ר, S0_LastTwoLetters: ר, S1B0Token: שב_על, S1S0Token: שב_וחזר, S1Token: שב, S1_LastThreeLetters: �ב, S1_LastTwoLetters: ב, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

5- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [שב]   B= [על, טענתו, ההולכת ,.. ]

B0Token: על, B0_LastThreeLetters: �ל, B0_LastTwoLetters: ל, B1Token: טענתו, B1_LastThreeLetters: �ו, B1_LastTwoLetters: ו, S0B0Token: שב_על, S0B1Token: שב_טענתו, S0B2Token: שב_ההולכת, S0Token: שב, S0_LastThreeLetters: �ב, S0_LastTwoLetters: ב, TransHistory1: 0, TransHistory2: 00, TransHistory3: 002, 

6- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [שב, על]   B= [טענתו, ההולכת, ומתבהרת ,.. ]

B0Token: טענתו, B0_LastThreeLetters: �ו, B0_LastTwoLetters: ו, B1Token: ההולכת, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, S0B0Token: על_טענתו, S0B1Token: על_ההולכת, S0B2Token: על_ומתבהרת, S0Token: על, S0_LastThreeLetters: �ל, S0_LastTwoLetters: ל, S1B0Token: שב_טענתו, S1S0Token: שב_על, S1Token: שב, S1_LastThreeLetters: �ב, S1_LastTwoLetters: ב, TransHistory1: 2, TransHistory2: 20, TransHistory3: 200, 

7- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[שב, על]]   B= [טענתו, ההולכת, ומתבהרת ,.. ]

B0Token: טענתו, B0_LastThreeLetters: �ו, B0_LastTwoLetters: ו, B1Token: ההולכת, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, S0B0Token: שב_על_טענתו, S0B1Token: שב_על_ההולכת, S0B2Token: שב_על_ומתבהרת, S0Token: שב_על, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

8- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [טענתו, ההולכת, ומתבהרת ,.. ]

B0Token: טענתו, B0_LastThreeLetters: �ו, B0_LastTwoLetters: ו, B1Token: ההולכת, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, TransHistory1: 1, TransHistory2: 10, TransHistory3: 102, 

9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [טענתו]   B= [ההולכת, ומתבהרת, מדברי ,.. ]

B0Token: ההולכת, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: ומתבהרת, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, S0B0Token: טענתו_ההולכת, S0B1Token: טענתו_ומתבהרת, S0B2Token: טענתו_מדברי, S0Token: טענתו, S0_LastThreeLetters: �ו, S0_LastTwoLetters: ו, TransHistory1: 2, TransHistory2: 21, TransHistory3: 210, 

10- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ההולכת, ומתבהרת, מדברי ,.. ]

B0Token: ההולכת, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: ומתבהרת, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, TransHistory1: 0, TransHistory2: 02, TransHistory3: 021, 

11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ההולכת]   B= [ומתבהרת, מדברי, צמרת ,.. ]

B0Token: ומתבהרת, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: מדברי, B1_LastThreeLetters: �י, B1_LastTwoLetters: י, S0B0Token: ההולכת_ומתבהרת, S0B1Token: ההולכת_מדברי, S0B2Token: ההולכת_צמרת, S0Token: ההולכת, S0_LastThreeLetters: �ת, S0_LastTwoLetters: ת, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

12- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ההולכת, ומתבהרת]   B= [מדברי, צמרת, ממשלתו ,.. ]

B0Token: מדברי, B0_LastThreeLetters: �י, B0_LastTwoLetters: י, B1Token: צמרת, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, S0B0Token: ומתבהרת_מדברי, S0B1Token: ומתבהרת_צמרת, S0B2Token: ומתבהרת_ממשלתו, S0Token: ומתבהרת, S0_LastThreeLetters: �ת, S0_LastTwoLetters: ת, S1B0Token: ההולכת_מדברי, S1S0Token: ההולכת_ומתבהרת, S1Token: ההולכת, S1_LastThreeLetters: �ת, S1_LastTwoLetters: ת, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

13- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[ההולכת, ומתבהרת]]   B= [מדברי, צמרת, ממשלתו ,.. ]

B0Token: מדברי, B0_LastThreeLetters: �י, B0_LastTwoLetters: י, B1Token: צמרת, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, S0B0Token: ההולכת_ומתבהרת_מדברי, S0B1Token: ההולכת_ומתבהרת_צמרת, S0B2Token: ההולכת_ומתבהרת_ממשלתו, S0Token: ההולכת_ומתבהרת, TransHistory1: 0, TransHistory2: 00, TransHistory3: 002, 

14- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [מדברי, צמרת, ממשלתו ,.. ]

B0Token: מדברי, B0_LastThreeLetters: �י, B0_LastTwoLetters: י, B1Token: צמרת, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, TransHistory1: 1, TransHistory2: 10, TransHistory3: 100, 

15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [מדברי]   B= [צמרת, ממשלתו, של ,.. ]

B0Token: צמרת, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: ממשלתו, B1_LastThreeLetters: �ו, B1_LastTwoLetters: ו, S0B0Token: מדברי_צמרת, S0B1Token: מדברי_ממשלתו, S0B2Token: מדברי_של, S0Token: מדברי, S0_LastThreeLetters: �י, S0_LastTwoLetters: י, TransHistory1: 2, TransHistory2: 21, TransHistory3: 210, 

16- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [צמרת, ממשלתו, של ,.. ]

B0Token: צמרת, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: ממשלתו, B1_LastThreeLetters: �ו, B1_LastTwoLetters: ו, TransHistory1: 0, TransHistory2: 02, TransHistory3: 021, 

17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [צמרת]   B= [ממשלתו, של, שרון ,.. ]

B0Token: ממשלתו, B0_LastThreeLetters: �ו, B0_LastTwoLetters: ו, B1Token: של, B1_LastThreeLetters: �ל, B1_LastTwoLetters: ל, S0B0Token: צמרת_ממשלתו, S0B1Token: צמרת_של, S0B2Token: צמרת_שרון, S0Token: צמרת, S0_LastThreeLetters: �ת, S0_LastTwoLetters: ת, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

18- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ממשלתו, של, שרון ,.. ]

B0Token: ממשלתו, B0_LastThreeLetters: �ו, B0_LastTwoLetters: ו, B1Token: של, B1_LastThreeLetters: �ל, B1_LastTwoLetters: ל, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ממשלתו]   B= [של, שרון, לא ,.. ]

B0Token: של, B0_LastThreeLetters: �ל, B0_LastTwoLetters: ל, B1Token: שרון, B1_LastThreeLetters: �ן, B1_LastTwoLetters: ן, S0B0Token: ממשלתו_של, S0B1Token: ממשלתו_שרון, S0B2Token: ממשלתו_לא, S0Token: ממשלתו, S0_LastThreeLetters: �ו, S0_LastTwoLetters: ו, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

20- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [של, שרון, לא ,.. ]

B0Token: של, B0_LastThreeLetters: �ל, B0_LastTwoLetters: ל, B1Token: שרון, B1_LastThreeLetters: �ן, B1_LastTwoLetters: ן, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [של]   B= [שרון, לא, מדובר ,.. ]

B0Token: שרון, B0_LastThreeLetters: �ן, B0_LastTwoLetters: ן, B1Token: לא, B1_LastThreeLetters: �א, B1_LastTwoLetters: א, S0B0Token: של_שרון, S0B1Token: של_לא, S0B2Token: של_מדובר, S0Token: של, S0_LastThreeLetters: �ל, S0_LastTwoLetters: ל, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

22- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [שרון, לא, מדובר ,.. ]

B0Token: שרון, B0_LastThreeLetters: �ן, B0_LastTwoLetters: ן, B1Token: לא, B1_LastThreeLetters: �א, B1_LastTwoLetters: א, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

23- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [שרון]   B= [לא, מדובר, רק ,.. ]

B0Token: לא, B0_LastThreeLetters: �א, B0_LastTwoLetters: א, B1Token: מדובר, B1_LastThreeLetters: �ר, B1_LastTwoLetters: ר, S0B0Token: שרון_לא, S0B1Token: שרון_מדובר, S0B2Token: שרון_רק, S0Token: שרון, S0_LastThreeLetters: �ן, S0_LastTwoLetters: ן, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

24- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [לא, מדובר, רק ,.. ]

B0Token: לא, B0_LastThreeLetters: �א, B0_LastTwoLetters: א, B1Token: מדובר, B1_LastThreeLetters: �ר, B1_LastTwoLetters: ר, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

25- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [לא]   B= [מדובר, רק, בהתנתקות ,.. ]

B0Token: מדובר, B0_LastThreeLetters: �ר, B0_LastTwoLetters: ר, B1Token: רק, B1_LastThreeLetters: �ק, B1_LastTwoLetters: ק, S0B0Token: לא_מדובר, S0B1Token: לא_רק, S0B2Token: לא_בהתנתקות, S0Token: לא, S0_LastThreeLetters: �א, S0_LastTwoLetters: א, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

26- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [מדובר, רק, בהתנתקות ,.. ]

B0Token: מדובר, B0_LastThreeLetters: �ר, B0_LastTwoLetters: ר, B1Token: רק, B1_LastThreeLetters: �ק, B1_LastTwoLetters: ק, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

27- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [מדובר]   B= [רק, בהתנתקות, מחבל ,.. ]

B0Token: רק, B0_LastThreeLetters: �ק, B0_LastTwoLetters: ק, B1Token: בהתנתקות, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, S0B0Token: מדובר_רק, S0B1Token: מדובר_בהתנתקות, S0B2Token: מדובר_מחבל, S0Token: מדובר, S0_LastThreeLetters: �ר, S0_LastTwoLetters: ר, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

28- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [רק, בהתנתקות, מחבל ,.. ]

B0Token: רק, B0_LastThreeLetters: �ק, B0_LastTwoLetters: ק, B1Token: בהתנתקות, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

29- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [רק]   B= [בהתנתקות, מחבל, עזה ,.. ]

B0Token: בהתנתקות, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: מחבל, B1_LastThreeLetters: �ל, B1_LastTwoLetters: ל, S0B0Token: רק_בהתנתקות, S0B1Token: רק_מחבל, S0B2Token: רק_עזה, S0Token: רק, S0_LastThreeLetters: �ק, S0_LastTwoLetters: ק, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

30- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [בהתנתקות, מחבל, עזה ,.. ]

B0Token: בהתנתקות, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: מחבל, B1_LastThreeLetters: �ל, B1_LastTwoLetters: ל, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

31- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [בהתנתקות]   B= [מחבל, עזה, ולא ,.. ]

B0Token: מחבל, B0_LastThreeLetters: �ל, B0_LastTwoLetters: ל, B1Token: עזה, B1_LastThreeLetters: �ה, B1_LastTwoLetters: ה, S0B0Token: בהתנתקות_מחבל, S0B1Token: בהתנתקות_עזה, S0B2Token: בהתנתקות_ולא, S0Token: בהתנתקות, S0_LastThreeLetters: �ת, S0_LastTwoLetters: ת, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

32- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [מחבל, עזה, ולא ,.. ]

B0Token: מחבל, B0_LastThreeLetters: �ל, B0_LastTwoLetters: ל, B1Token: עזה, B1_LastThreeLetters: �ה, B1_LastTwoLetters: ה, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

33- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [מחבל]   B= [עזה, ולא, רק ,.. ]

B0Token: עזה, B0_LastThreeLetters: �ה, B0_LastTwoLetters: ה, B1Token: ולא, B1_LastThreeLetters: �א, B1_LastTwoLetters: א, S0B0Token: מחבל_עזה, S0B1Token: מחבל_ולא, S0B2Token: מחבל_רק, S0Token: מחבל, S0_LastThreeLetters: �ל, S0_LastTwoLetters: ל, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

34- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [עזה, ולא, רק ,.. ]

B0Token: עזה, B0_LastThreeLetters: �ה, B0_LastTwoLetters: ה, B1Token: ולא, B1_LastThreeLetters: �א, B1_LastTwoLetters: א, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

35- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [עזה]   B= [ולא, רק, בהרס ,.. ]

B0Token: ולא, B0_LastThreeLetters: �א, B0_LastTwoLetters: א, B1Token: רק, B1_LastThreeLetters: �ק, B1_LastTwoLetters: ק, S0B0Token: עזה_ולא, S0B1Token: עזה_רק, S0B2Token: עזה_בהרס, S0Token: עזה, S0_LastThreeLetters: �ה, S0_LastTwoLetters: ה, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

36- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ולא, רק, בהרס ,.. ]

B0Token: ולא, B0_LastThreeLetters: �א, B0_LastTwoLetters: א, B1Token: רק, B1_LastThreeLetters: �ק, B1_LastTwoLetters: ק, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

37- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ולא]   B= [רק, בהרס, ובחורבן ,.. ]

B0Token: רק, B0_LastThreeLetters: �ק, B0_LastTwoLetters: ק, B1Token: בהרס, B1_LastThreeLetters: �ס, B1_LastTwoLetters: ס, S0B0Token: ולא_רק, S0B1Token: ולא_בהרס, S0B2Token: ולא_ובחורבן, S0Token: ולא, S0_LastThreeLetters: �א, S0_LastTwoLetters: א, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

38- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [רק, בהרס, ובחורבן ,.. ]

B0Token: רק, B0_LastThreeLetters: �ק, B0_LastTwoLetters: ק, B1Token: בהרס, B1_LastThreeLetters: �ס, B1_LastTwoLetters: ס, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

39- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [רק]   B= [בהרס, ובחורבן, של ,.. ]

B0Token: בהרס, B0_LastThreeLetters: �ס, B0_LastTwoLetters: ס, B1Token: ובחורבן, B1_LastThreeLetters: �ן, B1_LastTwoLetters: ן, S0B0Token: רק_בהרס, S0B1Token: רק_ובחורבן, S0B2Token: רק_של, S0Token: רק, S0_LastThreeLetters: �ק, S0_LastTwoLetters: ק, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

40- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [בהרס, ובחורבן, של ,.. ]

B0Token: בהרס, B0_LastThreeLetters: �ס, B0_LastTwoLetters: ס, B1Token: ובחורבן, B1_LastThreeLetters: �ן, B1_LastTwoLetters: ן, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

41- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [בהרס]   B= [ובחורבן, של, גוש ,.. ]

B0Token: ובחורבן, B0_LastThreeLetters: �ן, B0_LastTwoLetters: ן, B1Token: של, B1_LastThreeLetters: �ל, B1_LastTwoLetters: ל, S0B0Token: בהרס_ובחורבן, S0B1Token: בהרס_של, S0B2Token: בהרס_גוש, S0Token: בהרס, S0_LastThreeLetters: �ס, S0_LastTwoLetters: ס, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

42- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ובחורבן, של, גוש ,.. ]

B0Token: ובחורבן, B0_LastThreeLetters: �ן, B0_LastTwoLetters: ן, B1Token: של, B1_LastThreeLetters: �ל, B1_LastTwoLetters: ל, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

43- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ובחורבן]   B= [של, גוש, קטיף ,.. ]

B0Token: של, B0_LastThreeLetters: �ל, B0_LastTwoLetters: ל, B1Token: גוש, B1_LastThreeLetters: �ש, B1_LastTwoLetters: ש, S0B0Token: ובחורבן_של, S0B1Token: ובחורבן_גוש, S0B2Token: ובחורבן_קטיף, S0Token: ובחורבן, S0_LastThreeLetters: �ן, S0_LastTwoLetters: ן, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

44- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [של, גוש, קטיף ,.. ]

B0Token: של, B0_LastThreeLetters: �ל, B0_LastTwoLetters: ל, B1Token: גוש, B1_LastThreeLetters: �ש, B1_LastTwoLetters: ש, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

45- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [של]   B= [גוש, קטיף ,.. ]

B0Token: גוש, B0_LastThreeLetters: �ש, B0_LastTwoLetters: ש, B1Token: קטיף, B1_LastThreeLetters: �ף, B1_LastTwoLetters: ף, S0B0Token: של_גוש, S0B1Token: של_קטיף, S0Token: של, S0_LastThreeLetters: �ל, S0_LastTwoLetters: ל, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

46- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [גוש, קטיף ,.. ]

B0Token: גוש, B0_LastThreeLetters: �ש, B0_LastTwoLetters: ש, B1Token: קטיף, B1_LastThreeLetters: �ף, B1_LastTwoLetters: ף, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

47- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [גוש]   B= [קטיף]

B0Token: קטיף, B0_LastThreeLetters: �ף, B0_LastTwoLetters: ף, S0B0Token: גוש_קטיף, S0Token: גוש, S0_LastThreeLetters: �ש, S0_LastTwoLetters: ש, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

48- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [קטיף]

B0Token: קטיף, B0_LastThreeLetters: �ף, B0_LastTwoLetters: ף, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

49- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [קטיף]   B= [ ]

S0Token: קטיף, S0_LastThreeLetters: �ף, S0_LastTwoLetters: ף, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

50- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

## Sentence No. 173 - 
מה היה לה לתנועה איך איבדה דרכה איך אפשרנו להם לגנוב את הדרך ולהפוך את כל העשייה והבניה של הליכוד של תנועת החירות זה עשרות שנים ללעג ולקלס תהה ריבלין
### Existing MWEs: 
1- **איבדה דרכה** (ID)
2- **ולהפוך ללעג ולקלס** (VPC)



0- &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [מה, היה, לה ,.. ]

B0Token: מה, B0_LastThreeLetters: �ה, B0_LastTwoLetters: ה, B1Token: היה, B1_LastThreeLetters: �ה, B1_LastTwoLetters: ה, 

1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [מה]   B= [היה, לה, לתנועה ,.. ]

B0Token: היה, B0_LastThreeLetters: �ה, B0_LastTwoLetters: ה, B1Token: לה, B1_LastThreeLetters: �ה, B1_LastTwoLetters: ה, S0B0Token: מה_היה, S0B1Token: מה_לה, S0B2Token: מה_לתנועה, S0Token: מה, S0_LastThreeLetters: �ה, S0_LastTwoLetters: ה, 

2- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [היה, לה, לתנועה ,.. ]

B0Token: היה, B0_LastThreeLetters: �ה, B0_LastTwoLetters: ה, B1Token: לה, B1_LastThreeLetters: �ה, B1_LastTwoLetters: ה, TransHistory1: 0, 

3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [היה]   B= [לה, לתנועה, איך ,.. ]

B0Token: לה, B0_LastThreeLetters: �ה, B0_LastTwoLetters: ה, B1Token: לתנועה, B1_LastThreeLetters: �ה, B1_LastTwoLetters: ה, S0B0Token: היה_לה, S0B1Token: היה_לתנועה, S0B2Token: היה_איך, S0Token: היה, S0_LastThreeLetters: �ה, S0_LastTwoLetters: ה, TransHistory1: 2, TransHistory2: 20, 

4- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [לה, לתנועה, איך ,.. ]

B0Token: לה, B0_LastThreeLetters: �ה, B0_LastTwoLetters: ה, B1Token: לתנועה, B1_LastThreeLetters: �ה, B1_LastTwoLetters: ה, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [לה]   B= [לתנועה, איך, איבדה ,.. ]

B0Token: לתנועה, B0_LastThreeLetters: �ה, B0_LastTwoLetters: ה, B1Token: איך, B1_LastThreeLetters: �ך, B1_LastTwoLetters: ך, S0B0Token: לה_לתנועה, S0B1Token: לה_איך, S0B2Token: לה_איבדה, S0Token: לה, S0_LastThreeLetters: �ה, S0_LastTwoLetters: ה, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

6- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [לתנועה, איך, איבדה ,.. ]

B0Token: לתנועה, B0_LastThreeLetters: �ה, B0_LastTwoLetters: ה, B1Token: איך, B1_LastThreeLetters: �ך, B1_LastTwoLetters: ך, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [לתנועה]   B= [איך, איבדה, דרכה ,.. ]

B0Token: איך, B0_LastThreeLetters: �ך, B0_LastTwoLetters: ך, B1Token: איבדה, B1_LastThreeLetters: �ה, B1_LastTwoLetters: ה, S0B0Token: לתנועה_איך, S0B1Token: לתנועה_איבדה, S0B2Token: לתנועה_דרכה, S0Token: לתנועה, S0_LastThreeLetters: �ה, S0_LastTwoLetters: ה, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

8- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [איך, איבדה, דרכה ,.. ]

B0Token: איך, B0_LastThreeLetters: �ך, B0_LastTwoLetters: ך, B1Token: איבדה, B1_LastThreeLetters: �ה, B1_LastTwoLetters: ה, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [איך]   B= [איבדה, דרכה, איך ,.. ]

B0Token: איבדה, B0_LastThreeLetters: �ה, B0_LastTwoLetters: ה, B1Token: דרכה, B1_LastThreeLetters: �ה, B1_LastTwoLetters: ה, S0B0Token: איך_איבדה, S0B1Token: איך_דרכה, S0B2Token: איך_איך, S0Token: איך, S0_LastThreeLetters: �ך, S0_LastTwoLetters: ך, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

10- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [איבדה, דרכה, איך ,.. ]

B0Token: איבדה, B0_LastThreeLetters: �ה, B0_LastTwoLetters: ה, B1Token: דרכה, B1_LastThreeLetters: �ה, B1_LastTwoLetters: ה, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [איבדה]   B= [דרכה, איך, אפשרנו ,.. ]

B0Token: דרכה, B0_LastThreeLetters: �ה, B0_LastTwoLetters: ה, B1Token: איך, B1_LastThreeLetters: �ך, B1_LastTwoLetters: ך, S0B0Token: איבדה_דרכה, S0B1Token: איבדה_איך, S0B2Token: איבדה_אפשרנו, S0Token: איבדה, S0_LastThreeLetters: �ה, S0_LastTwoLetters: ה, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

12- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [איבדה, דרכה]   B= [איך, אפשרנו, להם ,.. ]

B0Token: איך, B0_LastThreeLetters: �ך, B0_LastTwoLetters: ך, B1Token: אפשרנו, B1_LastThreeLetters: �ו, B1_LastTwoLetters: ו, S0B0Token: דרכה_איך, S0B1Token: דרכה_אפשרנו, S0B2Token: דרכה_להם, S0Token: דרכה, S0_LastThreeLetters: �ה, S0_LastTwoLetters: ה, S1B0Token: איבדה_איך, S1S0Token: איבדה_דרכה, S1Token: איבדה, S1_LastThreeLetters: �ה, S1_LastTwoLetters: ה, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

13- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[איבדה, דרכה]]   B= [איך, אפשרנו, להם ,.. ]

B0Token: איך, B0_LastThreeLetters: �ך, B0_LastTwoLetters: ך, B1Token: אפשרנו, B1_LastThreeLetters: �ו, B1_LastTwoLetters: ו, S0B0Token: איבדה_דרכה_איך, S0B1Token: איבדה_דרכה_אפשרנו, S0B2Token: איבדה_דרכה_להם, S0Token: איבדה_דרכה, TransHistory1: 0, TransHistory2: 00, TransHistory3: 002, 

14- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [איך, אפשרנו, להם ,.. ]

B0Token: איך, B0_LastThreeLetters: �ך, B0_LastTwoLetters: ך, B1Token: אפשרנו, B1_LastThreeLetters: �ו, B1_LastTwoLetters: ו, TransHistory1: 1, TransHistory2: 10, TransHistory3: 100, 

15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [איך]   B= [אפשרנו, להם, לגנוב ,.. ]

B0Token: אפשרנו, B0_LastThreeLetters: �ו, B0_LastTwoLetters: ו, B1Token: להם, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, S0B0Token: איך_אפשרנו, S0B1Token: איך_להם, S0B2Token: איך_לגנוב, S0Token: איך, S0_LastThreeLetters: �ך, S0_LastTwoLetters: ך, TransHistory1: 2, TransHistory2: 21, TransHistory3: 210, 

16- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [אפשרנו, להם, לגנוב ,.. ]

B0Token: אפשרנו, B0_LastThreeLetters: �ו, B0_LastTwoLetters: ו, B1Token: להם, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, TransHistory1: 0, TransHistory2: 02, TransHistory3: 021, 

17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [אפשרנו]   B= [להם, לגנוב, את ,.. ]

B0Token: להם, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, B1Token: לגנוב, B1_LastThreeLetters: �ב, B1_LastTwoLetters: ב, S0B0Token: אפשרנו_להם, S0B1Token: אפשרנו_לגנוב, S0B2Token: אפשרנו_את, S0Token: אפשרנו, S0_LastThreeLetters: �ו, S0_LastTwoLetters: ו, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

18- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [להם, לגנוב, את ,.. ]

B0Token: להם, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, B1Token: לגנוב, B1_LastThreeLetters: �ב, B1_LastTwoLetters: ב, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [להם]   B= [לגנוב, את, הדרך ,.. ]

B0Token: לגנוב, B0_LastThreeLetters: �ב, B0_LastTwoLetters: ב, B1Token: את, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, S0B0Token: להם_לגנוב, S0B1Token: להם_את, S0B2Token: להם_הדרך, S0Token: להם, S0_LastThreeLetters: �ם, S0_LastTwoLetters: ם, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

20- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [לגנוב, את, הדרך ,.. ]

B0Token: לגנוב, B0_LastThreeLetters: �ב, B0_LastTwoLetters: ב, B1Token: את, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [לגנוב]   B= [את, הדרך, ולהפוך ,.. ]

B0Token: את, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: הדרך, B1_LastThreeLetters: �ך, B1_LastTwoLetters: ך, S0B0Token: לגנוב_את, S0B1Token: לגנוב_הדרך, S0B2Token: לגנוב_ולהפוך, S0Token: לגנוב, S0_LastThreeLetters: �ב, S0_LastTwoLetters: ב, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

22- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [את, הדרך, ולהפוך ,.. ]

B0Token: את, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: הדרך, B1_LastThreeLetters: �ך, B1_LastTwoLetters: ך, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

23- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [את]   B= [הדרך, ולהפוך, את ,.. ]

B0Token: הדרך, B0_LastThreeLetters: �ך, B0_LastTwoLetters: ך, B1Token: ולהפוך, B1_LastThreeLetters: �ך, B1_LastTwoLetters: ך, S0B0Token: את_הדרך, S0B1Token: את_ולהפוך, S0B2Token: את_את, S0Token: את, S0_LastThreeLetters: �ת, S0_LastTwoLetters: ת, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

24- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [הדרך, ולהפוך, את ,.. ]

B0Token: הדרך, B0_LastThreeLetters: �ך, B0_LastTwoLetters: ך, B1Token: ולהפוך, B1_LastThreeLetters: �ך, B1_LastTwoLetters: ך, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

25- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [הדרך]   B= [ולהפוך, את, כל ,.. ]

B0Token: ולהפוך, B0_LastThreeLetters: �ך, B0_LastTwoLetters: ך, B1Token: את, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, S0B0Token: הדרך_ולהפוך, S0B1Token: הדרך_את, S0B2Token: הדרך_כל, S0Token: הדרך, S0_LastThreeLetters: �ך, S0_LastTwoLetters: ך, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

26- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ולהפוך, את, כל ,.. ]

B0Token: ולהפוך, B0_LastThreeLetters: �ך, B0_LastTwoLetters: ך, B1Token: את, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

27- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ולהפוך]   B= [את, כל, העשייה ,.. ]

B0Token: את, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: כל, B1_LastThreeLetters: �ל, B1_LastTwoLetters: ל, S0B0Token: ולהפוך_את, S0B1Token: ולהפוך_כל, S0B2Token: ולהפוך_העשייה, S0Token: ולהפוך, S0_LastThreeLetters: �ך, S0_LastTwoLetters: ך, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

28- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ולהפוך, את]   B= [כל, העשייה, והבניה ,.. ]

B0Token: כל, B0_LastThreeLetters: �ל, B0_LastTwoLetters: ל, B1Token: העשייה, B1_LastThreeLetters: �ה, B1_LastTwoLetters: ה, S0B0Token: את_כל, S0B1Token: את_העשייה, S0B2Token: את_והבניה, S0Token: את, S0_LastThreeLetters: �ת, S0_LastTwoLetters: ת, S1B0Token: ולהפוך_כל, S1S0Token: ולהפוך_את, S1Token: ולהפוך, S1_LastThreeLetters: �ך, S1_LastTwoLetters: ך, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

29- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ולהפוך]   B= [כל, העשייה, והבניה ,.. ]

B0Token: כל, B0_LastThreeLetters: �ל, B0_LastTwoLetters: ל, B1Token: העשייה, B1_LastThreeLetters: �ה, B1_LastTwoLetters: ה, S0B0Token: ולהפוך_כל, S0B1Token: ולהפוך_העשייה, S0B2Token: ולהפוך_והבניה, S0Token: ולהפוך, S0_LastThreeLetters: �ך, S0_LastTwoLetters: ך, TransHistory1: 0, TransHistory2: 00, TransHistory3: 002, 

30- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ולהפוך, כל]   B= [העשייה, והבניה, של ,.. ]

B0Token: העשייה, B0_LastThreeLetters: �ה, B0_LastTwoLetters: ה, B1Token: והבניה, B1_LastThreeLetters: �ה, B1_LastTwoLetters: ה, S0B0Token: כל_העשייה, S0B1Token: כל_והבניה, S0B2Token: כל_של, S0Token: כל, S0_LastThreeLetters: �ל, S0_LastTwoLetters: ל, S1B0Token: ולהפוך_העשייה, S1S0Token: ולהפוך_כל, S1Token: ולהפוך, S1_LastThreeLetters: �ך, S1_LastTwoLetters: ך, TransHistory1: 2, TransHistory2: 20, TransHistory3: 200, 

31- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ולהפוך]   B= [העשייה, והבניה, של ,.. ]

B0Token: העשייה, B0_LastThreeLetters: �ה, B0_LastTwoLetters: ה, B1Token: והבניה, B1_LastThreeLetters: �ה, B1_LastTwoLetters: ה, S0B0Token: ולהפוך_העשייה, S0B1Token: ולהפוך_והבניה, S0B2Token: ולהפוך_של, S0Token: ולהפוך, S0_LastThreeLetters: �ך, S0_LastTwoLetters: ך, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

32- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ולהפוך, העשייה]   B= [והבניה, של, הליכוד ,.. ]

B0Token: והבניה, B0_LastThreeLetters: �ה, B0_LastTwoLetters: ה, B1Token: של, B1_LastThreeLetters: �ל, B1_LastTwoLetters: ל, S0B0Token: העשייה_והבניה, S0B1Token: העשייה_של, S0B2Token: העשייה_הליכוד, S0Token: העשייה, S0_LastThreeLetters: �ה, S0_LastTwoLetters: ה, S1B0Token: ולהפוך_והבניה, S1S0Token: ולהפוך_העשייה, S1Token: ולהפוך, S1_LastThreeLetters: �ך, S1_LastTwoLetters: ך, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

33- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ולהפוך]   B= [והבניה, של, הליכוד ,.. ]

B0Token: והבניה, B0_LastThreeLetters: �ה, B0_LastTwoLetters: ה, B1Token: של, B1_LastThreeLetters: �ל, B1_LastTwoLetters: ל, S0B0Token: ולהפוך_והבניה, S0B1Token: ולהפוך_של, S0B2Token: ולהפוך_הליכוד, S0Token: ולהפוך, S0_LastThreeLetters: �ך, S0_LastTwoLetters: ך, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

34- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ולהפוך, והבניה]   B= [של, הליכוד, של ,.. ]

B0Token: של, B0_LastThreeLetters: �ל, B0_LastTwoLetters: ל, B1Token: הליכוד, B1_LastThreeLetters: �ד, B1_LastTwoLetters: ד, S0B0Token: והבניה_של, S0B1Token: והבניה_הליכוד, S0B2Token: והבניה_של, S0Token: והבניה, S0_LastThreeLetters: �ה, S0_LastTwoLetters: ה, S1B0Token: ולהפוך_של, S1S0Token: ולהפוך_והבניה, S1Token: ולהפוך, S1_LastThreeLetters: �ך, S1_LastTwoLetters: ך, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

35- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ולהפוך]   B= [של, הליכוד, של ,.. ]

B0Token: של, B0_LastThreeLetters: �ל, B0_LastTwoLetters: ל, B1Token: הליכוד, B1_LastThreeLetters: �ד, B1_LastTwoLetters: ד, S0B0Token: ולהפוך_של, S0B1Token: ולהפוך_הליכוד, S0B2Token: ולהפוך_של, S0Token: ולהפוך, S0_LastThreeLetters: �ך, S0_LastTwoLetters: ך, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

36- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ולהפוך, של]   B= [הליכוד, של, תנועת ,.. ]

B0Token: הליכוד, B0_LastThreeLetters: �ד, B0_LastTwoLetters: ד, B1Token: של, B1_LastThreeLetters: �ל, B1_LastTwoLetters: ל, S0B0Token: של_הליכוד, S0B1Token: של_של, S0B2Token: של_תנועת, S0Token: של, S0_LastThreeLetters: �ל, S0_LastTwoLetters: ל, S1B0Token: ולהפוך_הליכוד, S1S0Token: ולהפוך_של, S1Token: ולהפוך, S1_LastThreeLetters: �ך, S1_LastTwoLetters: ך, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

37- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ולהפוך]   B= [הליכוד, של, תנועת ,.. ]

B0Token: הליכוד, B0_LastThreeLetters: �ד, B0_LastTwoLetters: ד, B1Token: של, B1_LastThreeLetters: �ל, B1_LastTwoLetters: ל, S0B0Token: ולהפוך_הליכוד, S0B1Token: ולהפוך_של, S0B2Token: ולהפוך_תנועת, S0Token: ולהפוך, S0_LastThreeLetters: �ך, S0_LastTwoLetters: ך, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

38- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ולהפוך, הליכוד]   B= [של, תנועת, החירות ,.. ]

B0Token: של, B0_LastThreeLetters: �ל, B0_LastTwoLetters: ל, B1Token: תנועת, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, S0B0Token: הליכוד_של, S0B1Token: הליכוד_תנועת, S0B2Token: הליכוד_החירות, S0Token: הליכוד, S0_LastThreeLetters: �ד, S0_LastTwoLetters: ד, S1B0Token: ולהפוך_של, S1S0Token: ולהפוך_הליכוד, S1Token: ולהפוך, S1_LastThreeLetters: �ך, S1_LastTwoLetters: ך, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

39- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ולהפוך]   B= [של, תנועת, החירות ,.. ]

B0Token: של, B0_LastThreeLetters: �ל, B0_LastTwoLetters: ל, B1Token: תנועת, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, S0B0Token: ולהפוך_של, S0B1Token: ולהפוך_תנועת, S0B2Token: ולהפוך_החירות, S0Token: ולהפוך, S0_LastThreeLetters: �ך, S0_LastTwoLetters: ך, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

40- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ולהפוך, של]   B= [תנועת, החירות, זה ,.. ]

B0Token: תנועת, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: החירות, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, S0B0Token: של_תנועת, S0B1Token: של_החירות, S0B2Token: של_זה, S0Token: של, S0_LastThreeLetters: �ל, S0_LastTwoLetters: ל, S1B0Token: ולהפוך_תנועת, S1S0Token: ולהפוך_של, S1Token: ולהפוך, S1_LastThreeLetters: �ך, S1_LastTwoLetters: ך, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

41- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ולהפוך]   B= [תנועת, החירות, זה ,.. ]

B0Token: תנועת, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: החירות, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, S0B0Token: ולהפוך_תנועת, S0B1Token: ולהפוך_החירות, S0B2Token: ולהפוך_זה, S0Token: ולהפוך, S0_LastThreeLetters: �ך, S0_LastTwoLetters: ך, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

42- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ולהפוך, תנועת]   B= [החירות, זה, עשרות ,.. ]

B0Token: החירות, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: זה, B1_LastThreeLetters: �ה, B1_LastTwoLetters: ה, S0B0Token: תנועת_החירות, S0B1Token: תנועת_זה, S0B2Token: תנועת_עשרות, S0Token: תנועת, S0_LastThreeLetters: �ת, S0_LastTwoLetters: ת, S1B0Token: ולהפוך_החירות, S1S0Token: ולהפוך_תנועת, S1Token: ולהפוך, S1_LastThreeLetters: �ך, S1_LastTwoLetters: ך, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

43- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ולהפוך]   B= [החירות, זה, עשרות ,.. ]

B0Token: החירות, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: זה, B1_LastThreeLetters: �ה, B1_LastTwoLetters: ה, S0B0Token: ולהפוך_החירות, S0B1Token: ולהפוך_זה, S0B2Token: ולהפוך_עשרות, S0Token: ולהפוך, S0_LastThreeLetters: �ך, S0_LastTwoLetters: ך, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

44- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ולהפוך, החירות]   B= [זה, עשרות, שנים ,.. ]

B0Token: זה, B0_LastThreeLetters: �ה, B0_LastTwoLetters: ה, B1Token: עשרות, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, S0B0Token: החירות_זה, S0B1Token: החירות_עשרות, S0B2Token: החירות_שנים, S0Token: החירות, S0_LastThreeLetters: �ת, S0_LastTwoLetters: ת, S1B0Token: ולהפוך_זה, S1S0Token: ולהפוך_החירות, S1Token: ולהפוך, S1_LastThreeLetters: �ך, S1_LastTwoLetters: ך, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

45- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ולהפוך]   B= [זה, עשרות, שנים ,.. ]

B0Token: זה, B0_LastThreeLetters: �ה, B0_LastTwoLetters: ה, B1Token: עשרות, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, S0B0Token: ולהפוך_זה, S0B1Token: ולהפוך_עשרות, S0B2Token: ולהפוך_שנים, S0Token: ולהפוך, S0_LastThreeLetters: �ך, S0_LastTwoLetters: ך, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

46- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ולהפוך, זה]   B= [עשרות, שנים, ללעג ,.. ]

B0Token: עשרות, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: שנים, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, S0B0Token: זה_עשרות, S0B1Token: זה_שנים, S0B2Token: זה_ללעג, S0Token: זה, S0_LastThreeLetters: �ה, S0_LastTwoLetters: ה, S1B0Token: ולהפוך_עשרות, S1S0Token: ולהפוך_זה, S1Token: ולהפוך, S1_LastThreeLetters: �ך, S1_LastTwoLetters: ך, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

47- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ולהפוך]   B= [עשרות, שנים, ללעג ,.. ]

B0Token: עשרות, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: שנים, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, S0B0Token: ולהפוך_עשרות, S0B1Token: ולהפוך_שנים, S0B2Token: ולהפוך_ללעג, S0Token: ולהפוך, S0_LastThreeLetters: �ך, S0_LastTwoLetters: ך, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

48- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ולהפוך, עשרות]   B= [שנים, ללעג, ולקלס ,.. ]

B0Token: שנים, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, B1Token: ללעג, B1_LastThreeLetters: �ג, B1_LastTwoLetters: ג, S0B0Token: עשרות_שנים, S0B1Token: עשרות_ללעג, S0B2Token: עשרות_ולקלס, S0Token: עשרות, S0_LastThreeLetters: �ת, S0_LastTwoLetters: ת, S1B0Token: ולהפוך_שנים, S1S0Token: ולהפוך_עשרות, S1Token: ולהפוך, S1_LastThreeLetters: �ך, S1_LastTwoLetters: ך, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

49- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ולהפוך]   B= [שנים, ללעג, ולקלס ,.. ]

B0Token: שנים, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, B1Token: ללעג, B1_LastThreeLetters: �ג, B1_LastTwoLetters: ג, S0B0Token: ולהפוך_שנים, S0B1Token: ולהפוך_ללעג, S0B2Token: ולהפוך_ולקלס, S0Token: ולהפוך, S0_LastThreeLetters: �ך, S0_LastTwoLetters: ך, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

50- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ולהפוך, שנים]   B= [ללעג, ולקלס, תהה ,.. ]

B0Token: ללעג, B0_LastThreeLetters: �ג, B0_LastTwoLetters: ג, B1Token: ולקלס, B1_LastThreeLetters: �ס, B1_LastTwoLetters: ס, S0B0Token: שנים_ללעג, S0B1Token: שנים_ולקלס, S0B2Token: שנים_תהה, S0Token: שנים, S0_LastThreeLetters: �ם, S0_LastTwoLetters: ם, S1B0Token: ולהפוך_ללעג, S1S0Token: ולהפוך_שנים, S1Token: ולהפוך, S1_LastThreeLetters: �ך, S1_LastTwoLetters: ך, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

51- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ולהפוך]   B= [ללעג, ולקלס, תהה ,.. ]

B0Token: ללעג, B0_LastThreeLetters: �ג, B0_LastTwoLetters: ג, B1Token: ולקלס, B1_LastThreeLetters: �ס, B1_LastTwoLetters: ס, S0B0Token: ולהפוך_ללעג, S0B1Token: ולהפוך_ולקלס, S0B2Token: ולהפוך_תהה, S0Token: ולהפוך, S0_LastThreeLetters: �ך, S0_LastTwoLetters: ך, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

52- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ולהפוך, ללעג]   B= [ולקלס, תהה, ריבלין ,.. ]

B0Token: ולקלס, B0_LastThreeLetters: �ס, B0_LastTwoLetters: ס, B1Token: תהה, B1_LastThreeLetters: �ה, B1_LastTwoLetters: ה, S0B0Token: ללעג_ולקלס, S0B1Token: ללעג_תהה, S0B2Token: ללעג_ריבלין, S0Token: ללעג, S0_LastThreeLetters: �ג, S0_LastTwoLetters: ג, S1B0Token: ולהפוך_ולקלס, S1S0Token: ולהפוך_ללעג, S1Token: ולהפוך, S1_LastThreeLetters: �ך, S1_LastTwoLetters: ך, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

53- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ולהפוך, ללעג, ולקלס]   B= [תהה, ריבלין ,.. ]

B0Token: תהה, B0_LastThreeLetters: �ה, B0_LastTwoLetters: ה, B1Token: ריבלין, B1_LastThreeLetters: �ן, B1_LastTwoLetters: ן, S0B0Token: ולקלס_תהה, S0B1Token: ולקלס_ריבלין, S0Token: ולקלס, S0_LastThreeLetters: �ס, S0_LastTwoLetters: ס, S1B0Token: ללעג_תהה, S1S0Token: ללעג_ולקלס, S1Token: ללעג, S1_LastThreeLetters: �ג, S1_LastTwoLetters: ג, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

54- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ולהפוך, [ללעג, ולקלס]]   B= [תהה, ריבלין ,.. ]

B0Token: תהה, B0_LastThreeLetters: �ה, B0_LastTwoLetters: ה, B1Token: ריבלין, B1_LastThreeLetters: �ן, B1_LastTwoLetters: ן, S0B0Token: ללעג_ולקלס_תהה, S0B1Token: ללעג_ולקלס_ריבלין, S0Token: ללעג_ולקלס, S1B0Token: ולהפוך_תהה, S1S0Token: ולהפוך_ללעג_ולקלס, S1Token: ולהפוך, S1_LastThreeLetters: �ך, S1_LastTwoLetters: ך, TransHistory1: 0, TransHistory2: 00, TransHistory3: 002, 

55- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[ולהפוך, [ללעג, ולקלס]]]   B= [תהה, ריבלין ,.. ]

B0Token: תהה, B0_LastThreeLetters: �ה, B0_LastTwoLetters: ה, B1Token: ריבלין, B1_LastThreeLetters: �ן, B1_LastTwoLetters: ן, S0B0Token: ולהפוך_ללעג_ולקלס_תהה, S0B1Token: ולהפוך_ללעג_ולקלס_ריבלין, S0Token: ולהפוך_ללעג_ולקלס, TransHistory1: 1, TransHistory2: 10, TransHistory3: 100, 

56- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [תהה, ריבלין ,.. ]

B0Token: תהה, B0_LastThreeLetters: �ה, B0_LastTwoLetters: ה, B1Token: ריבלין, B1_LastThreeLetters: �ן, B1_LastTwoLetters: ן, TransHistory1: 1, TransHistory2: 11, TransHistory3: 110, 

57- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [תהה]   B= [ריבלין]

B0Token: ריבלין, B0_LastThreeLetters: �ן, B0_LastTwoLetters: ן, S0B0Token: תהה_ריבלין, S0Token: תהה, S0_LastThreeLetters: �ה, S0_LastTwoLetters: ה, TransHistory1: 2, TransHistory2: 21, TransHistory3: 211, 

58- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ריבלין]

B0Token: ריבלין, B0_LastThreeLetters: �ן, B0_LastTwoLetters: ן, TransHistory1: 0, TransHistory2: 02, TransHistory3: 021, 

59- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ריבלין]   B= [ ]

S0Token: ריבלין, S0_LastThreeLetters: �ן, S0_LastTwoLetters: ן, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

60- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

## Sentence No. 218 - 
אם עד כה נאמר על המחשב שהוא גולם הקם על יוצרו הרי שמעתה ניתן לומר שהוא רק קם על יוצרו אלא אפילו נוזף בו ומנסה לעצב אותו מחדש
### Existing MWEs: 
1- **גולם הקם על יוצרו** (VPC)
2- **קם על יוצרו** (VPC)



0- &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [אם, עד, כה ,.. ]

B0Token: אם, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, B1Token: עד, B1_LastThreeLetters: �ד, B1_LastTwoLetters: ד, 

1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [אם]   B= [עד, כה, נאמר ,.. ]

B0Token: עד, B0_LastThreeLetters: �ד, B0_LastTwoLetters: ד, B1Token: כה, B1_LastThreeLetters: �ה, B1_LastTwoLetters: ה, S0B0Token: אם_עד, S0B1Token: אם_כה, S0B2Token: אם_נאמר, S0Token: אם, S0_LastThreeLetters: �ם, S0_LastTwoLetters: ם, 

2- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [עד, כה, נאמר ,.. ]

B0Token: עד, B0_LastThreeLetters: �ד, B0_LastTwoLetters: ד, B1Token: כה, B1_LastThreeLetters: �ה, B1_LastTwoLetters: ה, TransHistory1: 0, 

3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [עד]   B= [כה, נאמר, על ,.. ]

B0Token: כה, B0_LastThreeLetters: �ה, B0_LastTwoLetters: ה, B1Token: נאמר, B1_LastThreeLetters: �ר, B1_LastTwoLetters: ר, S0B0Token: עד_כה, S0B1Token: עד_נאמר, S0B2Token: עד_על, S0Token: עד, S0_LastThreeLetters: �ד, S0_LastTwoLetters: ד, TransHistory1: 2, TransHistory2: 20, 

4- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [כה, נאמר, על ,.. ]

B0Token: כה, B0_LastThreeLetters: �ה, B0_LastTwoLetters: ה, B1Token: נאמר, B1_LastThreeLetters: �ר, B1_LastTwoLetters: ר, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [כה]   B= [נאמר, על, המחשב ,.. ]

B0Token: נאמר, B0_LastThreeLetters: �ר, B0_LastTwoLetters: ר, B1Token: על, B1_LastThreeLetters: �ל, B1_LastTwoLetters: ל, S0B0Token: כה_נאמר, S0B1Token: כה_על, S0B2Token: כה_המחשב, S0Token: כה, S0_LastThreeLetters: �ה, S0_LastTwoLetters: ה, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

6- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [נאמר, על, המחשב ,.. ]

B0Token: נאמר, B0_LastThreeLetters: �ר, B0_LastTwoLetters: ר, B1Token: על, B1_LastThreeLetters: �ל, B1_LastTwoLetters: ל, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [נאמר]   B= [על, המחשב, שהוא ,.. ]

B0Token: על, B0_LastThreeLetters: �ל, B0_LastTwoLetters: ל, B1Token: המחשב, B1_LastThreeLetters: �ב, B1_LastTwoLetters: ב, S0B0Token: נאמר_על, S0B1Token: נאמר_המחשב, S0B2Token: נאמר_שהוא, S0Token: נאמר, S0_LastThreeLetters: �ר, S0_LastTwoLetters: ר, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

8- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [על, המחשב, שהוא ,.. ]

B0Token: על, B0_LastThreeLetters: �ל, B0_LastTwoLetters: ל, B1Token: המחשב, B1_LastThreeLetters: �ב, B1_LastTwoLetters: ב, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [על]   B= [המחשב, שהוא, גולם ,.. ]

B0Token: המחשב, B0_LastThreeLetters: �ב, B0_LastTwoLetters: ב, B1Token: שהוא, B1_LastThreeLetters: �א, B1_LastTwoLetters: א, S0B0Token: על_המחשב, S0B1Token: על_שהוא, S0B2Token: על_גולם, S0Token: על, S0_LastThreeLetters: �ל, S0_LastTwoLetters: ל, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

10- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [המחשב, שהוא, גולם ,.. ]

B0Token: המחשב, B0_LastThreeLetters: �ב, B0_LastTwoLetters: ב, B1Token: שהוא, B1_LastThreeLetters: �א, B1_LastTwoLetters: א, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [המחשב]   B= [שהוא, גולם, הקם ,.. ]

B0Token: שהוא, B0_LastThreeLetters: �א, B0_LastTwoLetters: א, B1Token: גולם, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, S0B0Token: המחשב_שהוא, S0B1Token: המחשב_גולם, S0B2Token: המחשב_הקם, S0Token: המחשב, S0_LastThreeLetters: �ב, S0_LastTwoLetters: ב, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

12- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [שהוא, גולם, הקם ,.. ]

B0Token: שהוא, B0_LastThreeLetters: �א, B0_LastTwoLetters: א, B1Token: גולם, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [שהוא]   B= [גולם, הקם, על ,.. ]

B0Token: גולם, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, B1Token: הקם, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, S0B0Token: שהוא_גולם, S0B1Token: שהוא_הקם, S0B2Token: שהוא_על, S0Token: שהוא, S0_LastThreeLetters: �א, S0_LastTwoLetters: א, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

14- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [גולם, הקם, על ,.. ]

B0Token: גולם, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, B1Token: הקם, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [גולם]   B= [הקם, על, יוצרו ,.. ]

B0Token: הקם, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, B1Token: על, B1_LastThreeLetters: �ל, B1_LastTwoLetters: ל, S0B0Token: גולם_הקם, S0B1Token: גולם_על, S0B2Token: גולם_יוצרו, S0Token: גולם, S0_LastThreeLetters: �ם, S0_LastTwoLetters: ם, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

16- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [גולם, הקם]   B= [על, יוצרו, הרי ,.. ]

B0Token: על, B0_LastThreeLetters: �ל, B0_LastTwoLetters: ל, B1Token: יוצרו, B1_LastThreeLetters: �ו, B1_LastTwoLetters: ו, S0B0Token: הקם_על, S0B1Token: הקם_יוצרו, S0B2Token: הקם_הרי, S0Token: הקם, S0_LastThreeLetters: �ם, S0_LastTwoLetters: ם, S1B0Token: גולם_על, S1S0Token: גולם_הקם, S1Token: גולם, S1_LastThreeLetters: �ם, S1_LastTwoLetters: ם, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [גולם, הקם, על]   B= [יוצרו, הרי, שמעתה ,.. ]

B0Token: יוצרו, B0_LastThreeLetters: �ו, B0_LastTwoLetters: ו, B1Token: הרי, B1_LastThreeLetters: �י, B1_LastTwoLetters: י, S0B0Token: על_יוצרו, S0B1Token: על_הרי, S0B2Token: על_שמעתה, S0Token: על, S0_LastThreeLetters: �ל, S0_LastTwoLetters: ל, S1B0Token: הקם_יוצרו, S1S0Token: הקם_על, S1Token: הקם, S1_LastThreeLetters: �ם, S1_LastTwoLetters: ם, TransHistory1: 0, TransHistory2: 00, TransHistory3: 002, 

18- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [גולם, הקם, על, יוצרו]   B= [הרי, שמעתה, ניתן ,.. ]

B0Token: הרי, B0_LastThreeLetters: �י, B0_LastTwoLetters: י, B1Token: שמעתה, B1_LastThreeLetters: �ה, B1_LastTwoLetters: ה, S0B0Token: יוצרו_הרי, S0B1Token: יוצרו_שמעתה, S0B2Token: יוצרו_ניתן, S0Token: יוצרו, S0_LastThreeLetters: �ו, S0_LastTwoLetters: ו, S1B0Token: על_הרי, S1S0Token: על_יוצרו, S1Token: על, S1_LastThreeLetters: �ל, S1_LastTwoLetters: ל, TransHistory1: 0, TransHistory2: 00, TransHistory3: 000, 

19- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [גולם, הקם, [על, יוצרו]]   B= [הרי, שמעתה, ניתן ,.. ]

B0Token: הרי, B0_LastThreeLetters: �י, B0_LastTwoLetters: י, B1Token: שמעתה, B1_LastThreeLetters: �ה, B1_LastTwoLetters: ה, S0B0Token: על_יוצרו_הרי, S0B1Token: על_יוצרו_שמעתה, S0B2Token: על_יוצרו_ניתן, S0Token: על_יוצרו, S1B0Token: הקם_הרי, S1S0Token: הקם_על_יוצרו, S1Token: הקם, S1_LastThreeLetters: �ם, S1_LastTwoLetters: ם, TransHistory1: 0, TransHistory2: 00, TransHistory3: 000, 

20- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [גולם, [הקם, [על, יוצרו]]]   B= [הרי, שמעתה, ניתן ,.. ]

B0Token: הרי, B0_LastThreeLetters: �י, B0_LastTwoLetters: י, B1Token: שמעתה, B1_LastThreeLetters: �ה, B1_LastTwoLetters: ה, S0B0Token: הקם_על_יוצרו_הרי, S0B1Token: הקם_על_יוצרו_שמעתה, S0B2Token: הקם_על_יוצרו_ניתן, S0Token: הקם_על_יוצרו, S1B0Token: גולם_הרי, S1S0Token: גולם_הקם_על_יוצרו, S1Token: גולם, S1_LastThreeLetters: �ם, S1_LastTwoLetters: ם, TransHistory1: 1, TransHistory2: 10, TransHistory3: 100, 

21- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[גולם, [הקם, [על, יוצרו]]]]   B= [הרי, שמעתה, ניתן ,.. ]

B0Token: הרי, B0_LastThreeLetters: �י, B0_LastTwoLetters: י, B1Token: שמעתה, B1_LastThreeLetters: �ה, B1_LastTwoLetters: ה, S0B0Token: גולם_הקם_על_יוצרו_הרי, S0B1Token: גולם_הקם_על_יוצרו_שמעתה, S0B2Token: גולם_הקם_על_יוצרו_ניתן, S0Token: גולם_הקם_על_יוצרו, TransHistory1: 1, TransHistory2: 11, TransHistory3: 110, 

22- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [הרי, שמעתה, ניתן ,.. ]

B0Token: הרי, B0_LastThreeLetters: �י, B0_LastTwoLetters: י, B1Token: שמעתה, B1_LastThreeLetters: �ה, B1_LastTwoLetters: ה, TransHistory1: 1, TransHistory2: 11, TransHistory3: 111, 

23- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [הרי]   B= [שמעתה, ניתן, לומר ,.. ]

B0Token: שמעתה, B0_LastThreeLetters: �ה, B0_LastTwoLetters: ה, B1Token: ניתן, B1_LastThreeLetters: �ן, B1_LastTwoLetters: ן, S0B0Token: הרי_שמעתה, S0B1Token: הרי_ניתן, S0B2Token: הרי_לומר, S0Token: הרי, S0_LastThreeLetters: �י, S0_LastTwoLetters: י, TransHistory1: 2, TransHistory2: 21, TransHistory3: 211, 

24- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [שמעתה, ניתן, לומר ,.. ]

B0Token: שמעתה, B0_LastThreeLetters: �ה, B0_LastTwoLetters: ה, B1Token: ניתן, B1_LastThreeLetters: �ן, B1_LastTwoLetters: ן, TransHistory1: 0, TransHistory2: 02, TransHistory3: 021, 

25- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [שמעתה]   B= [ניתן, לומר, שהוא ,.. ]

B0Token: ניתן, B0_LastThreeLetters: �ן, B0_LastTwoLetters: ן, B1Token: לומר, B1_LastThreeLetters: �ר, B1_LastTwoLetters: ר, S0B0Token: שמעתה_ניתן, S0B1Token: שמעתה_לומר, S0B2Token: שמעתה_שהוא, S0Token: שמעתה, S0_LastThreeLetters: �ה, S0_LastTwoLetters: ה, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

26- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ניתן, לומר, שהוא ,.. ]

B0Token: ניתן, B0_LastThreeLetters: �ן, B0_LastTwoLetters: ן, B1Token: לומר, B1_LastThreeLetters: �ר, B1_LastTwoLetters: ר, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

27- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ניתן]   B= [לומר, שהוא, רק ,.. ]

B0Token: לומר, B0_LastThreeLetters: �ר, B0_LastTwoLetters: ר, B1Token: שהוא, B1_LastThreeLetters: �א, B1_LastTwoLetters: א, S0B0Token: ניתן_לומר, S0B1Token: ניתן_שהוא, S0B2Token: ניתן_רק, S0Token: ניתן, S0_LastThreeLetters: �ן, S0_LastTwoLetters: ן, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

28- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [לומר, שהוא, רק ,.. ]

B0Token: לומר, B0_LastThreeLetters: �ר, B0_LastTwoLetters: ר, B1Token: שהוא, B1_LastThreeLetters: �א, B1_LastTwoLetters: א, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

29- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [לומר]   B= [שהוא, רק, קם ,.. ]

B0Token: שהוא, B0_LastThreeLetters: �א, B0_LastTwoLetters: א, B1Token: רק, B1_LastThreeLetters: �ק, B1_LastTwoLetters: ק, S0B0Token: לומר_שהוא, S0B1Token: לומר_רק, S0B2Token: לומר_קם, S0Token: לומר, S0_LastThreeLetters: �ר, S0_LastTwoLetters: ר, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

30- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [שהוא, רק, קם ,.. ]

B0Token: שהוא, B0_LastThreeLetters: �א, B0_LastTwoLetters: א, B1Token: רק, B1_LastThreeLetters: �ק, B1_LastTwoLetters: ק, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

31- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [שהוא]   B= [רק, קם, על ,.. ]

B0Token: רק, B0_LastThreeLetters: �ק, B0_LastTwoLetters: ק, B1Token: קם, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, S0B0Token: שהוא_רק, S0B1Token: שהוא_קם, S0B2Token: שהוא_על, S0Token: שהוא, S0_LastThreeLetters: �א, S0_LastTwoLetters: א, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

32- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [רק, קם, על ,.. ]

B0Token: רק, B0_LastThreeLetters: �ק, B0_LastTwoLetters: ק, B1Token: קם, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

33- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [רק]   B= [קם, על, יוצרו ,.. ]

B0Token: קם, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, B1Token: על, B1_LastThreeLetters: �ל, B1_LastTwoLetters: ל, S0B0Token: רק_קם, S0B1Token: רק_על, S0B2Token: רק_יוצרו, S0Token: רק, S0_LastThreeLetters: �ק, S0_LastTwoLetters: ק, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

34- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [קם, על, יוצרו ,.. ]

B0Token: קם, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, B1Token: על, B1_LastThreeLetters: �ל, B1_LastTwoLetters: ל, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

35- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [קם]   B= [על, יוצרו, אלא ,.. ]

B0Token: על, B0_LastThreeLetters: �ל, B0_LastTwoLetters: ל, B1Token: יוצרו, B1_LastThreeLetters: �ו, B1_LastTwoLetters: ו, S0B0Token: קם_על, S0B1Token: קם_יוצרו, S0B2Token: קם_אלא, S0Token: קם, S0_LastThreeLetters: �ם, S0_LastTwoLetters: ם, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

36- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [קם, על]   B= [יוצרו, אלא, אפילו ,.. ]

B0Token: יוצרו, B0_LastThreeLetters: �ו, B0_LastTwoLetters: ו, B1Token: אלא, B1_LastThreeLetters: �א, B1_LastTwoLetters: א, S0B0Token: על_יוצרו, S0B1Token: על_אלא, S0B2Token: על_אפילו, S0Token: על, S0_LastThreeLetters: �ל, S0_LastTwoLetters: ל, S1B0Token: קם_יוצרו, S1S0Token: קם_על, S1Token: קם, S1_LastThreeLetters: �ם, S1_LastTwoLetters: ם, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

37- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [קם, על, יוצרו]   B= [אלא, אפילו, נוזף ,.. ]

B0Token: אלא, B0_LastThreeLetters: �א, B0_LastTwoLetters: א, B1Token: אפילו, B1_LastThreeLetters: �ו, B1_LastTwoLetters: ו, S0B0Token: יוצרו_אלא, S0B1Token: יוצרו_אפילו, S0B2Token: יוצרו_נוזף, S0Token: יוצרו, S0_LastThreeLetters: �ו, S0_LastTwoLetters: ו, S1B0Token: על_אלא, S1S0Token: על_יוצרו, S1Token: על, S1_LastThreeLetters: �ל, S1_LastTwoLetters: ל, TransHistory1: 0, TransHistory2: 00, TransHistory3: 002, 

38- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [קם, [על, יוצרו]]   B= [אלא, אפילו, נוזף ,.. ]

B0Token: אלא, B0_LastThreeLetters: �א, B0_LastTwoLetters: א, B1Token: אפילו, B1_LastThreeLetters: �ו, B1_LastTwoLetters: ו, S0B0Token: על_יוצרו_אלא, S0B1Token: על_יוצרו_אפילו, S0B2Token: על_יוצרו_נוזף, S0Token: על_יוצרו, S1B0Token: קם_אלא, S1S0Token: קם_על_יוצרו, S1Token: קם, S1_LastThreeLetters: �ם, S1_LastTwoLetters: ם, TransHistory1: 0, TransHistory2: 00, TransHistory3: 000, 

39- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[קם, [על, יוצרו]]]   B= [אלא, אפילו, נוזף ,.. ]

B0Token: אלא, B0_LastThreeLetters: �א, B0_LastTwoLetters: א, B1Token: אפילו, B1_LastThreeLetters: �ו, B1_LastTwoLetters: ו, S0B0Token: קם_על_יוצרו_אלא, S0B1Token: קם_על_יוצרו_אפילו, S0B2Token: קם_על_יוצרו_נוזף, S0Token: קם_על_יוצרו, TransHistory1: 1, TransHistory2: 10, TransHistory3: 100, 

40- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [אלא, אפילו, נוזף ,.. ]

B0Token: אלא, B0_LastThreeLetters: �א, B0_LastTwoLetters: א, B1Token: אפילו, B1_LastThreeLetters: �ו, B1_LastTwoLetters: ו, TransHistory1: 1, TransHistory2: 11, TransHistory3: 110, 

41- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [אלא]   B= [אפילו, נוזף, בו ,.. ]

B0Token: אפילו, B0_LastThreeLetters: �ו, B0_LastTwoLetters: ו, B1Token: נוזף, B1_LastThreeLetters: �ף, B1_LastTwoLetters: ף, S0B0Token: אלא_אפילו, S0B1Token: אלא_נוזף, S0B2Token: אלא_בו, S0Token: אלא, S0_LastThreeLetters: �א, S0_LastTwoLetters: א, TransHistory1: 2, TransHistory2: 21, TransHistory3: 211, 

42- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [אפילו, נוזף, בו ,.. ]

B0Token: אפילו, B0_LastThreeLetters: �ו, B0_LastTwoLetters: ו, B1Token: נוזף, B1_LastThreeLetters: �ף, B1_LastTwoLetters: ף, TransHistory1: 0, TransHistory2: 02, TransHistory3: 021, 

43- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [אפילו]   B= [נוזף, בו, ומנסה ,.. ]

B0Token: נוזף, B0_LastThreeLetters: �ף, B0_LastTwoLetters: ף, B1Token: בו, B1_LastThreeLetters: �ו, B1_LastTwoLetters: ו, S0B0Token: אפילו_נוזף, S0B1Token: אפילו_בו, S0B2Token: אפילו_ומנסה, S0Token: אפילו, S0_LastThreeLetters: �ו, S0_LastTwoLetters: ו, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

44- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [נוזף, בו, ומנסה ,.. ]

B0Token: נוזף, B0_LastThreeLetters: �ף, B0_LastTwoLetters: ף, B1Token: בו, B1_LastThreeLetters: �ו, B1_LastTwoLetters: ו, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

45- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [נוזף]   B= [בו, ומנסה, לעצב ,.. ]

B0Token: בו, B0_LastThreeLetters: �ו, B0_LastTwoLetters: ו, B1Token: ומנסה, B1_LastThreeLetters: �ה, B1_LastTwoLetters: ה, S0B0Token: נוזף_בו, S0B1Token: נוזף_ומנסה, S0B2Token: נוזף_לעצב, S0Token: נוזף, S0_LastThreeLetters: �ף, S0_LastTwoLetters: ף, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

46- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [בו, ומנסה, לעצב ,.. ]

B0Token: בו, B0_LastThreeLetters: �ו, B0_LastTwoLetters: ו, B1Token: ומנסה, B1_LastThreeLetters: �ה, B1_LastTwoLetters: ה, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

47- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [בו]   B= [ומנסה, לעצב, אותו ,.. ]

B0Token: ומנסה, B0_LastThreeLetters: �ה, B0_LastTwoLetters: ה, B1Token: לעצב, B1_LastThreeLetters: �ב, B1_LastTwoLetters: ב, S0B0Token: בו_ומנסה, S0B1Token: בו_לעצב, S0B2Token: בו_אותו, S0Token: בו, S0_LastThreeLetters: �ו, S0_LastTwoLetters: ו, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

48- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ומנסה, לעצב, אותו ,.. ]

B0Token: ומנסה, B0_LastThreeLetters: �ה, B0_LastTwoLetters: ה, B1Token: לעצב, B1_LastThreeLetters: �ב, B1_LastTwoLetters: ב, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

49- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ומנסה]   B= [לעצב, אותו, מחדש ,.. ]

B0Token: לעצב, B0_LastThreeLetters: �ב, B0_LastTwoLetters: ב, B1Token: אותו, B1_LastThreeLetters: �ו, B1_LastTwoLetters: ו, S0B0Token: ומנסה_לעצב, S0B1Token: ומנסה_אותו, S0B2Token: ומנסה_מחדש, S0Token: ומנסה, S0_LastThreeLetters: �ה, S0_LastTwoLetters: ה, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

50- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [לעצב, אותו, מחדש ,.. ]

B0Token: לעצב, B0_LastThreeLetters: �ב, B0_LastTwoLetters: ב, B1Token: אותו, B1_LastThreeLetters: �ו, B1_LastTwoLetters: ו, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

51- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [לעצב]   B= [אותו, מחדש ,.. ]

B0Token: אותו, B0_LastThreeLetters: �ו, B0_LastTwoLetters: ו, B1Token: מחדש, B1_LastThreeLetters: �ש, B1_LastTwoLetters: ש, S0B0Token: לעצב_אותו, S0B1Token: לעצב_מחדש, S0Token: לעצב, S0_LastThreeLetters: �ב, S0_LastTwoLetters: ב, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

52- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [אותו, מחדש ,.. ]

B0Token: אותו, B0_LastThreeLetters: �ו, B0_LastTwoLetters: ו, B1Token: מחדש, B1_LastThreeLetters: �ש, B1_LastTwoLetters: ש, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

53- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [אותו]   B= [מחדש]

B0Token: מחדש, B0_LastThreeLetters: �ש, B0_LastTwoLetters: ש, S0B0Token: אותו_מחדש, S0Token: אותו, S0_LastThreeLetters: �ו, S0_LastTwoLetters: ו, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

54- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [מחדש]

B0Token: מחדש, B0_LastThreeLetters: �ש, B0_LastTwoLetters: ש, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

55- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [מחדש]   B= [ ]

S0Token: מחדש, S0_LastThreeLetters: �ש, S0_LastTwoLetters: ש, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

56- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

