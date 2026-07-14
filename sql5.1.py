## WHERE

import sqlite3

conexion = sqlite3.connect("escuela.db")

cursor = conexion.cursor()


caso = int(input("""Seleccione:
1. Solo alumnos de 21 años o mayores
2. Solo alumnos que se llamen "Ivan"
3. Solo alumnos menores a 23
4. Tendríamos que filtrar en python, lo cual sería mas dificil             
                        
"""))

str1 = """
            SELECT * FROM alumnos
            WHERE edad>=21
        """
str2 = """
            SELECT * FROM alumnos
            WHERE nombre='Ivan'
        """
        
str3 = """
            SELECT * FROM alumnos
            WHERE edad<23
        """


match caso:
    case 1:
        cursor.execute(str1)
    case 2:
        cursor.execute(str2)
    case 3:
        cursor.execute(str3)
            
alumnos = cursor.fetchall()

for alumno in alumnos:
    print(f"ID: {alumno[0]}")
    print(f"Nombre: {alumno[1]}")
    print(f"Edad: {alumno[2]}")
    print("*"*16)

conexion.close()