
try:
    value = int(input("Enter age: "))
except ValueError:
    print("That's not a number.")
else: 
    print("Your age is:", value)
finally:
    print("This block always runs.")

