
class Side:

    def __init__(self, lengde, farge):
        self._lengde = lengde
        self._farge = farge

    def hentLengde(self):
        return self._lengde

    def hentFarge(self):
        return self._farge

class Firkant:

    def __init__(self):
        self._topp = None
        self._bunn = None
        self._hoyre = None
        self._venstre = None

    def leggTilSide(self, side, plassering):
        if plassering.lower() == "topp":
            self._topp = side
        if plassering.lower() == "bunn":
            self._bunn = side
        if plassering.lower() == "venstre":
            self._venstre = side
        if plassering.lower() == "hoyre":
            self._hoyre = side

    def fjernSide(self, plassering):
        if plassering.lower() == "topp":
            self._topp = None
        if plassering.lower() == "bunn":
            self._bunn = None
        if plassering.lower() == "venstre":
            self._venstre = None
        if plassering.lower() == "hoyre":
            self._hoyre = None

    def erFirkant(self):
        return self._venstre is not None and self._hoyre is not None and self._topp is not None and self._bunn is not None


s1 = Side(13, "blå")
s2 = Side(13, "blå")
s3 = Side(13, "blå")
s4 = Side(13, "blå")

f1 = Firkant()
f2 = Firkant()
f3 = Firkant()

f1.leggTilSide(s1, "venstre")
f1.leggTilSide(s3, "hoyre")
f1.leggTilSide(s4, "topp")
f1.leggTilSide(s2, "bunn")

f2.leggTilSide(s1, "venstre")
f2.leggTilSide(s3, "hoyre")
f2.leggTilSide(s4, "topp")
f2.leggTilSide(s2, "bunn")

f3.leggTilSide(s1, "venstre")
f3.leggTilSide(s3, "hoyre")
f3.leggTilSide(s4, "topp")
f3.leggTilSide(s2, "bunn")

firkantListe = [f1, f2, f3]

def sjekkFirkant(liste):
    for firkant in liste:
        if(not firkant.erFirkant()):
            return False
    return True

print(sjekkFirkant(firkantListe))

print(Rektangel().erFirkant())
