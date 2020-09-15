"""
03.03: String-liste med måneder
"""

måned = ["Januar", "Februar", "Mars", "April", "Mai", "Juni", "Juli", "August",  "September", "Oktober", "November", "Desember"]

tallBruker = int(input("Heltall (1-12): ")) - 1

if (tallBruker > 0 and tallBruker < 13):
    print(f'Måneden du har valgt er {måned[tallBruker]}.')
else:
    print("Ugyldig nummer.")
