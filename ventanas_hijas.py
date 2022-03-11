
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
import entradas
from variables import *
from conexion import *
from estructura import *

#=====================================FUNCIONES DE LAS VENTANAS HIJAS============================================

#----------------------------VENTANA APARIENCIA----------------------------------
def apariencia():
    global ventanaconf
    ventanaconf = tk.Toplevel(root)
    ventanaconf.title("Apariencia")
    ventanaconf.geometry("543x340")
    ventanaconf.resizable(0,0)
    ventanaconf.iconbitmap("img/apariencia.ico")
    ventanaconf.configure(background=c_fondo1)

    #FRAME APARIENCIA
    frame1_ventanaconf=ttk.Frame(ventanaconf, width=500, height=300, padding=10 )        
    frame1_ventanaconf.place(x=20, y=20)

    #colores grises y amarillos de fondo(cambia el config.ini)
    def colores_clasicos():
        global correcto1
        #TABLA PAR
        config.set("TABLA", "tabla_par", '"#F9FC8D"')
        config.set("TABLA", "tabla_impar", '"white"')

        #BOTONES
        config.set("BOTONES", "t_borde_botones", "raised")
        config.set("BOTONES", "c_fondo_botones", '"#CCCCCC"')
        config.set("BOTONES", "fondo_boton", '"#6F6F6F"') 

        #COLOR FONDO LABEL
        config.set("COLOR_FONDO", "c_fondo_label", '#f0f0f0')
        config.set("COLOR_FONDO", "c_letra_fondo_label", 'black')
        config.set("COLOR_FONDO", "c_fondo_entry", '"#F9FC8D"')
       
        #BOTON COLORES CLASICOS
        config.set("OTRAS_IMAGENES", "escala_grises", "img/colores_clasicos.png")
        config.set("OTRAS_IMAGENES", "escala_azules", "img/colores_predeterminados.png")
        config.set("OTRAS_IMAGENES", "escala_noche", "img/colores_modo_noche.png")

        #COLOR FONDO VENTANA CLASICOS(tonos grises)
        config.set("COLOR_FONDO_GENERAL", "c_fondo_general", '"#ECECEC"')
        config.set("COLOR_FONDO_GENERAL", "c_letra_general", "black")

        #COLOR FORMULARIO CLASICOS(tonos grises)
        config.set("COLOR_FONDO", "c_fondo", '"#ECECEC"')
        config.set("COLOR_FONDO", "c_frame", '"#9B9B9B"')
        config.set("COLOR_FONDO", "c_letra", '"#FFFFFF"')


        #COLOR FORMULARIO CLASICOS(tonos grises)
        config.set("COLOR_IMAGEN", "c_imagen_configuracion", "img/rueda-dentada-amarillo1.png")
        config.set("COLOR_IMAGEN", "c_imagen_ayuda", "img/auriculares-amarillo.png")
        config.set("COLOR_IMAGEN", "c_imagen_info", "img/info2-amarillo.png")
        config.set("COLOR_IMAGEN", "c_imagen_precio_total", "img/euro-amarillo.png")
        config.set("COLOR_IMAGEN", "c_imagen_recargar", "img/recargar-amarillo.png")
        config.set("COLOR_IMAGEN", "c_imagen_borrar", "img/borrar-amarillo.png")
        config.set("COLOR_IMAGEN", "c_imagen_compras", "img/carrito-de-compras-amarillo.png")
        config.set("COLOR_IMAGEN", "c_imagen_abono", "img/abono-amarillo2.png")
        config.set("COLOR_IMAGEN", "c_imagen_usuario", "img/usuario-amarillo.png")
        config.set("COLOR_IMAGEN", "c_imagen_actualizar", "img/actualizar-amarillo2.png")
        config.set("COLOR_IMAGEN", "c_imagen_buscar", "img/buscar-amarillo2.png")
        config.set("COLOR_IMAGEN", "c_imagen_logo", "img/logo-amarillo.png")
        config.set("COLOR_IMAGEN", "c_imagen_apariencia", "img/controles-amarillo.png")
        config.set("COLOR_IMAGEN", "c_imagen_apariencia_tipo", "img/controles_amarillo_2.png")
        config.set("COLOR_IMAGEN", "c_imagen_tachuela", "img/tachuela-amarillo.png")
        config.set("COLOR_IMAGEN", "c_imagen_tuerca", "img/tuerca-amarilla.png")
        config.set("COLOR_IMAGEN", "c_imagen_contacto24", "img/contacto-amarillo24.png")

        with open("config.ini", "w") as f:
            config.write(f)
        
        #Confirmar seleccion de apariencia
        correcto1 = Label(ventanaconf, bg=c_frame1, compound = LEFT, fg="#6BF066", font=('', 9,'bold'),  text=" Se ha seleccionado la apariencia \"Clásica\". \n Los cambios se aplicarán después de reiniciar la aplicación.")     
        correcto1.place(width=400, height=40, x=70, y=260)
        if 'correcto3' in globals():
            correcto3.destroy()
        if 'correcto2' in globals():
            correcto2.destroy()


    #colores azul oscuro de fondo(cambia el config.ini)
    def colores_predeterminados():
        global correcto2
        #TABLA PAR
        config.set("TABLA", "tabla_par", '"#CCD0FB"')
        config.set("TABLA", "tabla_impar", '"white"')

        #COLOR FONDO VENTANA PREDETERMINADO
        config.set("COLOR_FONDO_GENERAL", "c_fondo_general", '"#009"')
        config.set("COLOR_FONDO_GENERAL", "c_letra_general", "white")

        config.set("OTRAS_IMAGENES", "escala_grises", "img/colores_clasicos.png")
        config.set("OTRAS_IMAGENES", "escala_azules", "img/colores_predeterminados.png")
        config.set("OTRAS_IMAGENES", "escala_noche", "img/colores_modo_noche.png")

        #COLOR FONDO FORMULARIO PREDETERMINADO
        config.set("COLOR_FONDO", "c_fondo", '"#009"')
        config.set("COLOR_FONDO", "c_frame", '"#020258"')
        config.set("COLOR_FONDO", "c_letra", '"#FFFFFF"')

        #COLOR IMAGEN PREDETERMINADO
        config.set("COLOR_IMAGEN", "c_imagen_configuracion", "img/rueda-dentada1.png")
        config.set("COLOR_IMAGEN", "c_imagen_precio_total", "img/euro3.png")
        config.set("COLOR_IMAGEN", "c_imagen_recargar", "img/recargar.png")
        config.set("COLOR_IMAGEN", "c_imagen_borrar", "img/borrar.png")
        config.set("COLOR_IMAGEN", "c_imagen_compras", "img/carrito-de-compras.png")
        config.set("COLOR_IMAGEN", "c_imagen_abono", "img/abono.png")
        config.set("COLOR_IMAGEN", "c_imagen_usuario", "img/usuario.png")
        config.set("COLOR_IMAGEN", "c_imagen_abono", "img/abono.png")
        config.set("COLOR_IMAGEN", "c_imagen_info", "img/info2.png")
        config.set("COLOR_IMAGEN", "c_imagen_ayuda", "img/auriculares.png")
        config.set("COLOR_IMAGEN", "c_imagen_actualizar", "img/actualizar.png")
        config.set("COLOR_IMAGEN", "c_imagen_buscar", "img/buscar.png")
        config.set("COLOR_IMAGEN", "c_imagen_logo", "img/logo.png")
        config.set("COLOR_IMAGEN", "c_imagen_apariencia", "img/controles.png")
        config.set("COLOR_IMAGEN", "c_imagen_apariencia_tipo", "img/controles_2.png")
        config.set("COLOR_IMAGEN", "c_imagen_tachuela", "img/tachuela.png")
        config.set("COLOR_IMAGEN", "c_imagen_tuerca", "img/tuerca.png")
        config.set("COLOR_IMAGEN", "c_imagen_contacto24", "img/contacto24.png")
        #COLOR FONDO LABEL
        config.set("COLOR_FONDO", "c_fondo_label", 'white')
        config.set("COLOR_FONDO", "c_letra_fondo_label", 'black')
        config.set("COLOR_FONDO", "c_fondo_entry", '"#F9FC8D"')

        #BOTON COLORES AL PASAR MOUSE
        config.set("BOTONES", "c_fondo_botones", '"#0101D7"')
        config.set("BOTONES", "t_borde_botones", "flat")
        config.set("BOTONES", "fondo_boton", '"#022671"') 

        with open("config.ini", "w") as f:
            config.write(f)

        #confirmar cambio apariencia
        correcto2 = Label(ventanaconf, bg=c_frame1, compound = LEFT, fg="#6BF066", font=('', 9,'bold'),  text=" Se ha seleccionado la apariencia \"Predeterminada\". \n Los cambios se aplicarán después de reiniciar la aplicación.")     
        correcto2.place(width=400, height=40, x=70, y=260)
        if 'correcto1' in globals():
            correcto1.destroy()
        if 'correcto3' in globals():
            correcto3.destroy()


    #colores gri y azul fuerte de fondo(cambia el config.ini)
    def colores_modo_noche():
        global correcto3
        #COLOR FORMULARIO modo noche
        config.set("COLOR_IMAGEN", "c_imagen_configuracion", "img/rueda-dentada-azul.png")
        config.set("COLOR_IMAGEN", "c_imagen_ayuda", "img/auriculares-azul.png")
        config.set("COLOR_IMAGEN", "c_imagen_info", "img/info2-azul.png")
        config.set("COLOR_IMAGEN", "c_imagen_precio_total", "img/euro-azul.png")
        config.set("COLOR_IMAGEN", "c_imagen_recargar", "img/recargar-azul.png")
        config.set("COLOR_IMAGEN", "c_imagen_borrar", "img/borrar-azul.png")
        config.set("COLOR_IMAGEN", "c_imagen_compras", "img/compra-azul.png")
        config.set("COLOR_IMAGEN", "c_imagen_abono", "img/abono-azul.png")
        config.set("COLOR_IMAGEN", "c_imagen_usuario", "img/usuario-azul2.png")
        config.set("COLOR_IMAGEN", "c_imagen_actualizar", "img/actualizar-azul.png")
        config.set("COLOR_IMAGEN", "c_imagen_buscar", "img/buscar-azul4.png")
        config.set("COLOR_IMAGEN", "c_imagen_logo", "img/logo-azul.png")
        config.set("COLOR_IMAGEN", "c_imagen_apariencia", "img/controles-azul.png")
        config.set("COLOR_IMAGEN", "c_imagen_apariencia_tipo", "img/controles-azul_2.png")
        config.set("COLOR_IMAGEN", "c_imagen_tachuela", "img/tachuela-azul.png")
        config.set("COLOR_IMAGEN", "c_imagen_tuerca", "img/tuerca-azul.png")
        config.set("COLOR_IMAGEN", "c_imagen_contacto24", "img/contacto-azul24.png")

        #COLOR FONDO VENTANA modo noche
        config.set("COLOR_FONDO_GENERAL", "c_fondo_general", '"#2B2B2B"')
        config.set("COLOR_FONDO_GENERAL", "c_letra_general", "white")

        #COLOR FORMULARIO modo noche
        config.set("COLOR_FONDO", "c_fondo", "#2B2B2B") #VENTANA DE BOTONES
        config.set("COLOR_FONDO", "c_frame", '"#454545"')
        config.set("COLOR_FONDO", "c_letra", '"white"')

        #BOTON COLORES modo noche
        config.set("OTRAS_IMAGENES", "escala_grises", "img/colores_clasicos.png")
        config.set("OTRAS_IMAGENES", "escala_azules", "img/colores_predeterminados.png")
        config.set("OTRAS_IMAGENES", "escala_noche", "img/colores_modo_noche.png")
        #COLOR FONDO LABEL
        config.set("COLOR_FONDO", "c_fondo_label", '"#188BA4"')
        config.set("COLOR_FONDO", "c_fondo_entry", '"#B5DDE5"')
        config.set("COLOR_FONDO", "c_letra_fondo_label", 'white')

        #BOTON COLORES modo noche
        config.set("BOTONES", "c_fondo_botones", '"#858585"')
        config.set("BOTONES", "fondo_boton", '"#6F6F6F"')
        config.set("BOTONES", "t_borde_botones", "flat")

        config.set("TABLA", "tabla_par", '"#ACE0EB"')
        config.set("TABLA", "tabla_impar", '"white"')


        with open("config.ini", "w") as f:
            config.write(f)
        
        #confirmar cambio color apariencia
        correcto3 = Label(ventanaconf, bg=c_frame1, compound = LEFT, fg="#6BF066", font=('', 9,'bold'),  text=" Se ha seleccionado la apariencia \"Modo noche\". \n Los cambios se aplicarán después de reiniciar la aplicación.")     
        correcto3.place(width=400, height=40, x=70, y=260)
        if 'correcto1' in globals():
            correcto1.destroy()
        if 'correcto2' in globals():
            correcto2.destroy()

    #texto "apariencia"
    apariencia = Label(frame1_ventanaconf, bg=c_frame1, image = photoimage35, compound = LEFT, fg="white", font=('', 11,'bold'),  text="  Apariencia")     
    apariencia.place(width=130, height=40, x=10, y=10)

    #BOTON APARIENCIA PREDETERMINADA
    b4 = Button(frame1_ventanaconf, bg = fondo1_boton, font=('', 10,''), text="Predeterminada     ", fg="white", relief=FLAT, command=colores_predeterminados, image = photoimage31, compound = RIGHT)
    b4.place(width=250, height=45, x=193, y=50)

    #BOTON APARIENCIA CLASICA
    b3 = Button(frame1_ventanaconf, bg = fondo1_boton, font=('', 10,''), text="Clásica                 ", fg="white", relief=FLAT, command=colores_clasicos, image = photoimage30, compound = RIGHT)
    b3.place(width=250, height=45, x=193, y=110)

    #BOTON APARIENCIA MODO NOCHE  
    b5 = Button(frame1_ventanaconf, bg = fondo1_boton, font=('', 10,''), text="Modo noche          ", fg="white", relief=FLAT,command=colores_modo_noche, image = photoimage32, compound = RIGHT)
    b5.place(width=250, height=45, x=193, y=170)



    #------------------CONFIGURACION SOMBREADO BOTONES APARIENCIA
    def enterB5(event):
        b5.configure(bg =c_fondo1_botones, fg = c_letra1)
    def leaveB5(event):
        b5.configure(bg = fondo1_boton, fg="white",)

    b5.bind('<Enter>', enterB5)
    b5.bind('<Leave>', leaveB5)
    #-----------------------------------------------------------
    def enterB3(event):
        b3.configure(bg =c_fondo1_botones, fg = c_letra1)

    def leaveB3(event):
        b3.configure(bg = fondo1_boton, fg="white",)

    b3.bind('<Enter>', enterB3)
    b3.bind('<Leave>', leaveB3)
    #-----------------------------------------------------------
    def enterB4(event):
        b4.configure(bg =c_fondo1_botones, fg=c_letra1,)

    def leaveB4(event):
        b4.configure(bg = fondo1_boton, fg="white",)

    b4.bind('<Enter>', enterB4)
    b4.bind('<Leave>', leaveB4)



