import boto3

s3 = boto3.client('s3', region_name='us-east-1')

bucket = 'ds2002-pdg8ya'
local_file = 'zoro.jpg'
key = 'zoro.jpg'

with open(local_file, 'rb') as data:
    response = s3.put_object(
        Bucket=bucket,
        Key=key,
        Body=data,
        ACL='public-read'
    )

print("File uploaded with public access")
