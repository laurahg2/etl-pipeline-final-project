import csv
import psycopg2
from dotenv import load_dotenv
path = '/workspace/data/2021-02-23-isle-of-wight.csv'
products_list = []
customers_list = []
orders_list = []

def import_csv(cached_list):
    try:
        with open(path) as file:
            fieldnames = ['date', 'location', 'full_name', 'order', 'payment_type', 'total', 'card_details']
            new_file = csv.DictReader(file, delimiter = ',', fieldnames=fieldnames)
            for row in new_file:
                date = str(row['date'])
                location = str(row['location'])
                order = str(row['order'])
                total = float(row['total'])
                cached_list.append({'date':date, 'location':location, 'order':order, 'total':total})
            return cached_list
    except Exception as e:
        print('An error occurred: ' + str(e))


new_list = []
import_csv(new_list)
for i in new_list:
    print(i)


def database_connection():
    load_dotenv()
    host = os.environ.get("host")
    user = os.environ.get("user")
    password = os.environ.get("passsword")
    database = os.environ.get("database")
    port = os.environ.get("port")

    connection = psycopg2.connect(
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
        """CREATE TABLE IF NOT EXISTS `products` (
            `product_id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
            `product_name` VARCHAR(150) NOT NULL,
            `product_price` FLOAT NOT NULL
            )
        """)
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS `customers` (
            `customer_id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
            `customer_name` VARCHAR(150) NOT NULL,
            `customer_surname` VARCHAR(150) NOT NULL
            )
        """)
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS `orders` (
            `orders_id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
            `order_date` VARCHAR(100) NOT NULL,
            `customer_id` INT NOT NULL,
            `product_id` INT NOT NULL,
            `payment_total` FLOAT NOT NULL,
            FOREIGN KEY(product_id) REFERENCES products(product_id),
            FOREIGN KEY(customer_id) REFERENCES customers(customer_id)
            )
        """)
    connection.commit()


# def add_products_to_database():
#     connection = database_connection()
#     cursor = connection.cursor()
#     print("   * You are adding a new product. *\n")
#     product_name = input("Enter product's name: ")
#     product_price = input("Enter the product's price: £")

#     if not product_name or not product_price:
#         error_message()
#     elif product_name and product_price:
#         try:
#             cursor.execute(
#                 """INSERT INTO `products` (
#                     `name`, `price`)
#                     VALUES (%s, %s)""",
#                 (product_name, float(product_price))
#                 )
#             connection.commit()
#             print("\n   * You have successfully added a product. *")
#         except Exception as e:
#             print(e)