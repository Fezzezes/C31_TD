from tkinter import *

from tour import Tour
from creep import Creep
from projectile import Projectile



class Vue:
    def __init__(self, controle, modele):
        self.controle = controle # parent
        self.modele = modele
        self.root = Tk()
        self.root.title("Tower Defense")
        self.dict_amelioration = {"default": "***cout;***desc;****tour"}
        ##creation  des interfaces graphiques
        self.dict_interfaces = {}
        self.creer_interfaces()

    def creer_interfaces(self):
        self.creer_frame_aire_jeu()
        self.creer_frame_menu()

    def creer_frame_aire_jeu(self):
        canvas_aire_jeu = Canvas(self.root, width=self.modele.unite_base * 32,
                                 height=self.modele.unite_base * 19,
                                 bg="SpringGreen4")

        # frame_aire_jeu.bind("<Button>", self.test_tags)
        canvas_aire_jeu.pack()
        self.dict_interfaces.update({"c_jeu": canvas_aire_jeu})

        bouton_construction = Button(canvas_aire_jeu, text="construction",
                                     font=("Arial", 14), fg="blue", bg="lightgray", padx=10, pady=5,
                                     command=self.test_toggle_construction)

        bouton_amelioration = Button(canvas_aire_jeu, text="amelioration",
                                     font=("Arial", 14), fg="blue", bg="lightgray", padx=10, pady=5,
                                     command=self.test_toggle_amelioration)

        bouton_construction.place(relx=0.6, rely=0.1, anchor="center", relheight=0.1, relwidth=0.1)
        bouton_amelioration.place(relx=0.8, rely=0.1, anchor="center", relheight=0.1, relwidth=0.1)
        self.dict_interfaces.update({"b_construction": bouton_construction})
        self.dict_interfaces.update({"b_amelioration": bouton_amelioration})


    def creer_frame_menu(self):
        frame_menu = Frame(self.root, width=self.modele.unite_base * 32,
                           height=self.modele.unite_base * 5, bg="light slate gray")

        frame_menu.pack()
        self.dict_interfaces.update({"f_menu": frame_menu})
        # self.creer_frame_vague()
        self.creer_frame_construction()
        self.creer_frame_amelioration()
        # self.creer_frame_ressource()

    def creer_frame_construction(self):

        ub = self.modele.unite_base
        frame_construction = Frame(self.dict_interfaces["f_menu"],
                                   width=ub * 12,
                                   height=ub * 4, bd=2,
                                 highlightthickness=2, relief="sunken", bg="sea green")

        frame_construction.place(x=10 * ub, y=5)

        bouton_projectile = Button(frame_construction,
                                   text="tour à projectile",
                                   font=("Arial", 14,), bg="RoyalBlue4",
                                   padx=10, pady=5,
                                   wraplength=ub * 2,fg="white",
                                   command=lambda: self.construire_tour(
                                       "projectile"))
        bouton_eclair = Button(frame_construction, text="tour à éclair",
                               font=("Arial", 14), fg="light yellow", bg="goldenrod",
                               padx=10, pady=5,
                               wraplength=ub * 2,
                               command=lambda: self.construire_tour("éclair"))
        bouton_poison = Button(frame_construction, text="tour de poison",
                               font=("Arial", 14), fg="white", bg="DarkOrchid4",
                               padx=10, pady=5,
                               wraplength=ub * 2,
                               command=lambda: self.construire_tour("poison"))

        bouton_projectile.place(relx=0.2, rely=0.5, anchor="center",
                                relheight=0.5, relwidth=0.2)
        bouton_eclair.place(relx=0.5, rely=0.5, anchor="center", relheight=0.5,
                            relwidth=0.2)
        bouton_poison.place(relx=0.8, rely=0.5, anchor="center", relheight=0.5,
                            relwidth=0.2)

        self.dict_interfaces.update({"f_construction": frame_construction})
        self.dict_interfaces.update({"b_projectile": bouton_projectile})
        self.dict_interfaces.update({"b_eclair": bouton_eclair})
        self.dict_interfaces.update({"b_poison": bouton_poison})
        pass

    def creer_frame_amelioration(self):
        ub = self.modele.unite_base
        cout, desc, tour = self.split_string_amelioration(
            self.dict_amelioration["default"])
        frame_amelioration = Frame(self.dict_interfaces["f_menu"],
                                   width=ub * 12,
                                   height=ub * 4, bg="purple")

        self.dict_interfaces.update({"f_amelioration": frame_amelioration})

        canvas_upgrade = Canvas(frame_amelioration, width=ub * 2,
                                height=ub * 2, bg="blue")

        canvas_upgrade.place(relx=0.2, rely=0.5, anchor="center",
                             relheight=0.5, relwidth=0.2)

        self.dict_interfaces.update({"c_upgrade": frame_amelioration})
        label_cout = Label(canvas_upgrade, text=cout,
                           font=("Arial", 14), fg="blue", bg="teal", padx=10,
                           pady=5,
                           wraplength=ub * 2)
        label_desc = Label(canvas_upgrade, text=desc,
                           font=("Arial", 14), fg="blue", bg="red", padx=10,
                           pady=5,
                           wraplength=ub * 2)

        label_cout.place(relx=0, rely=0, anchor="nw", relheight=0.3,
                         relwidth=1)
        label_desc.place(relx=0, rely=0.3, anchor="nw", relheight=0.7,
                         relwidth=1)

        bouton_upgrade = Button(frame_amelioration, text="Upgrade",
                                wraplength=ub * 2, command=self.upgrade)
        label_tour = Label(frame_amelioration, text=tour,
                           font=("Arial", 14), fg="blue", bg="gray", padx=10,
                           pady=5,
                           wraplength=ub * 2)

        bouton_upgrade.place(relx=0.5, rely=0.5, anchor="center",
                             relheight=0.5, relwidth=0.2)
        label_tour.place(relx=0.8, rely=0.5, anchor="center", relheight=0.5,
                         relwidth=0.2)

        self.dict_interfaces.update({"b_upgrade": bouton_upgrade})
        self.dict_interfaces.update({"l_am_cout": label_cout})
        self.dict_interfaces.update({"l_am_desc": label_desc})
        self.dict_interfaces.update({"l_am_tour": label_tour})
        # frame_amelioration.place(x=6 * ub, y=5)
        pass

    def afficher_troncons(self):
        jeu = self.dict_interfaces["c_jeu"]
        for t in self.modele.troncons:
            jeu.create_rectangle(t.posX, t.posY, (t.posX + t.largeur), (t.posY + t.hauteur),
                                 tags=("troncon", "permanent"),
                                 fill="salmon4", outline='')
            if t == self.modele.troncons[-1]:
                jeu.create_rectangle(t.posX, t.posY, (t.posX + t.largeur), (t.posY + t.hauteur),
                                     tags=("troncon", "permanent"),
                                     fill="gold", outline='')




    def animer_jeu(self):
        jeu = self.dict_interfaces["c_jeu"]
        self.modele.deplacer_objets()
        objets = jeu.find_all()
        for o in objets:
            tags = jeu.gettags(o)
            if "permanent" not in tags:
                jeu.delete(o)

        for o in self.modele.objets_animer:
            if isinstance(o, Creep):
                self.dessine_creep(o)
            elif isinstance(o, Projectile):
                self.dessine_projectile(o)

    def dessine_creep(self, creep):
        ub = self.modele.unite_base
        jeu = self.dict_interfaces["c_jeu"]

        jeu.create_oval(creep.posX, creep.posY, creep.posX + ub / 2, creep.posY + ub / 2,
                        fill="LavenderBlush4", tags=("creep",), outline='')

    def dessine_projectile(self, p):

        jeu = self.dict_interfaces["c_jeu"]
        if p.type == "projectile":
            jeu.create_oval(p.posX, p.posY,
                            p.posX + p.taille, p.posY + p.taille / 2,
                            fill=p.couleur, tags=("projectile", p.posX, p.posY))
        elif p.type == "eclair":
            self.frame_aire_jeu.create_line(p.posX, p.posY, p.cibleX, p.cibleY, fill='yellow', width=6, tags=("projectile", p.posX, p.posY))

        elif p.type == "laser":
            self.frame_aire_jeu.create_oval(p.posX, p.posY,
                                            p.posX + p.taille, p.posY + p.taille,
                                            fill=p.couleur, tags=("projectile", p.posX, p.posY))
        elif p.type == "poison":
            self.frame_aire_jeu.create_oval(p.posX, p.posY,
                                            p.posX + p.taille, p.posY + p.taille,
                                            fill="green", tags=("projectile", p.posX, p.posY))
        pass


    def dessiner_tour(self, index: str, tour: Tour):
        tag = "id_" + index
        self.dict_interfaces["c_jeu"].create_rectangle(tour.posX_1, tour.posY_1,
                                                       tour.posX_2, tour.posY_2,
                                                       fill="pink",
                                                       tags=(tag, "permanent"), outline='')

    def construire_tour(self, type: str):
        print(type)
        self.dict_interfaces["c_jeu"].bind("<Motion>",
                                           self.afficher_tour_temporaire)
        self.dict_interfaces["c_jeu"].bind("<Button-1>",
                                           lambda event, t=type: self.desactiver_tour_temporaire(event, t))

    def desactiver_tour_temporaire(self, evt, type: str) -> None:
        print(type)
        self.dict_interfaces["c_jeu"].unbind("<Motion>")
        self.dict_interfaces["c_jeu"].unbind("<Button-1>")
        self.retirer_tour_temporaire(evt, type)

    def retirer_tour_temporaire(self, evt, type: str) -> None:
        # Attention, si la taille de la tour change il faudra changer ici.
        x1, y1, x2, y2 = (evt.x, evt.y, (evt.x + self.modele.unite_base),
                          (evt.y + self.modele.unite_base))
        item_overlap = self.dict_interfaces["c_jeu"].find_overlapping(x1, y1,
                                                                      x2, y2)
        for item in item_overlap:
            if "permanent" in self.dict_interfaces["c_jeu"].gettags(item):
                return
        self.controle.creer_tour(x1, y1, type)

    def afficher_tour_temporaire(self, evt) -> None:
        self.dict_interfaces["c_jeu"].delete("temporaire")
        self.dict_interfaces["c_jeu"].create_rectangle(evt.x, evt.y,
                                                       evt.x + 20, evt.y + 20,
                                                       fill="red",
                                                       tags="temporaire")

    def upgrade(self):
        pass

    def split_string_amelioration(self, str_am):
        cout = str_am.split(";", 2)[0]
        desc = str_am.split(";", 2)[1]
        tour = str_am.split(";", 2)[2]
        print(cout)
        print(desc)
        print(tour)

        return [cout, desc, tour]
        pass

    def test_toggle_construction(self):
        print("showing construction")
        self.toggle_interface("f_amelioration", "f_construction")

    def test_toggle_amelioration(self):
        print("showing amelioration")
        self.toggle_interface("f_construction", "f_amelioration")

    def toggle_interface(self, remove, show):
        self.dict_interfaces[remove].place_forget()
        self.dict_interfaces[show].place(x=6 * self.modele.unite_base, y=5)
        pass

    def test_tour_detection(self):
        # crée un tour
        t1 = Tour(self.modele, 380, 400, "projectile")
        self.modele.tours.append(t1)
        self.dict_interfaces["c_jeu"].create_rectangle(t1.posX_1, t1.posY_1, t1.posX_2, t1.posY_2,
                                                            tags=("id_12", "t_poison", "lvl_2", "tour", "permanent"),

                                                            fill="pink")
        print("x1: ", t1.centreX+t1.dectetion_range)
        print("y1: ", t1.centreY+t1.dectetion_range)
        print("x2: ", t1.centreX-t1.dectetion_range)
        print("y2: ", t1.centreY-t1.dectetion_range)
        self.dict_interfaces["c_jeu"].create_oval(t1.centreX+t1.dectetion_range, t1.centreY+t1.dectetion_range,
                        t1.centreX-t1.dectetion_range, t1.centreY-t1.dectetion_range,
                         tags=("range", "permanent"))

        self.dict_interfaces["c_jeu"].create_oval(t1.centreX+t1.dectetion_range, t1.centreY+t1.dectetion_range,
                        t1.centreX-t1.dectetion_range, t1.centreY-t1.dectetion_range,
                         tags=("range", "permanent"))

        pass

    # def test_projectile(self):
    #     print("test projectile")
    #     jeu = self.dict_interfaces["c_jeu"]
    #
    #     bouton_projectile = Button(jeu, text="pew pew", font=("Arial", 14), fg="blue", bg="gray", padx=10, pady=5,
    #                                wraplength=self.modele.unite_base * 2, command=self.creer_projectile)
    #
    #     bouton_projectile.place(relx=0.1, rely=0.8, anchor="center", relheight=0.1, relwidth=0.1)

    def test_tour_et_projectile(self):
        self.test_tour_detection()
        # self.test_projectile()
        pass

    # def creer_projectile(self):
    #     print(self.modele.creeps)
    #     creep = self.modele.creeps[0]
    #     proc = Projectile(0, 0, creep)
    #     print(proc)
    #     self.modele.objets_animer.append(proc)
    #     # self.modele.objets_animer(proc)
    #     pass

