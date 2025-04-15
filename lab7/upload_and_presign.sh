#!/bin/bash

if [ "$#" -ne 3 ]; then
    echo "Usage: $0 <file_name> <bucket_name> <expiration_seconds>"
    exit 1
fi

FILE=$1
BUCKET=$2
EXPIRATION=$3

aws s3 cp "$FILE" "s3://$BUCKET/"

URL=$(aws s3 presign "s3://$BUCKET/$FILE" --expires-in "$EXPIRATION")

echo "Presigned URL (valid for $EXPIRATION seconds):"
echo "$URL"
