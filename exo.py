# Ouverture et fermeture automatique d'un fichier

# Ouvrir en même temps deux fichiers txt avec with open
with open('poeme.txt', encoding="UTF-8") as notre_poeme, open('test.txt', 'r', encoding="UTF-8") as test:
    # Permet de faire une boucle pour lire chaque ligne dans la variable notre_poeme
    for line in notre_poeme:
        print(line)
        for t in test:
            print(t)