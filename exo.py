# Lecture d'un fichier et la méthode readlines()
notre_poeme = open("poeme.txt", "r")

line = notre_poeme.readline()

while line != "":
    print(line)
    line = notre_poeme.readline()