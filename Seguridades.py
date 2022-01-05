
#El tipo de puertas estan alacenados en el array "seleccion[i]"
#seleccion[i] tendra valor :""Euchner", "pilz"
#En caso de no escoger ningun tipo el valor de la variable es "..."
#seleccion[0] corresponde con la puerta 1
#En numero de puesto asociado a una BI se almacena en n_bi_puesto[i]
#En en caso de que esta variable esté vacia, no existe BI. Siempre hay que poner un puesto / isla asociada
#En el array n_otro_1[i] se alamacenan otro tiepo de elemnto de seguridad en cual en las generacions de la aplicacion saldra algo como "sin definir"



from tkinter import *
import Constantes
from Maquetas import lista_puestos

class Seguridades(Frame):
    def __init__(self, container,  *args, **kwargs):
        super(Seguridades, self).__init__(container, *args, **kwargs)
        self.config(width=Constantes.ancho_frames, height=Constantes.alto_frames,bg=Constantes.blanco)
        self.componentes()


    def componentes(self):

        # declracion frames
        frame_izq = Frame(self)
        frame_izq.grid(row=0, column=0)
        frame_izq.config(bg=Constantes.blanco, width=(Constantes.ancho_frames) / 3, height=Constantes.alto_frames,
                         relief="sunken", bd=5)
        frame_izq.grid_propagate(0)

        frame_mid = Frame(self)
        frame_mid.grid(row=0, column=1)
        frame_mid.config(bg=Constantes.blanco, width=(Constantes.ancho_frames) / 3, height=Constantes.alto_frames,
                         relief="sunken", bd=5)
        frame_mid.grid_propagate(0)

        frame_der = Frame(self)
        frame_der.grid(row=0, column=2)
        frame_der.config(bg=Constantes.blanco, width=(Constantes.ancho_frames) / 3, height=Constantes.alto_frames,
                         relief="sunken", bd=5)
        frame_der.grid_propagate(0)



        opciones = ["Euchner", "pilz"]
        opcion=[0 for x in range(Constantes.dimension_seg)]
        seleccion=[0 for x in range(Constantes.dimension_seg)]
        n_puertas = [0 for x in range(Constantes.dimension_seg)]
        n_bi = [0 for x in range(Constantes.dimension_seg)]
        numero_bi = [0 for x in range(Constantes.dimension_seg)]
        n_otro = [0 for x in range(Constantes.dimension_seg)]
        n_otro_1 = [0 for x in range(Constantes.dimension_seg)]

        def seleccion_puesto():
            seleccion_puesto = [0 for x in range(Constantes.dimension_seg)]
            opcion_puesto = [0 for x in range(Constantes.dimension_seg)]
            for i in range(Constantes.dimension_seg):
                seleccion_puesto[i] = StringVar(frame_mid)
                seleccion_puesto[i].set("...")
                opcion_puesto[i] = OptionMenu(frame_mid, seleccion_puesto[i], *lista_puestos)
                opcion_puesto[i].config(cursor="hand1")
                opcion_puesto[i].config(width=20)
                opcion_puesto[i].grid(row=i + 1, column=2)

        for i in range(Constantes.dimension_seg):#con este for cubrimos de listas de seleccion el frame
            texto_puerta = "Puerta " + str(i + 1)+":"
            seleccion[i] = StringVar(frame_izq)
            seleccion[i].set("...")
            opcion[i] = OptionMenu(frame_izq, seleccion[i], *opciones)
            opcion[i].config(cursor="hand1")
            n_puertas[i] = Label(frame_izq, text=texto_puerta,bg=Constantes.blanco)
            opcion[i].config(width=20)
            opcion[i].grid(row=i + 1, column=1)
            n_puertas[i].grid(row=i + 1, column=0)

            texto_bi="BI :"
            n_bi[i] = Label(frame_mid, text=texto_bi,bg=Constantes.blanco)
            n_bi[i].grid(row=i + 1, column=0)

            numero_bi[i]=Entry(frame_mid,width=5)
            numero_bi[i].grid(row=i + 1, column=1)



            texto_otro="Otro " + str(i+1)+":"
            n_otro[i] = Label(frame_der, text=texto_otro,bg=Constantes.blanco)
            n_otro_1[i]=Entry(frame_der)
            n_otro[i].grid(row=i + 1, column=0)
            n_otro_1[i].grid(row=i + 1, column=1)

        texto_1 = Label(frame_mid, text="N_BI", bg=Constantes.blanco)
        texto_1.grid(row=0, column=1)
        texto_2 = Label(frame_izq, text="Referecia puerta", bg=Constantes.blanco)
        texto_2.grid(row=0, column=0,columnspan=2)
        texto_3 = Label(frame_der, text="Nombre Elemento", bg=Constantes.blanco)
        texto_3.grid(row=0, column=0,columnspan=2)
        boton_lista_puestos=Button(frame_mid,text="Lista_Puestos",command=lambda :seleccion_puesto())
        boton_lista_puestos.grid(row=0,column=2)



