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

    # SQL to create tables
    create_books_table = """
    CREATE TABLE IF NOT EXISTS books (
        book_id INT AUTO_INCREMENT PRIMARY KEY,
        title VARCHAR(130),
        author_id INT,
        price DOUBLE,
        publication_date DATE,
        FOREIGN KEY (author_id) REFERENCES authors(author_id)
    );
    """

    create_authors_table = """
    CREATE TABLE IF NOT EXISTS authors (
        author_id INT AUTO_INCREMENT PRIMARY KEY,
        author_name VARCHAR(215)
    );
    """

    create_customers_table = """
    CREATE TABLE IF NOT EXISTS customers (
        customer_id INT AUTO_INCREMENT PRIMARY KEY,
        customer_name VARCHAR(215),
        email VARCHAR(215),
        address TEXT
    );
    """

    create_orders_table = """
    CREATE TABLE IF NOT EXISTS orders (
        order_id INT AUTO_INCREMENT PRIMARY KEY,
        customer_id INT,
        order_date DATE,
        FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
    );
    """

    create_order_details_table = """
    CREATE TABLE IF NOT EXISTS order_details (
        orderdetailid INT AUTO_INCREMENT PRIMARY KEY,
        order_id INT,
        book_id INT,
        quantity DOUBLE,
        FOREIGN KEY (order_id) REFERENCES orders(order_id),
        FOREIGN KEY (book_id) REFERENCES books(book_id)
    );
    """

    # Execute the queries to create tables
    cursor.execute(create_authors_table)
    cursor.execute(create_books_table)
    cursor.execute(create_customers_table)
    cursor.execute(create_orders_table)
    cursor.execute(create_order_details_table)

    print("Tables created successfully!")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    if 'conn' in locals() and conn.is_connected():
        cursor.close()
        conn.close()
        print("Connection closed.")
