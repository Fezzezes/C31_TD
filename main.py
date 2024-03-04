from modele import *
from vue import *
from tkinter import *

class Controleur:
    def __init__(self):
        self.modele = Modele(self)
        self.vue = Vue(self, self.modele)
        self.vue.root.mainloop()

if __name__ == "__main__":
    c = Controleur()
