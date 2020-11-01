
class Dvd:

    def __init__(self, tittel, produsent, utgaveNummer):
        self._tittel = tittel
        self._produsent = produsent
        self._utgaveNummer = utgaveNummer

    def __str__(self):
        return self._tittel

    def __eq__(self, other):
        return self.__class__ == other.__class__

    
