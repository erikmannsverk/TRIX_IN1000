
class Skuff:

    def __init__(self):
        self._mineSokker = []

    def settInnSokk(self, sokken):
        self._mineSokker.append(sokken)

    def sjekkStatus(self):
        hoyre = 0
        venstre = 0
        for i in self._mineSokker:
            if i.hentSide() == "venstre":
                venstre += 1
            elif i.hentSide() == "hoyre":
                hoyre += 1

        if venstre == hoyre:
            print("Alt i orden!")
        else:
            print("Sokkene er ujevnt fordelt. ")
