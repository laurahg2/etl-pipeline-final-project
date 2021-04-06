import csv
from datetime import datetime
# path = '/workspace/data/2021-02-23-isle-of-wight.csv'

def read_csv(cached_list, data):
    try:
        csv_data = csv.reader(data.splitlines())
        for row in csv_data:
            datestr = row[0]     #.replace('/', '-')
            # print(datestr)
            date_obj = datetime.strptime(datestr, '%d/%m/%Y %H:%M')
            # print(date_obj)
            # time = str(row[0][-5:])
            location = str(row[1])
            order = str(row[3])
            total = str(row[4])
            cached_list.append({'date':date_obj, 'location':location, 'order':order, 'total':total})
        return cached_list
    except Exception as e:
        print('An error occurred: ' + str(e))