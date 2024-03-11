import math
from math import sqrt


class Tour:
    def __init__(self, parent, posX_1: int, posY_1: int, type: str):
        self.parent = parent
        self.taille = self.parent.unite_base/2
        self.dectetion_range = 250;
        self.posX_1 = posX_1
        self.posY_1 = posY_1
        self.posX_2 = posX_1 + self.calculer_diagonale()
        self.posY_2 = posY_1 + self.calculer_diagonale()
        self.centreX = self.calculer_point_median(self.posX_1)
        self.centreY = self.calculer_point_median(self.posY_1)
        self.rayon = self.calculer_rayon(self.dectetion_range)
        self.rayon = self.calculer_rayon(self.taille)
        self.type = type
        self.niveau = 1
        self.cooldown_base = 30
        self.cooldown = 0


    def calculer_diagonale(self) -> float:
        return sqrt(2) * self.taille

    def calculer_point_median(self, pos: int) -> float:
        return pos + self.calculer_diagonale() / 2

    def calculer_rayon(self, dectetion_range:float)->float:
        return dectetion_range/2 * math.sqrt(2)

    def detecter_creep(self):
        # pour chaque creep du modele
        for c in self.parent.creeps:
            if c.isAlive:
                print("centreX: ",self.centreX)
                print("centreY: ", self.centreY)
                print("creep centreX: ", self.calculer_point_median(c.posX))
                print("creep centreY: ", self.calculer_point_median(c.posY))
                distX = self.centreX - self.calculer_point_median(c.posX)
                distY = self.centreY - self.calculer_point_median(c.posY)
                dist = math.sqrt(distX**2 + distY**2)
                print(dist ," <= " ,(self.rayon + self.calculer_rayon(c.taille)))
                if dist <= self.rayon + self.calculer_rayon(c.taille):
                    #AJOUTER UN BREAK DU LOOP LORSQU'ON DECTECTE UN CREEP
                    if self.cooldown <= 0:
                        self.parent.creer_projectile(self, c)
                        self.cooldown = self.cooldown_base

        print(self.cooldown)
        if self.cooldown > 0:
            self.cooldown -= 1

    # def attaquer_creep(self, creep):
    #     print("pew pew pew")
    #     if self.cooldown <= 0:
    #         self.parent.creer_projectile(self, creep)
    #         self.cooldown = self.cooldown_base
    #     else:
    #         self.cooldown -= 1

    def calculer_rayon(self, taille: float) -> float:
        return taille / 2 * sqrt(2)

    # pour ameliorer: fonction qui concatène le type ET le niveau et qui retourne une string

