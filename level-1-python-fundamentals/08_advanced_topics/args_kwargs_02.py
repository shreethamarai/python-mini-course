
import requests
from pprint import pprint
def make_request(url, *args, **kwargs):
    print("Sending request to:", url)
    response = requests.get(url, *args, **kwargs)
    return response.json()

# Passing keyword args dynamically (headers, timeout, params, etc.,)

data = make_request(
        "https://api.github.com/users/shreethamarai/repos",
        headers = {"Accept": "application/vnd.github.v3+json"},
        timeout = 5
        )


pprint(data[:2])  # print repos
