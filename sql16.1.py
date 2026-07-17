import sqlite3

conexion = sqlite3.connect("escuela.db")
cursor = conexion.cursor()

cursor.executescript("""
    CREATE TABLE IF NOT EXISTS carreras(
        id INTEGER PRIMARY KEY,
        nombre TEXT
    );
    
    INSERT INTO carreras(nombre)
        VALUES
            ('Electronica'),
            ('Sistemas');
            
    ALTER TABLE alumnos
    ADD COLUMN carrera_id INTEGER;
    
    UPDATE alumnos
        SET carrera_id = 1
        WHERE carrera = 'Electronica';
        
    UPDATE alumnos
        SET carrera_id = 2
        WHERE carrera = 'Sistemas';
    """)

cursor.execute("""
    SELECT alumnos.nombre, carreras.nombre 
    FROM alumnos
    INNER JOIN carreras
    ON alumnos.carrera_id = carreras.id
    """)

resultado = cursor.fetchall()

for fila in resultado:
    print(resultado)
