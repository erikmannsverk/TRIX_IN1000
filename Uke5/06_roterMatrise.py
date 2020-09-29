"""
05.06 Roter matrise

"""

matriseEn = [
[1,4,7],
[2,5,8],
[3,6,9]
]

matriseTo = [
[1,2,3],
[4,5,6],
[7,8,9]
]

def roter(liste):
    nyListe = []
    teller = 0
    samlaMatrise = matriseEn[0] + matriseEn[1] + matriseEn[2]
    samlaMatrise.sort()

    for tall in range(3):
        innerliste = []
        for i in range(3):
            innerliste.append(samlaMatrise[teller])
            teller += 1
        nyListe.append(innerliste)

    return nyListe


print(roter(matriseEn))