#----------------------------VENTANA INFO situada en abonos----------------------------------
def informacion_abonos():
    global ventana_info_abonos
    ventana_info_abonos = tk.Toplevel(root)
    ventana_info_abonos.title("Información (abonos)")
    ventana_info_abonos.geometry("800x400")
    ventana_info_abonos.resizable(0,0)
    ventana_info_abonos.iconbitmap("img/info.ico")
    ventana_info_abonos.configure(background=c_fondo1)

    #FRAME VENTANA INFO situada en abonos
    frame1_ventana_info_abonos=ttk.Frame(ventana_info_abonos, width=335, height=165, padding=10 )        
    frame1_ventana_info_abonos.place(x=20, y=20)

    frame2_ventana_info_abonos=ttk.Frame(ventana_info_abonos, width=335, height=165, padding=10 )        
    frame2_ventana_info_abonos.place(x=20, y=200)

    frame3_ventana_info_abonos=ttk.Frame(ventana_info_abonos, width=335, height=165, padding=10 )        
    frame3_ventana_info_abonos.place(x=372, y=20)

    frame4_ventana_info_abonos=ttk.Frame(ventana_info_abonos, width=335, height=165, padding=10 )        
    frame4_ventana_info_abonos.place(x=372, y=200)

    #TEXTO EN FRAME1 DE LA VENTANA INFORMACION DE LOS ABONOS
    informacion_1 = Label(frame1_ventana_info_abonos, bg=c_frame1, compound = LEFT, fg="white", font=('', 11,'bold'),  text="¿Cómo se utiliza la pestaña \"Abonos\"?")     
    informacion_1.place(width=300, height=40, x=0, y=10)

    informacion_1_1 = Label(frame1_ventana_info_abonos, bg=c_frame1, compound = LEFT, fg="white", font=('', 10,''),  text="Primero debemos generar un abono \n en el panel de la izquierda.")     
    informacion_1_1.place(width=300, height=40, x=0, y=40)

    informacion_1_2 = Label(frame1_ventana_info_abonos, bg=c_frame1, compound = LEFT, fg="white", font=('', 10,''),  text="Despúes crearemos un cliente, que \n será asignado al abono creado con anterioridad.")     
    informacion_1_2.place(width=300, height=40, x=0, y=80)

    #TEXTO EN FRAME2 DE LA VENTANA INFORMACION DE LOS ABONOS
    informacion_2 = Label(frame2_ventana_info_abonos, bg=c_frame1, compound = LEFT, fg="white", font=('', 11,'bold'),  text="¿Qué diferencia hay de \"Abono\" \n Individual a Familiar?")     
    informacion_2.place(width=300, height=40, x=0, y=10)

    informacion_2_1 = Label(frame2_ventana_info_abonos, bg=c_frame1, compound = LEFT, fg="white", font=('', 10,''),  text="En el abono Individual tan solo podremos \n asignar un usuario pero en el \n abono Familiar podremos asignar lo que se deseen.")     
    informacion_2_1.place(width=300, height=70, x=0, y=45)

    #TEXTO EN FRAME3 DE LA VENTANA INFORMACION DE LOS ABONOS
    informacion_3 = Label(frame3_ventana_info_abonos, bg=c_frame1, compound = LEFT, fg="white", font=('', 11,'bold'),  text="¿Cuál es el precio de los abonos?")     
    informacion_3.place(width=300, height=40, x=0, y=10)

    informacion_3_1 = Label(frame3_ventana_info_abonos, bg=c_frame1, compound = LEFT, fg="white", font=('', 10,''),  text="El precio de los abonos es \n Individual: 33 € \n Familiar: 80 €")     
    informacion_3_1.place(width=300, height=70, x=0, y=40)

    #TEXTO EN FRAME4 DE LA VENTANA INFORMACION DE LOS ABONOS
    informacion_4 = Label(frame3_ventana_info_abonos, bg=c_frame1, compound = LEFT, fg="white", font=('', 11,'bold'),  text="¿Cuál es el precio de los \"Abonos\"?")     
    informacion_4.place(width=300, height=40, x=0, y=10)




