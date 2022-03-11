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
from datetime import datetime
import time
from variables import *
from conexion import *
from estructura import *
from ventanas_hijas import *
from entradas import *



#===================================== PESTAÑA ABONOS==================================================

db=sql.connect("database.db")
cur=db.cursor()


#nos muestra el numero de abono directamente de la tabla
tree16 = ttk.Treeview(frame1f2,  style="mystyle.Treeview", columns=("n_total_abonos"), selectmode="extended", height=1)
tree16.grid(row=4, column=3, padx=0, pady=15, columnspan=1, sticky=W)

tree16.heading('n_total_abonos',  text=" Nº abono", anchor=W)
tree16.column('#0', stretch=NO, minwidth=0, width=0)
tree16.column('#1', stretch=NO, minwidth=0, width=220)

tree16.tag_configure('par', font=('', 10,'bold'), background='#F9FC8D')



#---------------------FUNCIONES ABONOS Y AGREGAR CLIENTES--------------------

#funcion de seleccion del tipo de abono (individual o familiar)
def ldesplegable(event):
     print("")
     

listadesplegable1 = ttk.Combobox(frame1f2, font=('', 10,''), state="readonly", width=29,
                            values=[
                                    " --",
                                    " Individual", 
                                    " Familiar"])


listadesplegable1.grid(row=2, column=3, padx=0, pady=15, columnspan=1, sticky=W)
listadesplegable1.current(0)

listadesplegable1.bind("<<ComboboxSelected>>", ldesplegable)

#funcion que nos guarda los abonos en la tabla "abonos"
def g_abonos_1():
    
    #pregunta al usuario si desea generar un nuevo abono
    if messagebox.askyesno('Abonos', '¿Desea generar un nuevo abono?'):
        
        global contador_control_abonos
        global precio_abonos
        global tipo_abonos

        #listadesplegable1.current() nos saca la posicion donde está marcado el tipo de abono ("0" o "1" en este caso)
        if listadesplegable1.current() == 0:
            messagebox.showinfo('Seleccionar tipo de abono', 'No ha seleccionado ningún tipo de abono.')
        else:
            
            #segun el elemento seleccionado de la lista, modifica la variable "tipo_abonos"
            if listadesplegable1.current() == 1:
                tipo_abonos = "Individual"
                precio_abonos = 33
                contador_control_abonos = 0

            elif listadesplegable1.current() == 2:
                tipo_abonos = "Familiar"
                precio_abonos = 80
                contador_control_abonos = 0

            #muestra directamente el precio segun el tipo de abono + el simbolo de euros
            precio_abono25.set(str(precio_abonos) + euro)
            fecha = datetime.now()
            fecha1 = fecha.date()
            #guardamos en la bdd el abono
            cur.execute("INSERT INTO abonos(codigo_abonos,tipo_abonos,fecha_abonos,precio_abonos)VALUES(null,?,?,?)",(tipo_abonos,fecha1,precio_abonos))
            db.commit()


            #Selecionamos el ultimo campo de la columna codigo_abonos para monstarlo en pantalla    
            tree16.delete(*tree16.get_children())
            ultima_fila_abono = "SELECT codigo_abonos FROM abonos ORDER BY ROWID DESC LIMIT 1;"
            cur.execute(ultima_fila_abono) 
            fetch = cur.fetchall()

            #bucle for que nos va sacando cada fila de la tabla abonos. "par", es el color de la fila.
            for data in fetch:
            
                e_c_abonos.set(data)
                tree16.insert('', 'end', values=(data),  tags = ('par',))
            
                break
        
            global abonos_creados
            abonos_creados = 1
            global correcto8
            hora = datetime.now()
            #Texto en verde que nos confirma la creacion del abono con la hora.
            correcto8 = Label(f2, bg=c_fondo1, compound = LEFT, fg="#6BF066", font=('', 9,'bold'),  text="Se ha generado un nuevo abono " +tipo_abonos + " a las " +str(hora.strftime("%H:%M:%S")) + " \n ya puede añadir los usuarios correspondientes en el panel de \"Clientes\"." )   
            correcto8.place(width=460, height=50, x=95, y=520)


