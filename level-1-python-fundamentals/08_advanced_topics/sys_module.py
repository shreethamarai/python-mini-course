"""
    sys module - Python runtime info & control
"""

import sys

# Command-line arguments - CLI tools, automation scripts with dynamic inputs
# run: python3 script.py arg1 arg2
print(sys.argv)     # {"script.py", "arg1", "arg2"]

# Existing scripts - Fail gracefully when required inputs are missing
if len(sys.argv) < 2:
    print("Missing arguments")
    sys.exit(1) # exit with error code

# Python version check - Ensures compatibility for your code
print(sys.version)
if sys.version_info < (3,8):
    print("Upgrade Python")

# Redirecting output - Logging to files, avioding print overhead
sys.stdout.write("Custom output without print() \n")


