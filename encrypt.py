from cryptography.fernet import Fernet

# Generate a key and save it in a file
key = Fernet.generate_key()
with open("encryption_key.key", "wb") as key_file:
    key_file.write(key)

# Encrypt files
def encrypt_file(file_name):
    with open("encryption_key.key", "rb") as key_file:
        key = key_file.read()
    fernet = Fernet(key)

    with open(file_name, "rb") as file:
        original_content = file.read()
    encrypted_content = fernet.encrypt(original_content)

    with open(file_name, "wb") as encrypted_file:
        encrypted_file.write(encrypted_content)
    print(f"Encrypted {file_name}")

# List of files to encrypt
files_to_encrypt = ["calculator.py", "message.py"]
for file in files_to_encrypt:
    encrypt_file(file)
