---
name: malayalam-writing
description: Write, edit, proofread, translate and transliterate Malayalam (മലയാളം) correctly. Use whenever the user asks for anything in Malayalam, asks to translate to or from Malayalam, sends Manglish (Malayalam typed in Latin letters, e.g. "njan nale varum"), asks to proofread or correct Malayalam text, or works on Kerala-facing content, localization (UI strings, app copy, documents) or subtitles. Covers modern orthography, Unicode hygiene, register and politeness, and Kerala conventions for dates, numbers and names.
---

# Malayalam writing

Malayalam is the language of Kerala (about 35–40 million speakers), written in the
Malayalam script (Unicode block U+0D00–U+0D7F). Follow the rules below whenever
you produce or edit Malayalam. Load the reference files for detail:

- `reference/orthography.md` – script, Unicode encoding, spelling pitfalls
- `reference/style-and-register.md` – register, politeness, grammar, formats
- `reference/transliteration.md` – Manglish → Malayalam and romanization

## 1. Decide the register first

| Context | Register | Example ("Please try again") |
|---|---|---|
| Documents, news, official text, UI strings | Standard written Malayalam (മാനക മലയാളം) | ദയവായി വീണ്ടും ശ്രമിക്കുക. |
| Chat, social media, dialogue, ads | Colloquial, may code-mix with English | ഒന്നൂടെ നോക്കൂ. |
| Literature, formal speeches | Elevated, Sanskrit-rich vocabulary | ദയവായി ഒരിക്കൽക്കൂടി ഉദ്യമിക്കുക. |

Default to standard written Malayalam unless the user's own text is colloquial or
they ask for a casual tone. Do not mix registers inside one piece.

## 2. Orthography rules (always apply)

1. **Use only Malayalam-block characters** for Malayalam text. Never substitute
   look-alike Tamil, Kannada, Telugu or Devanagari letters (a common model error is
   Tamil ள் or ண் in place of Malayalam ൾ / ൺ).
2. **Chillus are atomic characters**: ൺ ൻ ർ ൽ ൾ (U+0D7A–U+0D7E). Never build them
   from consonant + virama + ZWJ (ണ/ന/ര/ല/ള + ് + ZWJ). Examples: അവൾ, വാൾ, കാൽ,
   നൽകുക, അവർ, ഊർജം, ഒൻപത്, കൺ.
3. **Consonant + virama without ZWJ is a different thing from a chillu.** അവൻ =
   "he", അവന് = "to him". Never "fix" a final ് into a chillu automatically.
4. **ന്റ (nta)** is written ന + ് + റ (U+0D28 U+0D4D U+0D31): എന്റെ, നിന്റെ,
   പാർലമെന്റ്, ഇന്റർനെറ്റ്. Do not use ൻ + ് + റ or ZWJ variants.
5. **ൗ (U+0D57) is the modern au-sign**: കൗതുകം, ഗൗരവം. The two-part sign ൌ
   (U+0D4C) is archaic.
6. **Samvruthokaram** (the half-u at the end of words like അത്, ഇത്, ഇന്ന്, ആണ്,
   വെള്ളത്തിന്): modern spelling ends in a bare virama (്). The older form
   അതു് (ു + ്) appears in older or classical texts and in some publications
   that keep the traditional orthography. Follow the source document's
   convention when editing; use the modern form when writing new text.
7. **ZWNJ (U+200C)** is legitimate only to keep a visible virama between two
   consonants that would otherwise ligate, mostly in loanwords: സോഫ്റ്റ്‌വെയർ,
   ഹാർഡ്‌വെയർ. Do not sprinkle ZWJ/ZWNJ anywhere else.
8. **Visarga** is ഃ (U+0D03), not a colon: ദുഃഖം, not ദു:ഖം.
9. **Punctuation** is Latin-style: . , ? ! ; : " " ( ). Malayalam does not use the
   danda ।. No space before punctuation; one space after.
10. **Digits**: use 0–9 (Arabic numerals). Malayalam digits ൦–൯ only for
    decorative or historical use.
11. **Gemination and near-homophones change meaning** – double-check: കല (art)
    / കല്ല് (stone); പനി (fever) / പണി (work); കുളം (pond) / കുലം (clan);
    പുര (house) / പുറ (outside).

## 3. Grammar reminders for natural output

- Word order is SOV; verbs come last. Modifiers precede the noun; relative clauses
  precede the noun (ഇന്നലെ വന്ന ആൾ = "the person who came yesterday").
- **Verbs do not change for person, number or gender** (ഞാൻ പോയി / അവർ പോയി).
  Politeness is carried by pronouns and sentence endings, not by verb agreement.
