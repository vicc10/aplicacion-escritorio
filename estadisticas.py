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
from datetime import datetime,date
import calendar
from variables import *
from conexion import *
from estructura import *
from ventanas_hijas import *
from entradas import *
from abonos import *
from buscar import *
from pie_de_pagina import *


#===================================== PESTAÑA ESTADISTICAS============================================



#--------------------------- NUMERO ENTRADAS VENDIDAS----------------------------------
tree2 = ttk.Treeview(frame2f4, style="mystyle.Treeview", columns=("n_total_entradas"), selectmode="extended", height=1)
tree2.grid(row=3, column=0, padx=10, pady=15, columnspan=2, sticky=E)

tree2.heading('n_total_entradas', text="Entradas vendidas ",anchor=W)
tree2.column('#0', stretch=NO, minwidth=0, width=0)
tree2.column('#1', stretch=NO, minwidth=0, width=230)

tree2.tag_configure('par', background=c_fondo1_entry)



#--------------------------- CANTIDAD DINERO RECAUDADO--------------------------------------
tree1 = ttk.Treeview(frame2f4, style="mystyle.Treeview", columns=("total_entradas"), selectmode="extended", height=1)
tree1.grid(row=4, column=0, padx=10, pady=15, columnspan=2, sticky=E)

tree1.heading('total_entradas', text=" Total (euros) ",anchor=W)
tree1.column('#0', stretch=NO, minwidth=0, width=0)
tree1.column('#1', stretch=NO, minwidth=0, width=230)

tree1.tag_configure('par', background=c_fondo1_entry)



#--------------------------- DINERO DE ENTRADAS RECAUDADO POR MES-------------------------------
tree3 = ttk.Treeview(frame2f4, style="mystyle.Treeview", columns=("total_mes_recaudado"), selectmode="extended", height=1)
tree3.grid(row=4, column=2, padx=10, pady=15, columnspan=2, sticky=E)

tree3.heading('total_mes_recaudado', text=" Total (euros) ",anchor=W)
tree3.column('#0', stretch=NO, minwidth=0, width=0)
tree3.column('#1', stretch=NO, minwidth=0, width=250)

tree3.tag_configure('par', background=c_fondo1_entry)



#===============================FUNCIONES ESTADISTICAS==================================


#---------------------INSERTA Y ACTUALIZA LOS CAMPOS DE LAS ENTRADAS----------------

