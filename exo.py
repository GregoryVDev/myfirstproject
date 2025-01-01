
def main():
    # La boucle while
    number = int(input("Choisit quel nombre souhaites-tu afficher sa yable de multiplication"))
    i = 0
    while i <= 10:
        print(i, "x", number, "=", i*number)
        i+=1



if __name__ == '__main__':
    main()