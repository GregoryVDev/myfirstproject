# Les dictionnaires et les fonctions
def occurence_character(chaine):
    dic = {}
    for c in chaine:
        if c in dic:
            dic[c] += 1
        else:
            dic[c] = 1
    return dic

chaine = "aaazgezgeznjfezjfcjeznfezjf"
occurence_character(chaine)

print(occurence_character(chaine))
