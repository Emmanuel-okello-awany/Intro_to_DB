import mysql.connector

# Connect to MySQL (without specifying a database)
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="A@dapemmizo1"
)

cursor = conn.cursor()

# Create database
cursor.execute("CREATE DATABASE IF NOT EXISTS testdb")

print("✅ Database 'testdb' created successfully!")

cursor.close()
conn.close()
