import mysql.connector

conn = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'admin@123',
    database = 'fbs'
)

sql = "SELECT * FROM emp"

# taking cursor
cursor = conn.cursor()
#Execute sql qurey for fetching data.
cursor.execute(sql)

# print(cursor.fetchall())      #gives all data under list in tuple format.

for row in cursor.fetchall():
    print(row)

# print(cursor.fetchone())        #gives first row of data.

