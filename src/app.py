# import src.extract as extract 
import src.transform as transform
# import src.load as load

def start_app(data):
    # setup_db function first
    # new_list = []
    # ext(new_list, data)
    trsform(data)
    # ld(new_list)
    # print(data)
    


# if __name__ == "__main__":
#     transform.clear_orders(new_list)
#     transform.create_orders_dictionary(new_list)
#     # extract.extract_unique_names(new_list)

# def ext(new_list, data):
#     extract.read_csv(new_list, data)

def trsform(new_list):
    first = transform.clear_orders(new_list)
    second = transform.create_orders_dictionary(first)
    return second

# def ld(new_list):
#     load.create_table()                
#     load.add_product_to_database(new_list)
#     load.add_location_to_database(new_list)
#     load.add_transaction_to_database(new_list)
#     load.add_basket_to_database(new_list)