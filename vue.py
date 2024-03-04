from tkinter import *


class Vue:
    def __init__(self, controle, modele):
        self.controle = controle
        self.modele = modele
        self.root = Tk()
        self.root.title("Tower Defense")
        ##creation  des interfaces graphiques
        self.dict_interfaces = {}
        self.creer_interfaces()

    def creer_interfaces(self):
        self.creer_frame_aire_jeu()

    def creer_frame_aire_jeu(self):
        frame_aire_jeu = Canvas(self.root, width=self.modele.unite_base * 32,
                                height=self.modele.unite_base * 19, bg="orange")

        # frame_aire_jeu.bind("<Button>", self.test_tags)
        frame_aire_jeu.pack()
        self.dict_interfaces.update({"f_jeu": frame_aire_jeu})

    def afficher_troncons(self):
        jeu = self.dict_interfaces["f_jeu"]
        for t in self.modele.troncons:
            jeu.create_rectangle(t.posX, t.posY, (t.posX + t.largeur), (t.posY + t.hauteur),
                                                           tags=("troncon",),
                                                           fill="red")
        pass
