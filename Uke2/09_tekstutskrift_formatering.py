"""
02.11: Tekstutskrift med formatering
1. Les om formatering av utskrift på side 54-57 i læreboken (Python for Everyone) eller i Python-dokumentasjonen .
2. Skriv et program som inneholder tre forskjellige navn inneholdt i tre forskjellige variabler. Pass på at navnene er av forskjellig lengde.
3. Skriv ut navnene, men sørg for at navnene blir skrevet ut justert til høyre. Se under for eksempelutskrift:
"""
#import math
#print(f'{math.pi:.3f}')

"""
table = {'Navn1': 'Daniel', 'Navn2': 'Mehdi', 'Navn3': 'Sigurd'}
for liste, navn in table.items():
    print(f'{liste:10} : {navn:10s}')
"""
navn1 = 'Daniel'
navn2 = 'Sigurd'
navn3 = 'Meh'

print('Navn1: {n1:>10}'.format(n1=navn1))
print('Navn2: {n2:>10}'.format(n2=navn2))
print('Navn3: {n3:>10}'.format(n3=navn3))
