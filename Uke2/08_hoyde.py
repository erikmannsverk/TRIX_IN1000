"""
02.10: Høyde
Du skal lage en program som gir tar inn en høyde i cm fra bruker, og skriver ut et av følgende alternativer:
- Du er lav.
- Du er middels.
- Du er høy.
Grensen for å være lav er om hoyde < 140 cm, og grensen for å være høy er om hoyde > 190 cm.
"""

def hoydeSjekk():
    hoyde = int(input('Hvor høy er du?\n> '))
    if hoyde < 140:
        print('Du er lav.')
    elif hoyde > 190:
        print('Du er høy.')
    else:
        print('Du er middels.')

hoydeSjekk()
