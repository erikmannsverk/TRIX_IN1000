"""
06.02: Finne flest forekomster i en liste

"""

fil = open("02_fil_tall.txt", "r")

def les_tall_fra_fil(fil):
    liste = []
    for linje in fil:
        biter = linje.strip()
        liste.append(biter)
    return liste

def antall_forekomster(liste, heltall):
    teller = 0
    for tall in liste:
        if int(tall) == heltall:
            teller += 1
    return teller

def flest_forekomster(liste):
    ordbok = {}

    for tall in liste:
        ordbok[tall] = 0

    for tall in liste:
        if tall in ordbok:
            ordbok[tall] += 1

    maks = 0
    flestForekomster = 0

    for tall in ordbok:
        if ordbok[tall] > maks:
            maks = ordbok[tall]
            flestForekomster = tall

    return flestForekomster

def main():
    liste_fil = les_tall_fra_fil(fil)
    print(liste_fil)
    print(f"Heltall 5: {antall_forekomster(liste_fil, 5)}")
    print(f"Flest forekomster: {flest_forekomster(liste_fil)}")

main()
