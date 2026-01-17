import mysql.connector

conn = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'admin@123'
)

# create database fbs
sql ='CREATE DATABASE fbs'

# taking cursor
cursor = conn.cursor()

#Execute sql qurey for creating database.
cursor.execute(sql)
