import sqlite3

conn = sqlite3.connect('py4e.db')

cur = conn.cursor()

cur.execute('''
            DROP TABLE IF EXISTS Users
            ''')

cur.execute('''
            CREATE TABLE Users (Name VARCHAR(128),email VARCHAR(128))
            ''')

cur.execute('''
            insert into Users(name,email) values ('Ulrich','ulrich@nilsson.se')
            ''')            
conn.commit()
sqlstr='select * from Users'
for row in cur.execute(sqlstr):
    print(row[0],row[1])
cur.close()
conn.close()

