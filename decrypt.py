from cryptography.fernet import Fernet

# Decrypt files
def decrypt_file(file_name):
    with open("encryption_key.key", "rb") as key_file:
        key = key_file.read()
    fernet = Fernet(key)

    with open(file_name, "rb") as encrypted_file:
        encrypted_content = encrypted_file.read()
    decrypted_content = fernet.decrypt(encrypted_content)

    with open(file_name, "wb") as decrypted_file:
        decrypted_file.write(decrypted_content)
    print(f"Decrypted {file_name}")

# List of files to decrypt
files_to_decrypt = ["calculator.py", "message.py"]
for file in files_to_decrypt:
    decrypt_file(file)
