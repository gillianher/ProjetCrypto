import tkinter as tk
from tkinter import filedialog
import tpchiffraes

def select_file(entry_var):
    file_path = filedialog.askopenfilename()
    entry_var.set(file_path)

def select_folder(entry_var):
    folder_path = filedialog.askdirectory()
    entry_var.set(folder_path)

def encrypt_file():
    # Logique de chiffrement ici
    selected_method = encryption_method_var.get()
    encfilepath= str(encrypted_folder_var.get())+"/"+str(encrypted_file_var.get())
    decfilepath=str(decrypted_folder_var.get())+"/"+str(decrypted_file_var.get())
    if (selected_method=="Symétrique"):
        tpchiffraes.chiffraes(file_var.get(),encrypted_file_var.get(),decrypted_file_var.get(),encfilepath,decfilepath)
       
def decrypt_file():
    # Logique de déchiffrement ici
    pass

def encryption_method_changed(event):
    selected_method = encryption_method_var.get()
    print(f"Sélection de méthode de chiffrement : {selected_method}")

# Création de la fenêtre principale
window = tk.Tk()
window.title("Application de Chiffrement")

# Variables pour stocker les chemins et noms de fichiers
file_var = tk.StringVar()
encrypted_file_var = tk.StringVar()
decrypted_file_var = tk.StringVar()
encrypted_folder_var = tk.StringVar()
decrypted_folder_var = tk.StringVar()

# Cadre principal
frame = tk.Frame(window, padx=10, pady=10)
frame.pack()

# Sélection de fichier
file_label = tk.Label(frame, text="Sélectionnez un fichier:")
file_label.grid(row=0, column=0, sticky="w")

file_entry = tk.Entry(frame, textvariable=file_var, width=40)
file_entry.grid(row=0, column=1, padx=5, pady=5)

file_button = tk.Button(frame, text="Parcourir", command=lambda: select_file(file_var))
file_button.grid(row=0, column=2)

# Nom du fichier chiffré
encrypted_file_label = tk.Label(frame, text="Nom du fichier chiffré:")
encrypted_file_label.grid(row=1, column=0, sticky="w")

encrypted_file_entry = tk.Entry(frame, textvariable=encrypted_file_var, width=40)
encrypted_file_entry.grid(row=1, column=1, padx=5, pady=5)

# Chemin du fichier chiffré
encrypted_file_path_label = tk.Label(frame, text="Chemin du fichier chiffré:")
encrypted_file_path_label.grid(row=2, column=0, sticky="w")

encrypted_file_folder_entry = tk.Entry(frame, textvariable=encrypted_folder_var, width=30)
encrypted_file_folder_entry.grid(row=2, column=1, padx=5, pady=5)

encrypted_file_folder_button = tk.Button(frame, text="Parcourir", command=lambda: select_folder(encrypted_folder_var))
encrypted_file_folder_button.grid(row=2, column=2)

# Nom du fichier déchiffré
decrypted_file_label = tk.Label(frame, text="Nom du fichier déchiffré:")
decrypted_file_label.grid(row=3, column=0, sticky="w")

decrypted_file_entry = tk.Entry(frame, textvariable=decrypted_file_var, width=40)
decrypted_file_entry.grid(row=3, column=1, padx=5, pady=5)

# Chemin du fichier déchiffré
decrypted_file_path_label = tk.Label(frame, text="Chemin du fichier déchiffré:")
decrypted_file_path_label.grid(row=4, column=0, sticky="w")

decrypted_file_folder_entry = tk.Entry(frame, textvariable=decrypted_folder_var, width=30)
decrypted_file_folder_entry.grid(row=4, column=1, padx=5, pady=5)

decrypted_file_folder_button = tk.Button(frame, text="Parcourir", command=lambda: select_folder(decrypted_folder_var))
decrypted_file_folder_button.grid(row=4, column=2)

# Menu déroulant pour la méthode de chiffrement
encryption_method_var = tk.StringVar()
encryption_method_var.set("Symétrique")  # Valeur par défaut

encryption_method_label = tk.Label(frame, text="Méthode de chiffrement:")
encryption_method_label.grid(row=5, column=0, sticky="w")

encryption_method_menu = tk.OptionMenu(frame, encryption_method_var, "Symétrique", "Asymétrique")
encryption_method_menu.grid(row=5, column=1, padx=5, pady=5)
encryption_method_menu.bind("<Configure>", encryption_method_changed)

# Boutons d'action
encrypt_button = tk.Button(frame, text="Chiffrer", command=encrypt_file)
encrypt_button.grid(row=6, column=0, pady=10)

decrypt_button = tk.Button(frame, text="Déchiffrer", command=decrypt_file)
decrypt_button.grid(row=6, column=1, pady=10)

# Lancer la boucle principale de l'application
window.mainloop()
