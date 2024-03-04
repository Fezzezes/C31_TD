from tkinter import *


class Vue:
    def __init__(self, controle, modele):
        self.controle = controle
        self.modele = modele
        self.dict_interfaces = {}
        self.root = Tk()
        print("hi")

        self.root.title("Test TD")
        self.creer_interfaces()

    def creer_interfaces(self):
        self.creer_frame_aire_jeu()

    def creer_frame_aire_jeu(self):

        frame_aire_jeu = Canvas(self.root, width=self.modele.unite_base * 32,
                                     height=self.modele.unite_base * 19, bg="orange")

        # frame_aire_jeu.bind("<Button>", self.test_tags)
        frame_aire_jeu.pack()
        self.dict_interfaces.update({"f_jeu": frame_aire_jeu})