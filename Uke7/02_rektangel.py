"""
07.02: Rektangel

"""

class Rektangel:

    def __init__(self, lengde, bredde):
        self._lengde = lengde
        self._bredde = bredde

    def oekLengde(self, oekning):
        self._lengde += oekning
        print(f"Ny lengde: {self._lengde}")

    def oekBredde(self, oekning):
        self._bredde += oekning
        print(f"Ny bredde: {self._bredde}")

    def areal(self):
        print(f"Areal: {self._lengde * self._bredde}")

    def omkrets(self):
        print(f"Omkrets: {self._lengde * 2 + self._bredde * 2}")

    def reduserLengde(self, reduksjon):
        self._lengde -= reduksjon
        print(f"Ny lengde: {self._lengde}")

    def reduserBredde(self, reduksjon):
        self._bredde -= reduksjon
        print(f"Ny bredde: {self._bredde}")


r1 = Rektangel(10, 20)
r2 = Rektangel(5, 3)
r1.areal()
r2.areal()
r1.oekLengde(20)
r2.oekBredde(2)
r1.omkrets()
r2.omkrets()
