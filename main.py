from modele import *
from vue import *
from tkinter import *


class Controleur:
    def __init__(self):
        self.testvar = False
        self.currentT = time.time()

        self.modele = Modele(self)
        self.vue = Vue(self, self.modele)
        self.initialise_partie()

        self.vue.root.mainloop()

    def initialise_partie(self):
        self.modele.creer_troncons()
        self.vue.afficher_troncons()
        self.modele.init_vague()
        self.vue.test_tour_et_projectile()
        self.currentT = time.time();
        pass

    def waitingTime(self):
        self.testvar = True
        self.animer_jeu()
        pass

    def ajouterCreep(self):
        if self.modele.creepBouge < self.modele.CREEP_PAR_NIVEAU:
            self.modele.ajouterCreep()

    def animer_jeu(self):
        if not self.testvar:
            self.vue.root.after(1000, self.waitingTime)  # change a 4000
            print(self.testvar)

        if self.testvar:
            print("dans le loop")
            self.vue.animer_jeu()

            self.ajouterCreep()
            self.vue.root.after(50, self.animer_jeu)


if __name__ == "__main__":
    c = Controleur()
