class Creep:
    def __init__(self, parent):
        self.parent = parent
        self.isAlive = True
        self.isWalking = False

        self.taille = 10
        self.couleur = "blue"
        self.vitesseX = 1
        self.vitesseY = 1
        self.trenconX = 0  #
        self.trenconY = 0  #
        self.largeur = 30  #
        self.hauteur = 100  #
        self.t = self.parent.troncons[1]
        self.limitXmin = self.trenconX
        self.limitXmax = self.trenconX + self.largeur
        self.limitYmin = self.trenconY
        self.limitYmax = self.trenconX + self.hauteur
        self.posX = 10
        self.posY = 10
        self.cibleY = 50
        self.cibleX = 15

    def collision(self):
        print("collision")

        if self.posX < self.limitXmin or self.posX + self.taille > self.limitXmax:
            self.vitesseX = self.vitesseX * -1

        if self.posY < self.limitYmin or self.posY + self.taille > self.limitYmax:
            self.vitesseY = self.vitesseY * -1

    def changer_cible(self):
        print("cible")
        self.t += 1
        self.vitesseX = 1
        self.limitXmax = 0
        self.limitXmax = 100
        self.limitYmin = 40
        self.limitYMax = 200

        self.cibleY = 100
        self.cibleX = 200

    def deplacer(self):
        # collision dans autre methode
        self.collision()

        if self.posX + self.taille >= self.cibleX and self.posY + self.taille >= self.cibleY:
            self.changer_cible()

        self.vitesseX = self.vitesseX + (0.003 * self.vitesseX)
        self.vitesseY = self.vitesseY + (0.003 * self.vitesseY)
        self.posX = self.posX + self.vitesseX
        self.posY = self.posY + self.vitesseY

        print(self.posY, self.posY)
        print(self.limitYmin)
