import csv
path = '/workspace/data/2021-02-23-isle-of-wight.csv'
from datetime import datetime

def import_csv(cached_list):
    try:
        with open(path) as file:
            fieldnames = ['date', 'location', 'full_name', 'order', 'payment_type', 'total', 'card_details']
            new_file = csv.DictReader(file, delimiter = ',', fieldnames=fieldnames)
            for row in new_file:
                date = (row['date'][0:10])
                time = (row['date'][-8:])
                location = str(row['location'])
                order = str(row['order'])
                total = float(row['total'])
                cached_list.append({'date':date, 'time':time, 'location':location, 'order':order, 'total':total})
            return cached_list
    except Exception as e:
        print('An error occurred: ' + str(e))