#----------------------------VENTANA INFO situada en entradas----------------------------------
def informacion_entradas():
    global ventana_info_entradas
    ventana_info_entradas = tk.Toplevel(root)
    ventana_info_entradas.title("Información (entradas)")
    ventana_info_entradas.geometry("800x400")
    ventana_info_entradas.resizable(0,0)
    ventana_info_entradas.iconbitmap("img/info.ico")
    ventana_info_entradas.configure(background=c_fondo1)

    #VENTANA DE FRAME entradas
    frame1_ventana_info_entradas=ttk.Frame(ventana_info_entradas, width=335, height=165, padding=10 )        
    frame1_ventana_info_entradas.place(x=20, y=20)

    frame2_ventana_info_entradas=ttk.Frame(ventana_info_entradas, width=335, height=165, padding=10 )        
    frame2_ventana_info_entradas.place(x=20, y=200)

    frame3_ventana_info_entradas=ttk.Frame(ventana_info_entradas, width=335, height=165, padding=10 )        
    frame3_ventana_info_entradas.place(x=372, y=20)

    frame4_ventana_info_entradas=ttk.Frame(ventana_info_entradas, width=335, height=165, padding=10 )        
    frame4_ventana_info_entradas.place(x=372, y=200)

    #TEXTO EN FRAME1 DE LA VENTANA INFORMACION DE LAS ENTRADAS
    informacion_1 = Label(frame1_ventana_info_entradas, bg=c_frame1, compound = LEFT, fg="white", font=('', 11,'bold'),  text="¿Cuál es el precio de las entradas?")     
    informacion_1.place(width=300, height=40, x=0, y=10)

    informacion_1_1 = Label(frame1_ventana_info_entradas, bg=c_frame1, compound = LEFT, fg="white", font=('', 10,''),  text="Entradas Adulto: "+precio1_adulto+" €. \n \nEntradas Infantil: "+precio1_infantil+" €")     
    informacion_1_1.place(width=300, height=70, x=0, y=45)

    #TEXTO EN FRAME2 DE LA VENTANA INFORMACION DE LAS ENTRADAS
    informacion_2 = Label(frame2_ventana_info_entradas, bg=c_frame1, compound = LEFT, fg="white", font=('', 11,'bold'),  text="¿Para qué sirve la casilla \"Efectivo\"?")     
    informacion_2.place(width=300, height=40, x=0, y=10)

    informacion_2_1 = Label(frame2_ventana_info_entradas, bg=c_frame1, compound = LEFT, fg="white", font=('', 10,''),  text="Ahí debemos ingresar el dinero que nos da \n el cliente para que el programa \n nos calcule las vueltas.")     
    informacion_2_1.place(width=300, height=70, x=0, y=45)

    #TEXTO EN FRAME3 DE LA VENTANA INFORMACION DE LAS ENTRADAS
    informacion_33 = Label(frame3_ventana_info_entradas, bg=c_frame1, compound = LEFT, fg="white", font=('', 11,'bold'),  text="¿Para qué sirve \"Control del aforo\" \n en Configuración?")     
    informacion_33.place(width=300, height=60, x=0, y=10)

    informacion_3_1 = Label(frame3_ventana_info_entradas, bg=c_frame1, compound = LEFT, fg="white", font=('', 10,''),  text="Este apartado nos creará una alerta cuando \n  se vaya llegando al límite establecido \n para saber los usuarios que \n hay dentro.")     
    informacion_3_1.place(width=300, height=70, x=0, y=60)

    #TEXTO EN FRAME4 DE LA VENTANA INFORMACION DE LAS ENTRADAS
    informacion_4 = Label(frame4_ventana_info_entradas, bg=c_frame1, compound = LEFT, fg="white", font=('', 11,'bold'),  text="")     
    informacion_4.place(width=300, height=40, x=0, y=10)



