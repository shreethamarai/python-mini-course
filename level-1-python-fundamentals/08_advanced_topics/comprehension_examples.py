
"""  Real-world uses """

# Clean data
names = [" Alice ", "Bob  ", "  carol"]
cleaned = [names.strip() for names in names]
print("cleaned list", cleaned)


# Flatten Lists
matrix = [[1,2], [3,4], [5,6]]
flat = [num for row in matrix for num in row]
print("flatten list", flat)

# Filter API results
users = [{"name":"Alice"},{"name":"Bob"},{"name":None}]
valid_names = [u["name"] for u in users if u["name"]]
print("valid list", valid_names)
