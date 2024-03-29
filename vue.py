from tkinter import *

from tour import Tour
from creep import Creep
from projectile import Projectile


class Vue:
    def __init__(self, controle, modele):
        self.controle = controle  # parent
        self.modele = modele
        self.root = Tk()
        self.root.title("Tower Defense")

        self.valeur_argent = StringVar()
        self.valeur_vie = StringVar()
        self.valeur_vague = StringVar()
        self.valeur_timer = StringVar()
        self.dict_amelioration = {"default": "***cout;***desc;****tour",
                                  "projectile1": "50;+Rapide\n+Power;Projectile 2",
                                  "projectile2": "50;+Rapide\n+Power;Projectile 3",
                                  "projectile3": "---;MAX;MAX",
                                  "éclair1": "50;Laser\n-Power;Éclair 2",
                                  "éclair2": "50;+Power;Éclair 3",
                                  "éclair3": "---;MAX;MAX",
                                  "poison1": "50;-Rapide\n+Poison;Poison 2",
                                  "poison2": "50;-Rapide\n+Poison;Poison 3",
                                  "poison3": "---;MAX;MAX"}
        ##creation  des interfaces graphiques
        self.dict_interfaces = {}
        self.creer_interfaces()
        self.tourCliquer = None

    def creer_interfaces(self):
        self.creer_frame_aire_jeu()
        self.creer_frame_menu()

    def creer_frame_aire_jeu(self):
        canvas_aire_jeu = Canvas(self.root, width=self.modele.unite_base * 32,
                                 height=self.modele.unite_base * 19,
                                 bg="SpringGreen4")
        canvas_aire_jeu.pack()
        self.dict_interfaces.update({"c_jeu": canvas_aire_jeu})

    def creer_frame_menu(self):
        frame_menu = Frame(self.root, width=self.modele.unite_base * 32,
                           height=self.modele.unite_base * 5, bg="light slate gray")

        frame_menu.pack()
        self.dict_interfaces.update({"f_menu": frame_menu})
        self.creer_frame_vague()
        self.creer_frame_construction()
        self.creer_frame_amelioration()
        self.creer_frame_ressource()
        self.creer_frame_gameover()

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
                                   wraplength=ub * 2, fg="white",
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
                                wraplength=ub * 2, command=self.ameliorerTour)
        label_tour = Label(frame_amelioration, text=tour,
                           font=("Arial", 14), fg="blue", bg="gray", padx=10,
                           pady=5,
                           wraplength=ub * 2)

        label_tour.place(relx=0.8, rely=0.5, anchor="center", relheight=0.5,
                         relwidth=0.2)

        bouton_quitter = Button(frame_amelioration, text=" X ",
                                font=("Arial", 14), fg="white", bg="DarkOrchid4",
                                padx=10, pady=5,
                                wraplength=ub * 2,
                                command=self.toggle_construction)
        bouton_quitter.place(relx=0.9, rely=0.1, anchor="center", relheight=0.2,
                             relwidth=0.2)

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

    def creer_frame_vague(self):
        frame_vague = Frame(self.dict_interfaces["f_menu"], width=self.modele.unite_base * 4,
                            height=self.modele.unite_base * 4, bd=2,
                            highlightthickness=2, relief="sunken", bg="sea green")

        frame_vague.place(x=40, y=5)

        label_timer = Label(frame_vague, textvariable=self.valeur_timer,
                            font=("Arial", 14), fg="blue", bg="lightgray", padx=10, pady=5)

        label_num_vague = Label(frame_vague, textvariable=self.valeur_vague,
                                font=("Arial", 14), fg="blue", bg="gray", padx=10, pady=5)

        # self.canvas_vague.place(relx=0, rely=0, anchor="nw", relwidth=1.0, relheight=1)
        label_timer.place(relx=0, rely=0, anchor="nw", relwidth=1.0, relheight=0.5)
        label_num_vague.place(relx=0, rely=0.5, anchor="nw", relwidth=1.0, relheight=0.5)

        self.dict_interfaces.update({"f_vague": frame_vague})
        self.dict_interfaces.update({"l_timer": label_timer})
        self.dict_interfaces.update({"l_numvague": label_num_vague.place})
        pass

    def creer_frame_ressource(self):
        frame_ressource = Frame(self.dict_interfaces["f_menu"], width=self.modele.unite_base * 5,
                                height=self.modele.unite_base * 4, bd=2,
                                highlightthickness=2, relief="sunken", bg="sea green")

        frame_ressource.place(x=960, y=5)
        label_vie = Label(frame_ressource, textvariable=self.valeur_vie,
                          font=("Arial", 14), fg="blue", bg="lightgray", padx=10, pady=5)

        label_argent = Label(frame_ressource, textvariable=self.valeur_argent,
                             font=("Arial", 14), fg="blue", bg="gray", padx=10, pady=5)

        label_vie.place(relx=0, rely=0, anchor="nw", relwidth=1.0, relheight=0.5)
        label_argent.place(relx=0, rely=0.75, anchor="nw", relwidth=1.0, relheight=0.25)

        self.dict_interfaces.update({"l_vie": label_vie})
        self.dict_interfaces.update({"f_argent": label_argent})
        self.dict_interfaces.update({"f_ressource": frame_ressource})
        pass

    def creer_frame_gameover(self):
        frame_gameover = Frame(self.root, width=self.modele.unite_base * 32,
                               height=self.modele.unite_base * 5, bg="light slate gray")

        label_texte_fin = Label(frame_gameover, text="GAME OVER",
                                font=("Arial", 40), fg="black", bg="light slate gray", padx=10, pady=5)
        label_texte_fin.place(relx=0, rely=0, anchor="nw", relwidth=1, relheight=1)

        self.dict_interfaces.update({"f_gameover": frame_gameover})
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
        objets = jeu.find_all()
        # deplace les objets non static du canvas
        # passer par le controleur au lieu de directement par le modele ????????????????????????
        self.modele.deplacer_objets()

        # delete les objets non permanents du canvas
        for o in objets:
            tags = jeu.gettags(o)
            if "permanent" not in tags:
                jeu.delete(o)

        # dessine les creeps et les projectiles
        for o in self.modele.objets_animer:
            if isinstance(o, Creep):
                self.dessine_creep(o)
            elif isinstance(o, Projectile):
                self.dessine_projectile(o)

        # dessine la zone de dectection des tours
        # for t in self.modele.liste_tours:
        #     self.dessine_range(t)

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
        elif p.type == "éclair":
            jeu.create_line(p.posX, p.posY, p.cibleX, p.cibleY, fill='yellow', width=6,
                            tags=("projectile", p.posX, p.posY))

        elif p.type == "laser":
            jeu.create_oval(p.posX, p.posY,
                            p.posX + p.taille, p.posY + p.taille,
                            fill=p.couleur, tags=("projectile", p.posX, p.posY))
        elif p.type == "poison":
            jeu.create_oval(p.posX, p.posY,
                            p.posX + p.taille, p.posY + p.taille,
                            fill="green", tags=("projectile", p.posX, p.posY))
        pass

    def dessiner_tour(self, index: str, tour: Tour):
        tag = "id_" + index

        t = self.dict_interfaces["c_jeu"].create_rectangle(tour.posX_1, tour.posY_1,
                                                           tour.posX_2, tour.posY_2,
                                                           fill=tour.couleur,
                                                           tags=(tag, "permanent"), outline='')
        self.dict_interfaces["c_jeu"].tag_bind(t, "<Button-1>", lambda t, test=tour: self.cliquerTour(t, test))

    def dessine_range(self, tour):
        x1 = tour.centreX + tour.range_detection
        y1 = tour.centreY + tour.range_detection
        x2 = tour.centreX - tour.range_detection
        y2 = tour.centreY - tour.range_detection
        color = "black"
        if tour.detecte_un_creep:
            color = "red"
        self.dict_interfaces["c_jeu"].create_oval(x1, y1, x2, y2, outline=color, width=4, tags=("range",))

    def construire_tour(self, type: str):
        if self.controle.verifier_argent(type):
            self.dict_interfaces["c_jeu"].bind("<Motion>",
                                               self.afficher_tour_temporaire)
            self.dict_interfaces["c_jeu"].bind("<Button-1>",
                                               lambda event, t=type: self.desactiver_tour_temporaire(event, t))

    def desactiver_tour_temporaire(self, evt, type: str) -> None:
        self.dict_interfaces["c_jeu"].unbind("<Motion>")
        self.dict_interfaces["c_jeu"].unbind("<Button-1>")
        self.retirer_tour_temporaire(evt, type)

    def retirer_tour_temporaire(self, evt, type: str) -> None:
        # Attention, si la taille de la tour change il faudra changer ici.
        x1, y1, x2, y2 = (evt.x, evt.y, (evt.x + self.modele.unite_base / 2),
                          (evt.y + self.modele.unite_base / 2))
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
                                                       fill="blue",
                                                       tags="temporaire")

    def split_string_amelioration(self, str_am):
        cout = str_am.split(";", 2)[0]
        desc = str_am.split(";", 2)[1]
        tour = str_am.split(";", 2)[2]
        return [cout, desc, tour]

    def toggle_construction(self):
        self.toggle_interface("f_amelioration", "f_construction")

    def toggle_amelioration(self):
        self.toggle_interface("f_construction", "f_amelioration")

    def toggle_interface(self, remove, show):
        self.dict_interfaces[remove].place_forget()
        self.dict_interfaces[show].place(x=10 * self.modele.unite_base, y=5)
        pass

    def toggle_gameover(self):
        self.toggle_menu_gameover("f_menu", "f_gameover")

    def toggle_menu(self):
        self.toggle_menu_gameover("f_gameover", "f_menu")

    def toggle_menu_gameover(self, remove, show):
        self.dict_interfaces[remove].pack_forget()
        self.dict_interfaces[show].pack()
        pass

    def update_menu_amelioration(self, tour):
        cle = tour.donner_cle_amelioration()
        cout, desc, tour = self.split_string_amelioration(self.dict_amelioration[cle])
        self.dict_interfaces["l_am_cout"].config(text=cout)
        self.dict_interfaces["l_am_desc"].config(text=desc)
        self.dict_interfaces["l_am_tour"].config(text=tour)
        pass

    def cliquerTour(self, event, t):  # toggle
        self.update_menu_amelioration(t)
        self.toggle_amelioration()
        # update la desc, le cout et le niveau de la tour

        self.tourCliquer = t

    def ameliorerTour(self):  # upgrapde_btn
        self.controle.ameliorerTour(self.tourCliquer)
        self.update_menu_amelioration(self.tourCliquer)

    def init_label(self, argent: str, vie: str, vague: str) -> None:
        self.valeur_timer.set("TIMER\n" + "5")
        self.valeur_argent.set("ARGENT\n" + argent)
        self.valeur_vie.set("VIES RESTANTES\n" + vie)
        self.valeur_vague.set("VAGUE\n" + vague)
