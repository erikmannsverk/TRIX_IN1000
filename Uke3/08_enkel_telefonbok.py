"""
03.11: Enkel telefonbok
"""

# Navn fylt inn i telefonboken samt. telefonnummer.
telefonbok = {"Arne":22334455, "Lisa":95959595, "Jonas":97959795, "Peder":12345678}

navn = input("Skriv inn et fornavn: ").capitalize()

if navn in telefonbok:
    print(telefonbok[navn])
else:
    print("Navnet du har oppgitt finnes ikke i denne telefonboken.")
