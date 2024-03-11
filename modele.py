import time

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
        self.CREEP_PAR_NIVEAU = 3  # SWITCH BACK A 20
        self.tours = []
        self.niveau = 0
        self.COOLDOWN_VAGUE = 5
        self.argent = 5
        self.ARGENT_PAR_NIVEAU = 100
        self.creepBouge = 1

    def creer_troncons(self):
        ub = self.unite_base  # x, y, largeur, hauteur, maxX,minX,maxY,minY):

        self.troncons.append(
            Troncon(self,
                    5 * ub,
                    0,
                    2 * ub,
                    16 * ub,
                    6 * ub,
                    16 * ub))

        self.troncons.append(
            Troncon(self,
                    5 * ub,
                    15 * ub,
                    8 * ub,
                    2 * ub,
                    12 * ub,
                    16 * ub))


        self.troncons.append(
            Troncon(self,
                    11 * ub,
                    4 * ub,
                    2 * ub,
                    13 * ub,
                    12 * ub,
                    5 * ub))


        self.troncons.append(
            Troncon(self,
                    11 * ub,
                    4 * ub,
                    17 * ub,
                    2 * ub,
                    29 * ub,
                    5 * ub))


        self.troncons.append(
            Troncon(self,
                    28 * ub,
                    4 * ub,
                    2 * ub,
                    7 * ub,
                    29 * ub,
                    10 * ub))


        self.troncons.append(
            Troncon(self,
                    19 * ub,
                    9 * ub,
                    11 * ub,
                    2 * ub,
                    20 * ub,
                    10 * ub))

        self.troncons.append(
            Troncon(self,
                    19 * ub,
                    9 * ub,
                    2 * ub,
                    8 * ub,
                    20 * ub,
                    16 * ub))


        self.troncons.append(
            Troncon(self,
                    19 * ub,
                    15 * ub,
                    10 * ub,
                    2 * ub,
                    30 * ub,
                    16 * ub))
        pass

    def deplacer_creeps(self):
        for c in self.creeps:
            c.deplacer()


    def deplacer_objets(self):
        for o in self.objets_animer:
            o.deplacer()

        pass

    def init_vague(self) -> None:
        self.niveau += 1
        self.argent += self.ARGENT_PAR_NIVEAU
        self.lancer_vague()

    def compte_rebours(self, temps_sec: int) -> None:
        while temps_sec > 0:
            print(f"Temps: {temps_sec}")
            sleep(temps_sec)
            temps_sec -= 1

    def mourir(self, creep):
        index = self.creeps.index(creep)
        indexObject = self.objets_animer.index(creep)
        self.argent += 5
        del self.creeps[index]
        del self.objets_animer[indexObject]


    def timer(self):
        start = time.time()
        a = True
        while a:
            currentTime = time.time()
            if currentTime - start >= 5:
                print("time's up")
                a = False
        pass

    def lancer_vague(self):
        for creep in range(self.CREEP_PAR_NIVEAU):
            c = Creep(self)
            self.creeps.append(c)
            self.objets_animer.append(c)
        

        self.controle.animer_jeu()  # -> c'est lancer_vague qui a cette méthode

        #  self.compte_rebours(self.COOLDOWN_VAGUE)  # attention, fonction bloquante

    def detecter_creeps(self):
        # loop au travers de chaque tour
        for tour in self.tours:
            tour.detecter_creep(self.creeps)


