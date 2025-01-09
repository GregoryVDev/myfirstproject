# Méthode simple et élégante pour lire un fichier
notre_poeme = open("poeme.txt", "r", encoding="utf-8")

for line in notre_poeme:
    print(line)