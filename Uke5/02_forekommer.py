"""
05.02: Forekomster av tegn

"""

def forekommer(streng, tegn):
    return True if tegn in streng else False

def uten_repetisjon(streng):
    listStreng = list(streng)
    nyStreng = ""

    for tegn in listStreng:
        nyStreng += tegn
        while tegn in listStreng:
            listStreng.remove(tegn)

    return nyStreng

def antall_forskjellige(streng):
    ant = uten_repetisjon(streng)
    return len(ant) + 1

def main():

    boksForekommer = forekommer("erik", "e")
    print(boksForekommer)

    uten = uten_repetisjon("aaaaabbbaabbbbacccbcc")
    print(uten)

    ant = antall_forskjellige("qwertyuiopasdfghjkløæzxcvbnm")
    print(ant)

main()
