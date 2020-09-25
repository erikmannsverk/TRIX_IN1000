"""
04.27 Prosedyrer URL

I denne oppgaven skal du lage en prosedyren netSok som tar inn et argument. Dette argumentet skal være navnet på en nettside. Prosedyren skal legge til www. og ".no" og print det ut. Slik at et kall med "NRK" som argument vill printe ut www.NRK.no
"""

def netSok(nettsideNavn):
    print("www." + nettsideNavn + ".no")

netSok("NRK")
