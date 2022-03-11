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



#=======================================BOTONES LATERALES========================================


#-------------------BOTON PESTAÑA ENTRADAS-----------------------------
#boton apariencia situado en entradas
photo = PhotoImage(file = c_imagen1_apariencia)  
photoimage = photo.subsample(1, 1) 
b19 = Button(f1, text = '', bg = c_frame1, fg = c_letra1, relief=FLAT, command=apariencia, image = photoimage, compound = LEFT)
b19.place(width=50, height=50, x=1280, y=60)

#boton info situado en entradas
photo1 = PhotoImage(file = c_imagen1_info)  
photoimage1 = photo1.subsample(1, 1) 
b20 = Button(f1, text = '', bg = c_frame1, fg = c_letra1, relief=FLAT, command=informacion_entradas, image = photoimage1, compound = LEFT)
b20.place(width=50, height=50, x=1280, y=120)

#boton ayuda situado en entradas
photo12 = PhotoImage(file = c_imagen1_ayuda)  
photoimage12 = photo12.subsample(1, 1) 
b21 = Button(f1, text = '', bg = c_frame1, fg = c_letra1, relief=FLAT, command=contacto, image = photoimage12, compound = LEFT)
b21.place(width=50, height=50, x=1280, y=180)

#boton configuracion situado en entradas
photo36 = PhotoImage(file = c_imagen1)  #imagen de la tuerca
photoimage36 = photo36.subsample(1, 1) 
b31 = Button(f1, text = '', bg = c_frame1, fg = c_letra1, relief=FLAT, command=configuracion, image = photoimage36, compound = LEFT)
b31.place(width=50, height=50, x=1280, y=240)


#-------------------BOTON PESTAÑA ABONOS-----------------------------
#boton apariencia situado en abonos
b14 = Button(f2, text = '', bg = c_frame1, fg = c_letra1, relief=FLAT, command=apariencia, image = photoimage, compound = LEFT)
b14.place(width=50, height=50, x=1280, y=60)

#boton info situado en abonos
b15 = Button(f2, text = '', bg = c_frame1, fg = c_letra1, relief=FLAT, command=informacion_abonos, image = photoimage1, compound = LEFT)
b15.place(width=50, height=50, x=1280, y=120)

#boton ayuda situado en abonos
b16 = Button(f2, text = '', bg = c_frame1, fg = c_letra1, relief=FLAT, command=contacto, image = photoimage12, compound = LEFT)
b16.place(width=50, height=50, x=1280, y=180)

#boton configuracion situado en abonos
b32 = Button(f2, text = '', bg = c_frame1, fg = c_letra1, relief=FLAT, command=configuracion, image = photoimage36, compound = LEFT)
b32.place(width=50, height=50, x=1280, y=240)


#-------------------BOTON PESTAÑA BUSCAR-----------------------------
#boton apariencia situado en buscar
b22 = Button(f3, text = '', bg = c_frame1, fg = c_letra1, relief=FLAT, command=apariencia, image = photoimage, compound = LEFT)
b22.place(width=50, height=50, x=1280, y=60)

#boton info situado en buscar
b23 = Button(f3, text = '', bg = c_frame1, fg = c_letra1, relief=FLAT, command=informacion_abonos, image = photoimage1, compound = LEFT)
b23.place(width=50, height=50, x=1280, y=120)

#boton ayuda situado en buscar
b24 = Button(f3, text = '', bg = c_frame1, fg = c_letra1, relief=FLAT, command=contacto, image = photoimage12, compound = LEFT)
b24.place(width=50, height=50, x=1280, y=180)

#boton configuracion situado en buscar
b33 = Button(f3, text = '', bg = c_frame1, fg = c_letra1, relief=FLAT, command=configuracion, image = photoimage36, compound = LEFT)
b33.place(width=50, height=50, x=1280, y=240)


#-------------------BOTON PESTAÑA ESTADISTICAS-----------------------------
#boton apariencia situado en estadisticas
b28 = Button(f4, text = '', bg = c_frame1, fg = c_letra1, relief=FLAT, command=apariencia, image = photoimage, compound = LEFT)
b28.place(width=50, height=50, x=1280, y=60)

#boton info situado en estadisticas
b29 = Button(f4, text = '', bg = c_frame1, fg = c_letra1, relief=FLAT, command=informacion_abonos, image = photoimage1, compound = LEFT)
b29.place(width=50, height=50, x=1280, y=120)

#boton ayuda situado en estadisticas
b30 = Button(f4, text = '', bg = c_frame1, fg = c_letra1, relief=FLAT, command=contacto, image = photoimage12, compound = LEFT)
b30.place(width=50, height=50, x=1280, y=180)

