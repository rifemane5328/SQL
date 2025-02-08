import sqlite3

connection = sqlite3.connect("contacts.db")
print("Database has been created successful")
connection.close()

create_genders_query = """
CREATE TABLE IF NOT EXISTS genders(
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
name VARCHAR(30),
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
"""

create_user_query = """
CREATE TABLE IF NOT EXISTS users(
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
name VARCHAR(30) NOT NULL,
email VARCHAR(25) UNIQUE NOT NULL,
password VARCHAR(30) NOT NULL,
age INTEGER,
gender_id INTEGER,
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
FOREIGN KEY (gender_id) REFERENCES genders (id)
    ON DELETE SET NULL
    ON UPDATE CASCADE
);
"""

create_contacts_query = """
CREATE TABLE IF NOT EXISTS contacts(
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
name VARCHAR(30) NOT NULL,
email VARCHAR(25) UNIQUE NOT NULL,
phone VARCHAR(30) NOT NULL,
favorite BOOLEAN DEFAULT FALSE,
user_id INT NOT NULL,
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
FOREIGN KEY(user_id) REFERENCES user (id)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);
"""

create_customers_query = """
CREATE TABLE IF NOT EXISTS customers(
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
customer_name VARCHAR(30) NOT NULL,
contact_name VARCHAR(30) NOT NULL,
address VARCHAR(50) NOT NULL,
city VARCHAR(30) NOT NULL,
country VARCHAR(30) NOT NULL,
postal_code TINYINT UNSIGNED,
customer_id INT NOT NULL,
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
FOREIGN KEY(customer_id) REFERENCES customer (id)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);
"""

# connection = sqlite3.connect("contacts.db")
# connection.execute(create_genders_query)
# connection.execute(create_user_query)
# connection.execute(create_contacts_query)
# connection.execute(create_customers_query)
# print("Table has been created successful")
# connection.close()
#
# connection = sqlite3.connect("contacts.db")
# insert_query_genders = """INSERT INTO genders (name)
# VALUES ('male'), ('female');
# """
# connection.execute(insert_query_genders)
# connection.commit()
# connection = sqlite3.connect("contacts.db")
# insert_users_query = """
# INSERT INTO users (name, email, password, age, gender_id)
# VALUES ('Boris', 'boris@test.com', 'password', 23, 1),
# ('Alina', 'alina@test.com', 'password', 32, 2),
# ('Maksim', 'maksim@test.com', 'password', 40, 1);
# """
#
# insert_contacts_query = """
# INSERT INTO contacts (name, email, phone, favorite, user_id)
# VALUES ('Allen Raymond', 'nulla.ante@vestibul.co.uk', '(992) 914-3792', 0, 1),
# ('Chaim Lewis', 'dui.in@egetlacus.ca', '(294) 840-6685', 1, 1),
# ('Kennedy Lane', 'mattis.Cras@nonenimMauris.net', '(542) 451-7038', 1, 2),
# ('Wylie Pope', 'est@utquamvel.net', '(692) 802-2949', 0, 2),
# ('Cyrus Jackson', 'nibh@semsempererat.com', '(501) 472-5218', 0, 1);
# """

connection = sqlite3.connect("contacts.db")
insert_customers_query = """
INSERT INTO customers(customer_name, contact_name, address, city, country, postal_code, customer_id)
VALUES ('Grocery store', 'Artur Conan Doyle', '222 street', 'New York', 'USA', '34421', '1'),
('White Clover Markets', 'Karl Jablonski', 'Keskuskatu 45', 'Seattle', 'Ukraine', '65948', '2');
"""

# connection.execute(create_customers_query)
# connection.execute(insert_users_query)
# connection.execute(insert_contacts_query)
connection.execute(insert_customers_query)
connection.commit()
connection.close()

connection = sqlite3.connect("contacts.db")
data = connection.execute("""
SELECT * FROM users
""")

for d in connection.execute("""SELECT * FROM users
WHERE age > 25 """):
    print(d)
