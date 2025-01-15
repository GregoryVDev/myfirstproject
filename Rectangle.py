# Le constucteur
class Rectangle:
    def __init__(self, long, large, coul):
        self.longueur = long
        self.largeur = large
        self.couleur = coul

    # Calculer le périmètre
    def calcule_perimetre(self):
        return (self.longueur+self.largeur)*2

    # Calculer longueur et largeur
    def calcule_air(self):
        return self.longueur * self.largeur

rectangle1 = Rectangle(10.0, 7.5, "Bleu")

print("Le périmètre du rectangle1 est:", rectangle1.calcule_perimetre())
print("L'air du rectangle1 est:", rectangle1.calcule_air())