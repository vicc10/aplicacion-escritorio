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
from pie_de_pagina import *


#===================================== PESTAÑA BUSCAR============================================


#-------------------------------TABLA------------------------

scrollbary = Scrollbar(frame2f3, orient=VERTICAL)
scrollbary.pack(side=RIGHT, fill=Y)

tree0 = ttk.Treeview(frame2f3, style="mystyle.Treeview", columns=("codigo_clientes", "nombre", "apellidos", "dni", "telefono", "fecha", "codigo_ab", "tipo_abonos"), selectmode="extended", height=15, yscrollcommand=scrollbary.set)
tree0.pack()

scrollbary.config(command=tree0.yview)
tree0.heading('codigo_clientes', text=" Codigo",anchor=W)
tree0.heading('nombre', text="Nombre",anchor=W)
tree0.heading('apellidos', text="Apellidos",anchor=W)
tree0.heading('dni', text="Dni",anchor=W)
tree0.heading('telefono', text="Telefono",anchor=W)
tree0.heading('fecha', text="Fecha de registro",anchor=W)
tree0.heading('codigo_ab', text="Codigo abono ",anchor=W)
tree0.heading('tipo_abonos', text="Tipo abono ",anchor=W)
tree0.column('#0', stretch=NO, minwidth=0, width=0)
tree0.column('#1', stretch=NO, minwidth=0, width=70)
tree0.column('#2', stretch=NO, minwidth=0, width=100)
tree0.column('#3', stretch=NO, minwidth=0, width=200)
tree0.column('#4', stretch=NO, minwidth=0, width=150)
tree0.column('#5', stretch=NO, minwidth=0, width=150)
tree0.column('#6', stretch=NO, minwidth=0, width=150)
tree0.column('#7', stretch=NO, minwidth=0, width=150)
tree0.column('#8', stretch=NO, minwidth=0, width=150)


#ESTILOS TABLA BUSCAR CLIENTES
style = ttk.Style()
style.configure("mystyle.Treeview", highlightthickness=3, bd=1) # Modify the font of the body
style.configure("mystyle.Treeview.Heading",  font=('franklin ghotic', 10,'bold')) # Modify the font of the headings
style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})]) # Remove the borders

#COLORES FILAS TABLA
tree0.tag_configure('impar', background=c_imagen1_tabla_impar)
tree0.tag_configure('par', background=c_imagen1_tabla)



#--------------------------------------FUNCIONES---------------------------------------
#muestra la tabla
def Buscar1():

    contador2=0
    db=sql.connect("database.db")
    cur=db.cursor()
    cur.execute("SELECT `codigo_clientes`, `nombre`, `apellidos`, `dni`, `telefono`, `fecha_clientes`, `codigo_ab`, `tipo_abonos`  FROM `clientes`, `abonos` WHERE codigo_ab=codigo_abonos ORDER BY `codigo_clientes` ASC")
    fetch = cur.fetchall()
    for data in fetch:
        if contador2 == 0:
            tree0.insert('', 'end', values=(data),  tags = ('par',))
            contador2 = 1
        elif contador2 == 1:
            tree0.insert('', 'end', values=(data),  tags = ('impar',))
            contador2 = 0
    
    cur.close()
    db.close()

