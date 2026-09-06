#!/usr/bin/env python3
"""
normalize_ml.py - Malayalam Unicode normalizer and checker.

Fixes the encoding-level problems that make Malayalam text hard to search, sort,
compare and render consistently:

  * legacy chillu sequences (consonant + virama + ZWJ)  ->  atomic chillus
  * variant encodings of the nta conjunct               ->  ന + ് + റ
  * archaic two-part au sign (ൌ, U+0D4C)                ->  ൗ (U+0D57)
  * mis-ordered two-part vowel signs (ാ + െ)             ->  ൊ / ോ
  * ASCII colon used as visarga (ദു:ഖം)                  ->  ഃ (ദുഃഖം)
  * stray ZWJ / ZWNJ that do nothing
  * NFC normalization, plus an optional old->modern samvruthokaram (ു് -> ്)

It never converts a bare consonant + virama into a chillu (അവന് != അവൻ).

Usage:
  python normalize_ml.py input.txt                # print normalized text
  python normalize_ml.py input.txt -o out.txt     # write to a file
  cat text | python normalize_ml.py               # stdin -> stdout
  python normalize_ml.py --check input.txt        # report issues, change nothing
  python normalize_ml.py --stats input.txt        # normalized text + counts on stderr
  python normalize_ml.py --selftest               # run built-in tests

Options:
  --keep-zwnj             keep every ZWNJ (default: keep only ZWNJ after a virama)
  --modern-samvruthokaram convert old-style ു് to ് (off by default: some
                          publications keep the traditional spelling on purpose)
  --nta {standard,keep}   normalize nta variants to ന്റ (default) or leave them

No third-party dependencies (Python 3.8+).
"""

import argparse
import re
import sys
import unicodedata
from collections import Counter

ZWJ = "\u200d"
ZWNJ = "\u200c"
VIRAMA = "്"  # ്

# legacy chillu sequences -> atomic chillus (Unicode 5.1+)
LEGACY_CHILLU = {
    "ണ" + VIRAMA + ZWJ: "ൺ",  # ണ്\u200d -> ൺ
    "ന" + VIRAMA + ZWJ: "ൻ",  # ന്\u200d -> ൻ
    "ര" + VIRAMA + ZWJ: "ർ",  # ര്\u200d -> ർ
    "ല" + VIRAMA + ZWJ: "ൽ",  # ല്\u200d -> ൽ
    "ള" + VIRAMA + ZWJ: "ൾ",  # ള്\u200d -> ൾ
    "ക" + VIRAMA + ZWJ: "ൿ",  # ക്\u200d -> ൿ
}

NTA_STANDARD = "ന" + VIRAMA + "റ"  # ന്റ
NTA_VARIANTS = (
    "ൻ" + VIRAMA + "റ",  # ൻ്റ  (chillu-based)
    "ന" + VIRAMA + ZWJ + "റ",  # ന്\u200dറ (ZWJ-based)
    "ന" + VIRAMA + ZWNJ + "റ",  # ന്\u200cറ (ZWNJ-based)
)

MALAYALAM_LETTER = r"[അ-ഹഺൺ-ൿ]"
# a visarga can only follow a vowel: independent vowel, consonant (inherent a)
# or vowel sign - never a virama, chillu or anusvara
VISARGA_BASE = r"[അ-ഔക-ഹാ-ൄെ-ൈൊ-ൌൗ]"
VOWEL_SIGN = r"[ാ-ൄെ-ൈൊ-ൌൗ]"

# look-alike letters from other Indic scripts that sometimes leak into Malayalam
FOREIGN_INDIC = re.compile(r"[஀-௿ఀ-౿ಀ-೿ऀ-ॿ]")
DANDA = re.compile(r"[।॥]")


