# L'encapsulation et les attributs privés
class Person:
    def __init__(self,name,fonction):
        # Déclarer un attribut privé avec "__"
        self.__person_name = name
        self.fonction = fonction

    def display(self):
        return "Le nom est: {} et la fonction est: {}".format(self.__person_name, self.fonction)


person1 = Person("Smith", "Développeur web")

person1.display()

print(person1.display())
