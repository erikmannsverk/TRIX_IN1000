"""
08.02 Budrunde på aksjon
"""

class Vare:

    def __init__(self, beskrivelse):
        self._beskrivelse = beskrivelse
        self._hoyesteBud = None

    def by(self, pris):
        if self._hoyesteBud == None:
            self._hoyesteBud = pris
        elif self._hoyesteBud < pris:
            self._hoyesteBud = pris
        else:
            print(f"Beklager, høyeste bud er {self._hoyesteBud}")

    def seBud(self):
        if self._hoyesteBud == None:
            print("Ingen har bydd på denne varen enda")
            return 0
        else:
            return self._hoyesteBud

vase = Vare("Vase")
vase.by(100)
print(vase.seBud())
vase.by(150)
print(vase.seBud())
vase.by(250)
print(vase.seBud())
vase.by(100)
