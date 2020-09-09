"""
02.06: Mindre eller større enn
a) Lag et program som tar inn et tall fra brukeren og skriver ut om tallet er mindre eller større enn 10.
b) Legg deretter til en test til for å sjekke om tallet er mindre eller større enn 20.
c) Endre programmet slik at brukeren kun får én tilbakemelding per tall som er tastet inn.
"""

def tallSjekk():
    tall = int(input('Tast inn et tall:\n> '))
    if tall >= 10 and tall <= 20:
        print('Tallet er mellom 10 og 20')
    elif tall < 10:
        print('Tallet er mindre enn 10')
    else:
        print('Tallet er større enn 20')

tallSjekk()
