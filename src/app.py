from file_handlers import csv
import psycopg2 as ps
path = '/workspace/data/2021-02-23-isle-of-wight.csv'
products_list = []
customers_list = []
orders_list = []




new_list = []
csv.import_csv(new_list)
for i in new_list:
    print(i)
    

# def database_connection():
#     host = "localhost"
#     user = "root"
#     password = "password"
#     database = "team-5-project_devcontainer_postgres_1"
#     port = "8080"

#     connection = ps.connect(
#         user,
#         password,
#         host,
#         port,
#         database
#     )
#     print('we are connected to the database', connection)
#     return connection



# connection = ps.connect(
#     host = "localhost",
#     user = "root",
#     password = "password",
#     database = "team-5-project_devcontainer_postgres_1",
#     port = 8080)
# print('we are connected to the database', connection)

# def create_table():
#     connection = database_connection()
#     cursor = connection.cursor()
#     cursor.execute(
#         """CREATE TABLE IF NOT EXISTS `products` (
#             `product_id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
#             `product_name` VARCHAR(150) NOT NULL,
#             `product_price` FLOAT NOT NULL
#             )
#         """)
#     cursor.execute(
#         """CREATE TABLE IF NOT EXISTS `customers` (
#             `customer_id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
#             `customer_name` VARCHAR(150) NOT NULL,
#             `customer_surname` VARCHAR(150) NOT NULL
#             )
#         """)
#     cursor.execute(
#         """CREATE TABLE IF NOT EXISTS `orders` (
#             `orders_id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
#             `order_date` VARCHAR(100) NOT NULL,
#             `customer_id` INT NOT NULL,
#             `product_id` INT NOT NULL,
#             `payment_total` FLOAT NOT NULL,
#             FOREIGN KEY(product_id) REFERENCES products(product_id),
#             FOREIGN KEY(customer_id) REFERENCES customers(customer_id)
#             )
#         """)
#     connection.commit()


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