def normalize(text, keep_zwnj=False, modern_samvruthokaram=False, nta="standard"):
    """Return (normalized_text, Counter of applied fixes)."""
    fixes = Counter()

    def sub(pattern, repl, s, label):
        new, n = re.subn(pattern, repl, s)
        if n:
            fixes[label] += n
        return new

    # 1. nta variants first, so the chillu step below does not swallow ന്\u200dറ
    if nta == "standard":
        for variant in NTA_VARIANTS:
            text = sub(re.escape(variant), NTA_STANDARD, text, "nta -> ന്റ")

    # 2. legacy chillus (consonant + virama + ZWJ) -> atomic chillus
    for legacy, atomic in LEGACY_CHILLU.items():
        text = sub(re.escape(legacy), atomic, text, f"legacy chillu -> {atomic}")

    # 3. canonical composition (െ+ാ -> ൊ, േ+ാ -> ോ, െ+ൗ -> ൌ, etc.)
    composed = unicodedata.normalize("NFC", text)
    if composed != text:
        fixes["NFC composition"] += 1
        text = composed

    # 4. mis-ordered two-part vowel signs typed as ാ + െ / ാ + േ
    text = sub("ാെ", "ൊ", text, "ാ+െ -> ൊ")
    text = sub("ാേ", "ോ", text, "ാ+േ -> ോ")

    # 5. archaic au sign -> modern au length mark
    text = sub("ൌ", "ൗ", text, "ൌ -> ൗ")

    # 6. colon used as visarga between Malayalam letters (ദു:ഖം -> ദുഃഖം)
    text = sub(rf"(?<={VISARGA_BASE}):(?={MALAYALAM_LETTER})", "ഃ", text, ": -> ഃ")

    # 7. optional: old-style samvruthokaram ു് -> ്
    if modern_samvruthokaram:
        text = sub("ു" + VIRAMA, VIRAMA, text, "ു് -> ്")

    # 8. stray joiners
    text = sub(ZWJ, "", text, "stray ZWJ removed")
    if not keep_zwnj:
        # keep ZWNJ only where it does something: directly after a virama
        text = sub(rf"(?<!{VIRAMA}){ZWNJ}", "", text, "stray ZWNJ removed")
    # a ZWNJ at the very end of a word or line never does anything
    text = sub(rf"{ZWNJ}(?=\s|$)", "", text, "trailing ZWNJ removed")

    # 9. duplicated virama / duplicated vowel signs from typing errors
    text = sub(VIRAMA + "{2,}", VIRAMA, text, "double virama")
    text = sub(rf"({VOWEL_SIGN})\1", r"\1", text, "double vowel sign")

    return text, fixes


def check(text):
    """Return a list of (issue, count) describing problems without changing text."""
    issues = []
    _, fixes = normalize(text)
    for label, n in fixes.items():
        issues.append((label.replace(" -> ", " should be "), n))

    foreign = FOREIGN_INDIC.findall(text)
    if foreign:
        issues.append(("characters from Tamil/Telugu/Kannada/Devanagari blocks", len(foreign)))
    dandas = DANDA.findall(text)
    if dandas:
        issues.append(("danda (।) used instead of a full stop", len(dandas)))
    old_u = len(re.findall("ു" + VIRAMA, text))
    if old_u:
        issues.append(("old-style samvruthokaram ു് (fine if intentional)", old_u))
    return issues


