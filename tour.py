from math import sqrt


class Tour:
    def __init__(self, parent, posX_1: int, posY_1: int, type: str):
        self.parent = parent
        self.taille = self.parent.unite_base / 2
        self.posX_1 = posX_1
        self.posY_1 = posY_1
        self.posX_2 = posX_1 + self.calculer_diagonale()
        self.posY_2 = posY_1 + self.calculer_diagonale()
        self.centreX = self.calculer_point_median(self.posX_1)
        self.centreY = self.calculer_point_median(self.posY_1)
        self.type = type
        self.niveau = 1

    def calculer_diagonale(self) -> float:
        return sqrt(2) * self.taille

    def calculer_point_median(self, pos: int) -> float:
        return pos + self.calculer_diagonale() / 2

    # fonction qui concatène le type ET le niveau et qui retourne une string
