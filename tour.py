import math
from math import sqrt
from helper import Helper as hp


class Tour:
    def __init__(self, parent, posX_1: int, posY_1: int, type: str):
        self.parent = parent

        self.taille = self.parent.unite_base / 2
        self.range_detection = 100
        self.posX_1 = posX_1
        self.posY_1 = posY_1
        self.posX_2 = posX_1 + hp.calculer_diagonale(self.taille)
        self.posY_2 = posY_1 + hp.calculer_diagonale(self.taille)
        self.centreX = hp.calculer_point_median(self.posX_1, self.taille)
        self.centreY = hp.calculer_point_median(self.posY_1, self.taille)
        self.rayon = hp.calculer_rayon(self.range_detection)
        self.type = type
        self.niveau = 1
        self.cooldown_base = 10
        self.cooldown = 0
        self.detecte_un_creep = False

    def detecter_creep(self):
        # pour chaque creep du modele
        for c in self.parent.creeps:
            if c.isAlive:
                distX = (self.centreX - hp.calculer_point_median(c.posX, c.taille)) ** 2
                distY = (self.centreY - hp.calculer_point_median(c.posY, c.taille)) ** 2
                dist = math.sqrt(distX + distY)
                rayon_creep = hp.calculer_rayon(c.taille)
                if dist <= (self.range_detection + rayon_creep):
                    self.detecte_un_creep = True
                    if self.cooldown <= 0:
                        self.parent.creer_projectile(self, c)
                        self.cooldown = self.cooldown_base

                    break
                else:
                    self.detecte_un_creep = False

        if self.cooldown > 0:
            self.cooldown -= 1

    # pour ameliorer: fonction qui concatène le type ET le niveau et qui retourne une string
