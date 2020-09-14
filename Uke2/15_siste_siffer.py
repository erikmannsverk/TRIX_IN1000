"""
02.21: Finn ut om siste siffer er felles

"""

a, b, c = 44, 31, 24

sisteSiffer_a = a%10
sisteSiffer_b = b%10
sisteSiffer_c = c%10

if sisteSiffer_a == sisteSiffer_b and sisteSiffer_a == sisteSiffer_c:
    print("A, B  og C har det samme siste sifferet: " + str(sisteSiffer_a))
elif sisteSiffer_a == sisteSiffer_b:
    print("A og B har det samme siste sifferet: " + str(sisteSiffer_a))
elif sisteSiffer_a == sisteSiffer_c:
    print("A og C har det samme siste sifferet: " + str(sisteSiffer_a))
elif sisteSiffer_b == sisteSiffer_c:
    print("B og C har det samme siste sifferet: " + str(sisteSiffer_a))
else:
    print("Ingen av heltallsvariablene har det samme siste sifferet.")
