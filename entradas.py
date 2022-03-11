
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
import configparser
from variables import *
from conexion import *
from estructura import *
from ventanas_hijas import *
from datetime import *



#=====================================PESTAÑA ENTRADAS============================================

#---------------------CONTROL DE DIAS-------------------------
#con estas condiciones conseguimos que cada dia las entradas vendidas se reinicien------
fecha_actual = datetime.now().date()  #fecha_actual

if str(fecha_actual) != str(fecha1_guardada):

    config.set("CONFIGURACION", "total_entradas_dia", str(resetear_entradas))

    with open("config.ini", "w") as f:
        config.write(f)


#---------------------CONFIGURACION DEL AFORO MAXIMO DE ENTRADAS-------------------
#aqui vamos a guardar en "casi _aforo _maximo" el numero de entradas que queramos que nos salte el aviso
#antes de llegar al maximo
#en este caso, "margen" = 20 con lo cual, "casi_aforo_maximo_entradas" será el aforo maximos que haya puesto
#menos 20, y lo guardamos en "casi_aforo_maximo" en el config.ini
casi_aforo_maximo_entradas = (+int(aforo1_maximo) - margen) #el aforo maximo puesto menos el margen(20 en este caso)
config.set("CONFIGURACION", "casi_aforo_maximo", str(casi_aforo_maximo_entradas)) #cambiamos el campo en el config.ini

with open("config.ini", "w") as f:
    config.write(f) #guardamos cambios




#---------------------------------FUNCIONES-----------------------------------

#multiplicacion del numero de entradas que vamos a vender con sus respectivos precios
def multiplicar():                                         
    global _valor
    global _valor1
    global _valor2
    global _valor3
    global valor_total
    global _valor_infantil
    global numero_total_entradas

    try:
        _valor1 = int(entrada_texto.get()) #numero de entradas de adulto del seleccionable
        _valor2 = float(precio1_adulto) #precio que valen las entradas de adulto
        _valor3 = int(entrada_textoinfantil.get()) #numero de entradas de niño del seleccionable         
        _valor4 = float(precio1_infantil) #precio que valen las entradas de niño
        _valor =  float("{0:.2f}".format(_valor1 * _valor2)) #multi del numero de entradas por el precio adulto
        _valor_infantil =  float("{0:.2f}".format(_valor3 * _valor4)) #multi del numero de entradas por el precio niño
        valor_total = float("{0:.2f}".format(_valor + _valor_infantil)) #suma precio total entradas niño + adulto


        valor25.set(str(valor_total) + euro) #Se muestra el resultado del precio total
        
    #Nos saltará el siguiente mensaje si se comete algún error
    except ValueError:
        messagebox.showinfo("Error", "El campo está vacío o ha introducido letras o caracteres especiales, introduzca un número entero por favor")

    
#Resta del precio total de las entradas con el dinero que nos ofrece el cliente. el objetivo de
#esta funcion es obtener el cambio.
def restar():  
    global _valor20
    global _valor30
    global valor_total

    try:
        _valor20 = int(entrada1_texto.get()) #Extrae del recuadro el dinero que nos da el cliente
        _valor30 = float("{0:.2f}".format(_valor20 - valor_total)) #lo restamos para que nos de las vueltas
        valor26.set(str(_valor30) + euro) #lo mostramos con el simbolo de euros

    #Nos saltará el siguiente mensaje si se comete algún error
    except ValueError:
         messagebox.showinfo("Error", "El campo está vacío o no ha introducido un caracter válido, por favor, introduzca un número entero.")




