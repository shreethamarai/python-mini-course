
from cryptography.fernet import Fernet

# Generate a key and save it securly

key = Fernet.generate_key()
cipher = Fernet(key)


# ENcrypt

with open("secert.txt", "wb") as file:
    file.write(b'THAMARAI KANNAN 007')

with open("secert.txt", "rb") as file:
    data = file.read()

encrypted = cipher.encrypt(data)

with open("secert.encrypted", "wb") as file:
    file.write(encrypted)

# Decrypt (for testing)

with open("secert.encrypted", "rb") as file:
    encrypted_data = file.read()

decrypted = cipher.decrypt(encrypted_data)

print("decrypted content:" , decrypted.decode())
