import boto3
import requests
import argparse

parser = argparse.ArgumentParser(description="Download a file, upload to S3, and generate a presigned URL")
parser.add_argument("url", help="URL of the file to download")
parser.add_argument("bucket", help="Name of your S3 bucket")
parser.add_argument("filename", help="Name to save the file as (also becomes the S3 object key)")
parser.add_argument("expires", type=int, help="Expiration time for presigned URL (in seconds)")
args = parser.parse_args()

response = requests.get(args.url)
if response.status_code != 200:
    print("Failed to download file.")
    exit(1)

with open(args.filename, "wb") as f:
    f.write(response.content)

print(f"Downloaded: {args.filename}")

s3 = boto3.client('s3', region_name='us-east-1')

with open(args.filename, "rb") as data:
    s3.put_object(
        Bucket=args.bucket,
        Key=args.filename,
        Body=data
    )

print(f"Uploaded {args.filename} to bucket {args.bucket}")

url = s3.generate_presigned_url(
    'get_object',
    Params={
        'Bucket': args.bucket,
        'Key': args.filename
    },
    ExpiresIn=args.expires
)

print("Presigned URL:")
print(url)
