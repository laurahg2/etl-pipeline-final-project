from app import new_list


raw_orders = []
for order in new_list:
    for key, value in order.items():
        if key == 'order':
            product = value.split(",,")
            raw_orders.append(product)


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

for order in list_of_dict:
    print(order)
