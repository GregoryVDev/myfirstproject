# Les accesseurs et les mutateurs (getters et setters)
class Person:
    def __init__(self,name,fonction):
        # Déclarer un attribut privé avec "__"
        self.__person_name = name
        self.fonction = fonction

    def getName(self):
        return self.__person_name

    def setName(self, name ):
        self.__person_name = name

person1 = Person("Smith", "Développeur web")

print("Nom:", person1.getName())