# Le polymorphisme
class Birds:
    def birds_species(self):
        print("Il existe de nombreux espèces d'oiseaux")

    def fly(self):
        print("La majorité des espèces d'oiseaux peuvent voler pendant plusieurs heures")

class Eagles(Birds):
    def fly(self):
        print("Les Aigles ont la capacité de voler plusieurs heures")

class Ostriches(Birds):
    def fly(self):
        print("Les Autruches ne peuvent pas voler")


bird1 = Birds()
eagle1 = Eagles()
ostrich1 = Ostriches()

bird1.fly()
eagle1.fly()
ostrich1.fly()