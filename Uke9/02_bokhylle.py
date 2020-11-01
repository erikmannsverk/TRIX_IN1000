
class Bok:

    def __init__(self, navn, forfatter, utgivelsesaar):
        self._navn = navn
        self._forfatter = forfatter
        self._utgivelsesaar = utgivelsesaar

    def hentNavn(self):
        return self._navn

    def hentUtgivelsesaar(self):
        return self._utgivelsesaar


class Bokhylle:

    def __init__(self, maxPlass):
        self._maxPlass = maxPlass
        self._boker = []

    def erDetPlass(self):
        return True if self._maxPlass > len(self._boker) else False

    def leggTilBok(self, bok):
        if self.erDetPlass():
            self._boker.append(bok)
            return True
        return False

    def finnBok(self, navn, utgivelsesaar):
        for bok in self._boker:
            if bok.hentNavn() == navn and bok.hentUtgivelsesaar == utgivelsesaar():
                return bok



def hovedprogram():

    bokhylle = Bokhylle(20)



hovedprogram()
