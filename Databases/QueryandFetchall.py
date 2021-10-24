import sqlite3

#Connect to a database
con = sqlite3.connect('Databases/Customer.db')

#Create a cursor
c = con.cursor()

#Inserting one value at a time
c.execute("""INSERT INTO customers VALUES ('Alex', 'Brew', 'abrew16@greycourt.org.uk')""")

#Inserting many values at once

many_customers = [('Joe', 'brown', 'joe12@greycourt.org.uk'), ('West', 'brown', 'west13@greycourt.org,uk'), ('Junior', 'Brown', 'junior16@greycourt.org.uk')]
c.executemany("INSERT INTO customers VALUES (?, ?, ?)", many_customers)

#Query and fetchall
# c.fetchone()
# c.fetchmany()
# c.fetchall()
for i in many_customers:
    print(c.fetchone())

#Commiting
con.commit()
print("Finished")
#Close the connection
con.close()