import rsa

def encrypt_file(input_file, output_file, public_key):
    chunk_size = 244  # Block size for encryption in bytes (adjust as needed)

    with open(input_file, 'rb') as infile, open(output_file, 'wb') as outfile:
        while True:
            chunk = infile.read(chunk_size)
            if not chunk:
                break
            encrypted_chunk = rsa.encrypt(chunk, public_key)
            outfile.write(encrypted_chunk)
        print("Chiffré")

def decrypt_file(input_file, output_file, private_key):
    chunk_size = 244 # Block size for decryption in bytes (adjust as needed)

    with open(input_file, 'rb') as infile, open(output_file, 'wb') as outfile:
        while True:
            encrypted_chunk = infile.read(chunk_size)
            print("22")
            if not encrypted_chunk:
                break
            decrypted_chunk = rsa.decrypt(encrypted_chunk, private_key)
            print("25")
            outfile.write(decrypted_chunk)
            print("27")

# Génération des clés RSA
publickey, privatekey = rsa.newkeys(2048)

# Sauvegarde des clés dans des fichiers PEM
with open('clepublic.pem', 'wb') as f:
    f.write(publickey.save_pkcs1("PEM"))
#pour chiffr
with open('cleprivate.pem', 'wb') as f:
    f.write(privatekey.save_pkcs1("PEM"))

# Chargement des clés depuis les fichiers PEM
with open('clepublic.pem', 'rb') as f:
    pubkey = rsa.PublicKey.load_pkcs1(f.read())

with open('cleprivate.pem', 'rb') as f:
    privkey = rsa.PrivateKey.load_pkcs1(f.read())

# Entrée du nom du fichier et de l'extension
file = input("Entrez le nom du fichier souhaité: ")
ext = input("Entrez maintenant l'extension du fichier (.png, .mp4, .txt, etc): ")

# Chemins d'entrée et de sortie
file_path = "C:/users/georg/ProjetCrypto/python/" + file + "." + ext
output_path = "C:/users/georg/ProjetCrypto/python/chiffr." + ext

# Chiffrement du fichier
encrypt_file(file_path, output_path, pubkey)

# Déchiffrement du fichier
decrypted_output_path = "C:/users/georg/ProjetCrypto/python/dechiffr." + ext
try:
    decrypt_file(output_path, decrypted_output_path, privkey)
    print("Déchiffrement réussi.")
except rsa.pkcs1.DecryptionError as e:
    print(f"Échec du déchiffrement : {e}")
except Exception as e:
    print(f"Erreur inattendue : {e}")
