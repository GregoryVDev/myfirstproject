# L'héritage multiple
class Mother:
    mother_name = ""
    def mother(self):
        print(self.mother_name)

class Father:
    father_name = ""
    def father(self):
        print(self.father_name)

class Children(Mother, Father):
    def parents(self):
        print("Mère:", self.mother_name)
        print("Père:", self.father_name)

soon1 = Children()
soon1.mother_name = "Teresa Carron"
soon1.father_name = "Maseau Jean-Louis"

soon1.parents()