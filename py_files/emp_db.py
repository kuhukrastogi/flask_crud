#db -- crud
#table -- empl1

import sqlite3
conn = sqlite3.connect('crud.db')
print('db open')

conn.execute("create table empl1 (ID INTEGER PRIMARY KEY AUTOINCREMENT, name text not null,\
                email TEXT UNIQUE NOT NULL, address TEXT NOT NULL )")
print('table create success')
conn.close()
#-------------------------------------------------------------------------------------------------------

