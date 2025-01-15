# L'encapsulation et les attributs privés
class Person:
    def __init__(self,name,fonction):
        self.person_name = name
        self.fonction = fonction

person1 = Person("Smith", "Développeur web")

print("Nom:", person1.person_name)
print("Fonction:", person1.fonction)


# Déclarer un attribut privé avec "__"