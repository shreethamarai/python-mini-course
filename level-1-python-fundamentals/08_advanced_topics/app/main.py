# self-contained FastAPI + decorator test version

from fastapi import FastAPI
import time
import functools
import threading
import uvicorn
import requests

app = FastAPI()

# Decorator
def request_logger(func):
    @functools.wraps(func)  # ✅ Keeps original function signature for FastAPI
    async def wrapper(*args, **kwargs):
        start = time.time()
        result = await func(*args, **kwargs)
        duration = time.time() - start
        print(f"[SERVER] Request handled in {duration:.3f} seconds")
        return result
    return wrapper

# Route
@app.get("/items/")
@request_logger
async def get_items(limit: int = 10):
    return {"items": list(range(1, limit + 1))}

# Function to run the server
def run_server():
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="error")

# Main entry point
if __name__ == "__main__":
    # Start FastAPI server in a separate thread
    server_thread = threading.Thread(target=run_server, daemon=True)
    server_thread.start()

    # Give the server a moment to start
    time.sleep(1)

    # Make request to our own server
    print("[CLIENT] Sending request to API...")
    response = requests.get("http://127.0.0.1:8000/items/?limit=5")

    # Print client response
    print("[CLIENT] Response JSON:", response.json())

    # Keep the server running for a bit to view logs
    time.sleep(1)

