from tkinter import *
from PIL import Image,ImageTk
from tkinter import filedialog
import os
import subprocess
import Constantes


class sup_dibujo(Frame):
    def __init__(self,contenedor,*args,**kwargs):
        super(sup_dibujo, self).__init__(contenedor,*args,**kwargs)
        self.config(width=Constantes.ancho_frames* (0.6), height=Constantes.alto_frames_pup , relief="sunken", bd=5)

        canvas = Canvas(self, height=400, width=400, bg="white") #añadimos el lienzo
        canvas.create_rectangle(0, 0, 400, 400) #Creamos el rectangulo donde iran los elementos
        canvas.grid(row=0, column=0,rowspan=13,columnspan=2)
        canvas.grid_propagate(0)

        path = StringVar() #declaramos la variable del path de las imagenes a insertar

        #valiables para la seleccion del elemento a insetar
        opciones = ["elemento1", "elemento2", "elemento3", "elemento4", "elemento5", "elemento6", "elemento7"]
        seleccion = StringVar(self)
        seleccion.set("...")
        opcion = OptionMenu(self, seleccion, *opciones)
        opcion.config(cursor="hand1", width=10, bg=Constantes.blanco)
        opcion.grid(row=4, column=4)

        def resize(image):#funcion para la redimension de la imagen
            w, h = image.size
            w1 = int(w / 1)
            h1 = int(h / 1)
            return image.resize((w1, h1))

        def show_image(path, nombre, seleccion): #funcion para la insercion de los elentos
            global img1 ,img2,img3,img4,img5,img6,img7

            # por cada seleccion se le asigna una posicion para la insercion
            if seleccion.get() == "elemento1":
                posx_etq = 200
                posy_etq = 80
                posx_img = 200
                posy_img = 120
                image = Image.open(path)  # Abrir imagen
                re_image = resize(image)  # Funciones de llamada
                img1 = ImageTk.PhotoImage(
                    re_image)  # La clase PhotoImage se usa para mostrar imágenes en etiquetas y lienzos
                canvas.create_image(posx_img, posy_img, anchor='center', image=img1)
            if seleccion.get() == "elemento2":
                posx_etq = 100
                posy_etq = 140
                posx_img = 100
                posy_img = 180
                image = Image.open(path)  # Abrir imagen
                re_image = resize(image)  # Funciones de llamada
                img2 = ImageTk.PhotoImage(
                    re_image)  # La clase PhotoImage se usa para mostrar imágenes en etiquetas y lienzos
                canvas.create_image(posx_img, posy_img, anchor='center', image=img2)
            if seleccion.get() == "elemento3":
                posx_etq = 100
                posy_etq = 220
                posx_img = 100
                posy_img = 260
                image = Image.open(path)  # Abrir imagen
                re_image = resize(image)  # Funciones de llamada
                img3 = ImageTk.PhotoImage(
                    re_image)  # La clase PhotoImage se usa para mostrar imágenes en etiquetas y lienzos
                canvas.create_image(posx_img, posy_img, anchor='center', image=img3)
            if seleccion.get() == "elemento4":
                posx_etq = 100
                posy_etq = 300
                posx_img = 100
                posy_img = 340
                image = Image.open(path)  # Abrir imagen
                re_image = resize(image)  # Funciones de llamada
                img4 = ImageTk.PhotoImage(
                    re_image)  # La clase PhotoImage se usa para mostrar imágenes en etiquetas y lienzos
                canvas.create_image(posx_img, posy_img, anchor='center', image=img4)
            if seleccion.get() == "elemento5":
                posx_etq = 300
                posy_etq = 140
                posx_img = 300
                posy_img = 180
                image = Image.open(path)  # Abrir imagen
                re_image = resize(image)  # Funciones de llamada
                img5 = ImageTk.PhotoImage(
                    re_image)  # La clase PhotoImage se usa para mostrar imágenes en etiquetas y lienzos
                canvas.create_image(posx_img, posy_img, anchor='center', image=img5)
            if seleccion.get() == "elemento6":
                posx_etq = 300
                posy_etq = 220
                posx_img = 300
                posy_img = 260
                image = Image.open(path)  # Abrir imagen
                re_image = resize(image)  # Funciones de llamada
                img6 = ImageTk.PhotoImage(
                    re_image)  # La clase PhotoImage se usa para mostrar imágenes en etiquetas y lienzos
                canvas.create_image(posx_img, posy_img, anchor='center', image=img6)
            if seleccion.get() == "elemento7":
                posx_etq = 300
                posy_etq = 300
                posx_img = 300
                posy_img = 340
                image = Image.open(path)  # Abrir imagen
                re_image = resize(image)  # Funciones de llamada
                img7 = ImageTk.PhotoImage(
                    re_image)  # La clase PhotoImage se usa para mostrar imágenes en etiquetas y lienzos
                canvas.create_image(posx_img, posy_img, anchor='center', image=img7)
            #insercion del nombre del elemento
            texto = nombre.get()
            canvas.create_text(posx_etq, posy_etq, fill="darkblue", font="Times 10 italic bold",
                               text=texto, tag="tit_tag")

        def openpicture(nombre, seleccion): #funcion seleccion de imagen
            # Abrir una imagen y mostrar
            global fileindex, fatherpath, files, file_num

            filepath = filedialog.askopenfilename()
            fatherpath = os.path.dirname(filepath)  # Obtener el camino de nivel superior del camino
            filename = os.path.basename(filepath)  # Obtenga el nombre del archivo debajo de la ruta
            files = os.listdir(fatherpath)  # Todos los archivos debajo de la ruta y generar una lista
            file_num = len(files)
            fileindex = files.index(filename)  # Obtener el valor de índice del archivo actual
            show_image(filepath, nombre, seleccion)

        def insert_tittle(title):#funcion para insertar la etiqueta del pupitre
            canvas.delete("some_tag")
            texto = title.get()
            canvas.create_text(200, 40, fill="darkblue", font="Times 10 italic bold",
                               text=texto, tag="some_tag")

        def save(): #funcion para guardar el lienzo como .pdf. Se guarda en la ruta del proyecto
            canvas.postscript(file="tmp.ps", colormode='color')
            process = subprocess.Popen(['ps2pdf', "tmp.ps", "result.pdf"], shell=True)
            process.wait()
            os.remove("tmp.ps")

        def borar(): #Borra todo el lienzo
            canvas.delete("all")
            canvas.create_rectangle(0, 0, 400, 400)  # Creamos el rectangulo donde iran los elementos
        l1=Label(self,text="Etiqueta:")
        l1.grid(row=0, column=2)
        etiqueta_pup = Entry(self, width=10) #Entrada de usuario para del nombre el pupitre
        etiqueta_pup.grid(row=0, column=3)
        boton_insertar_titulo = Button(self, text='insertar titulo', command=lambda: insert_tittle(etiqueta_pup))
        boton_insertar_titulo.grid(row=0, column=4)

        l2=Label(self,text="Etiqueta:")
        l2.grid(row=4, column=2)
        etiqueta_elem = Entry(self, width=10) #Entrada de usuario para del nombre del elemento
        etiqueta_elem.grid(row=4, column=3)
        boton_elegir_imagen = Button(self, text='insert_opjeto', command=lambda: openpicture(etiqueta_elem, seleccion))
        boton_elegir_imagen.grid(row=5, column=4)

        boton_export_pdf = Button(self, text="guardar", command=lambda: save())
        boton_export_pdf.grid(row=13, column=1)

        boton_borrar = Button(self, text="borrar", command=borar)
        boton_borrar.grid(row=13, column=0)



