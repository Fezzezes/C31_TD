from modele import *
from vue import *
from tkinter import *


class Controleur:
    def __init__(self):
        self.modele = Modele(self)
        self.vue = Vue(self, self.modele)
        self.initialise_partie()
        self.vue.root.mainloop()

    def initialise_partie(self):
        print("initpartie")
        self.modele.creer_troncons()
        self.vue.afficher_troncons()
        self.modele.init_vague()  # crée un problème, le jeu s'affiche après
        pass

    def animer_jeu(self):
        self.modele.deplacer_creeps()
        self.vue.animer_jeu()
        self.vue.root.after(50, self.animer_jeu)

    def creer_tour(self, posX: int, posY: int, type: str) -> None:
        index, tour = self.modele.creer_tour(posX, posY, type)
        self.vue.dessiner_tour(str(index), tour)


if __name__ == "__main__":
    c = Controleur()
