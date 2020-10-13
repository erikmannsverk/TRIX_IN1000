"""
08.01: Bryllup og giftemål
1. Definer klassen Person. Alle personer har et navn. Personer kan ha en ektefelle, men ingen personer er gift i det øyeblikket de opprettes.
2. Skriv en metode minStatus. Hvis personen er gift skal navnet på ektefellen printes til terminal, ellers skal det skrives ut at personen er singel.
3. Skriv en metode bryllup i klassen som tar én parameter. Parameteren skal være en referanse til en annen person. Funksjonen skal gjøre personen i parameteren til ektefellen til personen metoden er kalt på.
"""

class Person:

    def __init__(self, navn):
        self._navn = navn
        self._partner = None

    def minStatus(self):
        if self._partner:
            print(f"Beklager, jeg er alt gift med {self._partner.hentNavn()}.")
        else:
            print("Jeg er på sjekkern!")

    def bryllup(self, nyPartner):
        self._partner = nyPartner

    def hentNavn(self):
        return self._navn
