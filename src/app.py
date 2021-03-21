from file_handlers import csv
import extract
import connection

path = '/workspace/data/2021-02-23-isle-of-wight.csv'
products_list = []
customers_list = []
orders_list = []

new_list = []
csv.import_csv(new_list)



if __name__ == "__main__":
    extract.clear_orders(new_list)
    extract.create_orders_dictionary(new_list)
    # extract.extract_unique_names(new_list)
    # print(new_list)
    # for order in new_list:
    #     for key, value in order.items():
    #         if key == "order":
    #             orders_list = value
    #             for v in orders_list:
    #                 print(v["product_name"])
    # for order in new_list:
    #     for key, value in order.items():
    #         if key == 'date':
    #             date = value
    #             print(date)
    #         if key == 'time':
    #             time = value
    #             print(time)
connection.create_table()                
# connection.add_product_to_database(new_list)
# connection.add_location_to_database(new_list)
# connection.add_transaction_to_database(new_list)
connection.fetch_products_data()
connection.load_into_basket_table_and_update_local_ids(new_list)
connection.load_into_products_in_basket_table(new_list)
# connection.add_basket_to_database(new_list)
