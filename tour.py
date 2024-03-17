import math
from math import sqrt


class Tour:
    def __init__(self, parent, posX_1: int, posY_1: int, type: str):
        self.parent = parent
        self.taille = self.parent.unite_base / 2
        self.range_detection = self.calculer_range_detection(100)
        self.posX_1 = posX_1
        self.posY_1 = posY_1
        self.posX_2 = posX_1 + self.calculer_diagonale()
        self.posY_2 = posY_1 + self.calculer_diagonale()
        self.centreX = self.calculer_point_median(self.posX_1)
        self.centreY = self.calculer_point_median(self.posY_1)
        self.rayon = self.calculer_rayon(self.range_detection)
        self.type = type
        self.niveau = 1
        self.cooldown_base = 2
        self.cooldown = 0
        self.detecte_un_creep = False

    def calculer_diagonale(self) -> float:
        return sqrt(2) * self.taille

    def calculer_point_median(self, pos: int) -> float:
        return pos + self.calculer_diagonale() / 2

    def calculer_range_detection(self, detection_range: float) -> float:
        return detection_range * math.sqrt(2)

    def calculer_rayon(self, taille: float) -> float:
        return taille / 2 * sqrt(2)

    def detecter_creep(self):
        # pour chaque creep du modele
        # print(self.parent.creeps)
        for c in self.parent.creeps:
            if c.isAlive:
                distX = (self.centreX - self.calculer_point_median(c.posX)) ** 2
                distY = (self.centreY - self.calculer_point_median(c.posY)) ** 2
                dist = math.sqrt(distX + distY)
                rayon_creep = self.calculer_rayon(c.taille)
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
