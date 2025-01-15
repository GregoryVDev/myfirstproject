# Le constructeur
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

employe1 = Employe("Smith", "Joe", 40, "joe@gmail.fr")
print(employe1.employe_name, employe1.employe_firstname, "a pour âge", employe1.employe_age, "ans", "et son adresse email", employe1.employe_email)

employe1.login()
employe1.logout()
