"""
08.06 Modeller en familie!
"""

class Menneske:

    def __init__(self, navn, alder):
        self._navn = navn
        self._alder = alder
        self._erForelder = False
        self._barn = []

    def fodselsdag(self):
        self._alder += 1

    def bytteNavn(self, nyttNavn):
        self._navn = nyttNavn

    def faaBarn(self, navn):
        if not self._erForelder:
            self._erForelder = True

        # Lager barnobjektet i mennesket
        self._barn.append(Menneske(navn, 0))

    def hentBarn(self):
        return self._barn

def hovedprogram():

    p1 = Menneske("Nils", 19, False)

    p1.fodselsdag()
    p1.fodselsdag()
    p1.bytteNavn("Jan")
    p1.fodselsdag()
    p1.faaBarn("Janus")

    print(p1.hentBarn())


hovedprogram()
