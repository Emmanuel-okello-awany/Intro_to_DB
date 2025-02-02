import mysql.connector

try:
    # Attempt to connect to MySQL
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="A@dapemmizo1",  # Replace with your actual MySQL root password
        port=3306  # Use default port unless you've set a different one
    )

    if conn.is_connected():
        print("Successfully connected to MySQL!")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    if 'conn' in locals() and conn.is_connected():
        conn.close()
        print("Connection closed.")
