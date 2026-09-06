---
description: Convert Manglish (Malayalam typed in Latin letters) to proper Malayalam script
argument-hint: <manglish text, or a file path>
---

Convert the following Manglish text into correctly spelled Malayalam script,
following the `malayalam-writing` skill and its `reference/transliteration.md`.

Text: $ARGUMENTS

Rules:
1. Read the Manglish as spoken Malayalam and write the real dictionary spelling;
   do not map letters one-to-one. Resolve a/aa, l/L, n/N, r/R, th/T, s/S/sh from
   the actual word and context.
2. Word-final ണ ന ര ല ള with no vowel become chillus (avan → അവൻ, aval → അവൾ);
   dative -n stays ന് (avanu → അവന്). Final "u" after other consonants is the
   samvruthokaram ് (athu → അത്).
3. Use atomic chillus, ന്റ as ന + ് + റ, ൗ for the au sign, ഃ for visarga, no ZWJ.
4. English words: keep them in Latin script (chat style) unless the user asks for
   Malayalam-script loanwords; never translate names or brands.
5. Keep the user's register (casual stays casual) and punctuation.

Output the Malayalam text only. If a word is ambiguous even in context, give the
most likely spelling and list the alternatives afterwards in one short line.
