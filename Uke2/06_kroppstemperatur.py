"""
02.08: Kroppstemperatur
Hos friske mennesker varierer kroppstemperaturen vanligvis mellom 36.5 og 37.5 grader. Lag et program som avgjør om en persons kroppstemperatur ligger henholdsvis under, innenfor eller over normal kroppstemperatur. Programmet skal lese kroppstemperaturen fra terminal.
"""

def kroppstemp():
    kt = float(input('Hva er kroppstemperaturen din?\n> '))
    if kt >= 36.5 and kt <= 37.5:
        print('Din kroppstemperatur er normal')
    elif kt < 36.5:
        print('Din kroppstemperatur er er under normal.')
    else:
        print('Din kroppstemperatur er er over normal.')

kroppstemp()
