# L'encapsulation et les attributs privés
class Person:
    def __init__(self,name,fonction):
        # Déclarer un attribut privé avec "__"
        self.__person_name = name
        self.fonction = fonction

person1 = Person("Smith", "Développeur web")

print("Nom:", person1._Person__person_name)


