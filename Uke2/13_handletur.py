"""
02.18: Handletur
Programmet skal regne ut totalpris for en bruker etter å ha vært på handletur. De varene det er mulig å kjøpe er brød, melk, ost og yoghurt.
"""

# Gir de ulike varene gitt pris
brød, melk, ost, youghurt = 20, 15, 40, 12

print("Hei! Velkommen til IFI-butikken.")

def antall(x):
    a = int(input("Hvor mange " + x + " vil du ha?\n> "))
    return a

antBrød = antall("brød")
antMelk = antall("melk")
antOst = antall("ost")
antYog = antall("youghurt")

pris = (antBrød * brød) + (antMelk * melk) + (antOst * ost) + (antYog * youghurt)

print("Du skal betale: " + str(pris) + " kr")
