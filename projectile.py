from helper import Helper as hp


class Projectile:
    def __init__(self, parent, x, y, creep):

        self.parent = parent
        self.type = type
        # valeur à balancer
        self.taille = 10
        self.couleur = "yellow"
        self.speed = 5

        # position de départ
        self.posX = parent.x1
        self.posY = parent.y2

        # cible du projectile
        self.creep_cible = creep
        self.cibleX = creep.posX
        self.cibleY = creep.posY

        self.angle = None
        self.trouver_cible()

    def trouver_cible(self):
        # trouve l'angle vers la cible
        self.angle = hp.calcAngle(self.posX, self.posY, self.cibleX, self.cibleY)

    def deplacer(self):
        # deplace vers la cible
        if self.type != "eclair":
            self.posX, self.posY = hp.getAngledPoint(self.angle, self.speed, self.posX, self.posY)

        dist = hp.calcDistance(self.posX, self.posY, self.cibleX, self.cibleY)
        # si la distance est plus petite que la vitesse, next cible
        if dist <= self.speed / 3:
            self.impact()

    def impact(self):
        print("Impacte")
        # self.parent.modele.projectiles.remove(self)
        pass
