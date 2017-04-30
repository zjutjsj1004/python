# -*- coding:UTF-8 -*-
#参考资料:https://wizardforcel.gitbooks.io/w3school-db/content/sql/110.html
#参考资料:http://blog.csdn.net/zmq570235977/article/details/50396313  (SQLLite可视化工具：SQLiteExpert)
import sqlite3

dbName = "test.db"

conn = sqlite3.connect(dbName)

conn.execute('''CREATE TABLE IF NOT EXISTS COMPANY
       (ID INT PRIMARY KEY     NOT NULL,
       NAME           TEXT    NOT NULL,
       AGE            INT     NOT NULL,
       ADDRESS        CHAR(50),
       SALARY         REAL)''')
print "Table created successfully"

conn.close()

conn = sqlite3.connect(dbName)
print "Opened database successfully";

conn.execute("INSERT OR REPLACE INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (1, 'Paul', 32, 'California', 20000.00 )");

conn.execute("INSERT OR REPLACE INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (2, 'Allen', 25, 'Texas', 15000.00 )");

conn.execute("INSERT OR REPLACE INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )");

conn.execute("INSERT OR REPLACE INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )");

conn.commit()
print "Records created successfully";
conn.close()

conn = sqlite3.connect(dbName)
print "Opened database successfully";

cursor = conn.execute("SELECT id, name, address, salary  from COMPANY")
for row in cursor:
   print "ID = ", row[0]
   print "NAME = ", row[1]
   print "ADDRESS = ", row[2]
   print "SALARY = ", row[3], "\n"

print "Operation done successfully";
conn.close()