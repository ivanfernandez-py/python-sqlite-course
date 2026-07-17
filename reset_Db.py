# Reset DB

import sqlite3

conexion = sqlite3.connect("escuela.db")
cursor = conexion.cursor()

cursor.execute("""
    DELETE FROM ALUMNOS;
    """)

cursor.execute("""
    INSERT INTO alumnos (nombre, edad, carrera, promedio)
        VALUES
            ('Pancho',    22, 'Electronica', 8.5),
            ('Juana',     21, 'Sistemas',    9.2),
            ('Jacinta',   20, 'Electronica', 7.8),
            ('Ivan',      24, 'Sistemas',    9.7),
            ('Luis',      23, 'Electronica', 9.1),
            ('Ana',       19, 'Sistemas',    8.3),
            ('Carlos',    25, 'Electronica', 9.8),
            ('Maria',     22, 'Sistemas',    8.9),
            ('Fernanda',  21, 'Electronica', 8.0),
            ('Diego',     20, 'Sistemas',    7.5);
    """)

conexion.commit()

cursor.execute("""
    SELECT * FROM alumnos;
    """)

lectura = cursor.fetchall()

print("\t|ID\t|Nombre                \t|Edad\t|Carrera\t|Promedio")
print("-"*70)
for alumno in lectura: 
    print(f"\t|{alumno[0]}\t|{alumno[1]:<15}\t|{alumno[2]}\t|{alumno[3]}\t|{alumno[4]}\t")
print("-"*60)

conexion.close()

