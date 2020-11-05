
class Node:
    neste = None

    def __init__(self, tall):
        self._tall = tall


class Lenkeliste:
    forsteNode = None

    def __init__(self):
        pass

    def leggTilNode(self):
        if self.forsteNode == None:
            self.forsteNode = node
            return

        # Hvis vi er her så har vi en lenkeliste å jobbe med
        jobbNode = self.forsteNode

        harPlassertNode = False

        while harPlassertNode == False:
            # Startsjekk (kan være at det første tallet er større)
            if jobbNode.tall > node.tall:
                node.neste = jobbNode
                self.forsteNode = node
                return

            # Sjekk om vi er på slutten
            if jobbNode.neste == None:
                jobbNode.neste = node
                return


            # Sjekk om vi kan plassere noden inn etter jobbNoden
            if jobbNode.neste.tall > node.tall:
                # Vi skal legge inn noden på jobbNode.neste sin plass
                tmpNode = jobbNode.neste

                jobbNode.neste = node
                node.neste = tmpNode
                harPlassertNode = True

            jobbNode = jobbNode.neste

    def printLenkeliste(self):
            jobbNode = self.forsteNode

            while jobbNode != None:
                print(jobbNode.tall)
                jobbNode = jobbNode.neste


"""
Skjønte ikke en dritt
"""
