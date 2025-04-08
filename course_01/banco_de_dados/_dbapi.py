import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

connection = sqlite3.connect(ROOT_PATH / "my_database.db")
cursor = connection.cursor()

def create_table(connection, cursor):
    cursor.execute("CREATE TABLE clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(150))")
    connection.commit()


def insert_registry(connection, cursor, nome, email):
    data = (nome, email)
    cursor.execute(f"INSERT INTO clientes (nome, email) VALUES (?,?);", data)
    connection.commit()

def update_registry(connection, cursor, nome, email, id):
    data = (nome, email, id)
    cursor.execute("UPDATE clientes SET nome=?, email=? WHERE id=?;", data)
    connection.commit()

def delete_registry(connection, cursor, id):
    data = (id,)
    cursor.execute("DELETE FROM clientes WHERE id=?;", data)
    connection.commit()

def insert_many(connection, cursor, data):
    cursor.executemany("INSERT INTO clientes (nome, email) VALUES (?,?)", data)
    connection.commit()

def recover_client(cursor, id):
    cursor.execute("SELECT * FROM clientes WHERE id=?", (id,))
    return cursor.fetchone()


def list_clients(cursor):
    return cursor.execute("SELECT * FROM clientes")


cliente = recover_client(cursor, 2)
print(cliente)

clientes = list_clients(cursor)
for cliente in clientes:
    print(cliente)





# data = [
#    ("John", "john123@gmail.com"),
#    ("Carrie", "carrie321@gmail.com"),
#    ("Lena", "lena12@gmail.com"),
#   ]



# insert_many(connection, cursor, data)

# update_registry(connection, cursor, "John Bonham", "johnled@gmail.com", 1)
# delete_registry(connection, cursor, 1)
