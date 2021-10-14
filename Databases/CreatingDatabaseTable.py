import sqlite3

#Connect to a database
con = sqlite3.connect('Databases/Customer.db')

#Create a cursor
c = con.cursor()

#Create a table
c.execute("""CREATE TABLE customers(
        first_name TEXT,
        last_name TEXT,
        email TEXT
    )""")

# SQLite3 Data Types: NULL(exists or not), INTEGER, REAL, TEXT(string), BLOB(image, mp3, mp4)

#Commiting
con.commit()

#Close the connection
con.close()