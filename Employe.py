# Le polymorphisme
class Employe:
    def __init__(self, name, firstname, age, email):
        self.employe_name = name
        self.employe_firstname = firstname
        self.employe_age = age
        self.employe_email = email

    def login(self):
        print("J'ai besoin de me connecter")

    def logout(self):
        print("J'ai besoin de me déconnecter")

    def conge(self):
        print("Entant qu'employé, j'ai droit à un congé annuel")


class Human_resources(Employe):
    fonction = "Les agents de ressources humaines gèrent le personnel de l'entreprise"


class Human_resources(Employe):
    def __init__(self, name, firstname, age, email, fonction):
        Employe.__init__(self, name, firstname, age, email)
        self.employe_fonction = fonction

    def conge(self):
        Employe.conge(self)
        print("Entant que agent de ressources humaines, j'ai droit à un séjour payant")


agent1 = Human_resources("Mastafi", "Mohammed", 40, "mastafi@yahoo.fr", "Responsable")

agent1.conge()

print(agent1.employe_name, agent1.employe_firstname, "a pour âge:", agent1.employe_age, "ans et pour mail:", agent1.employe_email, "et pour fonction:", agent1.employe_fonction)
