from rorbu import Rorbu
from gjest import Gjest

def hovedprogram():
    ep1 = Rorbu()
    ep2 = Rorbu()

    ep1 = ep2

    for i in range(50):
        ep1.nyGjest(Gjest())

    print(ep1.hentAntallGjester())
    print(ep2.hentAntallGjester())

    for i in range(75):
        ep2.nyGjest(Gjest())

    print(ep1.hentAntallGjester())
    print(ep2.hentAntallGjester())

    ep1.fortellVits(10)
    ep1.fortellVits(200)
    ep1.fortellVits(400)

    print(ep2.hvorMorsomtHarViDet())



hovedprogram()
