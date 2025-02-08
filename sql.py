import sqlite3

# Connection to database and create
connection = sqlite3.connect("test.db")
print("Database opened successful")
# Create table
create_query = """CREATE TABLE IF NOT EXISTS Persons (
        ID INT NOT NULL PRIMARY KEY AUTOINCREMENT,
        FirstName varchar(255),
        LastName varchar(255),
        Address varchar(255),
        City varchar(255)
        );"""
connection.execute(create_query)
print("Table create successful")
connection.close()

connection = sqlite3.connect("test.db")
insert_query = """INSERT INTO Persons (FirstName, LastName, Address, City)
                VALUES ("Ivan", "Symonov", "1st street", "Odessa")"""
connection.execute(insert_query)
insert_query2 = """INSERT INTO Persons (FirstName, LastName, Address, City)
                VALUES ("Petro", "Lolenko", "2nd street", "Lviv")"""
connection.execute(insert_query2)
connection.commit()
connection = sqlite3.connect("test.db")
select_query = """SELECT * FROM Persons
    WHERE FirstName LIKE 'I%'"""
data = connection.execute(select_query)
for d in data:
    print(d)
