
"""  sorted() 
    - Returns a new sorted list ( does not chnage the original)
    - Works on any literable (list, tuple, dict keys, etc.,).
    - Has two important parameters:
        - key -> function to determine sortling logic.
        - reverse = True -> sort in descending order.


Real-world uses

Sorting leaderboard scores

Sorting logs by timestamp

Sorting API responses by a field

Sorting database query results in Python

Sorting tasks by priority

"""

# Basic sorting 
nums = [5, 2, 9, 1]
sorted_nums = sorted(nums)
print(sorted_nums)

# Sorting by length
words = ["banana", "apple", "cherry"]
sorted_words = sorted(words, key = len)
print(sorted_words)

# Sorting by last character
words = ["bat", "apple", "dog"]
sorted_last_char = sorted(words, key = lambda w: w[-1])

# Sorting list of dictionaries
students = [
        {"name": "ALice", "score":88},
        {"name":"Bob", "score":95},
        {"name":"Charlie", "score":70}
        ]
sorted_students = sorted(students, key=lambda s: s["score"])
print(sorted_students)

# Reverse sorting
nums = [5, 2, 9, 1]
print(sorted(nums, reverse = True))

# Sorting by multiple criteria
students = [
        ("Alice", 88),
        ("Bob",95),
        ("Charlie",88)
        ]

sorted_multi =sorted(students, key=lambda s: (-s[1], s[0]))
print(sorted_multi)

# Sorting dictionary by values
scores = {"Alice":88, "Bob":95, "Charlie":70}
sorted_by_value = sorted(scores.items(), key=lambda x: x[1], reverse=True)
print(sorted_by_value)


