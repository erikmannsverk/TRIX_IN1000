"""

05.01: Lesing fra fil

"""

navn = open('01_navn.txt', 'r')
navneListe = []

for linje in navn:
    biter = linje.strip()
    navneListe.append(biter)

navn.close()

print(navneListe)
