#Realiser par Badreddine ejjebli
text = input("saisir un texte (phrase, paragraphe ou plusieurs phrases) :")

#1. Analyse statistique du texte : 

def nbr_caractere(text):
    nbr_car = len(text)
    return nbr_car

def nbr_caractere_sans_espace(text):
    nbr_sans_espace = text.replace(" ","")
    nbr_sans = len(nbr_sans_espace)
    return nbr_sans

def nbr_mot(text):
    mot = text.split()
    nbr_mot = len(mot)
    return nbr_mot

def nbr_voy_cons(texte):
    voyelles = "aeiouàâäéèêëïîôùûüÿæœAEIOUÀÂÄÉÈÊËÏÎÔÙÛÜŸÆŒ"
    consonnes_lettres = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZçÇ"
    nb_voyelles = 0
    nb_consonnes = 0
    
    for caractere in texte:
        if caractere in voyelles:
            nb_voyelles = nb_voyelles + 1
        if caractere in consonnes_lettres:
            nb_consonnes = nb_consonnes + 1
    return nb_voyelles, nb_consonnes

def nbr_phrases(texte):
    nb_phrases = texte.count('.') + texte.count('!') + texte.count('?')
    return nb_phrases

def mot_plus_long_court(texte):
    mots = texte.split()
    
    if not mots:
        return "pas de mot touver"
    
    mot_plus_long = mots[0]
    mot_plus_court = mots[0]
    
    for mot in mots:
        if len(mot) > len(mot_plus_long):
            mot_plus_long = mot
        if len(mot) < len(mot_plus_court):
            mot_plus_court = mot
    
    return mot_plus_long, mot_plus_court
#2. Recherche et manipulation : 

#pardon moi j'ai pas eu le temps de finir cette partie </3

#3. Transformation du texte : 

#pardon moi j'ai pas eu le temps de finir cette partie </3

#Affichage :

print("\n================Analyze================\n")
print(f" || Nombre de caractères:              {nbr_caractere(text)}")
print(f" || Nombre de caractères sans espace : {nbr_caractere_sans_espace(text)}")
print(f" || Nombre de mots:                    {nbr_mot(text)}") 
voyelles, consonnes = nbr_voy_cons(text)
print(" || Nombre de voyelles:                {}".format(voyelles))
print(" || Nombre de consonnes:               {}".format(consonnes))
print(f" || Nombre des phrases :               {nbr_phrases(text)}")
mot_p_long , mot_p_court = mot_plus_long_court(text)
print(" || Le mot le plus long est :          {}".format(mot_p_long))
print(" || Le mot le plus court est :         {}".format(mot_p_court))
print("\n=========================================\n")


