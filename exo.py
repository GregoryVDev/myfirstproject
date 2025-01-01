
def main():
    # Conditions et opérateurs d'appartenance
    expression = "Ce cours concerne l'apprentissage de Python"
    if("Python" in expression):
        print("C'est un cours sur Python")
    else:
        print("Ce cours ne concerne pas Python")


    if("Python" not in expression):
        print("Ce cours ne concerne pas Python")
    else:
        print("Ce cours concerne Python (not in)")



if __name__ == '__main__':
    main()