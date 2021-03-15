import app


def database_connection():
    host = "172.20.0.2"
    user = "root"
    password = "password"
    database = "template1"
    port = "5432"

    connection = ps.connect(
        user,
        password,
        host,
        port,
        database
    )
    return connection


def create_table():
    connection = database_connection()
    cursor = connection.cursor()
    cursor.execute(
        """CREATE TYPE sizes AS ENUM (Small, Regular, Large);
        CREATE TABLE IF NOT EXISTS products (
            product_id INT SERIAL PRIMARY KEY NOT NULL,
            product_size sizes
            product_name VARCHAR(150) NOT NULL,
            product_price FLOAT NOT NULL
            CONSTRAINT fk_size FOREIGN KEY(size_id) REFERENCES size(size_id)
            )
        """)
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS transaction (
            transaction_id INT SERIAL PRIMARY KEY NOT NULL,
            transaction_date DATE(100) NOT NULL,
            transaction_time VARCHAR(100) NOT NULL,
            location_id INT,
            transaction_total FLOAT NOT NULL
            CONSTRAINT fk_location FOREIGN KEY(location_id) REFERENCES location(location_id)
            )
        """)
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS basket (
            basket_id INT SERIAL PRIMARY KEY NOT NULL,
            product_id INT,
            transaction_id INT,
            CONSTRAINT fk_products FOREIGN KEY(product_id) REFERENCES products(product_id)
            CONSTRAINT fk_transactions FOREIGN KEY(transaction_id) REFERENCES transactions(transaction_id)
            )
        """)
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS location(
            location_id INT SERIAL PRIMARY KEY NOT NULL,
            location_name VARCHAR(150) NOT NULL
            )
        """)
    cursor.execute(
        """SELECT SUM(transaction_total)
            FROM transaction
            WHERE transaction_id = %s;
        """
    )
    
    connection.commit()
    
    def add_products_to_database():
        connection = database_connection()
        cursor = connection.cursor()
        print("   * You are adding a new product. *\n")
    

    if not product_name or not product_price:
        error_message()
    elif product_name and product_price:
        try:
            cursor.execute(
                """INSERT INTO products (
                    product_name, product_price)
                    VALUES (%s, %s)""",
                (product_name, float(product_price))
                )
            connection.commit()
            print("\n   * You have successfully added a product. *")
        except Exception as e:
            print(e)


def error_message():
    print("This input does not exist")
    
