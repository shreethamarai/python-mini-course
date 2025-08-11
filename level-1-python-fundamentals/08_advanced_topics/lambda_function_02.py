from pprint import pprint

users = [
    {"name": "Kannan", "last_login": "2025-08-09"},
    {"name": "Thamarai", "last_login": "2025-08-11"},
    {"name": "Arun", "last_login": "2025-08-10"}
]


# Sort users by last_login date

users.sort(key=lambda x:x["last_login"], reverse = True)
pprint(users)
