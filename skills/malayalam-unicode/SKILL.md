---
name: malayalam-unicode
description: Normalize, check and repair Malayalam Unicode text at the encoding level. Use when Malayalam text looks right but behaves wrong — search or find-and-replace misses words, the same word sorts or counts as two, chillu letters (ൻ ർ ൽ ൾ ൺ) render inconsistently, text came from OCR, PDFs, old websites or legacy fonts (ML-TTKarthika and similar), or when preparing Malayalam corpora, subtitles, datasets or translations for release. Also use when the user mentions ZWJ/ZWNJ, atomic chillu, "nta" (ന്റ), samvruthokaram, or Malayalam encoding problems.
---

# Malayalam Unicode normalization

Malayalam has several *encoding-level* ambiguities: the same visible word can be
stored in different code-point sequences. This skill fixes them with a
deterministic script and explains what changed.

## When to run the script

- Text from OCR, PDFs, legacy websites, Word documents converted from ASCII fonts,
  or old Unicode (pre-5.1) systems.
- Before deduplicating, sorting, searching, tokenizing, diffing or training on
  Malayalam text.
- When a user reports that "the same word appears twice in search results" or
  that a chillu looks different in two places.

## How to run

```bash
python scripts/normalize_ml.py --check input.txt      # report only (safe)
python scripts/normalize_ml.py input.txt -o output.txt  # normalize, counts on stderr
cat snippet.txt | python scripts/normalize_ml.py       # quick stdin -> stdout
python scripts/normalize_ml.py --selftest              # verify the script works
```

Options: `--keep-zwnj` (never remove ZWNJ), `--modern-samvruthokaram` (convert
old-style ു് to ്; off by default because some publishers keep the traditional
spelling deliberately), `--nta keep` (leave nta variants untouched).

The script has no dependencies beyond Python 3.8+. If the file is not on disk,
apply the same rules by hand (see table).

## What it fixes and why

| Fix | Example | Reason |
|---|---|---|
| Legacy chillu (consonant + ് + ZWJ) → atomic chillu | അവള + ് + ZWJ → അവൾ | Unicode 5.1 atomic chillus are the standard; mixed encodings break search and sorting |
| nta variants → ന + ് + റ | എൻ്റെ → എന്റെ | one canonical encoding of the ന്റ conjunct |
| Archaic au sign ൌ → ൗ | കൌതുകം → കൗതുകം | modern orthography |
| Decomposed/mis-ordered two-part signs → ൊ ോ | ക+ാ+െ → കൊ | typing errors; NFC composition |
| ASCII colon as visarga → ഃ | ദു:ഖം → ദുഃഖം | visarga is a letter |
| Stray ZWJ / ZWNJ removed | മല + ZWNJ + യാളം → മലയാളം | joiners that do nothing pollute the text; ZWNJ after a virama (സോഫ്റ്റ്‌വെയർ) is kept |
| Double virama / double vowel sign | അത്് → അത് | typing errors |
| `--check` also flags | Tamil/Kannada/Telugu/Devanagari letters, danda ।, old-style ു് | script mixing and orthography drift |

What it deliberately does **not** do:

- It never turns consonant + virama into a chillu: അവന് (to him) and അവൻ (he)
  are different words.
- It does not change spelling, grammar or vocabulary. Use the `malayalam-writing`
  skill for that.
- It does not touch text in other scripts beyond NFC composition.

## Reporting to the user

After normalizing, summarise the counts per fix (the script prints them) and show
two or three before/after examples. If `--check` flags foreign-script characters,
list the words that contain them; those usually need manual correction because the
intended Malayalam letter must be inferred from context.

## Converting legacy ASCII-font text

Text typed in pre-Unicode fonts (ML-TTKarthika, ML-TTRevathi, Manorama, etc.) is
stored as Latin characters that only look like Malayalam in that font. This script
cannot convert it — recommend the free "Payyans" converter maintained by
Swathanthra Malayalam Computing (SMC), then run this normalizer on the result.