#selecciona los clientes
def Buscar_clientes():
    contador3=0

    #los selecciona por nombre, dni, apellidos
    if BUSCAR_CLI10.get() != "":
        tree0.delete(*tree0.get_children())
        db=sql.connect("database.db")
        cur=db.cursor()
        cur.execute("SELECT DISTINCT `codigo_clientes`, `nombre`, `apellidos`, `dni`, `telefono`, `fecha_clientes`, `codigo_ab`, `tipo_abonos`  FROM `clientes`, `abonos` WHERE codigo_ab=codigo_abonos AND `dni` LIKE ? ORDER BY `codigo_clientes` ASC", ('%'+str(BUSCAR_CLI10.get())+'%',))
        fetch = cur.fetchall()
    
    #los seleciona por codigo
    if BUSCAR_CLI11.get() != "":
        tree0.delete(*tree0.get_children())
        db=sql.connect("database.db")
        cur=db.cursor()
        cur.execute("SELECT DISTINCT `codigo_clientes`, `nombre`, `apellidos`, `dni`, `telefono`, `fecha_clientes`, `codigo_ab`, `tipo_abonos`  FROM `clientes`, `abonos` WHERE `codigo_ab` = ? AND `codigo_abonos` = ? ORDER BY `codigo_clientes` ASC", (BUSCAR_CLI11.get(),BUSCAR_CLI11.get()))
        fetch = cur.fetchall()
    
    #bucle nos inserta los datos con colores por fila
    for data in fetch:
        if contador3 == 0:
            tree0.insert('', 'end', values=(data),  tags = ('par',))
            contador3 = 1
        elif contador3 == 1:
            tree0.insert('', 'end', values=(data),  tags = ('impar',))
            contador3 = 0 

    cur.close()
    db.close()
 
#nos actualiza la tabla
def actualizar1():
    contador4=0
    db=sql.connect("database.db")
    cur=db.cursor()
    tree0.delete(*tree0.get_children())
    cur.execute("SELECT `codigo_clientes`, `nombre`, `apellidos`, `dni`, `telefono`, `fecha_clientes`, `codigo_ab`, `tipo_abonos`  FROM `clientes`, `abonos` WHERE codigo_ab=codigo_abonos ORDER BY `codigo_clientes` ASC")
    fetch = cur.fetchall()
    for data in fetch:
        if contador4 == 0:
            tree0.insert('', 'end', values=(data),  tags = ('par',))
            contador4 = 1
        elif contador4 == 1:
            tree0.insert('', 'end', values=(data),  tags = ('impar',))
            contador4 = 0
    cur.close()
    db.close()



#--------------------------RECUADRO Y ETIQUETAS BUSCAR CLIENTES----------------------------

#TEXTO PRINCIPAL BUSCAR CLIENTES
lbl_title = Label(frame1f3, width=49, fg=c_letra_fondo1_label, bg=c_fondo1_label, font=('dejavu sans', 18), text="Buscar clientes")
lbl_title.grid(row=1, column=1, columnspan=10, padx=5, pady=15, sticky=W)

#TEXTO BUSCAR1
lbl_title1 = Label(frame1f3, bg=c_frame1, fg=c_letra1, text="Dni: ")
lbl_title1.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky=E)

#CAJA INTRODUCIR NOMBRE APELLIDO O DNI
BUSCAR_CLI10 = StringVar()
Buscar_cli1 = Entry(frame1f3, width=37, textvariable=BUSCAR_CLI10)
Buscar_cli1.grid(row=3, column=2, columnspan=2, padx=5, pady=5, sticky=W)

#TEXTO BUSCAR2
lbl_title2 = Label(frame1f3, bg=c_frame1, fg=c_letra1, text="Código de abono: ")
lbl_title2.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky=E)
 
#CAJA INTRODUCIR CODIGO CLIENTE
BUSCAR_CLI11 = StringVar()
Buscar_cli2 = Entry(frame1f3, width=37, textvariable=BUSCAR_CLI11)
Buscar_cli2.grid(row=4, column=2, columnspan=2, padx=5, pady=5, sticky=W)

#BOTON BUSCAR
photo15 = PhotoImage(file = c_imagen1_buscar)  
photoimage15 = photo15.subsample(1, 1) 
b17 = Button(frame1f3, bg = fondo1_boton, fg = c_letra1, font=('', 10,''), text="   Buscar", relief=t_borde1_botones, borderwidth=2, command=Buscar_clientes, image = photoimage15, compound = LEFT)
b17.place(width=169, height=45, x=490, y=70)

#BOTON ACTUALIZAR
photo16 = PhotoImage(file = c_imagen1_actualizar)  
photoimage16 = photo16.subsample(1, 1) 
b18 = Button(frame1f3, text = '', bg = fondo1_boton, font=('', 10,''), fg = c_letra1, relief=t_borde1_botones, borderwidth=2, command=actualizar1, image = photoimage16, compound = LEFT)
b18.place(width=45, height=45, x=440, y=70)