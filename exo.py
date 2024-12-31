
def main():

    a,b = 3,1

    if(not(a<b)):
        a,b = b,a
        print("Les valeurs de a et b seront inversées")
        print("a= ", a)
        print("b = ", b)
    else:
        print("Les valeurs de a et b restent les mêmes")
        print("a = ", a)
        print("b = ", b)


if __name__ == '__main__':
    main()