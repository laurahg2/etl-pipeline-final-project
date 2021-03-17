import psycopg2 as ps




connection = ps.connect(
    host = "172.20.0.3",
    user = "root",
    password = "password",
    database = "template1",
    port = "5432"
)



def create_table():
        
    cursor = connection.cursor()
    cursor.execute(
        """
        DO $$ BEGIN
        IF NOT EXISTS (SELECT 1 FROM pg_type WHERE typname = 'sizes') THEN
        CREATE TYPE sizes AS ENUM ('Standard', 'Small', 'Regular', 'Large');
        END IF;
        END $$
        """)
    cursor.execute(
        """ 
        CREATE TABLE IF NOT EXISTS products (
            product_id SERIAL PRIMARY KEY NOT NULL,
            product_size VARCHAR(20) NOT NULL,
            product_name VARCHAR(150) NOT NULL,
            product_price FLOAT NOT NULL
            )
        """)
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS location(
            location_id SERIAL PRIMARY KEY NOT NULL,
            location_name VARCHAR(150) NOT NULL
            )
        """)
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS transaction (
            transaction_id SERIAL PRIMARY KEY NOT NULL,
            transaction_date TIMESTAMP(100),
            transaction_time VARCHAR(100),
            location_id INT,
            transaction_total FLOAT,
            CONSTRAINT fk_location FOREIGN KEY(location_id) REFERENCES location(location_id)
            )
        """)
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS basket (
            basket_id SERIAL PRIMARY KEY NOT NULL,
            product_id INT,
            transaction_id INT,
            CONSTRAINT fk_products FOREIGN KEY(product_id) REFERENCES products(product_id),
            CONSTRAINT fk_transaction FOREIGN KEY(transaction_id) REFERENCES transaction(transaction_id)
            )
        """)
    # cursor.execute(
    #     """SELECT SUM(transaction_total)
    #         FROM transaction
    #         WHERE transaction_id = %s;
    #     """
    # )
    
    connection.commit()
    
def add_product_to_database(new_list):
    with connection.cursor() as cursor:
        for order in new_list:
            for key, value in order.items():
                if key == "order":
                    orders_list = value
                    for v in orders_list:
                        product_name = v["product_name"]
                        product_price = v["product_price"]
                        product_size = v["product_size"]
                        sql = "INSERT INTO products (product_size, product_name, product_price) VALUES (%s, %s, %s)"
                        val = (product_size, product_name, product_price)
                        cursor.execute(sql, [val])
                        connection.commit()

def add_location_to_database(new_list):
    with connection.cursor() as cursor:
        item = new_list
        for it in item:
            location = it['location']
            sql = ("INSERT INTO location (location_name) VALUES (%s)")
            val = location
            cursor.execute(sql, [val])
            connection.commit()

def add_transaction_to_database(new_list):
    with connection.cursor() as cursor:
        item = new_list
        for it in item:
            transaction = it
            sql = "INSERT INTO transaction (transaction_date, transaction_time) VALUES (%s, %s)"
            val = ( transaction["date"], transaction["time"] )
            cursor.execute(sql, val)
            connection.commit()

def add_sizes_to_products(new_list):
    with connection.cursor() as cursor:
        for values in new_list:
            for value in values:
                size = value["product_size"]
                sql = "INSERT INTO products (product_size) VALUES (%s)"
                val = (size)
                cursor.execute(sql, val)
                connection.commit()

def error_message():
    print("This input does not exist")