#----------------------------VENTANA CONTACTO situada en todas las pestañas----------------------------------
def contacto():
    global ventana_contacto
    ventana_contacto = tk.Toplevel(root)
    ventana_contacto.title("Contacto")
    ventana_contacto.geometry("441x256")
    ventana_contacto.resizable(0,0)
    ventana_contacto.iconbitmap("img/contacto1.ico")
    ventana_contacto.configure(background=c_fondo1)

    #VENTANA DE FRAME ABONOS

    frame1_ventana_contacto=ttk.Frame(ventana_contacto, width=400, height=220, padding=10 )        
    frame1_ventana_contacto.place(x=20, y=20)


    #TEXTO EN FRAME1 DE LA VENTANA INFORMACION DE LOS ABONOS
    contacto_1 = Label(frame1_ventana_contacto, bg=c_frame1, compound = LEFT, fg="white", image = photoimage12, font=('', 11,'bold'),  text="  Contacto")     
    contacto_1.place(width=150, height=30, x=0, y=20)

    contacto_2 = Label(frame1_ventana_contacto, bg=fondo1_boton, compound = LEFT, fg="white", image = photoimage71, font=('', 10,''),  text="  675635585                            ")     
    contacto_2.place(width=220, height=40, x=50, y=80)

    contacto_3 = Label(frame1_ventana_contacto, bg=fondo1_boton, compound = LEFT, fg="white", image = photoimage72, font=('', 10,''),  text="  victorcarrasco702@gmail.com")     
    contacto_3.place(width=220, height=40, x=50, y=130)



