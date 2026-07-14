# RETO: ¿Ordenar por edad o por nombre?

import sqlite3

conexion = sqlite3.connect("escuela.db")
cursor = conexion.cursor()

seleccion = input("Seleccione: ¿Ordenar por edad 'e' o por nombre 'n'?: ")

if seleccion == 'e':
    cursor.execute("""
    SELECT * FROM alumnos 
    ORDER BY edad DESC
    """)
elif seleccion == 'n':
    alumnos = cursor.execute("""
    SELECT * FROM alumnos 
    ORDER BY nombre ASC
    """)
    
else:
    print("Entrada inválida. ")
    exit()
    
alumnos = cursor.fetchall()
for alumno in alumnos:
    print(f"ID: {alumno[0]} \t Nombre: {alumno[1]} \t Edad: {alumno[2]}")
    
conexion.close()