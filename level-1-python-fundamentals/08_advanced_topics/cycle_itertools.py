
""" itertools.cycle()
    - Repeats an iterable forever.
    - Great for round-robin scheduling
"""

from itertools import cycle

colors = ["red", "green", "blue"]
for i, color in zip(range(7), cycle(colors)):
    print(color)

# Use cases
#   Assigning turn order in multiplayer games
#   Repeating test patterns in simulations

