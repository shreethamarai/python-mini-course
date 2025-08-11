
square = lambda x: x**2
print(square(5))

users = [{"name": "B"}, {"name": "D"}, {"name": "A"}]
users.sort(key=lambda x: x["name"])
print(users)

