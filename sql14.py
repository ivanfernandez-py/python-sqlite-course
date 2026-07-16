# GROUP BY: Agrupando datos

import sqlite3

conexion = sqlite3.connect("escuela.db")
cursor = conexion.cursor()

cursor.execute("""
    SELECT carrera, COUNT(*)
    FROM alumnos
    GROUP BY carrera;
    """)
print(cursor.fetchall())

cursor.execute("""
    SELECT carrera, AVG(edad)
    FROM alumnos
    GROUP BY carrera;
    """)
print(cursor.fetchall())

cursor.execute("""
    SELECT carrera, AVG(promedio)
    FROM alumnos
    GROUP BY carrera;
    """)
print(cursor.fetchall())

cursor.execute("""
    SELECT carrera, MAX(promedio)
    FROM alumnos
    GROUP BY carrera;
    """)
print(cursor.fetchall())

cursor.execute("""
    SELECT carrera, MIN(promedio)
    FROM alumnos
    GROUP BY carrera;
    """)
print(cursor.fetchall())

conexion.close()