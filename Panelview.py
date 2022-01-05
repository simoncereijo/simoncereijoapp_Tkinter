from tkinter import *

import Constantes

class Panelview(Frame):
    def __init__(self, container,  *args, **kwargs):
        super(Panelview, self).__init__(container, *args, **kwargs)
        self.config(width=Constantes.ancho_frames, height=Constantes.alto_frames,bg=Constantes.blanco)
        self.opciones_seleccion()


    def opciones_seleccion(self):
        opciones = ["std-xx", "std-xx","std-xx","std-xx"]
        opcion=[0 for x in range(Constantes.dimension_pv)]
        seleccion=[0 for x in range(Constantes.dimension_pv)]
        n_pv = [0 for x in range(Constantes.dimension_pv)]
        for i in range(Constantes.dimension_pv):#con este for cubrimos de listas de seleccion el frame
            texto = "Panelview " + str(i + 1)+":"
            seleccion[i] = StringVar(self)
            seleccion[i].set("...")
            opcion[i] = OptionMenu(self, seleccion[i], *opciones)
            opcion[i].config(cursor = "hand1")
            n_pv[i] = Label(self, text=texto,bg=Constantes.blanco)
            opcion[i].config(width=20)
            opcion[i].grid(row=i + 1, column=1)
            n_pv[i].grid(row=i + 1, column=0)

