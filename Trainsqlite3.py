import sqlite3

with sqlite3.connect("database.db") as connection:
    c = connection.cursor()
    try:
        c.execute(
            """CREATE TABLE img_choice(image TEXT, A TEXT, B TEXT, C TEXT, D TEXT)""")
    except sqlite3.OperationalError:
        pass
