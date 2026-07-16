# RETO
# 1. Obtén el promedio escolar por carrera.
# 2. Obtén las carreras cuyo promedio escolar sea mayor a 9.
# 3. Cuenta cuántos alumnos hay por carrera, pero solamente muestra carreras que tengan más de 1 alumno.
# 4. Obtén la edad promedio por carrera, pero:
#       Ignora alumnos con edad menor a 21.
#       Solo muestra carreras cuyo promedio de edad sea mayor a 22.
# 5. "¿Qué carreras tienen un promedio escolar mayor a 8.5 considerando solamente alumnos mayores de 20 años?"


import sqlite3

conexion = sqlite3.connect("escuela.db")
cursor = conexion.cursor()

# 1.
cursor.execute("""
    SELECT carrera, AVG(promedio)
    FROM alumnos
    WHERE edad > 20
    GROUP BY carrera
    """)
resultado = cursor.fetchall()

print("\tCarrera \t| Promedio")
print("-"*32)
for carrera in resultado:
    print(f"\t{carrera[0]} \t| {carrera[1]}")
print("")

# 2.
cursor.execute("""
    SELECT carrera, AVG(promedio)
    FROM alumnos
    GROUP BY carrera
    HAVING AVG(promedio) > 9
    """)
resultado = cursor.fetchall()

print("\tCarrera \t| Promedio")
print("-"*32)
for carrera in resultado:
    print(f"\t{carrera[0]} \t| {carrera[1]}")
print("")

# 3.
cursor.execute("""
    SELECT carrera, COUNT(*)
    FROM alumnos
    GROUP BY carrera
    HAVING COUNT(*) > 1
    """)
resultado = cursor.fetchall()

print("\tCarrera \t| Alumnos")
print("-"*32)
for carrera in resultado:
    print(f"\t{carrera[0]} \t| {carrera[1]}")
print("")

# 4.
cursor.execute("""
    SELECT carrera, AVG(edad)
    FROM alumnos
    WHERE edad > 20
    GROUP BY carrera
    HAVING AVG(edad) > 22
    """)
resultado = cursor.fetchall()

print("\tCarrera \t| Promedio Edad")
print("-"*32)
for carrera in resultado:
    print(f"\t{carrera[0]} \t| {carrera[1]}")
print("")
    
# 5.
cursor.execute("""
    SELECT carrera, AVG(promedio)
    FROM alumnos
    WHERE edad > 20
    GROUP BY carrera
    HAVING AVG(promedio) > 8.5
    """)
resultado = cursor.fetchall()

print("\tCarrera \t| Promedio")
print("-"*32)
for carrera in resultado:
    print(f"\t{carrera[0]} \t| {carrera[1]}")
print("")


conexion.close()