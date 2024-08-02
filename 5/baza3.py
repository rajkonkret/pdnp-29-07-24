# baza danych - przechowywanie danych
# sql, nosql
# sytem CRUD
# Działanie	      Instrukcja SQL	HTTP	            DDS
# Create	           INSERT	        PUT / POST	        write
# Read (Retrieve)	   SELECT	        GET	                read / take
# Update	           UPDATE	        POST / PUT / PATCH	write
# Delete (Destroy)     DELETE	        DELETE	            dispose
import sqlite3

try:
    conn = sqlite3.connect('baza_danych.db')
    c = conn.cursor()
    print("Baza danych została podłączona")

    insert = """
        INSERT INTO software (id,name,price) VALUES (1, 'Python',200);
        """
    # c.execute(insert)
    # conn.commit()

    select = """
    SELECT * FROM software;
    """

    for row in c.execute(select):
        print(row)  # (1, 'Python', 200.0)

    update = """
    UPDATE software SET price=1000 WHERE id=1;
    """

    c.execute(update)
    conn.commit()

    delete = """
    DELETE FROM software WHERE id=1;
    """

    c.execute(delete)
    conn.commit()
except sqlite3.Error as e:
    print("Bład połączenia z bazą", e)
finally:
    if conn:
        conn.close()
        print("Połączenie zostało zamknięte")
# Baza danych została podłączona
# Połączenie zostało zamknięte
