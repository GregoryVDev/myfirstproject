# L'héritage multiple
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


class Responsables(Human_resources):
    task = "Dirige une équipe"
    prime_supp = True

resp1 = Responsables("Smith", "Jonathan", 40, "Smith@yahoo.fr")
print("Tâche:", resp1.task)
print("Prime supplémentaire:", resp1.prime_supp)
print("Fonction:", resp1.fonction)

print(resp1.employe_name, resp1.employe_firstname, "a pour âge:", resp1.employe_age, "ans et a pour mail:", resp1.employe_email)
