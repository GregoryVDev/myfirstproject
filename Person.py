class Person:
    def __init__(self, name, fonction):
        self.person_name = name
        self.person_fonction = fonction


person1 = Person("Mastafi", "Professeur")
print(person1.person_name, person1.person_fonction)