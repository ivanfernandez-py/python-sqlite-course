# ALTER TABLE: Modificar tablas existentes

import sqlite3

conexion = sqlite3.connect("escuela.db")
cursor = conexion.cursor()

cursor.execute("""
    ALTER TABLE alumnos
    ADD COLUMN carrera TEXT;           
    
    UPDATE alumnos
    SET carrera = 'Electronica'
    WHERE nombre = 'Pancho';          
    
    UPDATE alumnos
    SET carrera = 'Electronica'
    WHERE nombre = 'Pancho';
    
    UPDATE alumnos
    SET carrera = 'Sistemas'
    WHERE nombre = 'Juana';
    
    """)

print("Columna carrera añadida.")

conexion.commit()
conexion.close()

#   Cambiar el nombre a una columna:
#   ALTER TABLE alumnos
#   RENAME COLUMN carrera TO especialidad;

#   Cambiar nombre a la tabla
#   ALTER TABLE alumnos
#   RENAME TO estudiantes;