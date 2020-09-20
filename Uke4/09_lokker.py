"""

04.09: While-løkke med input

a) Lag et program som tar et tall som input fra bruker, og printer alle tall fra 0 opp til dette tallet (hint: while ...).

b) Utvid programmet med en ny while-løkke som ber om input fra bruker for hver "runde". Når brukeren taster tallet 10, skal programmet avsluttes.

"""

# Ber om tall fra bruker
tallBruker = int(input("Velg et tall: --> "))

i = 0

# Printer alle tallene fra 0 til tallBruker
while i <= tallBruker:
    print(i)
    i += 1

# Ny variabel som bruker kan modifisere senere
tallBruker_2 = 0

# Fortsetter å spørre om et nytt tall til bruker skriver 10
while tallBruker_2 != 10:
    tallBruker_2 = int(input("Velg et annet tall: --> "))

# Avslutningsmelding
print("Du tastet 10, programmet avsluttes.")
