
with open("demo.txt", "a") as file:
    file.write(" This line was appended. \n")

with open("demo.txt", "r") as file:
    for line in file:
        print("Line:", line.strip())

