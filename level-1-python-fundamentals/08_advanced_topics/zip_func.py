"""
   Zip () takes two or more iterables (lists, tuples, etc.,) and pairs their elements together.
   It stops at the shortest iterable length
"""

# zipping two lists
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

for name, score in zip (names, scores):
    print(name, score)


# Converting zipped result to a list
pairs = list(zip(names, scores))
print(pairs)

# Multiple lists
subjects = ["Math", "Science", "English"]
for name, score, subject in zip(names, scores, subjects):
    print(f"{name} got {score} in {subject}")

# Unzipping (reverse zip)
zipped = list(zip(names, scores))

names_unzipped, scores_unzipped = zip(*zipped)
print(names_unzipped, scores_unzipped, sep="\n")


####### Real-world uses 

# Combine coulmns into rows for CSV export
headers = ["Name", "Score"]
for row in zip(names, scores):
    print(dict(zip(headers, row)))

# parallel iteration for matrix addition
a = [1,2,3]
b = [4,5,6]
sum_list = [x + y for x, y in zip(a,b)]
print(sum_list)


