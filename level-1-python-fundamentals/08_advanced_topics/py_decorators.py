
def loggers(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@loggers
def add(a,b):
    return a + b

a = add(5,32)
print(a)
