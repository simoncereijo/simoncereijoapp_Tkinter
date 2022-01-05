from tkinter import *

import Constantes

class Motores(Frame):
    def __init__(self, container,  *args, **kwargs):
        super(Motores, self).__init__(container, *args, **kwargs)
        self.config(width=Constantes.ancho_frames, height=Constantes.alto_frames,bg=Constantes.blanco)
        self.etiqueta()
        self.entradas_datos()
        self.nmotor=[0 for x in range(Constantes.dimension_motores)]



    def entradas_datos(self):
        n_motores=[0 for x in range(Constantes.dimension_motores)]
        entrada_potencia=[0 for x in range(Constantes.dimension_motores)]
        entrada_puesto=[0 for x in range(Constantes.dimension_motores)]
        for i in range (10):#con este for cubrimos el frame con lineas de texto Robot i
            texto="Motor "+str(i+1)+":"
            n_motores[i] = Label(self, text=texto,bg=Constantes.blanco)
            entrada_potencia[i] = Entry(self)
            entrada_puesto[i] = Entry(self)
            n_motores[i].grid(row=i + 1, column=0)
            entrada_potencia[i].grid(row=i + 1, column=1)
            entrada_puesto[i].grid(row=i + 1, column=2)


    def etiqueta(self):
        cabecera=Label(self,bg=Constantes.blanco)
        cabecera.grid(row=0,column=0)
        potencia=Label(self,text="Potencia [KW]",bg=Constantes.blanco)
        potencia.grid(row=0,column=1)
        puesto=Label(self,text="Puesto maester",bg=Constantes.blanco)
        puesto.grid(row=0,column=2)

