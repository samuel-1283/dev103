import csv
import os
from datetime import datetime

def creer_fichier_exemple():
    """Créer un fichier CSV d'exemple"""
    nom_fichier = 'ventes.csv'
    with open(nom_fichier, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['produit', 'quantite', 'prix'])
        writer.writerow(['Pain', '50', '1.20'])
        writer.writerow(['Croissant', '30', '1.50'])
        writer.writerow(['Baguette', '80', '0.90'])
        writer.writerow(['Pain', '25', '1.20'])
        writer.writerow(['Croissant', '15', '1.50'])
        writer.writerow(['Gateau', '10', '5.00'])
    print(f"✓ Fichier d'exemple cree: {nom_fichier}\n")
    return nom_fichier

def lire_fichier_csv(nom_fichier):
    """Lire le fichier CSV"""
    ventes = []
    try:
        with open(nom_fichier, 'r', encoding='utf-8') as f:
            lecteur = csv.DictReader(f)
            for ligne in lecteur:
                ventes.append({
                    'produit': ligne['produit'].strip(),
                    'quantite': int(ligne['quantite']),
                    'prix': float(ligne['prix'])
                })
        return ventes
    except FileNotFoundError:
        print(f"✗ Erreur: Fichier '{nom_fichier}' introuvable")
        return None
    except Exception as e:
        print(f"✗ Erreur: {e}")
        return None

def calculer_chiffre_affaires(ventes):
    """Calculer le chiffre d'affaires total"""
    total = 0
    for vente in ventes:
        total += vente['quantite'] * vente['prix']
    return total

def produit_plus_vendu(ventes):
    """Trouver le produit le plus vendu"""
    quantites = {}
    for vente in ventes:
        produit = vente['produit']
        if produit in quantites:
            quantites[produit] += vente['quantite']
        else:
            quantites[produit] = vente['quantite']
    
    meilleur_produit = max(quantites, key=quantites.get)
    return meilleur_produit, quantites[meilleur_produit]

def statistiques_par_produit(ventes):
    """Calculer les statistiques par produit"""
    stats = {}
    for vente in ventes:
        produit = vente['produit']
        if produit not in stats:
            stats[produit] = {
                'quantite_totale': 0,
                'revenu_total': 0,
                'prix_moyen': 0
            }
        stats[produit]['quantite_totale'] += vente['quantite']
        stats[produit]['revenu_total'] += vente['quantite'] * vente['prix']
    
    # Calculer prix moyen
    for produit in stats:
        stats[produit]['prix_moyen'] = stats[produit]['revenu_total'] / stats[produit]['quantite_totale']
    
    return stats

def afficher_resultats(ventes):
    """Afficher tous les résultats"""
    print("\n" + "=" * 60)
    print("ANALYSE DES VENTES")
    print("=" * 60)
    
    # Chiffre d'affaires
    ca = calculer_chiffre_affaires(ventes)
    print(f"\n📊 CHIFFRE D'AFFAIRES TOTAL: {ca:.2f} EUR")
    
    # Produit le plus vendu
    produit, quantite = produit_plus_vendu(ventes)
    print(f"\n🏆 PRODUIT LE PLUS VENDU: {produit}")
    print(f"   Quantite vendue: {quantite} unites")
    
    # Statistiques par produit
    stats = statistiques_par_produit(ventes)
    print("\n" + "-" * 60)
    print("DETAILS PAR PRODUIT")
    print("-" * 60)
    
    for produit in sorted(stats.keys()):
        info = stats[produit]
        print(f"\n📦 {produit}")
        print(f"   Quantite totale: {info['quantite_totale']} unites")
        print(f"   Revenu total: {info['revenu_total']:.2f} EUR")
        print(f"   Prix moyen: {info['prix_moyen']:.2f} EUR")
    
    print("\n" + "=" * 60)
    print(f"Nombre total de transactions: {len(ventes)}")
    print("=" * 60 + "\n")

def generer_rapport(ventes, nom_fichier='rapport.txt'):
    """Générer un rapport texte"""
    ca = calculer_chiffre_affaires(ventes)
    produit, quantite = produit_plus_vendu(ventes)
    stats = statistiques_par_produit(ventes)
    
    with open(nom_fichier, 'w', encoding='utf-8') as f:
        f.write("=" * 60 + "\n")
        f.write("RAPPORT D'ANALYSE DES VENTES\n")
        f.write(f"Date: {datetime.now().strftime('%d/%m/%Y %H:%M')}\n")
        f.write("=" * 60 + "\n\n")
        
        f.write(f"CHIFFRE D'AFFAIRES TOTAL: {ca:.2f} EUR\n")
        f.write(f"NOMBRE DE TRANSACTIONS: {len(ventes)}\n\n")
        
        f.write(f"PRODUIT LE PLUS VENDU: {produit}\n")
        f.write(f"Quantite: {quantite} unites\n\n")
        
        f.write("-" * 60 + "\n")
        f.write("STATISTIQUES DETAILLEES PAR PRODUIT\n")
        f.write("-" * 60 + "\n\n")
        
        for produit in sorted(stats.keys()):
            info = stats[produit]
            f.write(f"Produit: {produit}\n")
            f.write(f"  - Quantite totale: {info['quantite_totale']} unites\n")
            f.write(f"  - Revenu total: {info['revenu_total']:.2f} EUR\n")
            f.write(f"  - Prix moyen: {info['prix_moyen']:.2f} EUR\n\n")
    
    print(f"✓ Rapport sauvegarde dans: {nom_fichier}")

def main():
    """Programme principal"""
    print("\n" + "=" * 60)
    print("ANALYSEUR DE VENTES JOURNALIERES")
    print("=" * 60 + "\n")
    
    # Demander si créer un exemple
    choix = input("Voulez-vous creer un fichier d'exemple? (o/n): ").strip().lower()
    if choix == 'o':
        nom_fichier = creer_fichier_exemple()
    else:
        nom_fichier = input("Nom du fichier CSV: ").strip()
        if not nom_fichier:
            nom_fichier = 'ventes.csv'
    
    # Lire le fichier
    print(f"\nLecture du fichier: {nom_fichier}...")
    ventes = lire_fichier_csv(nom_fichier)
    
    if not ventes:
        print("\n✗ Impossible de charger les donnees.")
        return
    
    print(f"✓ {len(ventes)} transactions chargees\n")
    
    # Afficher les résultats
    afficher_resultats(ventes)
    
    # Demander si générer un rapport
    choix = input("Voulez-vous generer un rapport texte? (o/n): ").strip().lower()
    if choix == 'o':
        nom_rapport = input("Nom du fichier rapport (Enter pour 'rapport.txt'): ").strip()
        if not nom_rapport:
            nom_rapport = 'rapport.txt'
        generer_rapport(ventes, nom_rapport)
    
    print("\n✓ Analyse terminee!\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nProgramme interrompu.\n")
    except Exception as e:
        print(f"\n✗ Erreur: {e}\n")
    
    input("Appuyez sur Enter pour quitter...")