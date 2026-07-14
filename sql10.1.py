# RETO: Preguntar al usuario cuantos elementos mostrar, y ordenar alumnos de mayor a menor

import sqlite3

conexion = sqlite3.connect("escuela.db")
cursor = conexion.cursor()

n = int(input("¿Cuántos alumnos desea mostrar?: "))

cursor.execute("""
SELECT * FROM alumnos
ORDER BY edad DESC
LIMIT ?
""",(n,))
alumnos = cursor.fetchall()

for alumno in alumnos:
    print("*"*16)
    print(f"ID: {alumno[0]}")
    print(f"Nombre: {alumno[1]}")
    print(f"Edad: {alumno[2]}")
    
conexion.close()