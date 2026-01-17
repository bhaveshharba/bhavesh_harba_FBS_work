import mysql.connector

conn = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'admin@123',
    database = 'fbs'
)

# checking connection is working or not
# print(conn)  

# insert values in emp table using insert query
sql = "INSERT INTO emp(eid, name, dept,sal) VALUES(101, 'ABC', 'SW', 20000)"
sql = "INSERT INTO emp(eid, name, dept,sal) VALUES(102, 'Aman', 'Testing', 40000)"
sql = "INSERT INTO emp(eid, name, dept,sal) VALUES(103, 'Nikhil', 'Admin', 25000)"
sql = "INSERT INTO emp(eid, name, dept,sal) VALUES(104, 'Vaibhav', 'Developer', 30000)"


# taking cursor
cursor = conn.cursor()

#Execute sql qurey for insert values in table.
cursor.execute(sql)

#for saving data in databse
conn.commit()