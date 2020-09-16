"""
03.13: Ordbok med flaggfarger
"""

# Ordbok med navn som nøkkelverdier
flaggOrdbok = {
"norge" : ["rødt", "hvitt", "blått"],
"sverige" : ["blått", "gult"],
"danmark" : ["rødt", "hvitt"],
"finland" : ["hvitt", "blått"],
"japan" : ["rødt", "hvitt"],
"gabon" : ["grønt", "gult", "blått"],
"storbritannia" : ["rødt", "blått", "hvitt"],
"chile" : ["blått", "hvitt", "rødt"]
}

# Legger til et nytt land og fargene på flagget
flaggOrdbok["tyskland"] = ["gult", "rødt", "svart"]

#
def velgLand():
    land = input("Hvilket lands farger vil du se? ").lower()

    if land in flaggOrdbok:
        print(flaggOrdbok[land])
    else:
        print(f"Beklager, {land} står desverre ikke på listen.")
    startFun()

def startFun():
    start = input("Skriv START hvis du vil starte, skriv EXIT hvis du vil avslutte: ").lower()

    if start == "start":
        velgLand()
    elif start == "exit":
        exit()
    else:
        print("Beklager, det forsto jeg ikke helt")
        startFun()

startFun()
