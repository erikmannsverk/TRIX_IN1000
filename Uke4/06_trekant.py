"""
04.06: Trekant

Lag en tom string stjerner og et heltall teller med verdi 0. Skriv en while-løkke som kjører så lenge teller er mindre enn 9. Hver gang løkken kjører skal du legge til "*" på slutten av stjerner og skrive den ut. Husk å øke teller med én for hver gang løkken kjøres.
"""

stjerner = ""

teller = 0

while teller < 9:
    #
    stjerner += "*"
    print(stjerner)

    # Øke teller med en hver gang for å ikke få en evig loop
    teller += 1
