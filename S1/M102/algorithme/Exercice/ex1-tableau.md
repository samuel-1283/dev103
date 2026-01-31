Algorithme moyenne_note
Variables
		Tableau N(318) : réel
		M , s : réel
		i : entier
Début
	Pour i <-- 0 a 317 pas 1 faire
		Ecrire("donner la valeur de l'etudiant num ", i+1 ":"
		Lire(N(i))
	fin Pour
	s <-- 0 
	Pour i <-- 0 a 317 pas 1 faire
		s <-- s + N(i)
	fin Pour
	M <-- s / 318
	Ecrire("la moyenne des note est : ",M)
Fin

