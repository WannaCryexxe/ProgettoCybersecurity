import os
from cryptography.fernet import Fernet

def load_key():
    return open("key.key", "rb").read()

def decrypt_file(file_path, key):
    cipher_suite = Fernet(key)
    with open(file_path, "rb") as file:
        encrypted_data = file.read()
    decrypted_data = cipher_suite.decrypt(encrypted_data)
    original_file_path = file_path.replace(".encrypted", "")
    with open(original_file_path, "wb") as file:
        file.write(decrypted_data)
    os.remove(file_path)

def simulate_decryption(directory):
    key = load_key()
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".encrypted"):
                file_path = os.path.join(root, file)
                decrypt_file(file_path, key)

# Esegui la simulazione di decrittazione su una directory di test
test_directory = "C:\\Test"
simulate_decryption(test_directory)
