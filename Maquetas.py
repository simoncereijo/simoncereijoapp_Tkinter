

# En el array entrada_ruta[i] se almacenan los direcciorios de los DRFs
# En este caso no hace falta añadir ningun campo a mayores ya que toda la informacion se extraerá del propio DRF




from tkinter import *
import Constantes
import pandas as pd
from tkinter import filedialog

global lista_puestos
lista_puestos = ["" for x in range(Constantes.dimension_robots)]
lista_tipo_puestos = ["" for x in range(Constantes.dimension_robots)]
class Maquetas(Frame):
    def __init__(self, container,  *args, **kwargs):
        super(Maquetas, self).__init__(container, *args, **kwargs)
        self.config(width=Constantes.ancho_frames, height=Constantes.alto_frames,bg=Constantes.blanco)
        self.entrada_ruta = [0 for x in range(Constantes.dimension_maquetas)]  # array donde se almacenan as rutas de los DRFs entrada_ruta[i]
        self.componentes()





    def componentes(self):

        global path
        path = ["" for x in range(Constantes.dimension_maquetas)]  # Esto es el texto

        n_maquetas=[0 for x in range(Constantes.dimension_maquetas)] #Esto es el texto

        self.n_maquetas=n_maquetas



        def carga_puesto(contenedor,directorio,lista_puestos,tipo):
            salida_puesto = ["" for x in range(Constantes.dimension_robots)]
            salida_tipo = ["" for x in range(Constantes.dimension_robots)]

            for i in range (Constantes.dimension_maquetas):


                if directorio[i]!="":
                    busquedahoja1=pd.read_excel(directorio[i],0)
                    lista_puestos[i] = busquedahoja1.iloc[17, 2]
                    lista_tipo_puestos[i] = busquedahoja1.iloc[14, 2]
                    salida_puesto[i] = Label(contenedor, text=lista_puestos[i],bg=Constantes.verde)
                    salida_puesto[i].grid(row=i+1, column=4)
                    salida_tipo[i] = Label(contenedor, text=lista_tipo_puestos[i],bg=Constantes.blanco)
                    salida_tipo[i].grid(row=i+1, column=5)
        def openpicture(posicion):

            # Abrir una imagen y mostrar
            global fileindex, fatherpath, files, file_num

            filepath = filedialog.askopenfilename()
            label=Label(self,text=filepath)
            label.grid(row=posicion+1,column=2)
            path[posicion]=filepath


        for i in range (Constantes.dimension_maquetas):
            texto="Directorio DRF "+str(i+1)+":"
            self.n_maquetas[i] = Label(self, text=texto,bg=Constantes.blanco,font='Helvetica 10 bold')
            self.n_maquetas[i].grid(row=i + 1, column=0)

        cargar_drf = Button(self, text="Cargar DRF", bg=Constantes.blanco, command=lambda: carga_puesto(self,path,lista_puestos,lista_tipo_puestos))
        cargar_drf.grid(row=0, column=0)
        boton_1=Button(self,text="Archivo...",command=lambda :openpicture(0))
        boton_1.grid(row=1, column=1)
        boton_2=Button(self,text="Archivo...",command=lambda :openpicture(1))
        boton_2.grid(row=2, column=1)
        boton_3=Button(self,text="Archivo...",command=lambda :openpicture(2))
        boton_3.grid(row=3, column=1)
        boton_4=Button(self,text="Archivo...",command=lambda :openpicture(3))
        boton_4.grid(row=4, column=1)
        boton_5=Button(self,text="Archivo...",command=lambda :openpicture(4))
        boton_5.grid(row=5, column=1)
        boton_6=Button(self,text="Archivo...",command=lambda :openpicture(5))
        boton_6.grid(row=6, column=1)
        boton_7=Button(self,text="Archivo...",command=lambda :openpicture(6))
        boton_7.grid(row=7, column=1)
        boton_8=Button(self,text="Archivo...",command=lambda :openpicture(7))
        boton_8.grid(row=8, column=1)
        boton_9=Button(self,text="Archivo...",command=lambda :openpicture(8))
        boton_9.grid(row=9, column=1)
        boton_10=Button(self,text="Archivo...",command=lambda :openpicture(9))
        boton_10.grid(row=10, column=1)
        boton_11=Button(self,text="Archivo...",command=lambda :openpicture(19))
        boton_11.grid(row=11, column=1)
        boton_12=Button(self,text="Archivo...",command=lambda :openpicture(11))
        boton_12.grid(row=12, column=1)
        boton_13=Button(self,text="Archivo...",command=lambda :openpicture(12))
        boton_13.grid(row=13, column=1)
        boton_14=Button(self,text="Archivo...",command=lambda :openpicture(13))
        boton_14.grid(row=14, column=1)
        boton_15=Button(self,text="Archivo...",command=lambda :openpicture(14))
        boton_15.grid(row=15, column=1)
        boton_16=Button(self,text="Archivo...",command=lambda :openpicture(15))
        boton_16.grid(row=16, column=1)
        boton_17=Button(self,text="Archivo...",command=lambda :openpicture(16))
        boton_17.grid(row=17, column=1)
        boton_18=Button(self,text="Archivo...",command=lambda :openpicture(17))
        boton_18.grid(row=18, column=1)
        boton_19=Button(self,text="Archivo...",command=lambda :openpicture(18))
        boton_19.grid(row=19, column=1)
        boton_20=Button(self,text="Archivo...",command=lambda :openpicture(19))
        boton_20.grid(row=20, column=1)







