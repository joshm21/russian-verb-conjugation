# is-russian-verb-conjugation-irregular
Script to check whether or not a Russian verb conjugates as expected.

Uses data from [OpenRussian.org](www.openrussian.org) and their [database](https://app.togetherdb.com/db/fwoedz5fvtwvq03v/russian3/)

# Steps
1. Download verbs and word_forms csv tables from OpenRussian database
2. Remove rows from word_forms csv table not related to verb conjugation
3. For each verb, generate expected conjugation
4. Compare expected to actual conjugations
5. Future: clasify unexpected conjugations into groups (eg интерестовать - я интересую; рисовать - я рисую; ова changes to у in present tense)

# Output
A new csv file, with the following columns
- verb infinitive
- verb aspect
- classification (eg regular, -ова- verb, irregular, etc)
- ending type (-ть, -ить/-еть, or irregular - eg идти)
- three columns for each conjugation form (present/future forms: я, ты, он, мы, вы, они, past forms: он, она, оно, они, command forms: ты, вы)
   * expected
   * actual
   * expected == actual?
   * Note: imperfective verbs have a present tense conjugation; perfective verbs have future tense conjugation

# Expected Conjugations
* Note: You can see these steps applied step by step by running python3 get_expected_conjugation --(your verb here).

Using the most basic conjugation rules, there are two types of verbs: ones that end in -ить/-еть or -ть (no и/е preceding ть).

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

Reflexive verbs (infinitive ends in -ся) are conjugated similarly. The -ся is first removed, then the -ть, -ить/-еть is rеmoved to form the stem. Then the endings are added as in the above table before finally adding the reflexive ending (-сь for я, вы, она past, оно past, они past, ты command; -ся for ты, он, мы, они, он past, вы command)

See a longer explanation [here](https://www.russianforeveryone.com/Rufe/Lessons/Course1/Grammar/GramUnit5/GramUnit5_2.htm)
