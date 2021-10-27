import mysql.connector

#Connecting

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Al3xandr0s",
    database = "MySQLDatabase"
)

#Creating cursor
c = mydb.cursor()

#Create database
c.execute("CREATE DATABASE Database")

#Check if Database Exists

c.execute("SHOW DATABASES")

for i in c:
    print(i)