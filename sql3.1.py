#RETO: Inserta varios datos en una sola llamada a INSERT INTO

import sqlite3

conexion = sqlite3.connect("escuela.db")

cursor = conexion.cursor()

# Datos separados por comas.
# Strings entre comillas simples 'string'.

cursor.execute("""
INSERT INTO alumnos(nombre,edad)
    VALUES
            ('Pancho',22),
            ('Juana',21),
            ('Jacinta',20)
                         
"""
)

# IMPORTANTE: Evitar pérdida de datos.
# Guardar los cambios con commit()
conexion.commit()

print("Alumnos agregados")

# Cerrar la conexión con la base de datos.
conexion.close()