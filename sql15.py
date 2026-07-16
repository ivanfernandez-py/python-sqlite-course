import sqlite3

conexion = sqlite3.connect("escuela.db")
cursor = conexion.cursor()

# CARRERAS CON PROMEDIO MAYOR A 9
cursor.execute("""
    SELECT carrera, AVG(promedio)
    FROM alumnos
    GROUP BY carrera
    HAVING AVG(promedio) > 9
    """) 
x = cursor.fetchall()
print(x)

# CARRERAS CON PROMEDIO MAYOR A 8 PERO SOLO ALUMNOS MAYORES A 20
cursor.execute("""
    SELECT carrera, AVG(promedio)
    FROM alumnos
    WHERE edad > 20
    GROUP BY carrera
    HAVING AVG(promedio) > 8
    """) 

conexion.close() 