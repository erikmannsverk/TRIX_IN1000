class Elev:
    def __init__(self, navn):
        self._navn = navn

    def __eq__(self, annenElev):
        return self._navn == annenElev._navn

stinaA = Elev("Stina")
stinaB = Elev("Stina")
stinaC = stinaA

print(stinaA == stinaB)
print(stinaA is stinaB)
print(stinaA == stinaC)
print(stinaA is stinaC)
print(stinaB == stinaC)
print(stinaB is stinaC)

stinaA = Elev("Stina")

print(stinaA == stinaB)
print(stinaA is stinaB)
print(stinaA == stinaC)
print(stinaA is stinaC)
print(stinaB == stinaC)
print(stinaB is stinaC)

"""
1. True
2. False
3. True
4. False (True)
5. True
6. False

7. True
8. False
9. True
10. False
11. True
12. False
"""
