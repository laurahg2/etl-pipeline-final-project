import psycopg2 as ps
# from dotenv import load_dotenv
# import os
from src.handler import connection
from uuid import uuid4
# load_dotenv()
# dbname = os.environ["db"]
# host = os.environ["host"]
# port = os.environ["port"]
# user = os.environ["user"]
# password = os.environ["pass"]

# connection = ps.connect(dbname=dbname, 
#                             host=host,
#                             port=port, 
#                             user=user, 
#                             password=password)



def create_table():
    cursor = connection.cursor()
    # cursor.execute(
    #     """
    #     DO $$ BEGIN
    #     IF NOT EXISTS (SELECT 1 FROM pg_type WHERE typname = 'sizes') THEN
    #     CREATE TYPE sizes AS ENUM ('Small', 'Regular', 'Large');
    #     END IF;
    #     END $$
    #     """)
    cursor.execute(
        """ CREATE TABLE IF NOT EXISTS products (
            product_id INT IDENTITY PRIMARY KEY NOT NULL,
            product_size VARCHAR(150) NOT NULL,
            product_name VARCHAR(150) NOT NULL,
            product_price FLOAT NOT NULL
            )
        """)
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS location(
            location_id INT IDENTITY PRIMARY KEY NOT NULL,
            location_name VARCHAR(150) NOT NULL
            )
        """)
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS transaction (
			transaction_id VARCHAR(36) PRIMARY KEY NOT NULL,
            transaction_date TIMESTAMP,
            location_id INT,
            transaction_total FLOAT,
            foreign key(location_id) REFERENCES location(location_id)
            )
        """)
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS basket (
            transaction_id VARCHAR(36),
            product_id INT,
            foreign key(transaction_id) REFERENCES transaction(transaction_id),
            foreign key(product_id) REFERENCES products(product_id)
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
            sql = (f"INSERT INTO products (product_size, product_name, product_price) SELECT '{product_size}', '{product_name}', '{product_price}' WHERE NOT EXISTS ( SELECT product_id FROM products WHERE product_size = '{product_size}' AND product_name = '{product_name}' AND product_price = '{product_price}' )")
            # val = (product_size, product_name, product_price)
            cursor.execute(sql)
            connection.commit()
        #     id = cursor.fetchall()
        #     print(id)
        #     v['product_id'] = id[0]
        # return newest_list

def add_location_to_database(new_list):
    with connection.cursor() as cursor:
        newest_list = list(set((item['location']) for item in new_list))
        for v in newest_list:
            location_name = v
            sql = (f"INSERT INTO location (location_name) SELECT '{location_name}' WHERE NOT EXISTS ( SELECT location_id FROM location WHERE location_name = '{location_name}' )")
            # val = (location_name)
            cursor.execute(sql)
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
            uuid_id = str(uuid4())
            print(uuid_id)
            location = v['location']
            # time = v['time']
            date = v['date']
            total = v['total']
            sql = "INSERT INTO transaction (transaction_id, location_id, transaction_date, transaction_total) VALUES (%s, %s, %s, %s)"
            val = (uuid_id, location, date, total)
            print(val)
            cursor.execute(sql, val)
            connection.commit()
            # id = cursor.fetchall()
            # print(id)
            v['transaction_id'] = uuid_id
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
