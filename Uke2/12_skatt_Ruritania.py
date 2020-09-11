"""
02.16: Skatt i Ruritania
I det fiktive landet Ruritania er skattereglene slik at hvis en person har inntekt < 10000, så betaler man 10% skatt på hele inntekten, og hvis inntekten >= 10000, så betaler man 10% skatt på de første 10000 kronene og 30% skatt på resten av inntekten. Lag et program som regner ut og skriver ut hvor mange kroner som skal betales i skatt. Programmet skal lese inntekten (som antas å være et desimaltall) fra terminal.
"""

def skatt_Ruri():
    lønn = float(input('Hei innbygger av Ruritania, hvor mye tjener du?\n> '))
    if lønn < 10000:
        skatt = str(lønn * 0.1)
        print(skatt, 'skal betales i skatt.')
    else:
        # 1000 kr skatt for de første 10000, og 30% for det over 10000
        skatt = ((lønn - 10000) * 0.3) + 1000
        print(skatt, 'skal betales i skatt.')

skatt_Ruri()
