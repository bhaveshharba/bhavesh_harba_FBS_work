import mysql.connector

conn = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'admin@123',
    database = 'fbs'
)

# Create emp table
sql ='CREATE TABLE emp(eid int, name varchar(20), dept varchar(20), sal int)'

# Taking cursor
cursor = conn.cursor()

#Execute sql qurey for creating emp table.
cursor.execute(sql)
