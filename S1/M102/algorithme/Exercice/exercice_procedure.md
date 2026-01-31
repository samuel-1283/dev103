Algorithme Exercice_procedure
	Procedure max(x : entier , y : entier )
	Variables 
		m : entier 
	Début 
		Si x >= y alors 
			m <-- x
		Sinon
			m <-- y
	    fin Si
		Ecrire("le nombre maximum est :",m )
	Fin 
	Variables 
		a,b : entier 
Début
	Ecrire("veuillez saisir deux nombre :")
	Lire(a,b)
	max(a,b)
Fin 