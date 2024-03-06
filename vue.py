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
        canvas_aire_jeu = Canvas(self.root, width=self.modele.unite_base * 32,
                                 height=self.modele.unite_base * 19, bg="orange")

        # frame_aire_jeu.bind("<Button>", self.test_tags)
        canvas_aire_jeu.pack()
        self.dict_interfaces.update({"c_jeu": canvas_aire_jeu})

    def afficher_troncons(self):
        jeu = self.dict_interfaces["c_jeu"]
        for t in self.modele.troncons:
            jeu.create_rectangle(t.posX, t.posY, (t.posX + t.largeur), (t.posY + t.hauteur), tags=("troncon",),
                                 fill="red")

    def animer_jeu(self):
        self.modele.deplacer_creeps()
        jeu = self.dict_interfaces["jeu"]
        objets = jeu.find_all()
        for o in objets:
            tags = jeu.gettags(o)
            if "troncon" not in tags:
                jeu.delete(o)

        for o in self.objets_animer:
            self.dessine_creep()

    def dessine_creep(self, creep):
        ub = self.modele.unite_base
        jeu = self.dict_interfaces["jeu"]
        jeu.create_oval(creep.posX, creep.posY,self.ub/2, self.ub/2, fill="red", tags=("creep",))