#boton configuracion situado en estadisticas
b34 = Button(f4, text = '', bg = c_frame1, fg = c_letra1, relief=FLAT, command=configuracion, image = photoimage36, compound = LEFT)
b34.place(width=50, height=50, x=1280, y=240)

#=====================================CONFIGURACION DE LOS BOTONES============================================
#nos proporcionan un sombreado al pasar por encima el raton y se quita al quitar el raton

def enterB(event):
    b1.configure(bg =c_fondo1_botones, fg = c_letra1)

def leaveB(event):
    b1.configure(bg = fondo1_boton, fg = c_letra1)

b1.bind('<Enter>', enterB)
b1.bind('<Leave>', leaveB)


#-----------------------------------------------------------
def enterB6(event):
    b6.configure(bg =c_fondo1_botones, fg = c_letra1)

def leaveB6(event):
    b6.configure(bg = fondo1_boton, fg = c_letra1)

b6.bind('<Enter>', enterB6)
b6.bind('<Leave>', leaveB6)
#-----------------------------------------------------------
def enterB7(event):
    b7.configure(bg =c_fondo1_botones, fg = c_letra1)

def leaveB7(event):
    b7.configure(bg = fondo1_boton, fg = c_letra1)

b7.bind('<Enter>', enterB7)
b7.bind('<Leave>', leaveB7)
#-----------------------------------------------------------
def enterB8(event):
    b8.configure(bg =c_fondo1_botones, fg = c_letra1)

def leaveB8(event):
    b8.configure(bg = fondo1_boton, fg = c_letra1)

b8.bind('<Enter>', enterB8)
b8.bind('<Leave>', leaveB8)
#-----------------------------------------------------------
def enterB9(event):
    b9.configure(bg =c_fondo1_botones, fg = c_letra1)

def leaveB9(event):
    b9.configure(bg = fondo1_boton, fg = c_letra1)

b9.bind('<Enter>', enterB9)
b9.bind('<Leave>', leaveB9)
#-----------------------------------------------------------
def enterB10(event):
    b10.configure(bg =c_fondo1_botones, fg = c_letra1)

def leaveB10(event):
    b10.configure(bg = fondo1_boton, fg = c_letra1)

b10.bind('<Enter>', enterB10)
b10.bind('<Leave>', leaveB10)
#-----------------------------------------------------------
def enterB11(event):
    b11.configure(bg =c_fondo1_botones, fg = c_letra1)

def leaveB11(event):
    b11.configure(bg = fondo1_boton, fg = c_letra1)

b11.bind('<Enter>', enterB11)
b11.bind('<Leave>', leaveB11)
#-----------------------------------------------------------
def enterB12(event):
    b12.configure(bg =c_fondo1_botones, fg = c_letra1)

def leaveB12(event):
    b12.configure(bg = fondo1_boton, fg = c_letra1)

b12.bind('<Enter>', enterB12)
b12.bind('<Leave>', leaveB12)
#-----------------------------------------------------------
def enterB13(event):
    b13.configure(bg =c_fondo1_botones, fg = c_letra1)

def leaveB13(event):
    b13.configure(bg = fondo1_boton, fg = c_letra1)

b13.bind('<Enter>', enterB13)
b13.bind('<Leave>', leaveB13)
#-----------------------------------------------------------
def enterB14(event):
    b14.configure(bg =c_fondo1_botones, fg = c_letra1)

def leaveB14(event):
    b14.configure(bg = c_frame1, fg = c_letra1)

b14.bind('<Enter>', enterB14)
b14.bind('<Leave>', leaveB14)
#-----------------------------------------------------------
def enterB15(event):
    b15.configure(bg =c_fondo1_botones, fg = c_letra1)

def leaveB15(event):
    b15.configure(bg = c_frame1, fg = c_letra1)

b15.bind('<Enter>', enterB15)
b15.bind('<Leave>', leaveB15)
#-----------------------------------------------------------
def enterB16(event):
    b16.configure(bg =c_fondo1_botones, fg = c_letra1)

def leaveB16(event):
    b16.configure(bg = c_frame1, fg = c_letra1)

b16.bind('<Enter>', enterB16)
b16.bind('<Leave>', leaveB16)
#-----------------------------------------------------------
def enterB17(event):
    b17.configure(bg =c_fondo1_botones, fg = c_letra1)

def leaveB17(event):
    b17.configure(bg = fondo1_boton, fg = c_letra1)

b17.bind('<Enter>', enterB17)
b17.bind('<Leave>', leaveB17)
#-----------------------------------------------------------
def enterB18(event):
    b18.configure(bg =c_fondo1_botones, fg = c_letra1)

def leaveB18(event):
    b18.configure(bg = fondo1_boton, fg = c_letra1)

b18.bind('<Enter>', enterB18)
b18.bind('<Leave>', leaveB18)
#-----------------------------------------------------------

