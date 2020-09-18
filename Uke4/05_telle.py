"""
04.05: Noen telle-funksjoner
Denne oppgaven har tre deloppgaver som er uavhengige av hverandre. I hver av deloppgavene skal du skrive en funksjon.


a) Skriv en funksjon som returnerer antall sifre i et tall. For eksempel er det 3 sifre i tallet 104.

b) Skriv en funksjon som gir hvor mange av en viss bokstav det er i et ord. For eksempel er det 2 forekomster av bokstaven "e" i ordet kakespade.

c) Skriv en funksjon som tar inn en streng og et tall, og som returnerer True eller False basert på om strengens lengde er høyere enn tall.

"""

# a)

def returSiffer(tall):
    # Deler opp tallet i en liste.
    listeDelt = list(str(tall))

    # Returnerer lengden på lista.
    return len(listeDelt)

    #/ EVENTUELT

    return len(str(tall))


retur = returSiffer(123104)
print(retur)

# b)

# Funksjon med to variabler: en for ordet og en for bokstaven.
def antallBokstaver(ord, bokstav):
    # Deler opp ordet i en liste.
    listeDelt = list(ord)

    # Lager en variabel, sum.
    sum = 0

    # Sjekker hva alle bokstavene i ordet er.
    for i in ord:
        if bokstav == i:
            # Hvis en av bokstavene er e, vil den lokale variablene sum få + 1.
            sum += 1

    return sum

bokstaver = antallBokstaver("erik er en mann", "e")
# print(bokstaver)

# c)

def lengdeOrd(streng, tall):
    # Deler opp ordet i en liste.
    listeOrd = list(streng)

    # Returnere true hvis ordet er lengre enn tallet, og motsatt.
    return True if len(listeOrd) > tall else False

print(lengdeOrd("Mange", 6))
