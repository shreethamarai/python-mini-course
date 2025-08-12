
""" Enumerate
enumerate() lets you get both the index and the value in one go
"""

# without enumerate()
items = ["apple", "banana", "cherry"]
index = 0
for fruit in items:
    print(index, fruit)
    index += 1

# with enumerate()
for index, fruit in enumerate(items):
    print(index, fruit)

for index, fruit in enumerate(items, start = 1):
    print(index, fruit)

