# L'héritage simple
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


class Human_resources(Employe):
    fonction = "Les agents de ressources humaines gèrent le personnel de l'entreprise"


agent1 = Human_resources("Eric", "Frederic", 35, "eric@gmail.com")
print(agent1.employe_name, agent1.employe_firstname, "a pour âge:", agent1.employe_age, "ans et a pour mail:", agent1.employe_email)

print("Fonction:", agent1.fonction)