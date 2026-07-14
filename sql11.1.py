# RETO: Crear un programa que permite buscar alumnos usando dos métodos:
# Rango de edad y nombre.

import sqlite3

conexion = sqlite3.connect("escuela.db")
cursor = conexion.cursor()

caso = int(input("""1- Buscar por rango de edad 
2- Buscar por nombre
Selección: """))

match caso:
    case 1:
        minimo = int(input("Edad mínima: "))
        maximo = int(input("Edad máxima: "))
        cursor.execute("""
            SELECT * FROM alumnos
            WHERE edad BETWEEN ? AND ?         
        """,(minimo,maximo))
    case 2:
        texto = input("Texto a buscar: ")
        texto = "%" + texto + "%"
        cursor.execute("""
            SELECT * FROM alumnos
            WHERE nombre LIKE ?         
        """,(texto,))
        
    case _: 
        print("Entrada inválida")
        conexion.close()
        exit()
        
        
resultados = cursor.fetchall()

if resultados:
    for alumno in resultados:
        print(f"ID: {alumno[0]}")
        print(f"Nombre: {alumno[1]}")
        print(f"Edad: {alumno[2]}")
        print("-"*20)
        
else: 
    print("No se encontraron alumnos.")
    
conexion.close()