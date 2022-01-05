from tkinter import *

import Maquetas
from Maquetas import lista_puestos,lista_tipo_puestos
from tkinter import messagebox

import Constantes

class Home(Frame):
    def __init__(self, container,  *args, **kwargs):
        super(Home, self).__init__(container, *args, **kwargs)
        self.config(width=Constantes.ancho_frames, height=Constantes.alto_frames,bg=Constantes.blanco)
        self.frames()



    #Dividimos la pantalla en 3 frames donde iremos colocandos nuestros elementos
    def frames(self):

        #Frame izquierdo
        frame_izq=Frame(self)
        frame_izq.grid(row=0,column=0)
        frame_izq.config(bg=Constantes.blanco,width=(Constantes.ancho_frames)/3, height=Constantes.alto_frames,relief="sunken",bd=5)
        frame_izq.grid_propagate(0)

        #imagen cabecera
        img = PhotoImage(file="scf.png")
        etiquetaIcono = Label(frame_izq, image=img)
        etiquetaIcono.image = img
        etiquetaIcono.grid(row=0, column=0)

        #Texots
        nombre_proy=Label(frame_izq,text="Nombre del proyecto:",bg=Constantes.blanco,width=20, height=1,anchor="nw",font='Helvetica 10 bold')
        nombre_proy.grid(row=1,column=0)
        nombre_carpeta=Label(frame_izq,text="Ruta carpeta:",bg=Constantes.blanco,width=20, height=1,anchor="nw",font='Helvetica 10 bold')
        nombre_carpeta.grid(row=2,column=0)
        nombre_zona=Label(frame_izq,text="Zona del proyecto:",bg=Constantes.blanco,width=20, height=1,anchor="nw",font='Helvetica 10 bold')
        nombre_zona.grid(row=3,column=0)
        nombre_responsable = Label(frame_izq,text="Responsable proyecto:",bg=Constantes.blanco,width=20, height=1,anchor="nw",font='Helvetica 10 bold')
        nombre_responsable.grid(row=4,column=0)

        #Entrada de datos
        self.entrada_proyecto=Entry(frame_izq)
        self.entrada_proyecto.grid(row=1,column=1)
        self.entrada_carpeta=Entry(frame_izq)
        self.entrada_carpeta.grid(row=2,column=1)
        self.entrada_zona=Entry(frame_izq)
        self.entrada_zona.grid(row=3,column=1)
        self.entrada_responsable=Entry(frame_izq)
        self.entrada_responsable.grid(row=4,column=1)




        #Frame central
        frame_mid=Frame(self)
        frame_mid.grid(row=0,column=1)
        frame_mid.config(bg=Constantes.blanco,width=(Constantes.ancho_frames)/3, height=Constantes.alto_frames,relief="sunken",bd=5)
        frame_mid.grid_propagate(0)

        def act_maquetas():
            n_puesto = [0 for x in range(Constantes.dimension_robots)]
            n_tipo = [0 for x in range(Constantes.dimension_robots)]
            for i in range( Constantes.dimension_maquetas):
                n_puesto[i]=Label(frame_mid,text=lista_puestos[i],bg=Constantes.blanco)
                n_puesto[i].grid(row=i+1,column=0)
                n_tipo[i]=Label(frame_mid,text=lista_tipo_puestos[i],bg=Constantes.blanco)
                n_tipo[i].grid(row=i + 1, column=1)




        actualizar=Button(frame_mid,text="Actualizar",height=2,command=lambda :act_maquetas())
        actualizar.grid(row=0,column=2)
        texto=Label(frame_mid,text="Listado de puestos",width=46,height=1)
        texto.grid(row=0,column=0,columnspan=2)


        frame_der=Frame(self)
        frame_der.grid(row=0,column=2)
        frame_der.config(bg=Constantes.blanco,width=(Constantes.ancho_frames)/3, height=Constantes.alto_frames,relief="sunken",bd=5)
        frame_der.grid_propagate(0)

        actualizar=Button(frame_der,text="Actualizar",height=2,command=lambda :act_maquetas())
        actualizar.grid(row=0,column=2)
        texto=Label(frame_der,text="Listado de Robots",width=46,height=1)
        texto.grid(row=0,column=0,columnspan=2)






