
def main():
    # Récolter une valeur porte monnaie
    wallet = 101
    print("Votre porte monnaie est de " + str(wallet) + "€")
    # Créer un produit qui aura pour valeur 50
    product = 50
    print("Le produit que vous voulez acheter est de " + str(product) + "€")
    # Afficher la nouvelle valeur du porte monnaie, après son achat
    result = (wallet - product)
    print("Apès votre achat de " + str(product) + " Votre porte monnaie restant est de " + str(resultAdded and ended the calculation exercise for a product to buy) + "€")


if __name__ == '__main__':
    main()