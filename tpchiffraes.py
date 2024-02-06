from cryptography.fernet import Fernet


def chiffraes(file,encfile,encpath):
# Générer la clé
    key = Fernet.generate_key()
    fernetAlgo = Fernet(key)

# Enregistrer la clé dans un fichier
    with open('mykey.key', 'wb') as filekey:
        filekey.write(key)
        print("Clé enregistrée")
        # Ouvrir le fichier à chiffrer
        with open(file, 'rb') as file:
            original = file.read()
    print("fichier texte ouvert")
    # Chiffrer le fichier
    encryptedFile = fernetAlgo.encrypt(original)
    with open(encfile, 'wb') as encrypted_file:
        encrypted_file.write(encryptedFile)
        print("fichier chiffré")
def decaes(fileenc,decpath,mail):
# Lire la clé depuis le fichier
    with open('mykey.key', 'rb') as filekeyD:
        keyD = filekeyD.read()
    
        fernetDe = Fernet(keyD)
        print("clé lue")
        # Décrypter le fichier
        with open(fileenc, 'rb') as enc_file:
            encrypted = enc_file.read()
            print("fichier decrypté")
            decrypted = fernetDe.decrypt(encrypted)
            with open(decfile, 'wb') as dec_file:
                dec_file.write(decrypted)
