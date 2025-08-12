
""" itertools.combinations()
    - Gives all combinations of a certain length from an iterable
    - Order does not matter
"""

from itertools import combinations

team = ["A", "B", "C"]
for combo in combinations(team,2):
    print(combo)

# Uses
#   - Selecting team members.
#   - Trying different ingredient mixes in receipes.
#   - Testing security PIN combinations without repeats.


""" itertools.permutations()
    - Gives all possible arrangements of a certain length.
    - Order matters.
"""

from itertools import permutations

team = ["A", "B", "C"]
for perm in permutations(team,2):
    print(perm)

# Uses
#   - Generating possible passwords
#   - Testing all possible task others
#   - Route planning (like Travelling Salesman Problem)


""" itertools.chain()
    - Combines multiple iterable into one continues sequence.
"""

from itertools import chain

a = [1,2,3]
b = ["x", "y"]
c = [True, False]

for item in chain(a,b,c):
    print(item)

# Uses
#   Merging lists without creating a big intermediate list in memory
#   Processing multiple data sources in one loop
#   Combining API results into a single stream


