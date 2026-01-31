import csv
from collections import defaultdict

def lire_csv(nom_fichier):
    """Lire le fichier CSV et retourner les données"""
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
        print(f"Erreur : Le fichier '{nom_fichier}' n'existe pas.")
        return None
    except Exception as e:
        print(f"Erreur lors de la lecture : {e}")
        return None

def calculer_chiffre_affaires(ventes):
    """Calculer le chiffre d'affaires total"""
    total = sum(v['quantite'] * v['prix'] for v in ventes)
    return total

def trouver_produit_plus_vendu(ventes):
    """Trouver le produit le plus vendu par quantité"""
    quantites = defaultdict(int)
    for v in ventes:
        quantites[v['produit']] += v['quantite']
    
    if not quantites:
        return None, 0
    
    produit_top = max(quantites.items(), key=lambda x: x[1])
    return produit_top[0], produit_top[1]

def generer_rapport(ventes, nom_fichier_sortie='rapport.txt'):
    """Générer un rapport texte des analyses"""
    ca = calculer_chiffre_affaires(ventes)
    produit, quantite = trouver_produit_plus_vendu(ventes)
    
    # Calculer statistiques par produit
    stats_produits = defaultdict(lambda: {'quantite': 0, 'revenu': 0})
    for v in ventes:
        stats_produits[v['produit']]['quantite'] += v['quantite']
        stats_produits[v['produit']]['revenu'] += v['quantite'] * v['prix']
    
    with open(nom_fichier_sortie, 'w', encoding='utf-8') as f:
        f.write("=" * 50 + "\n")
        f.write("RAPPORT D'ANALYSE DES VENTES\n")
        f.write("=" * 50 + "\n\n")
        
        f.write(f"Nombre total de transactions : {len(ventes)}\n")
        f.write(f"Chiffre d'affaires total : {ca:.2f} €\n\n")
        
        f.write(f"Produit le plus vendu : {produit}\n")
        f.write(f"Quantité vendue : {quantite} unités\n\n")
        
        f.write("-" * 50 + "\n")
        f.write("DÉTAILS PAR PRODUIT\n")
        f.write("-" * 50 + "\n\n")
        
        for prod, stats in sorted(stats_produits.items()):
            f.write(f"Produit : {prod}\n")
            f.write(f"  Quantité totale : {stats['quantite']} unités\n")
            f.write(f"  Revenu total : {stats['revenu']:.2f} €\n\n")
    
    print(f"Rapport généré : {nom_fichier_sortie}")

def afficher_menu():
    """Afficher le menu principal"""
    print("\n" + "=" * 50)
    print("ANALYSE DE VENTES")
    print("=" * 50)
    print("1. Lire et analyser le fichier CSV")
    print("2. Quitter")
    print("=" * 50)

def main():
    """Fonction principale"""
    ventes = None
    
    while True:
        afficher_menu()
        choix = input("\nChoisissez une option : ").strip()
        
        if choix == '1':
            nom_fichier = input("Nom du fichier CSV (ex: ventes.csv) : ").strip()
            ventes = lire_csv(nom_fichier)
            
            if ventes:
                print(f"\n✓ {len(ventes)} transactions chargées")
                
                # Calculer et afficher les résultats
                ca = calculer_chiffre_affaires(ventes)
                print(f"\nChiffre d'affaires total : {ca:.2f} €")
                
                produit, quantite = trouver_produit_plus_vendu(ventes)
                print(f"Produit le plus vendu : {produit} ({quantite} unités)")
                
                # Générer le rapport
                generer = input("\nGénérer un rapport texte ? (o/n) : ").strip().lower()
                if generer == 'o':
                    generer_rapport(ventes)
        
        elif choix == '2':
            print("\nAu revoir !")
            break
        
        else:
            print("\nOption invalide. Veuillez réessayer.")

if __name__ == "__main__":
    print("Assurez-vous d'avoir un fichier CSV avec les colonnes : produit, quantite, prix")
    main()