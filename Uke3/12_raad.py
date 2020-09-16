"""
03.18: Har du råd?

"""

#
def harDuRaad():
    saldo = float(input("Hva er saldoen din?\n> "))
    total = float(input("Hva er totalprisen på varen du vil kjøpe?\n> "))
    pengerIgjen = saldo - total

    if pengerIgjen > 0:
        print(f"Du har råd!\nDu har {pengerIgjen} kr igjen på konto.")
    else:
        print(f"Du har ikke råd ...\nDu mangler {round(pengerIgjen*-1, 2)} kr.")

harDuRaad()
