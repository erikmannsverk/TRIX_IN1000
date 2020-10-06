"""
07.03: Espressomaskin
"""

class EspressoMaskin:

    # Konstruktør
    def __init__(self):
        self._vann = 0

    def lagEspresso(self):
        if self._vann > 40:
            self._vann -= 40
            print("Her har du en espresso!")
        else:
            print("Det er ikke nok vann til å lage en espresso.")

    def lagLungo(self):
        if self._vann > 110:
            self._vann -= 110
            print("Her har du en lungo!")
        else:
            print("Det er ikke nok vann til å lage en lungo.")

    def fyllVann(self, ml):
        if self._vann + ml <= 1000:
            self._vann += ml
        else:
            print("Det er ikke plass til mer enn 1000 ml.")

    def hentVannmengde(self):
        print(f"Vannmengde: {self._vann} ml")

e1 = EspressoMaskin()

inputGodkjent = False
while inputGodkjent != True:

    print()
    brukerSvar = input("Lag espresso: 'e'\nLag Lungo: 'l'\nFyll på vann: 'f'\nHent Vannmengde 'v'\nAvslutt: 'a'\n\n> ").lower()
    print()

    if brukerSvar == 'e':
        e1.lagEspresso()
    elif brukerSvar == 'l':
        e1.lagLungo()
    elif brukerSvar == 'f':
        mengde = int(input("Hvor mye vann vil du fylle på (ml)? \n> "))
        e1.fyllVann(mengde)
    elif brukerSvar == 'v':
        e1.hentVannmengde()
    elif brukerSvar == 'a':
        inputGodkjent = True
