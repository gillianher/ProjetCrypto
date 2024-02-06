import tkinter as tk
from tkinter import filedialog
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, DES, DES3, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP, AES
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import scrypt
from Crypto.Util.Padding import pad, unpad
from cryptography.fernet import Fernet

#fonctions
def encrypt_file(filename, method):
    key = None
    cipher = None
    file = None
    encrypted_file = None
    
    if method == "AES":
        key = get_random_bytes(16)
        cipher = AES.new(key, AES.MODE_CBC)
    elif method == "DES":
        key = get_random_bytes(8)
        cipher = DES.new(key, DES.MODE_CBC)
    elif method == "RSA":
        key = RSA.generate(2048)
        cipher = PKCS1_OAEP.new(key)

    with open('mykey.key', 'wb') as filekey:
        filekey.write(key)

    with open(filename, 'rb') as file:
        original = file.read()
    
    encrypted_file = cipher.encrypt(pad(original, cipher.block_size))

    with open('encrypted_file.txt', 'wb') as file:
        file.write(encrypted_file)

def select_file(entry_var):
    file_path = filedialog.askopenfilename()
    entry_var.set(file_path)

def select_folder(entry_var):
    folder_path = filedialog.askdirectory()
    entry_var.set(folder_path)

#tkinter
def open_chiffrer_menu():
    frame.grid_forget()
    chiffrer_menu()

def open_dechiffrer_menu():
    frame.grid_forget()
    dechiffrer_menu()

def chiffrer_menu():
    file_var = tk.StringVar()

    # Widgets for encryption menu
    label_file = tk.Label(root, text="Sélectionnez le fichier à chiffrer:")
    label_file.grid(row=0, column=0, pady=10)

    button_browse = tk.Button(root, text="Parcourir", command=lambda: select_file(file_var))
    button_browse.grid(row=0, column=2, pady=10, padx=10)

    # Entry with the file value (row 0, column 1)
    fich_val = tk.Entry(root, textvariable=file_var, width=30)
    fich_val.grid(row=0, column=1)

    label_method = tk.Label(root, text="Sélectionnez la méthode de chiffrement:")
    label_method.grid(row=2, column=0, pady=10)

    # Dropdown for selecting encryption method
    method_var = tk.StringVar(root)
    method_var.set("AES")  # Default method
    methods = ["AES", "DES", "RSA"]
    method_dropdown = tk.OptionMenu(root, method_var, *methods)
    method_dropdown.grid(row=2, column=1, pady=10)

    button_encrypt = tk.Button(root, text="Chiffrer", command=lambda: encrypt_file(file_var.get(), method_var.get()))
    button_encrypt.grid(row=3, column=0, pady=10)

    button_back = tk.Button(root, text="Retour", command=go_back)
    button_back.grid(row=4, column=0, pady=10)


def dechiffrer_menu():
    # Widgets for decryption menu
    label_chiff_file = tk.Label(root, text="Sélectionnez le fichier chiffré:")
    label_chiff_file.grid(row=0, column=0, pady=10)

    button_browse_chiff = tk.Button(root, text="Parcourir", command=browse_chiff_file)
    button_browse_chiff.grid(row=1, column=0, pady=10)

    label_key_file = tk.Label(root, text="Sélectionnez le fichier clé de déchiffrement:")
    label_key_file.grid(row=2, column=0, pady=10)

    button_browse_key = tk.Button(root, text="Parcourir", command=browse_key_file)
    button_browse_key.grid(row=3, column=0, pady=10)

    button_decrypt = tk.Button(root, text="Déchiffrer", command=lambda: decrypt_file(chiff_file_var.get(), key_file_var.get()))
    button_decrypt.grid(row=4, column=0, pady=10)

    button_back = tk.Button(root, text="Retour", command=go_back)
    button_back.grid(row=5, column=0, pady=10)

def browse_chiff_file():
    file_path = filedialog.askopenfilename()
    # Perform actions with the selected file path (e.g., display it in a label)

def browse_key_file():
    key_path = filedialog.askopenfilename()
    # Perform actions with the selected key file path (e.g., display it in a label)

def decrypt_file(encrypted_file, key_file):
    pass

def go_back():
    frame.grid(row=0, column=0)

if __name__ == "__main__":
    root = tk.Tk()
    frame = tk.Frame(root)
    frame.grid(row=0, column=0)

    label_bienvenue = tk.Label(frame, text="Bienvenue sur notre application")
    label_bienvenue.grid(row=0, column=1, pady=10)

    button_chiffrer = tk.Button(frame, text="Chiffrer", command=open_chiffrer_menu)
    button_chiffrer.grid(row=1, column=0, pady=10, padx=10)

    button_dechiffrer = tk.Button(frame, text="Déchiffrer", command=open_dechiffrer_menu)
    button_dechiffrer.grid(row=1, column=2, pady=10, padx=10)

    root.mainloop()
