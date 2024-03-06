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
        self.creer_frame_menu()

    def creer_frame_aire_jeu(self):
        canvas_aire_jeu = Canvas(self.root, width=self.modele.unite_base * 32,
                                 height=self.modele.unite_base * 19, bg="orange")

        # frame_aire_jeu.bind("<Button>", self.test_tags)
        canvas_aire_jeu.pack()
        self.dict_interfaces.update({"c_jeu": canvas_aire_jeu})

    def creer_frame_menu(self):
        frame_menu = Frame(self.root, width=self.modele.unite_base * 32,
                           height=self.modele.unite_base * 5, bg="red")

        frame_menu.pack()
        self.dict_interfaces.update({"f_menu": frame_menu})
        # self.creer_frame_vague()
        self.creer_frame_construction()
        # self.creer_frame_amelioration()
        # self.creer_frame_ressource()

    def creer_frame_construction(self):

        ub = self.modele.unite_base
        frame_construction = Frame(self.dict_interfaces["f_menu"], width=ub * 12,
                                   height=ub * 4, bg="blue")

        frame_construction.place(x=6 * ub, y=5)

        label_projectile = Button(frame_construction, text="tour à projectile",
                                  font=("Arial", 14), fg="blue", bg="gray", padx=10, pady=5,
                                  wraplength=ub * 2, command=self.construire_tour_projectile)
        label_eclair = Button(frame_construction, text="tour à éclair",
                              font=("Arial", 14), fg="blue", bg="lightgray", padx=10, pady=5,
                              wraplength=ub * 2, command=self.construire_tour_eclair)
        label_poison = Button(frame_construction, text="tour de poison",
                              font=("Arial", 14), fg="blue", bg="gray", padx=10, pady=5,
                              wraplength=ub * 2, command=self.construire_tour_poison)

        label_projectile.place(relx=0.2, rely=0.5, anchor="center", relheight=0.5, relwidth=0.2)
        label_eclair.place(relx=0.5, rely=0.5, anchor="center", relheight=0.5, relwidth=0.2)
        label_poison.place(relx=0.8, rely=0.5, anchor="center", relheight=0.5, relwidth=0.2)

        self.dict_interfaces.update({"f_construction": frame_construction})
        pass

    def afficher_troncons(self):
        jeu = self.dict_interfaces["c_jeu"]
        for t in self.modele.troncons:
            jeu.create_rectangle(t.posX, t.posY, (t.posX + t.largeur), (t.posY + t.hauteur), tags=("troncon",),
                                 fill="red")

    def animer_jeu(self):
        self.modele.deplacer_creeps()
        jeu = self.dict_interfaces["c_jeu"]
        objets = jeu.find_all()
        for o in objets:
            tags = jeu.gettags(o)
            if "troncon" not in tags:
                jeu.delete(o)

        for o in self.modele.objets_animer:
            self.dessine_creep(o)

    def dessine_creep(self, creep):
        ub = self.modele.unite_base
        jeu = self.dict_interfaces["c_jeu"]
        jeu.create_oval(creep.posX, creep.posY, ub / 2, ub / 2, fill="red", tags=("creep",))

    def construire_tour_projectile(self):
        pass

    def construire_tour_eclair(self):
        pass

    def construire_tour_poison(self):
        pass
