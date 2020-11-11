
class Brev:

    def __init__(self, avsender, mottaker):
        self._avsender = avsender
        self._mottaker = mottaker
        self._liste = []

    def skrivLinje(self, streng):
        self._liste.append(streng)

    def lesBrev(self):
        print(f"\nHei, {self._mottaker}!\n")
        for i in range(len(self._liste)):
            print(self._liste[i])
        print(f"\nHilsen fra {self._avsender}\n")

b1 = Brev("Erik Mannsverk", "Nils med Skillz")

b1.skrivLinje("Hva skjer?")
b1.skrivLinje("Har du det bra?")
b1.skrivLinje("Jeg liker kaffe")

b1.lesBrev()