def ACTUALIZAR_TODO_F4_ENTRADAS():

    #conectamos con bdd
    db=sql.connect("database.db")
    cur=db.cursor()

    #Borramos todos los campos para así poder actualizarlos
    tree1.delete(*tree1.get_children())
    tree2.delete(*tree2.get_children())
    tree3.delete(*tree3.get_children())

    #----------SUMA DEL DINERO TOTAL RECAUDADO POR LAS ENTRADAS
    cur.execute("SELECT (select ROUND(sum(precio_entradas),2) from entradas) total_entradas from entradas") 
    fetch = cur.fetchall()
    for data in fetch:

        tree1.insert('', 'end', values=(data),  tags = ('par',))
        break



    #---------------SUMA DEL NUMERO TOTAL DE ENTRADAS VENDIDAS
    cur.execute("SELECT (select sum(numero_entradas) from entradas) n_total_entradas from entradas") 
    fetch = cur.fetchall()
    for data in fetch:

        tree2.insert('', 'end', values=(data),  tags = ('par',))
        break




    #----------SINCRONIZAMOS POSICION DE LA LISTA DESPLEGABLE CON LOS MESES DEL AÑO
    if ldesplegable_mes_entradas1.current() == 0 :
        mes_entradas = '01'
    elif ldesplegable_mes_entradas1.current() == 1 :
        mes_entradas = '02'
    elif ldesplegable_mes_entradas1.current() == 2 :
        mes_entradas = '03'
    elif ldesplegable_mes_entradas1.current() == 3 :
        mes_entradas = '04'
    elif ldesplegable_mes_entradas1.current() == 4 :
        mes_entradas = '05'
    elif ldesplegable_mes_entradas1.current() == 5 :
        mes_entradas = '06'
    elif ldesplegable_mes_entradas1.current() == 6 :
        mes_entradas = '07'
    elif ldesplegable_mes_entradas1.current() == 7 :
        mes_entradas = '08'
    elif ldesplegable_mes_entradas1.current() == 8 :
        mes_entradas = '09'
    elif ldesplegable_mes_entradas1.current() == 9 :
        mes_entradas = '10'
    elif ldesplegable_mes_entradas1.current() == 10 :
        mes_entradas = '11'
    elif ldesplegable_mes_entradas1.current() == 11 :
        mes_entradas = '12'

    #Sacamos año seleccionado en entradas
    anio_entradas = int(spinbox2.get())

    #añadimos guion para mas claridad de la funcion
    guion = '-'

    #Con calendar, conseguimos sacar una tupla con los dias que tiene un mes, segun el mes y el año ej (3,31)
    #donde el primer valor de la tupla será el primer dia de la semana donde empieza el mes y el segundo
    #valor de la tupla será los dias que tiene ese mes
    dia_del_mes = calendar.monthrange(int(anio_entradas),int(mes_entradas))

    
    #generamos la fecha inicial (fecha_ini) poniendo el primer dia del mes posible
    fecha_ini = str(anio_entradas) + str(guion) + str(mes_entradas) + str(guion) + str('01')
    #generamos la fecha final (fecha_fin) poniendo el ultimo dia del mes posible, el ultimo dia será
    #la segunda posicion de la tupla que hemos acado con calendar
    fecha_fin = str(anio_entradas) + str(guion) + str(mes_entradas) + str(guion) + str(dia_del_mes[1])

    #las convertimos en fechas entendibles para el SQL
    fecha_ini1 = datetime.strptime(fecha_ini, '%Y-%m-%d' )
    fecha_fin1 = datetime.strptime(fecha_fin, '%Y-%m-%d')

    fecha_ini2 = fecha_ini1.date()
    fecha_fin2 = fecha_fin1.date()

    #chivato
    print(fecha_ini2)
    print(fecha_fin2)

    #Guardamos la consulta en variables para facilitar el trabajo
    pregunta = "SELECT ROUND(SUM(precio_entradas),2) from entradas Where (entradas.fecha_entradas >= ? AND entradas.fecha_entradas <= ?)"
    argumento = (fecha_ini2, fecha_fin2)

    #realizamos la consulta creando el bucle para comparar todas las filas
    cur.execute(pregunta, argumento)
    fetch = cur.fetchall()
    for data in fetch:
        tree3.insert('', 'end', values=(data),  tags = ('par',))
        break

    #cerramos cursor y conexion con BDD
    cur.close()
    db.close()



#---------------------INSERTA Y ACTUALIZA LOS CAMPOS DE LOS ABONOS----------------