- Pronouns of address: താങ്കൾ (formal, respectful), നിങ്ങൾ (polite/neutral,
  also plural), നീ (intimate or to juniors — avoid in professional text).
- Requests: formal written = ദയവായി … ചെയ്യുക; polite spoken = … ചെയ്യൂ / …
  ചെയ്യാമോ?; official notices = … ചെയ്യേണ്ടതാണ്.
- Common written sandhi is joined: അതുകൊണ്ട്, എന്നാൽ, അതിനാൽ, വേണമെന്ന്,
  ചെയ്യുകയാണ്. Do not over-merge unfamiliar combinations.
- Quotative എന്ന് follows the quoted content: "വരാം" എന്ന് അവൻ പറഞ്ഞു.
- Yes/no questions take the clitic -ഓ: വരുമോ? ശരിയാണോ?

## 4. Translation guidance (English → Malayalam)

- Translate meaning, not word order. Re-order into SOV and use postpositions
  (വീട്ടിലേക്ക്, കുട്ടികൾക്കുവേണ്ടി).
- Keep established English technical terms as Malayalam-script loanwords
  (ലോഗിൻ, ഇമെയിൽ, ആപ്പ്, ഡൗൺലോഡ്, ഫയൽ, സെറ്റിങ്സ്) unless the user wants
  pure Malayalam (പ്രവേശിക്കുക, ഇ-തപാൽ, ക്രമീകരണങ്ങൾ, …). Never translate
  brand names.
- UI strings use the -ഉക imperative: തുറക്കുക (Open), അടയ്ക്കുക (Close),
  സേവ് ചെയ്യുക / സംരക്ഷിക്കുക (Save), റദ്ദാക്കുക (Cancel), തുടരുക (Continue),
  തിരയുക (Search), അയയ്ക്കുക (Send), ഇല്ലാതാക്കുക (Delete). Keep them short and
  consistent across the product.
- Gender-neutral by default; Malayalam pronouns അവർ (they/respectful) and
  വ്യക്തി (person) avoid gendered forms.
- When a term has no natural equivalent, keep the English word in Latin script
  inside Malayalam text rather than coining an awkward calque.

## 5. Manglish (Malayalam in Latin letters)

If the user writes Manglish (e.g. "ente peru Nikhil aanu, njan Kochiyil aanu
thamasikkunnathu"), read it as Malayalam. Reply in the same mode the user used
unless asked otherwise; when asked to convert, follow `reference/transliteration.md`:
resolve ambiguities (a/aa, l/L, n/N, r/R, th/T) with vocabulary knowledge, write
chillus at word ends (avan → അവൻ, aval → അവൾ, avar → അവർ), and use the modern
samvruthokaram (athu → അത്).

## 6. Kerala conventions

- Dates: "2026 സെപ്റ്റംബർ 7" or "7 സെപ്റ്റംബർ 2026"; weekday ഞായറാഴ്ച… ശനിയാഴ്ച.
  Malayalam-calendar (കൊല്ലവർഷം) months when relevant: ചിങ്ങം, കന്നി, തുലാം,
  വൃശ്ചികം, ധനു, മകരം, കുംഭം, മീനം, മേടം, ഇടവം, മിഥുനം, കർക്കടകം.
- Numbers: Indian grouping 12,34,567; ലക്ഷം (lakh), കോടി (crore); currency ₹ or രൂപ.
- District names in Malayalam with official English spellings are listed in
  `reference/style-and-register.md`; keep the official English spellings in
  English text (Thiruvananthapuram, Kozhikode, Thrissur, Kasaragod).

## 7. Proofreading procedure

When asked to proofread or correct Malayalam:

1. Run `scripts/normalize_ml.py --check` from the `malayalam-unicode` skill (if the
   file is available) to catch encoding-level issues; otherwise check rules in §2
   by eye.
2. Fix spelling, chillu/virama, ന്റ, ൗ, visarga, punctuation and spacing.
3. Fix grammar and register without rewriting the author's voice.
4. Return the corrected text first, then a short list of changes with reasons
   (in the user's language). Do not silently change meaning.

## 8. Self-check before sending Malayalam

- Every character in Malayalam words is from the Malayalam block; no ZWJ chillus.
- Chillus at word ends where intended; no accidental ൻ/ന് swaps.
- ന്റ, ൗ, ഃ encoded as specified; no stray ZWJ/ZWNJ.
- Register is consistent; verbs are sentence-final; the text reads naturally
  aloud to a native speaker.
