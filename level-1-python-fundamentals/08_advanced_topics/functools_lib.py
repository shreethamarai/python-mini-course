"""
    functools is a standard library module for higer-order functions
    (functions that work with other functions).
"""

"""
    functools.reduce()
        - Applies a function cumulatively to items of an iterable.
        - Think of it as "rolling up" a list into one value.
"""

from functools import reduce

nums = [1, 2, 3, 4, 5]
sum_all = reduce(lambda x, y: x+y, nums)
print(sum_all)

# Uses
#   - Summing all numbers
#   - Multiplying all numbers
#   - Combining strings or merge data


"""
    functools.lru_cache
        - Caches function results so repeated calls with the same inputs are instant.
        - Useful for experience or recursive computations
"""

from functools import lru_cache

@lru_cache
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

print(fib(30))

# Uses
#   - API response that don't change often.
#   - Recursive algorithms like Fibonacci, DFS, or dynamic programming
#   - Avoiding repeated database queries.


"""
    functools.partial()
        - Creates a new function with some arguments fixed
"""

from functools import partial

def power(base, exponent):
    return base ** exponent

square = partial(power, exponent=2)
cube = partial(power, exponent=3)

print(square(5))
print(cube(9))

# Uses
#   - Pre-filling common arguments for function
#   - Adapting a function for a differnet API signature
#   - Making cleaner callbacks in event-driven code

