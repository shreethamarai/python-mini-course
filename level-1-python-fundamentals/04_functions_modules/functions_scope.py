
x = "global"

def show_scope():
    x = "local"
    print("Inside function:", x)


show_scope()
print("Outside function:", x)

