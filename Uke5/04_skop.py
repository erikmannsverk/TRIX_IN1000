"""
05.04: Skop

a)
a lagres i variabelen a, prosedyre_en kjøres men returnerer ingen ting, så printes "en tekst!". Så printes b.

b)
Error siden b ikke er definert

c)
printer "hei".
printer "hei verden". 
"""


# A)
a = "En tekst!"
def prosedyre_en(parameter):
    parameter = parameter + "12"

prosedyre_en(a)
print (a)

b = 10
print (b)


# B)
def prosedyre_to():
    b = b + 10

prosedyre_to()
print(b)


# C)
c = "hei"
print (c)

def funksjon_en(parameter):
    parameter = parameter + "verden"
    return parameter

print (funksjon_en(c))
