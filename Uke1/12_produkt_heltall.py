"""
Lag et program som ber om og leser inn to heltall. Programmet skal deretter regne ut produktet av de to tallene og skrive ut svaret.
"""

# Problem: input skriver ut verdien av inputtet som en string og ikke et tall. Det blir derfor ikke mulig å summere/multiplisere.
print('GANGEKALKULATOR!!!')

# Bruker int() for å omgjøre inputet fra en string til et integral!:D
print('Oppgi verdien til x:')
x = int(input('>'))
print('Oppgi verdien til y:')
y = int(input('>'))

print('Produktet av x og y =', x * y)


""" LØSNINGSFORSLAG
x = int(input('Oppgi verdien til x:\n>'))
y = int(input('Oppgi verdien til y:\n>'))
print('Produktet av x og y =', x * y)
"""
