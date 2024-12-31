
def main():
    # Faire un input et le stocker dans la variable note
    note = float(input("Veuillez saisir votre note de mathématiques"))
    if note >= 16:
        print("Très bien")
    elif note >= 14:
        print("Bien")
    elif note >= 12:
        print("Assez bien")
    elif note >= 10:
        print("Votre travail est moyen")
    else:
        print("Vous devez faire un effort")

if __name__ == '__main__':
    main()