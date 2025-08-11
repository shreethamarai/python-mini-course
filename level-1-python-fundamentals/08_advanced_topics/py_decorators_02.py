
import time 
import functools

def log_execution_time(func):
    @functools.wraps(func) # preserves function metadata
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

@log_execution_time
def fetch_data():
    time.sleep(1)  # simulate delay
    return {"data" : "sample"}

# Run function with timing
result = fetch_data()
