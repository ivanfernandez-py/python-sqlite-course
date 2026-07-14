# RETO: Reporte estadístico de alumnos
# Crear un programa que genere un reporte: 

#------ REPORTE DE ALUMNOS ------

#Cantidad total de alumnos: 10

#Edad promedio: 21.5 años

#Alumno de mayor edad:
#Nombre: Carlos
#Edad: 35

#Alumno de menor edad:
#Nombre: Ana
#Edad: 17

#--------------------------------

import sqlite3

conexion = sqlite3.connect("escuela.db")
cursor = conexion.cursor()

cursor.execute("""
    SELECT COUNT(*) FROM alumnos;
    """)
total= cursor.fetchone()

cursor.execute("""
    SELECT AVG(edad) FROM alumnos;
    """)
promedioEdad= cursor.fetchone()

cursor.execute("""
    SELECT * FROM alumnos
    ORDER BY edad DESC
    LIMIT 1;
    """)
alumnoMayor= cursor.fetchone()

cursor.execute("""
    SELECT * FROM alumnos
    ORDER BY edad ASC
    LIMIT 1;
    """)
alumnoMenor= cursor.fetchone()

print("-"*6 + "REPORTE DE ALUMNOS" + "-"*6)  

print(f"Cantidad total de alumnos: {total[0]}")

print(f"Edad promedio: {promedioEdad[0]:.2f}")

print("Alumno de mayor edad:")
print(f"ID: {alumnoMayor[0]} \t Nombre: {alumnoMayor[1]} \t Edad: {alumnoMayor[2]}")

print("Alumno de menor edad:")
print(f"ID: {alumnoMenor[0]} \t Nombre: {alumnoMenor[1]} \t Edad: {alumnoMenor[2]}")

print("-"*27)  

conexion.close()