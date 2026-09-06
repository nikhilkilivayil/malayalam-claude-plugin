---
description: Translate text into natural Malayalam (or from Malayalam) with the right register
argument-hint: [--to en] [--register formal|neutral|casual|ui] <text or file path>
---

Translate using the `malayalam-writing` skill (§1 register, §4 translation
guidance, `reference/style-and-register.md`).

Input: $ARGUMENTS

Defaults: translate *into* Malayalam; register `neutral` (standard written
Malayalam with നിങ്ങൾ). `--to en` translates Malayalam → English. Registers:

- `formal`: താങ്കൾ, ദയവായി … ചെയ്യുക, native vocabulary over loanwords.
- `neutral`: നിങ്ങൾ, standard written Malayalam, common loanwords allowed.
- `casual`: spoken forms, English code-mixing allowed, no dialect unless asked.
- `ui`: short -ഉക imperatives (തുറക്കുക, റദ്ദാക്കുക), consistent glossary, keep
  placeholders like {name}, %s, {{count}} and markup untouched.

Rules:
1. Translate meaning, re-ordered into natural SOV Malayalam; never word-for-word.
2. Keep names, brands, code, URLs, numbers and placeholders exactly as given.
3. Established technical terms may stay as Malayalam-script loanwords (ലോഗിൻ,
   ഇമെയിൽ); in `formal` prefer native equivalents when they are in common use.
4. Apply the orthography rules (atomic chillus, ന്റ, ൗ, ഃ, no ZWJ, Latin punctuation).
5. For lists, tables, subtitles or UI strings, preserve the structure line by line.

Output the translation only. Add at most one short note if a term had no good
equivalent and you kept the English word.
