import src.extract as extract 
import src.transform as transform
import src.load as load

def start_app(cached_list, data):
    # setup_db function first
    # new_list = []
    ext(cached_list, data)
    trns = trsform(cached_list)
    ld(trns)
    # print(tform)

    # print(new_list)
    # return cached_list


# if __name__ == "__main__":
#     transform.clear_orders(new_list)
#     transform.create_orders_dictionary(new_list)
#     # extract.extract_unique_names(new_list)

def ext(new_list, data):
    extracted_csv = extract.read_csv(new_list, data)
    return extracted_csv

def trsform(new_list):
    first = transform.clear_orders(new_list)
    second = transform.transform_data(new_list)
    return second

def ld(new_list):
    load.create_table()                
    load.add_product_to_database(new_list)
    load.add_location_to_database(new_list)
    load.add_transaction_to_database(new_list)
    load.add_basket_to_database(new_list)