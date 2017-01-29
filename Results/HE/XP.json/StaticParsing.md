## Sentence No. 350 - 
ברוש אמר בפגישה עם יו " ר ההסתדרות כי מרגע שצוותי המו " מ לא יוכלו להתקדם יותר על שר האוצר ויו " ר ההסתדרות להכנס אישית לעובי הקורה ולנהל את המו " מ ברציפות אם בעצמם או בעזרת גורמים אחרים על מנת להביא את השיחות לסיום מוצלח ולמנוע שביתה שישית בנמלים בשנתיים האחרונות
### Existing MWEs: 
2- **המו " מ** (OTH)
3- **המו מ** (OTH), Embedded
1- **להכנס לעובי הקורה** (OTH)
4- **המו " מ** (OTH)
5- **המו מ** (OTH), Embedded



0- &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ברוש, אמר, בפגישה ,.. ]

B0Token: ברוש, B0_LastThreeLetters: �ש, B0_LastTwoLetters: ש, B1Token: אמר, B1_LastThreeLetters: �ר, B1_LastTwoLetters: ר, 

1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ברוש]   B= [אמר, בפגישה, עם ,.. ]

B0Token: אמר, B0_LastThreeLetters: �ר, B0_LastTwoLetters: ר, B1Token: בפגישה, B1_LastThreeLetters: �ה, B1_LastTwoLetters: ה, S0B0Token: ברוש_אמר, S0B1Token: ברוש_בפגישה, S0B2Token: ברוש_עם, S0Token: ברוש, S0_LastThreeLetters: �ש, S0_LastTwoLetters: ש, 

2- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [אמר, בפגישה, עם ,.. ]

B0Token: אמר, B0_LastThreeLetters: �ר, B0_LastTwoLetters: ר, B1Token: בפגישה, B1_LastThreeLetters: �ה, B1_LastTwoLetters: ה, TransHistory1: 0, 

3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [אמר]   B= [בפגישה, עם, יו ,.. ]

B0Token: בפגישה, B0_LastThreeLetters: �ה, B0_LastTwoLetters: ה, B1Token: עם, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, S0B0Token: אמר_בפגישה, S0B1Token: אמר_עם, S0B2Token: אמר_יו, S0Token: אמר, S0_LastThreeLetters: �ר, S0_LastTwoLetters: ר, TransHistory1: 2, TransHistory2: 20, 

4- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [בפגישה, עם, יו ,.. ]

B0Token: בפגישה, B0_LastThreeLetters: �ה, B0_LastTwoLetters: ה, B1Token: עם, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [בפגישה]   B= [עם, יו, " ,.. ]

B0Token: עם, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, B1Token: יו, B1_LastThreeLetters: �ו, B1_LastTwoLetters: ו, S0B0Token: בפגישה_עם, S0B1Token: בפגישה_יו, S0B2Token: בפגישה_", S0Token: בפגישה, S0_LastThreeLetters: �ה, S0_LastTwoLetters: ה, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

6- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [עם, יו, " ,.. ]

B0Token: עם, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, B1Token: יו, B1_LastThreeLetters: �ו, B1_LastTwoLetters: ו, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [עם]   B= [יו, ", ר ,.. ]

B0Token: יו, B0_LastThreeLetters: �ו, B0_LastTwoLetters: ו, B1Token: ", B1_LastThreeLetters: ", B1_LastTwoLetters: ", S0B0Token: עם_יו, S0B1Token: עם_", S0B2Token: עם_ר, S0Token: עם, S0_LastThreeLetters: �ם, S0_LastTwoLetters: ם, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

8- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [יו, ", ר ,.. ]

B0Token: יו, B0_LastThreeLetters: �ו, B0_LastTwoLetters: ו, B1Token: ", B1_LastThreeLetters: ", B1_LastTwoLetters: ", TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [יו]   B= [", ר, ההסתדרות ,.. ]

B0Token: ", B0_LastThreeLetters: ", B0_LastTwoLetters: ", B1Token: ר, B1_LastThreeLetters: ר, B1_LastTwoLetters: ר, S0B0Token: יו_", S0B1Token: יו_ר, S0B2Token: יו_ההסתדרות, S0Token: יו, S0_LastThreeLetters: �ו, S0_LastTwoLetters: ו, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

10- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [", ר, ההסתדרות ,.. ]

B0Token: ", B0_LastThreeLetters: ", B0_LastTwoLetters: ", B1Token: ר, B1_LastThreeLetters: ר, B1_LastTwoLetters: ר, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= ["]   B= [ר, ההסתדרות, כי ,.. ]

B0Token: ר, B0_LastThreeLetters: ר, B0_LastTwoLetters: ר, B1Token: ההסתדרות, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, S0B0Token: "_ר, S0B1Token: "_ההסתדרות, S0B2Token: "_כי, S0Token: ", S0_LastThreeLetters: ", S0_LastTwoLetters: ", TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

12- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ר, ההסתדרות, כי ,.. ]

B0Token: ר, B0_LastThreeLetters: ר, B0_LastTwoLetters: ר, B1Token: ההסתדרות, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ר]   B= [ההסתדרות, כי, מרגע ,.. ]

B0Token: ההסתדרות, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: כי, B1_LastThreeLetters: �י, B1_LastTwoLetters: י, S0B0Token: ר_ההסתדרות, S0B1Token: ר_כי, S0B2Token: ר_מרגע, S0Token: ר, S0_LastThreeLetters: ר, S0_LastTwoLetters: ר, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

14- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ההסתדרות, כי, מרגע ,.. ]

B0Token: ההסתדרות, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: כי, B1_LastThreeLetters: �י, B1_LastTwoLetters: י, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ההסתדרות]   B= [כי, מרגע, שצוותי ,.. ]

B0Token: כי, B0_LastThreeLetters: �י, B0_LastTwoLetters: י, B1Token: מרגע, B1_LastThreeLetters: �ע, B1_LastTwoLetters: ע, S0B0Token: ההסתדרות_כי, S0B1Token: ההסתדרות_מרגע, S0B2Token: ההסתדרות_שצוותי, S0Token: ההסתדרות, S0_LastThreeLetters: �ת, S0_LastTwoLetters: ת, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

16- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [כי, מרגע, שצוותי ,.. ]

B0Token: כי, B0_LastThreeLetters: �י, B0_LastTwoLetters: י, B1Token: מרגע, B1_LastThreeLetters: �ע, B1_LastTwoLetters: ע, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [כי]   B= [מרגע, שצוותי, המו ,.. ]

B0Token: מרגע, B0_LastThreeLetters: �ע, B0_LastTwoLetters: ע, B1Token: שצוותי, B1_LastThreeLetters: �י, B1_LastTwoLetters: י, S0B0Token: כי_מרגע, S0B1Token: כי_שצוותי, S0B2Token: כי_המו, S0Token: כי, S0_LastThreeLetters: �י, S0_LastTwoLetters: י, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

18- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [מרגע, שצוותי, המו ,.. ]

