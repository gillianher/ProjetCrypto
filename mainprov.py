import tkinter as tk
from tkinter import filedialog

class MainMenu:
    def __init__(self, master):
        self.master = master
        self.master.title("Menu Principal")

        self.frame = tk.Frame(master)
        self.frame.pack()

        # Label "Bienvenue"
        self.label_bienvenue = tk.Label(self.frame, text="Bienvenue dans notre application")
        self.label_bienvenue.pack(pady=10)

        # Buttons
        self.button_chiffrer = tk.Button(self.frame, text="Chiffrer", command=self.open_chiffrer_menu)
        self.button_chiffrer.pack(pady=10)

        self.button_dechiffrer = tk.Button(self.frame, text="Déchiffrer", command=self.open_dechiffrer_menu)
        self.button_dechiffrer.pack(pady=10)

    def open_chiffrer_menu(self):
        self.frame.pack_forget()
        ChiffrerMenu(self.master, self.frame)

    def open_dechiffrer_menu(self):
        self.frame.pack_forget()
        DechiffrerMenu(self.master, self.frame)

class ChiffrerMenu:
    def __init__(self, master, previous_frame):
        self.master = master
        self.previous_frame = previous_frame

        self.frame = tk.Frame(master)
        self.frame.pack()

        # Widgets for encryption menu
        self.label_file = tk.Label(self.frame, text="Sélectionnez le fichier à chiffrer:")
        self.label_file.pack(pady=10)

        self.button_browse = tk.Button(self.frame, text="Parcourir", command=self.browse_file)
        self.button_browse.pack(pady=10)

        self.label_method = tk.Label(self.frame, text="Sélectionnez la méthode de chiffrement:")
        self.label_method.pack(pady=10)

        # Dropdown for selecting encryption method
        self.method_var = tk.StringVar(self.frame)
        self.method_var.set("AES")  # Default method
        methods = ["AES", "DES", "RSA"]
        self.method_dropdown = tk.OptionMenu(self.frame, self.method_var, *methods)
        self.method_dropdown.pack(pady=10)

        # Add more widgets for selecting encryption options

        self.button_back = tk.Button(self.frame, text="Retour", command=self.go_back)
        self.button_back.pack(pady=10)

    def browse_file(self):
        file_path = filedialog.askopenfilename()
        # Perform actions with the selected file path (e.g., display it in a label)

    def go_back(self):
        self.frame.pack_forget()
        self.previous_frame.pack()

class DechiffrerMenu:
    def __init__(self, master, previous_frame):
        self.master = master
        self.previous_frame = previous_frame

        self.frame = tk.Frame(master)
        self.frame.pack()

        # Widgets for decryption menu
        self.label_chiff_file = tk.Label(self.frame, text="Sélectionnez le fichier chiffré:")
        self.label_chiff_file.pack(pady=10)

        self.button_browse_chiff = tk.Button(self.frame, text="Parcourir", command=self.browse_chiff_file)
        self.button_browse_chiff.pack(pady=10)

        self.label_key_file = tk.Label(self.frame, text="Sélectionnez le fichier clé de déchiffrement:")
        self.label_key_file.pack(pady=10)

        self.button_browse_key = tk.Button(self.frame, text="Parcourir", command=self.browse_key_file)
        self.button_browse_key.pack(pady=10)

        self.button_back = tk.Button(self.frame, text="Retour", command=self.go_back)
        self.button_back.pack(pady=10)

    def browse_chiff_file(self):
        file_path = filedialog.askopenfilename()
        # Perform actions with the selected file path (e.g., display it in a label)

    def browse_key_file(self):
        key_path = filedialog.askopenfilename()
        # Perform actions with the selected key file path (e.g., display it in a label)

    def go_back(self):
        self.frame.pack_forget()
        self.previous_frame.pack()


if __name__ == "__main__":
    root = tk.Tk()
    app = MainMenu(root)
    root.mainloop()
