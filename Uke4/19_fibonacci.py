"""
04.19: Fibonacci-sekvens


1.Skriv funksjonen finnAlleFibTall som tar inn et tall og returnerer en liste med alle Fibonacci-tallene som har lavere verdi enn tallet som tas inn. Gitt verdien 11, skal funksjonen altså returnere [0,1,1,2,3,5,8].

2. Skriv funksjonen laBrukerSkriveInnTall som lar brukeren skrive inn et tall, tallet skal returneres.

3. Skriv ferdig programmet slik at programmet ber brukeren om informasjon. Programmet skal så kjøre finnAlleFibTall med returverdien fra laBrukerSkriveInnTall. Her kan du bruke en for-løkke.
"""

FIBONACCI = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]

def finnAlleFibTall(tall):
    returnListe = []

    for elm in range(len(FIBONACCI)):
        if FIBONACCI[elm] <= tall:
            returnListe.append(FIBONACCI[elm])

    return returnListe

def laBrukerSkriveInnTall():
    return int(input("Velg et tall i Fibonacci-følgen: "))

def main():
    tallBruker = laBrukerSkriveInnTall()
    rekkefølge = finnAlleFibTall(tallBruker)
    print(rekkefølge)

main()