B0Token: מרגע, B0_LastThreeLetters: �ע, B0_LastTwoLetters: ע, B1Token: שצוותי, B1_LastThreeLetters: �י, B1_LastTwoLetters: י, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [מרגע]   B= [שצוותי, המו, " ,.. ]

B0Token: שצוותי, B0_LastThreeLetters: �י, B0_LastTwoLetters: י, B1Token: המו, B1_LastThreeLetters: �ו, B1_LastTwoLetters: ו, S0B0Token: מרגע_שצוותי, S0B1Token: מרגע_המו, S0B2Token: מרגע_", S0Token: מרגע, S0_LastThreeLetters: �ע, S0_LastTwoLetters: ע, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

20- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [שצוותי, המו, " ,.. ]

B0Token: שצוותי, B0_LastThreeLetters: �י, B0_LastTwoLetters: י, B1Token: המו, B1_LastThreeLetters: �ו, B1_LastTwoLetters: ו, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [שצוותי]   B= [המו, ", מ ,.. ]

B0Token: המו, B0_LastThreeLetters: �ו, B0_LastTwoLetters: ו, B1Token: ", B1_LastThreeLetters: ", B1_LastTwoLetters: ", S0B0Token: שצוותי_המו, S0B1Token: שצוותי_", S0B2Token: שצוותי_מ, S0Token: שצוותי, S0_LastThreeLetters: �י, S0_LastTwoLetters: י, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

22- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [המו, ", מ ,.. ]

B0Token: המו, B0_LastThreeLetters: �ו, B0_LastTwoLetters: ו, B1Token: ", B1_LastThreeLetters: ", B1_LastTwoLetters: ", TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

23- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [המו]   B= [", מ, לא ,.. ]

B0Token: ", B0_LastThreeLetters: ", B0_LastTwoLetters: ", B1Token: מ, B1_LastThreeLetters: מ, B1_LastTwoLetters: מ, S0B0Token: המו_", S0B1Token: המו_מ, S0B2Token: המו_לא, S0Token: המו, S0_LastThreeLetters: �ו, S0_LastTwoLetters: ו, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

24- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [המו, "]   B= [מ, לא, יוכלו ,.. ]

B0Token: מ, B0_LastThreeLetters: מ, B0_LastTwoLetters: מ, B1Token: לא, B1_LastThreeLetters: �א, B1_LastTwoLetters: א, S0B0Token: "_מ, S0B1Token: "_לא, S0B2Token: "_יוכלו, S0Token: ", S0_LastThreeLetters: ", S0_LastTwoLetters: ", S1B0Token: המו_מ, S1S0Token: המו_", S1Token: המו, S1_LastThreeLetters: �ו, S1_LastTwoLetters: ו, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

25- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [המו, ", מ]   B= [לא, יוכלו, להתקדם ,.. ]

B0Token: לא, B0_LastThreeLetters: �א, B0_LastTwoLetters: א, B1Token: יוכלו, B1_LastThreeLetters: �ו, B1_LastTwoLetters: ו, S0B0Token: מ_לא, S0B1Token: מ_יוכלו, S0B2Token: מ_להתקדם, S0Token: מ, S0_LastThreeLetters: מ, S0_LastTwoLetters: מ, S1B0Token: "_לא, S1S0Token: "_מ, S1Token: ", S1_LastThreeLetters: ", S1_LastTwoLetters: ", TransHistory1: 0, TransHistory2: 00, TransHistory3: 002, 

26- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [המו, [", מ]]   B= [לא, יוכלו, להתקדם ,.. ]

B0Token: לא, B0_LastThreeLetters: �א, B0_LastTwoLetters: א, B1Token: יוכלו, B1_LastThreeLetters: �ו, B1_LastTwoLetters: ו, S0B0Token: "_מ_לא, S0B1Token: "_מ_יוכלו, S0B2Token: "_מ_להתקדם, S0Token: "_מ, S1B0Token: המו_לא, S1S0Token: המו_"_מ, S1Token: המו, S1_LastThreeLetters: �ו, S1_LastTwoLetters: ו, TransHistory1: 0, TransHistory2: 00, TransHistory3: 000, 

27- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[המו, [", מ]]]   B= [לא, יוכלו, להתקדם ,.. ]

B0Token: לא, B0_LastThreeLetters: �א, B0_LastTwoLetters: א, B1Token: יוכלו, B1_LastThreeLetters: �ו, B1_LastTwoLetters: ו, S0B0Token: המו_"_מ_לא, S0B1Token: המו_"_מ_יוכלו, S0B2Token: המו_"_מ_להתקדם, S0Token: המו_"_מ, TransHistory1: 1, TransHistory2: 10, TransHistory3: 100, 

28- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [לא, יוכלו, להתקדם ,.. ]

B0Token: לא, B0_LastThreeLetters: �א, B0_LastTwoLetters: א, B1Token: יוכלו, B1_LastThreeLetters: �ו, B1_LastTwoLetters: ו, TransHistory1: 1, TransHistory2: 11, TransHistory3: 110, 

29- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [לא]   B= [יוכלו, להתקדם, יותר ,.. ]

B0Token: יוכלו, B0_LastThreeLetters: �ו, B0_LastTwoLetters: ו, B1Token: להתקדם, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, S0B0Token: לא_יוכלו, S0B1Token: לא_להתקדם, S0B2Token: לא_יותר, S0Token: לא, S0_LastThreeLetters: �א, S0_LastTwoLetters: א, TransHistory1: 2, TransHistory2: 21, TransHistory3: 211, 

30- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [יוכלו, להתקדם, יותר ,.. ]

B0Token: יוכלו, B0_LastThreeLetters: �ו, B0_LastTwoLetters: ו, B1Token: להתקדם, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, TransHistory1: 0, TransHistory2: 02, TransHistory3: 021, 

31- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [יוכלו]   B= [להתקדם, יותר, על ,.. ]

B0Token: להתקדם, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, B1Token: יותר, B1_LastThreeLetters: �ר, B1_LastTwoLetters: ר, S0B0Token: יוכלו_להתקדם, S0B1Token: יוכלו_יותר, S0B2Token: יוכלו_על, S0Token: יוכלו, S0_LastThreeLetters: �ו, S0_LastTwoLetters: ו, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

32- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [להתקדם, יותר, על ,.. ]

B0Token: להתקדם, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, B1Token: יותר, B1_LastThreeLetters: �ר, B1_LastTwoLetters: ר, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

33- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [להתקדם]   B= [יותר, על, שר ,.. ]

B0Token: יותר, B0_LastThreeLetters: �ר, B0_LastTwoLetters: ר, B1Token: על, B1_LastThreeLetters: �ל, B1_LastTwoLetters: ל, S0B0Token: להתקדם_יותר, S0B1Token: להתקדם_על, S0B2Token: להתקדם_שר, S0Token: להתקדם, S0_LastThreeLetters: �ם, S0_LastTwoLetters: ם, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

34- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [יותר, על, שר ,.. ]

B0Token: יותר, B0_LastThreeLetters: �ר, B0_LastTwoLetters: ר, B1Token: על, B1_LastThreeLetters: �ל, B1_LastTwoLetters: ל, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

35- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [יותר]   B= [על, שר, האוצר ,.. ]

B0Token: על, B0_LastThreeLetters: �ל, B0_LastTwoLetters: ל, B1Token: שר, B1_LastThreeLetters: �ר, B1_LastTwoLetters: ר, S0B0Token: יותר_על, S0B1Token: יותר_שר, S0B2Token: יותר_האוצר, S0Token: יותר, S0_LastThreeLetters: �ר, S0_LastTwoLetters: ר, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

36- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [על, שר, האוצר ,.. ]

B0Token: על, B0_LastThreeLetters: �ל, B0_LastTwoLetters: ל, B1Token: שר, B1_LastThreeLetters: �ר, B1_LastTwoLetters: ר, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

37- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [על]   B= [שר, האוצר, ויו ,.. ]

B0Token: שר, B0_LastThreeLetters: �ר, B0_LastTwoLetters: ר, B1Token: האוצר, B1_LastThreeLetters: �ר, B1_LastTwoLetters: ר, S0B0Token: על_שר, S0B1Token: על_האוצר, S0B2Token: על_ויו, S0Token: על, S0_LastThreeLetters: �ל, S0_LastTwoLetters: ל, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

38- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [שר, האוצר, ויו ,.. ]

B0Token: שר, B0_LastThreeLetters: �ר, B0_LastTwoLetters: ר, B1Token: האוצר, B1_LastThreeLetters: �ר, B1_LastTwoLetters: ר, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

39- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [שר]   B= [האוצר, ויו, " ,.. ]

B0Token: האוצר, B0_LastThreeLetters: �ר, B0_LastTwoLetters: ר, B1Token: ויו, B1_LastThreeLetters: �ו, B1_LastTwoLetters: ו, S0B0Token: שר_האוצר, S0B1Token: שר_ויו, S0B2Token: שר_", S0Token: שר, S0_LastThreeLetters: �ר, S0_LastTwoLetters: ר, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

40- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [האוצר, ויו, " ,.. ]

B0Token: האוצר, B0_LastThreeLetters: �ר, B0_LastTwoLetters: ר, B1Token: ויו, B1_LastThreeLetters: �ו, B1_LastTwoLetters: ו, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

41- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [האוצר]   B= [ויו, ", ר ,.. ]

B0Token: ויו, B0_LastThreeLetters: �ו, B0_LastTwoLetters: ו, B1Token: ", B1_LastThreeLetters: ", B1_LastTwoLetters: ", S0B0Token: האוצר_ויו, S0B1Token: האוצר_", S0B2Token: האוצר_ר, S0Token: האוצר, S0_LastThreeLetters: �ר, S0_LastTwoLetters: ר, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

42- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ויו, ", ר ,.. ]

B0Token: ויו, B0_LastThreeLetters: �ו, B0_LastTwoLetters: ו, B1Token: ", B1_LastThreeLetters: ", B1_LastTwoLetters: ", TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

43- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ויו]   B= [", ר, ההסתדרות ,.. ]

B0Token: ", B0_LastThreeLetters: ", B0_LastTwoLetters: ", B1Token: ר, B1_LastThreeLetters: ר, B1_LastTwoLetters: ר, S0B0Token: ויו_", S0B1Token: ויו_ר, S0B2Token: ויו_ההסתדרות, S0Token: ויו, S0_LastThreeLetters: �ו, S0_LastTwoLetters: ו, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

44- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [", ר, ההסתדרות ,.. ]

B0Token: ", B0_LastThreeLetters: ", B0_LastTwoLetters: ", B1Token: ר, B1_LastThreeLetters: ר, B1_LastTwoLetters: ר, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

45- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= ["]   B= [ר, ההסתדרות, להכנס ,.. ]

B0Token: ר, B0_LastThreeLetters: ר, B0_LastTwoLetters: ר, B1Token: ההסתדרות, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, S0B0Token: "_ר, S0B1Token: "_ההסתדרות, S0B2Token: "_להכנס, S0Token: ", S0_LastThreeLetters: ", S0_LastTwoLetters: ", TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

46- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ר, ההסתדרות, להכנס ,.. ]

B0Token: ר, B0_LastThreeLetters: ר, B0_LastTwoLetters: ר, B1Token: ההסתדרות, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

47- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ר]   B= [ההסתדרות, להכנס, אישית ,.. ]

B0Token: ההסתדרות, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: להכנס, B1_LastThreeLetters: �ס, B1_LastTwoLetters: ס, S0B0Token: ר_ההסתדרות, S0B1Token: ר_להכנס, S0B2Token: ר_אישית, S0Token: ר, S0_LastThreeLetters: ר, S0_LastTwoLetters: ר, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

48- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ההסתדרות, להכנס, אישית ,.. ]

B0Token: ההסתדרות, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: להכנס, B1_LastThreeLetters: �ס, B1_LastTwoLetters: ס, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

49- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ההסתדרות]   B= [להכנס, אישית, לעובי ,.. ]

B0Token: להכנס, B0_LastThreeLetters: �ס, B0_LastTwoLetters: ס, B1Token: אישית, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, S0B0Token: ההסתדרות_להכנס, S0B1Token: ההסתדרות_אישית, S0B2Token: ההסתדרות_לעובי, S0Token: ההסתדרות, S0_LastThreeLetters: �ת, S0_LastTwoLetters: ת, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

50- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [להכנס, אישית, לעובי ,.. ]

B0Token: להכנס, B0_LastThreeLetters: �ס, B0_LastTwoLetters: ס, B1Token: אישית, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

51- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [להכנס]   B= [אישית, לעובי, הקורה ,.. ]

B0Token: אישית, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: לעובי, B1_LastThreeLetters: �י, B1_LastTwoLetters: י, S0B0Token: להכנס_אישית, S0B1Token: להכנס_לעובי, S0B2Token: להכנס_הקורה, S0Token: להכנס, S0_LastThreeLetters: �ס, S0_LastTwoLetters: ס, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

52- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [להכנס, אישית]   B= [לעובי, הקורה, ולנהל ,.. ]

B0Token: לעובי, B0_LastThreeLetters: �י, B0_LastTwoLetters: י, B1Token: הקורה, B1_LastThreeLetters: �ה, B1_LastTwoLetters: ה, S0B0Token: אישית_לעובי, S0B1Token: אישית_הקורה, S0B2Token: אישית_ולנהל, S0Token: אישית, S0_LastThreeLetters: �ת, S0_LastTwoLetters: ת, S1B0Token: להכנס_לעובי, S1S0Token: להכנס_אישית, S1Token: להכנס, S1_LastThreeLetters: �ס, S1_LastTwoLetters: ס, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

53- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [להכנס]   B= [לעובי, הקורה, ולנהל ,.. ]

B0Token: לעובי, B0_LastThreeLetters: �י, B0_LastTwoLetters: י, B1Token: הקורה, B1_LastThreeLetters: �ה, B1_LastTwoLetters: ה, S0B0Token: להכנס_לעובי, S0B1Token: להכנס_הקורה, S0B2Token: להכנס_ולנהל, S0Token: להכנס, S0_LastThreeLetters: �ס, S0_LastTwoLetters: ס, TransHistory1: 0, TransHistory2: 00, TransHistory3: 002, 

54- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [להכנס, לעובי]   B= [הקורה, ולנהל, את ,.. ]

B0Token: הקורה, B0_LastThreeLetters: �ה, B0_LastTwoLetters: ה, B1Token: ולנהל, B1_LastThreeLetters: �ל, B1_LastTwoLetters: ל, S0B0Token: לעובי_הקורה, S0B1Token: לעובי_ולנהל, S0B2Token: לעובי_את, S0Token: לעובי, S0_LastThreeLetters: �י, S0_LastTwoLetters: י, S1B0Token: להכנס_הקורה, S1S0Token: להכנס_לעובי, S1Token: להכנס, S1_LastThreeLetters: �ס, S1_LastTwoLetters: ס, TransHistory1: 2, TransHistory2: 20, TransHistory3: 200, 

55- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [להכנס, לעובי, הקורה]   B= [ולנהל, את, המו ,.. ]

B0Token: ולנהל, B0_LastThreeLetters: �ל, B0_LastTwoLetters: ל, B1Token: את, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, S0B0Token: הקורה_ולנהל, S0B1Token: הקורה_את, S0B2Token: הקורה_המו, S0Token: הקורה, S0_LastThreeLetters: �ה, S0_LastTwoLetters: ה, S1B0Token: לעובי_ולנהל, S1S0Token: לעובי_הקורה, S1Token: לעובי, S1_LastThreeLetters: �י, S1_LastTwoLetters: י, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

56- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [להכנס, [לעובי, הקורה]]   B= [ולנהל, את, המו ,.. ]

B0Token: ולנהל, B0_LastThreeLetters: �ל, B0_LastTwoLetters: ל, B1Token: את, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, S0B0Token: לעובי_הקורה_ולנהל, S0B1Token: לעובי_הקורה_את, S0B2Token: לעובי_הקורה_המו, S0Token: לעובי_הקורה, S1B0Token: להכנס_ולנהל, S1S0Token: להכנס_לעובי_הקורה, S1Token: להכנס, S1_LastThreeLetters: �ס, S1_LastTwoLetters: ס, TransHistory1: 0, TransHistory2: 00, TransHistory3: 002, 

57- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[להכנס, [לעובי, הקורה]]]   B= [ולנהל, את, המו ,.. ]

B0Token: ולנהל, B0_LastThreeLetters: �ל, B0_LastTwoLetters: ל, B1Token: את, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, S0B0Token: להכנס_לעובי_הקורה_ולנהל, S0B1Token: להכנס_לעובי_הקורה_את, S0B2Token: להכנס_לעובי_הקורה_המו, S0Token: להכנס_לעובי_הקורה, TransHistory1: 1, TransHistory2: 10, TransHistory3: 100, 

58- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ולנהל, את, המו ,.. ]

B0Token: ולנהל, B0_LastThreeLetters: �ל, B0_LastTwoLetters: ל, B1Token: את, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, TransHistory1: 1, TransHistory2: 11, TransHistory3: 110, 

59- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ולנהל]   B= [את, המו, " ,.. ]

B0Token: את, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: המו, B1_LastThreeLetters: �ו, B1_LastTwoLetters: ו, S0B0Token: ולנהל_את, S0B1Token: ולנהל_המו, S0B2Token: ולנהל_", S0Token: ולנהל, S0_LastThreeLetters: �ל, S0_LastTwoLetters: ל, TransHistory1: 2, TransHistory2: 21, TransHistory3: 211, 

60- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [את, המו, " ,.. ]

B0Token: את, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: המו, B1_LastThreeLetters: �ו, B1_LastTwoLetters: ו, TransHistory1: 0, TransHistory2: 02, TransHistory3: 021, 

61- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [את]   B= [המו, ", מ ,.. ]

B0Token: המו, B0_LastThreeLetters: �ו, B0_LastTwoLetters: ו, B1Token: ", B1_LastThreeLetters: ", B1_LastTwoLetters: ", S0B0Token: את_המו, S0B1Token: את_", S0B2Token: את_מ, S0Token: את, S0_LastThreeLetters: �ת, S0_LastTwoLetters: ת, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

62- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [המו, ", מ ,.. ]

B0Token: המו, B0_LastThreeLetters: �ו, B0_LastTwoLetters: ו, B1Token: ", B1_LastThreeLetters: ", B1_LastTwoLetters: ", TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

63- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [המו]   B= [", מ, ברציפות ,.. ]

B0Token: ", B0_LastThreeLetters: ", B0_LastTwoLetters: ", B1Token: מ, B1_LastThreeLetters: מ, B1_LastTwoLetters: מ, S0B0Token: המו_", S0B1Token: המו_מ, S0B2Token: המו_ברציפות, S0Token: המו, S0_LastThreeLetters: �ו, S0_LastTwoLetters: ו, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

64- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [המו, "]   B= [מ, ברציפות, אם ,.. ]

B0Token: מ, B0_LastThreeLetters: מ, B0_LastTwoLetters: מ, B1Token: ברציפות, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, S0B0Token: "_מ, S0B1Token: "_ברציפות, S0B2Token: "_אם, S0Token: ", S0_LastThreeLetters: ", S0_LastTwoLetters: ", S1B0Token: המו_מ, S1S0Token: המו_", S1Token: המו, S1_LastThreeLetters: �ו, S1_LastTwoLetters: ו, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

65- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [המו, ", מ]   B= [ברציפות, אם, בעצמם ,.. ]

B0Token: ברציפות, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: אם, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, S0B0Token: מ_ברציפות, S0B1Token: מ_אם, S0B2Token: מ_בעצמם, S0Token: מ, S0_LastThreeLetters: מ, S0_LastTwoLetters: מ, S1B0Token: "_ברציפות, S1S0Token: "_מ, S1Token: ", S1_LastThreeLetters: ", S1_LastTwoLetters: ", TransHistory1: 0, TransHistory2: 00, TransHistory3: 002, 

66- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [המו, [", מ]]   B= [ברציפות, אם, בעצמם ,.. ]

B0Token: ברציפות, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: אם, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, S0B0Token: "_מ_ברציפות, S0B1Token: "_מ_אם, S0B2Token: "_מ_בעצמם, S0Token: "_מ, S1B0Token: המו_ברציפות, S1S0Token: המו_"_מ, S1Token: המו, S1_LastThreeLetters: �ו, S1_LastTwoLetters: ו, TransHistory1: 0, TransHistory2: 00, TransHistory3: 000, 

67- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[המו, [", מ]]]   B= [ברציפות, אם, בעצמם ,.. ]

B0Token: ברציפות, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: אם, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, S0B0Token: המו_"_מ_ברציפות, S0B1Token: המו_"_מ_אם, S0B2Token: המו_"_מ_בעצמם, S0Token: המו_"_מ, TransHistory1: 1, TransHistory2: 10, TransHistory3: 100, 

68- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ברציפות, אם, בעצמם ,.. ]

B0Token: ברציפות, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: אם, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, TransHistory1: 1, TransHistory2: 11, TransHistory3: 110, 

69- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ברציפות]   B= [אם, בעצמם, או ,.. ]

B0Token: אם, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, B1Token: בעצמם, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, S0B0Token: ברציפות_אם, S0B1Token: ברציפות_בעצמם, S0B2Token: ברציפות_או, S0Token: ברציפות, S0_LastThreeLetters: �ת, S0_LastTwoLetters: ת, TransHistory1: 2, TransHistory2: 21, TransHistory3: 211, 

70- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [אם, בעצמם, או ,.. ]

B0Token: אם, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, B1Token: בעצמם, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, TransHistory1: 0, TransHistory2: 02, TransHistory3: 021, 

71- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [אם]   B= [בעצמם, או, בעזרת ,.. ]

B0Token: בעצמם, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, B1Token: או, B1_LastThreeLetters: �ו, B1_LastTwoLetters: ו, S0B0Token: אם_בעצמם, S0B1Token: אם_או, S0B2Token: אם_בעזרת, S0Token: אם, S0_LastThreeLetters: �ם, S0_LastTwoLetters: ם, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

72- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [בעצמם, או, בעזרת ,.. ]

B0Token: בעצמם, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, B1Token: או, B1_LastThreeLetters: �ו, B1_LastTwoLetters: ו, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

73- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [בעצמם]   B= [או, בעזרת, גורמים ,.. ]

B0Token: או, B0_LastThreeLetters: �ו, B0_LastTwoLetters: ו, B1Token: בעזרת, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, S0B0Token: בעצמם_או, S0B1Token: בעצמם_בעזרת, S0B2Token: בעצמם_גורמים, S0Token: בעצמם, S0_LastThreeLetters: �ם, S0_LastTwoLetters: ם, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

74- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [או, בעזרת, גורמים ,.. ]

B0Token: או, B0_LastThreeLetters: �ו, B0_LastTwoLetters: ו, B1Token: בעזרת, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

75- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [או]   B= [בעזרת, גורמים, אחרים ,.. ]

B0Token: בעזרת, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: גורמים, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, S0B0Token: או_בעזרת, S0B1Token: או_גורמים, S0B2Token: או_אחרים, S0Token: או, S0_LastThreeLetters: �ו, S0_LastTwoLetters: ו, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

76- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [בעזרת, גורמים, אחרים ,.. ]

B0Token: בעזרת, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: גורמים, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

77- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [בעזרת]   B= [גורמים, אחרים, על ,.. ]

B0Token: גורמים, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, B1Token: אחרים, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, S0B0Token: בעזרת_גורמים, S0B1Token: בעזרת_אחרים, S0B2Token: בעזרת_על, S0Token: בעזרת, S0_LastThreeLetters: �ת, S0_LastTwoLetters: ת, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

78- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [גורמים, אחרים, על ,.. ]

B0Token: גורמים, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, B1Token: אחרים, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

79- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [גורמים]   B= [אחרים, על, מנת ,.. ]

B0Token: אחרים, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, B1Token: על, B1_LastThreeLetters: �ל, B1_LastTwoLetters: ל, S0B0Token: גורמים_אחרים, S0B1Token: גורמים_על, S0B2Token: גורמים_מנת, S0Token: גורמים, S0_LastThreeLetters: �ם, S0_LastTwoLetters: ם, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

80- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [אחרים, על, מנת ,.. ]

B0Token: אחרים, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, B1Token: על, B1_LastThreeLetters: �ל, B1_LastTwoLetters: ל, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

81- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [אחרים]   B= [על, מנת, להביא ,.. ]

B0Token: על, B0_LastThreeLetters: �ל, B0_LastTwoLetters: ל, B1Token: מנת, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, S0B0Token: אחרים_על, S0B1Token: אחרים_מנת, S0B2Token: אחרים_להביא, S0Token: אחרים, S0_LastThreeLetters: �ם, S0_LastTwoLetters: ם, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

82- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [על, מנת, להביא ,.. ]

B0Token: על, B0_LastThreeLetters: �ל, B0_LastTwoLetters: ל, B1Token: מנת, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

83- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [על]   B= [מנת, להביא, את ,.. ]

B0Token: מנת, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: להביא, B1_LastThreeLetters: �א, B1_LastTwoLetters: א, S0B0Token: על_מנת, S0B1Token: על_להביא, S0B2Token: על_את, S0Token: על, S0_LastThreeLetters: �ל, S0_LastTwoLetters: ל, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

84- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [מנת, להביא, את ,.. ]

B0Token: מנת, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: להביא, B1_LastThreeLetters: �א, B1_LastTwoLetters: א, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

85- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [מנת]   B= [להביא, את, השיחות ,.. ]

B0Token: להביא, B0_LastThreeLetters: �א, B0_LastTwoLetters: א, B1Token: את, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, S0B0Token: מנת_להביא, S0B1Token: מנת_את, S0B2Token: מנת_השיחות, S0Token: מנת, S0_LastThreeLetters: �ת, S0_LastTwoLetters: ת, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

86- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [להביא, את, השיחות ,.. ]

B0Token: להביא, B0_LastThreeLetters: �א, B0_LastTwoLetters: א, B1Token: את, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

87- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [להביא]   B= [את, השיחות, לסיום ,.. ]

B0Token: את, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: השיחות, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, S0B0Token: להביא_את, S0B1Token: להביא_השיחות, S0B2Token: להביא_לסיום, S0Token: להביא, S0_LastThreeLetters: �א, S0_LastTwoLetters: א, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

88- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [את, השיחות, לסיום ,.. ]

B0Token: את, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: השיחות, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

89- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [את]   B= [השיחות, לסיום, מוצלח ,.. ]

B0Token: השיחות, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: לסיום, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, S0B0Token: את_השיחות, S0B1Token: את_לסיום, S0B2Token: את_מוצלח, S0Token: את, S0_LastThreeLetters: �ת, S0_LastTwoLetters: ת, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

90- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [השיחות, לסיום, מוצלח ,.. ]

B0Token: השיחות, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: לסיום, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

91- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [השיחות]   B= [לסיום, מוצלח, ולמנוע ,.. ]

B0Token: לסיום, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, B1Token: מוצלח, B1_LastThreeLetters: �ח, B1_LastTwoLetters: ח, S0B0Token: השיחות_לסיום, S0B1Token: השיחות_מוצלח, S0B2Token: השיחות_ולמנוע, S0Token: השיחות, S0_LastThreeLetters: �ת, S0_LastTwoLetters: ת, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

92- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [לסיום, מוצלח, ולמנוע ,.. ]

B0Token: לסיום, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, B1Token: מוצלח, B1_LastThreeLetters: �ח, B1_LastTwoLetters: ח, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

93- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [לסיום]   B= [מוצלח, ולמנוע, שביתה ,.. ]

B0Token: מוצלח, B0_LastThreeLetters: �ח, B0_LastTwoLetters: ח, B1Token: ולמנוע, B1_LastThreeLetters: �ע, B1_LastTwoLetters: ע, S0B0Token: לסיום_מוצלח, S0B1Token: לסיום_ולמנוע, S0B2Token: לסיום_שביתה, S0Token: לסיום, S0_LastThreeLetters: �ם, S0_LastTwoLetters: ם, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

94- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [מוצלח, ולמנוע, שביתה ,.. ]

B0Token: מוצלח, B0_LastThreeLetters: �ח, B0_LastTwoLetters: ח, B1Token: ולמנוע, B1_LastThreeLetters: �ע, B1_LastTwoLetters: ע, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

95- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [מוצלח]   B= [ולמנוע, שביתה, שישית ,.. ]

B0Token: ולמנוע, B0_LastThreeLetters: �ע, B0_LastTwoLetters: ע, B1Token: שביתה, B1_LastThreeLetters: �ה, B1_LastTwoLetters: ה, S0B0Token: מוצלח_ולמנוע, S0B1Token: מוצלח_שביתה, S0B2Token: מוצלח_שישית, S0Token: מוצלח, S0_LastThreeLetters: �ח, S0_LastTwoLetters: ח, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

96- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ולמנוע, שביתה, שישית ,.. ]

B0Token: ולמנוע, B0_LastThreeLetters: �ע, B0_LastTwoLetters: ע, B1Token: שביתה, B1_LastThreeLetters: �ה, B1_LastTwoLetters: ה, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

97- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ולמנוע]   B= [שביתה, שישית, בנמלים ,.. ]

B0Token: שביתה, B0_LastThreeLetters: �ה, B0_LastTwoLetters: ה, B1Token: שישית, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, S0B0Token: ולמנוע_שביתה, S0B1Token: ולמנוע_שישית, S0B2Token: ולמנוע_בנמלים, S0Token: ולמנוע, S0_LastThreeLetters: �ע, S0_LastTwoLetters: ע, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

98- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [שביתה, שישית, בנמלים ,.. ]

B0Token: שביתה, B0_LastThreeLetters: �ה, B0_LastTwoLetters: ה, B1Token: שישית, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

99- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [שביתה]   B= [שישית, בנמלים, בשנתיים ,.. ]

B0Token: שישית, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: בנמלים, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, S0B0Token: שביתה_שישית, S0B1Token: שביתה_בנמלים, S0B2Token: שביתה_בשנתיים, S0Token: שביתה, S0_LastThreeLetters: �ה, S0_LastTwoLetters: ה, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

100- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [שישית, בנמלים, בשנתיים ,.. ]

B0Token: שישית, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: בנמלים, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

101- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [שישית]   B= [בנמלים, בשנתיים, האחרונות ,.. ]

B0Token: בנמלים, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, B1Token: בשנתיים, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, S0B0Token: שישית_בנמלים, S0B1Token: שישית_בשנתיים, S0B2Token: שישית_האחרונות, S0Token: שישית, S0_LastThreeLetters: �ת, S0_LastTwoLetters: ת, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

102- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [בנמלים, בשנתיים, האחרונות ,.. ]

B0Token: בנמלים, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, B1Token: בשנתיים, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

103- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [בנמלים]   B= [בשנתיים, האחרונות ,.. ]

B0Token: בשנתיים, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, B1Token: האחרונות, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, S0B0Token: בנמלים_בשנתיים, S0B1Token: בנמלים_האחרונות, S0Token: בנמלים, S0_LastThreeLetters: �ם, S0_LastTwoLetters: ם, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

104- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [בשנתיים, האחרונות ,.. ]

B0Token: בשנתיים, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, B1Token: האחרונות, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

105- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [בשנתיים]   B= [האחרונות]

B0Token: האחרונות, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, S0B0Token: בשנתיים_האחרונות, S0Token: בשנתיים, S0_LastThreeLetters: �ם, S0_LastTwoLetters: ם, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

106- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [האחרונות]

B0Token: האחרונות, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

107- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [האחרונות]   B= [ ]

S0Token: האחרונות, S0_LastThreeLetters: �ת, S0_LastTwoLetters: ת, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

108- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

## Sentence No. 3238 - 
ועל מה ולמה עוקרים אותם הוא ממשיך לתמוה מילא אם היה גורם ביטחוני אחד שקם ואמר שלאחר העקירה תהיה כאן רגיעה ביטחונית ועם ישראל ישכון לבטח שלוש מאות שנה מבלי שצר ואויב יאיים עליו ניתן עדיין להבין שאם כל המציל נפש אחת מישראל כאילו קיים עולם אז ניתן לשמוע שיש מישהו שעם כל הכאב חושב על פינוי של הקברים אך כשממול עומדים כל גורמי הביטחון והדגש על כל ואומרים בפה מלא שתוכנית ההתנתקות רק תזיק לעתידנו והמחבלים רק יקרבו את קו הגבול וזה ייתן להם רוח גבית להמשך מעשה הטרור איזה היתר יש לפנות שוכני עפר ממקום מנוחתם
### Existing MWEs: 
1- **ישכון לבטח** (OTH)
2- **כל המציל נפש אחת מישראל כאילו קיים עולם** (OTH)
3- **ואומרים בפה מלא** (ID)
4- **ייתן להם רוח גבית** (ID)
5- **שוכני עפר** (OTH)



0- &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ועל, מה, ולמה ,.. ]

B0Token: ועל, B0_LastThreeLetters: �ל, B0_LastTwoLetters: ל, B1Token: מה, B1_LastThreeLetters: �ה, B1_LastTwoLetters: ה, 

1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ועל]   B= [מה, ולמה, עוקרים ,.. ]

B0Token: מה, B0_LastThreeLetters: �ה, B0_LastTwoLetters: ה, B1Token: ולמה, B1_LastThreeLetters: �ה, B1_LastTwoLetters: ה, S0B0Token: ועל_מה, S0B1Token: ועל_ולמה, S0B2Token: ועל_עוקרים, S0Token: ועל, S0_LastThreeLetters: �ל, S0_LastTwoLetters: ל, 

2- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [מה, ולמה, עוקרים ,.. ]

B0Token: מה, B0_LastThreeLetters: �ה, B0_LastTwoLetters: ה, B1Token: ולמה, B1_LastThreeLetters: �ה, B1_LastTwoLetters: ה, TransHistory1: 0, 

3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [מה]   B= [ולמה, עוקרים, אותם ,.. ]

B0Token: ולמה, B0_LastThreeLetters: �ה, B0_LastTwoLetters: ה, B1Token: עוקרים, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, S0B0Token: מה_ולמה, S0B1Token: מה_עוקרים, S0B2Token: מה_אותם, S0Token: מה, S0_LastThreeLetters: �ה, S0_LastTwoLetters: ה, TransHistory1: 2, TransHistory2: 20, 

4- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ולמה, עוקרים, אותם ,.. ]

B0Token: ולמה, B0_LastThreeLetters: �ה, B0_LastTwoLetters: ה, B1Token: עוקרים, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ולמה]   B= [עוקרים, אותם, הוא ,.. ]

B0Token: עוקרים, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, B1Token: אותם, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, S0B0Token: ולמה_עוקרים, S0B1Token: ולמה_אותם, S0B2Token: ולמה_הוא, S0Token: ולמה, S0_LastThreeLetters: �ה, S0_LastTwoLetters: ה, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

6- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [עוקרים, אותם, הוא ,.. ]

B0Token: עוקרים, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, B1Token: אותם, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [עוקרים]   B= [אותם, הוא, ממשיך ,.. ]

B0Token: אותם, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, B1Token: הוא, B1_LastThreeLetters: �א, B1_LastTwoLetters: א, S0B0Token: עוקרים_אותם, S0B1Token: עוקרים_הוא, S0B2Token: עוקרים_ממשיך, S0Token: עוקרים, S0_LastThreeLetters: �ם, S0_LastTwoLetters: ם, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

8- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [אותם, הוא, ממשיך ,.. ]

B0Token: אותם, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, B1Token: הוא, B1_LastThreeLetters: �א, B1_LastTwoLetters: א, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [אותם]   B= [הוא, ממשיך, לתמוה ,.. ]

B0Token: הוא, B0_LastThreeLetters: �א, B0_LastTwoLetters: א, B1Token: ממשיך, B1_LastThreeLetters: �ך, B1_LastTwoLetters: ך, S0B0Token: אותם_הוא, S0B1Token: אותם_ממשיך, S0B2Token: אותם_לתמוה, S0Token: אותם, S0_LastThreeLetters: �ם, S0_LastTwoLetters: ם, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

10- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [הוא, ממשיך, לתמוה ,.. ]

B0Token: הוא, B0_LastThreeLetters: �א, B0_LastTwoLetters: א, B1Token: ממשיך, B1_LastThreeLetters: �ך, B1_LastTwoLetters: ך, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [הוא]   B= [ממשיך, לתמוה, מילא ,.. ]

B0Token: ממשיך, B0_LastThreeLetters: �ך, B0_LastTwoLetters: ך, B1Token: לתמוה, B1_LastThreeLetters: �ה, B1_LastTwoLetters: ה, S0B0Token: הוא_ממשיך, S0B1Token: הוא_לתמוה, S0B2Token: הוא_מילא, S0Token: הוא, S0_LastThreeLetters: �א, S0_LastTwoLetters: א, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

12- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ממשיך, לתמוה, מילא ,.. ]

B0Token: ממשיך, B0_LastThreeLetters: �ך, B0_LastTwoLetters: ך, B1Token: לתמוה, B1_LastThreeLetters: �ה, B1_LastTwoLetters: ה, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ממשיך]   B= [לתמוה, מילא, אם ,.. ]

B0Token: לתמוה, B0_LastThreeLetters: �ה, B0_LastTwoLetters: ה, B1Token: מילא, B1_LastThreeLetters: �א, B1_LastTwoLetters: א, S0B0Token: ממשיך_לתמוה, S0B1Token: ממשיך_מילא, S0B2Token: ממשיך_אם, S0Token: ממשיך, S0_LastThreeLetters: �ך, S0_LastTwoLetters: ך, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

14- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [לתמוה, מילא, אם ,.. ]

B0Token: לתמוה, B0_LastThreeLetters: �ה, B0_LastTwoLetters: ה, B1Token: מילא, B1_LastThreeLetters: �א, B1_LastTwoLetters: א, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [לתמוה]   B= [מילא, אם, היה ,.. ]

B0Token: מילא, B0_LastThreeLetters: �א, B0_LastTwoLetters: א, B1Token: אם, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, S0B0Token: לתמוה_מילא, S0B1Token: לתמוה_אם, S0B2Token: לתמוה_היה, S0Token: לתמוה, S0_LastThreeLetters: �ה, S0_LastTwoLetters: ה, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

16- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [מילא, אם, היה ,.. ]

B0Token: מילא, B0_LastThreeLetters: �א, B0_LastTwoLetters: א, B1Token: אם, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [מילא]   B= [אם, היה, גורם ,.. ]

B0Token: אם, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, B1Token: היה, B1_LastThreeLetters: �ה, B1_LastTwoLetters: ה, S0B0Token: מילא_אם, S0B1Token: מילא_היה, S0B2Token: מילא_גורם, S0Token: מילא, S0_LastThreeLetters: �א, S0_LastTwoLetters: א, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

18- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [אם, היה, גורם ,.. ]

B0Token: אם, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, B1Token: היה, B1_LastThreeLetters: �ה, B1_LastTwoLetters: ה, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [אם]   B= [היה, גורם, ביטחוני ,.. ]

B0Token: היה, B0_LastThreeLetters: �ה, B0_LastTwoLetters: ה, B1Token: גורם, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, S0B0Token: אם_היה, S0B1Token: אם_גורם, S0B2Token: אם_ביטחוני, S0Token: אם, S0_LastThreeLetters: �ם, S0_LastTwoLetters: ם, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

20- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [היה, גורם, ביטחוני ,.. ]

B0Token: היה, B0_LastThreeLetters: �ה, B0_LastTwoLetters: ה, B1Token: גורם, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [היה]   B= [גורם, ביטחוני, אחד ,.. ]

B0Token: גורם, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, B1Token: ביטחוני, B1_LastThreeLetters: �י, B1_LastTwoLetters: י, S0B0Token: היה_גורם, S0B1Token: היה_ביטחוני, S0B2Token: היה_אחד, S0Token: היה, S0_LastThreeLetters: �ה, S0_LastTwoLetters: ה, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

22- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [גורם, ביטחוני, אחד ,.. ]

B0Token: גורם, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, B1Token: ביטחוני, B1_LastThreeLetters: �י, B1_LastTwoLetters: י, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

23- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [גורם]   B= [ביטחוני, אחד, שקם ,.. ]

B0Token: ביטחוני, B0_LastThreeLetters: �י, B0_LastTwoLetters: י, B1Token: אחד, B1_LastThreeLetters: �ד, B1_LastTwoLetters: ד, S0B0Token: גורם_ביטחוני, S0B1Token: גורם_אחד, S0B2Token: גורם_שקם, S0Token: גורם, S0_LastThreeLetters: �ם, S0_LastTwoLetters: ם, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

24- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ביטחוני, אחד, שקם ,.. ]

B0Token: ביטחוני, B0_LastThreeLetters: �י, B0_LastTwoLetters: י, B1Token: אחד, B1_LastThreeLetters: �ד, B1_LastTwoLetters: ד, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

25- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ביטחוני]   B= [אחד, שקם, ואמר ,.. ]

B0Token: אחד, B0_LastThreeLetters: �ד, B0_LastTwoLetters: ד, B1Token: שקם, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, S0B0Token: ביטחוני_אחד, S0B1Token: ביטחוני_שקם, S0B2Token: ביטחוני_ואמר, S0Token: ביטחוני, S0_LastThreeLetters: �י, S0_LastTwoLetters: י, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

26- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [אחד, שקם, ואמר ,.. ]

B0Token: אחד, B0_LastThreeLetters: �ד, B0_LastTwoLetters: ד, B1Token: שקם, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

27- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [אחד]   B= [שקם, ואמר, שלאחר ,.. ]

B0Token: שקם, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, B1Token: ואמר, B1_LastThreeLetters: �ר, B1_LastTwoLetters: ר, S0B0Token: אחד_שקם, S0B1Token: אחד_ואמר, S0B2Token: אחד_שלאחר, S0Token: אחד, S0_LastThreeLetters: �ד, S0_LastTwoLetters: ד, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

28- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [שקם, ואמר, שלאחר ,.. ]

B0Token: שקם, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, B1Token: ואמר, B1_LastThreeLetters: �ר, B1_LastTwoLetters: ר, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

29- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [שקם]   B= [ואמר, שלאחר, העקירה ,.. ]

B0Token: ואמר, B0_LastThreeLetters: �ר, B0_LastTwoLetters: ר, B1Token: שלאחר, B1_LastThreeLetters: �ר, B1_LastTwoLetters: ר, S0B0Token: שקם_ואמר, S0B1Token: שקם_שלאחר, S0B2Token: שקם_העקירה, S0Token: שקם, S0_LastThreeLetters: �ם, S0_LastTwoLetters: ם, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

30- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ואמר, שלאחר, העקירה ,.. ]

B0Token: ואמר, B0_LastThreeLetters: �ר, B0_LastTwoLetters: ר, B1Token: שלאחר, B1_LastThreeLetters: �ר, B1_LastTwoLetters: ר, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

31- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ואמר]   B= [שלאחר, העקירה, תהיה ,.. ]

B0Token: שלאחר, B0_LastThreeLetters: �ר, B0_LastTwoLetters: ר, B1Token: העקירה, B1_LastThreeLetters: �ה, B1_LastTwoLetters: ה, S0B0Token: ואמר_שלאחר, S0B1Token: ואמר_העקירה, S0B2Token: ואמר_תהיה, S0Token: ואמר, S0_LastThreeLetters: �ר, S0_LastTwoLetters: ר, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

32- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [שלאחר, העקירה, תהיה ,.. ]

B0Token: שלאחר, B0_LastThreeLetters: �ר, B0_LastTwoLetters: ר, B1Token: העקירה, B1_LastThreeLetters: �ה, B1_LastTwoLetters: ה, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

33- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [שלאחר]   B= [העקירה, תהיה, כאן ,.. ]

B0Token: העקירה, B0_LastThreeLetters: �ה, B0_LastTwoLetters: ה, B1Token: תהיה, B1_LastThreeLetters: �ה, B1_LastTwoLetters: ה, S0B0Token: שלאחר_העקירה, S0B1Token: שלאחר_תהיה, S0B2Token: שלאחר_כאן, S0Token: שלאחר, S0_LastThreeLetters: �ר, S0_LastTwoLetters: ר, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

34- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [העקירה, תהיה, כאן ,.. ]

B0Token: העקירה, B0_LastThreeLetters: �ה, B0_LastTwoLetters: ה, B1Token: תהיה, B1_LastThreeLetters: �ה, B1_LastTwoLetters: ה, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

35- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [העקירה]   B= [תהיה, כאן, רגיעה ,.. ]

B0Token: תהיה, B0_LastThreeLetters: �ה, B0_LastTwoLetters: ה, B1Token: כאן, B1_LastThreeLetters: �ן, B1_LastTwoLetters: ן, S0B0Token: העקירה_תהיה, S0B1Token: העקירה_כאן, S0B2Token: העקירה_רגיעה, S0Token: העקירה, S0_LastThreeLetters: �ה, S0_LastTwoLetters: ה, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

36- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [תהיה, כאן, רגיעה ,.. ]

B0Token: תהיה, B0_LastThreeLetters: �ה, B0_LastTwoLetters: ה, B1Token: כאן, B1_LastThreeLetters: �ן, B1_LastTwoLetters: ן, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

37- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [תהיה]   B= [כאן, רגיעה, ביטחונית ,.. ]

B0Token: כאן, B0_LastThreeLetters: �ן, B0_LastTwoLetters: ן, B1Token: רגיעה, B1_LastThreeLetters: �ה, B1_LastTwoLetters: ה, S0B0Token: תהיה_כאן, S0B1Token: תהיה_רגיעה, S0B2Token: תהיה_ביטחונית, S0Token: תהיה, S0_LastThreeLetters: �ה, S0_LastTwoLetters: ה, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

38- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [כאן, רגיעה, ביטחונית ,.. ]

B0Token: כאן, B0_LastThreeLetters: �ן, B0_LastTwoLetters: ן, B1Token: רגיעה, B1_LastThreeLetters: �ה, B1_LastTwoLetters: ה, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

39- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [כאן]   B= [רגיעה, ביטחונית, ועם ,.. ]

B0Token: רגיעה, B0_LastThreeLetters: �ה, B0_LastTwoLetters: ה, B1Token: ביטחונית, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, S0B0Token: כאן_רגיעה, S0B1Token: כאן_ביטחונית, S0B2Token: כאן_ועם, S0Token: כאן, S0_LastThreeLetters: �ן, S0_LastTwoLetters: ן, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

40- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [רגיעה, ביטחונית, ועם ,.. ]

B0Token: רגיעה, B0_LastThreeLetters: �ה, B0_LastTwoLetters: ה, B1Token: ביטחונית, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

41- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [רגיעה]   B= [ביטחונית, ועם, ישראל ,.. ]

B0Token: ביטחונית, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: ועם, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, S0B0Token: רגיעה_ביטחונית, S0B1Token: רגיעה_ועם, S0B2Token: רגיעה_ישראל, S0Token: רגיעה, S0_LastThreeLetters: �ה, S0_LastTwoLetters: ה, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

42- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ביטחונית, ועם, ישראל ,.. ]

B0Token: ביטחונית, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: ועם, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

43- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ביטחונית]   B= [ועם, ישראל, ישכון ,.. ]

B0Token: ועם, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, B1Token: ישראל, B1_LastThreeLetters: �ל, B1_LastTwoLetters: ל, S0B0Token: ביטחונית_ועם, S0B1Token: ביטחונית_ישראל, S0B2Token: ביטחונית_ישכון, S0Token: ביטחונית, S0_LastThreeLetters: �ת, S0_LastTwoLetters: ת, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

44- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ועם, ישראל, ישכון ,.. ]

B0Token: ועם, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, B1Token: ישראל, B1_LastThreeLetters: �ל, B1_LastTwoLetters: ל, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

45- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ועם]   B= [ישראל, ישכון, לבטח ,.. ]

B0Token: ישראל, B0_LastThreeLetters: �ל, B0_LastTwoLetters: ל, B1Token: ישכון, B1_LastThreeLetters: �ן, B1_LastTwoLetters: ן, S0B0Token: ועם_ישראל, S0B1Token: ועם_ישכון, S0B2Token: ועם_לבטח, S0Token: ועם, S0_LastThreeLetters: �ם, S0_LastTwoLetters: ם, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

46- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ישראל, ישכון, לבטח ,.. ]

B0Token: ישראל, B0_LastThreeLetters: �ל, B0_LastTwoLetters: ל, B1Token: ישכון, B1_LastThreeLetters: �ן, B1_LastTwoLetters: ן, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

47- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ישראל]   B= [ישכון, לבטח, שלוש ,.. ]

