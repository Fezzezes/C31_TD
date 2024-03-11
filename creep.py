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
        self.posX = random.randint(int(self.t.minX+self.taille), int(self.t.maxX-self.taille))
        self.vitesse = 2

    def trouver_cible(self):

        x = random.randint(self.t.minX, self.t.maxX)
        y = random.randint(self.t.minY, self.t.maxY)

        newCible = x, y
        # print("cible: ")
        print(x, y)
        return newCible

    def deplacement(self):
        dirX = self.cibleX - self.posX
        dirY = self.cibleY - self.posY
        distance = math.sqrt(dirX ** 2 + dirY ** 2)

        if distance != 0:
            dirX /= distance
            dirY /= distance

        self.posX += int(dirX * self.vitesse)
        self.posY += int(dirY * self.vitesse)

    def deplacer(self):

        #BUG ICI, la posX est plus grande que cibleX, mais posY est plus petit que cibleY ???? speed/try-catch
        #:[ NEED TO FIX THAT
        if self.posY >= self.cibleY and self.posX >= self.cibleX:
            print("cible atteint! :D")
            self.currentT = self.currentT + 1
            # try:
            self.t = self.parent.troncons[self.currentT]
            self.cibleX, self.cibleY = self.trouver_cible()
            # except IndexError:
            #     print("UN CREEP EST RENTRE DANS LE CHATEAU D:<")
            #     self.isAlive = False
                # CATCH ERROR ICI, SI PAS DE NEXT => --VIE + DELETE CREEP?


        # print("troncon: ",self.currentT)
        # print("pos avant: ", self.posX / self.parent.unite_base, self.posY / self.parent.unite_base)
        # print("cible ",self.cibleX/self.parent.unite_base, self.cibleY/self.parent.unite_base)
        self.deplacement()

        # print("pos apres dep: ",self.posX/self.parent.unite_base, self.posY/self.parent.unite_base)
