#realiser par badreddine ejjebli
tuple_annonce = ()
liste_annonce = []

def ajouter_annonce():
    id = input("Id de l'annonce : ")
    titre = input("Titre de l'annonce : ")
    entreprise = input("Entreprise : ")
    ville = input("Ville : ")
    salaire = input("Salaire : ")
    annonce = (id, titre, entreprise, ville, salaire)
    liste_annonce.append(annonce)
    print("Annonce ajoutée avec succès.")

def afficher_annonce():
    for annonce in liste_annonce:
        print(annonce)

def rechercher_annonce():
    recherche = input("veuillez saisir l'id de l'annonce : ")
    for annonce in liste_annonce:
        if recherche in annonce:
            print(annonce)
            break
        else:
            print("Aucune annonce trouvée.")
            break
def afficher_la_meilleure_offre():
    for annonce in liste_annonce:
        if annonce[4] == max(liste_annonce[4]):
            print(annonce)
def afficher_statistiques():
    for annonce in liste_annonce:
        print(annonce)
    print("Nombre d'annonces : ", len(liste_annonce))
def supprimer_annonce():
    id = input("Id de l'annonce : ")
    for annonce in liste_annonce:
        if id in annonce:
            liste_annonce.remove(annonce)
            break
        else:
            print("Aucune annonce trouvée.")
            break
while True:
    print("""
    ====================Menu=======================
       1. Ajouter une annonce
       2. Afficher toutes les annonces disponibles
       3. Rechercher une annonce
       4. Afficher la meilleure offre
       5. Afficher des statistiques
       6. Supprimer une annonce
       7. Quitter
    ===============================================""")
    choix = input("Choisissez une option : ")
    if choix == "1":
        ajouter_annonce()
    elif choix == "2":
        afficher_annonce()
    elif choix == "3":
        rechercher_annonce()
    elif choix == "4":
        afficher_la_meilleure_offre()
    elif choix == "5":
        afficher_statistiques()
    elif choix == "6":
        supprimer_annonce()
    elif choix == "7":
        break
    else:
        print("Option invalide. Veuillez choisir une option valide.")