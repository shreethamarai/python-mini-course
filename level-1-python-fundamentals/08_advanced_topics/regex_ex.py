
"""
    Regular Expressions module used to search, match, and manipulate text using patterns.
"""

import re

pattern = r"cat"
text = "THe cat sat on the mat"
match = re.search(pattern, text)
if match:
    print("Found:", match.group())

"""
    r"..." means raw string - avoids issues with backslashes.

    Special Character
    . -> anyother character except newline
    ^ -> start of string
    $ -> end of string
    * -> 0 or more repeats
    + -> 1 or more repeats
    ? -> 0 or 1 occurance
    {n} -> exactly n times
    {n,} -> n or more times
    {n,m} -> between n and m times

    Character clsses
    [abc] -> a,b, or c
    [^abc] -> NOT a,b, or c
    \d -> digit
    \D -> non-digit
    \w -> word character (a-z, A-Z, 0-9, _)
    \W -> non-word character
    \s -> whitespace
    \S -> non-whitespace
"""
#   Matching and finding
emails = "Contact: test@example.com, hello@world.net"
matches = re.findall(r"[\w\.-]+@[\w\.-]+", emails)
print(matches)

# Replace text

text = "Hello 123 World 456"
new_text = re.sub(r"\d+", "#", text)
print(new_text)

# Validating input
pattern = r"^\d{4}-\d{2}-\d{2}$"
print(bool(re.match(pattern, "2025-08013")))
print(bool(re.match(pattern, "13-08-2025")))

# Real-world uses
#   - Email/ phone number validation
#   - Log file parsing
#   - Search & replace in text files
#   - Extracting structured data from messy text




