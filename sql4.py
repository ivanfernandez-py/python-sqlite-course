# Consultar datos de la tabla con SELECT
# SELECT * FROM

import sqlite3

conexion = sqlite3.connect("escuela.db")

cursor = conexion.cursor()

cursor.execute("""
SELECT * FROM alumnos            
"""
)

alumnos = cursor.fetchall()

for alumno in alumnos:
    print(alumno)

conexion.close()