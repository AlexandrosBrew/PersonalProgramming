import mysql.connector

#Connecting

mydb = mysql.connector.connect(
    database = "Database"
)

#Creating cursor
c = mydb.cursor()

#Create database
c.execute("CREATE DATABASE Database")

#Check if Database Exists

c.execute("SHOW DATABASES")

for i in c:
    print(i)