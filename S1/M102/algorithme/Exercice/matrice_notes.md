Algorithme matrice
	Tableau notes(5,3) : réel 
	Variables i,j : entier 
	Variables s,m : réel
Début
	s <-- 0
	Pour i <-- 0 a 4 pas 1 faire
		Pour j <-- 0 a 2 pas 1 faire
			Ecrire("veuillez saisir la note d'etudiant :",i+1,"dans la matiere ",j+1)
			Lire(notes(i,j)) 
		fin Pour
	fin Pour
	s <-- 0
	m <-- 0
	Pour i <-- 0 a 4 pas 1 faire
		Pour j <-- 0 a 2 pas 1 faire
			s <-- s + notes(i,j)
		fin Pour
		m <-- s / 3
		Ecrire("la moyenne ds l'etudiant num : ",i+1 ," est :",m)
		s <-- 0
	fin Pour
	
Fin 