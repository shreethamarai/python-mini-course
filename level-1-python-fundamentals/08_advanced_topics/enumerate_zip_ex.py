
""" 
    enumerate() and zip() examples with tuple, dict, set
"""

### Using with Tuples
# enumerate()
colors = ("red", "green", "blue")
for idx, color in enumerate(colors):
    print(idx, color)
# zip()
sizes = ("S", "M", "L")
for color, size in zip(colors, sizes):
    print(color, size)

### Using with Sets
""" Sets are unordered, so index positions are not fixed.
    - enumerate() works, but order may vary.
    - zip() works, but element pairing might not match between runs.
"""
# enumerate()
fruits = {"apple", "banana", "cherry"}
for idx, fruit in enumerate(fruits):
    print(idx, fruit)

# zip() 
set1 = {"apple", "banana", "cherry"}
set2 = {"red", "yellow", "pink"}
for fruit, color in zip(set1, set2):
    print(fruit, color)

### Using with Dictionaries
""" Dictionaries by default iterate over keys. 
    But you can explicitly get:
    - Keys with .keys()
    - Values with .values()
    - Key-Value pairs with .items()
"""
# enumerate()
person = {"name": "Alice","age":25,"city":"Paris"}
for idx, (key, value) in enumerate(person.items()):
    print(idx, key, value)

# zip()
scores = {"Alice":85, "Bob":90,"Charlie":78}
ages = {"Alice":25,"Bob":30, "Charlie":22}

for (name1, score), (name2, age) in zip(scores.items(), ages.items()):
    print(name1, score, age)