#funcion que nos calcula el cambio que le devolveremos al cliente segun lo que nos de.
def cambio():
    global cambio1
    global resultado_cambio                                         

    try:
        
        cambio1 = int(cambio_abonos_texto.get())
        resultado_cambio = float("{0:.2f}".format(cambio1 - precio_abonos))
        adevolver25.set(str(resultado_cambio) + euro)
    except ValueError:
         messagebox.showinfo("Error", "No se admiten letras ni caracteres especiales, introduzca un número entero por favor")


#funcion que introduce los clientes con el abono que hayamos seleccionado anteriormente.
def g_clientes():

    global contador_control_abonos
    global photoimage20
    global photoimage21
    global abonos_creados



    #si no se ha creado ningun abono:
    if  abonos_creados == 0:
        messagebox.showinfo('Asignar clientes', 'Se debe generar un abono para poder vincularle un cliente.')
    else :

        if messagebox.askyesno('Usuarios', '¿Está seguro de añadir un nuevo usuario?'):
            #ejecutamos las variables que nos comprueban los campos
            validar_nombre()
            validar_apellidos()
            validar_dni()
            validar_telefono()

            #si el nombre no es correcto
            if error_campo1 == 1:
                messagebox.showinfo("Error", "El Nombre no es correcto, Debe empezar por mayúscula, sin espacios y sin números.")
            #si el apellido no es correcto
            elif error_campo2 == 1:
                messagebox.showinfo("Error", "El Apellido no es correcto, Debe empezar por mayúscula y sin números.")
            #si el dni no es correcto
            elif error_campo3 == 1:
                messagebox.showinfo("Error", "El DNI no es correcto, Debe contener 8 dígitos y una letra final en MAYÚSCULA.")
            #si el telefono no es correcto
            elif error_campo4 ==1:
                messagebox.showinfo("Error", "El Teléfono no es correcto, Debe contener 9 dígitos, debe empezar por 6, 7 o 9.")
    
            else:
                #guarda los respectivos campos del formulario en las variables
                n_clientes = str(e_c_nombre.get())
                a_clientes = str(e_c_apellidos.get())
                dni_clientes = str(e_c_dni.get())
                t_clientes = int(e_c_telefono.get())
                c_abonos_pre = str(e_c_abonos.get())                            
                c_abonos = c_abonos_pre.strip("(" ")" ",") #Limpia los parentesis y las comas y lo guarda en c_abonos


                #si seleccionamos abono familiar el contador lo volvemos a poner a 0 
                if listadesplegable1.current() == 2 : 
                    contador_control_abonos = 0

                #si seleccionamos abono individual y ademas se ha guardado ya un cliente, no permitimos guardar mas.
                if listadesplegable1.current() == 1 and contador_control_abonos == 1 :
                    messagebox.showinfo("Error", "No puede introducir más de un cliente en un abono individual.")
                #si el abono no es individual o es individual pero no se ha creado ningun usuario, guardamos usuario en bdd
                else :
                    cur.execute("INSERT INTO clientes(codigo_clientes,nombre,apellidos,dni,telefono,fecha_clientes,codigo_ab)VALUES(null,?,?,?,?,current_date,?) ",(n_clientes,a_clientes,dni_clientes,t_clientes,c_abonos))
                    db.commit()
                    borrar1()
                    contador_control_abonos = 1

                    #Texto en verde que nos confirma la creacion del abono con la hora.
                    global correcto10
                    hora = datetime.now()
                    correcto10 = Label(f2, bg=c_fondo1, compound = LEFT, fg="#6BF066", font=('', 9,'bold'), text = 'Se ha guardado el usuario ' + str(n_clientes) + ' en el abono número ' + str(c_abonos) + ' a las ' +str(hora.strftime("%H:%M:%S"))  )   
                    correcto10.place(width=420, height=20, x=685, y=535)
        else:
            messagebox.showinfo("Usuarios", "Se ha cancelado el proceso de vinculación con los usuarios.")

         


#borramos las imagenes y los campos del cuadro "clientes"
def borrar1():
    

    imagen_validar1.place_forget()
    imagen_validar2.place_forget()
    imagen_validar3.place_forget()
    imagen_validar4.place_forget()
    e_c_nombre.set('')
    e_c_apellidos.set('')
    e_c_dni.set('')
    e_c_telefono.set('')

#borra los campos que nos interesan del cuadro "abonos"
def limpiar_abonos():

    valor5.set('')
    adevolver25.set('')

