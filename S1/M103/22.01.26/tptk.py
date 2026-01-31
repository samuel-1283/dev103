import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import random


def afficher():
    texte = Entry.get()
    if texte:
        messagebox.showinfo("Information", f"Texte saisi : {texte}")
    else:
        messagebox.showwarning("Attention", "Veuillez saisir du texte !")

def change_bgcolor():
    colors = ["lightgreen", "white", "lightpink", "lightgray", "blue", "lightcyan"]
    root.configure(bg=colors[random.randint(0, len(colors) - 1)])
    
root = tk.Tk()
root.title("Ttk Example")
root.geometry("600x400")
root.configure(bg="lightblue")
root.resizable(False, True)
root.minsize(400, 300)
root.maxsize(800, 600)
# root.iconbitmap("icon.ico")
root.attributes('-alpha', 0.95) 
root.attributes('-topmost', True)
root.config(cursor="hand2")

default_font = ("Arial", 12)
default_fg = "blue"
default_bg = "#f0f0f0"

style = ttk.Style()
style.configure(".", font=default_font, foreground=default_fg, background=default_bg)

label = tk.Label(
    root,
    text="Bienvenue au TP Tkinter",
    font=("Arial", 16, "bold"),
    fg=default_fg,
    bg="lightblue"
)
label.pack(pady=10)
Entry = tk.Entry(
    root,
    width=50
)
Entry.pack(pady=10)
btn1 = tk.Button(
    root,
    text="Afficher",
    font=("Arial", 8, "bold"),
    width=10,
    height=2,
    activebackground="green",
    cursor="hand2",
    bd=5,
    command=afficher)
btn1.pack(pady=10)

btn2 = tk.Button(
    root,
    text="Changer Couleur",
    font=("Arial", 8, "bold"),
    width=12,
    height=2,
    activebackground="green",
    cursor="hand2",
    bd=5,
    command=change_bgcolor)
btn2.pack(pady=10)

frame = ttk.Frame(root, 
    padding=10,
    borderwidth=5,
    relief="ridge"
)
frame_label = ttk.Label(
    frame,
    text="Utilisateur",
    font=("Arial", 14, "bold")
)
frame_entry = ttk.Entry(
    frame,
    width=30
)
frame_entry.pack(side="right", pady=10)
frame_label.pack(pady=10)
frame.pack(pady=10)
listbox = tk.Listbox(root)
listbox.pack()
listbox.insert(1, "Livre 1")
listbox.insert(2, "Livre 2")
listbox.insert(3, "Livre 3")

tree = ttk.Treeview(
    root,
    columns=("Titre", "Auteur"),           # Colonnes définies
    show="headings"                        # Affiche uniquement les colonnes, pas la colonne #0
)
tree.heading("Titre", text="Titre")        # Définition de l'en-tête de la colonne "Titre"
tree.heading("Auteur", text="Auteur")      # Définition de l'en-tête de la colonne "Auteur"
tree.pack()                                # Placement du tableau

# Ajouter des lignes au Treeview
tree.insert("", "end", values=("titre1", "auteur1"))
tree.insert("", "end", values=("titre2", "auteur2"))
notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill="both")
tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)
notebook.add(tab1, text="Gestion")
notebook.add(tab2, text="Liste")
tk.Label(tab1, text="Onglet Gestion").pack()
tk.Label(tab2, text="Onglet Liste").pack()





root.mainloop()