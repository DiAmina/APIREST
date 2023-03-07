import sqlite3

conn = sqlite3.connect('entite.db')
print("Opened database successfull")

conn.execute('''CREATE TABLE ENTITE
        (ID INT PRIMARY KEY NOT NULL,
        LABEL TEXT NOT NULL)''')
print("Table created successfully")

conn.close()
