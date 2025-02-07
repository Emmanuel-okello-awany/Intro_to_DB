import mysql.connector
from prettytable import PrettyTable

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="A@dapemmizo1",
    database="alx_book_store"
)
cursor = conn.cursor()

cursor.execute("SELECT * FROM customers")
rows = cursor.fetchall()

table = PrettyTable(["Customer ID", "Customer Name", "Email", "Address"])
for row in rows:
    table.add_row(row)

print(table)
conn.close()
