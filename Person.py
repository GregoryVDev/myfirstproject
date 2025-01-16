# La méthode spéciale __str__
class Person:
    def __init__(self, name, fonction):
        self.person_name = name
        self.person_fonction = fonction

    def __str__(self):
        return "Mon nom est {} et ma fonction est {}".format(self.person_name, self.person_fonction)



person1 = Person("Mastafi", "Professeur")
print(person1)
