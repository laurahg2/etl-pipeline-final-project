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
        """CREATE TYPE sizes AS ENUM ('Small', 'Regular', 'Large');
        CREATE TABLE IF NOT EXISTS products (
            product_id SERIAL PRIMARY KEY NOT NULL,
            product_size sizes,
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
            transaction_date TIMESTAMP(100) NOT NULL,
            transaction_time VARCHAR(100) NOT NULL,
            location_id INT,
            transaction_total FLOAT NOT NULL,
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
    
def add_product_to_database(create_orders_dictionary, list_of_dict):
    with connection.cursor() as cursor:
        
        for values in list_of_dict:
            for value in values:
                new_value = value
                sql = "INSERT INTO products (product_name, product_price, product_size) VALUES (%s, %s, %s)"
                val = (new_value["product_name"], new_value["product_price"], new_value["product_size"])
                cursor.execute(sql, val)
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


def error_message():
    print("This input does not exist")
