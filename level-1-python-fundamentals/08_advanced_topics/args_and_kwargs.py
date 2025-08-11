
def greet (*args, **kwargs):
    print("Positional:", args)
    print("Keywords:", kwargs)

greet("Hi", "Hello", name="Thamarai", role="Developer")
greet(1,2,3, "Hello", name="Thamarai", role="Developer", age = 30)
