# Importation des modules nécessaires
import tkinter as tk                     # Module principal Tkinter pour créer l'interface graphique
from tkinter import messagebox           # Module pour afficher des boîtes de dialogue (alertes, info, warning)
from tkinter import ttk                  # Module ttk pour des widgets modernes (Treeview, Notebook, etc.)

# -------------------------------
# Fonction appelée par le bouton
# -------------------------------
def afficher_info():
    messagebox.showinfo("Information","Bonjour avec ttk !")  # Affiche une boîte d'information avec un titre et un message

# -------------------------------
# Fenêtre principale
# -------------------------------
fenetre1 = tk.Tk()                        # Création de la fenêtre principale
fenetre1.title("DEV 104")                 # Titre de la fenêtre
fenetre1.geometry("500x200")              # Taille de la fenêtre (largeur x hauteur)
fenetre1.configure(bg="#010101")        # couleur de fond bleu clair
fenetre1.resizable(True, True)            # redimensionnable
# fenetre1.iconbitmap("icone.ico")          # icône de la fenêtre

# -------------------------------
# Label principal
# -------------------------------
label = tk.Label(
    fenetre1,                              # Fenêtre parent
    text="DEV 104",                        # Texte affiché
    font=("Arial", 30, "bold"),            # Police, taille et style
    fg="#010101",                               # Couleur du texte
    bg="white"                             # Couleur de fond
)
label.pack()                               # Placement automatique dans la fenêtre

# -------------------------------
# Bouton avec action
# -------------------------------
button1 = tk.Button(
    fenetre1,                              # Fenêtre parent
    text="Cliquez-moi",                     # Texte du bouton
    font=("Arial", 10, "bold"),            # Police et style
    width=15,                               # Largeur du bouton (en caractères)
    height=2,                               # Hauteur du bouton (en lignes)
    activebackground="Blue",                # Couleur de fond quand le bouton est pressé ou survolé
    cursor="hand2",                         # Curseur au survol (main)
    bd=14,                                  # Largeur de la bordure
    command=afficher_info                    # Fonction appelée au clic
)
button1.pack()                             # Placement du bouton

# -------------------------------
# Champ de saisie (Entry)
# -------------------------------
txt1 = tk.Entry(
    fenetre1,                               # Fenêtre parent
    width=40,                               # Largeur du champ
    show="",                                # Masque du texte ("" = visible, "*" = mot de passe)
    state="normal",                         # Etat du champ : normal (modifiable)
    justify="left"                          # Alignement du texte à gauche
)
txt1.pack()                                # Placement du champ

# -------------------------------
# Frame avec Label et Entry
# -------------------------------
frame = tk.Frame(fenetre1, bg="Red")      # Création d'un conteneur (Frame) avec fond rouge
frame.pack()                               # Placement du frame

tk.Label(frame, text="Utilisateur").pack(side="left")  # Label à l'intérieur du frame, aligné à gauche
tk.Entry(frame).pack(side="left")                      # Champ de saisie à côté du Label

# -------------------------------
# Listbox (liste simple)
# -------------------------------
listbox = tk.Listbox(fenetre1)             # Création d'une liste
listbox.pack()                             # Placement dans la fenêtre
listbox.insert(1, "Livre 1")              # Ajouter un élément à la liste (indice 1)
listbox.insert(2, "Livre 2")              # Ajouter un deuxième élément (indice 2)


# -------------------------------
# Combo box
# -------------------------------
combo = ttk.Combobox(fenetre1)
combo["values"]=("Python","Java","PHP")
combo.config(state="readonly")
combo.current(0)
combo.pack()

# -------------------------------
# Radio button
# -------------------------------
rd1 = tk.Radiobutton(fenetre1, text="Radio 1", value="Radio 1")
rd1.pack()
rd2 = tk.Radiobutton(fenetre1, text="Radio 2", value="Radio 2")
rd2.pack()


# -------------------------------
# Treeview (tableau)
# -------------------------------
tree = ttk.Treeview(
    fenetre1,
    columns=("Titre", "Auteur"),           # Colonnes définies
    show="headings"                        # Affiche uniquement les colonnes, pas la colonne #0
)
tree.heading("Titre", text="Titre")        # Définition de l'en-tête de la colonne "Titre"
tree.heading("Auteur", text="Auteur")      # Définition de l'en-tête de la colonne "Auteur"
tree.pack()                                # Placement du tableau

# Ajouter des lignes au Treeview
tree.insert("", "end", values=("Python 101", "Alice"))
tree.insert("", "end", values=("Java 101", "Bob"))

# -------------------------------
# Notebook (onglets)
# -------------------------------
notebook = ttk.Notebook(fenetre1)          # Création d'un widget Notebook (onglets)
tab1 = ttk.Frame(notebook)                 # Création du premier onglet (frame)
tab2 = ttk.Frame(notebook)                 # Création du deuxième onglet (frame)
notebook.add(tab1, text="Gestion")         # Ajouter le premier onglet avec texte "Gestion"
notebook.add(tab2, text="Liste")           # Ajouter le deuxième onglet avec texte "Liste"
notebook.pack(expand=True, fill="both")    # Placement du notebook : occupe tout l'espace

# Ajouter du contenu dans chaque onglet
tk.Label(tab1, text="Onglet Gestion").pack()  # Label dans le premier onglet
tk.Label(tab2, text="Onglet Liste").pack()    # Label dans le deuxième onglet

# -------------------------------
# Lancer la boucle principale
# -------------------------------
fenetre1.mainloop()                         # Démarre l'application et attend les interactions utilisateur
