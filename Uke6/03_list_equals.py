"""
06.03: Samme elementer

"""

liste1 = [1, 4, 9, 16, 9, 7, 4, 9, 11]
liste2 = [11, 11, 7, 9, 16, 4, 1]
liste3 = [11, 11, 7, 9, 16, 4, 1]
liste4 = [11, 7, 11, 4, 9, 1, 4]

def equals(liste_en, liste_to):
    if liste_en == liste_to:
        return True
    else:
        return False

print("To nøyaktig like lister:")
print(equals(liste3, liste2))

def sameSet(liste_a, liste_b):
    liste_a.sort()
    liste_b.sort()
    ordbok_en = {}
    ordbok_to = {}

    for tall in liste_a:
        ordbok_en[tall] = 0

    for tall in liste_b:
        ordbok_to[tall] = 0

    print(ordbok_en)
    print(ordbok_to)

    if ordbok_en == ordbok_to:
        return True
    else:
        return False

print("To lister med samme tall i ulike rekkefølge og ulikt antall av tall:")
print(sameSet(liste1, liste2))
