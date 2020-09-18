"""
04.03: Minst og størst
"""

tall = [6, -4, 7, -2, 8, -3, 9, -11]

minst = tall[0]
for i in tall:
    if i < minst:
        minst = i
    print(minst)

print(minst)

print()

størst = tall[0]
for e in tall:
    if e > størst:
        størst = e
    print(størst)

print(størst)
