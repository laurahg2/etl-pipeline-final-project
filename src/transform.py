def clear_orders(orders_list):
    for order in orders_list:
        for key, value in order.items():
            if key == 'order':
                products = value
                if products[0] == ",":
                    products = products[1:]
                if "Large," in products:
                    products = products.replace("Large,", "Large-")
                if "Large " in products:
                    products = products.replace("Large ", "Large-")
                if "Regular," in products:
                    products = products.replace("Regular,", "Regular-")
                if "Regular " in products:
                    products = products.replace("Regular ", "Regular-")
                if ",," in products:
                    products = products.replace(",,", ",")
        order['order'] = products
    return orders_list


# def create_orders_dictionary(orders_list):
#     list_of_dict =[]
#     for order in orders_list:
#         for key, value in order.items():
#             if key == 'order':
#                 list_order = []
#                 products = value
#                 number = products.count(",")
#                 product_data = products.split(",", number)
#                 n = 0
#                 while n in range(number):
#                     product_name = product_data[n]
#                     product_price = product_data[n+1]
#                     n += 2

#                     if "Large-" in product_name:
#                         size = product_name[:5]
#                         name = product_name[6:]
#                         dictionary = {
#                             "product_name": name,
#                             "product_price": product_price,
#                             "product_size": size
#                         }

#                     elif "Regular-" in product_name:
#                         size = product_name[:7]
#                         name = product_name[8:]
#                         dictionary = {
#                             "product_name": name,
#                             "product_price": product_price,
#                             "product_size": size
#                         }

#                     else:
#                         dictionary = {
#                             "product_name": product_name,
#                             "product_price": product_price,
#                             "product_size": "Regular"
#                         }
#                     list_order.append(dictionary)
#         order['order'] = list_order
#     return orders_list

def transform_data(orders_list):
    for transaction in orders_list:
        for key, value in transaction.items():
            if key == 'order':
                list_order = []
                products = value
                items = products.count(",")
                product_data = products.split(", ", items)
                # TO-DO: extract the code below into a new function
                # product_dictionary = {}
                for p in product_data:
                    if "Large-" in p:
                        size = p[:5]
                        name = p[6:-7]
                        price = p[-4:]
                        # product_dictionary["product_size"] = size
                        # product_dictionary[""]
                        dictionary = {
                            "product_size": size,
                            "product_name": name,
                            "product_price": price
                        }
                    else: 
                        size = p[:7]
                        name = p[8:-7]
                        price = p[-4:]
                        dictionary = {
                            "product_size": size,
                            "product_name": name,
                            "product_price": price
                        }
                    list_order.append(dictionary)
        transaction['order'] = list_order
    return orders_list 

# def extract_unique_names(orders_list):
#     duplicates_removed = []
#     for order in clear_orders:
#         list_to_string = ''.join(order)
#         number = list_to_string.count(",")
#         product = order.split(",", number)
#         n = 0
#         while n in range(number):
#             name = product[n]
#             price = product[n+1]
#             n += 2
#             product_string = name + "," + price
#             if product_string not in duplicates_removed:
#                 duplicates_removed.append(product_string)
#     return duplicates_removed