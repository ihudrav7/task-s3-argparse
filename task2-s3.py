"""Exercise upload_file()"""

import boto3
import argparse

def main():

    ACCESS_KEY_ID = ''
    ACCESS_SECRET_KEY = ''

    s3 = boto3.client('s3', aws_access_key_id = ACCESS_KEY_ID, aws_secret_access_key = ACCESS_SECRET_KEY)

    parser = argparse.ArgumentParser(description = 'Loading the file to s3 bucket')
    parser.add_argument('-b', '--bucket_name', help = 'Bucket_name')
    parser.add_argument('-f', '--file_name', help = 'File_name')
    parser.add_argument('-o', '--object_name', help = 'Object_name')
    args = parser.parse_args()

    s3.upload_file(args.file_name, args.bucket_name, args.object_name)

    response = s3.list_buckets()
    buckets = [bucket['Name'] for bucket in response['Buckets']]
    print("Bucket List: %s" % buckets)


if __name__ == '__main__':
    main()