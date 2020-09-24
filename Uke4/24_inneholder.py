"""
04.24 Inneholder

"""

def innholdSjekk(stringEn, stringTo):
    teller = 0

    if len(stringEn) == len(stringEn):
        for bokstav in stringEn:
            if bokstav in stringTo:
                teller += 1
                stringTo.replace(bokstav, '')
        if len(stringEn) == teller:
            return True
        else:
            return False
    else:
        return False

streng_1 = input("Skriv et ord: ").lower()
streng_2 = input("Skriv et ord: ").lower()
svar = innholdSjekk(streng_1, streng_2)
print(svar)
