
#===================================== LIBRERÍAS ========================================================

import sqlite3 as sql

#===================================== CONEXION BASE DE DATOS============================================

db=sql.connect("database.db")
cur=db.cursor()

#creamos la tabla entradas si no existe
cur.execute("CREATE TABLE  IF NOT EXISTS entradas (codigo_entradas INTEGER PRIMARY KEY AUTOINCREMENT, numero_entradas INT NOT NULL, fecha_entradas DATE, precio_entradas INT NOT NULL, tipo_entradas TEXT NOT NULL )") 
db.commit()

#creamos la tabla abonos si no existe
cur.execute("CREATE TABLE  IF NOT EXISTS abonos (codigo_abonos INTEGER PRIMARY KEY AUTOINCREMENT, tipo_abonos TEXT NOT NULL, fecha_abonos DATE, precio_abonos INT NOT NULL )") 
db.commit()

#creamos la tabla clientes si no existe
cur.execute("CREATE TABLE  IF NOT EXISTS clientes (codigo_clientes INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT NOT NULL, apellidos TEXT NOT NULL, dni TEXT NOT NULL, telefono TEXT NOT NULL, fecha_clientes DATE, codigo_ab INTEGER NOT NULL, FOREIGN KEY (codigo_ab) REFERENCES abonos(codigo_abonos) )") 
db.commit()

