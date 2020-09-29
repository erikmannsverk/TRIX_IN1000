"""
05.07 Handletur

"""
prisListe = [
    {"salat" : 12, "fisk" : 99, "melk" : 12, "brod" :12},
    {"salat" : 22, "fisk" : 60, "melk" : 18, "brod" :21},
    {"salat" : 8, "fisk" : 120, "melk" : 10, "brod" :19},
    {"salat" : 18, "fisk" : 40, "melk" : 30, "brod" :59},
    {"salat" : 15, "fisk" : 200, "melk" : 40, "brod" :9},
]

butikker = ["Rema1000", "Meny", "Kiwi","Spar", "Joker"]

handleListe = ["salat", "brod", "fisk"]

def finnButikk(handleListe, butikker, prisListe):
    samlaPris = 0
    for elem in handleListe:
        minstePris = prisListe[0][elem]
        for i in prisListe:
            if i[elem] < minstePris:
                minstePris = i[elem]
        samlaPris += minstePris
        print(f"Minstepris for {elem} er {minstePris} kr.")
    print(f"Samla pris for alle varer er {samlaPris} kr.")

finnButikk(handleListe, butikker, prisListe)
