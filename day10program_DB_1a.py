import sqlite3 as lite
con=lite.connect('mtica.db')
cur=con.cursor()
cur.execute("SELECT*FROM Car")
rows= cur.fetchall()
print(rows)
for i in rows:
    print(i)
##for row in rows:
##   print("{0:<3}|{1:<6}|{2:>8}". format(row[0],row[2],row[3]))
