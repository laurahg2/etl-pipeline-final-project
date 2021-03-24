import src.extract as extract 
import src.transform as transform
import src.load as load

path = '/workspace/data/2021-02-23-isle-of-wight.csv'

new_list = []
extract.import_csv(new_list)



load.create_table()                
load.add_product_to_database(new_list)
load.add_location_to_database(new_list)
load.add_transaction_to_database(new_list)
load.add_basket_to_database(new_list)

if __name__ == "__main__":
    transform.clear_orders(new_list)
    transform.create_orders_dictionary(new_list)
    # extract.extract_unique_names(new_list)

