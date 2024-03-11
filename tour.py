import math
from math import sqrt


class Tour:
    def __init__(self, parent, posX_1: int, posY_1: int, type: str):
        self.parent = parent
        self.taille = self.parent.unite_base *10000
        self.posX_1 = posX_1
        self.posY_1 = posY_1
        self.posX_2 = posX_1 + self.calculer_diagonale()
        self.posY_2 = posY_1 + self.calculer_diagonale()
        self.centreX = self.calculer_point_median(self.posX_1)
        self.centreY = self.calculer_point_median(self.posY_1)
        self.rayon = self.calculer_rayon(self.taille)
        self.type = type
        self.niveau = 1
        self.cooldown_base = 100;
        self.cooldown = 0;


    def calculer_diagonale(self) -> float:
        return sqrt(2) * self.taille

    def calculer_point_median(self, pos: int) -> float:
        return pos + self.calculer_diagonale() / 2

    def calculer_rayon(self, taille:float)->float:
        return taille/2 * math.sqrt(2)

    def detecter_creep(self):
        # pour chaque creep du modele
        print("scanning for trouble")
        for c in self.parent.creeps:
            if c.isAlive:
                distX = self.centreX - self.calculer_point_median(c.posX)
                distY = self.centreY - self.calculer_point_median(c.posY)
                dist = distX**2 + distY**2
                print(dist ," <= " ,(self.rayon + self.calculer_rayon(c.taille)))
                if dist <= self.rayon + self.calculer_rayon(c.taille):
                    self.attaquer_creep(c)

    def attaquer_creep(self, creep):
        print("pew pew pew")
        if self.cooldown <= 0:
            self.parent.creer_projectile(self, creep)
            self.cooldown = self.cooldown_base
        else:
            self.cooldown -= 1

