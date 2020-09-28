"""
05.03: Returverdier

a)
returnerer 5 og printer 5

b)
returnerer inputet og printer det

c)
reutrnerer ingenting og printer None
"""

# A)
def sum(a, b):
    return a + b

x = sum(2, 3)
print(x)


# B)
def hent_brukernavn():
    navn = input("Skriv inn brukernavn: ")
    return navn

x = hent_brukernavn()
print(x)


# C)
def jeg_returnerer_ingenting():
    x = 1 + 2

x = jeg_returnerer_ingenting()
print(x)
