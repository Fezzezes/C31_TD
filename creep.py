import math
import random
from helper import Helper as hp


class Creep:
    def __init__(self, parent):
        self.parent = parent
        self.taille = self.parent.unite_base / 2
        self.currentT = 0
        self.isAlive= True
        self.t = self.parent.troncons[self.currentT]
        self.couleur = "blue"
        self.cibleX, self.cibleY = self.trouver_cible()
        self.posY = 0
        self.posX = self.cibleX
        self.vitesse = 7
        self.vie = 15
        self.poison = 0
        self.acide = 0

    def degat(self, degat):
        self.vie -= degat
        if self.vie <= 0:
            self.parent.tuer_creep(self)

    def trouver_cible(self):
        newCible = self.t.cibleX, self.t.cibleY
        return newCible

    def atteindre_chateau(self):
        self.parent.atteindre_chateau()
        self.parent.retirer_creep(self)

    def deplacement(self):
        dirX = self.cibleX - self.posX
        dirY = self.cibleY - self.posY
        distance = hp.calcDistance(self.posX, self.posY, self.cibleX, self.cibleY)

        if distance <= self.vitesse:
            self.currentT = self.currentT + 1
            try:
                self.t = self.parent.troncons[self.currentT]
                self.cibleX, self.cibleY = self.trouver_cible()
            except IndexError:
                print("ARRIVER AU CHATEAU")
                self.atteindre_chateau()
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
