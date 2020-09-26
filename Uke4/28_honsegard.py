"""
04.28: Hønsegården
"""

antHons = int(input("Hvor mange høner bor i gården? "))
teller = 1

while antHons >= 0:
    print()
    rev = input(f"Natt {teller}: Kommer reven? ").lower()
    bonde = input(f"Natt {teller}: Sover bonden? ").lower()
    print()

    if rev == "ja":
        if bonde == "ja":
            antHons -= 1
            print(f"Det bor nå {antHons} høns i gaarden.")
        else:
            print(f"Det bor nå {antHons} høns i gaarden. Bonden selger ett reveskinn, og tjener 190 kr.")
    else:
        print(f"Det bor fortsatt {antHons} høns i gaarden.")

    teller += 1
