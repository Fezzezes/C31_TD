from creep import Creep
from troncon import Troncon
from time import sleep



class Modele:
    def __init__(self, controle):

        self.controle = controle
        self.unite_base = 40
        self.troncons = []
        self.creeps = []
        self.objets_animer = []
        self.CREEP_PAR_NIVEAU = 20
        self.niveau = 0
        self.COOLDOWN_VAGUE = 5
        self.argent = 0
        self.ARGENT_PAR_NIVEAU = 100

    def creer_troncons(self):
        ub = self.unite_base  #largeur,h
        self.troncons.append(
            Troncon(self, 5 * ub, 0, 2 * ub, 16 * ub,
                    "down"))
        # self.troncons.append(
        #     Troncon(self, 5 * ub, 15 * ub, 2 * ub, 2 * ub,
        #              "right"))
        self.troncons.append(
            Troncon(self, 5 * ub, 15 * ub, 8 * ub, 2 * ub,
                     "right"))
        self.troncons.append(
            Troncon(self, 11 * ub, 4 * ub, 2 * ub, 13 * ub,
                     "up"))
        # self.troncons.append(
        #     Troncon(self, 11 * ub, 6 * ub, 2 * ub, 9 * ub,
        #             "up"))
        self.troncons.append(
            Troncon(self, 11 * ub, 4 * ub, 17 * ub, 2 * ub,
                    "right"))
        # self.troncons.append(
        #     Troncon(self, 13 * ub, 4 * ub, 15 * ub, 2 * ub,
        #             "right"))
        self.troncons.append(
            Troncon(self, 28 * ub, 4 * ub, 2 * ub, 7 * ub,
                    "down"))
        # self.troncons.append(
        #     Troncon(self, 28 * ub, 6 * ub, 2 * ub, 3 * ub,
        #             "down"))
        self.troncons.append(
            Troncon(self, 19 * ub, 9 * ub, 11 * ub, 2 * ub,
                    "left"))
        # self.troncons.append(
        #     Troncon(self, 21 * ub, 9 * ub, 7 * ub, 2 * ub,
        #            "left"))
        self.troncons.append(
            Troncon(self, 19 * ub, 9 * ub, 2 * ub, 8 * ub,
                  "down"))
        # self.troncons.append(
        #     Troncon(self, 19 * ub, 11 * ub, 2 * ub, 4 * ub,
        #             "down"))
        self.troncons.append(
            Troncon(self, 19 * ub, 15 * ub, 10 * ub, 2 * ub,
                    "right"))
        # self.troncons.append(
        #     Troncon(self, 21 * ub, 15 * ub, 8 * ub, 2 * ub,
        #             "right"))

        print(self.troncons)
        pass




    def deplacer_creeps(self):
        ## deplace chaque creep
        for c in self.creeps:
            c.deplacer()

        pass

    def init_vague(self) -> None:
        self.niveau += 1
        self.argent += self.ARGENT_PAR_NIVEAU
        for creep in range(self.CREEP_PAR_NIVEAU):
            c = Creep(self)
            self.creeps.append(c)
            self.objets_animer.append(c)
        # self.compte_rebours(self.COOLDOWN_VAGUE) # attention, fonction bloquante
        # self.lancer_vague()
        # animer_jeu() -> c'est lancer_vague qui a cette méthode

    def compte_rebours(self, temps_sec: int) -> None:
        while temps_sec > 0:
            print(f"Temps: {temps_sec}")
            sleep(temps_sec)
            temps_sec -= 1