def ACTUALIZAR_TODO_F4_ABONOS():

    #conectamos con bdd
    db=sql.connect("database.db")
    cur=db.cursor()

    #Borramos todos los campos para así poder actualizarlos
    tree5.delete(*tree5.get_children())
    tree6.delete(*tree6.get_children())
    tree7.delete(*tree7.get_children())

    #----------SUMA DEL TOTAL RECAUDADO POR LOS ABONOS
    cur.execute("SELECT (select ROUND(sum(precio_abonos),2) from abonos) total_abonos from abonos") 
    fetch = cur.fetchall()
    for data in fetch:

        tree5.insert('', 'end', values=(data),  tags = ('par',))
        break

    
    
    #----------SUMA DE TODOS LOS ABONOS VENDIDOS
    ultima_fila_abono = "SELECT count(codigo_abonos) FROM abonos;"
    cur.execute(ultima_fila_abono) 
    fetch = cur.fetchall()

    for data in fetch:

        tree6.insert('', 'end', values=(data),  tags = ('par',))
        break
   

   #----------SINCRONIZAMOS POSICION DE LA LISTA DESPLEGABLE CON LOS MESES DEL AÑO ABONOS
    if ldesplegable_mes_abonos2.current() == 0 :
        mes_abonos = '01'
    elif ldesplegable_mes_abonos2.current() == 1 :
        mes_abonos = '02'
    elif ldesplegable_mes_abonos2.current() == 2 :
        mes_abonos = '03'
    elif ldesplegable_mes_abonos2.current() == 3 :
        mes_abonos = '04'
    elif ldesplegable_mes_abonos2.current() == 4 :
        mes_abonos = '05'
    elif ldesplegable_mes_abonos2.current() == 5 :
        mes_abonos = '06'
    elif ldesplegable_mes_abonos2.current() == 6 :
        mes_abonos = '07'
    elif ldesplegable_mes_abonos2.current() == 7 :
        mes_abonos = '08'
    elif ldesplegable_mes_abonos2.current() == 8 :
        mes_abonos = '09'
    elif ldesplegable_mes_abonos2.current() == 9 :
        mes_abonos = '10'
    elif ldesplegable_mes_abonos2.current() == 10 :
        mes_abonos = '11'
    elif ldesplegable_mes_abonos2.current() == 11 :
        mes_abonos = '12'

    #sacamos el año seleccionado en abonos
    anio_abonos = int(spinbox3.get())
    
    #transformo guion en variable para hacerlo mas entendible
    guion = '-'

    #Con calendar, conseguimos sacar una tupla con los dias que tiene un mes, segun el mes y el año ej (3,31)
    #donde el primer valor de la tupla será el primer dia de la semana donde empieza el mes y el segundo
    #valor de la tupla será los dias que tiene ese mes
    dia_del_mes = calendar.monthrange(int(anio_abonos),int(mes_abonos))

    
    #generamos la fecha inicial (fecha_ini) poniendo el primer dia del mes posible
    fecha_ini = str(anio_abonos) + str(guion) + str(mes_abonos) + str(guion) + str('01')
    #generamos la fecha final (fecha_fin) poniendo el ultimo dia del mes posible, el ultimo dia será
    #la segunda posicion de la tupla que hemos acado con calendar
    fecha_fin = str(anio_abonos) + str(guion) + str(mes_abonos) + str(guion) + str(dia_del_mes[1])

    #lo convertimos en legible para SQL
    fecha_ini1 = datetime.strptime(fecha_ini, '%Y-%m-%d' )
    fecha_fin1 = datetime.strptime(fecha_fin, '%Y-%m-%d')
    fecha_ini2 = fecha_ini1.date()
    fecha_fin2 = fecha_fin1.date()

    #chivatos
    print(fecha_ini2)
    print(fecha_fin2)

    #guardamos la consulta en variables
    pregunta = "SELECT ROUND(SUM(precio_abonos),2) from abonos Where (abonos.fecha_abonos >= ? AND abonos.fecha_abonos <= ?)"
    argumento = (fecha_ini2, fecha_fin2)

    #ejecutamos el cursosr y creamos el bucle
    cur.execute(pregunta, argumento)
    fetch = cur.fetchall()
    for data in fetch:
        tree7.insert('', 'end', values=(data),  tags = ('par',))
        break

    #cerramos cursor y bdd
    cur.close()
    db.close()



#seleccionable mes para saber las entradas vendidas
def ldesplegable_mes_entradas(event):
     print("Nuevo mes seleccionado")
     

ldesplegable_mes_entradas1 = ttk.Combobox(frame2f4, state="readonly", width=12,
                            values=[
                                    " Enero",
                                    " Febrero",
                                    " Marzo",
                                    " Abril",
                                    " Mayo",
                                    " Junio",
                                    " Julio",
                                    " Agosto",
                                    " Septiembre",
                                    " Octubre", 
                                    " Noviembre",
                                    " Diciembre"])


