
#=====================================LIBRERÍAS======================================================
import configparser
from datetime import *
#=====================================LLAMAR ARCHIVO DE CONFIGURACION================================
config = configparser.ConfigParser()
config.read('config.ini')

#=====================================VARIABLES GENERALES============================================

#------------------------------ "OTRAS" VARIABLES-------------------------------
euro = ' €'
abonos_creados = 0
numero_total_entradas = 0
_valor = 0
_valor1 = 0
_valor2 = 0
_valor3 = 0
valor_total = 0
_valor_infantil = 0
correcto = 5
correcto = 6
contador_control_abonos = 0
resetear_entradas = 0

margen = 20

#------------------------------ VARIABLES CONFIG.INI-------------------------------

#--------COLOR DE FONDO------------------------------
c_fondo1_pre = config.get("COLOR_FONDO", "c_fondo")
c_fondo1 = c_fondo1_pre.strip('""') #Limpia  las comillas

c_frame_pre = config.get("COLOR_FONDO", "c_frame")
c_frame1= c_frame_pre.strip('""') #Limpia  las comillas

c_letra_pre = config.get("COLOR_FONDO", "c_letra")
c_letra1= c_letra_pre.strip('""') #Limpia  las comillas

c_fondo_label_pre = config.get("COLOR_FONDO", "c_fondo_label")
c_fondo1_label= c_fondo_label_pre.strip('""') #Limpia  las comillas

c_letra_fondo_label_pre = config.get("COLOR_FONDO", "c_letra_fondo_label")
c_letra_fondo1_label= c_letra_fondo_label_pre.strip('""') #Limpia  las comillas

c_fondo_entry_pre = config.get("COLOR_FONDO", "c_fondo_entry")
c_fondo1_entry= c_fondo_entry_pre.strip('""') #Limpia  las comillas


#--------COLOR DE FONDO GENERAL----------------------
c_letra_pre_general = config.get("COLOR_FONDO_GENERAL", "c_letra_general")
c_letra1_general= c_letra_pre_general.strip('""') #Limpia  las comillas

c_fondo_pre_general = config.get("COLOR_FONDO_GENERAL", "c_fondo_general")
c_fondo1_general= c_fondo_pre_general.strip('""') #Limpia  las comillas


#--------CONFIGURACION DE LAS IMAGENES----------------
c_imagen_pre = config.get("COLOR_IMAGEN", "c_imagen_configuracion")
c_imagen1= c_imagen_pre.strip('""') #Limpia  las comillas

c_imagen_precio_total_pre = config.get("COLOR_IMAGEN", "c_imagen_precio_total")
c_imagen1_precio_total= c_imagen_precio_total_pre.strip('""') #Limpia  las comillas

c_imagen_recargar_pre = config.get("COLOR_IMAGEN", "c_imagen_recargar")
c_imagen1_recargar= c_imagen_recargar_pre.strip('""') #Limpia  las comillas

c_imagen_borrar_pre = config.get("COLOR_IMAGEN", "c_imagen_borrar")
c_imagen1_borrar= c_imagen_borrar_pre.strip('""') #Limpia  las comillas

c_imagen_compras_pre = config.get("COLOR_IMAGEN", "c_imagen_compras")
c_imagen1_compras= c_imagen_compras_pre.strip('""') #Limpia  las comillas

c_imagen_abono_pre = config.get("COLOR_IMAGEN", "c_imagen_abono")
c_imagen1_abono= c_imagen_abono_pre.strip('""') #Limpia  las comillas

c_imagen_usuario_pre = config.get("COLOR_IMAGEN", "c_imagen_usuario")
c_imagen1_usuario= c_imagen_usuario_pre.strip('""') #Limpia  las comillas

c_imagen_info_pre = config.get("COLOR_IMAGEN", "c_imagen_info")
c_imagen1_info= c_imagen_info_pre.strip('""') #Limpia  las comillas

c_imagen_ayuda_pre = config.get("COLOR_IMAGEN", "c_imagen_ayuda")
c_imagen1_ayuda= c_imagen_ayuda_pre.strip('""') #Limpia  las comillas

c_imagen_actualizar_pre = config.get("COLOR_IMAGEN", "c_imagen_actualizar")
c_imagen1_actualizar= c_imagen_actualizar_pre.strip('""') #Limpia  las comillas

