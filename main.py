#=====================================LIBRERIAS============================================

import tkinter
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import sqlite3 as sql
from tkinter import PhotoImage
import re  
from PIL import Image,ImageTk
import time
from variables import *
from conexion import *
from estructura import *
from ventanas_hijas import *
from entradas import *
from abonos import *
from buscar import *
from estadisticas import *
from pie_de_pagina import *
from conf_botones import *


#=====================================EVENTO FORMATO DE PESTAÑAS============================================
   
def on_tab(event):                                         
    global tab_styles
    global style
    nb = event.widget
    tab = nb.tab(nb.select(), "text")
    st = tab_styles[tab]
    style.map('TNotebook.Tab', **st)

nb.pack(expand=1, fill='both' )
nb.bind("<<NotebookTabChanged>>", on_tab)


#=====================================CONDICION AUTO-EJECUTABLE============================================

#la siguiente condicion nos dice que si el módulo que estás 
# ejecutando es el módulo principal, ejecutá el código que sigue. Con lo cual, las funciones que
# introduzcamos dentro de esta condicion, se ejecutaran automaticamente, sin pulsar ningun boton.
# esto es muy util para mostrar tablas, como es el caso.

if __name__ == '__main__':

    #funcion tabla buscar
    Buscar1()

    #funcion estadisticas entradas
    ACTUALIZAR_TODO_F4_ENTRADAS()
    #funcion estadisticas abonos
    ACTUALIZAR_TODO_F4_ABONOS()

    root.mainloop()