#funcion de comprobacion 
def validar_nombre():
        global imagen_validar1
        global error_campo1
        cadena=e_c_nombre.get()
        patron=('^([A-Z]{1}[a-zñáéíóú]+[\s]*)+$')
        
        if(re.match(patron,cadena)):
            imagen_validar1 = Label(frame2f2, image = photoimage20, bg=c_frame1, fg=c_letra1,  font=('', 10,''), text="")
            imagen_validar1.place(width=45, height=45, x=345, y=87)     
            error_campo1 = 0
        else:
            imagen_validar1 = Label(frame2f2, image = photoimage21, bg=c_frame1, fg=c_letra1,  font=('', 10,''), text="")
            imagen_validar1.place(width=45, height=45, x=345, y=87)     
            error_campo1 = 1

#funcion de comprobacion 
def validar_apellidos():
        global imagen_validar2
        global error_campo2
        cadena=e_c_apellidos.get()
        patron=('([A-Z][a-z]*)([\\s\\\'-][A-Z][a-z]*)*')
        if(re.match(patron,cadena)):
            imagen_validar2 = Label(frame2f2, image = photoimage20, bg=c_frame1, fg=c_letra1,  font=('', 10,''), text="")
            imagen_validar2.place(width=45, height=45, x=345, y=137)     
            error_campo2 = 0
        else:
            imagen_validar2 = Label(frame2f2, image = photoimage21, bg=c_frame1, fg=c_letra1,  font=('', 10,''), text="")
            imagen_validar2.place(width=45, height=45, x=345, y=137)     
            error_campo2 = 1

#funcion de comprobacion 
def validar_dni():
        global imagen_validar3
        global error_campo3
        cadena=e_c_dni.get()
        patron=('[0-9]{8}[TRWAGMYFPDXBNJZSQVHLCKE]$')
        if(re.match(patron,cadena)):
            imagen_validar3 = Label(frame2f2, image = photoimage20, bg=c_frame1, fg=c_letra1,  font=('', 10,''), text="")
            imagen_validar3.place(width=45, height=45, x=345, y=187)
            error_campo3 = 0
        else:
            imagen_validar3 = Label(frame2f2, image = photoimage21, bg=c_frame1, fg=c_letra1,  font=('', 10,''), text="")
            imagen_validar3.place(width=45, height=45, x=345, y=187)     
            error_campo3 = 1

#funcion de comprobacion 
def validar_telefono():
        global imagen_validar4
        global error_campo4
        cadena=e_c_telefono.get()
        patron=('[9|6|7][0-9]{8}$')
        if(re.match(patron,cadena)):
            imagen_validar4 = Label(frame2f2, image = photoimage20, bg=c_frame1, fg=c_letra1,  font=('', 10,''), text="")
            imagen_validar4.place(width=45, height=45, x=345, y=237)
            error_campo4 = 0
        else:
            imagen_validar4 = Label(frame2f2, image = photoimage21, bg=c_frame1, fg=c_letra1,  font=('', 10,''), text="")
            imagen_validar4.place(width=45, height=45, x=345, y=237) 
            error_campo4 = 1


#----------------------------RECUADROS Y ETIQUETAS CREAR ABONOS----------------------------------

lbl_title6 = Label(frame1f2, width=36, fg=c_letra_fondo1_label, bg=c_fondo1_label, font=('dejavu sans', 18), text="Generar abono")
lbl_title6.grid(row=0, column=0, columnspan=19, padx=5, pady=15, sticky=W)

#ESPACIO
esp = Label(frame1f2, bg=c_frame1, fg=c_letra1, font=('Verdana', 10,'bold'), text="")     
esp.grid(row=1, column=0, padx=0, pady=0, columnspan=14, sticky=E)


#TEXTO LISTA DESPLEGABLE
seleccionar1 = Label(frame1f2, bg=c_frame1, fg=c_letra1, font=('', 10,''), text="Abono: ")     
seleccionar1.grid(row=2, column=0, padx=5, pady=15, columnspan=3, sticky=E)

#BOTON CREAR ABONO
photo7 = PhotoImage(file = c_imagen1_abono)  
photoimage7 = photo7.subsample(1, 1) 
b9 = Button(frame1f2, text = '   Nuevo abono', font=('', 10,''), bg = fondo1_boton, fg = c_letra1, relief=t_borde1_botones, command=g_abonos_1, image = photoimage7, compound = LEFT)
b9.place(width=150, height=45, x=355, y=90)


