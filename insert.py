import sqlite3

conn = sqlite3.connect('test.db')
print("Opened database successfully")

conn.execute("INSERT INTO EMPLOYEES VALUES (11,'FAITH',34,450000.00)")
conn.execute("INSERT INTO EMPLOYEES  VALUES (12, 'JANE',51,350000.00);")
conn.execute("INSERT INTO EMPLOYEES VALUES (13,'PAUL',37,3000000.00);")
conn.execute("INSERT INTO EMPLOYEES VALUES (14,'GERALD',28,350000.00);")
conn.execute("INSERT INTO EMPLOYEES VALUES (15,'JANET',31,105000.00);")
conn.execute("INSERT INTO EMPLOYEES VALUES (16,'HARVEY',25,850000.00);")



conn.commit()

print("Records inserted successfully")
conn.close