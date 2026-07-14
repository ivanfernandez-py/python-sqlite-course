# RETO: Eliminación segura de registros

import sqlite3

conexion = sqlite3.connect("escuela.db")
cursor = conexion.cursor()

busqueda = input("Ingresa nombre de alumno a dar de baja: ")

cursor.execute("SELECT * FROM alumnos WHERE nombre = ?", (busqueda,))
resultado = cursor.fetchall()

if not resultado:
    print("Alumno no encontrado")
    
else:
    for alumno in resultado:
        print(f"ID: {alumno[0]}")
        print(f"NOMBRE: {alumno[1]}")  
        print(f"EDAD: {alumno[2]}")
        print("*"*16)
        confirmado = input("Escriba 'si' para eliminar al alumno: ")
    
        if confirmado == 'si':
            
            cursor.execute("""
                DELETE from alumnos WHERE nombre = ?
        """,(busqueda,))
            conexion.commit()
            print("Alumno eliminado de la base de datos.")
            
        elif confirmado != 'si':
            print("Cancelado...")
            
conexion.close()