#db -- flask.db

# import sqlite3
# conn = sqlite3.connect('flask.db')
# print('db open success')
#-------------------------------------------------------------------------

#create table -- empl_1
# import sqlite3
# conn = sqlite3.connect('flask.db')
# print('open db success')
#
# conn.execute('''CREATE TABLE empl_1
#        (ID INT PRIMARY KEY     NOT NULL,
#        NAME           TEXT    NOT NULL,
#        AGE            INT     NOT NULL,
#        ADDRESS        CHAR(50),
#        SALARY         REAL);''')
# print('table create success')
# conn.close()
#-------------------------------------------------------------------------

#insert op
# import sqlite3
# conn = sqlite3.connect('flask.db')
# print('open db success')
#
# conn.execute("insert into empl_1 (ID, NAME, AGE, SALARY, ADDRESS) \
#              VALUES (1, 'RUCHI', 50, 30000.00, 'GGN')")
#
# conn.execute("insert into empl_1 (ID, NAME, AGE, SALARY, ADDRESS) \
#               VALUES (2, 'KUHUK', 24, 28000.00, 'JPR')")
#
# conn.execute("insert into empl_1 (ID, NAME, AGE, SALARY, ADDRESS) \
#               VALUES (3, 'VINOD', 75, 48000.00, 'US')")
#
# conn.execute("insert into empl_1 (ID, NAME, AGE, SALARY, ADDRESS) \
#               VALUES (4, 'MOLLY', 21, 12000.00, 'USA')")
#
# conn.execute("insert into empl_1 (ID, NAME, AGE, SALARY, ADDRESS) \
#               VALUES (5, 'SHIVI', 20, 18000.00, 'UK')")
#
# conn.commit()
# print('records insert success')
# conn.close()
#-------------------------------------------------------------------------

#select op
# import sqlite3
# conn = sqlite3.connect('flask.db')
#
# data = conn.execute("select * from empl_1")
# for row in data:
#     print('id = ', row[0])
#     print('name = ', row[1])
#     print('age = ', row[2])
#     print('salary = ', row[4])
#     print('addr = ', row[3], "\n")
#
# conn.close()
#-------------------------------------------------------------------------

#update op
import sqlite3
conn = sqlite3.connect('flask.db')

conn.execute("update empl_1 set salary = 20000.00 where id = 5")
# conn.execute("delete from empl_1 where id = 2")       #delete op
conn.commit()
print('total changes = ', conn.total_changes)

data = conn.execute("select * from empl_1")
for row in data:
    print('id = ', row[0])
    print('name = ', row[1])
    print('age = ', row[2])
    print('salary = ', row[4])
    print('addr = ', row[3], "\n")

conn.close()
