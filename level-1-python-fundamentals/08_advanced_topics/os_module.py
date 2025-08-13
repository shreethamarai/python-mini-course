"""
    os modules - Working with operating system
"""
import os

### File & folder operations - Automated file management, cleaning temp files
print(os.system("pwd"))
if 'data' in os.listdir():
    os.system("rm -r data")
    print("folder existed, deleted")
os.mkdir("data")    # Create folder
os.listdir(".")     # List files in current folder
os.system("touch ./old.txt")
os.remove("old.txt")    # Delete file

### Environment variable - Store secrets securly (e.g DB passwords, API keys)
os.environ["API_KEY"] = "12345"
print("API key:", os.environ.get("API_KEY"))

### Running system commands - Automation scripts, DevOps tasks
os.system("python3 ./math_module.py")

### Path management (croos-platform) - Avoid hardcoding / or \ for portability
path = os.path.join("folder", "file.txt")
print(path)


