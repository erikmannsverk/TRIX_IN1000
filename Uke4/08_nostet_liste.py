"""
04.08: Nøstet liste

a) Lag en tom liste oliste. Bruk en for-løkke for å legge til strengen "o" i denne listen 5 ganger.

b) Lag en tom liste stjerneliste og legg til strengen "*" 5 ganger på samme måte som i a.

c) Lag en tom liste rutenett. Legg oliste inn i rutenett med rutenett.append(oliste).

d) Legg stjerneliste inn i rutenett på samme måte. Legg deretter inn oliste en gang til.

e) Skriv ut rutenett[0], rutenett [1] og rutenett[2] på hver sin linje. Test programmet ditt.

f) Endre programmet slik at innholdet av rutenett skrives ut ved hjelp av en enkel for-løkke. Test programmet på nytt.
"""

oliste = []
stjerneliste = []

# Legger til "o" fem ganger i oliste.
for i in range(0,5):
    oliste.append("o")
    stjerneliste.append("*")

print(oliste)
print(stjerneliste)

rutenett = []
rutenett.append(oliste)
rutenett.append(stjerneliste)
rutenett.append(oliste)

for i in range(0,3):
    print(rutenett[i])
