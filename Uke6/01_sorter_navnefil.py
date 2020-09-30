"""
06.01: Sorter fil-info
"""

navn = open('01_navn.txt', "r")

personer = []
hunder = []

for linje in navn:
    biter = linje.strip("\n")
    splitt = biter.split(" ")

    if splitt[0] == "P":
        personer.append(splitt[1])
    elif splitt[0] == "H":
        hunder.append(splitt[1])
    else:
        print("Feilinformasjon!")

print(personer)
print(hunder)
