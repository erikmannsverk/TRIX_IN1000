from sokk import Sokk
from skuff import Skuff

def hovedprogram():

    skuff = Skuff()

    s1 = Sokk("venstre")
    s2 = Sokk("hoyre")
    s3 = Sokk("venstre")
    s4 = Sokk("hoyre")

    skuff.settInnSokk(s1)
    skuff.settInnSokk(s2)
    skuff.settInnSokk(s3)
    skuff.settInnSokk(s4)

    skuff.sjekkStatus()




hovedprogram()
