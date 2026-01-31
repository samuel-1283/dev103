class Etudiant:

    def __init__(self,n,p):
        self.__nom = n
        self.__Prenom = p
#pour le nom :

    @property
    def nom(self):
        return self.__nom

    @nom.setter
    def nom(self,nom):
        self.__nom = nom

    @nom.deleter
    def nom(self):
        print("supprimer attribut nom")
        del self.__nom
#pour le prenom :

    @property
    def prenom(self):
        return self.__Prenom

    @prenom.setter    
    def prenom(sefl,prenom):
        self.__Prenom = prenom

    @prenom.deleter
    def prenom(self):
        print("supprimer attribut prenom")
        del self.__Prenom
