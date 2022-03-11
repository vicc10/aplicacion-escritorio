
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

#=====================================PIE DE PAGINA============================================


#--------------------IMAGEN PIE DE PAGINA----------------------
photo33 = PhotoImage(file = c_imagen1_logo)  
photoimage33 = photo33.subsample(1, 1)

#--------------------TEXTO 1 PIE DE PAGINA----------------------
#pestaña1
pie1 = Label(f1, width=63, fg=c_letra1, bg=c_frame1, image=photoimage33, font=('dejavu sans', 10), compound = LEFT, text=" TicketDesk ©")
pie1.place(width=1345, height=45, x=0, y=620)
#pestaña2
pie1 = Label(f2, width=63, fg=c_letra1, bg=c_frame1, image=photoimage33, font=('dejavu sans', 10), compound = LEFT, text=" TicketDesk ©")
pie1.place(width=1345, height=45, x=0, y=620)
#pestaña3
pie1 = Label(f3, width=63, fg=c_letra1, bg=c_frame1, image=photoimage33, font=('dejavu sans', 10), compound = LEFT, text=" TicketDesk ©")
pie1.place(width=1345, height=45, x=0, y=620)
#pestaña4
pie1 = Label(f4, width=63, fg=c_letra1, bg=c_frame1, image=photoimage33, font=('dejavu sans', 10), compound = LEFT, text=" TicketDesk ©")
pie1.place(width=1345, height=45, x=0, y=620)


#--------------------TEXTO 2 PIE DE PAGINA----------------------
#pagina1
pie2 = Label(f1, width=63, fg=c_letra1, bg=c_frame1, font=('dejavu sans', 7), text="Versión 1.9 Alpha")
pie2.place(width=300, height=45, x=1130, y=620)
#pagina2
pie2 = Label(f2, width=63, fg=c_letra1, bg=c_frame1, font=('dejavu sans', 7), text="Versión 1.9 Alpha")
pie2.place(width=300, height=45, x=1130, y=620)
#pagina3
pie2 = Label(f3, width=63, fg=c_letra1, bg=c_frame1, font=('dejavu sans', 7), text="Versión 1.9 Alpha")
pie2.place(width=300, height=45, x=1130, y=620)
#pagina4
pie2 = Label(f4, width=63, fg=c_letra1, bg=c_frame1, font=('dejavu sans', 7), text="Versión 1.9 Alpha")
pie2.place(width=300, height=45, x=1130, y=620)
