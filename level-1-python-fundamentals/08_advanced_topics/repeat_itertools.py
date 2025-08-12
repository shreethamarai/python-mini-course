
""" itertools.repeat()
    - Repeats a single value
    - Can be infinite or a fixed number of times
"""

from itertools import repeat

for msg in repeat("Hello", 3):
    print(msg)

# Use cases
#   - Pre-filling default values.
#   - Benchmarking by running the same input