#Con esta funcion guardaremos el numero de entrada vendidas, el tipo de entrada vendida (adulta o infantil)
# y el dinero obtenido.
def entradas1():

    #Extraer resultado de las entradas para comprobar si están vacias
    _valor1 = int(entrada_texto.get())
    _valor3 = int(entrada_textoinfantil.get())

    #si lo estan, se muestra el mensaje y se borra
    if  _valor1 == 0 and _valor3 == 0:
        messagebox.showinfo('Venta de entradas', 'Campos vacíos')
        borrar()
    
    #si no lo están, sigue el programa..
    else:
        if messagebox.askyesno('Vender entradas', '¿Está seguro de vender las entradas?'):
        
            _valor1 = int(entrada_texto.get())
            _valor2 = float(precio1_adulto)
            _valor3 = int(entrada_textoinfantil.get())
            _valor4 = float(precio1_infantil)
            p_entradas_adul =  float("{0:.2f}".format(_valor1 * _valor2))
            p_entradas_inf =  float("{0:.2f}".format(_valor3 * _valor4))

            #entradas adulto
            n_entradas_adul = int(entrada_texto.get())
            t_entradas_adul = "Adulto"

            #guardamos los resultados de los adultos en la tabla "entradas"
            cur.execute("INSERT INTO entradas(codigo_entradas,numero_entradas,fecha_entradas,precio_entradas, tipo_entradas)VALUES(null,?,current_date,?,?)",(n_entradas_adul,p_entradas_adul,t_entradas_adul))
            db.commit()

            #entradas infantil
            n_entradas_inf = int(entrada_textoinfantil.get())
            t_entradas_inf = "Infantil"
    
            #guardamos los resultados de los niños en la tabla "entradas"
            cur.execute("INSERT INTO entradas(codigo_entradas,numero_entradas,fecha_entradas,precio_entradas, tipo_entradas)VALUES(null,?,current_date,?,?)",(n_entradas_inf,p_entradas_inf,t_entradas_inf))
            db.commit()

            #llamamos a la variable borrar, para borrar los campos despues de introducirlos en la bdd
            borrar()

            #guardamos en una variable el numero total de entradas
            numero_total_entradas = n_entradas_adul + n_entradas_inf

            #mostramos el siguiente mensaje con el numero y la hora de las entradas vendidas
            global correcto5
            hora = datetime.now()
            correcto5 = Label(f1, bg=c_fondo1, compound = LEFT, fg="#6BF066", font=('', 9,'bold'),  text="Se han vendido "+str(numero_total_entradas) + " entradas a las " +str(hora.strftime("%H:%M:%S")) )   
            correcto5.place(width=300, height=35, x=513, y=455)


            #Abrimos fichero configuracion
            config = configparser.ConfigParser()
            config.read('config.ini')

            # saca las entradas que van vendidas
            total_entradas_dia_pre = config.get("CONFIGURACION", "total_entradas_dia")
            total_entradas1_dia= total_entradas_dia_pre.strip('""') #Limpia  las comillas

            total_entradas1_dia = int(total_entradas1_dia) + int(numero_total_entradas)
            
            #guardamos el resultado en el fichero para que si cerramos la aplicacion, no se borre.
            config.set("CONFIGURACION", "total_entradas_dia", str(total_entradas1_dia))
            config.set("CONFIGURACION", "fecha_guardada", str(fecha_actual))

            with open("config.ini", "w") as f:
                config.write(f)

            #---------------------------------CONTROL DE AFORO-----------------------------------
            #con esta condicion comprobamos si no se han vendido mas entradas que aforo tiene la piscina.
            if int(aforo1_maximo) < int(total_entradas1_dia):
                messagebox.showinfo("AVISO", "Se ha superado el aforo maximo.")
            
            #con esta condicion comprobamos que no se ha superado el maximo de entradas vendidas por dia.
            elif int(casi_aforo1_maximo) < int(total_entradas1_dia): #si casi_aforo_maximo es menor que las entradas
                messagebox.showinfo("AVISO", "Está cerca de superarse el aforo máximo permitido.")
            

        #si el usuario pulsa en cancelar venta de entradas mostramos el siguiente mensaje
        else:
            borrar()
            messagebox.showinfo('Venta de entradas', 'No se vendieron entradas')


#Esta funcion nos borra las casillas del ingreso de los nuevos usuarios abonados pero NO el letrero verde de los abonos
def borrar():

    valor.set(0)
    valor_tipo_entradas.set(0)
    _valor1 = 0
    _valor2 = 0
    valor25.set('')
    valor26.set('')
    valor2.set('')
    _valor10 = 0
    _valor20 = 0
    _valor30 = 0

#Esta funcion tambien borra los letreros verdes (correcto5, correcto6...)
def borrar_todo():

    if 'correcto5' in globals():
        correcto5.destroy()
    if 'incorrecto' in globals():
        incorrecto.destroy()
    
    valor.set(0)
    valor_tipo_entradas.set(0)
    _valor1 = 0
    _valor2 = 0
    valor25.set('')
    valor26.set('')
    valor2.set('')
    _valor10 = 0
    _valor20 = 0
    _valor30 = 0





#------------------------RECUADROS Y ETIQUETAS VENTA DE ENTRADAS------------------------------

#titulo
lbl_title5 = Label(frame1f1, width=66, fg=c_letra_fondo1_label, bg=c_fondo1_label,  font=('dejavu sans', 18), text="Vender entradas ")
lbl_title5.grid(row=0, column=0, columnspan=19, padx=5, pady=25, sticky=W)


#TEXTO NUMERO DE ENTRADAS ADULTOS
etiqueta = Label(frame1f1, bg=c_frame1, fg=c_letra1, font=('', 10,''),  text="Entradas adulto: ")     
etiqueta.grid(row=4, column=3, padx=5, pady=5, columnspan=4, sticky=E)

#RECUADRO NUMERO DE ENTRADAS                                                              
valor = StringVar()
entrada_texto = Spinbox(frame1f1, font=('', 10,''),  from_=0, to=30, width=30, textvariable=valor, state="readonly")
entrada_texto.grid(row=4, column=7, padx=5, pady=5, columnspan=5, sticky=W)


