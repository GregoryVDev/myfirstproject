
def main():
    # La boucle for et la fonction range
    expression = "Python est un langage de programmation"
    for n in range(101):
        if n%2 == 0:
            print("Le nombre: ",n, " est un nombre pair")
        else:
            print("Le nombre: ",n, " est un nombre impair")


if __name__ == '__main__':
    main()