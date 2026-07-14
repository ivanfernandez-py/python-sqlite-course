import sqlite3

conexion = sqlite3.connect("escuela.db")
cursor = conexion.cursor()

caso = int(input(""" 
Ingrese caso: 
1. Cambiar la edad de Ivan a 25
2. Cambiar el nombre de Pancho por Francisco
3. Cambiar la edad de todos los menores de 23 a 23.                     
"""))

match caso:
    case 1:
        str1 = """
        UPDATE alumnos
        SET edad = 25
        WHERE nombre = 'Ivan'
    """
    case 2:
        str1 = """
        UPDATE alumnos
        SET nombre = 'Francisco'
        WHERE nombre = 'Pancho'
        
    """    
    case 3:
        str1 = """
        UPDATE alumnos
        SET edad = 23
        WHERE edad < 23
        
    """
    case _:
        print("Opción inválida.")
        
cursor.execute(str1)


conexion.commit()
conexion.close()