"""
06.04: Løkker og prosedyrer

a) Skriv en prosedyre skriv_med_trykk som tar en tekststreng som parameter. Prosedyren skal skrive ut tekststrengen med et utropstegn på slutten.

b) Skriv en løkke som skal kjøres 5 ganger. For hver gang skal brukeren bes om å oppgi et kraftuttrykk. Programmet skal kalle skriv_med_trykk med brukerinput som parameter.

c) Utvid programmet slik at vi er ferdige hvis brukeren skriver "nei" når de blir bedt om input.
"""

def skriv_med_trykk(tekststreng):
    print(tekststreng.upper() + "!")

inputGodkjent = False
while inputGodkjent != True:
    brukerinput = input("Kraftuttrykk: ")
    if brukerinput == "nei":
        inputGodkjent = True
    else:
        skriv_med_trykk(brukerinput)
