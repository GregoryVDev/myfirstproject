# L'encapsulation et les attributs privés
class Person:
    def __init__(self,name,fonction):
        self.name = name
        self.fonction = fonction

person1 = Person("Smith", "Développeur web")

print("Nom:", person1.name)
print("Fonction:", person1.fonction)