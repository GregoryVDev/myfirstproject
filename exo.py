# Comment éviter que le programme se plante
def inverse(x):
    y = 1.0/x
    return y

try:
    x = float(input("Donnez un nombre que vous souhaitez avoir son inverse:"))
    print(inverse(x))
except:
    print("Ce que vous avez saisi n'admet pas d'inverse")