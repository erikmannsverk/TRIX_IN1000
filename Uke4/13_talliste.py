"""
04.13: Tall-liste med while-løkke

a) Lag et program med en while-løkke som ber bruker taste inn fem heltall og lagrer disse i en liste kalt tall (husk: int(...)).

b) Sum av liste: Utvid programmet slik at det regner ut summen av tallene ved hjelp av en løkke, og skriver ut resultatet.

c) Lave verdier: Legg til programkode som skriver ut alle verdiene i listen som er mindre enn 10.

d) Søk: Legg til programkode som skriver ut en beskjed om verdien 5 finnes eller ikke finnes i listen.
"""

#A
tall = []

teller = 0

while teller <= 4:
    brukerTall = int(input(f"Tall {teller + 1}: "))
    tall.append(brukerTall)
    teller += 1

print(tall)

#B
sum = 0
for elem in tall:
    sum += elem

print(f"Summen av tallene er {sum}.")

#C
print("Mindre enn 10:")
for elem in tall:
    if elem < 10:
        print(elem)

#D
fem_i_listen = False

for elem in tall:
    if elem == 5:
        fem_i_listen = True

if fem_i_listen:
    print("Tallet 5 er i listen.")
else:
    print("Tallet 5 er ikke i listen.")
