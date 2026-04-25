# init_db.py
import os
import sqlite3

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "database.db")
schema_path = os.path.join(BASE_DIR, "schema.sql")

connection = sqlite3.connect(db_path)

with open(schema_path, encoding="utf-8") as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute(
    "INSERT INTO products (name, price, description, seller_name) VALUES ('Classic T-Shirt', 15.99, 'A comfortable, 100% cotton t-shirt.', 'admin')"
)
cur.execute(
    "INSERT INTO products (name, price, description, seller_name) VALUES ('Stylish Mug', 9.99, 'A ceramic mug, perfect for your morning coffee.', 'admin')"
)

cur.execute("INSERT INTO users (username, password, is_admin) VALUES ('admin', 'password', 1)")

connection.commit()
connection.close()

print("Vulnerable database initialised with sample data.")
