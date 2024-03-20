from modele import *
from vue import *
from tkinter import *


class Controleur:
    def __init__(self):

        self.tempsDebut = time.time()
        self.compteur = 0
        self.modele = Modele(self)
        self.vue = Vue(self, self.modele)

        self.initialise_partie()
        self.vue.root.mainloop()

    def initialise_partie(self):
        self.modele.creer_troncons()
        self.vue.afficher_troncons()
        self.modele.init_vague()
        self.vue.init_label(str(self.modele.argent), str(self.modele.vie), str(self.modele.niveau))
        self.modele.lancer_vague()
        # self.vue.test_tour_et_projectile()

    def ameliorerTour(self, t):
        self.modele.ameliorerTour(t)

    def updateTour(self, t):
        self.vue.dessiner_tour(str(self.modele.liste_tours.index(t)), t)
        self.maj_argent()

    def updatArgent(self, argent):
        self.vue.updateArgent(argent)

    def ajouterCreep(self):
        if self.modele.creepBouge < self.modele.CREEP_PAR_NIVEAU:
            self.modele.ajouterCreep()

    def animer_jeu(self):
        if self.modele.partie_active:
            if not self.modele.niveau_terminer:
                time = round(self.modele.tempsPasse(self.modele.tempsDebut), 0)
                if 0 < time <= 5:
                    self.maj_timer(5-time)
                if self.modele.tempsPasse(self.modele.tempsDebut) > 5:
                    self.modele.ajouterCreep(self.compteur)
                    self.modele.detecter_creeps()
                    self.modele.checkPoison()
                    self.vue.animer_jeu()
                    self.compteur += 1
                    print(self.compteur)

                self.vue.root.after(50, self.animer_jeu)
            else:

                self.prochain_niveau()
        else:
            self.vue.toggle_gameover()
            print(self.modele.tempsPasse(self.modele.tempsDebut))

    def verifier_argent(self, type: str) -> bool:
        return self.modele.verifier_argent(type)

    def creer_tour(self, posX: int, posY: int, type: str) -> None:
        index, tour = self.modele.creer_tour(posX, posY, type)
        self.vue.valeur_argent.set("ARGENT\n" + str(self.modele.argent))
        self.vue.dessiner_tour(str(index), tour)

    def maj_vie(self):
        self.vue.valeur_vie.set("VIES RESTANTES\n" + str(self.modele.vie))

    def maj_argent(self):
        self.vue.valeur_argent.set("ARGENT\n" + str(self.modele.argent))

    def maj_timer(self, time):
        self.vue.valeur_timer.set("TIMER\n" + str(time))

    def prochain_niveau(self):
        self.modele.init_vague()
        self.vue.init_label(str(self.modele.argent), str(self.modele.vie), str(self.modele.niveau))
        self.modele.reset_objet_animer()
        self.modele.lancer_vague()
        pass


if __name__ == "__main__":
    c = Controleur()
