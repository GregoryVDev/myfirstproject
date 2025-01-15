# Instanciation des classes
class Employe:
    name = ""
    firstname = ""
    age = 0
    phone = ""
    email = ""

    def lingin(self):
        print("J'ai besoin de me connecter")

    def logout(self):
        print("J'ai terminé et j'ai besoin de me déconnecter")

employe1 = Employe()
employe2 = Employe()

print(employe1.age)