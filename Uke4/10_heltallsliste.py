"""

04.10: Heltallsliste og løkke

a) Lag fem heltallsvariabler som inneholer verdiene 0,1,2,3,4.
b) Skriv ut verdiene av variablene.
c) Lag en tom liste som heter tall.
d) Legg tallene 0 til 4 inn i listen ved hjelp av en løkke.
e) Skriv ut variablene i listen ved hjelp av en løkke.

"""

tall_en = 0
tall_to = 1
tall_tre = 2
tall_fire = 3
tall_fem = 4

print(tall_en)
print(tall_to)
print(tall_tre)
print(tall_fire)
print(tall_fem)

tall = []

for i in range(4):
    tall.append(i)

for i in tall:
    print(i)
