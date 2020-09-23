"""
04.18: Reverser liste

Lag en liste med verdiene 1, 2, 3, 4, 5 og 6. Lag en algoritme som reverserer listen. Forsøk å gjøre dette uten å bruke den innebygde funksjonen reversed. Gå deretter gjennom listen med en while-løkke og print ut alle verdiene.
"""

tall = [1, 2, 3, 4, 5, 6]
tall_reversert = []

storst = tall[0]

print(tall)

for elm in range(len(tall)):
    tall_reversert.append(max(tall))
    tall.remove(max(tall))

print(tall_reversert)
