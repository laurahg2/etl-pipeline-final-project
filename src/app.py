from file_handlers import csv
import extract
import connection

path = '/workspace/data/2021-02-23-isle-of-wight.csv'
products_list = []
customers_list = []
orders_list = []

new_list = []
csv.import_csv(new_list)
# for i in new_list:
#     print(i)


# connection.create_table()
# connection.add_location_to_database(new_list)
# connection.add_transaction_to_database(new_list)
# connection.add_sizes_to_products(new_list)
if __name__ == "__main__":
    # raw_orders = extract.get_orders(new_list)
    # clear_orders = extract.clear_orders(raw_orders)
    # orders_dict = extract.create_orders_dictionary(clear_orders)
    # unique_names = extract.extract_unique_names(orders_dict)
    # product_size = extract.split_product_size(unique_names)
    # for item in orders_dict:
    #     print(item)
    extract.clear_orders(new_list)
    extract.create_orders_dictionary(new_list)
    # print(new_list)
    # for order in new_list:
    #     for key, value in order.items():
    #         if key == "order":
    #             orders_list = value
    #             for v in orders_list:
    #                 print(v['product_size'])
connection.add_product_to_database(new_list)