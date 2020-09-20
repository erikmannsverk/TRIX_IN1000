"""
04.12: String-liste

a) Lag en liste som inneholder tekststrenger.
b) Lag en løkke som går like mange ganger som listen er lang. (Hint: Bruk en teller i en løkke).
c) Les inn tekst fra brukeren og lagre det i listen. Skriv ut listen for å se om programmet fungerer.

"""

strengListe = ["Mann", "Dame", "Gutt", "Venn", "Potet", "Pizza"]

teller = 0

while teller < len(strengListe):
    print(f"Indeks: {teller} : {strengListe[teller]} ")
    teller += 1

brukerStreng = input("Ord i listen: ")
strengListe.append(brukerStreng)

print(strengListe)
