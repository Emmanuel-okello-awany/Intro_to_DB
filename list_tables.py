import mysql.connector

try:
    # Connect to MySQL server
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="A@dapemmizo1",  # Replace with your MySQL root password
        database="alx_book_store",  # Specify the database to use
        port=3306
    )

    # Create a cursor object
    cursor = conn.cursor()

    # Query to list all tables
    cursor.execute("SHOW TABLES")

    # Fetch all tables
    tables = cursor.fetchall()

    # Print the tables
    print("Tables in alx_book_store database:")
    for table in tables:
        print(table[0])

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    if 'conn' in locals() and conn.is_connected():
        cursor.close()
        conn.close()
        print("Connection closed.")
