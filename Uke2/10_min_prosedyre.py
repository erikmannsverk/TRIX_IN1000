"""
02.12: Min prosedyre
a) Lag en prosedyre min_prosedyre som printer "Hei student!" til terminalen.
b) Endre programmet slik at min_prosedyre også skriver ut "Velkommen til et nytt semester!" i en annen print.
c) Lag en ny prosedyre linjeskift som printer ut et tomt linjeskift.
d) Kall på min_prosedyre to ganger, men mellom kallene skal du også kalle på prosedyren linjeskift, slik at det blir et linjeskift mellom hilsenene.
"""

def min_Prosedyre():
    # Oppgave a og b
    print('Hei student!')
    print('Velkommen til et nytt semester!')

def linjeskift():
    # Oppgave c
    print()

# Oppgave d
min_Prosedyre()
linjeskift()
min_Prosedyre()
