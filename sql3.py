# Insertar datos en tablas con INSERT INTO

import sqlite3

conexion = sqlite3.connect("escuela.db")

cursor = conexion.cursor()

cursor.execute("""
INSERT INTO alumnos(nombre, edad)
VALUES('Ivan',24)             
""")

conexion.commit()

print("Alumno agregado succesfulmente")

conexion.close()