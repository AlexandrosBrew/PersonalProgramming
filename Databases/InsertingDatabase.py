import sqlite3

#Connect to a database
con = sqlite3.connect('Customer.db')

#Create a cursor
c = con.cursor()

#Inserting one value at a time
c.execute("""INSERT INTO customers VALUES ('Alex', 'Brew', 'abrew16@greycourt.org.uk')""")

#Inserting many values at once

many_costumers = [('Joe', 'brown', 'joe12@greycourt.org.uk'), ('West', 'brown', 'west13@greycourt.org,uk'), ('Junior', 'Brown', 'junior16@greycourt.org.uk')]
c.executemany("INSERT INTO customers VALUES (?, ?, ?)", many_costumers)

#Commiting
con.commit()
print("Finished")
#Close the connection
con.close()