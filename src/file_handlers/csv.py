import csv
path = '/workspace/data/2021-02-23-isle-of-wight.csv'
def import_csv(cached_list):
    try:
        with open(path) as file:
            fieldnames = ['date', 'location', 'full_name', 'order', 'payment_type', 'total', 'card_details']
            new_file = csv.DictReader(file, delimiter = ',', fieldnames=fieldnames)
            for row in new_file:
                cached_list.append(row)
            return cached_list
    except Exception as e:
        print('An error occurred: ' + str(e))
    

# def import_csv(file_path, csv_file):
#     try:
#         with open(file_path) as file:
#             new_file = csv.DictReader(file, delimiter = ',')
#             for row in new_file:
#                 idx = int(row['id'])
#                 name = str(row['customer_name'])
#                 address = str(row['customer_address'])
#                 phone = str(row['customer_phone'])
#                 courier = int(row['courier'])
#                 status = str(row['status'])
#                 item = [int(i) for i in row['items'][1:-1].split(', ') if i.isnumeric() == True]
#                 csv_file.append({'id':idx, 'customer_name':name, 'customer_address':address, 'customer_phone':phone, 'courier':courier, 'status':status, 'items':item})
#         return csv_file
#     except Exception as e:
#         print('An error occurred: ' + str(e))