def enterB19(event):
    b19.configure(bg =c_fondo1_botones, fg = c_letra1)

def leaveB19(event):
    b19.configure(bg = c_frame1, fg = c_letra1)

b19.bind('<Enter>', enterB19)
b19.bind('<Leave>', leaveB19)
#-----------------------------------------------------------

def enterB20(event):
    b20.configure(bg =c_fondo1_botones, fg = c_letra1)

def leaveB20(event):
    b20.configure(bg = c_frame1, fg = c_letra1)

b20.bind('<Enter>', enterB20)
b20.bind('<Leave>', leaveB20)
#-----------------------------------------------------------


def enterB21(event):
    b21.configure(bg =c_fondo1_botones, fg = c_letra1)

def leaveB21(event):
    b21.configure(bg = c_frame1, fg = c_letra1)

b21.bind('<Enter>', enterB21)
b21.bind('<Leave>', leaveB21)

#-----------------------------------------------------------
#-----------------------------------------------------------

def enterB22(event):
    b22.configure(bg =c_fondo1_botones, fg = c_letra1)

def leaveB22(event):
    b22.configure(bg = c_frame1, fg = c_letra1)

b22.bind('<Enter>', enterB22)
b22.bind('<Leave>', leaveB22)
#-----------------------------------------------------------

def enterB23(event):
    b23.configure(bg =c_fondo1_botones, fg = c_letra1)

def leaveB23(event):
    b23.configure(bg = c_frame1, fg = c_letra1)

b23.bind('<Enter>', enterB23)
b23.bind('<Leave>', leaveB23)
#-----------------------------------------------------------


def enterB24(event):
    b24.configure(bg =c_fondo1_botones, fg = c_letra1)

def leaveB24(event):
    b24.configure(bg = c_frame1, fg = c_letra1)

b24.bind('<Enter>', enterB24)
b24.bind('<Leave>', leaveB24)

#-----------------------------------------------------------

def enterB26(event):
    b26.configure(bg =c_fondo1_botones, fg = c_letra1)
def leaveB26(event):
    b26.configure(bg = fondo1_boton, fg = c_letra1)

b26.bind('<Enter>', enterB26)
b26.bind('<Leave>', leaveB26)
#-----------------------------------------------------------


def enterB27(event):
    b27.configure(bg =c_fondo1_botones, fg = c_letra1)

def leaveB27(event):
    b27.configure(bg = fondo1_boton, fg = c_letra1)

b27.bind('<Enter>', enterB27)
b27.bind('<Leave>', leaveB27)

#-----------------------------------------------------------


def enterB28(event):
    b28.configure(bg =c_fondo1_botones, fg = c_letra1)

def leaveB28(event):
    b28.configure(bg = c_frame1, fg = c_letra1)

b28.bind('<Enter>', enterB28)
b28.bind('<Leave>', leaveB28)

#-----------------------------------------------------------


def enterB29(event):
    b29.configure(bg =c_fondo1_botones, fg = c_letra1)

def leaveB29(event):
    b29.configure(bg = c_frame1, fg = c_letra1)

b29.bind('<Enter>', enterB29)
b29.bind('<Leave>', leaveB29)

#-----------------------------------------------------------


def enterB30(event):
    b30.configure(bg =c_fondo1_botones, fg = c_letra1)

def leaveB30(event):
    b30.configure(bg = c_frame1, fg = c_letra1)

b30.bind('<Enter>', enterB30)
b30.bind('<Leave>', leaveB30)

#-----------------------------------------------------------
def enterB31(event):
    b31.configure(bg =c_fondo1_botones, fg = c_letra1)

def leaveB31(event):
    b31.configure(bg = c_frame1, fg = c_letra1)

b31.bind('<Enter>', enterB31)
b31.bind('<Leave>', leaveB31)

#-----------------------------------------------------------
def enterB32(event):
    b32.configure(bg =c_fondo1_botones, fg = c_letra1)

def leaveB32(event):
    b32.configure(bg = c_frame1, fg = c_letra1)

b32.bind('<Enter>', enterB32)
b32.bind('<Leave>', leaveB32)

#-----------------------------------------------------------
def enterB33(event):
    b33.configure(bg =c_fondo1_botones, fg = c_letra1)

def leaveB33(event):
    b33.configure(bg = c_frame1, fg = c_letra1)

b33.bind('<Enter>', enterB33)
b33.bind('<Leave>', leaveB33)

#-----------------------------------------------------------
def enterB34(event):
    b34.configure(bg =c_fondo1_botones, fg = c_letra1)

def leaveB34(event):
    b34.configure(bg = c_frame1, fg = c_letra1)

b34.bind('<Enter>', enterB34)
b34.bind('<Leave>', leaveB34)