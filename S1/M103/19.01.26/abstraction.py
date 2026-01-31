from abc import ABC, abstractmethod
#abc = abstract base classe
class personne(ABC): #classe abstrait     
    def __init__(self,s):
        self.salaire = s

    @abstractmethod
    def afficher(self): #methode sans corps
        pass
    @abstractmethod
    def calculer(self):
        pass

class employer(personne):
    def afficher(self):
        print("salaire ",self.salaire)

    def calculer(self):
        return self.salaire * 1.5

e1 = employer(1500)
e1.afficher()
print(e1.calculer())