# RETO Reporte estadístico por carrera

#   1. numero de alumnos por carrera
#Carrera          Alumnos
#--------------------------------
#Electronica      2
#Sistemas         2
#   2. Promedio de edad por carrera
#Carrera          Promedio Edad
#------------------------------
#Electronica      21.0
#Sistemas         22.5
#   3. Promedio de calificacion por carrera
# Carrera          Promedio Escolar
#---------------------------------
#Electronica      8.15
#Sistemas         9.45
# 4. Ordenar carreras de mayor a menor segun promedio escolar.
# Ordena las carreras de mayor a menor según su promedio escolar.


import sqlite3

conexion = sqlite3.connect("escuela.db")
cursor = conexion.cursor()

# 1
cursor.execute("""
    SELECT carrera, COUNT(*)
    FROM alumnos
    GROUP BY carrera;
    """)
carreras = cursor.fetchall()
print("\tCarrera \t| Alumnos")
print("-"*32)
for carrera in carreras:
    print(f"\t{carrera[0]} \t| {carrera[1]}")
print("")
    
# 2
cursor.execute("""
    SELECT carrera, AVG(edad)
    FROM alumnos
    GROUP BY carrera;
    """)
carreras = cursor.fetchall()
print("\tCarrera \t| Promedio Edad")
print("-"*32)
for carrera in carreras:
    print(f"\t{carrera[0]} \t| {carrera[1]}")
print("") 

# 3
cursor.execute("""
    SELECT carrera, AVG(promedio)
    FROM alumnos
    GROUP BY carrera;
    """)
carreras = cursor.fetchall()
print("\tCarrera \t| Promedio")
print("-"*32)
for carrera in carreras:
    print(f"\t{carrera[0]} \t| {carrera[1]}")
print("") 

#4
cursor.execute("""
    SELECT carrera, AVG(promedio)
    FROM alumnos
    GROUP BY carrera
    ORDER BY AVG(promedio) DESC;
    """)
carreras = cursor.fetchall()
print("\tCarrera \t| Promedio")
print("-"*32)
for carrera in carreras:
    print(f"\t{carrera[0]} \t| {carrera[1]}")
print("") 

conexion.close()

