"""
04.17 Enkle prosedyrer og funksjoner

a) Skriv en prosedyre velkommen som tar imot en variabel bruker som parameter og skriver ut en velkomstmelding med dette navnet. Test prosedyren ved å be bruker om en tekststreng brukernavn og kalle på velkommen med dette som parameter.

b) Skriv en funksjon strenginator(streng1, streng2) som legger sammen (konkatenerer) to strenger med et mellomrom og returnerer den sammenslåtte strengen. Kall på metoden med to strenger med verdi du velger selv og legg returverdien i en konkatenert. Skriv ut konkatenert til terminal.
"""

# A
def velkommen(navn):
    print(f"Velkommen, {navn}!")


brukernavn = input("Hva heter du? ").capitalize()
velkommen(brukernavn)

# B
def strenginator(streng1, streng2):
    streng3 = streng1 + " " + streng2

    return streng3

konkatenert = strenginator("Hei", "Erik")
print(konkatenert)
