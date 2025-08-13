
"""
    Collections module gives us high performance data sturctures beyond the built-in list, dict, set, and tuple.
"""

### Counter - counts how many times each element appears

from collections import Counter

fruits = ["apple", "banana", "apple", "orange", "banana", "apple"]
count = Counter(fruits)
print(count)
print(count.most_common(1))

# Uses
#   - Word feequency in text analysis
#   - Counting votes in elections
#   - Finding most common items in a dataset

### defaultdict - Like a normal dict, but if a kehy doesn't exist, it creates it with a default value.

from collections import defaultdict

scores = defaultdict(int)
scores["Alice"] += 10
scores["Bob"] += 5
print(scores)

# Uses
#   - Grouping data without key existence checks
#   - Initializing lists for appending

groups = defaultdict(list)
groups["A"].append(1)
groups["A"].append(2)
print(groups)

### namedtuple - tuple with named fields - readable and lightweight alternative to classes.

from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])
p = Point(10, 20)
print(p.x, p.y)

# Uses
#   - Returning multiple values from functions with names
#   - Representing database records
#   - Immutable data containers


### deque - double-ended queue - fast appends and pops from both ends

from collections import deque

d = deque([1,2,3])
d.appendleft(0)
d.append(4)
print(d)
d.pop()
d.popleft()
print(d)

# Uses
#   - Task queues
#   - Undo/redo funcctionality
#   - Sliding window problems





