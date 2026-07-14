# LIMIT. Evita que sql regrese demasiados resultados

import sqlite3

conexion = sqlite3.connect("escuela.db")
cursor = conexion.cursor()

cantidad = 2

cursor.execute("""
SELECT * FROM alumnos
ORDER BY edad DESC
LIMIT ?
""", (cantidad,))
resultado = cursor.fetchall()

print(resultado)

conexion.close()
