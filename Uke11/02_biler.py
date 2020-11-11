
class Person:

    def __init__(self, navn, alder):
        self._mineBiler = []
        self._laanteBiler = []
        self._navn = navn
        self._alder = alder

    def leggTilBil(self, bilObjekt):
        self._mineBiler.append(bilObjekt)

    def leggTilLaanebil(self, bilObjekt):
        self._laanteBiler.append(bilObjekt)

    def fjernBil(self, bilObjekt):
        self._mineBiler.remove(bilObjekt)

    def hentBiler(self):
        return self._mineBiler

    def hentNavn(self):
        return self._navn

    def laanBil(self, personObjekt, bilObjekt):

        for bil in personObjekt.hentBiler():
            if bil == bilObjekt:
                personObjekt.fjernBil(bilObjekt)
                self._laanteBiler.append(bilObjekt)

class Bil:

    def __init__(self, merke, farge):
        self._merke = merke
        self._farge = farge
        self._eier = None

    def settEier(self, personObjekt):
        self._eier = personObjekt

    def hentEier(self):
        return self._eier

def hovedprogram():
    nils = Person("Nils", 20)
    jan = Person("Jan", 49)
    tore = Person("Tore", 70)

    sabb = Bil("Sabb", "Svart")
    porche = Bil("Porche", "Gul")

    nils.leggTilBil(sabb)
    nils.leggTilBil(porche)
    sabb.settEier(nils)
    porche.settEier(nils)

    jan.laanBil(nils, sabb)
    print(sabb.hentEier().hentNavn())





hovedprogram()
