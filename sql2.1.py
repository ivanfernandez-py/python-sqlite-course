# RETO: Crear una segunda tabla dentro de la misma base de datos
# La segunda table se llama "profesores"

import sqlite3

conexion = sqlite3.connect("escuela.db")

cursor = conexion.cursor()


cursor.execute("""  
CREATE TABLE profesores(             
    id INTEGER PRIMARY KEY,     
    nombre TEXT,
    materia TEXT            
)
""")

conexion.commit()

print("Tabla creada exitosamente.")

conexion.close()