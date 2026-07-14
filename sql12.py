# Funciones de agregación: 
# COUNT, AVG, SUM, MAX y MIN

import sqlite3
conexion = sqlite3.connect("escuela.db")
cursor = conexion.cursor()

seleccion = int(input("""
    1. COUNT
    2. AVG
    3. SUM
    4. MAX
    5. MIN
    Seleccione: 
    """))

match seleccion:
    case 1:
        # COUNT() - Contar registros
        cursor.execute("""
        SELECT COUNT(*) FROM alumnos
        """)

    case 2:
        # AVG() - Promedio
        cursor.execute("""
        SELECT AVG(edad) FROM alumnos;
        """)

    case 3:
        # SUM() — Suma total
        cursor.execute("""
        SELECT SUM(edad) FROM alumnos;
        """)

    case 4:
        # MAX() — Valor MÁXIMO
        cursor.execute("""
        SELECT MAX(edad) FROM alumnos;
        """)

    case 5:
        # MIN() — Valor MÍNIMO
        cursor.execute("""
        SELECT MIN(edad) FROM alumnos;
        """)
    case _:
        print("Selección inválida...")
        conexion.close()
        exit()
        
cantidad = cursor.fetchone()
print(cantidad)
conexion.close()
        
        
