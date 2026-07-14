# IMPORTANTE: Nunca se usan f-strings dentro de comandos en execute.
# Se utiliza "?". El sistema sería vulnerable a ataques si utilizaras f-strings
# Ya que, una persona mal intencionada puede insertar condicionales dentro del campo. 
# Este ataque se conoce como Sql-Injection.

import sqlite3

conexion = sqlite3.connect("escuela.db")
cursor = conexion.cursor()

nombre = input("Ingresa nombre del estudiante: ")

cursor.execute("""
SELECT * FROM alumnos
WHERE nombre = ?             
""", (nombre,))
resultado = cursor.fetchall()

print(resultado)

conexion.close()