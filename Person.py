# La méthode spéciale __contains__
class Person:
    def __init__(self, name, fonction):
        self.person_name = name
        self.person_fonction = fonction

    # Permet de retourner si l'élément item est dans le person_name
    def __contains__(self, item):
        # Vérifie si la lettre "r" existe ou dans le nom  ou dans la fonction
        return item in self.person_name or self.person_fonction

person1 = Person("Mastafi", "Professeur")

print("r" in person1)
