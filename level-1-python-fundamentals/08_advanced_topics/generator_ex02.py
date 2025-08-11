"""
Exercise — API Pagination with a Generator
Scenario:
You have an API that returns data in pages. Each page has limit items, and you have to fetch all items without knowing how many pages there are in advance.

Your generator should:

Take base_url and limit as arguments

Request the next page until no more data

Yield each item one at a time (not the whole page)

"""


import requests

def fetch_paginated_data(base_url, limit=10):
    page = 1
    while True:
        response = requests.get(base_url, params={"page":page, "limit":limit})
        data = response.json()

        # Stop if no data
        if not data:
            break

        # Yield items one at a time
        for item in data:
            yield item

        page += 1

# Example usage (this URL is fake for demo)

for product in fetch_paginated_data("https://api.example.com/products", limit = 5):
    print(product)



