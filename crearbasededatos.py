# -*- coding: utf-8 -*-
import sqlite3
conexion = sqlite3.connect("bdbiblioteca.db")
# En una cadena guardaremos el script de creacion de la tabla pais
tabla_pais = """CREATE TABLE pais(

idpais INTEGER PRIMARY KEY AUTOINCREMENT,
nombre TEXT UNIQUE,
estado TEXT
)
"""
tabla_editorial = """ CREATE TABLE editorial(

ideditorial INTEGER PRIMARY KEY AUTOINCREMENT,
nombre TEXT,
estado TEXT
)
"""
tabla_autor = """ CREATE TABLE autor(

idautor INTEGER PRIMARY KEY AUTOINCREMENT,
nombre TEXT,
f_nacimiento TEXT
)
"""
tabla_libro = """ CREATE TABLE libro(

idlibro INTEGER PRIMARY KEY AUTOINCREMENT,
titulo TEXT,
cantidad INTEGER,
anio INTEGER,
precio REAL,
estado TEXT,
idpais INTEGER REFERENCES pais,
ideditorial INTEGER REFERENCES editorial,
idautor INTEGER REFERENCES autor
)
"""
cursor = conexion.cursor()
cursor.execute(tabla_pais)
cursor.execute(tabla_editorial)
cursor.execute(tabla_autor)
cursor.execute(tabla_libro)
conexion.close()


import sqlite3
conexion = sqlite3.connect("bdbiblioteca.db")
consulta = """INSERT INTO
pais(NOMBRE, ESTADO)
VALUES ('Brasil', 'A')
"""
cursor = conexion.cursor()
cursor.execute(consulta)
conexion.commit()
conexion.close()


import sqlite3
conexion = sqlite3.connect("bdbiblioteca.db")
consulta = """INSERT INTO
pais (nombre, estado)
values ('USA', 'A')
"""
cursor = conexion.cursor()
cursor.execute(consulta)
conexion.commit()
conexion.close()


import sqlite3
conexion = sqlite3.connect("bdbiblioteca.db")
consulta = """INSERT INTO
editorial (nombre, estado)
values ('Colombus', 'A'),
('Centro', 'A')

"""
cursor = conexion.cursor()
cursor.execute(consulta)
conexion.commit()
conexion.close()


import sqlite3
conexion = sqlite3.connect("bdbiblioteca.db")
consulta = """INSERT INTO
libro (titulo, cantidad, anio, precio, estado, idpais, ideditorial, idautor)
values ('Oracle 11g', 10, 2019, 50, 'A', 1, 1, 1),
('Sistemas Operativos', 14, 2016, 59, 'A', 1, 4, 3),
('Estructuras de Datos', 6, 2018, 20, 'A', 2, 2, 3),
('Algoritmos con Python', 8, 2017, 70, 'A', 2, 2, 1),
('BI', 6, 1998, 50, 'A', 1, 4, 2),
('Ing. de Software', 9, 2000, 56, 'A', 3, 2, 4),
('Organización de PC', 9, 2016, 60, 'A', 7, 2,1),
('Ensamblaje', 9, 2018, 50, 'A', 4, 4, 3)

"""
cursor = conexion.cursor()
cursor.execute(consulta)
conexion.commit()
conexion.close()



import sqlite3
conexion = sqlite3.connect("bdbiblioteca.db")
cursor = conexion.cursor()
consulta = """ SELECT *
FROM LIBRO
WHERE
precio >= 55
ORDER BY titulo
"""
cursor = conexion.cursor()
cursor.execute(consulta)
libros = cursor.fetchall()
# Acá libros es una lista... entonces utilizamos un for
for libro in libros:
    print(libro)
conexion.close()

