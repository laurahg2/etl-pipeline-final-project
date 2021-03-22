import boto3
import csv


def handle(event, context):
    # Get key and bucket informaition
    key = event['Records'][0]['s3']['object']['key']
    bucket = event['Records'][0]['s3']['bucket']['name']
    
    # use boto3 library to get object from S3
    s3 = boto3.client('s3')
    s3_object = s3.get_object(Bucket = bucket, Key = key)
    data = s3_object['Body'].read().decode('utf-8')
    
    # read CSV
    csv_data = csv.read(data.splitlines())
    
    # Form all the lines of data into a list of lists
    all_lines = [line for line in csv_data]
    
    print_all_lines = [print(line) for line in all_lines]
    print_all_lines
    return {"message": "success!!! Check the cloud watch logs for this lambda in cloudwatch https://eu-west-1.console.aws.amazon.com/cloudwatch/home?region=eu-west-1#logsV2:log-groups"}
