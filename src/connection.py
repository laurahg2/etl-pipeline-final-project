import psycopg2 as ps




connection = ps.connect(
    host = "172.20.0.2",
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
        transaction_list = list({'date':order['date'], 'time':order['time'], 'location':order['location'], 'total':order['total']} for order in new_list)
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
            total = v['total']
            sql = "INSERT INTO transaction (location_id, transaction_date, transaction_time, transaction_total) VALUES (%s, %s, %s, %s)"
            val = ( location, date, time, total )
            cursor.execute(sql, val)
            connection.commit()
            
            # "FROM location(location_id) INSERT INTO transaction(location_id)"

# def add_basket_to_database(new_list):
#     with connection.cursor() as cursor:
#         products_list = list(set((products['product_name'], products['product_price'], products['product_size']) for order_dict in new_list for products in order_dict['order']))
#         transactions_list = list({'transaction_id':transaction['transaction_id']} for index, transaction in enumerate(new_list, start=1))
#         basket = {}
#         for transaction in transactions_list:
#             print(transaction)
#             for product in products_list:
#                 print(product)
#                 if product in transactions_list['transaction_id']:
#                     id = transaction
#                     pro = product
#                     basket['transaction_id'] = id
#                     basket['product_id'] = pro
#         print(basket)
        
        # for b in basket:
        # sql = ("""SELECT products.product_id, transaction.transaction_id 
        #                FROM products, transaction""")
        # val = ()
        # products = cursor.fethall()
        
        
        # for transaction in enumerate(new_list)
        
        # for product in products:
        #     print(product)
            
        # cursor.execute("SELECT transaction_id FROM transaction")
        # transactions = cursor.fethall()
        
        # for transaction in transactions:
        #     print(transaction)
        
def fetch_products_data():
    temp_list =[]
    with connection.cursor() as cursor:
        postresql = "SELECT * FROM products"
        cursor.execute(postresql)
        rows = cursor.fetchall()
        for row in rows:
            temp_dict = {'product_id': int, 'product_name': str}
            temp_dict['product_id'] = row[0]
            temp_dict['product_name'] = row[1]
            temp_list.append(temp_dict)
    return temp_list

def load_into_basket_table_and_update_local_ids(new_list):
    temp_list = fetch_products_data()
    with connection.cursor() as cursor:
        for dictionary in new_list:
            for temp_dict in temp_list:
                postgresql_2 = "SELECT transaction_id FROM transaction WHERE transaction_id = (SELECT max(transaction_id) FROM transaction)"
                cursor.execute(postgresql_2)
                row = cursor.fetchone()
                dictionary['id'] = row[0]
    

def load_into_products_in_basket_table(new_list):
    temp_list = fetch_products_data()
    with connection.cursor() as cursor:
        for dictionary in new_list:
            for temp_dict in temp_list:
                if dictionary['id'] == temp_dict['product_name']:
                    postgresql = "INSERT INTO basket (transaction_id, product_id) VALUES ('{}', '{}')".format((dictionary['id']), temp_dict['product_id'])
                    cursor.execute(postgresql)
                    connection.commit()



def error_message():
    print("This input does not exist")
