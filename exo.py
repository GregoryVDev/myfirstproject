# Le module datetime

from datetime import date

# Afficher la date entière
date = date(1995, 12, 10)

format = date.strftime("%d/%m/%y")
print("Ma date de naissance est", format)