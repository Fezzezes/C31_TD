from helper import Helper as hp
import math


class Projectile:
    def __init__(self, parent, creep):

        self.parent = parent
        self.type = parent.type
        self.rayonImpact = 20 # variableee !!!!! ???

        # valeur à balancer
        self.taille = 20
        self.couleur = "yellow"
        # self.speed = 100

        # position de départ
        self.posX = parent.centreX
        self.posY = parent.centreY

        # cible du projectile
        self.creep_cible = creep

        self.cibleX = hp.calculer_point_median(creep.posX, creep.taille)
        self.cibleY = hp.calculer_point_median(creep.posY, creep.taille)

        self.angle = None
        self.dist_precedente = hp.calcDistance(self.posX, self.posY, self.cibleX, self.cibleY)
        self.trajet_fini = False

    def trouver_cible(self):
        # trouve l'angle vers la cible
        self.angle = hp.calcAngle(self.posX, self.posY, self.cibleX, self.cibleY)
        dist = self.calcule_distance_fin_trajectoire(self.posX, self.posY, self.cibleX, self.cibleY)
        # pour conserver une animation fluide, on calcule la vitesse idéale pour qu'un projectile atteigne le creep
        self.speed = dist/(self.creep_cible.taille/(self.creep_cible.vitesse*1.5))

    def deplacer(self):
        # deplace vers la cible
        if self.angle is None:
            self.trouver_cible()
        else:
            self.posX, self.posY = hp.getAngledPoint(self.angle, self.speed, self.posX, self.posY)
            dist = self.calcule_distance_fin_trajectoire(self.posX, self.posY, self.cibleX, self.cibleY)
            # si la distance est plus petite que la vitesse, next cible
            # print("fin de la trajectoire?", dist, "<= ", self.speed / 3, " ? ", (dist <= self.speed / 4))
            if dist <= 0 or dist > self.parent.range_detection:
                self.posX, self.posY = self.cibleX, self.cibleY
                self.trajet_fini = True
                self.impact()

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
        distance= hp.calcDistance(self.cibleX,self.cibleY, self.creep_cible.posX,self.creep_cible.posY)

        if distance <= self.rayonImpact:
            if self.type == "poison":
                self.creep_cible.poison += self.parent.puissance#variable de projectile

            else:
                self.creep_cible.degat(self.parent.puissance)  #variable de projectile




