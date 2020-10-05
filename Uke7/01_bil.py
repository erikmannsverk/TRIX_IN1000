"""
07.01: Bil-objekter

a) Skriv en klasse med navn 'Bil':

b) Bilen skal ha variabelen eier. Denne skal være en tekst streng.

c) Sett eier verdien i en konstruktør (init-metode).

d) Skriv en metode for å skrive ut navnet til eieren.

e) Test klassen din ved å opprette to Bil-objekter med forskjellige eiere og skrive ut navnet på eieren av det siste objektet du opprettet.
"""

class Bil:
    def __init__(self, eier):
        self.eier = eier

    def printEier(self):
        print(self.eier + " eier denne bilen.")

b1 = Bil("Erik")
b2 = Bil("Nils")
b2.printEier()
