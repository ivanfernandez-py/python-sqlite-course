# Eliminar datos
# IMPORTANTE: En producción casi NUNCA se borran datos de la base
# Siempre se utiliza un soft delete, una columna booleana que indica si está activo o no.

import sqlite3

conexion = sqlite3.connect("escuela.db")
cursor = conexion.cursor()

nombre = input("Nombre a eliminar: ")

cursor.execute("DELETE FROM alumnos WHERE nombre = ?",(nombre,))

conexion.commit()
conexion.close()