"""
06.06: Middagskalender

"""
import random
matfil = open("06_matliste.txt", "r")
matplan = open("06_matplan.txt", "w")

def lesInnMatFil(fil):
    liste = []

    for linje in fil:
        innerListe = []
        biter = linje.strip("\n")
        splitt = biter.split(",")

        innerListe.append(splitt[0])
        innerListe.append(splitt[1])
        liste.append(innerListe)

    return liste

matListe = lesInnMatFil(matfil)

def velgMatrett(n):
    nMatretter = []
    for i in range(n):
        mat = matListe[random.randrange(len(matListe))]
        nMatretter.append(mat)
    return nMatretter

matRetter = velgMatrett(3)

def skrivMatretterTilFil(fil):
    for matrett in matRetter:
        fil.write(matrett[0] + ", " + matrett[1] + "\n")

skrivMatretterTilFil(matplan)
