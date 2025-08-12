""" enumerate() Real-world uses """

# Processing CSV rows with row numbers

rows = ["name,age", "Alice,30", "Bob,25"]
for line_number, row in enumerate(rows, start = 1):
    print(f"Row {line_number}: {row}")

# Tracking positions in search

words = ["dog", "cat", "fish"]
target = "cat"

for index, word in enumerate(words):
    if word == target:
        print(f"Found '{target}' at index {index}")

