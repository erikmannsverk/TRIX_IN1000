
class Student:

    def __init__(self, navn, brukernavn, telefonnummer):
        self._navn = navn
        self._brukernavn = brukernavn
        self._telefonnummer = telefonnummer

    def printInfo(self):
        penStreng = "\n"
        penStreng += f"Navn: {self._navn}\n"
        penStreng += f"Brukernavn: {self._brukernavn}\n"
        penStreng += f"Telefonnummer: {self._telefonnummer}\n"
        print(penStreng)




def hovedprogram():
    ordliste = {}

    ordliste["erik"] = Student("Erik", "Erikrma", 91310982)
    ordliste["nils"] = Student("Nils", "Nilsern", 12321031)
    ordliste["gunnar"] = Student("Gunnar", "Gunnls", 47549299)

    for student in ordliste:
        ordliste[student].printInfo()



hovedprogram()
