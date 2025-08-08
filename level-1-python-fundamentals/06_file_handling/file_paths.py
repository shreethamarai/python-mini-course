
import os

current_dir = os.getcwd()
file_path = os.path.join(current_dir, "demo.txt")

print("File path:", file_path)

#Open file using the absolute path

with open(file_path,"r") as file:
    print(file.read())

