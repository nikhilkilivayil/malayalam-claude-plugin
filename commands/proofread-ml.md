---
description: Proofread Malayalam text for spelling, encoding, grammar and register
argument-hint: <malayalam text, or a file path>
---

Proofread the following Malayalam text using the `malayalam-writing` skill
(rules in §2 and `reference/orthography.md`) and, if the file is available, the
`malayalam-unicode` script (`python scripts/normalize_ml.py --check`).

Text: $ARGUMENTS

Do this in order:
1. Encoding: legacy chillus, ന്റ variants, ൌ/ൗ, colon-as-visarga, stray ZWJ/ZWNJ,
   foreign-script look-alike letters.
2. Spelling: ന/ണ, ല/ള, ര/റ, ശ/ഷ/സ confusions, gemination, chillu vs virama
   (അവൻ/അവന്), anusvara vs മ്, common misspellings.
3. Grammar and usage: sentence-final verbs, case endings and postpositions,
   negation (ഇല്ല/അല്ല/വേണ്ട), consistent register and pronouns of address.
4. Punctuation and spacing: no danda, no space before punctuation, Indian digit
   grouping, ₹/രൂപ.

Output:
- First the fully corrected text.
- Then a compact list of changes: `original → corrected — reason` (one line
  each), in the language the user wrote their request in.
- Do not change meaning, tone or dialect; if something is ambiguous, keep the
  author's choice and flag it as a question instead.
