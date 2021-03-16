<<<<<<< Updated upstream
from app import new_list
=======
import connection

def get_orders(orders_list):
    raw_orders = []
    for order in orders_list:
        for key, value in order.items():
            if key == 'order':
                product = value.split(",,")
                raw_orders.append(product)
    return raw_orders
>>>>>>> Stashed changes


raw_orders = []
for order in new_list:
    for key, value in order.items():
        if key == 'order':
            product = value.split(",,")
            raw_orders.append(product)


<<<<<<< Updated upstream
clear_orders = []
for items in raw_orders:
    for lines in items:
        if lines[0] == ",":
            lines = lines[1:]
    list_to_string = ''.join(lines).replace("Large,", "Large ").replace("Regular,", "Regular ")
    clear_orders.append(list_to_string)


list_of_dict = []
for order in clear_orders:
    #how many times "," appears, split that many times
    list_to_string = ''.join(order)
    number = list_to_string.count(",")
    if number == 1:
        product = order.split(",", number)
        product_name = product[0]
        product_price = product[1]
        dictionary = {
            "product_name": product_name,
            "product_price": product_price
        }
        list_order = []
        list_order.append(dictionary)
        list_of_dict.append(list_order)

    elif number > 1:
=======
def create_orders_dictionary(orders_list):
    for order in orders_list:
        list_to_string = ''.join(order)
        number = list_to_string.count(",")
>>>>>>> Stashed changes
        product = order.split(",", number)
        list_order = []
        n = 0
        while n in range(number):
            product_name = product[n]
            product_price = product[n+1]
            n += 2
            dictionary = {
            "product_name" : product_name,
            "product_price" : product_price
            }
            list_order.append(dictionary)
        list_of_dict.append(list_order)
<<<<<<< Updated upstream

for order in list_of_dict:
    print(order)
=======
    return list_of_dict

list_of_dict =[]


def extract_unique_names(orders_list):
    duplicates_removed = []
    for order in clear_orders:
        list_to_string = ''.join(order)
        number = list_to_string.count(",")
        product = order.split(",", number)
        n = 0
        while n in range(number):
            name = product[n]
            price = product[n+1]
            n += 2
            product_string = name + "," + price
            if product_string not in duplicates_removed:
                duplicates_removed.append(product_string)
    return duplicates_removed


def split_product_size(orders_list):
    for dictionary in orders_list:
        for key, value in dictionary.items():
            if key == "product_name":
                convert_to_string = ''.join(value)
                large = "Large "
                regular = "Regular "
                if large in convert_to_string:
                    size = convert_to_string[:6]
                    name = convert_to_string[6:]
                    dictionary.update(
                    {"product_size": size.strip(),
                    "product_name": name}
                    )
                elif regular in convert_to_string:
                    size = convert_to_string[:7]
                    name = convert_to_string[7:]
                    dictionary.update(
                    {"product_size": size.strip(),
                    "product_name": name}
                    )
    return orders_list

order_list = []
connection.add_product_to_database(create_orders_dictionary, list_of_dict)
>>>>>>> Stashed changes
