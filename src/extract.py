
def get_to_products(orders_list: list):
    for order in orders_list:
        for key, value in order.items():
            if key == 'order':
                products = value
    return products


def clear_orders(orders_list: list):
    products = get_to_products(orders_list)
    if products[0] == ",":
        products = products[1:]
    if "Large," in products:
        products = products.replace("Large,", "Large-")
    if "Regular," in products:
        products = products.replace("Regular,", "Regular-")
    if ",," in products:
        products = products.replace(",,", ",")
    for order in orders_list:
        order['order'] = products

    return orders_list


def create_orders_dictionary(orders_list: list):
    products = get_to_products(orders_list)
    count_commas = products.count(",")
    product_string = products.split(",", count_commas)
    list_order = []
    n = 0
    while n in range(count_commas):
        product_name = product_string[n]
        product_price = product_string[n+1]
        n += 2
        if "Large-" in product_name:
            product_size = product_name[:5]
            product_name = product_name[6:]
        elif "Regular-" in product_name:
            product_size = product_name[:7]
            product_name = product_name[8:]
        else:
            product_size = "Standard"
        dictionary = {
                "product_name": product_name,
                "product_size": product_size,
                "product_price": product_price
            }
        list_order.append(dictionary)
    for order in orders_list:
        order['order'] = list_order
    return orders_list


# def extract_unique_names(orders_list):
#     duplicates_removed = []
#     for order in clear_orders:
#         list_to_string = ''.join(order)
#         count_commas = list_to_string.count(",")
#         product = order.split(",", count_commas)
#         n = 0
#         while n in range(count_commas):
#             name = product[n]
#             price = product[n+1]
#             n += 2
#             product_string = name + "," + price
#             if product_string not in duplicates_removed:
#                 duplicates_removed.append(product_string)
#     return duplicates_removed
