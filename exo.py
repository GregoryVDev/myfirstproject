# Comment préciser le type des erreurs
def inverse(x):
    y = 1.0/x
    return y

try:
    x = float(input("Donnez un nombre que vous souhaitez avoir son inverse:"))
    y = inverse(x)
except Exception as e:
    print("Ce que vous avez saisi n'admet pas d'inverse")
    # Indiquer un message avec un type d'erreur qui correspond
    print("Le type d'erreur est:", e.__class__)
else:
    print(y)