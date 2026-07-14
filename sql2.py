# Crear tabla con cursor.execute()

import sqlite3
conexion = sqlite3.connect("escuela.db")

cursor = conexion.cursor()


# Entre comillas, es un string, Python no lo entiende.
# El string dentro de cursor.execute se envía a Sql 
cursor.execute("""
CREATE TABLE alumnos(
    id INTEGER PRIMARY KEY,
    nombre TEXT,
    edad INTEGER
)
""")

conexion.commit()

print("Tabla creada correctamente")

conexion.close()