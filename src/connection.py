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
    
    connection.commit()

                        
def add_product_to_database(new_list):
    with connection.cursor() as cursor:
        newest_list = list(set((products['product_name'], products['product_price'], products['product_size']) for order_dict in new_list for products in order_dict['order']))

        for v in newest_list:
            product_name = v[0]
            product_price = v[1]
            product_size = v[2]
            sql = "INSERT INTO products (product_size, product_name, product_price) VALUES (%s, %s, %s) RETURNING product_id"
            val = (product_size, product_name, product_price)
            cursor.execute(sql, val)
            connection.commit()
            id = cursor.fetchall()
            print(id)
            v['product_id'] = id[0]
        return newest_list

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
        
        locations_id = {}
        cursor.execute("SELECT * FROM location")
        row = cursor.fetchall()

        for location in row:
            id = location[0]
            location_name = location[1]
            locations_id[location_name] = id
        
        for transaction in new_list:
            transaction['location'] = locations_id[transaction['location']]
            
        # Create new tuple
        # which is made of the valuesfrom each dictionary in each transaction_list
        # sql = "INSERT INTO transaction (location_id, transaction_date, transaction_time) VALUES (%s, %s, %s)"
        # print('***',location_list)
            
            
        # print('***',location_list)
        # newest_list = list(set((order['date'], order['time']) for order in new_list))
        for v in new_list:
            location = v['location']
            time = v['time']
            date = v['date']
            total = v['total']
            sql = "INSERT INTO transaction (location_id, transaction_date, transaction_time, transaction_total) VALUES (%s, %s, %s, %s) RETURNING transaction_id"
            val = ( location, date, time, total )
            cursor.execute(sql, val)
            connection.commit()
            id = cursor.fetchall()
            print(id)
            v['transaction_id'] = id[0][0]
        return new_list
            


def get_product_by_name(name):
    with connection.cursor() as cursor:
        sql = 'Select * FROM products WHERE product_name = %s'
        val = (name)
        cursor.execute(sql, [val])
        result = cursor.fetchall()
        
        return {'product_id':result[0][0]}

def add_basket_to_database(new_list):
    with connection.cursor() as cursor:
        for transaction in new_list:
            for orders in transaction['order']:
                transaction_id = transaction['transaction_id'] 
                product = get_product_by_name(orders['product_name'])
                sql = ("""INSERT INTO basket(transaction_id, product_id) VALUES (%s,%s)
                               """)
                val = (transaction_id, product['product_id'])
                cursor.execute(sql, val)
                connection.commit()


def error_message():
    print("This input does not exist")
