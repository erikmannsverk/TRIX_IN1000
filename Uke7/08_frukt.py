"""
07.08: (Spiselige?) Frukter
"""
fruktListe = []
spiseligeVannFrukter = []

class Frukt:

    def __init__(self, navn, vann, spiselig):
        self._navn = navn
        self._vann = vann
        self._spiselig = spiselig

    def hentNavn(self):
        return self._navn

    def hentVannPr100(self):
        return self._vann

    def erSpiselig(self):
        return self._spiselig

ananas = Frukt("Ananas", 87, True)
banan = Frukt("Banan", 76, True)
eple = Frukt("Eple", 86, True)
nektarin = Frukt("Nektarin", 89, True)
morell = Frukt("Morell", 83, True)
papaya = Frukt("Papaya", 88, True)
sitron = Frukt("Sitron", 90, True)
mango = Frukt("Mango", 92, True)
trollhegg = Frukt("Trollhegg", 90, False)
slyngsøtvier = Frukt("Slyngsøtvier", 80, False)

fruktListe.append(ananas)
fruktListe.append(banan)
fruktListe.append(eple)
fruktListe.append(nektarin)
fruktListe.append(morell)
fruktListe.append(papaya)
fruktListe.append(sitron)
fruktListe.append(mango)
fruktListe.append(trollhegg)
fruktListe.append(slyngsøtvier)

for frukt in fruktListe:
    if frukt.hentVannPr100() > 85 and frukt.erSpiselig():
        spiseligeVannFrukter.append(frukt.hentNavn())

print(spiseligeVannFrukter)