B0Token: ישכון, B0_LastThreeLetters: �ן, B0_LastTwoLetters: ן, B1Token: לבטח, B1_LastThreeLetters: �ח, B1_LastTwoLetters: ח, S0B0Token: ישראל_ישכון, S0B1Token: ישראל_לבטח, S0B2Token: ישראל_שלוש, S0Token: ישראל, S0_LastThreeLetters: �ל, S0_LastTwoLetters: ל, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

48- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ישכון, לבטח, שלוש ,.. ]

B0Token: ישכון, B0_LastThreeLetters: �ן, B0_LastTwoLetters: ן, B1Token: לבטח, B1_LastThreeLetters: �ח, B1_LastTwoLetters: ח, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

49- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ישכון]   B= [לבטח, שלוש, מאות ,.. ]

B0Token: לבטח, B0_LastThreeLetters: �ח, B0_LastTwoLetters: ח, B1Token: שלוש, B1_LastThreeLetters: �ש, B1_LastTwoLetters: ש, S0B0Token: ישכון_לבטח, S0B1Token: ישכון_שלוש, S0B2Token: ישכון_מאות, S0Token: ישכון, S0_LastThreeLetters: �ן, S0_LastTwoLetters: ן, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

50- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ישכון, לבטח]   B= [שלוש, מאות, שנה ,.. ]

B0Token: שלוש, B0_LastThreeLetters: �ש, B0_LastTwoLetters: ש, B1Token: מאות, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, S0B0Token: לבטח_שלוש, S0B1Token: לבטח_מאות, S0B2Token: לבטח_שנה, S0Token: לבטח, S0_LastThreeLetters: �ח, S0_LastTwoLetters: ח, S1B0Token: ישכון_שלוש, S1S0Token: ישכון_לבטח, S1Token: ישכון, S1_LastThreeLetters: �ן, S1_LastTwoLetters: ן, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

51- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[ישכון, לבטח]]   B= [שלוש, מאות, שנה ,.. ]

B0Token: שלוש, B0_LastThreeLetters: �ש, B0_LastTwoLetters: ש, B1Token: מאות, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, S0B0Token: ישכון_לבטח_שלוש, S0B1Token: ישכון_לבטח_מאות, S0B2Token: ישכון_לבטח_שנה, S0Token: ישכון_לבטח, TransHistory1: 0, TransHistory2: 00, TransHistory3: 002, 

52- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [שלוש, מאות, שנה ,.. ]

B0Token: שלוש, B0_LastThreeLetters: �ש, B0_LastTwoLetters: ש, B1Token: מאות, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, TransHistory1: 1, TransHistory2: 10, TransHistory3: 100, 

53- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [שלוש]   B= [מאות, שנה, מבלי ,.. ]

B0Token: מאות, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: שנה, B1_LastThreeLetters: �ה, B1_LastTwoLetters: ה, S0B0Token: שלוש_מאות, S0B1Token: שלוש_שנה, S0B2Token: שלוש_מבלי, S0Token: שלוש, S0_LastThreeLetters: �ש, S0_LastTwoLetters: ש, TransHistory1: 2, TransHistory2: 21, TransHistory3: 210, 

54- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [מאות, שנה, מבלי ,.. ]

B0Token: מאות, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: שנה, B1_LastThreeLetters: �ה, B1_LastTwoLetters: ה, TransHistory1: 0, TransHistory2: 02, TransHistory3: 021, 

55- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [מאות]   B= [שנה, מבלי, שצר ,.. ]

B0Token: שנה, B0_LastThreeLetters: �ה, B0_LastTwoLetters: ה, B1Token: מבלי, B1_LastThreeLetters: �י, B1_LastTwoLetters: י, S0B0Token: מאות_שנה, S0B1Token: מאות_מבלי, S0B2Token: מאות_שצר, S0Token: מאות, S0_LastThreeLetters: �ת, S0_LastTwoLetters: ת, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

56- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [שנה, מבלי, שצר ,.. ]

B0Token: שנה, B0_LastThreeLetters: �ה, B0_LastTwoLetters: ה, B1Token: מבלי, B1_LastThreeLetters: �י, B1_LastTwoLetters: י, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

57- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [שנה]   B= [מבלי, שצר, ואויב ,.. ]

B0Token: מבלי, B0_LastThreeLetters: �י, B0_LastTwoLetters: י, B1Token: שצר, B1_LastThreeLetters: �ר, B1_LastTwoLetters: ר, S0B0Token: שנה_מבלי, S0B1Token: שנה_שצר, S0B2Token: שנה_ואויב, S0Token: שנה, S0_LastThreeLetters: �ה, S0_LastTwoLetters: ה, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

58- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [מבלי, שצר, ואויב ,.. ]

B0Token: מבלי, B0_LastThreeLetters: �י, B0_LastTwoLetters: י, B1Token: שצר, B1_LastThreeLetters: �ר, B1_LastTwoLetters: ר, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

59- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [מבלי]   B= [שצר, ואויב, יאיים ,.. ]

B0Token: שצר, B0_LastThreeLetters: �ר, B0_LastTwoLetters: ר, B1Token: ואויב, B1_LastThreeLetters: �ב, B1_LastTwoLetters: ב, S0B0Token: מבלי_שצר, S0B1Token: מבלי_ואויב, S0B2Token: מבלי_יאיים, S0Token: מבלי, S0_LastThreeLetters: �י, S0_LastTwoLetters: י, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

60- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [שצר, ואויב, יאיים ,.. ]

B0Token: שצר, B0_LastThreeLetters: �ר, B0_LastTwoLetters: ר, B1Token: ואויב, B1_LastThreeLetters: �ב, B1_LastTwoLetters: ב, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

61- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [שצר]   B= [ואויב, יאיים, עליו ,.. ]

B0Token: ואויב, B0_LastThreeLetters: �ב, B0_LastTwoLetters: ב, B1Token: יאיים, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, S0B0Token: שצר_ואויב, S0B1Token: שצר_יאיים, S0B2Token: שצר_עליו, S0Token: שצר, S0_LastThreeLetters: �ר, S0_LastTwoLetters: ר, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

62- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ואויב, יאיים, עליו ,.. ]

B0Token: ואויב, B0_LastThreeLetters: �ב, B0_LastTwoLetters: ב, B1Token: יאיים, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

63- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ואויב]   B= [יאיים, עליו, ניתן ,.. ]

B0Token: יאיים, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, B1Token: עליו, B1_LastThreeLetters: �ו, B1_LastTwoLetters: ו, S0B0Token: ואויב_יאיים, S0B1Token: ואויב_עליו, S0B2Token: ואויב_ניתן, S0Token: ואויב, S0_LastThreeLetters: �ב, S0_LastTwoLetters: ב, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

64- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [יאיים, עליו, ניתן ,.. ]

B0Token: יאיים, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, B1Token: עליו, B1_LastThreeLetters: �ו, B1_LastTwoLetters: ו, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

65- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [יאיים]   B= [עליו, ניתן, עדיין ,.. ]

B0Token: עליו, B0_LastThreeLetters: �ו, B0_LastTwoLetters: ו, B1Token: ניתן, B1_LastThreeLetters: �ן, B1_LastTwoLetters: ן, S0B0Token: יאיים_עליו, S0B1Token: יאיים_ניתן, S0B2Token: יאיים_עדיין, S0Token: יאיים, S0_LastThreeLetters: �ם, S0_LastTwoLetters: ם, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

66- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [עליו, ניתן, עדיין ,.. ]

B0Token: עליו, B0_LastThreeLetters: �ו, B0_LastTwoLetters: ו, B1Token: ניתן, B1_LastThreeLetters: �ן, B1_LastTwoLetters: ן, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

67- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [עליו]   B= [ניתן, עדיין, להבין ,.. ]

B0Token: ניתן, B0_LastThreeLetters: �ן, B0_LastTwoLetters: ן, B1Token: עדיין, B1_LastThreeLetters: �ן, B1_LastTwoLetters: ן, S0B0Token: עליו_ניתן, S0B1Token: עליו_עדיין, S0B2Token: עליו_להבין, S0Token: עליו, S0_LastThreeLetters: �ו, S0_LastTwoLetters: ו, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

68- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ניתן, עדיין, להבין ,.. ]

B0Token: ניתן, B0_LastThreeLetters: �ן, B0_LastTwoLetters: ן, B1Token: עדיין, B1_LastThreeLetters: �ן, B1_LastTwoLetters: ן, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

69- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ניתן]   B= [עדיין, להבין, שאם ,.. ]

B0Token: עדיין, B0_LastThreeLetters: �ן, B0_LastTwoLetters: ן, B1Token: להבין, B1_LastThreeLetters: �ן, B1_LastTwoLetters: ן, S0B0Token: ניתן_עדיין, S0B1Token: ניתן_להבין, S0B2Token: ניתן_שאם, S0Token: ניתן, S0_LastThreeLetters: �ן, S0_LastTwoLetters: ן, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

70- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [עדיין, להבין, שאם ,.. ]

B0Token: עדיין, B0_LastThreeLetters: �ן, B0_LastTwoLetters: ן, B1Token: להבין, B1_LastThreeLetters: �ן, B1_LastTwoLetters: ן, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

71- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [עדיין]   B= [להבין, שאם, כל ,.. ]

B0Token: להבין, B0_LastThreeLetters: �ן, B0_LastTwoLetters: ן, B1Token: שאם, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, S0B0Token: עדיין_להבין, S0B1Token: עדיין_שאם, S0B2Token: עדיין_כל, S0Token: עדיין, S0_LastThreeLetters: �ן, S0_LastTwoLetters: ן, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

72- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [להבין, שאם, כל ,.. ]

B0Token: להבין, B0_LastThreeLetters: �ן, B0_LastTwoLetters: ן, B1Token: שאם, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

73- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [להבין]   B= [שאם, כל, המציל ,.. ]

B0Token: שאם, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, B1Token: כל, B1_LastThreeLetters: �ל, B1_LastTwoLetters: ל, S0B0Token: להבין_שאם, S0B1Token: להבין_כל, S0B2Token: להבין_המציל, S0Token: להבין, S0_LastThreeLetters: �ן, S0_LastTwoLetters: ן, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

74- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [שאם, כל, המציל ,.. ]

B0Token: שאם, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, B1Token: כל, B1_LastThreeLetters: �ל, B1_LastTwoLetters: ל, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

75- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [שאם]   B= [כל, המציל, נפש ,.. ]

B0Token: כל, B0_LastThreeLetters: �ל, B0_LastTwoLetters: ל, B1Token: המציל, B1_LastThreeLetters: �ל, B1_LastTwoLetters: ל, S0B0Token: שאם_כל, S0B1Token: שאם_המציל, S0B2Token: שאם_נפש, S0Token: שאם, S0_LastThreeLetters: �ם, S0_LastTwoLetters: ם, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

76- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [כל, המציל, נפש ,.. ]

B0Token: כל, B0_LastThreeLetters: �ל, B0_LastTwoLetters: ל, B1Token: המציל, B1_LastThreeLetters: �ל, B1_LastTwoLetters: ל, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

77- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [כל]   B= [המציל, נפש, אחת ,.. ]

B0Token: המציל, B0_LastThreeLetters: �ל, B0_LastTwoLetters: ל, B1Token: נפש, B1_LastThreeLetters: �ש, B1_LastTwoLetters: ש, S0B0Token: כל_המציל, S0B1Token: כל_נפש, S0B2Token: כל_אחת, S0Token: כל, S0_LastThreeLetters: �ל, S0_LastTwoLetters: ל, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

78- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [כל, המציל]   B= [נפש, אחת, מישראל ,.. ]

B0Token: נפש, B0_LastThreeLetters: �ש, B0_LastTwoLetters: ש, B1Token: אחת, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, S0B0Token: המציל_נפש, S0B1Token: המציל_אחת, S0B2Token: המציל_מישראל, S0Token: המציל, S0_LastThreeLetters: �ל, S0_LastTwoLetters: ל, S1B0Token: כל_נפש, S1S0Token: כל_המציל, S1Token: כל, S1_LastThreeLetters: �ל, S1_LastTwoLetters: ל, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

79- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [כל, המציל, נפש]   B= [אחת, מישראל, כאילו ,.. ]

B0Token: אחת, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: מישראל, B1_LastThreeLetters: �ל, B1_LastTwoLetters: ל, S0B0Token: נפש_אחת, S0B1Token: נפש_מישראל, S0B2Token: נפש_כאילו, S0Token: נפש, S0_LastThreeLetters: �ש, S0_LastTwoLetters: ש, S1B0Token: המציל_אחת, S1S0Token: המציל_נפש, S1Token: המציל, S1_LastThreeLetters: �ל, S1_LastTwoLetters: ל, TransHistory1: 0, TransHistory2: 00, TransHistory3: 002, 

80- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [כל, המציל, נפש, אחת]   B= [מישראל, כאילו, קיים ,.. ]

B0Token: מישראל, B0_LastThreeLetters: �ל, B0_LastTwoLetters: ל, B1Token: כאילו, B1_LastThreeLetters: �ו, B1_LastTwoLetters: ו, S0B0Token: אחת_מישראל, S0B1Token: אחת_כאילו, S0B2Token: אחת_קיים, S0Token: אחת, S0_LastThreeLetters: �ת, S0_LastTwoLetters: ת, S1B0Token: נפש_מישראל, S1S0Token: נפש_אחת, S1Token: נפש, S1_LastThreeLetters: �ש, S1_LastTwoLetters: ש, TransHistory1: 0, TransHistory2: 00, TransHistory3: 000, 

81- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [כל, המציל, נפש, אחת, מישראל]   B= [כאילו, קיים, עולם ,.. ]

B0Token: כאילו, B0_LastThreeLetters: �ו, B0_LastTwoLetters: ו, B1Token: קיים, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, S0B0Token: מישראל_כאילו, S0B1Token: מישראל_קיים, S0B2Token: מישראל_עולם, S0Token: מישראל, S0_LastThreeLetters: �ל, S0_LastTwoLetters: ל, S1B0Token: אחת_כאילו, S1S0Token: אחת_מישראל, S1Token: אחת, S1_LastThreeLetters: �ת, S1_LastTwoLetters: ת, TransHistory1: 0, TransHistory2: 00, TransHistory3: 000, 

82- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [כל, המציל, נפש, אחת, מישראל, כאילו]   B= [קיים, עולם, אז ,.. ]

B0Token: קיים, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, B1Token: עולם, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, S0B0Token: כאילו_קיים, S0B1Token: כאילו_עולם, S0B2Token: כאילו_אז, S0Token: כאילו, S0_LastThreeLetters: �ו, S0_LastTwoLetters: ו, S1B0Token: מישראל_קיים, S1S0Token: מישראל_כאילו, S1Token: מישראל, S1_LastThreeLetters: �ל, S1_LastTwoLetters: ל, TransHistory1: 0, TransHistory2: 00, TransHistory3: 000, 

83- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [כל, המציל, נפש, אחת, מישראל, כאילו, קיים]   B= [עולם, אז, ניתן ,.. ]

B0Token: עולם, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, B1Token: אז, B1_LastThreeLetters: �ז, B1_LastTwoLetters: ז, S0B0Token: קיים_עולם, S0B1Token: קיים_אז, S0B2Token: קיים_ניתן, S0Token: קיים, S0_LastThreeLetters: �ם, S0_LastTwoLetters: ם, S1B0Token: כאילו_עולם, S1S0Token: כאילו_קיים, S1Token: כאילו, S1_LastThreeLetters: �ו, S1_LastTwoLetters: ו, TransHistory1: 0, TransHistory2: 00, TransHistory3: 000, 

84- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [כל, המציל, נפש, אחת, מישראל, כאילו, קיים, עולם]   B= [אז, ניתן, לשמוע ,.. ]

B0Token: אז, B0_LastThreeLetters: �ז, B0_LastTwoLetters: ז, B1Token: ניתן, B1_LastThreeLetters: �ן, B1_LastTwoLetters: ן, S0B0Token: עולם_אז, S0B1Token: עולם_ניתן, S0B2Token: עולם_לשמוע, S0Token: עולם, S0_LastThreeLetters: �ם, S0_LastTwoLetters: ם, S1B0Token: קיים_אז, S1S0Token: קיים_עולם, S1Token: קיים, S1_LastThreeLetters: �ם, S1_LastTwoLetters: ם, TransHistory1: 0, TransHistory2: 00, TransHistory3: 000, 

85- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [כל, המציל, נפש, אחת, מישראל, כאילו, [קיים, עולם]]   B= [אז, ניתן, לשמוע ,.. ]

B0Token: אז, B0_LastThreeLetters: �ז, B0_LastTwoLetters: ז, B1Token: ניתן, B1_LastThreeLetters: �ן, B1_LastTwoLetters: ן, S0B0Token: קיים_עולם_אז, S0B1Token: קיים_עולם_ניתן, S0B2Token: קיים_עולם_לשמוע, S0Token: קיים_עולם, S1B0Token: כאילו_אז, S1S0Token: כאילו_קיים_עולם, S1Token: כאילו, S1_LastThreeLetters: �ו, S1_LastTwoLetters: ו, TransHistory1: 0, TransHistory2: 00, TransHistory3: 000, 

86- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [כל, המציל, נפש, אחת, מישראל, [כאילו, [קיים, עולם]]]   B= [אז, ניתן, לשמוע ,.. ]

B0Token: אז, B0_LastThreeLetters: �ז, B0_LastTwoLetters: ז, B1Token: ניתן, B1_LastThreeLetters: �ן, B1_LastTwoLetters: ן, S0B0Token: כאילו_קיים_עולם_אז, S0B1Token: כאילו_קיים_עולם_ניתן, S0B2Token: כאילו_קיים_עולם_לשמוע, S0Token: כאילו_קיים_עולם, S1B0Token: מישראל_אז, S1S0Token: מישראל_כאילו_קיים_עולם, S1Token: מישראל, S1_LastThreeLetters: �ל, S1_LastTwoLetters: ל, TransHistory1: 1, TransHistory2: 10, TransHistory3: 100, 

87- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [כל, המציל, נפש, אחת, [מישראל, [כאילו, [קיים, עולם]]]]   B= [אז, ניתן, לשמוע ,.. ]

B0Token: אז, B0_LastThreeLetters: �ז, B0_LastTwoLetters: ז, B1Token: ניתן, B1_LastThreeLetters: �ן, B1_LastTwoLetters: ן, S0B0Token: מישראל_כאילו_קיים_עולם_אז, S0B1Token: מישראל_כאילו_קיים_עולם_ניתן, S0B2Token: מישראל_כאילו_קיים_עולם_לשמוע, S0Token: מישראל_כאילו_קיים_עולם, S1B0Token: אחת_אז, S1S0Token: אחת_מישראל_כאילו_קיים_עולם, S1Token: אחת, S1_LastThreeLetters: �ת, S1_LastTwoLetters: ת, TransHistory1: 1, TransHistory2: 11, TransHistory3: 110, 

88- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [כל, המציל, נפש, [אחת, [מישראל, [כאילו, [קיים, עולם]]]]]   B= [אז, ניתן, לשמוע ,.. ]

