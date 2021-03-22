from file_handlers import csv
import extract
#import connection

path = '/workspace/data/2021-02-23-isle-of-wight.csv'

new_list = []
csv.import_csv(new_list)


if __name__ == "__main__":
    extract.clear_orders(new_list)
    extract.create_orders_dictionary(new_list)
    # extract.extract_unique_names(new_list)

connection.create_table()                
connection.add_product_to_database(new_list)
connection.add_location_to_database(new_list)
connection.add_transaction_to_database(new_list)
connection.add_basket_to_database(new_list)

