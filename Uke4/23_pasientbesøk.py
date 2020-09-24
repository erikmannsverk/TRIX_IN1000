"""
04.23: Pasientbesøk

"""
listeEn = [[31], [14, 15, 16, 17, 18]]
listeTo = [[1,2,3], [2, 3, 4], [28, 31], [14, 15, 16, 17, 18]]
listeTre = [[1,2,3], [2, 3, 4], [28, 31], [14, 15, 16, 17, 18], [1, 2, 4, 5], [9, 12, 16, 19], [21, 23, 25, 27, 28]]

def maxBesok(liste):
    max = len(liste[0])

    for pasient in range(len(liste)):
        if len(liste[pasient]) > max:
            max = pasient

    return max + 1

def minBesok(liste):
    min = len(liste[0])

    for pasient in range(len(liste)):
        if len(liste[pasient]) < min:
            min = pasient

    return min + 1

def alleBesok(liste):
    sum = 0

    for besok in liste:
        for dag in besok:
            sum += 1

    return sum

def hvemVarPaaDato(liste):
    dato = int(input("Dato 1 - 31: "))

    pasientNummer = 0
    pasientListe = []

    for pasient in liste:
        pasientNummer += 1
        for besøk in pasient:
            if besøk == dato:
                pasientListe.append(pasientNummer)

    return pasientListe

antallBesokTo = alleBesok(listeTo)
maxListeTo = maxBesok(listeTo)
minListeTo = minBesok(listeTo)
hvemVarTo = hvemVarPaaDato(listeTo)
print(f"Max besøk pasient:{maxListeTo}")
print(f"Min besøk pasient:{minListeTo}")
print(f"Alle besøk: {antallBesokTo}")
print(f"På valgte dato var pasient {hvemVarTo} tilstede.")
