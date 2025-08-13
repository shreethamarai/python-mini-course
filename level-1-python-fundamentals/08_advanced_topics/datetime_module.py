
"""
    datetime module 
"""

""" 
    Logging events with timestamps 
         - Used in Every log entry in systems (apps, servers) needs precise time for debugging & auditing
"""

from datetime import datetime

def log_event(event):
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}]{event}")

log_event("User logged in")
log_event("File uploaded")


""" 
    Scheduling a reminder 
        - Used in apps to send alerts or trigger events after a fixed delay 
"""

from datetime import datetime , timedelta

reminder_time = datetime.now() + timedelta(hours=2)
print("Reminder set for:", reminder_time.strftime("%H:%M:%S"))

# Simulate checking  if reminder time reached
if datetime.now() >= reminder_time:
    print("Time for your reminder!")

# Why useful: Used in apps to send alters or trigger events after fixed delay

""" 
    Calculating expiry dates 
        - Useful in E-commerce, subscriptions, and licenses often need automated expiry tracking
"""

from datetime import datetime, timedelta

purchase_date = datetime(2025,8,13)
warranty_period = timedelta(days=365)
expiry_date = purchase_date + warranty_period

print("Warranty expires on:", expiry_date.strftime("%Y-%m-%d"))

"""
    parsing string to datetime
        - Useful in Convert text data (logs, CSV, API reponses) into actual date objects where you can compare or calculate with.
"""

from datetime import datetime

date_str = "2025-08-13 14:30:00"
dt_obj = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
print("Pared datetime:", dt_obj)



"""
    Timezone-aware operations
        - Essential for apps with global-users to ensure correct time display based on location
"""

from datetime import datetime
from zoneinfo import ZoneInfo

ny_time = datetime.now(ZoneInfo("America/New_York"))
ist_time = ny_time.astimezone(ZoneInfo("Asia/Kolkata"))

print("NY Time:", ny_time.strftime("%Y-%m-%d %H:%M"))
print("IST Time:", ist_time.strftime("%Y-%m-%d %H:%M"))







