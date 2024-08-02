# baza danych - przechowywanie danych
# sql, nosql
import sqlite3

try:
    conn = sqlite3.connect('baza_danych.db')
    c = conn.cursor()
    print("Baza danych została podłączona")

    query = '''
    CREATE TABLE IF NOT EXISTS developers (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    joining_date DATETIME,
    salary REAL NOT NULL);
    '''

    # c.execute(query)
    # conn.commit()

    # wykonanie skryptu z pliku na bazie danych
    with open('tables.sql', 'r') as f:
        sql_script = f.read()

        c.executescript(sql_script)

except sqlite3.Error as e:
    print("Bład połączenia z bazą", e)
finally:
    if conn:
        conn.close()
        print("Połączenie zostało zamknięte")
# Baza danych została podłączona
# Połączenie zostało zamknięte
