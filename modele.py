from troncon import Troncon


class Modele:
    def __init__(self, controle):
        self.controle = controle
        self.unite_base = 40
        self.troncons = []

    def creer_troncons(self):
        self.troncons.append(
            Troncon(self, 5*self.unite_base,0,2*self.unite_base, 16*self.unite_base, 16*self.unite_base))
        self.troncons.append(
            Troncon(self, 5 * self.unite_base, 15*self.unite_base, 2 * self.unite_base, 2 * self.unite_base, 14*self.unite_base))
        self.troncons.append(
            Troncon(self, 7 * self.unite_base, 15*self.unite_base, 4 * self.unite_base, 2 * self.unite_base, 5 * self.unite_base))
        self.troncons.append(
            Troncon(self, 11 * self.unite_base, 15*self.unite_base, 2 * self.unite_base, 2 * self.unite_base, 5 * self.unite_base))
        self.troncons.append(
            Troncon(self, 11 * self.unite_base, 6*self.unite_base, 2 * self.unite_base, 9 * self.unite_base, 5 * self.unite_base))
        self.troncons.append(
            Troncon(self, 11 * self.unite_base, 4*self.unite_base, 2 * self.unite_base, 2 * self.unite_base, 5 * self.unite_base))
        self.troncons.append(
            Troncon(self, 13 * self.unite_base, 4*self.unite_base, 15 * self.unite_base, 2 * self.unite_base, 5 * self.unite_base))
        self.troncons.append(
            Troncon(self, 28 * self.unite_base, 4*self.unite_base, 2 * self.unite_base, 2 * self.unite_base, 5 * self.unite_base))
        self.troncons.append(
            Troncon(self, 28 * self.unite_base, 6*self.unite_base, 2 * self.unite_base, 3 * self.unite_base, 5 * self.unite_base))
        self.troncons.append(
            Troncon(self, 28 * self.unite_base, 9 * self.unite_base, 2 * self.unite_base, 2 * self.unite_base, 5 * self.unite_base))
        self.troncons.append(
            Troncon(self, 21 * self.unite_base, 9 * self.unite_base, 7 * self.unite_base, 2 * self.unite_base, 5 * self.unite_base))
        self.troncons.append(
            Troncon(self, 19 * self.unite_base, 9 * self.unite_base, 2 * self.unite_base, 2 * self.unite_base, 5 * self.unite_base))
        self.troncons.append(
            Troncon(self, 19 * self.unite_base, 11 * self.unite_base, 2 * self.unite_base, 4 * self.unite_base,5 * self.unite_base))
        self.troncons.append(
            Troncon(self, 19 * self.unite_base, 15 * self.unite_base, 2 * self.unite_base, 2* self.unite_base,5 * self.unite_base))
        self.troncons.append(
            Troncon(self, 21 * self.unite_base, 15 * self.unite_base, 8 * self.unite_base, 2* self.unite_base,5 * self.unite_base))

        print(self.troncons)
        pass