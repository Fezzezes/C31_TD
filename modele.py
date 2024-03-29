import math
import time

from creep import Creep
from projectile import Projectile
from tour import Tour
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
        self.niveau = 0  # correspond à la vague
        self.COOLDOWN_VAGUE = 5
        self.vie = 20
        self.argent = 0
        self.ARGENT_PAR_NIVEAU = 200

        self.partie_active = True
        self.niveau_terminer = False
        self.creep_creation_terminer = False
        self.tempsDebut = time.time()

        self.creepCreer = 0
        self.liste_tours = []
        self.stats_tours = {
            "projectile": {
                "prix_base": 100,
                "couleur": "gray",
                "cooldown_base": 10,
                "range_detection": 100,
                "puissance": 3,
                "ameliorations": {
                    2: {
                        "cout": 50,
                        "cooldown": 5,
                        "puissance": 5,
                        "couleur": "dim gray",
                    },
                    3: {
                        "cout": 50,
                        "cooldown": 2,
                        "puissance": 7,
                        "couleur": "black",
                    },
                }
            },
            "éclair": {
                "prix_base": 100,
                "couleur": "yellow",
                "cooldown_base": 10,
                "range_detection": 100,
                "puissance": 3,
                "ameliorations": {
                    2: {
                        "cout": 50,
                        "cooldown": 0,
                        "puissance": 1,
                        "couleur": "goldenrod"
                    },
                    3: {
                        "cout": 50,
                        "cooldown":2,
                        "couleur": "dark goldenrod",
                        "puissance": 7
                    },
                }
            },
            "poison": {
                "prix_base": 100,
                "couleur": "MediumPurple3",
                "cooldown_base": 10,
                "range_detection": 100,
                "puissance": 2,
                "ameliorations": {
                    2: {
                        "cout": 50,
                        "cooldown": 5,
                        "couleur": "purple1",
                        "puissance": 5
                    },
                    3: {
                        "cout": 50,
                        "cooldown": 2,
                        "couleur": "purple4",
                        "puissance": 7
                    },
                }
            }
        }

    def ameliorerTour(self, t):
        next_level = t.niveau + 1
        if next_level <= 3:
            stats = t.ameliorations[next_level]
            if stats['cout'] <= self.argent:

                t.cooldown_base = stats['cooldown']
                t.puissance = stats['puissance']
                self.argent -= stats['cout']
                t.couleur = stats['couleur']
                t.niveau += 1
                self.controle.updateTour(t)
            else:
                print("MANQUE DE FONDS")

    def checkPoison(self):
        for c in self.creeps:
            if c.poison > 0:
                c.degat(1)
                c.poison -= 1


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

        self.troncons.append(
            Troncon(self,
                    29 * ub,
                    15 * ub,
                    2 * ub,
                    2 * ub,
                    30 * ub,
                    16 * ub))
        pass

    def deplacer_objets(self):
        # deplace tous les objets du canvas n'ayant pas le tag static
        for o in self.objets_animer:
            o.deplacer()
            if isinstance(o, Projectile) and o.trajet_fini:
                self.objets_animer.remove(o)

    def creer_tour(self, posX: int, posY: int, type: str) -> tuple[int, Tour]:
        tour = Tour(self, posX, posY, type, self.stats_tours[type])
        self.liste_tours.append(tour)
        self.argent -= self.stats_tours[type]["prix_base"]
        return len(self.liste_tours) - 1, tour

    def init_vague(self) -> None:
        self.niveau_terminer = False
        self.creepCreer = 0
        self.creep_creation_terminer = False
        self.niveau += 1
        self.argent += self.ARGENT_PAR_NIVEAU
        self.tempsDebut = time.time()
        self.tempsPasse(self.tempsDebut)


    def atteindre_chateau(self) -> None:
        if self.vie - 1 > 0:
            self.vie -= 1
            self.controle.maj_vie()
        else:
            self.partie_active = False
            self.controle.finir_partie()

    def retirer_creep(self, creep):
        try:
            index = self.creeps.index(creep)
            indexObject = self.objets_animer.index(creep)
            del self.creeps[index]
            del self.objets_animer[indexObject]
            if len(self.creeps) == 0 and self.creep_creation_terminer:
                self.niveau_terminer = True
        except ValueError:
            print("creep mort :D")

    def impact_projectile(self, projectile):
        self.objets_animer.remove(projectile)

    def tempsPasse(self, timerStart):
        tempecoule = time.time() - timerStart
        return tempecoule

    def lancer_vague(self):
        self.controle.animer_jeu()  # -> c'est lancer_vague qui a cette méthode

    def detecter_creeps(self):
        for tour in self.liste_tours:
            tour.detecter_creep()

    def creer_projectile(self, tour, creep):
        self.objets_animer.append(Projectile(tour, creep))
        pass

    def ajouterCreep(self, test):
        if self.creepCreer < self.CREEP_PAR_NIVEAU and test % 30 == 1:
            c = Creep(self)
            self.creeps.append(c)
            self.objets_animer.append(c)
            self.creepCreer += 1
            if self.creepCreer == self.CREEP_PAR_NIVEAU:
                self.creep_creation_terminer = True

    def tuer_creep(self, creep: Creep):
        self.argent += 15
        self.controle.maj_argent()
        self.retirer_creep(creep)

    def verifier_argent(self, type: str) -> bool:
        if self.argent >= self.stats_tours[type]["prix_base"]:
            return True
        else:
            return False

    def reset_objet_animer(self):
        self.objets_animer.clear()
        pass
