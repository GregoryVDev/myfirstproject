
def main():
    # Faire un input et le stocker dans la variable note
    age = float(input("Veuillez saisir votre age:"))
    woman_age = float(input("Veuillez saisir l'âge de votre partenaire:"))


    if age <= 30:
        if woman_age < age:
            print("Vous avez moins de 30 ans et votre partenaire est moins agé que vous!")
        else:
            print("Vous avez moins de 30 ans mais votre partenaire est plus agé que vous!")
    else:
        print("Votre age est supérieur à 30")


if __name__ == '__main__':
    main()