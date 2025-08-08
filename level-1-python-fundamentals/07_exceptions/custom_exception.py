try:
    raw = input("Enter your age: ")
    age = int(float(raw))  # accepts both 18 and 18.5
    if age < 18:
        raise UnderAgeError("You're underaged!")
    print("Access granted.")
except ValueError:
    print("Invalid input — please enter a number.")
except UnderAgeError as e:
    print("Access denied:", e)

