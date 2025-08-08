

# List are mutable
a = [1, 2, 3]
b = a
b.append(4)
print("a:", a) # a also changes

# Tuples are immutable
x = (1,2,3)
y = x

try:
    y += (4,)
except Exception as e:
    print("Error:", e)

print("x:", x)
print("y:", y)

