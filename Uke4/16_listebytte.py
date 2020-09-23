"""

04.16: Verdier i liste

a) Lag et program som inneholder en heltallsliste
b) Finn minste verdi i listen
c) Finn største verdi i listen
d) Bytt plass på verdiene
e) Print listen både før og etter at du bytter plass på verdiene for å se at det blir riktig

"""

# A
tall_liste = [15, 2, 4, 20, 40, 3, 18,]

minste = tall_liste[0]
storste = tall_liste[0]
minsteIndeks = 0
storsteIndeks = 0

for elem in tall_liste:

    # B ) Sjekker om elemenetet er det minste i listen.
    if elem < minste:
        minste = elem
        minsteIndeks = tall_liste.index(elem)

    # C ) Sjekker om element er det største i listen.
    if elem > storste:
        storste = elem
        storsteIndeks = tall_liste.index(elem)

print(minste)
print(storste)
print(tall_liste)

# D
tmp = tall_liste[minste]
tall_liste[minste] = tall_liste[storste]
tall_liste[storste] = tmp

print(tall_liste)
