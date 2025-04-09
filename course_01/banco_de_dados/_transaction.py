import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

connection = sqlite3.connect(ROOT_PATH / "my_database.db")
cursor = connection.cursor()
cursor.row_factory = sqlite3.Row

try:
  cursor.execute("INSERT INTO clientes (nome, email) VALUES (?,?)", ("Teste 2", "teste2@gmail.com"))
  cursor.execute("INSERT INTO clientes (id, nome, email) VALUES (?,?,?)", (2, "Teste 3", "teste3@gmail.com"))
  cursor.execute("DELETE FROM clientes WHERE id = 6;")
  connection.commit()
except Exception as exc:
  print(f"AN ERROR ocurred ! {exc}")
  connection.rollback()
