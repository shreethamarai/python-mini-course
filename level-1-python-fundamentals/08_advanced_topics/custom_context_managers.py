"""
How Context Managers works intenrally

A context manager needs two methods:
    - __enter__() -> runs at the start (setup)
    - __exit__() -> runs at the end (cleanup)

"""

# Option 1: Example custom context manager

class MyContext:
    def __enter__(self):
        print("Entering context...")
        return "Resource Ready"

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting context..")
        if exc_type:
            print(f"An error occured: {exc_value}")
        return False   # False means exceptions will be raised


# Using it
with MyContext() as resource:
    print(resource)



# Option 2: Using contextlib lib

from contextlib import contextmanager

@contextmanager
def managed_resource():
    print("Setup resource")
    yield "Using resource"
    print("Cleanup resource")

with managed_resource() as res:
    print(res)

