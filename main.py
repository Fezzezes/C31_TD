from modele import *
from vue import *
from tkinter import *


class Controleur:
    def __init__(self):

        self.tempsDebut= time.time()
        self.compteur=0
        self.modele = Modele(self)
        self.vue = Vue(self, self.modele)
        self.tempcurrent = self.modele.tempsPasse(self.tempsDebut)
        self.initialise_partie()

        self.vue.root.mainloop()

    def initialise_partie(self):
        self.modele.creer_troncons()
        self.vue.afficher_troncons()
        self.modele.init_vague()
        # self.vue.test_tour_et_projectile()

        pass

    def ameliorerTour(self, t):
        self.modele.ameliorerTour(t)

    def ajouterCreep(self):
        if self.modele.creepBouge < self.modele.CREEP_PAR_NIVEAU:
            self.modele.ajouterCreep()

    def animer_jeu(self):
        if self.modele.tempsPasse(self.tempsDebut) > 5:
            self.modele.detecter_creeps()
            self.vue.animer_jeu()
            self.compteur += 1
            if self.modele.creepCreer < self.modele.CREEP_PAR_NIVEAU and self.compteur % 20 == 1:  # change 20 pour ralenir ou accelerer
                self.modele.ajouterCreep()

        self.vue.root.after(50, self.animer_jeu)
        print(self.modele.tempsPasse(self.tempsDebut))

    def verifier_argent(self, type: str) -> bool:
        return self.modele.verifier_argent(type)

    def creer_tour(self, posX: int, posY: int, type: str) -> None:
        index, tour = self.modele.creer_tour(posX, posY, type)
        self.vue.dessiner_tour(str(index), tour)


if __name__ == "__main__":
    c = Controleur()