ldesplegable_mes_entradas1.place(x=365, y=133)
ldesplegable_mes_entradas1.current(0)

ldesplegable_mes_entradas1.bind("<<ComboboxSelected>>", ldesplegable_mes_entradas)


#-----------------------------------RECUADROS Y ETIQUETAS ESTADISTICAS---------------------------------------

#Titulo estadisticas
lbl_title = Label(frame1f4, width=30, font=('dejavu sans', 18), fg=c_letra_fondo1_label, bg=c_fondo1_label,text="Estadísticas generales")
lbl_title.grid(row=1, column=1, columnspan=5, padx=5, pady=15, sticky=W)


#Titulo estadisticas entradas
lbl_entradas = Label(frame2f4, width=56, fg=c_letra_fondo1_label, bg=c_fondo1_label, font=('dejavu sans', 11), text="Estadísticas de las entradas")
lbl_entradas.grid(row=0, column=0, columnspan=5, padx=5, pady=15, sticky=W)

#ESPACIO
esp = Label(frame2f4, bg=c_frame1, fg=c_letra1, font=('Verdana', 10,'bold'), text="")     
esp.grid(row=1, column=0, padx=0, pady=0, columnspan=14, sticky=E)


#Recaudacion total entradas
etiqueta13 = Label(frame2f4, bg=c_frame1, fg=c_letra1, font=('dejavu sans', 9,'bold'), text="Recaudación total entradas")     
etiqueta13.grid(row=2, column=0, padx=5, pady=5, columnspan=2, sticky=W)

#Entradas totales por meses entradas
etiqueta14 = Label(frame2f4, bg=c_frame1, fg=c_letra1, font=('dejavu sans', 9,'bold'), text="Recaudación total por mes")     
etiqueta14.grid(row=2, column=2, padx=5, pady=5, columnspan=5, sticky=W)

etiqueta15 = Label(frame2f4, bg=c_frame1, fg=c_letra1, text="Seleccione el mes: ")     
etiqueta15.grid(row=3, column=2, padx=5, pady=5, columnspan=1, sticky=W)

valor_anio = StringVar()
spinbox2 = Spinbox(frame2f4, font=('', 10,''),  from_=2019, to=2999, width=5, textvariable=valor_anio, state="readonly")
spinbox2.place(x=462, y=132)

#BOTON ACTUALIZAR_ENTRADAS
b27 = Button(frame6f4, bg = fondo1_boton, width=141, fg = c_letra1, font=('', 10,''), text="     Actualizar", relief=t_borde1_botones, command=ACTUALIZAR_TODO_F4_ENTRADAS, image = photoimage16, compound = LEFT)
b27.place(width=169, height=40, x=350, y=0)





#--------------------------------DISEÑO TABLA TOTAL RECAUDADO ABONOS----------------------------

#--------------------------- NUMERO ABONOS VENDIDOS------------------------
tree6 = ttk.Treeview(frame5f4, style="mystyle.Treeview", columns=("n_total_abonos"), selectmode="extended", height=1)
tree6.grid(row=3, column=0, padx=10, pady=15, columnspan=2, sticky=E)

tree6.heading('n_total_abonos', text=" Abonos vendidos ",anchor=W)
tree6.column('#0', stretch=NO, minwidth=0, width=0)
tree6.column('#1', stretch=NO, minwidth=0, width=230)

tree6.tag_configure('par', background=c_fondo1_entry)



#--------------------------- CANTIDAD DINERO RECAUDADO-----------------------
tree5 = ttk.Treeview(frame5f4, style="mystyle.Treeview", columns=("total_abonos"), selectmode="extended", height=1)
tree5.grid(row=4, column=0, padx=10, pady=15, columnspan=2, sticky=E)

