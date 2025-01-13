# Gérer les erreurs et les exceptions

while True:
    try:
        number = int(input("Entrez un nombre:"))

        print("Le nombre est :", number)
        break
    except:
        print("Vous n'avez pas saisi un nombre")