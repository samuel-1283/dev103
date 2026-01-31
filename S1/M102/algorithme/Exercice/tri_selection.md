Algorithme tri_selection
	Variables i, j, indmin : entier 
	Variables temp : entier 
	Tableau T(n) : entier 
Début 
	Pour i <-- 1 a n - 1 faire 
		indmin <-- i 
		Pour j <-- i + 1 a n faire
			Si T[j] < T[indmin] alors
				indmin <-- j
			fin Si 
		fin Pour
		temp <-- T[i]
		T[i] <-- T[indmin]
		T[indmin] <-- temp
	fin Pour	
Fin 