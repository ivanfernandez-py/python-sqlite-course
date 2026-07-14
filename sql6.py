import sqlite3

conexion = sqlite3.connect("escuela.db")

cursor = conexion.cursor()

cursor.execute("""
    UPDATE alumnos
    SET edad = 23
    WHERE nombre = 'Pancho'       
""")

conexion.commit()
print("Registro actualizado.")
conexion.close()