# Malayalam orthography and Unicode reference

## Script inventory (Unicode block U+0D00–U+0D7F)

| Group | Characters |
|---|---|
| Independent vowels | അ ആ ഇ ഈ ഉ ഊ ഋ എ ഏ ഐ ഒ ഓ ഔ |
| Vowel signs | ാ ി ീ ു ൂ ൃ െ േ ൈ ൊ ോ ൗ |
| Anusvara / visarga | ം (U+0D02) ഃ (U+0D03) |
| Virama (ചന്ദ്രക്കല) | ് (U+0D4D) |
| Consonants | ക ഖ ഗ ഘ ങ ച ഛ ജ ഝ ഞ ട ഠ ഡ ഢ ണ ത ഥ ദ ധ ന പ ഫ ബ ഭ മ യ ര ല വ ശ ഷ സ ഹ ള ഴ റ |
| Chillus (atomic) | ൺ U+0D7A, ൻ U+0D7B, ർ U+0D7C, ൽ U+0D7D, ൾ U+0D7E, ൿ U+0D7F |
| Digits (rare) | ൦ ൧ ൨ ൩ ൪ ൫ ൬ ൭ ൮ ൯ |

Archaic letters (ഩ U+0D29, ഺ U+0D3A, ൎ dot reph U+0D4E, ൔ ൕ ൖ chillus, fractions
൘–൵) should not appear in contemporary text unless the user is transcribing old
material.

## Encoding rules

### Chillus

Chillu letters are "pure" consonants without an inherent vowel. Since Unicode 5.1
they are single code points. The legacy encoding consonant + ് + ZWJ (U+200D)
renders identically in most fonts but breaks search, sorting and comparison, and
mixed encodings inside one document are a common source of "duplicate" words.

| Legacy sequence | Atomic chillu |
|---|---|
| ണ + ് + ZWJ | ൺ |
| ന + ് + ZWJ | ൻ |
| ര + ് + ZWJ | ർ |
| ല + ് + ZWJ | ൽ |
| ള + ് + ZWJ | ൾ |
| ക + ് + ZWJ | ൿ |

Only convert sequences that contain the ZWJ. A consonant followed by a bare virama
is a real, different spelling: അവൻ (he) vs അവന് (to him), മകൻ (son) vs മകന്
(to the son).

### ന്റ (nta)

The conjunct ന്റ is encoded ന + ് + റ (U+0D28 U+0D4D U+0D31): എന്റെ, നിന്റെ,
അവന്റെ, പാർലമെന്റ്, ഇന്റർനെറ്റ്, സെന്റർ, മന്ത്രിയുടേതിന്റെ.
Variants seen in the wild – ൻ + ് + റ (chillu-based) and ന + ് + ZWJ + റ – should
be normalized to the standard form.

### The au sign

- Modern: consonant + ൗ (U+0D57 AU LENGTH MARK): കൗതുകം, ഗൗരവം, സൗകര്യം, മൗനം.
- Archaic: consonant + ൌ (U+0D4C, displayed as െ + ൗ). Unicode NFC composes
  െ + ൗ into ൌ; convert ൌ → ൗ for modern text.

### Two-part vowel signs

ൊ (U+0D4A) and ോ (U+0D4B) are single code points; Unicode NFC composes the
sequences െ + ാ and േ + ാ into them. The reversed typing error ാ + െ / ാ + േ is
never valid and should be corrected to ൊ / ോ.

### Samvruthokaram (the half-u)

Words like അത്, ഇത്, ഇന്ന്, ആണ്, വരുന്നത്, വെള്ളത്തിന് end in a bare virama in the
post-1971 orthography. The traditional spelling writes ു + ് (അതു്, ആണു്). Both are
readable; be consistent, and keep the convention of a document you are editing.

### ZWJ and ZWNJ

- ZWJ (U+200D) has no role in modern Malayalam except inside legacy chillu
  sequences. Remove it once those are converted.
- ZWNJ (U+200C) prevents two consonants from forming a conjunct and keeps a
  visible ്. Legitimate uses are loanwords and a few compounds: സോഫ്റ്റ്‌വെയർ,
  ഹാർഡ്‌വെയർ, എക്സ്‌പോർട്ട്, തമിഴ്‌നാട്. Never insert it after a chillu (chillus never
  ligate) or between letters that do not form a conjunct.

### Visarga and colon

ഃ (U+0D03) is a letter; ":" is punctuation. Write ദുഃഖം, ദുഃസ്വപ്നം, നിഃശബ്ദം;
never ദു:ഖം.

### Anusvara

ം stands for a final or pre-consonantal /m/: മരം, കളം, സംഭവം, സംസ്ഥാനം. Do not
write മ + ് in its place at the end of a word (മരം, not മരമ്).

### Old script vs new script

The 1971 script reform ("പുതിയ ലിപി") writes the u/uu signs and the reph
separately instead of as ligatures. This is a font/rendering choice: the Unicode
encoding is identical. Do not try to imitate old-script ligatures with control
characters.

## Common spelling pitfalls

| Correct | Frequent error | Note |
|---|---|---|
| ഇംഗ്ലീഷ് | ഇംഗ്ലിഷ് / ഇങ്ങ്ലീഷ് | anusvara + ഗ്ല |
| ദുഃഖം | ദു:ഖം | visarga, not colon |
| ഭാഷ | ഭാശ | ഷ vs ശ |
| ശരി | സരി | ശ vs സ |
| സാഹിത്യം | സാഹിത്തിയം | conjunct ത്യ |
| ജ്ഞാനം | ഞാനം (as a noun) | ജ്ഞ conjunct (ഞാൻ = I is a different word) |
| വിദ്യാർഥി / വിദ്യാർത്ഥി | — | both attested; pick one and stay consistent |
| ഉദ്ദേശ്യം (purpose) | ഉദ്ദേശം | the shorter form is colloquial |
| പ്രധാനം (important) | പ്രദാനം (bestowal) | different words |
| അവൻ (he) / അവന് (to him) | swapped | chillu vs virama |
| കല (art) / കല്ല് (stone) | — | gemination changes meaning |
| പനി (fever) / പണി (work) | — | ന vs ണ |
| കുളം (pond) / കുലം (clan) | — | ള vs ല |
| പുര (house) / പുറ (outside) | — | ര vs റ |
| വളരെ | വളരേ | short െ in the adverb |
| നന്ദി | നന്ധി | ന്ദ |

## Look-alike characters from other scripts

Models and OCR sometimes emit characters from neighbouring scripts. All of the
following are wrong inside Malayalam text and must be replaced:

- Tamil: ள ண ந ர ல ழ ன ் (U+0B80 block)
- Kannada / Telugu: ಕ ಗ ಳ (U+0C80 block), క గ ళ (U+0C00 block)
- Devanagari danda । (U+0964) and double danda ॥ (U+0965) – Malayalam uses "."

A quick test: every letter of a Malayalam word must have a code point between
U+0D00 and U+0D7F, or be ZWNJ in a legitimate position.
