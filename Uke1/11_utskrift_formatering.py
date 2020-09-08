"""
1. Les om formatering av utskrift i læreboka s. 54-57 eller i Python-dokumentasjonen (https://docs.python.org/3/tutorial/inputoutput.html).
2. Skriv et program hvor du definerer to flyttallsvariabler: lengde og bredde. Gi disse variabelen verdiene 10.101 og 3.843.
3. Skriv ut følgende setning ved å bruke formatering av utskrift og de to variablene:
"""

lengde = 10.101
bredde = 3.843
s = 'Rektangelet er ' + str(lengde) + 'langt, og' + str(bredde) + 'bredt'
str(s)

print(f'Rektangelet er {lengde} langt, og {bredde} bredt.')
