# La méthode spéciale __len__
class Person:
    def __init__(self, name, fonction):
        self.person_name = name
        self.person_fonction = fonction

    def __len__(self):
        print("C'est une formation en Python")
        return len(self.person_name)

person1 = Person("Mastafi", "Professeur")
print(len(person1))
