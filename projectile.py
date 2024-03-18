from helper import Helper as hp
import math


class Projectile:
    def __init__(self, parent, creep):

        self.parent = parent
        self.type = parent.type
        # valeur à balancer
        self.taille = 20
        self.couleur = "yellow"
        self.speed = 100

        # position de départ
        self.posX = parent.centreX
        self.posY = parent.centreY

        # cible du projectile
        self.creep_cible = creep
        self.cibleX = creep.posX
        self.cibleY = creep.posY

        self.angle = None
        self.dist_precedente = hp.calcDistance(self.posX, self.posY, self.cibleX, self.cibleY)
        self.trajet_fini = False


    def trouver_cible(self):
        # trouve l'angle vers la cible
        self.angle = hp.calcAngle(self.posX, self.posY, self.cibleX, self.cibleY)
        # self.speed =

    def deplacer(self):
        # deplace vers la cible
        if self.angle is None:
            self.trouver_cible()
            if self.type != "éclair":
                # permet d'afficher le projectile au moins une fois si la cible est très proche de la tour
                self.posX, self.posY = hp.getAngledPoint(self.angle, self.speed/2, self.posX, self.posY)
        else:
            self.posX, self.posY = hp.getAngledPoint(self.angle, self.speed, self.posX, self.posY)
            dist = self.calcule_distance_fin_trajectoire(self.posX, self.posY, self.cibleX, self.cibleY)
            # si la distance est plus petite que la vitesse, next cible
            print("fin de la trajectoire?", dist, "<= ", self.speed / 3, " ? ", (dist <= self.speed / 4))
            if dist <= self.speed / 3 or dist > self.parent.range_detection:
                self.posX, self.posY = self.cibleX, self.cibleY
                self.trajet_fini = True
                
    def calcule_distance_fin_trajectoire(self, x1, y1, x2, y2):

        dx = (x2 - x1) ** 2  # strip abs FAIT
        dy = (y2 - y1) ** 2
        distance = math.sqrt(dx + dy)
        # si un projectile dépasse sa cible (du à une grande vitesse), la valeur de la distance augmentera,
        # logiquement ceci indiquerait que le projectile a fini son trajet
        if self.dist_precedente < distance:
            return 0
        else:
            self.dist_precedente = distance
        return distance

    def impact(self):
        print("Impacte")
        self.parent.parent.impact_projectile(self)
        # self.parent.modele.projectiles.remove(self)
        pass
