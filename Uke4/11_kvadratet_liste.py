"""
04.11: Kvadratet av alle tallene i en liste

a) Lag en liste med tallene 1, 2, 3, 4 og 5.

b) Finn kvadratet av hvert tall, og sett det inn på dens tidligere plass i listen.
"""

liste = []

for i in range(1,6):
    liste.append(i)

print(liste)

teller = 0

while teller < len(liste):
    liste[teller] = liste[teller] * liste[teller]
    teller += 1

print(liste)
