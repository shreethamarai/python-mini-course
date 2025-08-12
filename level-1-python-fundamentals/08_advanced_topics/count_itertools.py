
"""  itertools.count()
    - Generates an endless sequence of numbers.
    - You can give it a start and a step.
    - Useful when you need an auto-incrementing number without manually 
      managing a counter

"""

from itertools import count
for i in count(start=5, step=2):
    print(i)
    if i>15:
        break

# Real-world uses
# Auto ID Assignment

usernames = ["Alice", "Bob", "Charlie"]
for uid, name in zip(count(1001), usernames):
    print(uid, name)

# Pagination systems: Auto- generating page numbers without storing them in a variable.
# Streaming data indexing: Giving each incoming API record an incremental ID.


