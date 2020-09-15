"""
03.04: Enkel tegning
"""
# a )importere GraphicsWindow fra modulen ezgraphics.
from ezgraphics import GraphicsWindow

# b) Opprett et grafikkvindu og lagre det med navnet win.
win = GraphicsWindow()

# c) Opprett et kanvas og lagre det med navnet canvas.
canvas = win.canvas()

# d) Så skal du bruke kode til å tegne et enkelt rektangel. Gjør det ved å skrive følgende linje inn i programmet ditt:
canvas.drawRectangle(x,20,100,75)

# e) Hvis du kjører programmet nå vil tegningen du lager forsvinne med en gang. For å unngå dette kan du skrive følgende linje nederst i koden:
win.wait()

# f) Test programmet ditt. Du kan lukke vinduet du får opp ved å trykke på krysset øverst i høyre hjørne. Prøv å endre verdiene til drawRect() og se hvordan det forandrer tegningen din.
