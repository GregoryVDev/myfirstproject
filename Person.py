# La méthode spéciale __contains__
class Person:
    def __init__(self, name, fonction):
        self.person_name = name
        self.person_fonction = fonction

    # Permet de retourner si l'élément item est dans le person_name
    def __contains__(self, item):
        # Vérifie si la lettre "r" existe et dans le nom et dans la fonction pour renvoyer true, il faut que la lettre demandé soit sur les deux mots (nom et fonction)
        return item in self.person_name and self.person_fonction

person1 = Person("Mastafi", "Professeur")

print("r" in person1)
