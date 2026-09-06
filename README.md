# Malayalam plugin for Claude

Write, proofread, translate and transliterate **Malayalam (മലയാളം)** correctly in
Claude Code and Claude Cowork.

Large language models handle Malayalam reasonably well until the details: legacy
chillu encodings, ZWJ/ZWNJ noise, the ന്റ conjunct, the archaic au-sign, Tamil
look-alike letters, over-Sanskritised register, and Manglish that gets mapped
letter-by-letter. This plugin gives Claude the rules a careful Malayalam editor
applies, plus a script that repairs Malayalam text at the Unicode level.

## What's inside

| Component | What it does |
|---|---|
| `skills/malayalam-writing` | Orthography, Unicode hygiene, register/politeness, grammar reminders, translation and UI-localization guidance, Kerala conventions (dates, numbers, districts), Manglish rules. Loads automatically whenever Malayalam is involved. |
| `skills/malayalam-unicode` | `scripts/normalize_ml.py` — dependency-free normalizer/checker: atomic chillus, ന്റ, ൗ, visarga, stray joiners, NFC, foreign-script detection. |
| `/manglish` | Convert Manglish ("njan nale varum") to Malayalam script (ഞാൻ നാളെ വരും). |
| `/proofread-ml` | Proofread Malayalam text: encoding → spelling → grammar → punctuation, with a change list. |
| `/translate-ml` | Translate to/from Malayalam with a chosen register: formal, neutral, casual or UI strings. |

## Install

Claude Code:

```bash
claude plugin marketplace add nikhilkilivayil/malayalam-claude-plugin
claude plugin install malayalam@malayalam-plugins
```

Or, once listed in the Claude plugin directory, install it from
[claude.com/plugins](https://claude.com/plugins) (Cowork) or `/plugin` (Claude Code).

## Try it

```
/manglish ente peru Nikhil aanu, njan Kochiyil aanu thamasikkunnathu
→ എന്റെ പേര് നിഖിൽ ആണ്, ഞാൻ കൊച്ചിയിൽ ആണ് താമസിക്കുന്നത്.

/translate-ml --register ui "Save changes"
→ മാറ്റങ്ങൾ സേവ് ചെയ്യുക

python skills/malayalam-unicode/scripts/normalize_ml.py --check subtitles.srt
```

## Normalizer

```bash
python skills/malayalam-unicode/scripts/normalize_ml.py --selftest
python skills/malayalam-unicode/scripts/normalize_ml.py input.txt -o output.txt
```

It converts legacy chillu sequences (ള + ് + ZWJ → ൾ), nta variants (ൻ്റ → ന്റ), the
archaic au sign (ൌ → ൗ), colon-as-visarga (ദു:ഖം → ദുഃഖം), mis-ordered vowel
signs, stray ZWJ/ZWNJ and typing doubles, and applies NFC. It never turns a bare
virama into a chillu (അവന് ≠ അവൻ). `--check` reports without changing anything.

## Why this exists

Malayalam is spoken by around 35–40 million people, yet Malayalam-specific
tooling for AI assistants is thin. This plugin encodes the conventions used by
Kerala's publishing, localization (SMC/GNOME/Wikipedia) and subtitling
communities so that Claude's Malayalam is correct by default.

## Contributing

Issues and pull requests are welcome — especially corrections from native
editors, additional Manglish conventions, and dialect notes.

## License

MIT © Nikhil Kilivayil
