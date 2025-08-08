import requests

response = requests.get("https://api.github.com")
print("GitHub API Status Code:", response.status_code)

