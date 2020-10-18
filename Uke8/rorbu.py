from gjest import Gjest

class Rorbu:

    def __init__(self):
        self._gjester = []

    def nyGjest(self, gjest):
        for gjesten in self._gjester:
            gjesten = Gjest()
            gjesten.underhold(1)

        gjest = Gjest()
        self._gjester.append(gjest)

    def fortellVits(self, morsomhet):
        for gjest in self._gjester:
            gjest.underhold(morsomhet)

    def hvorMorsomtHarViDet(self):
        sum = 0
        for gjest in self._gjester:
            sum += gjest.hentUnderholdningsverdi()

        summen = sum/len(self._gjester)

        if summen < 200:
            return "Kjedelig kveld"
        elif summen >= 200 and summen < 400:
            return "Dette var jo litt gøy"
        elif summen >= 400 and summen < 600:
            return "Dette var artig"
        elif summen > 600:
            return "Dra på Lopphavet - bi dæ godtar no så gyt e!"
