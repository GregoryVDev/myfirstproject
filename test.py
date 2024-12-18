
def main():
    # Récolter une première note
    note1 = int(input("Entrer la première note"))
    # Récolter la deuxième note
    note2 = int(input("Entrer la deuxième note"))
    # Récolter la troisièmre note
    note3 = int(input("Entrer la troisième note"))
    # Calculer la moyenne
    result = (note1 + note2 + note3) / 3
    # Afficher le resultat
    print("La moyenne de l'élève est de  " + str(result))


if __name__ == '__main__':
    main()