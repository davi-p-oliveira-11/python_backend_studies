import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

connection = sqlite3.connect(ROOT_PATH / "my_database.db")
cursor = connection.cursor()
cursor.row_factory = sqlite3.Row

id_cliente = input("Informe o id do cliente: ")
cursor.execute("SELECT * FROM clientes WHERE id=?", (id_cliente,))

clientes = cursor.fetchall()

for cliente in clientes:
  print(dict(cliente))