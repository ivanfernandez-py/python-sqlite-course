##Crear y conectar a la base de datos

import sqlite3

conexion = sqlite3.connect("escuela.db")

print("Base de datos creada.")

conexion.close()