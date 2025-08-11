from fastapi import FastAPI
import time
import functools

app = FastAPI()

# Decorator
def request_logger(func):
    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        start = time.time()
        result = await func(*args, **kwargs)
        duration = time.time() - start
        print(f"Request handled in {duration:.3f} seconds")
        return result
    return wrapper

# Route
@app.get("/items/")
@request_logger
async def get_items(limit: int = 10):
    return {"items": list(range(1, limit + 1))}