#----------------------------VENTANA CONFIGURACION situada en todas las pestañas----------------------------------
def configuracion():
    global ventana_configuracion
    ventana_configuracion = tk.Toplevel(root)
    ventana_configuracion.title("Configuracion")
    ventana_configuracion.geometry("1100x522")
    ventana_configuracion.resizable(0,0)
    ventana_configuracion.iconbitmap("img/configuracion.ico")
    ventana_configuracion.configure(background=c_fondo1)

    #VENTANA DE FRAME ABONOS
    frame1_ventana_configuracion=ttk.Frame(ventana_configuracion, width=1050, height=480, padding=10 )        
    frame1_ventana_configuracion.place(x=20, y=20)

    frame2_dentro_frame1=ttk.Frame(frame1_ventana_configuracion,  width=400, height=220, padding=10 )        
    frame2_dentro_frame1.place(x=50, y=30)

    frame3_dentro_frame1=ttk.Frame(frame1_ventana_configuracion,  width=400, height=320, padding=10 )        
    frame3_dentro_frame1.place(x=50, y=250)

    frame4_dentro_frame1=ttk.Frame(frame1_ventana_configuracion,  width=400, height=320, padding=10 )        
    frame4_dentro_frame1.place(x=450, y=30)

    frame5_dentro_frame1=ttk.Frame(frame1_ventana_configuracion,  width=400, height=320, padding=10 )        
    frame5_dentro_frame1.place(x=450, y=250)



    #TEXTO EN FRAME1 DE LA VENTANA INFORMACION DE LOS ABONOS
    configuracion_1 = Label(frame1_ventana_configuracion, bg=c_frame1, compound = LEFT, fg="white", font=('', 11,'bold'), image = photoimage70, text="  Configuracion")     
    configuracion_1.place(width=150, height=40, x=0, y=0)

    configuracion_2 = Label(frame2_dentro_frame1, bg=fondo1_boton, compound = LEFT, fg="white", font=('', 10,'bold'),  text="Control del aforo máximo permitido                     ")     
    configuracion_2.place(width=350, height=30, x=30, y=20)

    configuracion_2_1 = Label(frame2_dentro_frame1, bg=fondo1_boton, compound = LEFT, fg="white", font=('', 10,''),  text="     El aforo máximo actual es de:" )     
    configuracion_2_1.place(width=350, height=30, x=30, y=50)
    configuracion_2_2 = Label(frame2_dentro_frame1, bg=fondo1_boton, compound = LEFT, fg="white", font=('', 10,''),  text=aforo1_maximo )     
    configuracion_2_2.place(width=30, height=30, x=310, y=50)


    #RECUADRO FIJAR AFORO
    configuracion_2_3 = Label(frame2_dentro_frame1, bg=fondo1_boton, compound = LEFT, fg="white", font=('', 10,''),  text="                   Fijar un nuevo aforo: " )     
    configuracion_2_3.place(width=350, height=50, x=30, y=70)
    valor35 = StringVar()
    configuracion_2_44 = Entry(frame2_dentro_frame1, width=5, font=('', 10,'bold'), textvariable=valor35)
    configuracion_2_44.place( x=310, y=85)

    def fijar():

        try:
            nuevo_aforo = int(configuracion_2_44.get())
            print(nuevo_aforo)

            config.set("CONFIGURACION", "aforo_maximo", str(nuevo_aforo))
            with open("config.ini", "w") as f:
                config.write(f)
            correcto4 = Label(frame2_dentro_frame1, bg=fondo1_boton, compound = LEFT, fg="#6BF066", font=('', 10,''),  text="Cambios guardados. \n los cambios se aplicarán al reiniciar la aplicación." )     
            correcto4.place(width=350, height=30, x=30, y=168)
        
        except ValueError:
            messagebox.showinfo('Aforo máximo', 'No se pudo fijar un nuevo aforo máximo, por favor, revise los datos introducidos.', parent=frame4_dentro_frame1)
            
        
    #BOTON APARIENCIA MODO NOCHE 
    fijar1 = Label(frame2_dentro_frame1, bg=fondo1_boton, compound = LEFT, fg="white", font=('', 10,''),  text="\n \n" )     
    fijar1.place(width=350, height=150, x=30, y=120)
    b35 = Button(frame2_dentro_frame1, bg = c_frame1, font=('', 10,''), text="  Fijar nuevo aforo", image = photoimage37, fg="white", relief=FLAT,command=fijar, compound = LEFT)
    b35.place(width=150, height=40, x=200, y=120)

    def enterB35(event):
        b35.configure(bg =c_fondo1_botones, fg = c_letra1)

    def leaveB35(event):
        b35.configure(bg = c_frame1, fg = c_letra1)

    b35.bind('<Enter>', enterB35)
    b35.bind('<Leave>', leaveB35)



    #-----------------NUEVA PESTAÑA gestionar CLIENTES DENTRO DE CONFIGURACION------------------------------
    def conf_gestionar_clientes():
        global ventana_gestionar_clientes
        ventana_gestionar_clientes = tk.Toplevel(ventana_configuracion)
        ventana_gestionar_clientes.title("Configuracion")
        ventana_gestionar_clientes.geometry("470x315")
        ventana_gestionar_clientes.resizable(0,0)
        ventana_gestionar_clientes.iconbitmap("img/configuracion.ico")
        ventana_gestionar_clientes.configure(background=c_fondo1)

        #-------------------------------------FUNCIONES VENTANA GESTIONAR USUARIOS--------------------
        def borrar_clientes():

            if valor36.get() != "":
                if messagebox.askyesno('Eliminar usuario', '¿Está seguro de eliminar el usuario?', parent=frame1_ventana_gestionar_clientes):
                    codigo_cliente1_pre = str(valor36.get())                            
                    codigo_cliente1 = codigo_cliente1_pre.strip("(" ")" ",")
                    cur.execute("DELETE FROM clientes WHERE codigo_clientes=?",(codigo_cliente1,))
                    db.commit()
                    borrar_campos()
                    global correcto8
                    hora = datetime.now()
                    #Texto en verde que nos confirma la creacion del abono con la hora.
                    correcto8 = Label(frame1_ventana_gestionar_clientes, bg=c_frame1, compound = LEFT, fg="#6BF066", font=('', 9,'bold'),  text="Se ha borrado el usuario " +codigo_cliente1 + " a las " +str(hora.strftime("%H:%M:%S")))   
                    correcto8.place(width=350, height=40, x=30, y=190)

                else:
                    borrar_campos()
                    messagebox.showinfo('Eliminar usuario', 'No se eliminó el usuario', parent=frame1_ventana_gestionar_clientes)
            else:
                messagebox.showinfo('Eliminar usuario', 'Campos vacíos.', parent=frame1_ventana_gestionar_clientes)


                
        def borrar_campos():

            if 'correcto8' in globals():
                correcto8.destroy()
            
            valor36.set('')


        #----------------------------VENTANA DE FRAME GESTIONAR USUARIOS-----------------------
        frame1_ventana_gestionar_clientes=ttk.Frame(ventana_gestionar_clientes, width=430, height=275, padding=10 )        
        frame1_ventana_gestionar_clientes.place(x=20, y=20)

        gestionar_clientes1 = Label(frame1_ventana_gestionar_clientes, bg=c_frame1, compound = LEFT, fg="white", font=('', 11,'bold'),  text="Gestionar usuarios                         ")     
        gestionar_clientes1.place(width=250, height=40, x=20, y=0)

        gestionar_clientes2 = Label(frame1_ventana_gestionar_clientes, bg=fondo1_boton, compound = LEFT, fg="white", font=('', 10,'bold'),  text="Borrar usuarios                                                   ")     
        gestionar_clientes2.place(width=350, height=50, x=30, y=50)

        gestionar_clientes3 = Label(frame1_ventana_gestionar_clientes, bg=fondo1_boton, compound = LEFT, fg="white", font=('', 10,''),  text="                   Código de usuario: " )     
        gestionar_clientes3.place(width=350, height=50, x=30, y=80)
        valor36 = StringVar()
        gestionar_clientes4 = Entry(frame1_ventana_gestionar_clientes, width=5, font=('', 10,'bold'), textvariable=valor36)
        gestionar_clientes4.place( x=310, y=95)


        b36 = Button(frame1_ventana_gestionar_clientes, bg = fondo1_boton, font=('', 10,''), image = photoimage6, text="  Borrar usuario", fg="white", relief=FLAT,command=borrar_clientes, compound = LEFT)
        b36.place(width=150, height=40, x=230, y=135)

        def enterB36(event):
            b36.configure(bg =c_fondo1_botones, fg = c_letra1)

        def leaveB36(event):
            b36.configure(bg = fondo1_boton, fg = c_letra1)

        b36.bind('<Enter>', enterB36)
        b36.bind('<Leave>', leaveB36)

    #------------------------------------------------------------------------------------------------------

    #-----------------NUEVA PESTAÑA gestionar abonos DENTRO DE CONFIGURACION------------------------------
    def conf_gestionar_abonos():
        global ventana_gestionar_abonos
        ventana_gestionar_abonos = tk.Toplevel(ventana_configuracion)
        ventana_gestionar_abonos.title("Configuracion")
        ventana_gestionar_abonos.geometry("470x315")
        ventana_gestionar_abonos.resizable(0,0)
        ventana_gestionar_abonos.iconbitmap("img/configuracion.ico")
        ventana_gestionar_abonos.configure(background=c_fondo1)

        #-------------------------------------FUNCIONES VENTANA GESTIONAR ABONOS--------------------
        def borrar_abonos():

            if valor37.get() != "":
                if messagebox.askyesno('Eliminar abono', '¿Está seguro de eliminar el abono?', parent=frame1_ventana_gestionar_abonos):
                    codigo_abonos1_pre = str(valor37.get())                            
                    codigo_abonos1 = codigo_abonos1_pre.strip("(" ")" ",")
                    cur.execute("DELETE FROM abonos WHERE codigo_abonos=?",(codigo_abonos1,))
                    db.commit()
                    borrar_campos1()
                    global correcto11
                    hora = datetime.now()
                    #Texto en verde que nos confirma la creacion del abono con la hora.
                    correcto11 = Label(frame1_ventana_gestionar_abonos, bg=c_frame1, compound = LEFT, fg="#6BF066", font=('', 9,'bold'),  text="Se ha borrado el abono " +codigo_abonos1 + " a las " +str(hora.strftime("%H:%M:%S")) )   
                    correcto11.place(width=350, height=40, x=30, y=190)

                else:
                    borrar_campos1()
                    messagebox.showinfo('Eliminar abonos', 'No se eliminó el abono', parent=frame1_ventana_gestionar_abonos)
            else:
                messagebox.showinfo('Eliminar abonos', 'Campos vacíos.', parent=frame1_ventana_gestionar_abonos)

                
        def borrar_campos1():

            if 'correcto11' in globals():
                correcto11.destroy()            
            valor37.set('')


        #----------------------------VENTANA DE FRAME GESTIONAR ABONOS-----------------------
        frame1_ventana_gestionar_abonos=ttk.Frame(ventana_gestionar_abonos, width=430, height=275, padding=10 )        
        frame1_ventana_gestionar_abonos.place(x=20, y=20)

        gestionar_abonos1 = Label(frame1_ventana_gestionar_abonos, bg=c_frame1, compound = LEFT, fg="white", font=('', 11,'bold'),  text="Gestionar abonos                         ")     
        gestionar_abonos1.place(width=250, height=40, x=20, y=0)

        gestionar_abonos2 = Label(frame1_ventana_gestionar_abonos, bg=fondo1_boton, compound = LEFT, fg="white", font=('', 10,'bold'),  text="Borrar abonos                                                   ")     
        gestionar_abonos2.place(width=350, height=50, x=30, y=50)

        gestionar_abonos3 = Label(frame1_ventana_gestionar_abonos, bg=fondo1_boton, compound = LEFT, fg="white", font=('', 10,''),  text="                   Código de abono: " )     
        gestionar_abonos3.place(width=350, height=50, x=30, y=80)
        valor37 = StringVar()
        gestionar_abonos4 = Entry(frame1_ventana_gestionar_abonos, width=5, font=('', 10,'bold'), textvariable=valor37)
        gestionar_abonos4.place( x=310, y=95)


        b38 = Button(frame1_ventana_gestionar_abonos, bg = fondo1_boton, font=('', 10,''), image = photoimage6, text="  Borrar abono", fg="white", relief=FLAT,command=borrar_abonos, compound = LEFT)
        b38.place(width=150, height=40, x=230, y=135)

        def enterB38(event):
            b38.configure(bg =c_fondo1_botones, fg = c_letra1)

        def leaveB38(event):
            b38.configure(bg = fondo1_boton, fg = c_letra1)

        b38.bind('<Enter>', enterB38)
        b38.bind('<Leave>', leaveB38)

