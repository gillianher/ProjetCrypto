import rsa

publickey, privatekey = rsa.newkeys(1024)

with open('clepublic.pem', 'wb') as f:
    f.write(publickey.save_pkcs1("PEM"))

with open('cleprivate.pem', 'wb') as f:
    f.write(privatekey.save_pkcs1("PEM"))

with open('clepublic.pem', 'rb') as f:
    pubkey = rsa.PublicKey.load_pkcs1(f.read())

with open('cleprivate.pem', 'rb') as f:
    privkey = rsa.PrivateKey.load_pkcs1(f.read())

file = input("Entrez le nom du fichier souhaité: ")
ext = input("Entrez maintenant l'extension du fichier (.png, .mp4, .txt, etc): ")

file_path = "C:/xampp/htdocs/ProjetCrypto/python/" + file + "." + ext
with open(file_path, "rb") as f:
    data = f.read()

datachiffr = rsa.encrypt(data, pubkey)

output_path = "C:/xampp/htdocs/ProjetCrypto/python/chiffr." + ext
with open(output_path, "wb") as f:
    f.write(datachiffr)

encrypteddata = open(output_path, "rb").read()

datadech = rsa.decrypt(encrypteddata, privkey)
print(datadech.decode())