B0Token: אז, B0_LastThreeLetters: �ז, B0_LastTwoLetters: ז, B1Token: ניתן, B1_LastThreeLetters: �ן, B1_LastTwoLetters: ן, S0B0Token: אחת_מישראל_כאילו_קיים_עולם_אז, S0B1Token: אחת_מישראל_כאילו_קיים_עולם_ניתן, S0B2Token: אחת_מישראל_כאילו_קיים_עולם_לשמוע, S0Token: אחת_מישראל_כאילו_קיים_עולם, S1B0Token: נפש_אז, S1S0Token: נפש_אחת_מישראל_כאילו_קיים_עולם, S1Token: נפש, S1_LastThreeLetters: �ש, S1_LastTwoLetters: ש, TransHistory1: 1, TransHistory2: 11, TransHistory3: 111, 

89- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [כל, המציל, [נפש, [אחת, [מישראל, [כאילו, [קיים, עולם]]]]]]   B= [אז, ניתן, לשמוע ,.. ]

B0Token: אז, B0_LastThreeLetters: �ז, B0_LastTwoLetters: ז, B1Token: ניתן, B1_LastThreeLetters: �ן, B1_LastTwoLetters: ן, S0B0Token: נפש_אחת_מישראל_כאילו_קיים_עולם_אז, S0B1Token: נפש_אחת_מישראל_כאילו_קיים_עולם_ניתן, S0B2Token: נפש_אחת_מישראל_כאילו_קיים_עולם_לשמוע, S0Token: נפש_אחת_מישראל_כאילו_קיים_עולם, S1B0Token: המציל_אז, S1S0Token: המציל_נפש_אחת_מישראל_כאילו_קיים_עולם, S1Token: המציל, S1_LastThreeLetters: �ל, S1_LastTwoLetters: ל, TransHistory1: 1, TransHistory2: 11, TransHistory3: 111, 

90- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [כל, [המציל, [נפש, [אחת, [מישראל, [כאילו, [קיים, עולם]]]]]]]   B= [אז, ניתן, לשמוע ,.. ]

B0Token: אז, B0_LastThreeLetters: �ז, B0_LastTwoLetters: ז, B1Token: ניתן, B1_LastThreeLetters: �ן, B1_LastTwoLetters: ן, S0B0Token: המציל_נפש_אחת_מישראל_כאילו_קיים_עולם_אז, S0B1Token: המציל_נפש_אחת_מישראל_כאילו_קיים_עולם_ניתן, S0B2Token: המציל_נפש_אחת_מישראל_כאילו_קיים_עולם_לשמוע, S0Token: המציל_נפש_אחת_מישראל_כאילו_קיים_עולם, S1B0Token: כל_אז, S1S0Token: כל_המציל_נפש_אחת_מישראל_כאילו_קיים_עולם, S1Token: כל, S1_LastThreeLetters: �ל, S1_LastTwoLetters: ל, TransHistory1: 1, TransHistory2: 11, TransHistory3: 111, 

91- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[כל, [המציל, [נפש, [אחת, [מישראל, [כאילו, [קיים, עולם]]]]]]]]   B= [אז, ניתן, לשמוע ,.. ]

B0Token: אז, B0_LastThreeLetters: �ז, B0_LastTwoLetters: ז, B1Token: ניתן, B1_LastThreeLetters: �ן, B1_LastTwoLetters: ן, S0B0Token: כל_המציל_נפש_אחת_מישראל_כאילו_קיים_עולם_אז, S0B1Token: כל_המציל_נפש_אחת_מישראל_כאילו_קיים_עולם_ניתן, S0B2Token: כל_המציל_נפש_אחת_מישראל_כאילו_קיים_עולם_לשמוע, S0Token: כל_המציל_נפש_אחת_מישראל_כאילו_קיים_עולם, TransHistory1: 1, TransHistory2: 11, TransHistory3: 111, 

92- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [אז, ניתן, לשמוע ,.. ]

B0Token: אז, B0_LastThreeLetters: �ז, B0_LastTwoLetters: ז, B1Token: ניתן, B1_LastThreeLetters: �ן, B1_LastTwoLetters: ן, TransHistory1: 1, TransHistory2: 11, TransHistory3: 111, 

93- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [אז]   B= [ניתן, לשמוע, שיש ,.. ]

B0Token: ניתן, B0_LastThreeLetters: �ן, B0_LastTwoLetters: ן, B1Token: לשמוע, B1_LastThreeLetters: �ע, B1_LastTwoLetters: ע, S0B0Token: אז_ניתן, S0B1Token: אז_לשמוע, S0B2Token: אז_שיש, S0Token: אז, S0_LastThreeLetters: �ז, S0_LastTwoLetters: ז, TransHistory1: 2, TransHistory2: 21, TransHistory3: 211, 

94- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ניתן, לשמוע, שיש ,.. ]

B0Token: ניתן, B0_LastThreeLetters: �ן, B0_LastTwoLetters: ן, B1Token: לשמוע, B1_LastThreeLetters: �ע, B1_LastTwoLetters: ע, TransHistory1: 0, TransHistory2: 02, TransHistory3: 021, 

95- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ניתן]   B= [לשמוע, שיש, מישהו ,.. ]

B0Token: לשמוע, B0_LastThreeLetters: �ע, B0_LastTwoLetters: ע, B1Token: שיש, B1_LastThreeLetters: �ש, B1_LastTwoLetters: ש, S0B0Token: ניתן_לשמוע, S0B1Token: ניתן_שיש, S0B2Token: ניתן_מישהו, S0Token: ניתן, S0_LastThreeLetters: �ן, S0_LastTwoLetters: ן, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

96- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [לשמוע, שיש, מישהו ,.. ]

B0Token: לשמוע, B0_LastThreeLetters: �ע, B0_LastTwoLetters: ע, B1Token: שיש, B1_LastThreeLetters: �ש, B1_LastTwoLetters: ש, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

97- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [לשמוע]   B= [שיש, מישהו, שעם ,.. ]

B0Token: שיש, B0_LastThreeLetters: �ש, B0_LastTwoLetters: ש, B1Token: מישהו, B1_LastThreeLetters: �ו, B1_LastTwoLetters: ו, S0B0Token: לשמוע_שיש, S0B1Token: לשמוע_מישהו, S0B2Token: לשמוע_שעם, S0Token: לשמוע, S0_LastThreeLetters: �ע, S0_LastTwoLetters: ע, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

98- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [שיש, מישהו, שעם ,.. ]

B0Token: שיש, B0_LastThreeLetters: �ש, B0_LastTwoLetters: ש, B1Token: מישהו, B1_LastThreeLetters: �ו, B1_LastTwoLetters: ו, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

99- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [שיש]   B= [מישהו, שעם, כל ,.. ]

B0Token: מישהו, B0_LastThreeLetters: �ו, B0_LastTwoLetters: ו, B1Token: שעם, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, S0B0Token: שיש_מישהו, S0B1Token: שיש_שעם, S0B2Token: שיש_כל, S0Token: שיש, S0_LastThreeLetters: �ש, S0_LastTwoLetters: ש, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

100- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [מישהו, שעם, כל ,.. ]

B0Token: מישהו, B0_LastThreeLetters: �ו, B0_LastTwoLetters: ו, B1Token: שעם, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

101- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [מישהו]   B= [שעם, כל, הכאב ,.. ]

B0Token: שעם, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, B1Token: כל, B1_LastThreeLetters: �ל, B1_LastTwoLetters: ל, S0B0Token: מישהו_שעם, S0B1Token: מישהו_כל, S0B2Token: מישהו_הכאב, S0Token: מישהו, S0_LastThreeLetters: �ו, S0_LastTwoLetters: ו, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

102- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [שעם, כל, הכאב ,.. ]

B0Token: שעם, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, B1Token: כל, B1_LastThreeLetters: �ל, B1_LastTwoLetters: ל, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

103- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [שעם]   B= [כל, הכאב, חושב ,.. ]

B0Token: כל, B0_LastThreeLetters: �ל, B0_LastTwoLetters: ל, B1Token: הכאב, B1_LastThreeLetters: �ב, B1_LastTwoLetters: ב, S0B0Token: שעם_כל, S0B1Token: שעם_הכאב, S0B2Token: שעם_חושב, S0Token: שעם, S0_LastThreeLetters: �ם, S0_LastTwoLetters: ם, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

104- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [כל, הכאב, חושב ,.. ]

B0Token: כל, B0_LastThreeLetters: �ל, B0_LastTwoLetters: ל, B1Token: הכאב, B1_LastThreeLetters: �ב, B1_LastTwoLetters: ב, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

105- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [כל]   B= [הכאב, חושב, על ,.. ]

B0Token: הכאב, B0_LastThreeLetters: �ב, B0_LastTwoLetters: ב, B1Token: חושב, B1_LastThreeLetters: �ב, B1_LastTwoLetters: ב, S0B0Token: כל_הכאב, S0B1Token: כל_חושב, S0B2Token: כל_על, S0Token: כל, S0_LastThreeLetters: �ל, S0_LastTwoLetters: ל, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

106- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [הכאב, חושב, על ,.. ]

B0Token: הכאב, B0_LastThreeLetters: �ב, B0_LastTwoLetters: ב, B1Token: חושב, B1_LastThreeLetters: �ב, B1_LastTwoLetters: ב, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

107- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [הכאב]   B= [חושב, על, פינוי ,.. ]

B0Token: חושב, B0_LastThreeLetters: �ב, B0_LastTwoLetters: ב, B1Token: על, B1_LastThreeLetters: �ל, B1_LastTwoLetters: ל, S0B0Token: הכאב_חושב, S0B1Token: הכאב_על, S0B2Token: הכאב_פינוי, S0Token: הכאב, S0_LastThreeLetters: �ב, S0_LastTwoLetters: ב, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

108- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [חושב, על, פינוי ,.. ]

B0Token: חושב, B0_LastThreeLetters: �ב, B0_LastTwoLetters: ב, B1Token: על, B1_LastThreeLetters: �ל, B1_LastTwoLetters: ל, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

109- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [חושב]   B= [על, פינוי, של ,.. ]

B0Token: על, B0_LastThreeLetters: �ל, B0_LastTwoLetters: ל, B1Token: פינוי, B1_LastThreeLetters: �י, B1_LastTwoLetters: י, S0B0Token: חושב_על, S0B1Token: חושב_פינוי, S0B2Token: חושב_של, S0Token: חושב, S0_LastThreeLetters: �ב, S0_LastTwoLetters: ב, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

110- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [על, פינוי, של ,.. ]

B0Token: על, B0_LastThreeLetters: �ל, B0_LastTwoLetters: ל, B1Token: פינוי, B1_LastThreeLetters: �י, B1_LastTwoLetters: י, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

111- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [על]   B= [פינוי, של, הקברים ,.. ]

B0Token: פינוי, B0_LastThreeLetters: �י, B0_LastTwoLetters: י, B1Token: של, B1_LastThreeLetters: �ל, B1_LastTwoLetters: ל, S0B0Token: על_פינוי, S0B1Token: על_של, S0B2Token: על_הקברים, S0Token: על, S0_LastThreeLetters: �ל, S0_LastTwoLetters: ל, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

112- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [פינוי, של, הקברים ,.. ]

B0Token: פינוי, B0_LastThreeLetters: �י, B0_LastTwoLetters: י, B1Token: של, B1_LastThreeLetters: �ל, B1_LastTwoLetters: ל, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

113- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [פינוי]   B= [של, הקברים, אך ,.. ]

B0Token: של, B0_LastThreeLetters: �ל, B0_LastTwoLetters: ל, B1Token: הקברים, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, S0B0Token: פינוי_של, S0B1Token: פינוי_הקברים, S0B2Token: פינוי_אך, S0Token: פינוי, S0_LastThreeLetters: �י, S0_LastTwoLetters: י, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

114- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [של, הקברים, אך ,.. ]

B0Token: של, B0_LastThreeLetters: �ל, B0_LastTwoLetters: ל, B1Token: הקברים, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

115- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [של]   B= [הקברים, אך, כשממול ,.. ]

B0Token: הקברים, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, B1Token: אך, B1_LastThreeLetters: �ך, B1_LastTwoLetters: ך, S0B0Token: של_הקברים, S0B1Token: של_אך, S0B2Token: של_כשממול, S0Token: של, S0_LastThreeLetters: �ל, S0_LastTwoLetters: ל, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

116- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [הקברים, אך, כשממול ,.. ]

B0Token: הקברים, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, B1Token: אך, B1_LastThreeLetters: �ך, B1_LastTwoLetters: ך, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

117- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [הקברים]   B= [אך, כשממול, עומדים ,.. ]

B0Token: אך, B0_LastThreeLetters: �ך, B0_LastTwoLetters: ך, B1Token: כשממול, B1_LastThreeLetters: �ל, B1_LastTwoLetters: ל, S0B0Token: הקברים_אך, S0B1Token: הקברים_כשממול, S0B2Token: הקברים_עומדים, S0Token: הקברים, S0_LastThreeLetters: �ם, S0_LastTwoLetters: ם, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

118- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [אך, כשממול, עומדים ,.. ]

B0Token: אך, B0_LastThreeLetters: �ך, B0_LastTwoLetters: ך, B1Token: כשממול, B1_LastThreeLetters: �ל, B1_LastTwoLetters: ל, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

119- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [אך]   B= [כשממול, עומדים, כל ,.. ]

B0Token: כשממול, B0_LastThreeLetters: �ל, B0_LastTwoLetters: ל, B1Token: עומדים, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, S0B0Token: אך_כשממול, S0B1Token: אך_עומדים, S0B2Token: אך_כל, S0Token: אך, S0_LastThreeLetters: �ך, S0_LastTwoLetters: ך, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

120- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [כשממול, עומדים, כל ,.. ]

B0Token: כשממול, B0_LastThreeLetters: �ל, B0_LastTwoLetters: ל, B1Token: עומדים, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

121- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [כשממול]   B= [עומדים, כל, גורמי ,.. ]

B0Token: עומדים, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, B1Token: כל, B1_LastThreeLetters: �ל, B1_LastTwoLetters: ל, S0B0Token: כשממול_עומדים, S0B1Token: כשממול_כל, S0B2Token: כשממול_גורמי, S0Token: כשממול, S0_LastThreeLetters: �ל, S0_LastTwoLetters: ל, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

122- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [עומדים, כל, גורמי ,.. ]

B0Token: עומדים, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, B1Token: כל, B1_LastThreeLetters: �ל, B1_LastTwoLetters: ל, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

123- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [עומדים]   B= [כל, גורמי, הביטחון ,.. ]

B0Token: כל, B0_LastThreeLetters: �ל, B0_LastTwoLetters: ל, B1Token: גורמי, B1_LastThreeLetters: �י, B1_LastTwoLetters: י, S0B0Token: עומדים_כל, S0B1Token: עומדים_גורמי, S0B2Token: עומדים_הביטחון, S0Token: עומדים, S0_LastThreeLetters: �ם, S0_LastTwoLetters: ם, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

124- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [כל, גורמי, הביטחון ,.. ]

B0Token: כל, B0_LastThreeLetters: �ל, B0_LastTwoLetters: ל, B1Token: גורמי, B1_LastThreeLetters: �י, B1_LastTwoLetters: י, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

125- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [כל]   B= [גורמי, הביטחון, והדגש ,.. ]

B0Token: גורמי, B0_LastThreeLetters: �י, B0_LastTwoLetters: י, B1Token: הביטחון, B1_LastThreeLetters: �ן, B1_LastTwoLetters: ן, S0B0Token: כל_גורמי, S0B1Token: כל_הביטחון, S0B2Token: כל_והדגש, S0Token: כל, S0_LastThreeLetters: �ל, S0_LastTwoLetters: ל, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

126- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [גורמי, הביטחון, והדגש ,.. ]

B0Token: גורמי, B0_LastThreeLetters: �י, B0_LastTwoLetters: י, B1Token: הביטחון, B1_LastThreeLetters: �ן, B1_LastTwoLetters: ן, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

127- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [גורמי]   B= [הביטחון, והדגש, על ,.. ]

B0Token: הביטחון, B0_LastThreeLetters: �ן, B0_LastTwoLetters: ן, B1Token: והדגש, B1_LastThreeLetters: �ש, B1_LastTwoLetters: ש, S0B0Token: גורמי_הביטחון, S0B1Token: גורמי_והדגש, S0B2Token: גורמי_על, S0Token: גורמי, S0_LastThreeLetters: �י, S0_LastTwoLetters: י, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

128- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [הביטחון, והדגש, על ,.. ]

B0Token: הביטחון, B0_LastThreeLetters: �ן, B0_LastTwoLetters: ן, B1Token: והדגש, B1_LastThreeLetters: �ש, B1_LastTwoLetters: ש, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

129- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [הביטחון]   B= [והדגש, על, כל ,.. ]

B0Token: והדגש, B0_LastThreeLetters: �ש, B0_LastTwoLetters: ש, B1Token: על, B1_LastThreeLetters: �ל, B1_LastTwoLetters: ל, S0B0Token: הביטחון_והדגש, S0B1Token: הביטחון_על, S0B2Token: הביטחון_כל, S0Token: הביטחון, S0_LastThreeLetters: �ן, S0_LastTwoLetters: ן, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

130- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [והדגש, על, כל ,.. ]

B0Token: והדגש, B0_LastThreeLetters: �ש, B0_LastTwoLetters: ש, B1Token: על, B1_LastThreeLetters: �ל, B1_LastTwoLetters: ל, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

131- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [והדגש]   B= [על, כל, ואומרים ,.. ]

B0Token: על, B0_LastThreeLetters: �ל, B0_LastTwoLetters: ל, B1Token: כל, B1_LastThreeLetters: �ל, B1_LastTwoLetters: ל, S0B0Token: והדגש_על, S0B1Token: והדגש_כל, S0B2Token: והדגש_ואומרים, S0Token: והדגש, S0_LastThreeLetters: �ש, S0_LastTwoLetters: ש, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

132- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [על, כל, ואומרים ,.. ]

B0Token: על, B0_LastThreeLetters: �ל, B0_LastTwoLetters: ל, B1Token: כל, B1_LastThreeLetters: �ל, B1_LastTwoLetters: ל, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

133- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [על]   B= [כל, ואומרים, בפה ,.. ]

B0Token: כל, B0_LastThreeLetters: �ל, B0_LastTwoLetters: ל, B1Token: ואומרים, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, S0B0Token: על_כל, S0B1Token: על_ואומרים, S0B2Token: על_בפה, S0Token: על, S0_LastThreeLetters: �ל, S0_LastTwoLetters: ל, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

134- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [כל, ואומרים, בפה ,.. ]

B0Token: כל, B0_LastThreeLetters: �ל, B0_LastTwoLetters: ל, B1Token: ואומרים, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

135- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [כל]   B= [ואומרים, בפה, מלא ,.. ]

B0Token: ואומרים, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, B1Token: בפה, B1_LastThreeLetters: �ה, B1_LastTwoLetters: ה, S0B0Token: כל_ואומרים, S0B1Token: כל_בפה, S0B2Token: כל_מלא, S0Token: כל, S0_LastThreeLetters: �ל, S0_LastTwoLetters: ל, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

136- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ואומרים, בפה, מלא ,.. ]

B0Token: ואומרים, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, B1Token: בפה, B1_LastThreeLetters: �ה, B1_LastTwoLetters: ה, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

137- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ואומרים]   B= [בפה, מלא, שתוכנית ,.. ]

B0Token: בפה, B0_LastThreeLetters: �ה, B0_LastTwoLetters: ה, B1Token: מלא, B1_LastThreeLetters: �א, B1_LastTwoLetters: א, S0B0Token: ואומרים_בפה, S0B1Token: ואומרים_מלא, S0B2Token: ואומרים_שתוכנית, S0Token: ואומרים, S0_LastThreeLetters: �ם, S0_LastTwoLetters: ם, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

138- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ואומרים, בפה]   B= [מלא, שתוכנית, ההתנתקות ,.. ]

B0Token: מלא, B0_LastThreeLetters: �א, B0_LastTwoLetters: א, B1Token: שתוכנית, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, S0B0Token: בפה_מלא, S0B1Token: בפה_שתוכנית, S0B2Token: בפה_ההתנתקות, S0Token: בפה, S0_LastThreeLetters: �ה, S0_LastTwoLetters: ה, S1B0Token: ואומרים_מלא, S1S0Token: ואומרים_בפה, S1Token: ואומרים, S1_LastThreeLetters: �ם, S1_LastTwoLetters: ם, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

139- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ואומרים, בפה, מלא]   B= [שתוכנית, ההתנתקות, רק ,.. ]

B0Token: שתוכנית, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: ההתנתקות, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, S0B0Token: מלא_שתוכנית, S0B1Token: מלא_ההתנתקות, S0B2Token: מלא_רק, S0Token: מלא, S0_LastThreeLetters: �א, S0_LastTwoLetters: א, S1B0Token: בפה_שתוכנית, S1S0Token: בפה_מלא, S1Token: בפה, S1_LastThreeLetters: �ה, S1_LastTwoLetters: ה, TransHistory1: 0, TransHistory2: 00, TransHistory3: 002, 

140- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ואומרים, [בפה, מלא]]   B= [שתוכנית, ההתנתקות, רק ,.. ]

B0Token: שתוכנית, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: ההתנתקות, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, S0B0Token: בפה_מלא_שתוכנית, S0B1Token: בפה_מלא_ההתנתקות, S0B2Token: בפה_מלא_רק, S0Token: בפה_מלא, S1B0Token: ואומרים_שתוכנית, S1S0Token: ואומרים_בפה_מלא, S1Token: ואומרים, S1_LastThreeLetters: �ם, S1_LastTwoLetters: ם, TransHistory1: 0, TransHistory2: 00, TransHistory3: 000, 

141- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[ואומרים, [בפה, מלא]]]   B= [שתוכנית, ההתנתקות, רק ,.. ]

B0Token: שתוכנית, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: ההתנתקות, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, S0B0Token: ואומרים_בפה_מלא_שתוכנית, S0B1Token: ואומרים_בפה_מלא_ההתנתקות, S0B2Token: ואומרים_בפה_מלא_רק, S0Token: ואומרים_בפה_מלא, TransHistory1: 1, TransHistory2: 10, TransHistory3: 100, 

142- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [שתוכנית, ההתנתקות, רק ,.. ]

B0Token: שתוכנית, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: ההתנתקות, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, TransHistory1: 1, TransHistory2: 11, TransHistory3: 110, 

143- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [שתוכנית]   B= [ההתנתקות, רק, תזיק ,.. ]

B0Token: ההתנתקות, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: רק, B1_LastThreeLetters: �ק, B1_LastTwoLetters: ק, S0B0Token: שתוכנית_ההתנתקות, S0B1Token: שתוכנית_רק, S0B2Token: שתוכנית_תזיק, S0Token: שתוכנית, S0_LastThreeLetters: �ת, S0_LastTwoLetters: ת, TransHistory1: 2, TransHistory2: 21, TransHistory3: 211, 

144- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ההתנתקות, רק, תזיק ,.. ]

B0Token: ההתנתקות, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: רק, B1_LastThreeLetters: �ק, B1_LastTwoLetters: ק, TransHistory1: 0, TransHistory2: 02, TransHistory3: 021, 

145- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ההתנתקות]   B= [רק, תזיק, לעתידנו ,.. ]

B0Token: רק, B0_LastThreeLetters: �ק, B0_LastTwoLetters: ק, B1Token: תזיק, B1_LastThreeLetters: �ק, B1_LastTwoLetters: ק, S0B0Token: ההתנתקות_רק, S0B1Token: ההתנתקות_תזיק, S0B2Token: ההתנתקות_לעתידנו, S0Token: ההתנתקות, S0_LastThreeLetters: �ת, S0_LastTwoLetters: ת, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

146- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [רק, תזיק, לעתידנו ,.. ]

B0Token: רק, B0_LastThreeLetters: �ק, B0_LastTwoLetters: ק, B1Token: תזיק, B1_LastThreeLetters: �ק, B1_LastTwoLetters: ק, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

147- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [רק]   B= [תזיק, לעתידנו, והמחבלים ,.. ]

B0Token: תזיק, B0_LastThreeLetters: �ק, B0_LastTwoLetters: ק, B1Token: לעתידנו, B1_LastThreeLetters: �ו, B1_LastTwoLetters: ו, S0B0Token: רק_תזיק, S0B1Token: רק_לעתידנו, S0B2Token: רק_והמחבלים, S0Token: רק, S0_LastThreeLetters: �ק, S0_LastTwoLetters: ק, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

148- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [תזיק, לעתידנו, והמחבלים ,.. ]

B0Token: תזיק, B0_LastThreeLetters: �ק, B0_LastTwoLetters: ק, B1Token: לעתידנו, B1_LastThreeLetters: �ו, B1_LastTwoLetters: ו, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

149- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [תזיק]   B= [לעתידנו, והמחבלים, רק ,.. ]

B0Token: לעתידנו, B0_LastThreeLetters: �ו, B0_LastTwoLetters: ו, B1Token: והמחבלים, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, S0B0Token: תזיק_לעתידנו, S0B1Token: תזיק_והמחבלים, S0B2Token: תזיק_רק, S0Token: תזיק, S0_LastThreeLetters: �ק, S0_LastTwoLetters: ק, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

150- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [לעתידנו, והמחבלים, רק ,.. ]

B0Token: לעתידנו, B0_LastThreeLetters: �ו, B0_LastTwoLetters: ו, B1Token: והמחבלים, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

151- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [לעתידנו]   B= [והמחבלים, רק, יקרבו ,.. ]

B0Token: והמחבלים, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, B1Token: רק, B1_LastThreeLetters: �ק, B1_LastTwoLetters: ק, S0B0Token: לעתידנו_והמחבלים, S0B1Token: לעתידנו_רק, S0B2Token: לעתידנו_יקרבו, S0Token: לעתידנו, S0_LastThreeLetters: �ו, S0_LastTwoLetters: ו, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

152- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [והמחבלים, רק, יקרבו ,.. ]

B0Token: והמחבלים, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, B1Token: רק, B1_LastThreeLetters: �ק, B1_LastTwoLetters: ק, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

153- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [והמחבלים]   B= [רק, יקרבו, את ,.. ]

B0Token: רק, B0_LastThreeLetters: �ק, B0_LastTwoLetters: ק, B1Token: יקרבו, B1_LastThreeLetters: �ו, B1_LastTwoLetters: ו, S0B0Token: והמחבלים_רק, S0B1Token: והמחבלים_יקרבו, S0B2Token: והמחבלים_את, S0Token: והמחבלים, S0_LastThreeLetters: �ם, S0_LastTwoLetters: ם, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

154- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [רק, יקרבו, את ,.. ]

B0Token: רק, B0_LastThreeLetters: �ק, B0_LastTwoLetters: ק, B1Token: יקרבו, B1_LastThreeLetters: �ו, B1_LastTwoLetters: ו, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

155- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [רק]   B= [יקרבו, את, קו ,.. ]

B0Token: יקרבו, B0_LastThreeLetters: �ו, B0_LastTwoLetters: ו, B1Token: את, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, S0B0Token: רק_יקרבו, S0B1Token: רק_את, S0B2Token: רק_קו, S0Token: רק, S0_LastThreeLetters: �ק, S0_LastTwoLetters: ק, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

156- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [יקרבו, את, קו ,.. ]

B0Token: יקרבו, B0_LastThreeLetters: �ו, B0_LastTwoLetters: ו, B1Token: את, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

157- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [יקרבו]   B= [את, קו, הגבול ,.. ]

B0Token: את, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: קו, B1_LastThreeLetters: �ו, B1_LastTwoLetters: ו, S0B0Token: יקרבו_את, S0B1Token: יקרבו_קו, S0B2Token: יקרבו_הגבול, S0Token: יקרבו, S0_LastThreeLetters: �ו, S0_LastTwoLetters: ו, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

158- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [את, קו, הגבול ,.. ]

B0Token: את, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: קו, B1_LastThreeLetters: �ו, B1_LastTwoLetters: ו, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

159- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [את]   B= [קו, הגבול, וזה ,.. ]

B0Token: קו, B0_LastThreeLetters: �ו, B0_LastTwoLetters: ו, B1Token: הגבול, B1_LastThreeLetters: �ל, B1_LastTwoLetters: ל, S0B0Token: את_קו, S0B1Token: את_הגבול, S0B2Token: את_וזה, S0Token: את, S0_LastThreeLetters: �ת, S0_LastTwoLetters: ת, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

160- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [קו, הגבול, וזה ,.. ]

B0Token: קו, B0_LastThreeLetters: �ו, B0_LastTwoLetters: ו, B1Token: הגבול, B1_LastThreeLetters: �ל, B1_LastTwoLetters: ל, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

161- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [קו]   B= [הגבול, וזה, ייתן ,.. ]

B0Token: הגבול, B0_LastThreeLetters: �ל, B0_LastTwoLetters: ל, B1Token: וזה, B1_LastThreeLetters: �ה, B1_LastTwoLetters: ה, S0B0Token: קו_הגבול, S0B1Token: קו_וזה, S0B2Token: קו_ייתן, S0Token: קו, S0_LastThreeLetters: �ו, S0_LastTwoLetters: ו, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

162- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [הגבול, וזה, ייתן ,.. ]

B0Token: הגבול, B0_LastThreeLetters: �ל, B0_LastTwoLetters: ל, B1Token: וזה, B1_LastThreeLetters: �ה, B1_LastTwoLetters: ה, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

163- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [הגבול]   B= [וזה, ייתן, להם ,.. ]

B0Token: וזה, B0_LastThreeLetters: �ה, B0_LastTwoLetters: ה, B1Token: ייתן, B1_LastThreeLetters: �ן, B1_LastTwoLetters: ן, S0B0Token: הגבול_וזה, S0B1Token: הגבול_ייתן, S0B2Token: הגבול_להם, S0Token: הגבול, S0_LastThreeLetters: �ל, S0_LastTwoLetters: ל, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

164- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [וזה, ייתן, להם ,.. ]

B0Token: וזה, B0_LastThreeLetters: �ה, B0_LastTwoLetters: ה, B1Token: ייתן, B1_LastThreeLetters: �ן, B1_LastTwoLetters: ן, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

165- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [וזה]   B= [ייתן, להם, רוח ,.. ]

B0Token: ייתן, B0_LastThreeLetters: �ן, B0_LastTwoLetters: ן, B1Token: להם, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, S0B0Token: וזה_ייתן, S0B1Token: וזה_להם, S0B2Token: וזה_רוח, S0Token: וזה, S0_LastThreeLetters: �ה, S0_LastTwoLetters: ה, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

166- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ייתן, להם, רוח ,.. ]

B0Token: ייתן, B0_LastThreeLetters: �ן, B0_LastTwoLetters: ן, B1Token: להם, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

167- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ייתן]   B= [להם, רוח, גבית ,.. ]

B0Token: להם, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, B1Token: רוח, B1_LastThreeLetters: �ח, B1_LastTwoLetters: ח, S0B0Token: ייתן_להם, S0B1Token: ייתן_רוח, S0B2Token: ייתן_גבית, S0Token: ייתן, S0_LastThreeLetters: �ן, S0_LastTwoLetters: ן, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

168- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ייתן, להם]   B= [רוח, גבית, להמשך ,.. ]

B0Token: רוח, B0_LastThreeLetters: �ח, B0_LastTwoLetters: ח, B1Token: גבית, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, S0B0Token: להם_רוח, S0B1Token: להם_גבית, S0B2Token: להם_להמשך, S0Token: להם, S0_LastThreeLetters: �ם, S0_LastTwoLetters: ם, S1B0Token: ייתן_רוח, S1S0Token: ייתן_להם, S1Token: ייתן, S1_LastThreeLetters: �ן, S1_LastTwoLetters: ן, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

169- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ייתן, להם, רוח]   B= [גבית, להמשך, מעשה ,.. ]

B0Token: גבית, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: להמשך, B1_LastThreeLetters: �ך, B1_LastTwoLetters: ך, S0B0Token: רוח_גבית, S0B1Token: רוח_להמשך, S0B2Token: רוח_מעשה, S0Token: רוח, S0_LastThreeLetters: �ח, S0_LastTwoLetters: ח, S1B0Token: להם_גבית, S1S0Token: להם_רוח, S1Token: להם, S1_LastThreeLetters: �ם, S1_LastTwoLetters: ם, TransHistory1: 0, TransHistory2: 00, TransHistory3: 002, 

170- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ייתן, להם, רוח, גבית]   B= [להמשך, מעשה, הטרור ,.. ]

B0Token: להמשך, B0_LastThreeLetters: �ך, B0_LastTwoLetters: ך, B1Token: מעשה, B1_LastThreeLetters: �ה, B1_LastTwoLetters: ה, S0B0Token: גבית_להמשך, S0B1Token: גבית_מעשה, S0B2Token: גבית_הטרור, S0Token: גבית, S0_LastThreeLetters: �ת, S0_LastTwoLetters: ת, S1B0Token: רוח_להמשך, S1S0Token: רוח_גבית, S1Token: רוח, S1_LastThreeLetters: �ח, S1_LastTwoLetters: ח, TransHistory1: 0, TransHistory2: 00, TransHistory3: 000, 

171- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ייתן, להם, [רוח, גבית]]   B= [להמשך, מעשה, הטרור ,.. ]

B0Token: להמשך, B0_LastThreeLetters: �ך, B0_LastTwoLetters: ך, B1Token: מעשה, B1_LastThreeLetters: �ה, B1_LastTwoLetters: ה, S0B0Token: רוח_גבית_להמשך, S0B1Token: רוח_גבית_מעשה, S0B2Token: רוח_גבית_הטרור, S0Token: רוח_גבית, S1B0Token: להם_להמשך, S1S0Token: להם_רוח_גבית, S1Token: להם, S1_LastThreeLetters: �ם, S1_LastTwoLetters: ם, TransHistory1: 0, TransHistory2: 00, TransHistory3: 000, 

172- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ייתן, [להם, [רוח, גבית]]]   B= [להמשך, מעשה, הטרור ,.. ]

B0Token: להמשך, B0_LastThreeLetters: �ך, B0_LastTwoLetters: ך, B1Token: מעשה, B1_LastThreeLetters: �ה, B1_LastTwoLetters: ה, S0B0Token: להם_רוח_גבית_להמשך, S0B1Token: להם_רוח_גבית_מעשה, S0B2Token: להם_רוח_גבית_הטרור, S0Token: להם_רוח_גבית, S1B0Token: ייתן_להמשך, S1S0Token: ייתן_להם_רוח_גבית, S1Token: ייתן, S1_LastThreeLetters: �ן, S1_LastTwoLetters: ן, TransHistory1: 1, TransHistory2: 10, TransHistory3: 100, 

173- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[ייתן, [להם, [רוח, גבית]]]]   B= [להמשך, מעשה, הטרור ,.. ]

B0Token: להמשך, B0_LastThreeLetters: �ך, B0_LastTwoLetters: ך, B1Token: מעשה, B1_LastThreeLetters: �ה, B1_LastTwoLetters: ה, S0B0Token: ייתן_להם_רוח_גבית_להמשך, S0B1Token: ייתן_להם_רוח_גבית_מעשה, S0B2Token: ייתן_להם_רוח_גבית_הטרור, S0Token: ייתן_להם_רוח_גבית, TransHistory1: 1, TransHistory2: 11, TransHistory3: 110, 

174- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [להמשך, מעשה, הטרור ,.. ]

B0Token: להמשך, B0_LastThreeLetters: �ך, B0_LastTwoLetters: ך, B1Token: מעשה, B1_LastThreeLetters: �ה, B1_LastTwoLetters: ה, TransHistory1: 1, TransHistory2: 11, TransHistory3: 111, 

175- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [להמשך]   B= [מעשה, הטרור, איזה ,.. ]

B0Token: מעשה, B0_LastThreeLetters: �ה, B0_LastTwoLetters: ה, B1Token: הטרור, B1_LastThreeLetters: �ר, B1_LastTwoLetters: ר, S0B0Token: להמשך_מעשה, S0B1Token: להמשך_הטרור, S0B2Token: להמשך_איזה, S0Token: להמשך, S0_LastThreeLetters: �ך, S0_LastTwoLetters: ך, TransHistory1: 2, TransHistory2: 21, TransHistory3: 211, 

176- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [מעשה, הטרור, איזה ,.. ]

B0Token: מעשה, B0_LastThreeLetters: �ה, B0_LastTwoLetters: ה, B1Token: הטרור, B1_LastThreeLetters: �ר, B1_LastTwoLetters: ר, TransHistory1: 0, TransHistory2: 02, TransHistory3: 021, 

177- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [מעשה]   B= [הטרור, איזה, היתר ,.. ]

B0Token: הטרור, B0_LastThreeLetters: �ר, B0_LastTwoLetters: ר, B1Token: איזה, B1_LastThreeLetters: �ה, B1_LastTwoLetters: ה, S0B0Token: מעשה_הטרור, S0B1Token: מעשה_איזה, S0B2Token: מעשה_היתר, S0Token: מעשה, S0_LastThreeLetters: �ה, S0_LastTwoLetters: ה, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

178- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [הטרור, איזה, היתר ,.. ]

B0Token: הטרור, B0_LastThreeLetters: �ר, B0_LastTwoLetters: ר, B1Token: איזה, B1_LastThreeLetters: �ה, B1_LastTwoLetters: ה, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

179- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [הטרור]   B= [איזה, היתר, יש ,.. ]

B0Token: איזה, B0_LastThreeLetters: �ה, B0_LastTwoLetters: ה, B1Token: היתר, B1_LastThreeLetters: �ר, B1_LastTwoLetters: ר, S0B0Token: הטרור_איזה, S0B1Token: הטרור_היתר, S0B2Token: הטרור_יש, S0Token: הטרור, S0_LastThreeLetters: �ר, S0_LastTwoLetters: ר, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

180- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [איזה, היתר, יש ,.. ]

B0Token: איזה, B0_LastThreeLetters: �ה, B0_LastTwoLetters: ה, B1Token: היתר, B1_LastThreeLetters: �ר, B1_LastTwoLetters: ר, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

181- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [איזה]   B= [היתר, יש, לפנות ,.. ]

B0Token: היתר, B0_LastThreeLetters: �ר, B0_LastTwoLetters: ר, B1Token: יש, B1_LastThreeLetters: �ש, B1_LastTwoLetters: ש, S0B0Token: איזה_היתר, S0B1Token: איזה_יש, S0B2Token: איזה_לפנות, S0Token: איזה, S0_LastThreeLetters: �ה, S0_LastTwoLetters: ה, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

182- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [היתר, יש, לפנות ,.. ]

B0Token: היתר, B0_LastThreeLetters: �ר, B0_LastTwoLetters: ר, B1Token: יש, B1_LastThreeLetters: �ש, B1_LastTwoLetters: ש, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

183- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [היתר]   B= [יש, לפנות, שוכני ,.. ]

B0Token: יש, B0_LastThreeLetters: �ש, B0_LastTwoLetters: ש, B1Token: לפנות, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, S0B0Token: היתר_יש, S0B1Token: היתר_לפנות, S0B2Token: היתר_שוכני, S0Token: היתר, S0_LastThreeLetters: �ר, S0_LastTwoLetters: ר, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

184- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [יש, לפנות, שוכני ,.. ]

B0Token: יש, B0_LastThreeLetters: �ש, B0_LastTwoLetters: ש, B1Token: לפנות, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

185- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [יש]   B= [לפנות, שוכני, עפר ,.. ]

B0Token: לפנות, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: שוכני, B1_LastThreeLetters: �י, B1_LastTwoLetters: י, S0B0Token: יש_לפנות, S0B1Token: יש_שוכני, S0B2Token: יש_עפר, S0Token: יש, S0_LastThreeLetters: �ש, S0_LastTwoLetters: ש, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

186- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [לפנות, שוכני, עפר ,.. ]

B0Token: לפנות, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: שוכני, B1_LastThreeLetters: �י, B1_LastTwoLetters: י, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

187- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [לפנות]   B= [שוכני, עפר, ממקום ,.. ]

B0Token: שוכני, B0_LastThreeLetters: �י, B0_LastTwoLetters: י, B1Token: עפר, B1_LastThreeLetters: �ר, B1_LastTwoLetters: ר, S0B0Token: לפנות_שוכני, S0B1Token: לפנות_עפר, S0B2Token: לפנות_ממקום, S0Token: לפנות, S0_LastThreeLetters: �ת, S0_LastTwoLetters: ת, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

188- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [שוכני, עפר, ממקום ,.. ]

B0Token: שוכני, B0_LastThreeLetters: �י, B0_LastTwoLetters: י, B1Token: עפר, B1_LastThreeLetters: �ר, B1_LastTwoLetters: ר, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

189- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [שוכני]   B= [עפר, ממקום, מנוחתם ,.. ]

B0Token: עפר, B0_LastThreeLetters: �ר, B0_LastTwoLetters: ר, B1Token: ממקום, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, S0B0Token: שוכני_עפר, S0B1Token: שוכני_ממקום, S0B2Token: שוכני_מנוחתם, S0Token: שוכני, S0_LastThreeLetters: �י, S0_LastTwoLetters: י, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

190- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [שוכני, עפר]   B= [ממקום, מנוחתם ,.. ]

B0Token: ממקום, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, B1Token: מנוחתם, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, S0B0Token: עפר_ממקום, S0B1Token: עפר_מנוחתם, S0Token: עפר, S0_LastThreeLetters: �ר, S0_LastTwoLetters: ר, S1B0Token: שוכני_ממקום, S1S0Token: שוכני_עפר, S1Token: שוכני, S1_LastThreeLetters: �י, S1_LastTwoLetters: י, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

191- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[שוכני, עפר]]   B= [ממקום, מנוחתם ,.. ]

B0Token: ממקום, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, B1Token: מנוחתם, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, S0B0Token: שוכני_עפר_ממקום, S0B1Token: שוכני_עפר_מנוחתם, S0Token: שוכני_עפר, TransHistory1: 0, TransHistory2: 00, TransHistory3: 002, 

192- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ממקום, מנוחתם ,.. ]

B0Token: ממקום, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, B1Token: מנוחתם, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, TransHistory1: 1, TransHistory2: 10, TransHistory3: 100, 

193- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ממקום]   B= [מנוחתם]

B0Token: מנוחתם, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, S0B0Token: ממקום_מנוחתם, S0Token: ממקום, S0_LastThreeLetters: �ם, S0_LastTwoLetters: ם, TransHistory1: 2, TransHistory2: 21, TransHistory3: 210, 

194- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [מנוחתם]

B0Token: מנוחתם, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, TransHistory1: 0, TransHistory2: 02, TransHistory3: 021, 

195- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [מנוחתם]   B= [ ]

S0Token: מנוחתם, S0_LastThreeLetters: �ם, S0_LastTwoLetters: ם, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

196- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

## Sentence No. 174 - 
אבל חברים המשיך ריבלין בדברי עידוד לבאי האירוע כשם שמנחם בגין וזאב לא כופפו ראשם וכך לימדנו גם תלמידם וחברם שמואל חתן השמחה גם אנו לא נכרע ולא ולא ולא נבוש ונאבק עד שנכבוש את ההר
### Existing MWEs: 
1- **כופפו ראשם** (ID)
2- **לא נכרע** (OTH)
3- **ולא נבוש** (OTH)
4- **שנכבוש את ההר** (OTH)



0- &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [אבל, חברים, המשיך ,.. ]

B0Token: אבל, B0_LastThreeLetters: �ל, B0_LastTwoLetters: ל, B1Token: חברים, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, 

1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [אבל]   B= [חברים, המשיך, ריבלין ,.. ]

B0Token: חברים, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, B1Token: המשיך, B1_LastThreeLetters: �ך, B1_LastTwoLetters: ך, S0B0Token: אבל_חברים, S0B1Token: אבל_המשיך, S0B2Token: אבל_ריבלין, S0Token: אבל, S0_LastThreeLetters: �ל, S0_LastTwoLetters: ל, 

2- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [חברים, המשיך, ריבלין ,.. ]

B0Token: חברים, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, B1Token: המשיך, B1_LastThreeLetters: �ך, B1_LastTwoLetters: ך, TransHistory1: 0, 

3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [חברים]   B= [המשיך, ריבלין, בדברי ,.. ]

B0Token: המשיך, B0_LastThreeLetters: �ך, B0_LastTwoLetters: ך, B1Token: ריבלין, B1_LastThreeLetters: �ן, B1_LastTwoLetters: ן, S0B0Token: חברים_המשיך, S0B1Token: חברים_ריבלין, S0B2Token: חברים_בדברי, S0Token: חברים, S0_LastThreeLetters: �ם, S0_LastTwoLetters: ם, TransHistory1: 2, TransHistory2: 20, 

4- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [המשיך, ריבלין, בדברי ,.. ]

B0Token: המשיך, B0_LastThreeLetters: �ך, B0_LastTwoLetters: ך, B1Token: ריבלין, B1_LastThreeLetters: �ן, B1_LastTwoLetters: ן, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [המשיך]   B= [ריבלין, בדברי, עידוד ,.. ]

B0Token: ריבלין, B0_LastThreeLetters: �ן, B0_LastTwoLetters: ן, B1Token: בדברי, B1_LastThreeLetters: �י, B1_LastTwoLetters: י, S0B0Token: המשיך_ריבלין, S0B1Token: המשיך_בדברי, S0B2Token: המשיך_עידוד, S0Token: המשיך, S0_LastThreeLetters: �ך, S0_LastTwoLetters: ך, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

6- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ריבלין, בדברי, עידוד ,.. ]

B0Token: ריבלין, B0_LastThreeLetters: �ן, B0_LastTwoLetters: ן, B1Token: בדברי, B1_LastThreeLetters: �י, B1_LastTwoLetters: י, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ריבלין]   B= [בדברי, עידוד, לבאי ,.. ]

B0Token: בדברי, B0_LastThreeLetters: �י, B0_LastTwoLetters: י, B1Token: עידוד, B1_LastThreeLetters: �ד, B1_LastTwoLetters: ד, S0B0Token: ריבלין_בדברי, S0B1Token: ריבלין_עידוד, S0B2Token: ריבלין_לבאי, S0Token: ריבלין, S0_LastThreeLetters: �ן, S0_LastTwoLetters: ן, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

8- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [בדברי, עידוד, לבאי ,.. ]

B0Token: בדברי, B0_LastThreeLetters: �י, B0_LastTwoLetters: י, B1Token: עידוד, B1_LastThreeLetters: �ד, B1_LastTwoLetters: ד, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [בדברי]   B= [עידוד, לבאי, האירוע ,.. ]

B0Token: עידוד, B0_LastThreeLetters: �ד, B0_LastTwoLetters: ד, B1Token: לבאי, B1_LastThreeLetters: �י, B1_LastTwoLetters: י, S0B0Token: בדברי_עידוד, S0B1Token: בדברי_לבאי, S0B2Token: בדברי_האירוע, S0Token: בדברי, S0_LastThreeLetters: �י, S0_LastTwoLetters: י, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

10- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [עידוד, לבאי, האירוע ,.. ]

B0Token: עידוד, B0_LastThreeLetters: �ד, B0_LastTwoLetters: ד, B1Token: לבאי, B1_LastThreeLetters: �י, B1_LastTwoLetters: י, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [עידוד]   B= [לבאי, האירוע, כשם ,.. ]

B0Token: לבאי, B0_LastThreeLetters: �י, B0_LastTwoLetters: י, B1Token: האירוע, B1_LastThreeLetters: �ע, B1_LastTwoLetters: ע, S0B0Token: עידוד_לבאי, S0B1Token: עידוד_האירוע, S0B2Token: עידוד_כשם, S0Token: עידוד, S0_LastThreeLetters: �ד, S0_LastTwoLetters: ד, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

12- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [לבאי, האירוע, כשם ,.. ]

B0Token: לבאי, B0_LastThreeLetters: �י, B0_LastTwoLetters: י, B1Token: האירוע, B1_LastThreeLetters: �ע, B1_LastTwoLetters: ע, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [לבאי]   B= [האירוע, כשם, שמנחם ,.. ]

B0Token: האירוע, B0_LastThreeLetters: �ע, B0_LastTwoLetters: ע, B1Token: כשם, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, S0B0Token: לבאי_האירוע, S0B1Token: לבאי_כשם, S0B2Token: לבאי_שמנחם, S0Token: לבאי, S0_LastThreeLetters: �י, S0_LastTwoLetters: י, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

14- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [האירוע, כשם, שמנחם ,.. ]

B0Token: האירוע, B0_LastThreeLetters: �ע, B0_LastTwoLetters: ע, B1Token: כשם, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [האירוע]   B= [כשם, שמנחם, בגין ,.. ]

B0Token: כשם, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, B1Token: שמנחם, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, S0B0Token: האירוע_כשם, S0B1Token: האירוע_שמנחם, S0B2Token: האירוע_בגין, S0Token: האירוע, S0_LastThreeLetters: �ע, S0_LastTwoLetters: ע, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

16- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [כשם, שמנחם, בגין ,.. ]

B0Token: כשם, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, B1Token: שמנחם, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [כשם]   B= [שמנחם, בגין, וזאב ,.. ]

B0Token: שמנחם, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, B1Token: בגין, B1_LastThreeLetters: �ן, B1_LastTwoLetters: ן, S0B0Token: כשם_שמנחם, S0B1Token: כשם_בגין, S0B2Token: כשם_וזאב, S0Token: כשם, S0_LastThreeLetters: �ם, S0_LastTwoLetters: ם, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

18- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [שמנחם, בגין, וזאב ,.. ]

B0Token: שמנחם, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, B1Token: בגין, B1_LastThreeLetters: �ן, B1_LastTwoLetters: ן, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [שמנחם]   B= [בגין, וזאב, לא ,.. ]

B0Token: בגין, B0_LastThreeLetters: �ן, B0_LastTwoLetters: ן, B1Token: וזאב, B1_LastThreeLetters: �ב, B1_LastTwoLetters: ב, S0B0Token: שמנחם_בגין, S0B1Token: שמנחם_וזאב, S0B2Token: שמנחם_לא, S0Token: שמנחם, S0_LastThreeLetters: �ם, S0_LastTwoLetters: ם, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

20- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [בגין, וזאב, לא ,.. ]

B0Token: בגין, B0_LastThreeLetters: �ן, B0_LastTwoLetters: ן, B1Token: וזאב, B1_LastThreeLetters: �ב, B1_LastTwoLetters: ב, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [בגין]   B= [וזאב, לא, כופפו ,.. ]

B0Token: וזאב, B0_LastThreeLetters: �ב, B0_LastTwoLetters: ב, B1Token: לא, B1_LastThreeLetters: �א, B1_LastTwoLetters: א, S0B0Token: בגין_וזאב, S0B1Token: בגין_לא, S0B2Token: בגין_כופפו, S0Token: בגין, S0_LastThreeLetters: �ן, S0_LastTwoLetters: ן, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

22- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [וזאב, לא, כופפו ,.. ]

B0Token: וזאב, B0_LastThreeLetters: �ב, B0_LastTwoLetters: ב, B1Token: לא, B1_LastThreeLetters: �א, B1_LastTwoLetters: א, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

23- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [וזאב]   B= [לא, כופפו, ראשם ,.. ]

B0Token: לא, B0_LastThreeLetters: �א, B0_LastTwoLetters: א, B1Token: כופפו, B1_LastThreeLetters: �ו, B1_LastTwoLetters: ו, S0B0Token: וזאב_לא, S0B1Token: וזאב_כופפו, S0B2Token: וזאב_ראשם, S0Token: וזאב, S0_LastThreeLetters: �ב, S0_LastTwoLetters: ב, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

24- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [לא, כופפו, ראשם ,.. ]

B0Token: לא, B0_LastThreeLetters: �א, B0_LastTwoLetters: א, B1Token: כופפו, B1_LastThreeLetters: �ו, B1_LastTwoLetters: ו, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

25- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [לא]   B= [כופפו, ראשם, וכך ,.. ]

B0Token: כופפו, B0_LastThreeLetters: �ו, B0_LastTwoLetters: ו, B1Token: ראשם, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, S0B0Token: לא_כופפו, S0B1Token: לא_ראשם, S0B2Token: לא_וכך, S0Token: לא, S0_LastThreeLetters: �א, S0_LastTwoLetters: א, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

26- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [כופפו, ראשם, וכך ,.. ]

B0Token: כופפו, B0_LastThreeLetters: �ו, B0_LastTwoLetters: ו, B1Token: ראשם, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

27- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [כופפו]   B= [ראשם, וכך, לימדנו ,.. ]

B0Token: ראשם, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, B1Token: וכך, B1_LastThreeLetters: �ך, B1_LastTwoLetters: ך, S0B0Token: כופפו_ראשם, S0B1Token: כופפו_וכך, S0B2Token: כופפו_לימדנו, S0Token: כופפו, S0_LastThreeLetters: �ו, S0_LastTwoLetters: ו, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

28- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [כופפו, ראשם]   B= [וכך, לימדנו, גם ,.. ]

B0Token: וכך, B0_LastThreeLetters: �ך, B0_LastTwoLetters: ך, B1Token: לימדנו, B1_LastThreeLetters: �ו, B1_LastTwoLetters: ו, S0B0Token: ראשם_וכך, S0B1Token: ראשם_לימדנו, S0B2Token: ראשם_גם, S0Token: ראשם, S0_LastThreeLetters: �ם, S0_LastTwoLetters: ם, S1B0Token: כופפו_וכך, S1S0Token: כופפו_ראשם, S1Token: כופפו, S1_LastThreeLetters: �ו, S1_LastTwoLetters: ו, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

29- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[כופפו, ראשם]]   B= [וכך, לימדנו, גם ,.. ]

B0Token: וכך, B0_LastThreeLetters: �ך, B0_LastTwoLetters: ך, B1Token: לימדנו, B1_LastThreeLetters: �ו, B1_LastTwoLetters: ו, S0B0Token: כופפו_ראשם_וכך, S0B1Token: כופפו_ראשם_לימדנו, S0B2Token: כופפו_ראשם_גם, S0Token: כופפו_ראשם, TransHistory1: 0, TransHistory2: 00, TransHistory3: 002, 

30- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [וכך, לימדנו, גם ,.. ]

B0Token: וכך, B0_LastThreeLetters: �ך, B0_LastTwoLetters: ך, B1Token: לימדנו, B1_LastThreeLetters: �ו, B1_LastTwoLetters: ו, TransHistory1: 1, TransHistory2: 10, TransHistory3: 100, 

31- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [וכך]   B= [לימדנו, גם, תלמידם ,.. ]

B0Token: לימדנו, B0_LastThreeLetters: �ו, B0_LastTwoLetters: ו, B1Token: גם, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, S0B0Token: וכך_לימדנו, S0B1Token: וכך_גם, S0B2Token: וכך_תלמידם, S0Token: וכך, S0_LastThreeLetters: �ך, S0_LastTwoLetters: ך, TransHistory1: 2, TransHistory2: 21, TransHistory3: 210, 

32- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [לימדנו, גם, תלמידם ,.. ]

B0Token: לימדנו, B0_LastThreeLetters: �ו, B0_LastTwoLetters: ו, B1Token: גם, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, TransHistory1: 0, TransHistory2: 02, TransHistory3: 021, 

33- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [לימדנו]   B= [גם, תלמידם, וחברם ,.. ]

B0Token: גם, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, B1Token: תלמידם, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, S0B0Token: לימדנו_גם, S0B1Token: לימדנו_תלמידם, S0B2Token: לימדנו_וחברם, S0Token: לימדנו, S0_LastThreeLetters: �ו, S0_LastTwoLetters: ו, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

34- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [גם, תלמידם, וחברם ,.. ]

B0Token: גם, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, B1Token: תלמידם, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

35- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [גם]   B= [תלמידם, וחברם, שמואל ,.. ]

B0Token: תלמידם, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, B1Token: וחברם, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, S0B0Token: גם_תלמידם, S0B1Token: גם_וחברם, S0B2Token: גם_שמואל, S0Token: גם, S0_LastThreeLetters: �ם, S0_LastTwoLetters: ם, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

36- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [תלמידם, וחברם, שמואל ,.. ]

B0Token: תלמידם, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, B1Token: וחברם, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

37- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [תלמידם]   B= [וחברם, שמואל, חתן ,.. ]

B0Token: וחברם, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, B1Token: שמואל, B1_LastThreeLetters: �ל, B1_LastTwoLetters: ל, S0B0Token: תלמידם_וחברם, S0B1Token: תלמידם_שמואל, S0B2Token: תלמידם_חתן, S0Token: תלמידם, S0_LastThreeLetters: �ם, S0_LastTwoLetters: ם, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

38- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [וחברם, שמואל, חתן ,.. ]

B0Token: וחברם, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, B1Token: שמואל, B1_LastThreeLetters: �ל, B1_LastTwoLetters: ל, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

39- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [וחברם]   B= [שמואל, חתן, השמחה ,.. ]

B0Token: שמואל, B0_LastThreeLetters: �ל, B0_LastTwoLetters: ל, B1Token: חתן, B1_LastThreeLetters: �ן, B1_LastTwoLetters: ן, S0B0Token: וחברם_שמואל, S0B1Token: וחברם_חתן, S0B2Token: וחברם_השמחה, S0Token: וחברם, S0_LastThreeLetters: �ם, S0_LastTwoLetters: ם, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

40- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [שמואל, חתן, השמחה ,.. ]

B0Token: שמואל, B0_LastThreeLetters: �ל, B0_LastTwoLetters: ל, B1Token: חתן, B1_LastThreeLetters: �ן, B1_LastTwoLetters: ן, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

41- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [שמואל]   B= [חתן, השמחה, גם ,.. ]

B0Token: חתן, B0_LastThreeLetters: �ן, B0_LastTwoLetters: ן, B1Token: השמחה, B1_LastThreeLetters: �ה, B1_LastTwoLetters: ה, S0B0Token: שמואל_חתן, S0B1Token: שמואל_השמחה, S0B2Token: שמואל_גם, S0Token: שמואל, S0_LastThreeLetters: �ל, S0_LastTwoLetters: ל, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

42- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [חתן, השמחה, גם ,.. ]

B0Token: חתן, B0_LastThreeLetters: �ן, B0_LastTwoLetters: ן, B1Token: השמחה, B1_LastThreeLetters: �ה, B1_LastTwoLetters: ה, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

43- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [חתן]   B= [השמחה, גם, אנו ,.. ]

B0Token: השמחה, B0_LastThreeLetters: �ה, B0_LastTwoLetters: ה, B1Token: גם, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, S0B0Token: חתן_השמחה, S0B1Token: חתן_גם, S0B2Token: חתן_אנו, S0Token: חתן, S0_LastThreeLetters: �ן, S0_LastTwoLetters: ן, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

44- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [השמחה, גם, אנו ,.. ]

B0Token: השמחה, B0_LastThreeLetters: �ה, B0_LastTwoLetters: ה, B1Token: גם, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

45- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [השמחה]   B= [גם, אנו, לא ,.. ]

B0Token: גם, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, B1Token: אנו, B1_LastThreeLetters: �ו, B1_LastTwoLetters: ו, S0B0Token: השמחה_גם, S0B1Token: השמחה_אנו, S0B2Token: השמחה_לא, S0Token: השמחה, S0_LastThreeLetters: �ה, S0_LastTwoLetters: ה, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

46- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [גם, אנו, לא ,.. ]

B0Token: גם, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, B1Token: אנו, B1_LastThreeLetters: �ו, B1_LastTwoLetters: ו, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

47- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [גם]   B= [אנו, לא, נכרע ,.. ]

B0Token: אנו, B0_LastThreeLetters: �ו, B0_LastTwoLetters: ו, B1Token: לא, B1_LastThreeLetters: �א, B1_LastTwoLetters: א, S0B0Token: גם_אנו, S0B1Token: גם_לא, S0B2Token: גם_נכרע, S0Token: גם, S0_LastThreeLetters: �ם, S0_LastTwoLetters: ם, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

48- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [אנו, לא, נכרע ,.. ]

B0Token: אנו, B0_LastThreeLetters: �ו, B0_LastTwoLetters: ו, B1Token: לא, B1_LastThreeLetters: �א, B1_LastTwoLetters: א, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

49- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [אנו]   B= [לא, נכרע, ולא ,.. ]

B0Token: לא, B0_LastThreeLetters: �א, B0_LastTwoLetters: א, B1Token: נכרע, B1_LastThreeLetters: �ע, B1_LastTwoLetters: ע, S0B0Token: אנו_לא, S0B1Token: אנו_נכרע, S0B2Token: אנו_ולא, S0Token: אנו, S0_LastThreeLetters: �ו, S0_LastTwoLetters: ו, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

50- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [לא, נכרע, ולא ,.. ]

B0Token: לא, B0_LastThreeLetters: �א, B0_LastTwoLetters: א, B1Token: נכרע, B1_LastThreeLetters: �ע, B1_LastTwoLetters: ע, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

51- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [לא]   B= [נכרע, ולא, ולא ,.. ]

B0Token: נכרע, B0_LastThreeLetters: �ע, B0_LastTwoLetters: ע, B1Token: ולא, B1_LastThreeLetters: �א, B1_LastTwoLetters: א, S0B0Token: לא_נכרע, S0B1Token: לא_ולא, S0B2Token: לא_ולא, S0Token: לא, S0_LastThreeLetters: �א, S0_LastTwoLetters: א, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

52- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [לא, נכרע]   B= [ולא, ולא, ולא ,.. ]

B0Token: ולא, B0_LastThreeLetters: �א, B0_LastTwoLetters: א, B1Token: ולא, B1_LastThreeLetters: �א, B1_LastTwoLetters: א, S0B0Token: נכרע_ולא, S0B1Token: נכרע_ולא, S0B2Token: נכרע_ולא, S0Token: נכרע, S0_LastThreeLetters: �ע, S0_LastTwoLetters: ע, S1B0Token: לא_ולא, S1S0Token: לא_נכרע, S1Token: לא, S1_LastThreeLetters: �א, S1_LastTwoLetters: א, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

53- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[לא, נכרע]]   B= [ולא, ולא, ולא ,.. ]

B0Token: ולא, B0_LastThreeLetters: �א, B0_LastTwoLetters: א, B1Token: ולא, B1_LastThreeLetters: �א, B1_LastTwoLetters: א, S0B0Token: לא_נכרע_ולא, S0B1Token: לא_נכרע_ולא, S0B2Token: לא_נכרע_ולא, S0Token: לא_נכרע, TransHistory1: 0, TransHistory2: 00, TransHistory3: 002, 

54- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ולא, ולא, ולא ,.. ]

B0Token: ולא, B0_LastThreeLetters: �א, B0_LastTwoLetters: א, B1Token: ולא, B1_LastThreeLetters: �א, B1_LastTwoLetters: א, TransHistory1: 1, TransHistory2: 10, TransHistory3: 100, 

55- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ולא]   B= [ולא, ולא, נבוש ,.. ]

B0Token: ולא, B0_LastThreeLetters: �א, B0_LastTwoLetters: א, B1Token: ולא, B1_LastThreeLetters: �א, B1_LastTwoLetters: א, S0B0Token: ולא_ולא, S0B1Token: ולא_ולא, S0B2Token: ולא_נבוש, S0Token: ולא, S0_LastThreeLetters: �א, S0_LastTwoLetters: א, TransHistory1: 2, TransHistory2: 21, TransHistory3: 210, 

56- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ולא, ולא, נבוש ,.. ]

B0Token: ולא, B0_LastThreeLetters: �א, B0_LastTwoLetters: א, B1Token: ולא, B1_LastThreeLetters: �א, B1_LastTwoLetters: א, TransHistory1: 0, TransHistory2: 02, TransHistory3: 021, 

57- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ולא]   B= [ולא, נבוש, ונאבק ,.. ]

B0Token: ולא, B0_LastThreeLetters: �א, B0_LastTwoLetters: א, B1Token: נבוש, B1_LastThreeLetters: �ש, B1_LastTwoLetters: ש, S0B0Token: ולא_ולא, S0B1Token: ולא_נבוש, S0B2Token: ולא_ונאבק, S0Token: ולא, S0_LastThreeLetters: �א, S0_LastTwoLetters: א, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

58- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ולא, נבוש, ונאבק ,.. ]

B0Token: ולא, B0_LastThreeLetters: �א, B0_LastTwoLetters: א, B1Token: נבוש, B1_LastThreeLetters: �ש, B1_LastTwoLetters: ש, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

59- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ולא]   B= [נבוש, ונאבק, עד ,.. ]

B0Token: נבוש, B0_LastThreeLetters: �ש, B0_LastTwoLetters: ש, B1Token: ונאבק, B1_LastThreeLetters: �ק, B1_LastTwoLetters: ק, S0B0Token: ולא_נבוש, S0B1Token: ולא_ונאבק, S0B2Token: ולא_עד, S0Token: ולא, S0_LastThreeLetters: �א, S0_LastTwoLetters: א, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

60- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ולא, נבוש]   B= [ונאבק, עד, שנכבוש ,.. ]

B0Token: ונאבק, B0_LastThreeLetters: �ק, B0_LastTwoLetters: ק, B1Token: עד, B1_LastThreeLetters: �ד, B1_LastTwoLetters: ד, S0B0Token: נבוש_ונאבק, S0B1Token: נבוש_עד, S0B2Token: נבוש_שנכבוש, S0Token: נבוש, S0_LastThreeLetters: �ש, S0_LastTwoLetters: ש, S1B0Token: ולא_ונאבק, S1S0Token: ולא_נבוש, S1Token: ולא, S1_LastThreeLetters: �א, S1_LastTwoLetters: א, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

61- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[ולא, נבוש]]   B= [ונאבק, עד, שנכבוש ,.. ]

B0Token: ונאבק, B0_LastThreeLetters: �ק, B0_LastTwoLetters: ק, B1Token: עד, B1_LastThreeLetters: �ד, B1_LastTwoLetters: ד, S0B0Token: ולא_נבוש_ונאבק, S0B1Token: ולא_נבוש_עד, S0B2Token: ולא_נבוש_שנכבוש, S0Token: ולא_נבוש, TransHistory1: 0, TransHistory2: 00, TransHistory3: 002, 

62- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ונאבק, עד, שנכבוש ,.. ]

B0Token: ונאבק, B0_LastThreeLetters: �ק, B0_LastTwoLetters: ק, B1Token: עד, B1_LastThreeLetters: �ד, B1_LastTwoLetters: ד, TransHistory1: 1, TransHistory2: 10, TransHistory3: 100, 

63- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ונאבק]   B= [עד, שנכבוש, את ,.. ]

B0Token: עד, B0_LastThreeLetters: �ד, B0_LastTwoLetters: ד, B1Token: שנכבוש, B1_LastThreeLetters: �ש, B1_LastTwoLetters: ש, S0B0Token: ונאבק_עד, S0B1Token: ונאבק_שנכבוש, S0B2Token: ונאבק_את, S0Token: ונאבק, S0_LastThreeLetters: �ק, S0_LastTwoLetters: ק, TransHistory1: 2, TransHistory2: 21, TransHistory3: 210, 

64- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [עד, שנכבוש, את ,.. ]

B0Token: עד, B0_LastThreeLetters: �ד, B0_LastTwoLetters: ד, B1Token: שנכבוש, B1_LastThreeLetters: �ש, B1_LastTwoLetters: ש, TransHistory1: 0, TransHistory2: 02, TransHistory3: 021, 

65- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [עד]   B= [שנכבוש, את, ההר ,.. ]

B0Token: שנכבוש, B0_LastThreeLetters: �ש, B0_LastTwoLetters: ש, B1Token: את, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, S0B0Token: עד_שנכבוש, S0B1Token: עד_את, S0B2Token: עד_ההר, S0Token: עד, S0_LastThreeLetters: �ד, S0_LastTwoLetters: ד, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

66- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [שנכבוש, את, ההר ,.. ]

B0Token: שנכבוש, B0_LastThreeLetters: �ש, B0_LastTwoLetters: ש, B1Token: את, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

67- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [שנכבוש]   B= [את, ההר ,.. ]

B0Token: את, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: ההר, B1_LastThreeLetters: �ר, B1_LastTwoLetters: ר, S0B0Token: שנכבוש_את, S0B1Token: שנכבוש_ההר, S0Token: שנכבוש, S0_LastThreeLetters: �ש, S0_LastTwoLetters: ש, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

68- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [שנכבוש, את]   B= [ההר]

B0Token: ההר, B0_LastThreeLetters: �ר, B0_LastTwoLetters: ר, S0B0Token: את_ההר, S0Token: את, S0_LastThreeLetters: �ת, S0_LastTwoLetters: ת, S1B0Token: שנכבוש_ההר, S1S0Token: שנכבוש_את, S1Token: שנכבוש, S1_LastThreeLetters: �ש, S1_LastTwoLetters: ש, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

69- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [שנכבוש, את, ההר]   B= [ ]

S0Token: ההר, S0_LastThreeLetters: �ר, S0_LastTwoLetters: ר, S1S0Token: את_ההר, S1Token: את, S1_LastThreeLetters: �ת, S1_LastTwoLetters: ת, TransHistory1: 0, TransHistory2: 00, TransHistory3: 002, 

70- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [שנכבוש, [את, ההר]]   B= [ ]

S0Token: את_ההר, S1S0Token: שנכבוש_את_ההר, S1Token: שנכבוש, S1_LastThreeLetters: �ש, S1_LastTwoLetters: ש, TransHistory1: 0, TransHistory2: 00, TransHistory3: 000, 

71- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[שנכבוש, [את, ההר]]]   B= [ ]

S0Token: שנכבוש_את_ההר, TransHistory1: 1, TransHistory2: 10, TransHistory3: 100, 

72- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

## Sentence No. 175 - 
האמת כבדה היא על כן נושאיה מעטים אך סוף האמת לנצח ויש בידינו לעשות ולהצליח ואין לנו ברירה כי אין לנו ארץ אחרת ואין לנו תנועה אחרת
### Existing MWEs: 
1- **האמת כבדה היא על כן נושאיה מעטים** (OTH)
4- **כבדה היא על כן נושאיה מעטים האמת** (OTH), Interleaving 
2- **סוף האמת לנצח** (OTH)
3- **לעשות ולהצליח** (OTH)



0- &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [האמת, כבדה, היא ,.. ]

B0Token: האמת, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: כבדה, B1_LastThreeLetters: �ה, B1_LastTwoLetters: ה, 

1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [האמת]   B= [כבדה, היא, על ,.. ]

B0Token: כבדה, B0_LastThreeLetters: �ה, B0_LastTwoLetters: ה, B1Token: היא, B1_LastThreeLetters: �א, B1_LastTwoLetters: א, S0B0Token: האמת_כבדה, S0B1Token: האמת_היא, S0B2Token: האמת_על, S0Token: האמת, S0_LastThreeLetters: �ת, S0_LastTwoLetters: ת, 

2- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [האמת, כבדה]   B= [היא, על, כן ,.. ]

B0Token: היא, B0_LastThreeLetters: �א, B0_LastTwoLetters: א, B1Token: על, B1_LastThreeLetters: �ל, B1_LastTwoLetters: ל, S0B0Token: כבדה_היא, S0B1Token: כבדה_על, S0B2Token: כבדה_כן, S0Token: כבדה, S0_LastThreeLetters: �ה, S0_LastTwoLetters: ה, S1B0Token: האמת_היא, S1S0Token: האמת_כבדה, S1Token: האמת, S1_LastThreeLetters: �ת, S1_LastTwoLetters: ת, TransHistory1: 0, 

3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [האמת, כבדה, היא]   B= [על, כן, נושאיה ,.. ]

B0Token: על, B0_LastThreeLetters: �ל, B0_LastTwoLetters: ל, B1Token: כן, B1_LastThreeLetters: �ן, B1_LastTwoLetters: ן, S0B0Token: היא_על, S0B1Token: היא_כן, S0B2Token: היא_נושאיה, S0Token: היא, S0_LastThreeLetters: �א, S0_LastTwoLetters: א, S1B0Token: כבדה_על, S1S0Token: כבדה_היא, S1Token: כבדה, S1_LastThreeLetters: �ה, S1_LastTwoLetters: ה, TransHistory1: 0, TransHistory2: 00, 

4- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [האמת, כבדה, היא, על]   B= [כן, נושאיה, מעטים ,.. ]

B0Token: כן, B0_LastThreeLetters: �ן, B0_LastTwoLetters: ן, B1Token: נושאיה, B1_LastThreeLetters: �ה, B1_LastTwoLetters: ה, S0B0Token: על_כן, S0B1Token: על_נושאיה, S0B2Token: על_מעטים, S0Token: על, S0_LastThreeLetters: �ל, S0_LastTwoLetters: ל, S1B0Token: היא_כן, S1S0Token: היא_על, S1Token: היא, S1_LastThreeLetters: �א, S1_LastTwoLetters: א, TransHistory1: 0, TransHistory2: 00, TransHistory3: 000, 

5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [האמת, כבדה, היא, על, כן]   B= [נושאיה, מעטים, אך ,.. ]

B0Token: נושאיה, B0_LastThreeLetters: �ה, B0_LastTwoLetters: ה, B1Token: מעטים, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, S0B0Token: כן_נושאיה, S0B1Token: כן_מעטים, S0B2Token: כן_אך, S0Token: כן, S0_LastThreeLetters: �ן, S0_LastTwoLetters: ן, S1B0Token: על_נושאיה, S1S0Token: על_כן, S1Token: על, S1_LastThreeLetters: �ל, S1_LastTwoLetters: ל, TransHistory1: 0, TransHistory2: 00, TransHistory3: 000, 

6- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [האמת, כבדה, היא, על, כן, נושאיה]   B= [מעטים, אך, סוף ,.. ]

B0Token: מעטים, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, B1Token: אך, B1_LastThreeLetters: �ך, B1_LastTwoLetters: ך, S0B0Token: נושאיה_מעטים, S0B1Token: נושאיה_אך, S0B2Token: נושאיה_סוף, S0Token: נושאיה, S0_LastThreeLetters: �ה, S0_LastTwoLetters: ה, S1B0Token: כן_מעטים, S1S0Token: כן_נושאיה, S1Token: כן, S1_LastThreeLetters: �ן, S1_LastTwoLetters: ן, TransHistory1: 0, TransHistory2: 00, TransHistory3: 000, 

7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [האמת, כבדה, היא, על, כן, נושאיה, מעטים]   B= [אך, סוף, האמת ,.. ]

