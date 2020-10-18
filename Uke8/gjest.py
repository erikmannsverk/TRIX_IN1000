
class Gjest:

    def __init__(self):
        self._underholdningsverdi = 0

    def underhold(self, verdi):
        self._underholdningsverdi += verdi

    def hentUnderholdningsverdi(self):
        return self._underholdningsverdi
