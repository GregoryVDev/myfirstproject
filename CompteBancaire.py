# Class et constructeur
class Account:
    def __init__(self, name = "Dupond", solde = 1000):
        self.name = name
        self.solde = solde

    def depot(self, somme):
        self.solde += somme
        return self.solde

    def retrait(self, somme):
        self.solde -= somme
        return self.solde

    def afficher(self):
        print("Le compte bancaire de", self.name, "a pour solde:", self.solde)

compte1 = Account("Christopher", 1500)
compte1.afficher()

compte1.depot(5000)
compte1.afficher()