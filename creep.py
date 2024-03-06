class Creep:
    def __init__(self, parent):
        self.parent = parent
        self.isAlive = True
        self.isWalking = False
        self.taille = self.parent.unite_base / 2
        self.couleur = "blue"
        self.vitesseX = 3
        self.vitesseY = 3
        self.currentT = 0
        self.t = self.parent.troncons[self.currentT]
        self.limitXmin = self.t.posX
        self.limitXmax = self.t.posX + self.t.largeur
        self.limitYmin = self.t.posY
        self.limitYmax = self.t.posY + self.t.hauteur
        self.posX = self.t.posX
        self.posY = self.t.posY
        self.dir = self.t.dir

        self.cibleY = self.t.posY + self.t.largeur -10
        self.cibleX = self.t.posX


    def collision(self):
        if self.posX < self.limitXmin or self.posX + self.taille > self.limitXmax:
            self.vitesseX *= -1

        if self.posY < self.limitYmin or self.posY + self.taille > self.limitYmax:
            self.vitesseY *= -1

    def changer_cible(self):

        if self.t.dir == "right":
            if self.posX > self.cibleX:
                print("changer cible")
                self.currentT += 1
                self.t = self.parent.troncons[self.currentT]

            self.limitXmax = self.t.posX + self.t.largeur
            self.limitXmin = self.t.posX
            self.limitYmin = self.t.posY
            self.limitYmax = self.t.posY + self.t.hauteur
            self.cibleY = self.t.posY
            self.vitesseX = 1
            self.vitesseY = 1
            self.cibleX = self.posX + self.t.largeur

        elif self.t.dir == "down":
            if self.posY > self.cibleY and self.posX == self.cibleX:
                self.currentT += 1
                self.t = self.parent.troncons[self.currentT]

            self.limitXmin = self.t.posX
            self.limitXmax = self.t.posX + self.t.largeur
            self.limitYmin = self.t.posY
            self.limitYmax = self.t.posY + self.t.hauteur
            self.posX = self.t.posX
            self.posY = self.t.posY
            self.dir = self.t.dir

            self.cibleY = self.t.posY + self.t.largeur
            self.cibleX = self.t.posX





    def deplacer(self):
        # collision dans autre methode
        self.collision()
        print(self.cibleX)
        print(self.cibleY)
        print(self.t.dir)

        self.changer_cible()

        self.posX = self.posX + self.vitesseX
        self.posY = self.posY + self.vitesseY

        print(self.posY, self.posY)
