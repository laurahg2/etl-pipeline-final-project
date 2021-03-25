import boto3
import src.app as app
import csv

def handle(event, context):
    # Get key and bucket informaition
    key = event['Records'][0]['s3']['object']['key']
    bucket = event['Records'][0]['s3']['bucket']['name']
    
    # use boto3 library to get object from S3
    s3 = boto3.client('s3')
    s3_object = s3.get_object(Bucket = bucket, Key = key)
    data = s3_object['Body'].read().decode('utf-8')
    all_lines = []
    
    # read CSV
    # fieldnames = ['date', 'location', 'full_name', 'order', 'payment_type', 'total', 'card_details']
    # csv_data = csv.DictReader(data, delimiter = ',', fieldnames=fieldnames)
    # for row in csv_data:
    #     date = str(row['date'][0:10])
    #     time = str(row['date'][-8:])
    #     location = str(row['location'])
    #     order = str(row['order'])
    #     total = str(row['total'])
    #     all_lines.append({'date':date, 'time':time, 'location':location, 'order':order, 'total':total})
    csv_data = csv.reader(data.splitlines())
    for row in csv_data:
        date = str(row[0][0:10])
        time = str(row[0][-8:])
        location = str(row[1])
        order = str(row[3])
        total = str(row[5])
        all_lines.append({'date':date, 'time':time, 'location':location, 'order':order, 'total':total})
    # return cached_list
    # print(all_lines)
    app.start_app(all_lines)
    
    print_all_lines = [print(line) for line in all_lines]
    print_all_lines
    
    return {"message": "success!!! Check the cloud watch logs for this lambda in cloudwatch https://eu-west-1.console.aws.amazon.com/cloudwatch/home?region=eu-west-1#logsV2:log-groups"}
    
    # Form all the lines of data into a list of lists
    # all_lines = [line for line in csv_data]
    # print(data)
    # print(all_lines)
    