SELFTESTS = [
    # legacy chillus (consonant + virama + ZWJ) -> atomic chillus
    ("അവള്\u200d", "അവൾ"),
    ("കാര്\u200d", "കാർ"),
    ("അവന്\u200d", "അവൻ"),
    ("കാല്\u200d", "കാൽ"),
    ("കണ്\u200d", "കൺ"),
    # a bare virama is NOT a chillu (അവന് = "to him")
    ("അവന്", "അവന്"),
    # nta variants -> ന്റ
    ("എൻ്റെ", "എന്റെ"),
    ("എന്\u200dറെ", "എന്റെ"),
    ("എന്\u200cറെ", "എന്റെ"),
    ("എന്റെ", "എന്റെ"),
    # au sign: archaic ൌ and decomposed െ+ൗ -> ൗ
    ("കൌതുകം", "കൗതുകം"),
    ("കൌതുകം", "കൗതുകം"),
    # two-part vowel signs: decomposed and mis-ordered
    ("കോട്ടയം", "കോട്ടയം"),
    ("കാേട്ടയം", "കോട്ടയം"),
    ("കാെച്ചി", "കൊച്ചി"),
    # colon used as visarga
    ("ദു:ഖം", "ദുഃഖം"),
    ("സമയം: 10 മണി", "സമയം: 10 മണി"),
    ("പേര്:നിഖിൽ", "പേര്:നിഖിൽ"),
    # ZWNJ kept after a virama, stray ZWNJ removed
    ("സോഫ്റ്റ്\u200cവെയർ", "സോഫ്റ്റ്\u200cവെയർ"),
    ("മല\u200cയാളം", "മലയാളം"),
    ("അത്\u200c വേണം", "അത് വേണം"),
    # stray ZWJ removed
    ("മല\u200dയാളം", "മലയാളം"),
    # typing errors
    ("അത്്", "അത്"),
    ("കാാലം", "കാലം"),
    # mixed sample from a legacy document
    (
        "സര്\u200dക്കാര്\u200d ദു:ഖം എന്\u200dറെ കൌമാരം",
        "സർക്കാർ ദുഃഖം എന്റെ കൗമാരം",
    ),
]


def selftest():
    failed = 0
    for src, expected in SELFTESTS:
        got, _ = normalize(src)
        ok = got == expected
        failed += not ok
        status = "PASS" if ok else "FAIL"
        extra = "" if ok else f"   (expected {expected!r})"
        print(f"{status} {src!r} -> {got!r}{extra}")
    # samvruthokaram is opt-in
    got, _ = normalize("അതു്", modern_samvruthokaram=True)
    ok = got == "അത്"
    failed += not ok
    print(("PASS" if ok else "FAIL"), "അതു് -> അത് (with --modern-samvruthokaram)")
    total = len(SELFTESTS) + 1
    print(f"{total - failed}/{total} passed")
    return failed == 0


def main(argv=None):
    parser = argparse.ArgumentParser(description="Normalize or check Malayalam Unicode text.")
    parser.add_argument("input", nargs="?", help="input file (default: stdin)")
    parser.add_argument("-o", "--output", help="write normalized text here instead of stdout")
    parser.add_argument("--check", action="store_true", help="report issues; do not modify")
    parser.add_argument("--stats", action="store_true", help="print fix counts to stderr")
    parser.add_argument("--keep-zwnj", action="store_true", help="never remove ZWNJ")
    parser.add_argument("--modern-samvruthokaram", action="store_true", help="convert ു് to ്")
    parser.add_argument("--nta", choices=["standard", "keep"], default="standard")
    parser.add_argument("--selftest", action="store_true", help="run built-in tests")
    args = parser.parse_args(argv)

    if args.selftest:
        return 0 if selftest() else 1

    if args.input:
        with open(args.input, encoding="utf-8") as f:
            text = f.read()
    else:
        text = sys.stdin.read()

    if args.check:
        issues = check(text)
        if not issues:
            print("No encoding issues found.")
        for issue, n in issues:
            print(f"{n:6d}  {issue}")
        return 0

    out, fixes = normalize(
        text,
        keep_zwnj=args.keep_zwnj,
        modern_samvruthokaram=args.modern_samvruthokaram,
        nta=args.nta,
    )
    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(out)
    else:
        sys.stdout.write(out)
    if args.stats or args.output:
        total = sum(fixes.values())
        print(f"{total} fix(es) applied", file=sys.stderr)
        for label, n in fixes.most_common():
            print(f"{n:6d}  {label}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
