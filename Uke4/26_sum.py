"""
04.26 Sum av elementer



"""
liste = [8, 5, 5, 10, 9, 1, 1, 2]

def sum(liste_tall):
    isTrue = False
    for i in range(len(liste_tall) - 2):
        if liste_tall[i] + (liste_tall[i+1]) == liste_tall[i+2]:
            print(liste_tall[i], liste_tall[i+1], liste_tall[i+2])
            isTrue = True
    return isTrue
print(sum(liste))
