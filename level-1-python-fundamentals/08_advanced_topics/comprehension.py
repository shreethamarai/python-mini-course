
"""
A Comprehension is a shorthand way to create lists, dict, sets or generators in single readble line.

They replace 1. for loop, 2. an append() or add() function

"""

### Type 1: List Comprehension

# Normal way
squares = []
for x in range(5):
    squares.append(x**2)
# Comprehension way
squares = [x**2 for x in range(5)]

### Type 2: Dictionary Comprehension

# Normal way
num_map = {}
for x in range(5):
    num_map[x] = x**2
# Comprehension way
num_map = {x: x**2 for x in range(5)}

### Type 3: Set Comprehension

# Normal way
unique_squares = set()
for x in range(5):
    unique_squares.add(x**2)
# Comprehension way
unique_squares = {x**2 for x in range(5)}


### Type 4: Generator Comprehension

# Comprehension way
gen = (x**2 for x in range(5))
print(next(gen))
print(next(gen))

# add conditions
even_squares = [x**2 for x in range(10) if x % 2 == 0] # if condition use

labels = ["even" if x % 2 == 0 else "odd" for x in range(5)] # if-else condn used



