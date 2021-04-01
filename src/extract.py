import csv
# path = '/workspace/data/birmingham_25-03-2021_09-00-00.csv'

def read_csv(cached_list, file):
    try:
        # with open(path) as file:
            csv_data = csv.reader(file.splitlines())
            for row in csv_data:
                date = str(row[0][0:10])
                time = str(row[0][-5:])
                location = str(row[1])
                order = str(row[3])
                total = str(row[4])
                cached_list.append({'date':date, 'time':time, 'location':location, 'order':order, 'total':total})
            return cached_list
    except Exception as e:
        print('An error occurred: ' + str(e))
    
