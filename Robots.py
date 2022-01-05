

#El tipo de robots estan alacenados en el array "seleccion[i]"
#seleccion[i] tendra valor :"Vigo-M", "Vigo-SPF","Vigo-SPE","Vigo-S2PF","Vigo-M+PF","Francia-M", "Francia-SPF","Francia-SPE","Francia-S2PF","Francia-M+PF"
#En caso de no escoger ningun tipo el valor de la variable es "..."
#seleccion[0] corresponde con e robot 1



from tkinter import *
import Constantes


#Definicion clase ventana Robots
class Robots(Frame):
    def __init__(self, container,  *args, **kwargs):
        super(Robots, self).__init__(container, *args, **kwargs)
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

        #Calculo del nodo
        def nodo_robot(seleccion,dnet_r,dlr_r,calculo_nodo,label,contenedor):
            for i in range(Constantes.dimension_robots):

                if dnet_r[i].get()!=dlr_r[i].get():
                    if seleccion[i].get() != "..." and dnet_r[i].get() == True:
                        calculo_nodo[i] = str(i + 10)
                    if seleccion[i].get() != "..." and dlr_r[i].get() == True:
                        calculo_nodo[i] = "192.168.1." + (str(i + 50))
                    label[i] = Label(contenedor, bg=Constantes.blanco, text=calculo_nodo[i],width=10)
                    label[i].grid(row=i + 1, column=4)
                else:
                    calculo_nodo[i] = "xx"
                    label[i] = Label(contenedor, bg=Constantes.rojo, text=calculo_nodo[i],width=10)
                    label[i].grid(row=i + 1, column=4)



        #Valores desplegables
        marca=["ABB", "Fanuc"]
        opciones = ["Vigo-M", "Vigo-SPF","Vigo-SPE","Vigo-S2PF","Vigo-M+PF","Francia-M", "Francia-SPF","Francia-SPE","Francia-S2PF","Francia-M+PF"]
        redes = ["A", "B","C","D","E"]
        #Variables nodo
        self.nodo=[0 for x in range(Constantes.dimension_robots)]
        self.calculo_nodo=[0 for x in range(Constantes.dimension_robots)]
        red_dnt_seleccionada=[0 for x in range(Constantes.dimension_robots)]
        opcion_red_dnet=[0 for x in range(Constantes.dimension_robots)]
        red_dlr_seleccionada=[0 for x in range(Constantes.dimension_robots)]
        opcion_red_dlr=[0 for x in range(Constantes.dimension_robots)]
        self.dnet_r = [0 for x in range(Constantes.dimension_robots)]
        dnet = [0 for x in range(Constantes.dimension_robots)]
        self.dlr_r = [0 for x in range(Constantes.dimension_robots)]
        dlr = [0 for x in range(Constantes.dimension_robots)]
        #variables marca
        self.marca_seleccionada=[0 for x in range(Constantes.dimension_robots)]
        opcion_marca=[0 for x in range(Constantes.dimension_robots)]
        opcion=[0 for x in range(Constantes.dimension_robots)]
        self.seleccion=[0 for x in range(Constantes.dimension_robots)]
        #Textos de numero de robot
        n_robots_izq = [0 for x in range(Constantes.dimension_robots)]
        n_robots_mid = [0 for x in range(Constantes.dimension_robots)]
        #variables levas
        self.levas_eje1=[0 for x in range(Constantes.dimension_robots)]
        eje1 = [0 for x in range(Constantes.dimension_robots)]
        self.levas_eje2=[0 for x in range(Constantes.dimension_robots)]
        eje2 = [0 for x in range(Constantes.dimension_robots)]
        self.levas_eje3 = [0 for x in range(Constantes.dimension_robots)]
        eje3 = [0 for x in range(Constantes.dimension_robots)]


        for i in range(Constantes.dimension_robots):#con este for cubrimos de listas de seleccion el frame
            #Texto ROBOT x:
            texto = "ROBOT " + str(i + 1)+":"
            n_robots_izq[i] = Label(frame_izq, text=texto,bg=Constantes.blanco,width=10)
            n_robots_izq[i].grid(row=i + 1, column=0)

            #Seleccion metier
            self.seleccion[i] = StringVar(frame_izq)
            self.seleccion[i].set("...")
            opcion[i] = OptionMenu(frame_izq, self.seleccion[i], *opciones)
            opcion[i].config(cursor="hand1",width=20,bg=Constantes.blanco)
            opcion[i].grid(row=i + 1, column=1)

            #Seleccion marca
            self.marca_seleccionada[i]=StringVar(frame_izq)
            self.marca_seleccionada[i].set("...")
            opcion_marca[i] = OptionMenu(frame_izq, self.marca_seleccionada[i], *marca)
            opcion_marca[i].config(cursor="hand1",width=10,bg=Constantes.blanco)
            opcion_marca[i].grid(row=i + 1, column=2)

            #Texto ROBOT x:
            texto = "ROBOT " + str(i + 1)+":"
            n_robots_mid[i] = Label(frame_mid, text=texto,bg=Constantes.blanco,width=10)
            n_robots_mid[i].grid(row=i + 1, column=0)


            #seleccion levas
            self.levas_eje1[i]=BooleanVar()
            self.levas_eje1[i].set(False)
            eje1[i]=Checkbutton(frame_mid,text="Levas Eje1",var=self.levas_eje1[i])
            eje1[i].config(bg=Constantes.blanco,width=10)
            eje1[i].grid(row=i+1,column=1)

            self.levas_eje2[i]=BooleanVar()
            self.levas_eje2[i].set(False)
            eje2[i]=Checkbutton(frame_mid,text="Levas Eje2",var=self.levas_eje2[i])
            eje2[i].config(bg=Constantes.blanco,width=10)
            eje2[i].grid(row=i+1,column=2)

            self.levas_eje3[i]=BooleanVar()
            self.levas_eje3[i].set(False)
            eje3[i]=Checkbutton(frame_mid,text="Levas Eje3",var=self.levas_eje3[i])
            eje3[i].config(bg=Constantes.blanco,width=10)
            eje3[i].grid(row=i+1,column=3)

            #Red
            self.dnet_r[i]=BooleanVar()
            self.dnet_r[i].set(False)
            dnet[i]=Checkbutton(frame_der,text="Dnet",var=self.dnet_r[i])
            dnet[i].config(bg=Constantes.blanco)
            dnet[i].grid(row=i+1,column=0)
            red_dnt_seleccionada[i]=StringVar(self)
            red_dnt_seleccionada[i].set("...")
            opcion_red_dnet[i] = OptionMenu(frame_der, red_dnt_seleccionada[i], *redes)
            opcion_red_dnet[i].config(cursor="hand1",width=10,bg=Constantes.blanco)
            opcion_red_dnet[i].grid(row=i + 1, column=1)

            self.dlr_r[i]=BooleanVar()
            self.dlr_r[i].set(False)
            dlr[i]=Checkbutton(frame_der,text="DLR",var=self.dlr_r[i])
            dlr[i].config(bg=Constantes.blanco)
            dlr[i].grid(row=i+1,column=2)
            red_dlr_seleccionada[i]=StringVar(self)
            red_dlr_seleccionada[i].set("...")
            opcion_red_dlr[i] = OptionMenu(frame_der, red_dlr_seleccionada[i], *redes)
            opcion_red_dlr[i].config(cursor="hand1",width=10,bg=Constantes.blanco)
            opcion_red_dlr[i].grid(row=i + 1, column=3)


        boton_nodos=Button(frame_der,text="Calc. Nodos",command=lambda:nodo_robot(self.seleccion,self.dnet_r,self.dlr_r,self.calculo_nodo,self.nodo,frame_der))
        boton_nodos.grid(row=0,column=4)

        #Textos cabeceras
        cabecera1=Label(frame_izq, text="Nº Robot:",bg=Constantes.blanco,font='Helvetica 10 bold')
        cabecera1.grid(row=0,column=0)
        cabecera2=Label(frame_izq, text="Tipo:",bg=Constantes.blanco,font='Helvetica 10 bold')
        cabecera2.grid(row=0,column=1)
        cabecera3=Label(frame_izq, text="Marca:",bg=Constantes.blanco,font='Helvetica 10 bold')
        cabecera3.grid(row=0,column=2)
        cabecera4=Label(frame_mid, text="Levas:",bg=Constantes.blanco,font='Helvetica 10 bold')
        cabecera4.grid(row=0,column=0,columnspan=5)
        cabecera5=Label(frame_der, text="RED:",bg=Constantes.blanco,font='Helvetica 10 bold')
        cabecera5.grid(row=0,column=0,columnspan=4)