#---------------------------------------------ETIQUETAS Y BOTONES FRAME 3-------------------------------
    configuracion_3 = Label(frame3_dentro_frame1, bg=fondo1_boton, compound = LEFT, fg="white", font=('', 10,'bold'),  text="Base de datos                                                ")     
    configuracion_3.place(width=350, height=30, x=30, y=20)

    esp = Label(frame3_dentro_frame1, bg=fondo1_boton, compound = LEFT, fg="white", font=('', 10,''),  text="")     
    esp.place(width=350, height=150, x=30, y=40)

    esp1 = Label(frame3_dentro_frame1, bg=fondo1_boton, compound = LEFT, fg="white", font=('', 10,''),  text="")     
    esp1.place(width=350, height=60, x=30, y=115)

    b36 = Button(frame3_dentro_frame1, bg = c_frame1, font=('', 10,''), text="  Gestionar usuarios", fg="white", relief=FLAT,command=conf_gestionar_clientes, image = photoimage10,  compound = LEFT)
    b36.place(width=150, height=40, x=200, y=65)
    
    b37 = Button(frame3_dentro_frame1, bg = c_frame1, font=('', 10,''), text="  Gestionar abonos", fg="white", relief=FLAT,command=conf_gestionar_abonos, image = photoimage7,  compound = LEFT)
    b37.place(width=150, height=40, x=200, y=115)


