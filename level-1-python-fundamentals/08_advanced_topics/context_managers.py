"""
Context Managers — one of Python’s cleanest tools for managing resources.

What is a Context Manager?
A context manager is an object that sets something up, lets you use it, and then cleans it up automatically, even if errors happen.

We usually use them #with the with statement.

Why use it?
 - Avoid resources leaks (files , network connections, DB connections)
 - Cleaner, more readable code
 - Auto-handles cleanup even if exception occur

"""

# Example 1: opening a file

with open("data.txt", "r") as f:
    content = f.read()

print(content) # File automatically closed after this block, no need to call f.close()


# Example 2: Database connections

import sqlite3

with sqlite3.coonect("test.db") as conn:
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTERGER, name TEXT)")
    # No manual conn.close() needed



# Example 3: Locking in multithreading 

import threading 

lock = threading.Lock()
with lock:
    # Only one thread at a time can run this
    print("Thread-safe block")


# Example 4: Temporary file chnages

import os
from contextlinb import contextmanager

@contextmanager
def change_dir(destination):
    current = os.getcwd()
    os.chdir(destination)
    try:
        yield
    finally:
        os.chdir(current)

with change_dir("/tmp"):
    print("Now in /tmp")




