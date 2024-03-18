import math


class Helper(object):
    def getAngledPoint(angle, longueur, cx, cy):
        x = (math.cos(angle) * longueur) + cx
        y = (math.sin(angle) * longueur) + cy
        return x, y

    getAngledPoint = staticmethod(getAngledPoint)

    def calcAngle(x1, y1, x2, y2):
        dx = x2 - x1
        dy = y2 - y1
        angle = (math.atan2(dy, dx))
        # retourne l'angle en radian
        return angle

    calcAngle = staticmethod(calcAngle)

    def calcDistance(x1, y1, x2, y2):
        dx = (x2 - x1) ** 2  # strip abs FAIT
        dy = (y2 - y1) ** 2
        distance = math.sqrt(dx + dy)
        return distance

    calcDistance = staticmethod(calcDistance)

    def calculer_rayon(taille: float) -> float:
        return taille / 2 * math.sqrt(2)

    calculer_rayon = staticmethod(calculer_rayon)

    def calculer_diagonale(taille: float) -> float:
        return math.sqrt(2) * taille

    calculer_diagonale = staticmethod(calculer_diagonale)

    def calculer_point_median(pos: int, taille: float) -> float:
        return pos + Helper.calculer_diagonale(taille) / 2

    calculer_point_median = staticmethod(calculer_point_median)
