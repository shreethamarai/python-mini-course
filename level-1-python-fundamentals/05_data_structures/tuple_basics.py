person = ("Thamarai", 27, "India")
print("Name:", person[0])

#Tuples are immutable
try:
    person[1] = 28
except TypeError as e:
    print("Error:", e)


