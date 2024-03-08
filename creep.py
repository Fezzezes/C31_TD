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
        self.posY = 0
        self.posX = random.randint(self.t.minX, self.t.maxX)
        self.cibleX, self.cibleY = self.trouver_cible()
        self.vitesse=3


    def trouver_cible(self):

        x= random.randint(self.t.minX, self.t.maxX)
        y= random.randint(self.t.minY, self.t.maxY)
        newCible= x,y
        print(x,y)
        return newCible

    def calculer_vitesse(self):
        dirX= self.cibleX -self.posX
        dirY= self.cibleY-self.posY
        distance= math.sqrt(dirX**2 + dirY**2)

        if distance!=0:
            dirX/=distance
            dirY/=distance

        self.posX+=int (dirX*self.vitesse)
        self.posY=int (dirY*self.vitesse)

    def deplacer(self):

        if(self.posY==self.cibleY and self.posX==self.cibleX):
            self.trouver_cible()

        else:
           print(self.posY, self.posY)
           self.calculer_vitesse()

        print(self.posY, self.posY)
