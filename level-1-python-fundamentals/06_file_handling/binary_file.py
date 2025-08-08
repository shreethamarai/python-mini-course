
with open("binary_sample.bin", "wb") as file:
    file.write(b"This is binary data. ")

with open("binary_sample.bin", "rb") as file:
    content = file.read()
    print("Binary content:", content)
