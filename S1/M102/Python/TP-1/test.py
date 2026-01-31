import csv
import os
from typing import List, Dict, Optional

class GestionInventaire:
    def __init__(self, fichier_csv: str = "inventaire.csv"):
        self.fichier_csv = fichier_csv
        self.colonnes = ["Code", "Nom", "Catégorie", "Quantité", "PrixUnitaire"]
        self.creer_fichier_si_inexistant()
    
    def creer_fichier_si_inexistant(self):
        """Crée le fichier CSV s'il n'existe pas"""
        if not os.path.exists(self.fichier_csv):
            with open(self.fichier_csv, 'w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=self.colonnes)
                writer.writeheader()
            print(f"✓ Fichier '{self.fichier_csv}' créé avec succès.")
    
    def lire_inventaire(self) -> List[Dict]:
        """Lit et retourne tous les produits de l'inventaire"""
        produits = []
        with open(self.fichier_csv, 'r', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                produits.append(row)
        return produits
    
    def ecrire_inventaire(self, produits: List[Dict]):
        """Écrit la liste de produits dans le fichier CSV"""
        with open(self.fichier_csv, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=self.colonnes)
            writer.writeheader()
            writer.writerows(produits)
    
    def afficher_produits(self, produits: Optional[List[Dict]] = None):
        """Affiche la liste des produits"""
        if produits is None:
            produits = self.lire_inventaire()
        
        if not produits:
            print("\n❌ Aucun produit dans l'inventaire.")
            return
        
        print("\n" + "="*90)
        print(f"{'Code':<10} {'Nom':<20} {'Catégorie':<15} {'Quantité':<10} {'Prix Unit.':<10}")
        print("="*90)
        
        for p in produits:
            print(f"{p['Code']:<10} {p['Nom']:<20} {p['Catégorie']:<15} "
                  f"{p['Quantité']:<10} {float(p['PrixUnitaire']):<10.2f}")
        print("="*90)
        print(f"Total: {len(produits)} produit(s)\n")
    
    def ajouter_produit(self, code: str, nom: str, categorie: str, 
                        quantite: int, prix_unitaire: float):
        """Ajoute un nouveau produit à l'inventaire"""
        produits = self.lire_inventaire()
        
        # Vérifier si le code existe déjà
        if any(p['Code'] == code for p in produits):
            print(f"❌ Erreur: Le code '{code}' existe déjà.")
            return False
        
        nouveau_produit = {
            'Code': code,
            'Nom': nom,
            'Catégorie': categorie,
            'Quantité': str(quantite),
            'PrixUnitaire': str(prix_unitaire)
        }
        
        produits.append(nouveau_produit)
        self.ecrire_inventaire(produits)
        print(f"✓ Produit '{nom}' ajouté avec succès.")
        return True
    
    def mettre_a_jour_quantite(self, code: str, modification: int):
        """Met à jour la quantité d'un produit (positive ou négative)"""
        produits = self.lire_inventaire()
        
        for p in produits:
            if p['Code'] == code:
                ancienne_qte = int(p['Quantité'])
                nouvelle_qte = ancienne_qte + modification
                
                if nouvelle_qte < 0:
                    print(f"❌ Erreur: Quantité insuffisante (actuelle: {ancienne_qte}).")
                    return False
                
                p['Quantité'] = str(nouvelle_qte)
                self.ecrire_inventaire(produits)
                print(f"✓ Quantité mise à jour: {ancienne_qte} → {nouvelle_qte}")
                return True
        
        print(f"❌ Produit avec le code '{code}' introuvable.")
        return False
    
    def modifier_produit(self, code: str, **modifications):
        """Modifie les attributs d'un produit existant"""
        produits = self.lire_inventaire()
        
        for p in produits:
            if p['Code'] == code:
                if 'nom' in modifications:
                    p['Nom'] = modifications['nom']
                if 'categorie' in modifications:
                    p['Catégorie'] = modifications['categorie']
                if 'prix_unitaire' in modifications:
                    p['PrixUnitaire'] = str(modifications['prix_unitaire'])
                
                self.ecrire_inventaire(produits)
                print(f"✓ Produit '{code}' modifié avec succès.")
                return True
        
        print(f"❌ Produit avec le code '{code}' introuvable.")
        return False
    
    def supprimer_produit(self, code: str):
        """Supprime un produit de l'inventaire"""
        produits = self.lire_inventaire()
        produits_filtres = [p for p in produits if p['Code'] != code]
        
        if len(produits) == len(produits_filtres):
            print(f"❌ Produit avec le code '{code}' introuvable.")
            return False
        
        self.ecrire_inventaire(produits_filtres)
        print(f"✓ Produit '{code}' supprimé avec succès.")
        return True
    
    def rechercher_par_categorie(self, categorie: str) -> List[Dict]:
        """Recherche des produits par catégorie"""
        produits = self.lire_inventaire()
        resultats = [p for p in produits if p['Catégorie'].lower() == categorie.lower()]
        return resultats
    
    def rechercher_par_nom(self, nom: str) -> List[Dict]:
        """Recherche des produits par nom (recherche partielle)"""
        produits = self.lire_inventaire()
        resultats = [p for p in produits if nom.lower() in p['Nom'].lower()]
        return resultats
    
    def calculer_valeur_stock(self) -> float:
        """Calcule la valeur totale du stock"""
        produits = self.lire_inventaire()
        valeur_totale = sum(
            int(p['Quantité']) * float(p['PrixUnitaire']) 
            for p in produits
        )
        return valeur_totale
    
    def exporter_inventaire(self, nom_fichier: str, filtre_categorie: Optional[str] = None):
        """Exporte l'inventaire (ou une catégorie) vers un nouveau CSV"""
        if filtre_categorie:
            produits = self.rechercher_par_categorie(filtre_categorie)
        else:
            produits = self.lire_inventaire()
        
        if not produits:
            print("❌ Aucun produit à exporter.")
            return False
        
        with open(nom_fichier, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=self.colonnes)
            writer.writeheader()
            writer.writerows(produits)
        
        print(f"✓ {len(produits)} produit(s) exporté(s) vers '{nom_fichier}'.")
        return True


def afficher_menu():
    """Affiche le menu principal"""
    print("\n" + "="*50)
    print("  SYSTÈME DE GESTION D'INVENTAIRE")
    print("="*50)
    print("1.  Afficher tous les produits")
    print("2.  Ajouter un produit")
    print("3.  Mettre à jour la quantité")
    print("4.  Modifier un produit")
    print("5.  Supprimer un produit")
    print("6.  Rechercher par catégorie")
    print("7.  Rechercher par nom")
    print("8.  Calculer la valeur du stock")
    print("9.  Exporter l'inventaire")
    print("0.  Quitter")
    print("="*50)


def main():
    """Fonction principale avec menu interactif"""
    gestion = GestionInventaire()
    
    while True:
        afficher_menu()
        choix = input("Votre choix: ").strip()
        
        if choix == "1":
            gestion.afficher_produits()
        
        elif choix == "2":
            print("\n--- Ajouter un produit ---")
            code = input("Code: ").strip()
            nom = input("Nom: ").strip()
            categorie = input("Catégorie: ").strip()
            try:
                quantite = int(input("Quantité: ").strip())
                prix = float(input("Prix unitaire: ").strip())
                gestion.ajouter_produit(code, nom, categorie, quantite, prix)
            except ValueError:
                print("❌ Erreur: Valeurs numériques invalides.")
        
        elif choix == "3":
            print("\n--- Mettre à jour la quantité ---")
            code = input("Code du produit: ").strip()
            try:
                modif = int(input("Modification (+/-): ").strip())
                gestion.mettre_a_jour_quantite(code, modif)
            except ValueError:
                print("❌ Erreur: Valeur numérique invalide.")
        
        elif choix == "4":
            print("\n--- Modifier un produit ---")
            code = input("Code du produit: ").strip()
            nom = input("Nouveau nom (laisser vide pour ne pas modifier): ").strip()
            categorie = input("Nouvelle catégorie (laisser vide pour ne pas modifier): ").strip()
            prix = input("Nouveau prix (laisser vide pour ne pas modifier): ").strip()
            
            modifications = {}
            if nom:
                modifications['nom'] = nom
            if categorie:
                modifications['categorie'] = categorie
            if prix:
                try:
                    modifications['prix_unitaire'] = float(prix)
                except ValueError:
                    print("❌ Prix invalide, ignoré.")
            
            if modifications:
                gestion.modifier_produit(code, **modifications)
            else:
                print("❌ Aucune modification spécifiée.")
        
        elif choix == "5":
            print("\n--- Supprimer un produit ---")
            code = input("Code du produit: ").strip()
            confirmation = input(f"Confirmer la suppression de '{code}' (o/n): ").strip().lower()
            if confirmation == 'o':
                gestion.supprimer_produit(code)
        
        elif choix == "6":
            print("\n--- Rechercher par catégorie ---")
            categorie = input("Catégorie: ").strip()
            resultats = gestion.rechercher_par_categorie(categorie)
            print(f"\n{len(resultats)} résultat(s) trouvé(s):")
            gestion.afficher_produits(resultats)
        
        elif choix == "7":
            print("\n--- Rechercher par nom ---")
            nom = input("Nom (ou partie du nom): ").strip()
            resultats = gestion.rechercher_par_nom(nom)
            print(f"\n{len(resultats)} résultat(s) trouvé(s):")
            gestion.afficher_produits(resultats)
        
        elif choix == "8":
            valeur = gestion.calculer_valeur_stock()
            print(f"\n💰 Valeur totale du stock: {valeur:.2f} DH")
        
        elif choix == "9":
            print("\n--- Exporter l'inventaire ---")
            nom_fichier = input("Nom du fichier de sortie: ").strip()
            filtre = input("Filtrer par catégorie (laisser vide pour tout exporter): ").strip()
            gestion.exporter_inventaire(
                nom_fichier, 
                filtre if filtre else None
            )
        
        elif choix == "0":
            print("\n👋 Au revoir!")
            break
        
        else:
            print("❌ Choix invalide. Veuillez réessayer.")


if __name__ == "__main__":
    main()