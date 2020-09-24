"""
04.22. Samme forbokstav

"""

personer = {}

inputGodkjent = False
while inputGodkjent != True:

    inputBruker = input("Skriv 'y' for å fortsette: ").lower()

    if inputBruker == 'y':
        navn = input("Hva heter du? ").lower()
        alder = input("Hvor gammel er du? ")
        personer[navn] = alder
    else:
        bokstav = input("Oppgi en bokstav! ").lower()

        while len(bokstav) != 1:
            bokstav = input("Oppgi en bokstav! ").lower()

        for key in personer:
            if key[0] == bokstav:
                print(f"{key}:{personer[key]}")

        inputGodkjent = True
