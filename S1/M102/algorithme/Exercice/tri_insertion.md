Algorithme tri_insertion
	Variables i, j, pos : entier 
	Variables temp : entier 
Début 
	Pour i <-- 2 a n faire 
		temp <-- T[i]
		pos <-- i - 1
		Tantque (pos >= 1) et (T[pos] > temp ) faire
			T[pos + 1 ] <-- T[pos]
			pos <-- pos - 1
		finTanque
		T[pos + 1] <-- temp
	fin Pour
Fin 