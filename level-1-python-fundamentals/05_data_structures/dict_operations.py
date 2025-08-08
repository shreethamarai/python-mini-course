
person = {
        "name" : "Thamarai",
        "age" : 27,
        "location" : "India"
        }

print("Name:", person["name"])

#Update and loop 
person["age"] = 28
for key, value in person.items():
    print(f"{key} -> {value}:")


