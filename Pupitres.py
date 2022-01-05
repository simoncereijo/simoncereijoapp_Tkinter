
#Las pantallas de los pupitres son mas complejas:
#Hay un frame base donde se pusieron los botones de llamada a cada pupitre
#Cada uno de los pupitres se confuguran en un frame diferente f_pupitres[i]
#Dentro de cada uno de los frames se parametrizan las entradas/salidas de esta forma:
#en el frame f_pupitres[i] (correspondiente al pupitre 1):
    #e_pup0[x] es donde el usuario introduce las entradas
    #s_pup0[x] es donde el usuario introduce las salidas
    #es_pup0[x] es donde el usuario introduce las entradas safety
    #e_seleccion[x] el color de la entrada  ("Azul", "Verde","Rojo","Naranja","Amarillo")
    #s_seleccion[x] el color de la salida ("Azul", "Verde","Rojo","Naranja","Amarillo")

    #Por tanto para acceder al valor de usuario de la entrada 1 pupitre 1 seria: pupitres_e[0][0].get()





from tkinter import *
import Constantes
from clase_canvas import *


class Pupitres(Frame):

    def __init__(self, container,  *args, **kwargs):
        super(Pupitres, self).__init__(container, *args, **kwargs)
        self.config(width=Constantes.ancho_frames, height=Constantes.alto_frames,relief="sunken",bd=5,bg=Constantes.blanco)




        #Declaracion de variables
        botones_pupitres=[0 for x in range (Constantes.dimension_pupitres)]
        f_pupitres = [0 for x in range(Constantes.dimension_pupitres)]
        dibujo_canvas=[0 for x in range(Constantes.dimension_pupitres)]
        etiqueta = [0 for x in range(Constantes.dimension_pupitres)]
        e_opciones = ["Azul", "Verde","Rojo","Naranja","Amarillo"]
        e_opcion=[0 for x in range(Constantes.dimension_config_pupitres)]
        self.e_seleccion=[0 for x in range(Constantes.dimension_config_pupitres)]
        s_opciones = ["Azul", "Verde","Rojo","Naranja","Amarillo"]
        s_opcion=[0 for x in range(Constantes.dimension_config_pupitres)]
        self.s_seleccion=[0 for x in range(Constantes.dimension_config_pupitres)]
        self.e_pup0=[0 for x in range(Constantes.dimension_config_pupitres)]
        self.s_pup0 = [0 for x in range(Constantes.dimension_config_pupitres)]
        self.es_pup0 = [0 for x in range(Constantes.dimension_config_pupitres)]
        self.pupitres_e = [0 for x in range(7)], [0 for x in range(7)], [0 for x in range(7)], [0 for x in range(7)], [0 for x in range(7)], [0 for x in range(7)], [0 for x in range(7)], [0 for x in range(7)], [0 for x in range(7)], [0 for x in range(7)]
        self.pupitres_s = [0 for x in range(7)], [0 for x in range(7)], [0 for x in range(7)], [0 for x in range(7)], [0 for x in range( 7)], [0 for x in range(7)], [0 for x in range(7)], [0 for x in range(7)], [0 for x in range(7)], [0 for x in range(7)]
        self.pupitres_es = [0 for x in range(7)], [0 for x in range(7)], [0 for x in range(7)], [0 for x in range(7)], [0 for x in range(7)], [0 for x in range(7)], [0 for x in range(7)], [0 for x in range(7)], [0 for x in range(7)], [0 for x in range(7)]
        self.pupitres_e_color = [0 for x in range(7)], [0 for x in range(7)], [0 for x in range(7)], [0 for x in range(7)], [0 for x in range(7)], [0 for x in range(7)], [0 for x in range(7)], [0 for x in range(7)], [0 for x in range(7)], [0 for x in range(7)]
        self.pupitres_s_color = [0 for x in range(7)], [0 for x in range(7)], [0 for x in range(7)], [0 for x in range(7)], [0 for x in range(7)], [0 for x in range(7)], [0 for x in range(7)], [0 for x in range(7)], [0 for x in range(7)], [0 for x in range(7)]

        for i in range(Constantes.dimension_pupitres):#Generamos las pantallas para los pupitres

            f_pupitres[i] = Frame(self)
            f_pupitres[i].config(width=Constantes.ancho_frames, height=Constantes.alto_frames_pup,relief="sunken",bd=5,bg=Constantes.blanco)
            f_pupitres[i].grid(row=1, column=0,columnspan=9)
            f_pupitres[i].grid_propagate(0)




            #Textos fijos pantallas
            etiqueta_E = Label(f_pupitres[i], text="Pulsadores:",bg=Constantes.blanco)
            etiqueta_E.grid(row=1,column=0)
            etiqueta_S = Label(f_pupitres[i], text="Pilotos:",bg=Constantes.blanco)
            etiqueta_S.grid(row=1,column=2)
            etiqueta_ES = Label(f_pupitres[i], text="Emergencia:",bg=Constantes.blanco)
            etiqueta_ES.grid(row=1,column=4)

            # Aqui configuramos las pantallas de los pupitres
            for x in range(Constantes.dimension_config_pupitres):

                dibujo_canvas[i] = sup_dibujo(f_pupitres[i])
                dibujo_canvas[i].grid(row=1, column=5,rowspan=20)
                dibujo_canvas[i].grid_propagate(0)


                # Estrada usuario para nombre entrada puitre
                self.e_pup0[x] = Entry(f_pupitres[i])
                self.e_pup0[x].grid(row=x + 2, column=0)
                #caca(i,x,self.e_pup0[x],self.pupitres)
                self.pupitres_e[i][x]=self.e_pup0[x]


                # Estrada usuario para nombre Salida puitre
                self.s_pup0[x] = Entry(f_pupitres[i])
                self.s_pup0[x].grid(row=x + 2, column=2)
                self.pupitres_s[i][x] = self.s_pup0[x]

                # Estrada usuario para nombre entrada safety puitre
                self.es_pup0[x] = Entry(f_pupitres[i])
                self.es_pup0[x].grid(row=x + 2, column=4)
                self.pupitres_es[i][x] = self.es_pup0[x]

                # Seleccion color pilotos
                self.e_seleccion[x] = StringVar(f_pupitres[i])
                self.e_seleccion[x].set("...")
                e_opcion[x] = OptionMenu(f_pupitres[i], self.e_seleccion[x], *e_opciones)
                e_opcion[x].config(cursor="hand1")
                e_opcion[x].config(height=1, width=8)
                e_opcion[x].grid(row=x + 2, column=1)
                self.pupitres_e_color[i][x] = self.e_seleccion[x]

                # seleccion color pilotos
                self.s_seleccion[x] = StringVar(f_pupitres[i])
                self.s_seleccion[x].set("...")
                s_opcion[x] = OptionMenu(f_pupitres[i], self.s_seleccion[x], *s_opciones)
                s_opcion[x].config(cursor="hand1")
                s_opcion[x].config(height=1, width=8)
                s_opcion[x].grid(row=x + 2, column=3)
                self.pupitres_s_color[i][x] = self.s_seleccion[x]





        #con este metodo traemos al frente el frame seleccionado
        def swap(frame,botones,n):
            frame.tkraise()
            for i in range(9):
                    botones[i].config(bg=Constantes.blanco)
            botones[n].config(bg=Constantes.verde)




        botones_pupitres[0]=Button(self, text="Pupitre 1",cursor="hand1",bg=Constantes.verde,bd=0,command=lambda: swap(f_pupitres[0],botones_pupitres,0))
        botones_pupitres[0].grid(row=0, column=0)
        botones_pupitres[1]=Button(self, text="Pupitre 2",cursor="hand1",bg=Constantes.blanco,bd=0,command=lambda: swap(f_pupitres[1],botones_pupitres,1))
        botones_pupitres[1].grid(row=0, column=1)
        botones_pupitres[2]=Button(self, text="Pupitre 3",cursor="hand1",bg=Constantes.blanco,bd=0,command=lambda: swap(f_pupitres[2],botones_pupitres,2))
        botones_pupitres[2].grid(row=0, column=2)
        botones_pupitres[3]=Button(self, text="Pupitre 4",cursor="hand1",bg=Constantes.blanco,bd=0,command=lambda: swap(f_pupitres[3],botones_pupitres,3))
        botones_pupitres[3].grid(row=0, column=3)
        botones_pupitres[4]=Button(self, text="Pupitre 5",cursor="hand1",bg=Constantes.blanco,bd=0,command=lambda: swap(f_pupitres[4],botones_pupitres,4))
        botones_pupitres[4].grid(row=0, column=4)
        botones_pupitres[5]=Button(self, text="Pupitre 6",cursor="hand1",bg=Constantes.blanco,bd=0,command=lambda: swap(f_pupitres[5],botones_pupitres,5))
        botones_pupitres[5].grid(row=0, column=5)
        botones_pupitres[6]=Button(self, text="Pupitre 7",cursor="hand1",bg=Constantes.blanco,bd=0,command=lambda: swap(f_pupitres[6],botones_pupitres,6))
        botones_pupitres[6].grid(row=0, column=6)
        botones_pupitres[7]=Button(self, text="Pupitre 8",cursor="hand1",bg=Constantes.blanco,bd=0,command=lambda: swap(f_pupitres[7],botones_pupitres,7))
        botones_pupitres[7].grid(row=0, column=7)
        botones_pupitres[8]=Button(self, text="Pupitre 9",cursor="hand1",bg=Constantes.blanco,bd=0,command=lambda: swap(f_pupitres[8],botones_pupitres,8))
        botones_pupitres[8].grid(row=0, column=8)




        f_pupitres[0].tkraise()

