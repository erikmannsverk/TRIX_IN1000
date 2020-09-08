"""
Skriv et program der du ber om brukerinput på ett eller flere trivia-spørsmål. Hvis du ikke kommer på et spørsmål får du et gratis her: "Hva heter hovedstaden i Marokko?" (svaret er "Rabat").

Lagre det rette svaret i en tekststreng.

Skriv en if-test for å sjekke om brukeren har svart rett på spørsmålet. Hvis de har svart riktig skal programmet skrive ut "Helt rett!". Hvis ikke skal programmet skrive ut "Beklager, svaret var" og deretter det riktige svaret du har lagret.
"""

# Skriver ut spørsmålet i terminalen, samt. lar brukeren selv skrive ut sitt svar som et input.
print('Whos the president of USA?')
answ = input()

# Input lar brukeren selv velge sitt svar, for deretter å sjekke om svaret er korrekt
right_answ = 'Donald Trump'

if answ == right_answ:
    print('Your answear is right!!!')
else :
    print('Sorry, the right answear was:', right_answ )
