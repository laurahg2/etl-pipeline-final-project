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
        CREATE TYPE sizes AS ENUM ('Small', 'Regular', 'Large');
        END IF;
        END $$
        """)
    cursor.execute(
        """ 
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
            transaction_date VARCHAR(100),
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
    #         WHERE transaction_id = product_price;
    #     """
    # )
    
    connection.commit()
    
# def add_product_to_database(new_list):
#     with connection.cursor() as cursor:
#         newest_list = list(set(products['product_name'] for order_dict in new_list for products in order_dict['order']))
#         for order in new_list:
#             for key, value in order.items():
#                 if key == "order":
#                     orders_list = value
#                     for v in orders_list:
#                         product_name = v["product_name"]
#                         product_price = v["product_price"]
#                         product_size = v["product_size"]
#                         sql = "INSERT INTO products (product_size, product_name, product_price) VALUES (%s, %s, %s)"
#                         val = (product_size, product_name, product_price)
#                         cursor.execute(sql, val)
#                         connection.commit()
                        
def add_product_to_database(new_list):
    with connection.cursor() as cursor:
        newest_list = list(set((products['product_name'], products['product_price'], products['product_size']) for order_dict in new_list for products in order_dict['order']))

        for v in newest_list:
            product_name = v[0]
            product_price = v[1]
            product_size = v[2]
            sql = "INSERT INTO products (product_size, product_name, product_price) VALUES (%s, %s, %s)"
            val = (product_size, product_name, product_price)
            cursor.execute(sql, val)
            connection.commit()

def add_location_to_database(new_list):
    with connection.cursor() as cursor:
        newest_list = list(set((item['location']) for item in new_list))
        
        for v in newest_list:
            location_name = v
            sql = ("INSERT INTO location (location_name) VALUES (%s)")
            val = (location_name)
            cursor.execute(sql, [val])
            connection.commit()

def add_transaction_to_database(new_list):
    with connection.cursor() as cursor:
        transaction_list = list({'date':order['date'], 'time':order['time'], 'location':order['location']} for order in new_list)
        locations_id = {}
        cursor.execute("SELECT * FROM location")
        row = cursor.fetchall()
        # print(type(row))
        # print(type(row[0]))
        for location in row:
            id = location[0]
            location_name = location[1]
            locations_id[location_name] = id
        
        for transaction in transaction_list:
            transaction['location'] = locations_id[transaction['location']]
            
        # Create new tuple
        # which is made of the valuesfrom each dictionary in each transaction_list
        # sql = "INSERT INTO transaction (location_id, transaction_date, transaction_time) VALUES (%s, %s, %s)"
        # print('***',location_list)
            
            
        # print('***',location_list)
        # newest_list = list(set((order['date'], order['time']) for order in new_list))
        for v in transaction_list:
            location = v['location']
            time = v['time']
            date = v['date']
            sql = "INSERT INTO transaction (location_id, transaction_date, transaction_time) VALUES (%s, %s, %s)"
            val = ( location, date, time )
            cursor.execute(sql, val)
            connection.commit()
            
            # "FROM location(location_id) INSERT INTO transaction(location_id)"

def add_basket_to_database(new_list):
    with connection.cursor() as cursor:
        
        cursor.execute("""SELECT products.product_id, transaction.transaction_id 
                       FROM products, transaction 
                       """)
        row = cursor.fetchall()
        print(row)


def error_message():
    print("This input does not exist")
