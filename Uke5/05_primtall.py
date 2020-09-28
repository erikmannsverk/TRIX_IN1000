"""
05.05: Primtall lavere enn N
"""

def primtallUnder():
    tallBruker = int(input("Tall: "))
    primtall = []

    for element in range(1, tallBruker):
        teller = 0
        for tall in range(2, (element//2 + 1)):
            if (element % tall == 0):
                teller += 1
                break

        if(teller == 0 and element != 1):
            primtall.append(element)

    return primtall

print(primtallUnder())
