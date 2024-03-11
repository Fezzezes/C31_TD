import math
import random


class Creep:
    def __init__(self, parent):
        self.parent = parent
        self.isAlive = True
        self.isWalking = False
        self.taille = self.parent.unite_base / 2
        self.currentT = 0
        self.t = self.parent.troncons[self.currentT]
        self.couleur = "blue"
        self.cibleX, self.cibleY = self.trouver_cible()
        self.posY = 0
        self.posX = self.cibleX
        self.vitesse = 10

    def trouver_cible(self):

        newCible = self.t.cibleX, self.t.cibleY
        print("cible: ")
        print(self.t.cibleX, self.t.cibleY)
        return newCible

    def deplacement(self):
        dirX = self.cibleX - self.posX
        dirY = self.cibleY - self.posY
        distance = math.sqrt(dirX ** 2 + dirY ** 2)

        if distance <= 2:
            self.currentT = self.currentT + 1
            try:
                self.t = self.parent.troncons[self.currentT]
                self.cibleX, self.cibleY = self.trouver_cible()
            except IndexError:
                print("ARRIVER AU CHATEAU")
                self.parent.mourir(self)

            exit

        if distance != 0:
            dirX /= distance
            dirY /= distance

        dirY = round(dirY)
        dirX = round(dirX)

        self.posX += int(dirX * self.vitesse)
        self.posY += int(dirY * self.vitesse)

    def deplacer(self):

        self.deplacement()

