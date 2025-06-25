import sqlite3
import os

DB_PATH = "puntajes.db"

# Crear tabla si no existe
def inicializar_bd():
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS puntajes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                puntos INTEGER NOT NULL
            )
        """)
        conn.commit()

# Guardar nuevo puntaje
def guardar_puntaje(nombre, puntos):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO puntajes (nombre, puntos) VALUES (?, ?)", (nombre, puntos))
        conn.commit()

# Obtener top 3 ordenado
def obtener_top_3():
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT nombre, puntos FROM puntajes ORDER BY puntos DESC LIMIT 3")
        return cursor.fetchall()