tree5.heading('total_abonos', text=" Total (euros) ",anchor=W)
tree5.column('#0', stretch=NO, minwidth=0, width=0)
tree5.column('#1', stretch=NO, minwidth=0, width=230)

tree5.tag_configure('par', background=c_fondo1_entry)



#--------------------------- DINERO DE abonos RECAUDADO POR MES-----------------
tree7 = ttk.Treeview(frame5f4, style="mystyle.Treeview", columns=("total_mes_recaudado"), selectmode="extended", height=1)
tree7.grid(row=4, column=3, padx=10, pady=15, columnspan=2, sticky=E)

tree7.heading('total_mes_recaudado', text=" Total (euros) ",anchor=W)
tree7.column('#0', stretch=NO, minwidth=0, width=0)
tree7.column('#1', stretch=NO, minwidth=0, width=250)

tree7.tag_configure('par', background=c_fondo1_entry)



#-----------------------------FUNCIONES ESTADISTICAS(abonos)----------------------------



#lista desplegable dinero ganado por mes de los abonos
def ldesplegable_mes_abonos(event):
     print("Nuevo mes seleccionado")
     

ldesplegable_mes_abonos2 = ttk.Combobox(frame5f4, state="readonly", width=12,
                            values=[
                                    " Enero",
                                    " Febrero",
                                    " Marzo",
                                    " Abril",
                                    " Mayo",
                                    " Junio",
                                    " Julio",
                                    " Agosto",
                                    " Septiembre",
                                    " Octubre", 
                                    " Noviembre",
                                    " Diciembre"])


ldesplegable_mes_abonos2.place(x=365, y=133)
ldesplegable_mes_abonos2.current(0)

ldesplegable_mes_abonos2.bind("<<ComboboxSelected>>", ldesplegable_mes_abonos)




#-------------------------------------ETIQUETAS Y BOTONES ABONOS----------------------
#Titulo estadisticas abonos
lbl_abonos10 = Label(frame5f4, width=56, fg=c_letra_fondo1_label, bg=c_fondo1_label, font=('dejavu sans', 11), text="Estadísticas de los abonos")
lbl_abonos10.grid(row=0, column=0, columnspan=5, padx=5, pady=15, sticky=W)

#ESPACIO
esp = Label(frame5f4, bg=c_frame1, fg=c_letra1, font=('Verdana', 10,'bold'), text="")     
esp.grid(row=1, column=0, padx=0, pady=0, columnspan=14, sticky=E)

#Recaudacion total abonos
etiqueta16 = Label(frame5f4, bg=c_frame1, fg=c_letra1, font=('dejavu sans', 9,'bold'), text="Recaudación total abonos")     
etiqueta16.grid(row=2, column=0, padx=5, pady=5, columnspan=2, sticky=W)

#abonos totales por meses abonos
etiqueta16 = Label(frame5f4, bg=c_frame1, fg=c_letra1, font=('dejavu sans', 9,'bold'), text="Recaudación total por mes")     
etiqueta16.grid(row=2, column=3, padx=5, pady=5, columnspan=5, sticky=W)

etiqueta19 = Label(frame5f4, bg=c_frame1, fg=c_letra1, text="Seleccione el mes: ")     
etiqueta19.grid(row=3, column=2, padx=5, pady=5, columnspan=2, sticky=W)

valor_anio1 = StringVar()
spinbox3 = Spinbox(frame5f4, font=('', 10,''),  from_=2019, to=2999, width=5, textvariable=valor_anio1, state="readonly")
spinbox3.place(x=462, y=132)



#BOTON ACTUALIZAR ABONOS
b26 = Button(frame7f4, bg = fondo1_boton, fg = c_letra1, font=('', 10,''), text="     Actualizar", relief=t_borde1_botones, command=ACTUALIZAR_TODO_F4_ABONOS, image = photoimage16, compound = LEFT)
b26.place(width=169, height=40, x=350, y=0)
