"""
07.06: Buss
"""

class Buss:

    def __init__(self, maksKapasitet):
        self._maksKapasitet = maksKapasitet
        self._antallPassasjerer = 0

    def erTom(self):
        if self._antallPassasjerer == 0:
            return True
        else:
            return False

    def erFull(self):
        if self._antallPassasjerer == self._maksKapasitet:
            return True
        else:
            return False

    def plukkOpp(self):
        if self.erFull():
            print("Bussen er full, ingen kan plukkes opp.")
        else:
            print("Tok opp en passasjer.")
            self._antallPassasjerer += 1

    def slippAv(self):
        if self.erTom():
            print("Bussen er tom, ingen kan slippes av.")
        else:
            print("Slapp av en passasjer.")
            self._antallPassasjerer -= 1

    def antPaaBuss(self):
        print(self._antallPassasjerer)

def main():
    b1 = Buss(20)

    for i in range(10):
        b1.plukkOpp()

    b1.antPaaBuss()

    for i in range(12):
        b1.plukkOpp()

    b1.antPaaBuss()

    for i in range(15):
        b1.slippAv()

    b1.antPaaBuss()

main()
