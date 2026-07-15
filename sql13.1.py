# RETO: Agregar otra columna, PROMEDIO tipo REAL Actualizar promedios
# Pancho	8.5
# Juana	    9.2
# Jacinta	7.8
# Ivan	    9.7

import sqlite3

conexion = sqlite3.connect("escuela.db")
cursor = conexion.cursor() 

# executescript() permite envíar varias instrucciones a la vez, pero no permite fetchall() ni fetchone() después.
cursor.executescript("""
    ALTER TABLE alumnos
    ADD COLUMN promedio REAL;
    
    UPDATE alumnos
    SET promedio = 8.5
    WHERE nombre = 'Pancho';
    
    UPDATE alumnos
    SET promedio = 9.2
    WHERE nombre = 'Juana';
    
    UPDATE alumnos
    SET promedio = 7.8
    WHERE nombre = 'Jacinta';
    
    UPDATE alumnos
    SET promedio = 9.7
    WHERE nombre = 'Ivan';
    """)
conexion.commit()

cursor.execute(""" PRAGMA table_info(alumnos); """)
infotabla = cursor.fetchall()
for columna in infotabla:
    print(columna)


cursor.execute("""
    SELECT * FROM alumnos
    """)

alumnos = cursor.fetchall()

print(f"\t ID \t Nombre \t Edad \t Carrera \t Promedio")
for alumno in alumnos:
    print(f"\t {alumno[0]} \t {alumno[1]} \t {alumno[2]} \t {alumno[3]} \t {alumno[4]}")
    
conexion.close()
