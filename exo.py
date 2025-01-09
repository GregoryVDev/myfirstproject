# Méthode simple et élégante pour lire un fichier
notre_poeme = open("poeme.txt", "r")

for line in notre_poeme:
    print(line)