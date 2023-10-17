# russian-verb-forms
Conjugate Russian verbs. Compare expected to actual conjugation. Classify similarly conjugated verbs into groups.

Uses data from [OpenRussian.org](www.openrussian.org) and their [database](https://app.togetherdb.com/db/fwoedz5fvtwvq03v/russian3/).

# Conjugating Verbs (using most basic rules)

- Past Tense
    - remove -ть ending, then add л, ла, ло, ли endings depending on subject

- Present + Imperative Tense
    - verbs fall into one of two categories
    - remove ending (-ть or -ить/-еть)
    - add endings (see table below)

|     | -ть | -ить/-еть |
|-----|-----|-----------|
| я   | ю   | у         |
| ты  | ешь | ишь       |
| он, она, оно  | ет  | ит        |
| мы  | ем  | им        |
| вы  | ете | ите       |
| они | ют  | ят        |
| ты command | й | и |
| вы command | йте | ите |

- Reflexive verbs
    - Simply remove the -ся and conjugate like above. Then add the appropriate reflexive endings.

See a longer explanation [here](https://www.russianforeveryone.com/Rufe/Lessons/Course1/Grammar/GramUnit5/GramUnit5_2.htm)

TODO: add rules for participles and gerunds


# Expected Conjugation Algorithm in Plain English
* NOTE: You can see this algorithm applied step by step by running python3 conjugate.py with logging level set to DEBUG.

1. Set the verb stem equal to the full infinitive
2. Reflexive check; if stem ends in -ся, mark verb reflexive and remove the ending ся from the stem
3. Irregular check; if stem does not end in -ть, mark verb as irregular stem; unable to conjugate, so return early
4. Form past tense; add past tense endings to current stem (-л, -ла, -ло, -ли)
5. Accented ending check; if current stem ends in an accent, update present / future endings so first letter of ending is accented
6. Verb group check;
   * if current stem ends in -и or -е, mark as group two verb and remove и/е from stem
   * else, mark as group one verb
7. Form present/future + imperative tense; add group one/two endings to current stem
8. Reflexive additions; if verb is reflexive, add reflexive endings to all conjugated verb forms


