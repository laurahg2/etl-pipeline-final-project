import boto3
import src.extract as extract
import src.transform as transform
import src.load as load

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
    # csv_data = csv.reader(data.splitlines())
    extract.import_csv(all_lines, data)
    # Form all the lines of data into a list of lists
    # all_lines = [line for line in csv_data]
    
    print_all_lines = [print(line) for line in all_lines]
    print_all_lines
    
    transform.clear_orders(all_lines)
    transform.create_orders_dictionary(all_lines)

    load.create_table()                
    load.add_product_to_database(all_lines)
    load.add_location_to_database(all_lines)
    load.add_transaction_to_database(all_lines)
    load.add_basket_to_database(all_lines)
    return {"message": "success!!! Check the cloud watch logs for this lambda in cloudwatch https://eu-west-1.console.aws.amazon.com/cloudwatch/home?region=eu-west-1#logsV2:log-groups"}