B0Token: אך, B0_LastThreeLetters: �ך, B0_LastTwoLetters: ך, B1Token: סוף, B1_LastThreeLetters: �ף, B1_LastTwoLetters: ף, S0B0Token: מעטים_אך, S0B1Token: מעטים_סוף, S0B2Token: מעטים_האמת, S0Token: מעטים, S0_LastThreeLetters: �ם, S0_LastTwoLetters: ם, S1B0Token: נושאיה_אך, S1S0Token: נושאיה_מעטים, S1Token: נושאיה, S1_LastThreeLetters: �ה, S1_LastTwoLetters: ה, TransHistory1: 0, TransHistory2: 00, TransHistory3: 000, 

8- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [האמת, כבדה, היא, על, כן, [נושאיה, מעטים]]   B= [אך, סוף, האמת ,.. ]

B0Token: אך, B0_LastThreeLetters: �ך, B0_LastTwoLetters: ך, B1Token: סוף, B1_LastThreeLetters: �ף, B1_LastTwoLetters: ף, S0B0Token: נושאיה_מעטים_אך, S0B1Token: נושאיה_מעטים_סוף, S0B2Token: נושאיה_מעטים_האמת, S0Token: נושאיה_מעטים, S1B0Token: כן_אך, S1S0Token: כן_נושאיה_מעטים, S1Token: כן, S1_LastThreeLetters: �ן, S1_LastTwoLetters: ן, TransHistory1: 0, TransHistory2: 00, TransHistory3: 000, 

9- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [האמת, כבדה, היא, על, [כן, [נושאיה, מעטים]]]   B= [אך, סוף, האמת ,.. ]

B0Token: אך, B0_LastThreeLetters: �ך, B0_LastTwoLetters: ך, B1Token: סוף, B1_LastThreeLetters: �ף, B1_LastTwoLetters: ף, S0B0Token: כן_נושאיה_מעטים_אך, S0B1Token: כן_נושאיה_מעטים_סוף, S0B2Token: כן_נושאיה_מעטים_האמת, S0Token: כן_נושאיה_מעטים, S1B0Token: על_אך, S1S0Token: על_כן_נושאיה_מעטים, S1Token: על, S1_LastThreeLetters: �ל, S1_LastTwoLetters: ל, TransHistory1: 1, TransHistory2: 10, TransHistory3: 100, 

10- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [האמת, כבדה, היא, [על, [כן, [נושאיה, מעטים]]]]   B= [אך, סוף, האמת ,.. ]

B0Token: אך, B0_LastThreeLetters: �ך, B0_LastTwoLetters: ך, B1Token: סוף, B1_LastThreeLetters: �ף, B1_LastTwoLetters: ף, S0B0Token: על_כן_נושאיה_מעטים_אך, S0B1Token: על_כן_נושאיה_מעטים_סוף, S0B2Token: על_כן_נושאיה_מעטים_האמת, S0Token: על_כן_נושאיה_מעטים, S1B0Token: היא_אך, S1S0Token: היא_על_כן_נושאיה_מעטים, S1Token: היא, S1_LastThreeLetters: �א, S1_LastTwoLetters: א, TransHistory1: 1, TransHistory2: 11, TransHistory3: 110, 

11- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [האמת, כבדה, [היא, [על, [כן, [נושאיה, מעטים]]]]]   B= [אך, סוף, האמת ,.. ]

B0Token: אך, B0_LastThreeLetters: �ך, B0_LastTwoLetters: ך, B1Token: סוף, B1_LastThreeLetters: �ף, B1_LastTwoLetters: ף, S0B0Token: היא_על_כן_נושאיה_מעטים_אך, S0B1Token: היא_על_כן_נושאיה_מעטים_סוף, S0B2Token: היא_על_כן_נושאיה_מעטים_האמת, S0Token: היא_על_כן_נושאיה_מעטים, S1B0Token: כבדה_אך, S1S0Token: כבדה_היא_על_כן_נושאיה_מעטים, S1Token: כבדה, S1_LastThreeLetters: �ה, S1_LastTwoLetters: ה, TransHistory1: 1, TransHistory2: 11, TransHistory3: 111, 

12- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [האמת, [כבדה, [היא, [על, [כן, [נושאיה, מעטים]]]]]]   B= [אך, סוף, האמת ,.. ]

B0Token: אך, B0_LastThreeLetters: �ך, B0_LastTwoLetters: ך, B1Token: סוף, B1_LastThreeLetters: �ף, B1_LastTwoLetters: ף, S0B0Token: כבדה_היא_על_כן_נושאיה_מעטים_אך, S0B1Token: כבדה_היא_על_כן_נושאיה_מעטים_סוף, S0B2Token: כבדה_היא_על_כן_נושאיה_מעטים_האמת, S0Token: כבדה_היא_על_כן_נושאיה_מעטים, S1B0Token: האמת_אך, S1S0Token: האמת_כבדה_היא_על_כן_נושאיה_מעטים, S1Token: האמת, S1_LastThreeLetters: �ת, S1_LastTwoLetters: ת, TransHistory1: 1, TransHistory2: 11, TransHistory3: 111, 

13- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[האמת, [כבדה, [היא, [על, [כן, [נושאיה, מעטים]]]]]]]   B= [אך, סוף, האמת ,.. ]

B0Token: אך, B0_LastThreeLetters: �ך, B0_LastTwoLetters: ך, B1Token: סוף, B1_LastThreeLetters: �ף, B1_LastTwoLetters: ף, S0B0Token: האמת_כבדה_היא_על_כן_נושאיה_מעטים_אך, S0B1Token: האמת_כבדה_היא_על_כן_נושאיה_מעטים_סוף, S0B2Token: האמת_כבדה_היא_על_כן_נושאיה_מעטים_האמת, S0Token: האמת_כבדה_היא_על_כן_נושאיה_מעטים, TransHistory1: 1, TransHistory2: 11, TransHistory3: 111, 

14- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [אך, סוף, האמת ,.. ]

B0Token: אך, B0_LastThreeLetters: �ך, B0_LastTwoLetters: ך, B1Token: סוף, B1_LastThreeLetters: �ף, B1_LastTwoLetters: ף, TransHistory1: 1, TransHistory2: 11, TransHistory3: 111, 

15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [אך]   B= [סוף, האמת, לנצח ,.. ]

B0Token: סוף, B0_LastThreeLetters: �ף, B0_LastTwoLetters: ף, B1Token: האמת, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, S0B0Token: אך_סוף, S0B1Token: אך_האמת, S0B2Token: אך_לנצח, S0Token: אך, S0_LastThreeLetters: �ך, S0_LastTwoLetters: ך, TransHistory1: 2, TransHistory2: 21, TransHistory3: 211, 

16- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [סוף, האמת, לנצח ,.. ]

B0Token: סוף, B0_LastThreeLetters: �ף, B0_LastTwoLetters: ף, B1Token: האמת, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, TransHistory1: 0, TransHistory2: 02, TransHistory3: 021, 

17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [סוף]   B= [האמת, לנצח, ויש ,.. ]

B0Token: האמת, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: לנצח, B1_LastThreeLetters: �ח, B1_LastTwoLetters: ח, S0B0Token: סוף_האמת, S0B1Token: סוף_לנצח, S0B2Token: סוף_ויש, S0Token: סוף, S0_LastThreeLetters: �ף, S0_LastTwoLetters: ף, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

18- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [סוף, האמת]   B= [לנצח, ויש, בידינו ,.. ]

B0Token: לנצח, B0_LastThreeLetters: �ח, B0_LastTwoLetters: ח, B1Token: ויש, B1_LastThreeLetters: �ש, B1_LastTwoLetters: ש, S0B0Token: האמת_לנצח, S0B1Token: האמת_ויש, S0B2Token: האמת_בידינו, S0Token: האמת, S0_LastThreeLetters: �ת, S0_LastTwoLetters: ת, S1B0Token: סוף_לנצח, S1S0Token: סוף_האמת, S1Token: סוף, S1_LastThreeLetters: �ף, S1_LastTwoLetters: ף, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [סוף, האמת, לנצח]   B= [ויש, בידינו, לעשות ,.. ]

B0Token: ויש, B0_LastThreeLetters: �ש, B0_LastTwoLetters: ש, B1Token: בידינו, B1_LastThreeLetters: �ו, B1_LastTwoLetters: ו, S0B0Token: לנצח_ויש, S0B1Token: לנצח_בידינו, S0B2Token: לנצח_לעשות, S0Token: לנצח, S0_LastThreeLetters: �ח, S0_LastTwoLetters: ח, S1B0Token: האמת_ויש, S1S0Token: האמת_לנצח, S1Token: האמת, S1_LastThreeLetters: �ת, S1_LastTwoLetters: ת, TransHistory1: 0, TransHistory2: 00, TransHistory3: 002, 

20- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [סוף, [האמת, לנצח]]   B= [ויש, בידינו, לעשות ,.. ]

B0Token: ויש, B0_LastThreeLetters: �ש, B0_LastTwoLetters: ש, B1Token: בידינו, B1_LastThreeLetters: �ו, B1_LastTwoLetters: ו, S0B0Token: האמת_לנצח_ויש, S0B1Token: האמת_לנצח_בידינו, S0B2Token: האמת_לנצח_לעשות, S0Token: האמת_לנצח, S1B0Token: סוף_ויש, S1S0Token: סוף_האמת_לנצח, S1Token: סוף, S1_LastThreeLetters: �ף, S1_LastTwoLetters: ף, TransHistory1: 0, TransHistory2: 00, TransHistory3: 000, 

21- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[סוף, [האמת, לנצח]]]   B= [ויש, בידינו, לעשות ,.. ]

B0Token: ויש, B0_LastThreeLetters: �ש, B0_LastTwoLetters: ש, B1Token: בידינו, B1_LastThreeLetters: �ו, B1_LastTwoLetters: ו, S0B0Token: סוף_האמת_לנצח_ויש, S0B1Token: סוף_האמת_לנצח_בידינו, S0B2Token: סוף_האמת_לנצח_לעשות, S0Token: סוף_האמת_לנצח, TransHistory1: 1, TransHistory2: 10, TransHistory3: 100, 

22- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ויש, בידינו, לעשות ,.. ]

B0Token: ויש, B0_LastThreeLetters: �ש, B0_LastTwoLetters: ש, B1Token: בידינו, B1_LastThreeLetters: �ו, B1_LastTwoLetters: ו, TransHistory1: 1, TransHistory2: 11, TransHistory3: 110, 

23- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ויש]   B= [בידינו, לעשות, ולהצליח ,.. ]

B0Token: בידינו, B0_LastThreeLetters: �ו, B0_LastTwoLetters: ו, B1Token: לעשות, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, S0B0Token: ויש_בידינו, S0B1Token: ויש_לעשות, S0B2Token: ויש_ולהצליח, S0Token: ויש, S0_LastThreeLetters: �ש, S0_LastTwoLetters: ש, TransHistory1: 2, TransHistory2: 21, TransHistory3: 211, 

24- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [בידינו, לעשות, ולהצליח ,.. ]

B0Token: בידינו, B0_LastThreeLetters: �ו, B0_LastTwoLetters: ו, B1Token: לעשות, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, TransHistory1: 0, TransHistory2: 02, TransHistory3: 021, 

25- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [בידינו]   B= [לעשות, ולהצליח, ואין ,.. ]

B0Token: לעשות, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: ולהצליח, B1_LastThreeLetters: �ח, B1_LastTwoLetters: ח, S0B0Token: בידינו_לעשות, S0B1Token: בידינו_ולהצליח, S0B2Token: בידינו_ואין, S0Token: בידינו, S0_LastThreeLetters: �ו, S0_LastTwoLetters: ו, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

26- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [לעשות, ולהצליח, ואין ,.. ]

B0Token: לעשות, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: ולהצליח, B1_LastThreeLetters: �ח, B1_LastTwoLetters: ח, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

27- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [לעשות]   B= [ולהצליח, ואין, לנו ,.. ]

B0Token: ולהצליח, B0_LastThreeLetters: �ח, B0_LastTwoLetters: ח, B1Token: ואין, B1_LastThreeLetters: �ן, B1_LastTwoLetters: ן, S0B0Token: לעשות_ולהצליח, S0B1Token: לעשות_ואין, S0B2Token: לעשות_לנו, S0Token: לעשות, S0_LastThreeLetters: �ת, S0_LastTwoLetters: ת, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

28- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [לעשות, ולהצליח]   B= [ואין, לנו, ברירה ,.. ]

B0Token: ואין, B0_LastThreeLetters: �ן, B0_LastTwoLetters: ן, B1Token: לנו, B1_LastThreeLetters: �ו, B1_LastTwoLetters: ו, S0B0Token: ולהצליח_ואין, S0B1Token: ולהצליח_לנו, S0B2Token: ולהצליח_ברירה, S0Token: ולהצליח, S0_LastThreeLetters: �ח, S0_LastTwoLetters: ח, S1B0Token: לעשות_ואין, S1S0Token: לעשות_ולהצליח, S1Token: לעשות, S1_LastThreeLetters: �ת, S1_LastTwoLetters: ת, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

29- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[לעשות, ולהצליח]]   B= [ואין, לנו, ברירה ,.. ]

B0Token: ואין, B0_LastThreeLetters: �ן, B0_LastTwoLetters: ן, B1Token: לנו, B1_LastThreeLetters: �ו, B1_LastTwoLetters: ו, S0B0Token: לעשות_ולהצליח_ואין, S0B1Token: לעשות_ולהצליח_לנו, S0B2Token: לעשות_ולהצליח_ברירה, S0Token: לעשות_ולהצליח, TransHistory1: 0, TransHistory2: 00, TransHistory3: 002, 

30- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ואין, לנו, ברירה ,.. ]

B0Token: ואין, B0_LastThreeLetters: �ן, B0_LastTwoLetters: ן, B1Token: לנו, B1_LastThreeLetters: �ו, B1_LastTwoLetters: ו, TransHistory1: 1, TransHistory2: 10, TransHistory3: 100, 

31- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ואין]   B= [לנו, ברירה, כי ,.. ]

B0Token: לנו, B0_LastThreeLetters: �ו, B0_LastTwoLetters: ו, B1Token: ברירה, B1_LastThreeLetters: �ה, B1_LastTwoLetters: ה, S0B0Token: ואין_לנו, S0B1Token: ואין_ברירה, S0B2Token: ואין_כי, S0Token: ואין, S0_LastThreeLetters: �ן, S0_LastTwoLetters: ן, TransHistory1: 2, TransHistory2: 21, TransHistory3: 210, 

32- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [לנו, ברירה, כי ,.. ]

B0Token: לנו, B0_LastThreeLetters: �ו, B0_LastTwoLetters: ו, B1Token: ברירה, B1_LastThreeLetters: �ה, B1_LastTwoLetters: ה, TransHistory1: 0, TransHistory2: 02, TransHistory3: 021, 

33- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [לנו]   B= [ברירה, כי, אין ,.. ]

B0Token: ברירה, B0_LastThreeLetters: �ה, B0_LastTwoLetters: ה, B1Token: כי, B1_LastThreeLetters: �י, B1_LastTwoLetters: י, S0B0Token: לנו_ברירה, S0B1Token: לנו_כי, S0B2Token: לנו_אין, S0Token: לנו, S0_LastThreeLetters: �ו, S0_LastTwoLetters: ו, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

34- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ברירה, כי, אין ,.. ]

B0Token: ברירה, B0_LastThreeLetters: �ה, B0_LastTwoLetters: ה, B1Token: כי, B1_LastThreeLetters: �י, B1_LastTwoLetters: י, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

35- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ברירה]   B= [כי, אין, לנו ,.. ]

B0Token: כי, B0_LastThreeLetters: �י, B0_LastTwoLetters: י, B1Token: אין, B1_LastThreeLetters: �ן, B1_LastTwoLetters: ן, S0B0Token: ברירה_כי, S0B1Token: ברירה_אין, S0B2Token: ברירה_לנו, S0Token: ברירה, S0_LastThreeLetters: �ה, S0_LastTwoLetters: ה, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

36- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [כי, אין, לנו ,.. ]

B0Token: כי, B0_LastThreeLetters: �י, B0_LastTwoLetters: י, B1Token: אין, B1_LastThreeLetters: �ן, B1_LastTwoLetters: ן, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

37- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [כי]   B= [אין, לנו, ארץ ,.. ]

B0Token: אין, B0_LastThreeLetters: �ן, B0_LastTwoLetters: ן, B1Token: לנו, B1_LastThreeLetters: �ו, B1_LastTwoLetters: ו, S0B0Token: כי_אין, S0B1Token: כי_לנו, S0B2Token: כי_ארץ, S0Token: כי, S0_LastThreeLetters: �י, S0_LastTwoLetters: י, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

38- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [אין, לנו, ארץ ,.. ]

B0Token: אין, B0_LastThreeLetters: �ן, B0_LastTwoLetters: ן, B1Token: לנו, B1_LastThreeLetters: �ו, B1_LastTwoLetters: ו, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

39- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [אין]   B= [לנו, ארץ, אחרת ,.. ]

B0Token: לנו, B0_LastThreeLetters: �ו, B0_LastTwoLetters: ו, B1Token: ארץ, B1_LastThreeLetters: �ץ, B1_LastTwoLetters: ץ, S0B0Token: אין_לנו, S0B1Token: אין_ארץ, S0B2Token: אין_אחרת, S0Token: אין, S0_LastThreeLetters: �ן, S0_LastTwoLetters: ן, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

40- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [לנו, ארץ, אחרת ,.. ]

B0Token: לנו, B0_LastThreeLetters: �ו, B0_LastTwoLetters: ו, B1Token: ארץ, B1_LastThreeLetters: �ץ, B1_LastTwoLetters: ץ, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

41- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [לנו]   B= [ארץ, אחרת, ואין ,.. ]

B0Token: ארץ, B0_LastThreeLetters: �ץ, B0_LastTwoLetters: ץ, B1Token: אחרת, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, S0B0Token: לנו_ארץ, S0B1Token: לנו_אחרת, S0B2Token: לנו_ואין, S0Token: לנו, S0_LastThreeLetters: �ו, S0_LastTwoLetters: ו, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

42- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ארץ, אחרת, ואין ,.. ]

B0Token: ארץ, B0_LastThreeLetters: �ץ, B0_LastTwoLetters: ץ, B1Token: אחרת, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

43- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ארץ]   B= [אחרת, ואין, לנו ,.. ]

B0Token: אחרת, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: ואין, B1_LastThreeLetters: �ן, B1_LastTwoLetters: ן, S0B0Token: ארץ_אחרת, S0B1Token: ארץ_ואין, S0B2Token: ארץ_לנו, S0Token: ארץ, S0_LastThreeLetters: �ץ, S0_LastTwoLetters: ץ, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

44- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [אחרת, ואין, לנו ,.. ]

B0Token: אחרת, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: ואין, B1_LastThreeLetters: �ן, B1_LastTwoLetters: ן, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

45- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [אחרת]   B= [ואין, לנו, תנועה ,.. ]

B0Token: ואין, B0_LastThreeLetters: �ן, B0_LastTwoLetters: ן, B1Token: לנו, B1_LastThreeLetters: �ו, B1_LastTwoLetters: ו, S0B0Token: אחרת_ואין, S0B1Token: אחרת_לנו, S0B2Token: אחרת_תנועה, S0Token: אחרת, S0_LastThreeLetters: �ת, S0_LastTwoLetters: ת, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

46- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ואין, לנו, תנועה ,.. ]

B0Token: ואין, B0_LastThreeLetters: �ן, B0_LastTwoLetters: ן, B1Token: לנו, B1_LastThreeLetters: �ו, B1_LastTwoLetters: ו, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

47- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ואין]   B= [לנו, תנועה, אחרת ,.. ]

B0Token: לנו, B0_LastThreeLetters: �ו, B0_LastTwoLetters: ו, B1Token: תנועה, B1_LastThreeLetters: �ה, B1_LastTwoLetters: ה, S0B0Token: ואין_לנו, S0B1Token: ואין_תנועה, S0B2Token: ואין_אחרת, S0Token: ואין, S0_LastThreeLetters: �ן, S0_LastTwoLetters: ן, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

48- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [לנו, תנועה, אחרת ,.. ]

B0Token: לנו, B0_LastThreeLetters: �ו, B0_LastTwoLetters: ו, B1Token: תנועה, B1_LastThreeLetters: �ה, B1_LastTwoLetters: ה, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

49- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [לנו]   B= [תנועה, אחרת ,.. ]

B0Token: תנועה, B0_LastThreeLetters: �ה, B0_LastTwoLetters: ה, B1Token: אחרת, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, S0B0Token: לנו_תנועה, S0B1Token: לנו_אחרת, S0Token: לנו, S0_LastThreeLetters: �ו, S0_LastTwoLetters: ו, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

50- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [תנועה, אחרת ,.. ]

B0Token: תנועה, B0_LastThreeLetters: �ה, B0_LastTwoLetters: ה, B1Token: אחרת, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

51- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [תנועה]   B= [אחרת]

B0Token: אחרת, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, S0B0Token: תנועה_אחרת, S0Token: תנועה, S0_LastThreeLetters: �ה, S0_LastTwoLetters: ה, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

52- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [אחרת]

B0Token: אחרת, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

53- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [אחרת]   B= [ ]

S0Token: אחרת, S0_LastThreeLetters: �ת, S0_LastTwoLetters: ת, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

54- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

## Sentence No. 4059 - 
מול כוחות רשע אטומים מול אנשים חסרי ערכים ציוניים מול דיקטטור מטורף הגורר את המדינה למלחמת אזרחים אנו נציב מחדש את סולם הערכים הציוני התיישבותי שהקים את מדינת ישראל ביתו הלאומי של העם היהודי אומרים מארגני האירוע
### Existing MWEs: 
1- **הגורר את המדינה** (VPC)
2- **נציב מחדש את סולם הערכים** (OTH)
3- **נציב מחדש סולם הערכים** (OTH), Embedded
4- **נציב מחדש סולם הערכים את** (OTH), Interleaving 



0- &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [מול, כוחות, רשע ,.. ]

B0Token: מול, B0_LastThreeLetters: �ל, B0_LastTwoLetters: ל, B1Token: כוחות, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, 

1- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [מול]   B= [כוחות, רשע, אטומים ,.. ]

B0Token: כוחות, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: רשע, B1_LastThreeLetters: �ע, B1_LastTwoLetters: ע, S0B0Token: מול_כוחות, S0B1Token: מול_רשע, S0B2Token: מול_אטומים, S0Token: מול, S0_LastThreeLetters: �ל, S0_LastTwoLetters: ל, 

2- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [כוחות, רשע, אטומים ,.. ]

B0Token: כוחות, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: רשע, B1_LastThreeLetters: �ע, B1_LastTwoLetters: ע, TransHistory1: 0, 

3- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [כוחות]   B= [רשע, אטומים, מול ,.. ]

B0Token: רשע, B0_LastThreeLetters: �ע, B0_LastTwoLetters: ע, B1Token: אטומים, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, S0B0Token: כוחות_רשע, S0B1Token: כוחות_אטומים, S0B2Token: כוחות_מול, S0Token: כוחות, S0_LastThreeLetters: �ת, S0_LastTwoLetters: ת, TransHistory1: 2, TransHistory2: 20, 

4- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [רשע, אטומים, מול ,.. ]

B0Token: רשע, B0_LastThreeLetters: �ע, B0_LastTwoLetters: ע, B1Token: אטומים, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

5- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [רשע]   B= [אטומים, מול, אנשים ,.. ]

B0Token: אטומים, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, B1Token: מול, B1_LastThreeLetters: �ל, B1_LastTwoLetters: ל, S0B0Token: רשע_אטומים, S0B1Token: רשע_מול, S0B2Token: רשע_אנשים, S0Token: רשע, S0_LastThreeLetters: �ע, S0_LastTwoLetters: ע, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

6- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [אטומים, מול, אנשים ,.. ]

B0Token: אטומים, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, B1Token: מול, B1_LastThreeLetters: �ל, B1_LastTwoLetters: ל, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

7- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [אטומים]   B= [מול, אנשים, חסרי ,.. ]

B0Token: מול, B0_LastThreeLetters: �ל, B0_LastTwoLetters: ל, B1Token: אנשים, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, S0B0Token: אטומים_מול, S0B1Token: אטומים_אנשים, S0B2Token: אטומים_חסרי, S0Token: אטומים, S0_LastThreeLetters: �ם, S0_LastTwoLetters: ם, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

8- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [מול, אנשים, חסרי ,.. ]

B0Token: מול, B0_LastThreeLetters: �ל, B0_LastTwoLetters: ל, B1Token: אנשים, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

9- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [מול]   B= [אנשים, חסרי, ערכים ,.. ]

B0Token: אנשים, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, B1Token: חסרי, B1_LastThreeLetters: �י, B1_LastTwoLetters: י, S0B0Token: מול_אנשים, S0B1Token: מול_חסרי, S0B2Token: מול_ערכים, S0Token: מול, S0_LastThreeLetters: �ל, S0_LastTwoLetters: ל, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

10- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [אנשים, חסרי, ערכים ,.. ]

B0Token: אנשים, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, B1Token: חסרי, B1_LastThreeLetters: �י, B1_LastTwoLetters: י, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

11- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [אנשים]   B= [חסרי, ערכים, ציוניים ,.. ]

B0Token: חסרי, B0_LastThreeLetters: �י, B0_LastTwoLetters: י, B1Token: ערכים, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, S0B0Token: אנשים_חסרי, S0B1Token: אנשים_ערכים, S0B2Token: אנשים_ציוניים, S0Token: אנשים, S0_LastThreeLetters: �ם, S0_LastTwoLetters: ם, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

12- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [חסרי, ערכים, ציוניים ,.. ]

B0Token: חסרי, B0_LastThreeLetters: �י, B0_LastTwoLetters: י, B1Token: ערכים, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

13- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [חסרי]   B= [ערכים, ציוניים, מול ,.. ]

B0Token: ערכים, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, B1Token: ציוניים, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, S0B0Token: חסרי_ערכים, S0B1Token: חסרי_ציוניים, S0B2Token: חסרי_מול, S0Token: חסרי, S0_LastThreeLetters: �י, S0_LastTwoLetters: י, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

14- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ערכים, ציוניים, מול ,.. ]

B0Token: ערכים, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, B1Token: ציוניים, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

15- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ערכים]   B= [ציוניים, מול, דיקטטור ,.. ]

B0Token: ציוניים, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, B1Token: מול, B1_LastThreeLetters: �ל, B1_LastTwoLetters: ל, S0B0Token: ערכים_ציוניים, S0B1Token: ערכים_מול, S0B2Token: ערכים_דיקטטור, S0Token: ערכים, S0_LastThreeLetters: �ם, S0_LastTwoLetters: ם, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

16- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ציוניים, מול, דיקטטור ,.. ]

B0Token: ציוניים, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, B1Token: מול, B1_LastThreeLetters: �ל, B1_LastTwoLetters: ל, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

17- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ציוניים]   B= [מול, דיקטטור, מטורף ,.. ]

B0Token: מול, B0_LastThreeLetters: �ל, B0_LastTwoLetters: ל, B1Token: דיקטטור, B1_LastThreeLetters: �ר, B1_LastTwoLetters: ר, S0B0Token: ציוניים_מול, S0B1Token: ציוניים_דיקטטור, S0B2Token: ציוניים_מטורף, S0Token: ציוניים, S0_LastThreeLetters: �ם, S0_LastTwoLetters: ם, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

18- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [מול, דיקטטור, מטורף ,.. ]

B0Token: מול, B0_LastThreeLetters: �ל, B0_LastTwoLetters: ל, B1Token: דיקטטור, B1_LastThreeLetters: �ר, B1_LastTwoLetters: ר, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

19- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [מול]   B= [דיקטטור, מטורף, הגורר ,.. ]

B0Token: דיקטטור, B0_LastThreeLetters: �ר, B0_LastTwoLetters: ר, B1Token: מטורף, B1_LastThreeLetters: �ף, B1_LastTwoLetters: ף, S0B0Token: מול_דיקטטור, S0B1Token: מול_מטורף, S0B2Token: מול_הגורר, S0Token: מול, S0_LastThreeLetters: �ל, S0_LastTwoLetters: ל, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

20- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [דיקטטור, מטורף, הגורר ,.. ]

B0Token: דיקטטור, B0_LastThreeLetters: �ר, B0_LastTwoLetters: ר, B1Token: מטורף, B1_LastThreeLetters: �ף, B1_LastTwoLetters: ף, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

21- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [דיקטטור]   B= [מטורף, הגורר, את ,.. ]

B0Token: מטורף, B0_LastThreeLetters: �ף, B0_LastTwoLetters: ף, B1Token: הגורר, B1_LastThreeLetters: �ר, B1_LastTwoLetters: ר, S0B0Token: דיקטטור_מטורף, S0B1Token: דיקטטור_הגורר, S0B2Token: דיקטטור_את, S0Token: דיקטטור, S0_LastThreeLetters: �ר, S0_LastTwoLetters: ר, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

22- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [מטורף, הגורר, את ,.. ]

B0Token: מטורף, B0_LastThreeLetters: �ף, B0_LastTwoLetters: ף, B1Token: הגורר, B1_LastThreeLetters: �ר, B1_LastTwoLetters: ר, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

23- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [מטורף]   B= [הגורר, את, המדינה ,.. ]

B0Token: הגורר, B0_LastThreeLetters: �ר, B0_LastTwoLetters: ר, B1Token: את, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, S0B0Token: מטורף_הגורר, S0B1Token: מטורף_את, S0B2Token: מטורף_המדינה, S0Token: מטורף, S0_LastThreeLetters: �ף, S0_LastTwoLetters: ף, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

24- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [הגורר, את, המדינה ,.. ]

B0Token: הגורר, B0_LastThreeLetters: �ר, B0_LastTwoLetters: ר, B1Token: את, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

25- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [הגורר]   B= [את, המדינה, למלחמת ,.. ]

B0Token: את, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: המדינה, B1_LastThreeLetters: �ה, B1_LastTwoLetters: ה, S0B0Token: הגורר_את, S0B1Token: הגורר_המדינה, S0B2Token: הגורר_למלחמת, S0Token: הגורר, S0_LastThreeLetters: �ר, S0_LastTwoLetters: ר, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

26- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [הגורר, את]   B= [המדינה, למלחמת, אזרחים ,.. ]

B0Token: המדינה, B0_LastThreeLetters: �ה, B0_LastTwoLetters: ה, B1Token: למלחמת, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, S0B0Token: את_המדינה, S0B1Token: את_למלחמת, S0B2Token: את_אזרחים, S0Token: את, S0_LastThreeLetters: �ת, S0_LastTwoLetters: ת, S1B0Token: הגורר_המדינה, S1S0Token: הגורר_את, S1Token: הגורר, S1_LastThreeLetters: �ר, S1_LastTwoLetters: ר, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

27- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [הגורר, את, המדינה]   B= [למלחמת, אזרחים, אנו ,.. ]

B0Token: למלחמת, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: אזרחים, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, S0B0Token: המדינה_למלחמת, S0B1Token: המדינה_אזרחים, S0B2Token: המדינה_אנו, S0Token: המדינה, S0_LastThreeLetters: �ה, S0_LastTwoLetters: ה, S1B0Token: את_למלחמת, S1S0Token: את_המדינה, S1Token: את, S1_LastThreeLetters: �ת, S1_LastTwoLetters: ת, TransHistory1: 0, TransHistory2: 00, TransHistory3: 002, 

28- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [הגורר, [את, המדינה]]   B= [למלחמת, אזרחים, אנו ,.. ]

B0Token: למלחמת, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: אזרחים, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, S0B0Token: את_המדינה_למלחמת, S0B1Token: את_המדינה_אזרחים, S0B2Token: את_המדינה_אנו, S0Token: את_המדינה, S1B0Token: הגורר_למלחמת, S1S0Token: הגורר_את_המדינה, S1Token: הגורר, S1_LastThreeLetters: �ר, S1_LastTwoLetters: ר, TransHistory1: 0, TransHistory2: 00, TransHistory3: 000, 

29- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[הגורר, [את, המדינה]]]   B= [למלחמת, אזרחים, אנו ,.. ]

B0Token: למלחמת, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: אזרחים, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, S0B0Token: הגורר_את_המדינה_למלחמת, S0B1Token: הגורר_את_המדינה_אזרחים, S0B2Token: הגורר_את_המדינה_אנו, S0Token: הגורר_את_המדינה, TransHistory1: 1, TransHistory2: 10, TransHistory3: 100, 

30- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [למלחמת, אזרחים, אנו ,.. ]

B0Token: למלחמת, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: אזרחים, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, TransHistory1: 1, TransHistory2: 11, TransHistory3: 110, 

31- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [למלחמת]   B= [אזרחים, אנו, נציב ,.. ]

B0Token: אזרחים, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, B1Token: אנו, B1_LastThreeLetters: �ו, B1_LastTwoLetters: ו, S0B0Token: למלחמת_אזרחים, S0B1Token: למלחמת_אנו, S0B2Token: למלחמת_נציב, S0Token: למלחמת, S0_LastThreeLetters: �ת, S0_LastTwoLetters: ת, TransHistory1: 2, TransHistory2: 21, TransHistory3: 211, 

32- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [אזרחים, אנו, נציב ,.. ]

B0Token: אזרחים, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, B1Token: אנו, B1_LastThreeLetters: �ו, B1_LastTwoLetters: ו, TransHistory1: 0, TransHistory2: 02, TransHistory3: 021, 

33- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [אזרחים]   B= [אנו, נציב, מחדש ,.. ]

B0Token: אנו, B0_LastThreeLetters: �ו, B0_LastTwoLetters: ו, B1Token: נציב, B1_LastThreeLetters: �ב, B1_LastTwoLetters: ב, S0B0Token: אזרחים_אנו, S0B1Token: אזרחים_נציב, S0B2Token: אזרחים_מחדש, S0Token: אזרחים, S0_LastThreeLetters: �ם, S0_LastTwoLetters: ם, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

34- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [אנו, נציב, מחדש ,.. ]

B0Token: אנו, B0_LastThreeLetters: �ו, B0_LastTwoLetters: ו, B1Token: נציב, B1_LastThreeLetters: �ב, B1_LastTwoLetters: ב, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

35- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [אנו]   B= [נציב, מחדש, את ,.. ]

B0Token: נציב, B0_LastThreeLetters: �ב, B0_LastTwoLetters: ב, B1Token: מחדש, B1_LastThreeLetters: �ש, B1_LastTwoLetters: ש, S0B0Token: אנו_נציב, S0B1Token: אנו_מחדש, S0B2Token: אנו_את, S0Token: אנו, S0_LastThreeLetters: �ו, S0_LastTwoLetters: ו, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

36- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [נציב, מחדש, את ,.. ]

B0Token: נציב, B0_LastThreeLetters: �ב, B0_LastTwoLetters: ב, B1Token: מחדש, B1_LastThreeLetters: �ש, B1_LastTwoLetters: ש, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

37- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [נציב]   B= [מחדש, את, סולם ,.. ]

B0Token: מחדש, B0_LastThreeLetters: �ש, B0_LastTwoLetters: ש, B1Token: את, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, S0B0Token: נציב_מחדש, S0B1Token: נציב_את, S0B2Token: נציב_סולם, S0Token: נציב, S0_LastThreeLetters: �ב, S0_LastTwoLetters: ב, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

38- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [נציב, מחדש]   B= [את, סולם, הערכים ,.. ]

B0Token: את, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: סולם, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, S0B0Token: מחדש_את, S0B1Token: מחדש_סולם, S0B2Token: מחדש_הערכים, S0Token: מחדש, S0_LastThreeLetters: �ש, S0_LastTwoLetters: ש, S1B0Token: נציב_את, S1S0Token: נציב_מחדש, S1Token: נציב, S1_LastThreeLetters: �ב, S1_LastTwoLetters: ב, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

39- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [נציב, מחדש, את]   B= [סולם, הערכים, הציוני ,.. ]

B0Token: סולם, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, B1Token: הערכים, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, S0B0Token: את_סולם, S0B1Token: את_הערכים, S0B2Token: את_הציוני, S0Token: את, S0_LastThreeLetters: �ת, S0_LastTwoLetters: ת, S1B0Token: מחדש_סולם, S1S0Token: מחדש_את, S1Token: מחדש, S1_LastThreeLetters: �ש, S1_LastTwoLetters: ש, TransHistory1: 0, TransHistory2: 00, TransHistory3: 002, 

40- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [נציב, מחדש, את, סולם]   B= [הערכים, הציוני, התיישבותי ,.. ]

B0Token: הערכים, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, B1Token: הציוני, B1_LastThreeLetters: �י, B1_LastTwoLetters: י, S0B0Token: סולם_הערכים, S0B1Token: סולם_הציוני, S0B2Token: סולם_התיישבותי, S0Token: סולם, S0_LastThreeLetters: �ם, S0_LastTwoLetters: ם, S1B0Token: את_הערכים, S1S0Token: את_סולם, S1Token: את, S1_LastThreeLetters: �ת, S1_LastTwoLetters: ת, TransHistory1: 0, TransHistory2: 00, TransHistory3: 000, 

41- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [נציב, מחדש, את, סולם, הערכים]   B= [הציוני, התיישבותי, שהקים ,.. ]

B0Token: הציוני, B0_LastThreeLetters: �י, B0_LastTwoLetters: י, B1Token: התיישבותי, B1_LastThreeLetters: �י, B1_LastTwoLetters: י, S0B0Token: הערכים_הציוני, S0B1Token: הערכים_התיישבותי, S0B2Token: הערכים_שהקים, S0Token: הערכים, S0_LastThreeLetters: �ם, S0_LastTwoLetters: ם, S1B0Token: סולם_הציוני, S1S0Token: סולם_הערכים, S1Token: סולם, S1_LastThreeLetters: �ם, S1_LastTwoLetters: ם, TransHistory1: 0, TransHistory2: 00, TransHistory3: 000, 

42- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [נציב, מחדש, את, [סולם, הערכים]]   B= [הציוני, התיישבותי, שהקים ,.. ]

B0Token: הציוני, B0_LastThreeLetters: �י, B0_LastTwoLetters: י, B1Token: התיישבותי, B1_LastThreeLetters: �י, B1_LastTwoLetters: י, S0B0Token: סולם_הערכים_הציוני, S0B1Token: סולם_הערכים_התיישבותי, S0B2Token: סולם_הערכים_שהקים, S0Token: סולם_הערכים, S1B0Token: את_הציוני, S1S0Token: את_סולם_הערכים, S1Token: את, S1_LastThreeLetters: �ת, S1_LastTwoLetters: ת, TransHistory1: 0, TransHistory2: 00, TransHistory3: 000, 

43- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [נציב, מחדש, [את, [סולם, הערכים]]]   B= [הציוני, התיישבותי, שהקים ,.. ]

B0Token: הציוני, B0_LastThreeLetters: �י, B0_LastTwoLetters: י, B1Token: התיישבותי, B1_LastThreeLetters: �י, B1_LastTwoLetters: י, S0B0Token: את_סולם_הערכים_הציוני, S0B1Token: את_סולם_הערכים_התיישבותי, S0B2Token: את_סולם_הערכים_שהקים, S0Token: את_סולם_הערכים, S1B0Token: מחדש_הציוני, S1S0Token: מחדש_את_סולם_הערכים, S1Token: מחדש, S1_LastThreeLetters: �ש, S1_LastTwoLetters: ש, TransHistory1: 1, TransHistory2: 10, TransHistory3: 100, 

44- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [נציב, [מחדש, [את, [סולם, הערכים]]]]   B= [הציוני, התיישבותי, שהקים ,.. ]

B0Token: הציוני, B0_LastThreeLetters: �י, B0_LastTwoLetters: י, B1Token: התיישבותי, B1_LastThreeLetters: �י, B1_LastTwoLetters: י, S0B0Token: מחדש_את_סולם_הערכים_הציוני, S0B1Token: מחדש_את_סולם_הערכים_התיישבותי, S0B2Token: מחדש_את_סולם_הערכים_שהקים, S0Token: מחדש_את_סולם_הערכים, S1B0Token: נציב_הציוני, S1S0Token: נציב_מחדש_את_סולם_הערכים, S1Token: נציב, S1_LastThreeLetters: �ב, S1_LastTwoLetters: ב, TransHistory1: 1, TransHistory2: 11, TransHistory3: 110, 

45- **MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [[נציב, [מחדש, [את, [סולם, הערכים]]]]]   B= [הציוני, התיישבותי, שהקים ,.. ]

B0Token: הציוני, B0_LastThreeLetters: �י, B0_LastTwoLetters: י, B1Token: התיישבותי, B1_LastThreeLetters: �י, B1_LastTwoLetters: י, S0B0Token: נציב_מחדש_את_סולם_הערכים_הציוני, S0B1Token: נציב_מחדש_את_סולם_הערכים_התיישבותי, S0B2Token: נציב_מחדש_את_סולם_הערכים_שהקים, S0Token: נציב_מחדש_את_סולם_הערכים, TransHistory1: 1, TransHistory2: 11, TransHistory3: 111, 

46- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [הציוני, התיישבותי, שהקים ,.. ]

B0Token: הציוני, B0_LastThreeLetters: �י, B0_LastTwoLetters: י, B1Token: התיישבותי, B1_LastThreeLetters: �י, B1_LastTwoLetters: י, TransHistory1: 1, TransHistory2: 11, TransHistory3: 111, 

47- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [הציוני]   B= [התיישבותי, שהקים, את ,.. ]

B0Token: התיישבותי, B0_LastThreeLetters: �י, B0_LastTwoLetters: י, B1Token: שהקים, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, S0B0Token: הציוני_התיישבותי, S0B1Token: הציוני_שהקים, S0B2Token: הציוני_את, S0Token: הציוני, S0_LastThreeLetters: �י, S0_LastTwoLetters: י, TransHistory1: 2, TransHistory2: 21, TransHistory3: 211, 

48- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [התיישבותי, שהקים, את ,.. ]

B0Token: התיישבותי, B0_LastThreeLetters: �י, B0_LastTwoLetters: י, B1Token: שהקים, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, TransHistory1: 0, TransHistory2: 02, TransHistory3: 021, 

49- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [התיישבותי]   B= [שהקים, את, מדינת ,.. ]

B0Token: שהקים, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, B1Token: את, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, S0B0Token: התיישבותי_שהקים, S0B1Token: התיישבותי_את, S0B2Token: התיישבותי_מדינת, S0Token: התיישבותי, S0_LastThreeLetters: �י, S0_LastTwoLetters: י, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

50- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [שהקים, את, מדינת ,.. ]

B0Token: שהקים, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, B1Token: את, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

51- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [שהקים]   B= [את, מדינת, ישראל ,.. ]

B0Token: את, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: מדינת, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, S0B0Token: שהקים_את, S0B1Token: שהקים_מדינת, S0B2Token: שהקים_ישראל, S0Token: שהקים, S0_LastThreeLetters: �ם, S0_LastTwoLetters: ם, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

52- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [את, מדינת, ישראל ,.. ]

B0Token: את, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: מדינת, B1_LastThreeLetters: �ת, B1_LastTwoLetters: ת, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

53- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [את]   B= [מדינת, ישראל, ביתו ,.. ]

B0Token: מדינת, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: ישראל, B1_LastThreeLetters: �ל, B1_LastTwoLetters: ל, S0B0Token: את_מדינת, S0B1Token: את_ישראל, S0B2Token: את_ביתו, S0Token: את, S0_LastThreeLetters: �ת, S0_LastTwoLetters: ת, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

54- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [מדינת, ישראל, ביתו ,.. ]

B0Token: מדינת, B0_LastThreeLetters: �ת, B0_LastTwoLetters: ת, B1Token: ישראל, B1_LastThreeLetters: �ל, B1_LastTwoLetters: ל, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

55- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [מדינת]   B= [ישראל, ביתו, הלאומי ,.. ]

B0Token: ישראל, B0_LastThreeLetters: �ל, B0_LastTwoLetters: ל, B1Token: ביתו, B1_LastThreeLetters: �ו, B1_LastTwoLetters: ו, S0B0Token: מדינת_ישראל, S0B1Token: מדינת_ביתו, S0B2Token: מדינת_הלאומי, S0Token: מדינת, S0_LastThreeLetters: �ת, S0_LastTwoLetters: ת, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

56- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ישראל, ביתו, הלאומי ,.. ]

B0Token: ישראל, B0_LastThreeLetters: �ל, B0_LastTwoLetters: ל, B1Token: ביתו, B1_LastThreeLetters: �ו, B1_LastTwoLetters: ו, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

57- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ישראל]   B= [ביתו, הלאומי, של ,.. ]

B0Token: ביתו, B0_LastThreeLetters: �ו, B0_LastTwoLetters: ו, B1Token: הלאומי, B1_LastThreeLetters: �י, B1_LastTwoLetters: י, S0B0Token: ישראל_ביתו, S0B1Token: ישראל_הלאומי, S0B2Token: ישראל_של, S0Token: ישראל, S0_LastThreeLetters: �ל, S0_LastTwoLetters: ל, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

58- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ביתו, הלאומי, של ,.. ]

B0Token: ביתו, B0_LastThreeLetters: �ו, B0_LastTwoLetters: ו, B1Token: הלאומי, B1_LastThreeLetters: �י, B1_LastTwoLetters: י, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

59- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [ביתו]   B= [הלאומי, של, העם ,.. ]

B0Token: הלאומי, B0_LastThreeLetters: �י, B0_LastTwoLetters: י, B1Token: של, B1_LastThreeLetters: �ל, B1_LastTwoLetters: ל, S0B0Token: ביתו_הלאומי, S0B1Token: ביתו_של, S0B2Token: ביתו_העם, S0Token: ביתו, S0_LastThreeLetters: �ו, S0_LastTwoLetters: ו, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

60- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [הלאומי, של, העם ,.. ]

B0Token: הלאומי, B0_LastThreeLetters: �י, B0_LastTwoLetters: י, B1Token: של, B1_LastThreeLetters: �ל, B1_LastTwoLetters: ל, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

61- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [הלאומי]   B= [של, העם, היהודי ,.. ]

B0Token: של, B0_LastThreeLetters: �ל, B0_LastTwoLetters: ל, B1Token: העם, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, S0B0Token: הלאומי_של, S0B1Token: הלאומי_העם, S0B2Token: הלאומי_היהודי, S0Token: הלאומי, S0_LastThreeLetters: �י, S0_LastTwoLetters: י, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

62- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [של, העם, היהודי ,.. ]

B0Token: של, B0_LastThreeLetters: �ל, B0_LastTwoLetters: ל, B1Token: העם, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

63- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [של]   B= [העם, היהודי, אומרים ,.. ]

B0Token: העם, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, B1Token: היהודי, B1_LastThreeLetters: �י, B1_LastTwoLetters: י, S0B0Token: של_העם, S0B1Token: של_היהודי, S0B2Token: של_אומרים, S0Token: של, S0_LastThreeLetters: �ל, S0_LastTwoLetters: ל, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

64- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [העם, היהודי, אומרים ,.. ]

B0Token: העם, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, B1Token: היהודי, B1_LastThreeLetters: �י, B1_LastTwoLetters: י, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

65- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [העם]   B= [היהודי, אומרים, מארגני ,.. ]

B0Token: היהודי, B0_LastThreeLetters: �י, B0_LastTwoLetters: י, B1Token: אומרים, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, S0B0Token: העם_היהודי, S0B1Token: העם_אומרים, S0B2Token: העם_מארגני, S0Token: העם, S0_LastThreeLetters: �ם, S0_LastTwoLetters: ם, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

66- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [היהודי, אומרים, מארגני ,.. ]

B0Token: היהודי, B0_LastThreeLetters: �י, B0_LastTwoLetters: י, B1Token: אומרים, B1_LastThreeLetters: �ם, B1_LastTwoLetters: ם, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

67- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [היהודי]   B= [אומרים, מארגני, האירוע ,.. ]

B0Token: אומרים, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, B1Token: מארגני, B1_LastThreeLetters: �י, B1_LastTwoLetters: י, S0B0Token: היהודי_אומרים, S0B1Token: היהודי_מארגני, S0B2Token: היהודי_האירוע, S0Token: היהודי, S0_LastThreeLetters: �י, S0_LastTwoLetters: י, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

68- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [אומרים, מארגני, האירוע ,.. ]

B0Token: אומרים, B0_LastThreeLetters: �ם, B0_LastTwoLetters: ם, B1Token: מארגני, B1_LastThreeLetters: �י, B1_LastTwoLetters: י, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

69- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [אומרים]   B= [מארגני, האירוע ,.. ]

B0Token: מארגני, B0_LastThreeLetters: �י, B0_LastTwoLetters: י, B1Token: האירוע, B1_LastThreeLetters: �ע, B1_LastTwoLetters: ע, S0B0Token: אומרים_מארגני, S0B1Token: אומרים_האירוע, S0Token: אומרים, S0_LastThreeLetters: �ם, S0_LastTwoLetters: ם, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

70- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [מארגני, האירוע ,.. ]

B0Token: מארגני, B0_LastThreeLetters: �י, B0_LastTwoLetters: י, B1Token: האירוע, B1_LastThreeLetters: �ע, B1_LastTwoLetters: ע, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

71- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [מארגני]   B= [האירוע]

B0Token: האירוע, B0_LastThreeLetters: �ע, B0_LastTwoLetters: ע, S0B0Token: מארגני_האירוע, S0Token: מארגני, S0_LastThreeLetters: �י, S0_LastTwoLetters: י, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

72- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [האירוע]

B0Token: האירוע, B0_LastThreeLetters: �ע, B0_LastTwoLetters: ע, TransHistory1: 0, TransHistory2: 02, TransHistory3: 020, 

73- SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= [האירוע]   B= [ ]

S0Token: האירוע, S0_LastThreeLetters: �ע, S0_LastTwoLetters: ע, TransHistory1: 2, TransHistory2: 20, TransHistory3: 202, 

74- COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;S= []   B= [ ]

