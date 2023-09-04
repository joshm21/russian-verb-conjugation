# is-russian-verb-conjugation-irregular
Script to check whether or not a Russian verb conjugates as expected.

Uses data from [OpenRussian.org](www.openrussian.org) and their [database](https://app.togetherdb.com/db/fwoedz5fvtwvq03v/russian3/)

# Steps
1. Download verbs and word_forms csv tables from OpenRussian database
2. Remove rows from word_forms csv table not related to verb conjugation
3. For each verb, generate expected conjugation
4. Compare expected to actual conjugations
5. Future: clasify unexpected conjugations into groups (eg интерестовать - я интересую; рисовать - я рисую; ова changes to у in present tense)

# Expected Conjugations
Using the most basic conjugation rules, there are two types of verbs, ones that end in -ить/-еть or -ть (no и/е preceding ть).

The conjugated verb is formed by removing the ending to create the verb stem, and then adding the appropriate endings.

The present tense endings are shown below:
|     | -ть | -ить/-еть |
|-----|-----|-----------|
| я   | ю   | у         |
| ты  | ешь | ишь       |
| он  | ет  | ит        |
| мы  | ем  | им        |
| вы  | ете | ите       |
| они | ют  | ят        |


See a longer explanation [here](https://www.russianforeveryone.com/Rufe/Lessons/Course1/Grammar/GramUnit5/GramUnit5_2.htm)
