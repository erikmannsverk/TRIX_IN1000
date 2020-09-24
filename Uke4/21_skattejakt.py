"""
04.21: Skattejakt

"""
import time

def lagSkattekart(size):
    skattekart = []

    for e in range(size):
        a = []

        for e in range(size):
            a.append("O")

        skattekart.append(a)

    return skattekart

skattekart = lagSkattekart(5)

def tegnSkattekart(skattekart):
    for e in skattekart:
        for i in e:
            print(i, end = "")
            # end = "" sørger for at vi ikke får linjeskift enda
        print("")

tegn = tegnSkattekart(skattekart)

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

inputGodkjent_1 = False
while inputGodkjent_1 != True:

    x_spiller1 = input(f"X (1 - {len(skattekart)}): ")
    y_spiller1 = input(f"Y (1 - {len(skattekart)}): ")

    if is_number(x_spiller1) and is_number(y_spiller1):
        xs_1 = int(x_spiller1)
        ys_1 = int(y_spiller1)

        if xs_1 <= len(skattekart) and ys_1 <= len(skattekart) and xs_1 > 0 and ys_1 > 0:
            inputGodkjent_1 = True
            x_1 = xs_1 - 1
            y_1 = ys_1 - 1
        else:
            print("********************************")
            print(f"x: %s{xs_1} og y: %s{ys_1} er ikke godkjent" %("",""))
            print("********************************")
    else:
        print("********************************")
        print(f"x: %s'{x_spiller1}' og y: %s'{y_spiller1}' er ikke godkjent" %("",""))
        print("********************************")

skattekart[y_1][x_1] = "X"
nyTegn = tegnSkattekart(skattekart)

for linjeskift in range(5):
    print()
    print("LOADING")
    time.sleep(0.5)
    linjeskift = "\n"
    for e in range(3):
        print(linjeskift)
        time.sleep(0.1)

print(f"Hei spiller 2. Du skal nå gjette hvilke av de {(len(skattekart))*len(skattekart)} rutene spiller 1 har valgt:D")
print()
print("Lykke til!")

feilsvar = 0
inputGodkjent_2 = False
while inputGodkjent_2 != True:
    if feilsvar == 3:
        print("Spiller 1 vinner. Her er fasiten:")
        tegnSkattekart(skattekart)
        inputGodkjent_2 = True
    else:
        print(f"Forsøk {feilsvar + 1}: ")
        x_spiller2 = input(f"X (1 - {len(skattekart)}): ")
        y_spiller2 = input(f"Y (1 - {len(skattekart)}): ")

        if is_number(x_spiller2) and is_number(y_spiller2):
            xs_2 = int(x_spiller2)
            ys_2 = int(y_spiller2)

            if xs_2 <= len(skattekart) and ys_2 <= len(skattekart) and xs_2 > 0 and ys_2 > 0:
                x_2 = xs_2 - 1
                y_2 = ys_2 - 1
                if x_1 == x_2 and y_1 == y_2:
                    inputGodkjent_2 = True
                    tegnSkattekart(skattekart)
                    print("Gratulerer! Du gjettet riktig!\nSpiller 2 vinner:D")
                else:
                    feilsvar += 1
                    print("")

            else:
                feilsvar += 1
                print("********************************")
                print(f"x: %s{xs_2} og y: %s{ys_2} er ikke godkjent" %("",""))
                print(f"Du har {3-feilsvar} forsøk igjen.")
                print("********************************")
        else:
            feilsvar += 1
            print("********************************")
            print(f"x: %s'{x_spiller2}' og y: %s'{y_spiller2}' er ikke godkjent" %("",""))
            print(f"Du har {3-feilsvar} forsøk igjen.")
            print("********************************")
