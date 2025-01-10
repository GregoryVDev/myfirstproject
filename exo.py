# Ouverture et fermeture automatique d'un fichier

# Ouvrir poeme.txt avec le mode par défaut 'r' et l'encoder UTF-8 avec un alias "notre_poeme"
with open('poeme.txt', encoding="UTF-8") as notre_poeme:
    # Permet de faire une boucle pour lire chaque ligne dans la variable notre_poeme
    for line in notre_poeme:
        print(line)