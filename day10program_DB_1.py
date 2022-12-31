import sqlite3 as lite
con=lite.connect('mtica.db')

cur=con.cursor()
cur.execute("DROP TABLE IF EXISTS Car")
cur.execute('''CREATE TABLE  Car(Id INT,Name TEXT ,Prise INT)''')
print("table cars created.")
cur.execute("INSERT INTO Car VALUES(1,'Audi',357698)")
cur.execute("INSERT INTO Car VALUES(2,'Mercedes',876548)")

cur.execute("INSERT INTO Car VALUES(3,'Skoda',654786)")
cur.execute("INSERT INTO Car VALUES(4,'Volvo',357698)")

con.commit()
print("values in table car inserted.")


