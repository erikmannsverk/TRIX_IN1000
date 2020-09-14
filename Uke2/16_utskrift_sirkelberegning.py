import math

#
rad = float(input("Radius: "))
dia = rad * 2
areal = (rad ** 2) * math.pi
omkrets = dia * math.pi
print(f'Diameter:{dia:10.2f}')
print(f'Areal:{areal:13.2f}')
print(f'Omkrets:{omkrets:11.2f}')
