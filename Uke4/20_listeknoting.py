"""
04.20: Listeknoting


Skriv en funksjon vanligKonkat som konkatenerer to lister. Dersom du har to lister: [a, b, c] og [1, 2, 3], skal listen som funksjonen returnerer se slik ut: [a, b, c, 1, 2, 3]. Ikke bruk den innebygde concat-funksjonen.

Skriv funksjonen annenhverKonkat som konkatenerer to lister slik: gitt [a, b, c] og [1, 2, 3] så skal funksjonen returnere listen: [a, 1, b, 2, c, 3].

Skriv funksjonen listesum som returnerer summen av alle tallene i en liste. Dvs. listen [5, 3, 10] skal returnere 18.

Skriv en funksjon tallTilListe som returnerer en liste med siffer gitt et tall. Dvs. tallet 895 skal returnere listen [8, 9, 5].

Utfordring! Skriv en funksjon erPalindrom som sjekker om et ord er et palindrom (et ord som gir samme resultat enten det leses fra høyre eller venstre).

"""

def vanligKonkat(liste1, liste2):
    return liste1 + liste2

def annenhverKonkat(liste1, liste2):
    nyListe = []

    for elm in range(len(liste1)):
        nyListe.append(liste1[elm])
        nyListe.append(liste2[elm])

    return nyListe

def listeSum(liste):
    return sum(liste)

def tallTilListe(tall):
    return list(tall)

def erPalindrom(ord):
    listeOrd = list(ord)
    listeOrd2 = list(ord)
    listeOrd2.reverse()

    if listeOrd == listeOrd2:
        print("Palindrom")
        return ord
    else:
        print("Ikke Palindrom")
        return None

erPalindrom("anna")
a = annenhverKonkat(["1","2","3"], ["a","b","c"])
print(a)