#PRECIO ABONO
etiqueta6 = Label(frame1f2, bg=c_frame1, fg=c_letra1, font=('Verdana', 10,'bold'), text="Precio: ")     
etiqueta6.grid(row=6, column=0, padx=5, pady=15, columnspan=3, sticky=E)


#RECUADRO PRECIO TOTAL DE ENTRADAS
precio_abono25 = StringVar()
precio_abono = Entry(frame1f2, width=31, state="readonly", readonlybackground=c_fondo1_entry, font=('', 10,'bold'), textvariable=precio_abono25)
precio_abono.grid(row=6, column=3, padx=0, pady=15, columnspan=2, sticky=W)

#TEXTO EFECTIVO 
etiqueta7 = Label(frame1f2, bg=c_frame1, fg=c_letra1, font=('', 10,''), text="Efectivo(euros): ")     
etiqueta7.grid(row=8, column=0, columnspan=3, padx=5, pady=15, sticky=E)

#EFECTIVO INTRODUCIDO POR EL CLIENTE
valor5 = StringVar()
cambio_abonos_texto = Entry(frame1f2, width=31, font=('', 10,''), textvariable=valor5)
cambio_abonos_texto.grid(row=8, column=3, columnspan=2, padx=0, pady=15, sticky=W)

#TEXTO DEVOLUCION
adevolver1 = Label(frame1f2, bg=c_frame1, fg=c_letra1, font=('', 10,'bold'), text="A devolver: ")     
adevolver1.grid(row=10, column=0, columnspan=3, padx=5, pady=15, sticky=E)

#RECUADRO VUELTAS QUE SE LE DEBEN AL CLIENTE
adevolver25 = StringVar()
adevolver2 = Entry(frame1f2, width=31, state="readonly", readonlybackground=c_fondo1_entry,font=('', 10,'bold'), textvariable=adevolver25)
adevolver2.grid(row=10, column=3, padx=0, pady=15, columnspan=2, sticky=W)


#BOTON DE DEVOLUCION
photo8 = PhotoImage(file = c_imagen1_recargar)  
photoimage8 = photo8.subsample(1, 1) 
b10 = Button(frame1f2, bg = fondo1_boton, fg = c_letra1, font=('', 10,''), text="   Devolucion", relief=t_borde1_botones, command=cambio, image = photoimage8, compound = LEFT)
b10.place(width=150, height=45, x=355, y=266)

#BOTON DE BORRAR
photo9 = PhotoImage(file = c_imagen1_borrar)  
photoimage9 = photo9.subsample(1, 1) 
b11 = Button(frame1f2, bg = fondo1_boton, fg = c_letra1, font=('', 10,''), text="   Borrar todo", relief=t_borde1_botones, borderwidth=2, command=limpiar_abonos, image = photoimage9, compound = LEFT)
b11.place(width=150, height=45, x=355, y=377)


#IMAGENES CORRECTO
photo20 = PhotoImage(file = r"img/marcarverde.png")  
photoimage20 = photo20.subsample(1, 1) 

#IMAGENES DE ERROR
photo21 = PhotoImage(file = r"img/multiplicar2.png")  
photoimage21 = photo21.subsample(1, 1) 

#boton limpiar abonos
espacio= Button(frame1f2, bg = c_frame1, highlightthickness=0, borderwidth=0,  fg = c_letra1, text="", command=limpiar_abonos)
espacio.grid(row=11, column=2, padx=0, pady=25,  columnspan=1, sticky=E)



#--------------------------------RECUADROS Y ETIQUETAS CREAR CLIENTES---------------------------
#titulo
lbl_title6 = Label(frame2f2, width=36, fg=c_letra_fondo1_label, bg=c_fondo1_label, font=('dejavu sans', 18), text="Añadir cliente")
lbl_title6.grid(row=0, column=0, columnspan=19, padx=5, pady=15, sticky=E)

#ESPACIO
esp = Label(frame2f2, bg=c_frame1, fg=c_letra1, font=('', 10,''), text="")     
esp.grid(row=1, column=0, padx=5, pady=0, columnspan=14, sticky=E)

#TEXTO NOMBRE
nombre_cli = Label(frame2f2, bg=c_frame1, fg=c_letra1, font=('', 10,''), text="Nombre: ")     
nombre_cli.grid(row=2, column=0, padx=5, pady=0, columnspan=3, sticky=E)

