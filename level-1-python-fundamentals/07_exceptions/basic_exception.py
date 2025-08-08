
try:
    x = int(input("Enter a number: "))
    result = 10 / x 
    print("Result:", result)
except ZeroDivisionError:
    print("You can't divide by zero!")
except ValueError:
    print("Invaild input. Please enter a number.")

