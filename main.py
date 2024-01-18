from cryptography.fernet import Fernet

# Générer la clé
key = Fernet.generate_key()
fernetAlgo = Fernet(key)

# Enregistrer la clé dans un fichier
with open('mykey.key', 'wb') as filekey:
    filekey.write(key)

# Ouvrir le fichier à chiffrer
with open('test.txt', 'rb') as file:
    original = file.read()

# Chiffrer le fichier
encryptedFile = fernetAlgo.encrypt(original)
with open('testCrypt.txt', 'wb') as encrypted_file:
    encrypted_file.write(encryptedFile)

# Lire la clé depuis le fichier
with open('mykey.key', 'rb') as filekeyD:
    keyD = filekeyD.read()

fernetDe = Fernet(keyD)

# Décrypter le fichier
with open('testCrypt.txt', 'rb') as enc_file:
    encrypted = enc_file.read()

decrypted = fernetDe.decrypt(encrypted)
with open('testDecrypt.txt', 'wb') as dec_file:
    dec_file.write(decrypted)
