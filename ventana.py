from tkinter import *
from tkinter import messagebox

#Diseño ventana principal
root=Tk() #ventana principal
root.title("ventana principal")
root.geometry("600x300") #dimensiones ventana principal
root.iconbitmap("noted_note_pen_notebook_write_icon_193919.ico") #icono
root.resizable(0,0)#bloqueamos el tamaño del la ventana principal

#Diseño frame principal
frame=Frame(root) #nuestro frame pricipal esta dentro de la ventana principal
frame.pack() #empaquetamos el frame
frame.config(width=600, height=300) #le damos las mismas dimensiones que la ventana principal


#funcion salir de la aplicacion
def salir():
    valor=messagebox.askquestion("salir","texto desea sallir")
    if valor=="yes":
        root.destroy()


#clase nueva ventana
class nueva_ventana:
    def __init__(self):
        ventana_1 = Toplevel()
        ventana_1.title("ventana1")
        ventana_1.config(width=600, height=300)
        ventana_1.iconbitmap("noted_note_pen_notebook_write_icon_193919.ico")
        #si queremos asignar una lista de opciones en esta ventana
        var = StringVar(ventana_1)  #generamos variame string"
        var.set("...")  #nombre de la lista
        opciones = ["opcion1", "opcion2"]  #opciones de la lista
        seleccion = StringVar(ventana_1)
        opcion = OptionMenu(ventana_1, var, *opciones)
        opcion.config(width=20)
        opcion.grid(row=0, column=0)

#boton salir
Boton_salir=Button(frame,text="EXIT",command=salir)
Boton_salir.grid(row=6,column=1)#explandimos el boton de salir

#texto
texto_titulo = Label(frame, text="TITULO:")
texto_titulo.grid(row=0, column=0)
entrada_titulo=Entry(frame)
entrada_titulo.grid(row=0,column=1)
#Zona
texto_zona = Label(frame, text="ZONA:")
texto_zona.grid(row=1, column=0)
entrada_zona=Entry(frame)
entrada_zona.grid(row=1,column=1)
#configuraciones
config = Label(frame, text="CONFIGURAR:")
config.grid(row=2, column=0)
Boton_robots=Button(frame,text="ROBOTS",command=nueva_ventana)
Boton_robots.grid(row=2,column=2)
Boton_puertas=Button(frame,text="PUERTAS",command=nueva_ventana)
Boton_puertas.grid(row=2,column=3)
Boton_maquetas=Button(frame,text="MAQUETAS",command=nueva_ventana)
Boton_maquetas.grid(row=2,column=4)
Boton_pupitres=Button(frame,text="PUPITRES",command=nueva_ventana)
Boton_pupitres.grid(row=2,column=5)
Boton_panelview=Button(frame,text="PANELVIEW",command=nueva_ventana)
Boton_panelview.grid(row=2,column=6)
Boton_motores=Button(frame,text="MOTORES",command=nueva_ventana)
Boton_motores.grid(row=2,column=7)
#botor generar
Boton_gen=Button(frame,text="GENERAR PROYECTO",command=nueva_ventana)
Boton_gen.grid(row=5,column=0,columnspan=2)


root.mainloop() #bucle