import json

with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)
# les fonctions 
def ajouter():
    id = int(input("Entrer l'id de produit :"))
    nom = str(input("Entrer le nom de produit :"))
    data["id"] = id
    data["nom"] = nom
    print("le produit a ete ajoute.")

def rechercher():
    cle = input("Entrer l'id ou le nom de produit :")
    if data["id"] == cle or data["nom"] == cle :
        print("Produit trouvé :")
        print(data)

def modifier():
    cle1 = input("Entrer l'id ou le nom de produit :")
    if data["id"] == cle1 or data["nom"] == cle1 :
        id2 = int(input("Entrer le nouveau id de produit :"))
        nom2 = str(input("Entrer le nouveau nom de produit :"))
        data["id"] = id2
        data["nom"] = nom2
        print("le produit a ete modifie.")

def supprimer():
    cle2 = input("Entrer l'id ou le nom de produit vous pouvez supprimer :")
    if data["id"] == cle2 or data["nom"] == cle2 :
        del data[cle2]
        print("le produit a ete supprimer.")
def afficher():
    print(data)
while True:
    print("""
    ======================= Gestion de Catalogue des produits =======================
                1. Ajouter un livre 
                2. Rechercher un livre par id ou nom
                3. Modifier les informations d'un livre 
                4. Supprimer un livre
                5. Afficher tous les livres
                0. Quitter
    =================================================================================""")
    choix = int(input("Votre choix :"))
    if choix == 1:
        ajouter()
    elif choix == 2:
        rechercher()
    elif choix == 3:
        modifier()
    elif choix == 4:
        supprimer()
    elif choix == 5:
        afficher()
    elif choix == 0:
        print("Au revoir!")
        break
    else:
        print("Choix invalide!")
