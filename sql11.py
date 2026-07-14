# Operadores de búsqueda: AND, OR, IN, BETWEEN y LIKE
# AND: Cumplir varias condiciones
# OR: Una u otra condición
# IN: Buscar entre varios valores
# BETWEEN: rangos
# LIKE: búsqueda por patrones

import sqlite3

conexion = sqlite3.connect("escuela.db")
cursor = conexion.cursor()

print("""
   ¿Qué tipo de búsqueda desea realizar?
   
1 - AND (varias condiciones)
2 - OR (una condición u otra)
3 - IN (varios valores)
4 - BETWEEN (rango)
5 - LIKE (búsqueda por patrón)
""")

opcion = input("Seleccione una opción: ")

match opcion:
    
    case "1":
        #AND
        
        edad_minima = int(input("Edad mínima: "))
        edad_maxima = int(input("Edad máxima: "))
        
        cursor.execute("""
            SELECT * FROM alumnos
            WHERE edad >= ? AND edad <= ?
        """, (edad_minima, edad_maxima))
    
    case "2":
        #OR
        
        edad = int(input("Buscar alumnos con edad menor a: "))
        cursor.execute("""
        SELECT * FROM alumnos
        WHERE edad < ? OR edad > 60
        
        """, (edad,))
        
    case "3":
        #IN:
        
        nombre1 = input("Primer nombre: ")
        nombre2 = input("Segundo nombre: ")
        nombre3 = input("Tercer nombre: ")
        
        cursor.execute("""
            SELECT * FROM alumnos
            WHERE nombre IN (?, ?, ?) 
        """(nombre1,nombre2,nombre3))
    
    case "4":
        #BETWEEN
        
        minimo = int(input("Edad mínima: "))
        maximo = int(input("Edad máxima: "))
        
        cursor.execute("""
            SELECT * FROM alumnos
            WHERE edad BETWEEN ? AND ?
        """, (minimo,maximo))
    
    case "5":
        # LIKE: 
        
        texto = input("Texto a buscar en nombre: ")
        texto = "%" + texto + "%"
        
        cursor.execute("""
            SELECT * FROM alumnos
            WHERE nombre LIKE ?
        """, (texto,))
        
    case _:
        print("Opción inválida. ")
        conexion.close()
        exit()
        
alumnos = cursor.fetchall()

print("\nResultados: ")
print("-"*20)

if alumnos:
    for alumno in alumnos:
        print(f"ID: {alumno[0]}")
        print(f"Nombre: {alumno[1]}")
        print(f"Edad: {alumno[2]}")
        print("-"*20)
        
else:
    print("No se encontraron alumnos. ")

conexion.close()