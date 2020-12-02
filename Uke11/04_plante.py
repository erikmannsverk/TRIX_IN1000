"""
11.04: Plante

Lag en planteklasse med ulike metoder

"""

# Klassen plante
class Plante:

    # Konstruktør
    def __init__(self, maksgrenseVann):
        self._maksgrenseVann = maksgrenseVann
        self._vannbeholder = 0
        self._lever = True

    # Vanne plantene med selvvalgt mengde
    def vannPlante(self, vannCl):
        self._vannbeholder += vannCl
        if self._vannbeholder > self._maksgrenseVann:
            self._lever = False

    # For hver dag mister planten 20 cl med vann
    def nyDag(self):
        self._vannbeholder -= 20
        if self._vannbeholder <= 0:
            self._lever = False

    # Returnerer om planten er levende
    def levende(self):
        return self._lever

p1 = Plante(40)
p2 = Plante(90)

p1.vannPlante(10)
p2.vannPlante(10)

# 2 nye dager for begge plantene
p1.nyDag()
p2.nyDag()
p1.nyDag()
p2.nyDag()

print(p1.levende())
print(p2.levende())
