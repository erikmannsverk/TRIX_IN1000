"""
04.15: Binærtall


Skriv et program som leser inn et tall og skriver ut de binære siffrene i tallet. For å gjøre dette kan du ta tallet og skrive ut resultatet du får av operasjonen tall % 2, så kan du erstatte tallet med tall // 2. Altså heltallsdivisjonen av tallet delt på to.

"""

tallBruker = int(input("Skriv et tall du vil se i binærtall: "))

while tallBruker > 0:
    rest = tallBruker % 2
    print(rest)
    tallBruker = tallBruker // 2
