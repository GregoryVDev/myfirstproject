# Instanciation des classes
class Employe:
    name = ""
    firstname = ""
    age = 0
    phone = ""
    email = ""

    def login(self):
        print("J'ai besoin de me connecter")

    def logout(self):
        print("J'ai terminé et j'ai besoin de me déconnecter")

employe1 = Employe()
employe2 = Employe()

employe1.name = "Doe"
employe1.firstname = "John"
employe1.age = 40

employe2.name = "Smith"
employe2.firstname = "Leon"
employe2.age = 29

print(employe1.name, employe1.firstname, "a pour âge ", employe1.age)
print(employe2.name, employe2.firstname, "a pour âge ", employe2.age)

employe1.login()
employe1.logout()