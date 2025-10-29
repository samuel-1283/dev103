ttc = float(input("veuillez saisir ttc :"))
tva = float(input("veuillez saisir tva :"))

ht = ttc / (1+tva)
print("ht est :",ht)