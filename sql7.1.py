import sqlite3

conexion = sqlite3.connect("escuela.db")
cursor = conexion.cursor()

caso = int(input("""
1. Buscar por nombre
2. Buscar por edad            
Seleccion:     
"""))

match caso:
    case 1:
        nombre = input("Ingresa el nombre a buscar: ")
        
        sql = """
        SELECT * FROM alumnos
        WHERE nombre = ?

        """
        # Se utiliza una tupla con un elemento, por eso se usa la coma.
        cursor.execute(sql, (nombre,))
        resultado = cursor.fetchall()

        if not resultado:
            print("No se encontraron alumnos con ese nombre")

        for alumno in resultado:
            print(f"ID: {alumno[0]}")
            print(f"NOMBRE: {alumno[1]}")  
            print(f"EDAD: {alumno[2]}")
            print("*"*16)
        
        
    case 2:
        edad = (int(input("Ingresa el edad a buscar: ")))     
        sql = """
        SELECT * FROM alumnos
        WHERE edad = ?

        """
        cursor.execute(sql, (edad,))
        resultado = cursor.fetchall()

        if not resultado:
            print("No se encontraron alumnos con esa edad")

        for alumno in resultado:
            print(f"ID: {alumno[0]}")
            print(f"NOMBRE: {alumno[1]}")  
            print(f"EDAD: {alumno[2]}")
            print("*"*16)
            
conexion.close()