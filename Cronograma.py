from tkinter import *
import Constantes


class Cronograma(Frame):

    def __init__(self, container,  *args, **kwargs):
        super(Cronograma, self).__init__(container, *args, **kwargs)
        self.config(width=Constantes.ancho_frames, height=Constantes.alto_frames,relief="sunken",bd=5,bg=Constantes.blanco)