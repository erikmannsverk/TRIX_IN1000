"""
04.14: Ordbok med grønnsaksbeholdning

Du driver en grønnsaksforretning og skal legge til grønnsaker i beholdningen.

a) Lag en tom ordbok beholdning.

b) Lag en løkke som kjører så lenge brukeren ønsker å fortsette å gi input.

c) Inne i løkken skal du be brukeren om å oppgi en grønnsak. Deretter skal brukeren oppgi en pris. Sjekk at brukeren oppgir et heltall! Hvis de oppgir gyldige verdier skal du legge til det brukeren har oppgitt i ordboken din, slik at grønnsaksstrengen blir en nøkkel og antallet blir den tilhørende verdien.

d) Når brukeren er ferdig med å oppgi grønnsaker skal du bruke en for-løkke for å skrive ut beholdningen din. Skriv ut alle grønnsakene med tilhørende antall.
"""

#A
beholdning = {}

#B og C
teller = True

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

while teller:

    grønnsak = input("Oppgi grønnsak: ")
    pris = input("Oppgi pris: ")

    if is_number(pris):
        float(pris)
        beholdning[grønnsak] = pris
    else:
        print("Du har oppgitt ugyldig pris.")

    brukerInput = input("Vil du fortsette (ja/nei): ").lower()

    if brukerInput == "nei":
        teller = False

#D 
for elem in beholdning:
    print(f"{elem} : {beholdning[elem]}")
