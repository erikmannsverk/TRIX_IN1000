"""
02.20: Busstur
"""

st1 = input("Stasjon 1! Hvor mange går på bussen?\n> ")
st2 = input("Stasjon 2! Hvor mange går på bussen?\n> ")
st3 = input("Stasjon 3! Hvor mange går på bussen?\n> ")
plass = int(st1) + int(st2) + int(st3)

if plass <= 30:
    print("Bussen har " + str(30 - plass) + " ledige plasser. Bussen kjører!")
else:
    print("Bussen er full. " + str(plass - 30) + " må gå til fots.")
