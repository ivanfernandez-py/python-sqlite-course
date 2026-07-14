import sqlite3

conexion = sqlite3.connect("escuela.db")

cursor = conexion.cursor()

cursor.execute("""
SELECT * FROM alumnos               
""")

# fetchall() y fetchone() permiten asignarle los datos consultados al cursor
alumnos = cursor.fetchall()

for alumno in alumnos:
    print(f"ID: {alumno[0]}")
    print(f"Nombre: {alumno[1]}")
    print(f"Edad: {alumno[2]}")
    print('*'*8)

conexion.commit()
conexion.close()