"""
04.04: For løkke i ulike forbehold
I denne oppgaven skal du bruke en for løkke for å iterere gjennom en liste, en ordbok og en mengde. Print ut alle elementene i listen, mengden, alle navn og alle kalle navn.
"""

# Liste - Alt blir printet ut i riktig rekkefølge.
aviser = ["Aftenposten", "VG", "Morgenbladet", "Dagbladet", "Klassekampen"]

for i in aviser:
    print(i)

print()
# Ordbok - Kun nøkkel blir printet ut.
kalleNavn = {"Roger" : "Roggis", "Magnus" : "Kluten", "Stine" : "Lappen", "Ingeborg" : "Skruen"}

for i in kalleNavn:
    print(i)
    print(kalleNavn[i])
    print("__")

print()
# Mengde - tallene blir printet ut i stigende rekkefølge.
parTall = {10, 8, 4, 2, 6, 0}

for i in parTall:
    print(i)
