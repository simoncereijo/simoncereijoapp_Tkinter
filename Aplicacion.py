from tkinter import *
from tkinter import messagebox
from Home import Home
from Robots import Robots
from Motores import Motores
from Cronograma import Cronograma
from Maquetas import *
from Seguridades import Seguridades
from Panelview import Panelview
from Pupitres import Pupitres



#Generamos la clase donde iran contenidos todos los frames de las ventanas auxiliares
class Aplicacion (Tk):
    def __init__(self,*args,**kwargs):
        super(Aplicacion, self).__init__(*args,**kwargs)
        self.title("Generador Proyectos PSA-Vigo")
        self.iconbitmap("noted_note_pen_notebook_write_icon_193919.ico") #si queremos añadirle un icono
        self.config(bg="ivory2",relief="sunken",bd=5)
        self.geometry(Constantes.tamaño_root)
        #self.resizable(0,0) si quieres dejar fijo el tamaño del root
        self.Home=Home(self)
        self.Robots=Robots(self)
        self.Maquetas=Maquetas(self)
        self.Motores=Motores(self)
        self.Panelview=Panelview(self)
        self.Seguridades=Seguridades(self)
        self.Pupitres=Pupitres(self)
        self.Cronograma=Cronograma(self)


        # Definicion mensaje de ayuda
        def ayuda():
            messagebox.showinfo("ayuda", "Búscate la vida")

        #####   self.Maquetas.entrada_ruta[1].get() aqui estaria almacenado la ruta de los drf

        def test():
            import variables_a_almacenar


        #funcion para traer al frente la srceen seleccionada
        def swap(frame):
            frame.tkraise()


        #Metodo salir de la aplicacion
        def salir(app):
            valor = messagebox.askquestion("salir", "Desea salir")
            if valor == "yes":
                app.destroy()

        #superponemos todas las screens
        for f in (self.Home,self.Robots,self.Motores,self.Maquetas,self.Seguridades,self.Panelview,self.Pupitres,self.Cronograma):
            f.grid(row=1,column=0,columnspan=12)
            f.grid_propagate(0)


        #Aqui generamos los botones de llamada a las sreens
        #boton home
        mostrar_home=Button(self,text="HOME",cursor="hand1",relief="ridge", borderwidth=5,width=10, height=1,command=lambda:swap(self.Home))
        mostrar_home.grid(row=0,column=0)
        #boton Robot
        mostrar_robots=Button(self,text="ROBOTS",cursor="hand1",relief="ridge", borderwidth=5,width=10, height=1,command=lambda:swap(self.Robots))
        mostrar_robots.grid(row=0,column=1)
        #boton Puertas
        mostrar_seguridades=Button(self,text="SEGURIDADES",cursor="hand1",relief="ridge", borderwidth=5,width=10, height=1,command=lambda:swap(self.Seguridades))
        mostrar_seguridades.grid(row=0,column=2)
        #boton Maquetas
        mostrar_maquetas=Button(self,text="MAQUETAS",cursor="hand1",relief="ridge", borderwidth=5,width=10, height=1,command=lambda:swap(self.Maquetas))
        mostrar_maquetas.grid(row=0,column=3)
        #boton Pupitres
        mostrar_pupitres=Button(self,text="PUPITRES",cursor="hand1",relief="ridge", borderwidth=5,width=10, height=1,command=lambda:swap(self.Pupitres))
        mostrar_pupitres.grid(row=0,column=4)
        #boton Panelview
        mostrar_panelview=Button(self,text="PANELVIEW",cursor="hand1",relief="ridge", borderwidth=5,width=10, height=1,command=lambda:swap(self.Panelview))
        mostrar_panelview.grid(row=0,column=5)
        #boton Motores
        mostrar_motores=Button(self,text="MOTORES",cursor="hand1",relief="ridge", borderwidth=5,width=10, height=1,command=lambda:swap(self.Motores))
        mostrar_motores.grid(row=0,column=6)
        #boton cronograma
        mostrar_cronograma=Button(self,text="CRONOGRAMA",cursor="hand1",relief="ridge", borderwidth=5,width=12, height=1,command=lambda:swap(self.Cronograma))
        mostrar_cronograma.grid(row=0,column=7)
        #boton reserva
        res2=Button(self,text="RESERVA2",cursor="hand1",relief="ridge", borderwidth=5,width=10, height=1,command=lambda :print(self.Robots.seleccion[0].get()))
        res2.grid(row=0,column=8)
        #boton reserva
        res3=Button(self,text="RESERVA3",cursor="hand1",relief="ridge", borderwidth=5,width=10, height=1)
        res3.grid(row=0,column=9)
        #boton ayuda
        boton_gen_ayuda=Button(self,text="AYUDA",cursor="hand1",relief="ridge", borderwidth=5,width=10, height=1,command=lambda:ayuda())
        boton_gen_ayuda.grid(row=0,column=10)
        #boton Exit
        mostrar_exit=Button(self,text="EXIT",cursor="hand1",relief="ridge", borderwidth=5,width=10, height=1,command=lambda:salir(self))
        mostrar_exit.grid(row=0,column=11)

        #Al abrir mostramos la ventana home
        self.Home.tkraise()

        #información de las otras ventanas










