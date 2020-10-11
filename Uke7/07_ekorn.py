"""
07.07: Feil i Ekorn-klasse
I denne oppgava skal du finne feil i programmet under. Du trenger ikke å tenke på at noen av feilene ikke blir relevante fordi programmet slutter å kjøre tidlig; regn med alle feila du finner.
"""

class Ekorn:
    def _init_(self, pelsfarge, bosted):
        self._pelsfarge = pelsfarge
        self._bosted = bosted

    def hentPelsfarge():
        return self._pelsfarge

    def hentBosted(self):
        return self.bosted

ekorn1 = Ekorn("brunt","Drammen")
ekorn2 = Ekorn("svart")
ekorn3 = ekorn("grått","Tjøme")
