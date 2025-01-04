
def main():
    # La notion de compréhension de liste
    entiers = [-10, -3, -1, 0, 23, 56, 78]
    carres_entiers_negatif = [i*i for i in entiers if i<0]

    print(carres_entiers_negatif)



if __name__ == '__main__':
    main()