"""
Activity 2.4 – Regex Examples (PEP‑8 Rewrites)
Sources:
- W3Schools Python RegEx
- Real Python: Regex Part 1
- Real Python: Regex Part 2
All examples rewritten in PEP‑8 style with explanatory comments.
"""

import re

# ============================================================
# SECTION 1 — W3SCHOOLS REGEX EXAMPLES (PEP‑8 REWRITES)
# ============================================================

# Basic search example
text = "The rain in Spain"
pattern = r"^The.*Spain$"
match = re.search(pattern, text)
print(match)

# findall(): find all occurrences of "ai"
matches = re.findall("ai", text)
print(matches)

# findall(): no match returns empty list
matches = re.findall("Portugal", text)
print(matches)

# search(): find first whitespace
match = re.search(r"\s", text)
print("First whitespace at index:", match.start())

# search(): no match returns None
match = re.search("Portugal", text)
print(match)

# split(): split on whitespace
parts = re.split(r"\s", text)
print(parts)

# split(): limit number of splits
parts = re.split(r"\s", text, maxsplit=1)
print(parts)

# sub(): replace whitespace with '9'
result = re.sub(r"\s", "9", text)
print(result)

# sub(): replace first two whitespaces
result = re.sub(r"\s", "9", text, count=2)
print(result)

# Match object: span()
match = re.search(r"\bS\w+", text)
print(match.span())

# Match object: string
print(match.string)

# Match object: group()
print(match.group())


# ============================================================
# SECTION 2 — REAL PYTHON REGEX PART 1 (PEP‑8 REWRITES)
# ============================================================

# Search for digits inside a string
match = re.search(r"(\d+)", "foo123bar")
print(match.group())

# Case‑insensitive search
match = re.search(r"[a-z]+", "123FOO456", flags=re.IGNORECASE)
print(match.group())

# search() returns None if no match
print(re.search(r"\d+", "foo.bar"))

# search() finds first match anywhere
print(re.search(r"\d+", "foo123bar"))

# match() only checks at the beginning
print(re.match(r"\d+", "123foobar"))
print(re.match(r"\d+", "foo123bar"))

# MULTILINE anchor behaviour
multiline_text = "foo\nbar\nbaz"
print(re.search("^bar", multiline_text, flags=re.MULTILINE))

# fullmatch(): entire string must match
print(re.fullmatch(r"\d+", "123"))
print(re.fullmatch(r"\d+", "123foo"))
print(re.fullmatch(r"\d+", "foo123"))

# findall(): return all matches
print(re.findall(r"\w+", "...foo,,,,bar:%$baz//|"))

# finditer(): iterator of match objects
for match in re.finditer(r"\w+", "...foo,,,,bar:%$baz//|"):
    print(match.group())


# ============================================================
# SECTION 3 — REAL PYTHON REGEX PART 2 (PEP‑8 REWRITES)
# ============================================================

# -------------------------
# Substitution examples
# -------------------------

sample_text = "foo.123.bar.789.baz"

# Replace digits with '#'
print(re.sub(r"\d+", "#", sample_text))

# Replace words with '(*)'
print(re.sub(r"[a-z]+", "(*)", sample_text))

# Swap captured groups
print(re.sub(r"(\w+),bar,baz,(\w+)", r"\2,bar,baz,\1", "foo,bar,baz,qux"))

# Named groups in substitution
print(
    re.sub(
        r"foo,(?P<w1>\w+),(?P<w2>\w+),qux",
        r"foo,\g<w2>,\g<w1>,qux",
        "foo,bar,baz,qux",
    )
)

# Avoiding \10 ambiguity using \g<1>
print(re.sub(r"(\d+)", r"\g<1>0", "foo 123 bar"))

# Entire match reference
print(re.sub(r"\d+", r"/\g<0>/", "foo 123 bar"))

# Zero‑length match substitution
print(re.sub("x*", "-", "foo"))

# Substitution using a function
def transform(match_obj):
    """Multiply digits by 10, uppercase words."""
    token = match_obj.group(0)
    if token.isdigit():
        return str(int(token) * 10)
    return token.upper()


print(re.sub(r"\w+", transform, "foo.10.bar.20.baz.30"))

# Limit number of replacements
print(re.sub(r"\w+", "xxx", "foo.bar.baz.qux", count=2))

# subn(): returns (new_string, number_of_replacements)
print(re.subn(r"\w+", "xxx", "foo.bar.baz.qux"))


# -------------------------
# Splitting examples
# -------------------------

print(re.split(r"\s*[,;/]\s*", "foo,bar ; baz / qux"))

# Capturing delimiter
print(re.split(r"(\s*[,;/]\s*)", "foo,bar ; baz / qux"))

# Non‑capturing group
print(re.split(r"(?:\s*[,;/]\s*)", "foo,bar ; baz / qux"))

# maxsplit
long_list = "foo, bar, baz, qux, quux, corge"
print(re.split(r",\s*", long_list, maxsplit=3))


# -------------------------
# Compiled regex objects
# -------------------------

compiled_digits = re.compile(r"(\d+)")
print(compiled_digits.search("foo123bar").group())

compiled_case = re.compile(r"ba[rz]", flags=re.IGNORECASE)
print(compiled_case.search("FOOBARBAZ").group())


# -------------------------
# Match object methods
# -------------------------

match = re.search(r"(\w+),(\w+),(\w+)", "foo,bar,baz")
print(match.group(1))
print(match.group(3))

named_match = re.match(
    r"(?P<w1>\w+),(?P<w2>\w+),(?P<w3>\w+)", "quux,corge,grault"
)
print(named_match.group("w1"))
print(named_match.group("w3"))

# Multiple groups at once
print(match.group(1, 3))

# Groupdict
print(named_match.groupdict())

# Span positions
print(match.span())
print(match.span(1))

# Access original string
print(match.string)
