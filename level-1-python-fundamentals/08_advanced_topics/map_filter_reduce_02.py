
from functools import reduce

# Simulating API data with mixed values

api_data = ["10", "20", "Invaild", "30", ""]

# Step 1: Convert to integers where possible (Map)
def safe_int(x):
    try:
        return int(x)
    except ValueError:
        return None

numbers = list(map(safe_int, api_data))

# Step 2: Filter out None values
valid_numbers = list(filter(lambda x: x is not None, numbers))

#Step 3: Reduce to find total
total = reduce(lambda x, y : x + y, valid_numbers)

print("Vaild numbers:", valid_numbers)
print("total sum:", total)
