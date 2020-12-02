"""
11.05: Personsystem
"""
class Person:
    def __init__(self, navn):
        self._navn = navn

    def hentNavn(self):
        return self._navn

class Personsystem:

    def __init__(self):
        self._listePersoner = []

    def leggTilPerson(self, personObjekt):
        self._listePersoner.append(personObjekt)

    def finnPerson(self, navn):
        for person in self._listePersoner:
            if navn.lower() == person.hentNavn().lower():
                return person
        return None


def hovedprogram():

    ps = Personsystem()

    mads = Person("Mads")
    nils = Person("Nils")
    hilde = Person("Hilde")
    bjarte = Person("Bjarte")
    karin = Person("Karin")

    listeNavn = [mads, nils, hilde, bjarte, karin]
    for navn in listeNavn:
        ps.leggTilPerson(navn)

    print(ps.finnPerson("hilde"))


hovedprogram()
