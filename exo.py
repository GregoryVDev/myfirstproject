# La clause finaly
def inverse(x):
    y = 1.0/x
    return y

try:
    x = float(input("Donnez un nombre que vous souhaitez avoir son inverse:"))
    y = inverse(x)
except ZeroDivisionError:
    print("Impossible de calculer l'inverse de zéro, veuillez entrer un nombre différent de zéro")
except ValueError:
    print("La valeur entrée n'est pas un nombre")
else:
    print(y)
finally:
    print("Le contenu de ce bloc est toujours exécuté!")