"""
04.25 nest minste

I denne oppgaven skal du skrive en funksjon som returnerer det nest minste tallet i en liste. Dette skal du gjøre uten å bruke min(). Om det minste tallet finnes flere steder i den samme listen skal du returnere det nest minste tallet, som ikke tilsvarer det minste. Altså [1,1,2,2,3,4,5] skal returnere 2.

"""

liste1 = [1, 4, 6, 8, 10, 15, 6, 2, 1, 1]
liste2 = [1, 3, 5, 7]

def nestMinsteTallet(liste):
    nestMinst = liste[0]

    # Finnner minste på nytt og på nytt
    for elem in liste:
        if elem < nestMinst:
            nestMinst = elem

    # Fjerner den minste til den er borte for godt
    while nestMinst in liste:
        liste.remove(nestMinst)

    #Gjør prosessen på nytt
    nestMinst = liste[0]

    # Finner den minste av de som er igjen.
    for elem in liste:
        if elem < nestMinst:
            nestMinst = elem

    return nestMinst

nest_minst_l1 = nestMinsteTallet(liste1)
print(nest_minst_l1)