e_c_nombre = StringVar()
nombre_cli = Entry(frame2f2, width=31, font=('', 10,''), textvariable=e_c_nombre)
nombre_cli.grid(row=2, column=3, padx=5, pady=15, columnspan=6, sticky=W)

#TEXTO APELLIDOS
apellidos_cli = Label(frame2f2, bg=c_frame1, font=('', 10,''), fg=c_letra1, text="Apellidos: ")     
apellidos_cli.grid(row=3, column=0, padx=5, pady=5, columnspan=3, sticky=E)

e_c_apellidos = StringVar()
apellidos_cli = Entry(frame2f2, font=('', 10,''), width=31, textvariable=e_c_apellidos)
apellidos_cli.grid(row=3, column=3, padx=5, pady=15, columnspan=6, sticky=W)

#TEXTO DNI
dni_cli = Label(frame2f2, bg=c_frame1, font=('', 10,''), fg=c_letra1, text="Dni: ")     
dni_cli.grid(row=4, column=0, padx=5, pady=15, columnspan=3, sticky=E)

e_c_dni = StringVar()
dni_cli = Entry(frame2f2, width=31, font=('', 10,''), textvariable=e_c_dni)
dni_cli.grid(row=4, column=3, padx=5, pady=15, columnspan=6, sticky=W)

#NUMERO TELEFONO
telefono_cli = Label(frame2f2, bg=c_frame1, font=('', 10,''), fg=c_letra1, text="Telefono: ")     
telefono_cli.grid(row=5, column=0, padx=5, pady=15, columnspan=3, sticky=E)

e_c_telefono = StringVar()
telefono_cli = Entry(frame2f2, width=31, font=('', 10,''), textvariable=e_c_telefono)
telefono_cli.grid(row=5, column=3, padx=5, pady=15, columnspan=6, sticky=W)

#CODIGO ABONOS
etiqueta_u_f_a = Label(frame2f2, bg=c_frame1, font=('', 10,''), fg=c_letra1, text="")   
etiqueta_u_f_a.grid(row=6, column=3, padx=5, pady=15, columnspan=3, sticky=W)

abonos_cli = Label(frame2f2, bg=c_frame1, fg=c_letra1, font=('Verdana', 10,'bold'), text="Nº de Abono: ")     
abonos_cli.grid(row=6, column=0, padx=5, pady=15, columnspan=3, sticky=E)

e_c_abonos = StringVar()
abonos_cli = Entry(frame2f2, width=4, readonlybackground='#F9FC8D',textvariable=e_c_abonos, font=('', 10,'bold'), state="readonly")
abonos_cli.grid(row=6, column=3, padx=5, pady=15, columnspan=4, sticky=W)

#ESPACIO
espacio2 = Label(frame2f2, bg=c_frame1, fg=c_letra1, font=('', 10,''), text="")     
espacio2.grid(row=7, column=0, padx=5, pady=0, columnspan=7, sticky=E)

#ESPACIO
espacio2 = Label(frame2f2, bg=c_frame1, fg=c_letra1, font=('', 10,''), text="")     
espacio2.grid(row=8, column=4, padx=0, pady=25, columnspan=4, sticky=E)

#ESPACIO
espacio2 = Label(frame2f2, bg=c_frame1, fg=c_letra1, font=('', 10,''), text="")     
espacio2.grid(row=8, column=11, padx=11, pady=1, columnspan=4, sticky=W)

#BOTON BORRAR_TODO
photo11 = PhotoImage(file = c_imagen1_borrar)  
photoimage11 = photo11.subsample(1, 1) 
b12 = Button(frame2f2, bg = fondo1_boton, fg = c_letra1, font=('', 10,''), text="   Borrar todo", relief=t_borde1_botones, borderwidth=2, command=borrar1, image = photoimage11, compound = LEFT)
b12.place(width=150, height=45, x=170, y=377)

#BOTON AÑADIR CLIENTE
photo10 = PhotoImage(file = c_imagen1_usuario)  
photoimage10 = photo10.subsample(1, 1) 
b13 = Button(frame2f2, bg = fondo1_boton, fg = c_letra1, font=('', 10,''), text="   Añadir cliente", relief=t_borde1_botones, borderwidth=2, command=g_clientes, image = photoimage10, compound = LEFT)
b13.place(width=169, height=45, x=335, y=377)