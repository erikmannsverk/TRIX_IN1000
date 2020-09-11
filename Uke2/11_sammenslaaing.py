"""
02.15: Kodeforståelse

"""

# A) Vil få en feil siden int og str ikke kan printes ut sammen med +

a = 10
b = 'Hei'
c = str(a) + b
print(c)


# B) Funker siden begge er 'str'
x = '10'
y = 'Hei'
print(x + y)

# C) Går ikke. Samme som oppgave A)
i = 10
j = int('12')
print(i + j)
