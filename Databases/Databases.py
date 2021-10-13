import sqlite3

#Connect to a database
con = sqlite3.connect('Customer.db')

#Create a cursor
c = con.cursor()

#Create a table
c.execute("""CREATE TABLE customers(
        first_name STRING,
        last_name STRING,
        email STRING
    )""")

# SQLite3 Data Types: NULL(exists or not), INTEGER, REAL, TEXT(string), BLOB()