c_imagen_buscar_pre = config.get("COLOR_IMAGEN", "c_imagen_buscar")
c_imagen1_buscar= c_imagen_buscar_pre.strip('""') #Limpia  las comillas

c_imagen_logo_pre = config.get("COLOR_IMAGEN", "c_imagen_logo")
c_imagen1_logo= c_imagen_logo_pre.strip('""') #Limpia  las comillas

c_imagen_apariencia_pre = config.get("COLOR_IMAGEN", "c_imagen_apariencia")
c_imagen1_apariencia= c_imagen_apariencia_pre.strip('""') #Limpia  las comillas

c_imagen_apariencia2_pre = config.get("COLOR_IMAGEN", "c_imagen_apariencia_tipo")
c_imagen1_apariencia2= c_imagen_apariencia2_pre.strip('""') #Limpia  las comillas

c_imagen_borrar_cliente_pre = config.get("COLOR_IMAGEN", "c_imagen_borrar_cliente")
c_imagen1_borrar_cliente= c_imagen_borrar_cliente_pre.strip('""') #Limpia  las comillas

c_imagen_tachuela_pre = config.get("COLOR_IMAGEN", "c_imagen_tachuela")
c_imagen1_tachuela= c_imagen_tachuela_pre.strip('""') #Limpia  las comillas

c_imagen_tuerca_pre = config.get("COLOR_IMAGEN", "c_imagen_tuerca")
c_imagen1_tuerca= c_imagen_tuerca_pre.strip('""') #Limpia  las comillas

c_imagen_contacto24_pre = config.get("COLOR_IMAGEN", "c_imagen_contacto24")
c_imagen1_contacto24= c_imagen_contacto24_pre.strip('""') #Limpia  las comillas

#--------CONFIGURACION IMAGENES SELECCION DE APARIENCIA----------------
c_imagen_gris_pre = config.get("OTRAS_IMAGENES", "escala_grises")
c_imagen1_gris= c_imagen_gris_pre.strip('""') #Limpia  las comillas

c_imagen_azules_pre = config.get("OTRAS_IMAGENES", "escala_azules")
c_imagen1_azules= c_imagen_azules_pre.strip('""') #Limpia  las comillas

c_imagen_noche_pre = config.get("OTRAS_IMAGENES", "escala_noche")
c_imagen1_noche= c_imagen_noche_pre.strip('""') #Limpia  las comillas


#--------CONFIGURACION TABLA----------------
c_imagen_tabla_pre = config.get("TABLA", "tabla_par")
c_imagen1_tabla= c_imagen_tabla_pre.strip('""') #Limpia  las comillas

c_imagen_tabla_impar_pre = config.get("TABLA", "tabla_impar")
c_imagen1_tabla_impar= c_imagen_tabla_impar_pre.strip('""') #Limpia  las comillas


#--------CONFIGURACION BOTONES----------------
c_fondo_botones_pre = config.get("BOTONES", "c_fondo_botones")
c_fondo1_botones= c_fondo_botones_pre.strip('""') #Limpia  las comillas

t_borde_botones_pre = config.get("BOTONES", "t_borde_botones")
t_borde1_botones= t_borde_botones_pre.strip('""') #Limpia  las comillas

fondo_boton_pre = config.get("BOTONES", "fondo_boton")
fondo1_boton= fondo_boton_pre.strip('""') #Limpia  las comillas


#--------CONFIGURACION ----------------

fecha_guardada_pre = config.get("CONFIGURACION", "fecha_guardada")
fecha1_guardada= fecha_guardada_pre.strip('""') #Limpia  las comillas

casi_aforo_maximo_pre = config.get("CONFIGURACION", "casi_aforo_maximo")
casi_aforo1_maximo= casi_aforo_maximo_pre.strip('""') #Limpia  las comillas

aforo_maximo_pre = config.get("CONFIGURACION", "aforo_maximo")
aforo1_maximo= aforo_maximo_pre.strip('""') #Limpia  las comillas

precio_adulto_pre = config.get("CONFIGURACION", "precio_adulto")
precio1_adulto= precio_adulto_pre.strip('""') #Limpia  las comillas

precio_infantil_pre = config.get("CONFIGURACION", "precio_infantil")
precio1_infantil= precio_infantil_pre.strip('""') #Limpia  las comillas