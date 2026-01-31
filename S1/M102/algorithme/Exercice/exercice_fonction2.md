Algorithme exercice2_fonction 
	Fonction min (x : entier , y : entier ) : entier 
		Variables 
			min : entier 
		Début 
			Si x >= y alors
				min <-- y 
			Sinon 
				min <-- x 
			fin Si
			Retourne min
		Fin 
	Variables
		x , y : entier 
Début
	Ecrire("veuillez saisir deux nombre :")
	Lire(x,y)
	Ecrire("le nombre min est : ", min(x,y))
Fin 