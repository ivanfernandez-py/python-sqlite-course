# Ordenar consultas (ASC, DESC)

import sqlite3

conexion = sqlite3.connect("escuela.db")
cursor = conexion.cursor()

cursor.execute("""
SELECT * FROM alumnos
ORDER BY edad DESC               
""")

alumnos = cursor.fetchall()

for alumno in alumnos: 
    print(alumno)
    
conexion.close()