#---------------------------------------------ETIQUETAS Y BOTONES FRAME 4-------------------------------
    def ultimas_entradas():
        if messagebox.askyesno('Eliminar entradas', '¿Está seguro de eliminar las últimas entradas?', parent=frame4_dentro_frame1):
            cur.execute("delete from entradas where codigo_entradas IN (SELECT codigo_entradas from entradas order by codigo_entradas asc limit 2)")
            db.commit()
            borrar11()
            entradas.borrar_todo()

            
            #Texto en verde que nos confirma la creacion del abono con la hora.
            global correcto12
            global incorrecto
            correcto12 = Label(frame4_dentro_frame1, bg=fondo1_boton, compound = LEFT, fg="#6BF066", font=('', 9,'bold'),  text="Se han cancelado las últimas entradas vendidas.")   
            correcto12.place(width=350, height=30, x=30, y=175)
            incorrecto = Label(f1, bg=c_fondo1, compound = LEFT, fg="#E93E3E", font=('', 9,'bold'),  text="Se ha cancelado la venta ANTERIOR de entradas. ")   
            incorrecto.place(width=300, height=35, x=513, y=455)             
        else:
            messagebox.showinfo('Eliminar entradas', 'No se eliminaron las entradas', parent=frame4_dentro_frame1)
    def borrar11():

        if 'correcto12' in globals():
            correcto12.destroy()


    configuracion_3 = Label(frame4_dentro_frame1, bg=fondo1_boton, compound = LEFT, fg="white", font=('', 10,'bold'),  text="Base de datos                                                ")     
    configuracion_3.place(width=350, height=30, x=30, y=20)

    esp = Label(frame4_dentro_frame1, bg=fondo1_boton, compound = LEFT, fg="white", font=('', 10,''),  text="")     
    esp.place(width=350, height=160, x=30, y=50)

    b40 = Button(frame4_dentro_frame1, bg ='#C96565', font=('', 10,''), text="Cancelar la última venta de entradas", fg="white", relief=FLAT,command=ultimas_entradas, compound = LEFT)
    b40.place(width=350, height=50, x=30, y=60)

    configuracion_2_2_5 = Label(frame4_dentro_frame1, bg=fondo1_boton, compound = LEFT, fg="white", font=('', 10,''),  text="Solo se eliminarán las entradas correspondientes a \n la última venta. Si repetimos el proceso, \nse eliminarán las anteriores.")     
    configuracion_2_2_5.place(width=350, height=50, x=30, y=115)

    #TEXTO EN FRAME5 DE LA VENTANA FIJAR PRECIO DE ENTRADAS
    esp = Label(frame5_dentro_frame1, bg=fondo1_boton, compound = LEFT, fg="white", font=('', 10,''),  text="")     
    esp.place(width=350, height=160, x=30, y=30)

    configuracion_2_2_2 = Label(frame5_dentro_frame1, bg=fondo1_boton, compound = LEFT, fg="white", font=('', 10,'bold'),  text="Nuevos precios de las entradas                             ")     
    configuracion_2_2_2.place(width=350, height=30, x=30, y=20)

    #RECUADRO FIJAR AFORO
    configuracion_2_3 = Label(frame5_dentro_frame1, bg=fondo1_boton, compound = LEFT, fg="white", font=('', 10,''),  text="          Nuevo precio adulto: " )     
    configuracion_2_3.place(width=350, height=40, x=30, y=50)
    valor39 = StringVar()

    configuracion_2_4 = Entry(frame5_dentro_frame1, width=5, font=('', 10,'bold'), textvariable=valor39)
    configuracion_2_4.place( x=310, y=60)




    configuracion_2_5 = Label(frame5_dentro_frame1, bg=fondo1_boton, compound = LEFT, fg="white", font=('', 10,''),  text="          Nuevo precio infantil: " )     
    configuracion_2_5.place(width=350, height=50, x=30, y=80)
    
    valor40 = StringVar()
    configuracion_2_6 = Entry(frame5_dentro_frame1, width=5, font=('', 10,'bold'), textvariable=valor40)
    configuracion_2_6.place( x=310, y=95)

    def precio_entradas1():
        try:
            precio_adulto = float(configuracion_2_4.get())
            precio_infantil = float(configuracion_2_6.get())
            config.set("CONFIGURACION", "precio_adulto", str(precio_adulto))
            config.set("CONFIGURACION", "precio_infantil", str(precio_infantil))
            with open("config.ini", "w") as f:
                config.write(f)
        
            correcto4 = Label(frame5_dentro_frame1, bg=fondo1_boton, compound = LEFT, fg="#6BF066", font=('', 10,'bold'),  text="Cambios guardados. \n debe reiniciar." )     
            correcto4.place(width=150, height=30, x=40, y=130)
        except ValueError:
            messagebox.showinfo('Error', 'No se pudo fijar un nuevo precio. Por favor, revise los datos introducidos.', parent=frame5_dentro_frame1)

    #BOTON APARIENCIA MODO NOCHE 
    #precioentradas = Label(frame5_dentro_frame1, bg=fondo1_boton, compound = LEFT, fg="white", font=('', 10,''),  text="\n \n" )     
    #precioentradas.place(width=350, height=150, x=30, y=120)
    b41 = Button(frame5_dentro_frame1, bg = c_frame1, font=('', 10,''), text="  Fijar precios", image = photoimage37, fg="white", relief=FLAT,command=precio_entradas1, compound = LEFT)
    b41.place(width=150, height=40, x=200, y=125)


    def enterB36(event):
        b36.configure(bg =c_fondo1_botones, fg = c_letra1)

    def leaveB36(event):
        b36.configure(bg = c_frame1, fg = c_letra1)

    b36.bind('<Enter>', enterB36)
    b36.bind('<Leave>', leaveB36)


    def enterB37(event):
        b37.configure(bg =c_fondo1_botones, fg = c_letra1)

    def leaveB37(event):
        b37.configure(bg = c_frame1, fg = c_letra1)

    b37.bind('<Enter>', enterB37)
    b37.bind('<Leave>', leaveB37)

    def enterB40(event):
        b40.configure(bg ='#F48686', fg = c_letra1)

    def leaveB40(event):
        b40.configure(bg = '#C96565', fg = c_letra1)

    b40.bind('<Enter>', enterB40)
    b40.bind('<Leave>', leaveB40)

    def enterB41(event):
        b41.configure(bg =c_fondo1_botones, fg = c_letra1)

    def leaveB41(event):
        b41.configure(bg = c_frame1, fg = c_letra1)

    b41.bind('<Enter>', enterB41)
    b41.bind('<Leave>', leaveB41)
    
