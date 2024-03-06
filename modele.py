from troncon import Troncon


class Modele:
    def __init__(self, controle):
        self.controle = controle
        self.unite_base = 40
        self.troncons = []

    def creer_troncons(self):
        ub = self.unite_base
        self.troncons.append(
            Troncon(self, 5 * ub, 0, 2 * ub, 16 * ub,
                    15 * ub))
        self.troncons.append(
            Troncon(self, 5 * ub, 15 * ub, 2 * ub, 2 * ub,
                    7 * ub))
        self.troncons.append(
            Troncon(self, 7 * ub, 15 * ub, 4 * ub, 2 * ub,
                    11 * ub))
        self.troncons.append(
            Troncon(self, 11 * ub, 15 * ub, 2 * ub, 2 * ub,
                    15 * ub))
        self.troncons.append(
            Troncon(self, 11 * ub, 6 * ub, 2 * ub, 9 * ub,
                    6 * ub))
        self.troncons.append(
            Troncon(self, 11 * ub, 4 * ub, 2 * ub, 2 * ub,
                    13 * ub))
        self.troncons.append(
            Troncon(self, 13 * ub, 4 * ub, 15 * ub, 2 * ub,
                    28 * ub))
        self.troncons.append(
            Troncon(self, 28 * ub, 4 * ub, 2 * ub, 2 * ub,
                    6 * ub))
        self.troncons.append(
            Troncon(self, 28 * ub, 6 * ub, 2 * ub, 3 * ub,
                    9 * ub))
        self.troncons.append(
            Troncon(self, 28 * ub, 9 * ub, 2 * ub, 2 * ub,
                    28 * ub))
        self.troncons.append(
            Troncon(self, 21 * ub, 9 * ub, 7 * ub, 2 * ub,
                    21 * ub))
        self.troncons.append(
            Troncon(self, 19 * ub, 9 * ub, 2 * ub, 2 * ub,
                    11 * ub))
        self.troncons.append(
            Troncon(self, 19 * ub, 11 * ub, 2 * ub, 4 * ub,
                    15 * ub))
        self.troncons.append(
            Troncon(self, 19 * ub, 15 * ub, 2 * ub, 2 * ub,
                    21 * ub))
        self.troncons.append(
            Troncon(self, 21 * ub, 15 * ub, 8 * ub, 2 * ub,
                    29 * ub))

        print(self.troncons)
        pass
