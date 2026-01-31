class Rectangle:
    def __init__(self, longeur, largeur, nom):
        self.longeur = longeur
        self.largeur = largeur
        self.nom = nom
    def surface(self):
        return self.longeur * self.largeur
    def afficher(self):
        print(f"""
        longeur : {self.longeur}
        largeur : {self.largeur}
        nom : {self.nom}
        surface : {self.surface()}
       """)

class Caree(Rectangle):
    def __init__(self, longeur, largeur):
        super().__init__(longeur,largeur,"rectangle")
        if self.longeur == self.largeur:
            self.nom = "carre"
    def surface(self):
        return self.longeur * self.largeur