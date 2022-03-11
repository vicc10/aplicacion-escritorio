
#=====================================LIBRERÍAS============================================
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

#=====================================OPCIONES DE LA VENTANA RAIZ============================================

root = tkinter.Tk()

root.maxsize(width=1366, height=705)
root.minsize(width=1366, height=705)
root.title("TicketDesk")
root.iconbitmap("img/favicon.ico")
root.state('zoomed')


#=====================================APARIENCIA DE LAS PESTAÑAS============================================

style2 = ttk.Style()
style2.theme_create('estilo_frame1', parent = 'alt',
    settings = {
        'TFrame': {
            'configure': {
                'bd': 7,  'borderwidth':4, 'background': c_frame1, 'foreground': "#000000", 'highlightbackground':"#000000", 'highlightcolor':"#000000",
            }
        }

    }
)

style2.theme_use('estilo_frame1')


#ESTILO DE LOS FRAMES

tab_styles = {}
nb = ttk.Notebook(width=966, height=200, padding=10)
nb.pressed_index = None

f1 = tkinter.Frame(nb, background=c_fondo1_general)  #COLOR FONDO VENTANA ENTERA SELECCIONADA
f2 = tkinter.Frame(nb, background=c_fondo1_general)  #COLOR FONDO VENTANA ENTERA SELECCIONADA
f3 = tkinter.Frame(nb, background=c_fondo1_general)  #COLOR FONDO VENTANA ENTERA SELECCIONADA
f4 = tkinter.Frame(nb, background=c_fondo1_general)  #COLOR FONDO VENTANA ENTERA SELECCIONADA


nb.add(f1, text="                    Entradas                    ")
tab_styles["                    Entradas                    "] = {"background": [("selected", c_fondo1_general)], #COLOR FONDO PESTAÑA SELECCIONADA
                      "foreground": [("selected", c_letra1_general)]  #COLOR LETRAS PESTAÑA SELECCIONADA
                     }
nb.add(f2, text="                    Abonos                    ")
tab_styles["                    Abonos                    "] = {"background": [("selected", c_fondo1_general)], #COLOR FONDO PESTAÑA SELECCIONADA
                      "foreground": [("selected", c_letra1_general)]   #COLOR LETRAS PESTAÑA SELECCIONADA
                     }

nb.add(f3, text="                    Buscar                    ")
tab_styles["                    Buscar                    "] = {"background": [("selected", c_fondo1_general)], #COLOR FONDO PESTAÑA SELECCIONADA
                      "foreground": [("selected", c_letra1_general)]  #COLOR LETRAS PESTAÑA SELECCIONADA
                     }

nb.add(f4, text="                    Estadisticas                    ")
tab_styles["                    Estadisticas                    "] = {"background": [("selected", c_fondo1_general)], #COLOR FONDO PESTAÑA SELECCIONADA
                      "foreground": [("selected", c_letra1_general)]  #COLOR LETRAS PESTAÑA SELECCIONADA
                     }


#=====================================CONFIGURACION DE LOS FRAMES============================================


#--------------------FRAMES PESTAÑA ENTRADAS----------------------
frame1f1=ttk.Frame(f1,width=100, height=100, padding=10)        
frame1f1.place(x=185, y=60)


#--------------------FRAMES PESTAÑA ABONOS----------------------
#abonos
frame1f2=ttk.Frame(f2, width=300, height=400, padding=10 )        
frame1f2.place(x=59, y=60)

#clientes
frame2f2=ttk.Frame(f2, width=300, height=400, padding=10)        
frame2f2.place(x=630, y=60)


#--------------------FRAMES PESTAÑA BUSCAR----------------------
#buscar
frame1f3=ttk.Frame(f3, width=100, height=100, padding=10 )        
frame1f3.place(x=59, y=60)

#tabla buscar
frame2f3=ttk.Frame(f3, width=100, height=100, padding=10 )        
frame2f3.place(x=59, y=220)


#--------------------FRAMES PESTAÑA ESTADISTICAS----------------------
#titulo estadisticas generales
frame1f4=ttk.Frame(f4, width=100, height=100, padding=10 )        
frame1f4.place(x=59, y=60)

#estadisticas entradas
frame2f4=ttk.Frame(f4, width=100, height=0, padding=10 )        
frame2f4.place(x=59, y=160)

#boton actualizar entradas
frame6f4=ttk.Frame(f4, width=540, height=60, padding=10 )        
frame6f4.place(x=59, y=430 )

#estadisticas abonos
frame5f4=ttk.Frame(f4, width=100, height=0, padding=10 )        
frame5f4.place(x=630, y=160 )

#boton actualizar abonos
frame7f4=ttk.Frame(f4,width=540, height=60, padding=10)        
frame7f4.place(x=630, y=430 )
