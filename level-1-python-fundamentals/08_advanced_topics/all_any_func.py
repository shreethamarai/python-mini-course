
""" all()
    - returns True only if every element in the iterable is truthy.
    - If even one is False (or falsy like 0, "", None), it returns False.
"""

marks = [80, 90, 85]
print(all(m >= 40 for m in marks)) # True - all above 40

marks = [80, 30, 85]
print(all(m >= 40 for m in marks)) # False - 30 fails

""" any()
    - Returns True if at least one element is truthy.
    - Returns False only if all are falsy
"""
marks = [0, 0, 85]
print(any(m >= 40 for m in marks)) # True - 85 passes

marks = [0, 30, 20]
print(any(m >= 40 for m in marks)) # False - nobody passes


""" Real - world uses
"""

# Form validation
fields = ["John", "Doe", "john@example.com", "password123"]

if all(fields):
    print("Form is complete")
else:
    print("Some fields are empty")

# Secuirty - At least one admin present
roles = ["users", "moderator", "admin"]
if any (role == "admi" for role in roles):
    print("Admin found, allow access")

# Monitoring system health
server_status = [True, True, False]
if all(server_status):
    print("All servers are running")
else:
    print("Some servers are down")

# AI/ML - Model metric checks
accuracy_scores = [0.85, 0.88, 0.90]
if all(score > 0.8 for score in accuracy_scores):
    print("All models meet accuracy target")

# Payment systems - At least one method available
payment_methods = {"credit_card" : False, "paypal":False, "upi": True}
if any(payment_methods.values()):
    print("Payment possible")



