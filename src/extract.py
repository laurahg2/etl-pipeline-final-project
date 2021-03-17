
def clear_orders(orders_list):
    for order in orders_list:
        for key, value in order.items():
            if key == 'order':
                products = value
                if products[0] == ",":
                    products = products[1:]
                if "Large," in products:
                    products = products.replace("Large,", "Large-")
                if "Regular," in products:
                    products = products.replace("Regular,", "Regular-")
                if ",," in products:
                    products = products.replace(",,", ",")
        order['order'] = products


def create_orders_dictionary(orders_list):
    for order in orders_list:
        for key, value in order.items():
            if key == 'order':
                list_order = []
                products = value
                number = products.count(",")
                product_data = products.split(",", number)
                n = 0
                while n in range(number):
                    product_name = product_data[n]
                    product_price = product_data[n+1]
                    n += 2

                    if "Large-" in product_name:
                        size = product_name[:5]
                        name = product_name[6:]
                        dictionary = {
                            "product_name": name,
                            "product_price": product_price,
                            "product_size": size
                        }

                    elif "Regular-" in product_name:
                        size = product_name[:7]
                        name = product_name[8:]
                        dictionary = {
                            "product_name": name,
                            "product_price": product_price,
                            "product_size": size
                        }

                    else:
                        dictionary = {
                            "product_name": product_name,
                            "product_price": product_price,
                            "product_size": "Standard"
                        }
                    list_order.append(dictionary)
        order['order'] = list_order


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

