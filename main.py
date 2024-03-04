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
        self.modele.creer_troncons()
        self.vue.afficher_troncons()
        pass

if __name__ == "__main__":
    c = Controleur()
