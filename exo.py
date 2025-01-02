
def main():
    # Le mot clé break et continue
    for i in range(7):
        print("Début de la boucle numéro :", i)
        print("Bienvenue dans la formation Python ! :")
        if i < 4:
            continue
        print("La valeur de i est supérieur ou égale à:", i)
    print("fin de la boucle")


if __name__ == '__main__':
    main()