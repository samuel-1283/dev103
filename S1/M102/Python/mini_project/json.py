import json
import os

# Nom du fichier JSON
FICHIER_JSON = "catalogue_produits.json"

def charger_catalogue():
    """Charge le catalogue depuis le fichier JSON."""
    if os.path.exists(FICHIER_JSON):
        try:
            with open(FICHIER_JSON, 'r', encoding='utf-8') as f:
                return json.load(f)
        except json.JSONDecodeError:
            print("⚠️  Erreur de lecture du fichier. Création d'un nouveau catalogue.")
            return []
    else:
        print("ℹ️  Aucun catalogue existant. Création d'un nouveau catalogue.")
        return []

def sauvegarder_catalogue(catalogue):
    """Sauvegarde le catalogue dans le fichier JSON."""
    with open(FICHIER_JSON, 'w', encoding='utf-8') as f:
        json.dump(catalogue, f, ensure_ascii=False, indent=2)
    print("✅ Catalogue sauvegardé avec succès!")

def generer_id(catalogue):
    """Génère un nouvel ID unique pour un produit."""
    if not catalogue:
        return 1
    return max(produit['id'] for produit in catalogue) + 1

def ajouter_produit(catalogue):
    """Ajoute un nouveau produit au catalogue."""
    print("\n=== AJOUTER UN PRODUIT ===")
    
    nom = input("Nom du produit : ").strip()
    if not nom:
        print("❌ Le nom ne peut pas être vide.")
        return
    
    try:
        prix = float(input("Prix (DH) : "))
        if prix < 0:
            print("❌ Le prix ne peut pas être négatif.")
            return
    except ValueError:
        print("❌ Prix invalide.")
        return
    
    try:
        quantite = int(input("Quantité en stock : "))
        if quantite < 0:
            print("❌ La quantité ne peut pas être négative.")
            return
    except ValueError:
        print("❌ Quantité invalide.")
        return
    
    categorie = input("Catégorie : ").strip()
    
    nouveau_produit = {
        'id': generer_id(catalogue),
        'nom': nom,
        'prix': prix,
        'quantite': quantite,
        'categorie': categorie
    }
    
    catalogue.append(nouveau_produit)
    print(f"✅ Produit ajouté avec l'ID {nouveau_produit['id']}")

def rechercher_produit(catalogue):
    """Recherche un produit par ID ou nom."""
    print("\n=== RECHERCHER UN PRODUIT ===")
    print("1. Rechercher par ID")
    print("2. Rechercher par nom")
    
    choix = input("Votre choix : ").strip()
    
    if choix == '1':
        try:
            id_recherche = int(input("ID du produit : "))
            resultats = [p for p in catalogue if p['id'] == id_recherche]
        except ValueError:
            print("❌ ID invalide.")
            return
    elif choix == '2':
        nom_recherche = input("Nom du produit (ou partie du nom) : ").strip().lower()
        resultats = [p for p in catalogue if nom_recherche in p['nom'].lower()]
    else:
        print("❌ Choix invalide.")
        return
    
    if resultats:
        print(f"\n🔍 {len(resultats)} produit(s) trouvé(s) :")
        afficher_produits(resultats)
    else:
        print("❌ Aucun produit trouvé.")

def afficher_produits(produits):
    """Affiche une liste de produits."""
    print("\n" + "="*80)
    for p in produits:
        print(f"ID: {p['id']} | Nom: {p['nom']} | Prix: {p['prix']} DH | "
              f"Quantité: {p['quantite']} | Catégorie: {p['categorie']}")
    print("="*80)

def modifier_produit(catalogue):
    """Modifie les informations d'un produit."""
    print("\n=== MODIFIER UN PRODUIT ===")
    
    try:
        id_produit = int(input("ID du produit à modifier : "))
    except ValueError:
        print("❌ ID invalide.")
        return
    
    produit = next((p for p in catalogue if p['id'] == id_produit), None)
    
    if not produit:
        print("❌ Produit non trouvé.")
        return
    
    print("\nProduit actuel :")
    afficher_produits([produit])
    
    print("\n(Laissez vide pour conserver la valeur actuelle)")
    
    nom = input(f"Nouveau nom [{produit['nom']}] : ").strip()
    if nom:
        produit['nom'] = nom
    
    prix_str = input(f"Nouveau prix [{produit['prix']}] : ").strip()
    if prix_str:
        try:
            prix = float(prix_str)
            if prix >= 0:
                produit['prix'] = prix
            else:
                print("⚠️  Prix négatif ignoré.")
        except ValueError:
            print("⚠️  Prix invalide ignoré.")
    
    quantite_str = input(f"Nouvelle quantité [{produit['quantite']}] : ").strip()
    if quantite_str:
        try:
            quantite = int(quantite_str)
            if quantite >= 0:
                produit['quantite'] = quantite
            else:
                print("⚠️  Quantité négative ignorée.")
        except ValueError:
            print("⚠️  Quantité invalide ignorée.")
    
    categorie = input(f"Nouvelle catégorie [{produit['categorie']}] : ").strip()
    if categorie:
        produit['categorie'] = categorie
    
    print("✅ Produit modifié avec succès!")

def supprimer_produit(catalogue):
    """Supprime un produit du catalogue."""
    print("\n=== SUPPRIMER UN PRODUIT ===")
    
    try:
        id_produit = int(input("ID du produit à supprimer : "))
    except ValueError:
        print("❌ ID invalide.")
        return
    
    produit = next((p for p in catalogue if p['id'] == id_produit), None)
    if not produit:
        print("❌ Produit non trouvé.")
        return
    
    print("\nProduit à supprimer :")
    afficher_produits([produit])
    
    confirmation = input("Confirmer la suppression ? (o/n) : ").strip().lower()
    
    if confirmation == 'o':
        catalogue.remove(produit)
        print("✅ Produit supprimé avec succès!")
    else:
        print("❌ Suppression annulée.")

def afficher_catalogue(catalogue):
    """Affiche tous les produits du catalogue."""
    if not catalogue:
        print("\n📦 Le catalogue est vide.")
    else:
        print(f"\n📦 CATALOGUE ({len(catalogue)} produit(s)) :")
        afficher_produits(catalogue)

def afficher_menu():
    """Affiche le menu principal."""
    print("\n" + "="*50)
    print("🛒  GESTION DE CATALOGUE DE PRODUITS")
    print("="*50)
    print("1. Afficher le catalogue")
    print("2. Ajouter un produit")
    print("3. Rechercher un produit")
    print("4. Modifier un produit")
    print("5. Supprimer un produit")
    print("6. Sauvegarder et quitter")
    print("="*50)

def main():
    """Fonction principale du programme."""
    catalogue = charger_catalogue()
    
    while True:
        afficher_menu()
        choix = input("Votre choix : ").strip()
        
        if choix == '1':
            afficher_catalogue(catalogue)
        elif choix == '2':
            ajouter_produit(catalogue)
        elif choix == '3':
            rechercher_produit(catalogue)
        elif choix == '4':
            modifier_produit(catalogue)
        elif choix == '5':
            supprimer_produit(catalogue)
        elif choix == '6':
            sauvegarder_catalogue(catalogue)
            print("👋 Au revoir!")
            break
        else:
            print("❌ Choix invalide. Veuillez réessayer.")

if __name__ == "__main__":
    main()