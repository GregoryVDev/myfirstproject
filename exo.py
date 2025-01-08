# Lecture d'un fichier et la méthode readlines()
notre_poeme = open("poeme.txt", "r")

lignes = notre_poeme.readlines()

for ligne in lignes:
    print(ligne)