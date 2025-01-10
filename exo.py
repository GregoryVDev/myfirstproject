# Ecriture dans un fichier

# Créer un nouveau fichier dans le repertoire du dossier
fichier = open('test_file.txt', 'w', encoding="UTF-8")

# Ecrire deux messages dans le fichier test_file.txt
fichier.write("Salut mes camarades \n")
fichier.write("Nous sommes en train d'apprendre Python tout doucement \n")

# Fermer le fichier
fichier.close()

# Ouvrir de nouveau le fichier test_file (le fichier est vide car il a remplacé ce qu'on a écrit par un nouveau fichier vide
fichier = open('test_file.txt', 'w', encoding="UTF-8")
