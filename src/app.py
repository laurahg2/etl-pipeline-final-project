from file_handlers import csv
import extract
#import connection

path = '/workspace/data/2021-02-23-isle-of-wight.csv'

new_list = []
csv.import_csv(new_list)


# connection.database_connection()
# connection.create_table()
# connection.add_product_to_database(extract.create_orders_dictionary, extract.list_of_dict)
# connection.add_location_to_database(new_list)

if __name__ == "__main__":
    clear_orders = extract.clear_orders(new_list)
    orders_dict = extract.create_orders_dictionary(clear_orders)
    # for item in orders_dict:
    #     print(item)
