from bokhylle import Bokhylle

class Bibliotek:

    def __init__(self):
        self._bokhyller = [Bokhylle(30)]

    def finnBokIBibliotek(self, boknavn, utgivelsesaar):

        for bokhylle in self._bokhyller:
            if bokhylle.finnBok(boknavn, utgivelsesaar).hentNavn() == boknavn and bokhylle.finnBok(boknavn, utgivelsesaar).hentUtgivelsesaar() == utgivelsesaar:
                return bokhylle.finnBok(boknavn, utgivelsesaar)
            else:
                return False

    def leggTilBokIBibliotek(self, bok):
        ledigBokhylle = None

        for bokhylle in self._bokhyller:
            if bokhylle.erDetPlass():
                ledigBokhylle = bokhylle

        if ledigBokhylle == None:
            ledigBokhylle = self._utvidBibliotek()

        ledigBokhylle.leggTilBok(bok)

    def _utvidBibliotek(self):
        self._bokhyller.append(Bokhylle(30))