#------------------------------IMAGEN DE BOTONES DENTRO DE LAS PESTAÑAS HIJAS----------------------------------
photo7 = PhotoImage(file = c_imagen1_abono)  
photoimage7 = photo7.subsample(1, 1) 

photo10 = PhotoImage(file = c_imagen1_usuario)  
photoimage10 = photo10.subsample(1, 1) 

photo30 = PhotoImage(file = c_imagen1_gris)  
photoimage30 = photo30.subsample(1, 1)

photo31 = PhotoImage(file = c_imagen1_azules)  
photoimage31 = photo31.subsample(1, 1)

photo32 = PhotoImage(file = c_imagen1_noche)  
photoimage32 = photo32.subsample(1, 1)

photo35 = PhotoImage(file = c_imagen1_apariencia2)  
photoimage35 = photo35.subsample(1, 1)

photo36 = PhotoImage(file = c_imagen1_borrar_cliente)  
photoimage36 = photo36.subsample(1, 1)

photo37 = PhotoImage(file = c_imagen1_tachuela)  
photoimage37 = photo37.subsample(1, 1)

photo6 = PhotoImage(file = c_imagen1_borrar)  
photoimage6 = photo6.subsample(1, 1)

photo70 = PhotoImage(file = c_imagen1_tuerca)  
photoimage70 = photo70.subsample(1, 1)

photo12 = PhotoImage(file = c_imagen1_contacto24)  
photoimage12 = photo12.subsample(1, 1) 

photo71 = PhotoImage(file = r"img/whatsapp.png")  
photoimage71 = photo71.subsample(1, 1)

photo72 = PhotoImage(file = r"img/gmail.png")  
photoimage72 = photo72.subsample(1, 1)