#TEXTO NUMERO DE ENTRADAS INFANTILES
etiqueta_infantil = Label(frame1f1, bg=c_frame1, fg=c_letra1, font=('', 10,''),  text="Entradas infantil: ")     
etiqueta_infantil.grid(row=5, column=3, padx=5, pady=5, columnspan=4, sticky=E)

#RECUADRO NUMERO DE ENTRADAS                                                              
valor_tipo_entradas = StringVar()
entrada_textoinfantil = Spinbox(frame1f1,  font=('', 10,''),  from_=0, to=30, width=30, textvariable=valor_tipo_entradas, state="readonly")
entrada_textoinfantil.grid(row=5, column=7, padx=5, pady=5, columnspan=5, sticky=W)


#BOTON "MULTIPLICAR"
photo2 = PhotoImage(file = c_imagen1_precio_total)  
photoimage2 = photo2.subsample(1, 1) 
b1 = Button(frame1f1, text = '   Precio total', font=('', 10,''), bg = fondo1_boton, fg = c_letra1, relief=t_borde1_botones, command=multiplicar, image = photoimage2, compound = LEFT)
b1.place(width=150, height=45, x=600, y=90)



#TEXTO PARA INDICAR LO QUE CUESTAN TODAS LAS ENTRADAS
etiqueta25 = Label(frame1f1, bg=c_frame1, fg=c_letra1, font=('', 10,'bold'),  text="Precio total: ")     
etiqueta25.grid(row=8, column=3, columnspan=4, padx=5, pady=15, sticky=E)


#RECUADRO PRECIO TOTAL DE ENTRADAS
valor25 = StringVar()
entrada25_texto = Entry(frame1f1, width=31, font=('', 10,'bold'),  state="readonly", readonlybackground='#F9FC8D', textvariable=valor25)
entrada25_texto.grid(row=8, column=7, padx=5, pady=15, columnspan=5, sticky=W)


#TEXTO EFECTIVO 
etiqueta4 = Label(frame1f1, bg=c_frame1, font=('', 10,''),  fg=c_letra1, text="Efectivo(euros): ")     
etiqueta4.grid(row=10, column=3, padx=5, pady=15, columnspan=4, sticky=E)

#RECUADRO DE LO QUE TE DA EL CLIENTE PARA PAGAR ESAS ENTRADAS !!!!!!!!!!!!!!!!
valor2 = StringVar()
entrada1_texto = Entry(frame1f1, width=31, font=('', 10,''),  textvariable=valor2)
entrada1_texto.grid(row=10, column=7, columnspan=5, padx=5, pady=5, sticky=W)


#TEXTO DEVOLUCION
etiqueta2 = Label(frame1f1, bg=c_frame1, fg=c_letra1, font=('', 10,'bold'),  text="A devolver: ")     
etiqueta2.grid(row=12, column=3, columnspan=4, padx=5, pady=15, sticky=E)

#RECUADRO VUELTAS QUE SE LE DEBEN AL CLIENTE

valor26 = StringVar()
entrada26_texto = Entry(frame1f1, width=31, font=('', 10,'bold'), state="readonly", readonlybackground=c_fondo1_entry, textvariable=valor26)
entrada26_texto.grid(row=12, column=7, padx=5, pady=15, columnspan=5, sticky=W)


#BOTON "DEVOLUCION"
photo3 = PhotoImage(file = c_imagen1_recargar)  
photoimage3 = photo3.subsample(1, 1) 
b6 = Button(frame1f1, bg = fondo1_boton, fg = c_letra1, font=('', 10,''), text="   Devolucion", relief=t_borde1_botones, command=restar, image = photoimage3, compound = LEFT)
b6.place(width=150, height=45, x=600, y=226)



#BOTON "BORRAR_TODO"
photo6 = PhotoImage(file = c_imagen1_borrar)  
photoimage6 = photo6.subsample(1, 1) 
b7 = Button(frame1f1, bg = fondo1_boton, fg = c_letra1, font=('', 10,''), text="   Borrar todo", relief=t_borde1_botones, borderwidth=2, command=borrar_todo, image = photoimage6, compound = LEFT)
b7.place(width=150, height=45, x=600, y=316)


#ESPACIO
espacio = Button(frame1f1, bg = c_frame1, highlightthickness=0, borderwidth=0, fg = c_letra1, text="",  command=entradas1)            
espacio.grid(row=19, column=7, columnspan=5, padx=35, pady=25, sticky=W)

#BOTON "ENTRADAS", guardamos las entradas en la bdd.
photo4 = PhotoImage(file = c_imagen1_compras)  
photoimage4 = photo4.subsample(1, 1) 
b8 = Button(frame1f1, bg = fondo1_boton, fg = c_letra1, font=('', 10,''), text="   Vender entradas", relief=t_borde1_botones, borderwidth=2, command=entradas1, image = photoimage4, compound = LEFT)
b8.place(width=169, height=45, x=765, y=316)