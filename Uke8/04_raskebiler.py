"""
08.04: Raske biler
"""

class RaskBil:

    def __init__(self, navn, merke, bilnummer, drivstoff):
        self._navn = navn
        self._merke = merke
        self._bilnummer = bilnummer
        self._drivstoff = drivstoff

    def skrivInfo(self):
        print(f"\nNavn: {self._navn}\nMerke: {self._merke}\nBilnummer: {self._bilnummer}\nDrivstoff: {self._drivstoff}")

b1 = RaskBil("Fela", "Porche", "BM31039", "Diesel")
b2 = RaskBil("Nina", "BMW", "SP03993", "Bensin")
b3 = RaskBil("Brom", "Lambo", "PL29481", "Diesel")

listeBiler = [b1, b2, b3]

for i in listeBiler:
    i.skrivInfo()
    print()
