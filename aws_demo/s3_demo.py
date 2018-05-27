import boto3
import json

s3_resource = boto3.resource('s3')
s3_client = boto3.client('s3')
my_bucket = 'avinash-demo-1'
my_key = 'uploaded_people.json'


def print_bucket_names():
    for bucket in s3_resource.buckets.all():
        print(bucket)
        print(bucket.name)


def upload_people_json_file():
    with open('./people.json', 'r') as fp:
        print(fp.readlines())
        fp.seek(0)  # move cursor to beginning
        json_data = json.load(fp, 'utf-8')
        print(json.dumps(json_data))
    s3_client.upload_file('./people.json', my_bucket, my_key)


def delete_uploaded_file():
    delete_response = s3_resource.Object(my_bucket, my_key).delete()
    print(delete_response)


def get_uploaded_file():
    s3_get_response = s3_resource.Object(my_bucket, my_key).get()
    print(s3_get_response)
    print(s3_get_response['Body'].read())


def main():
    print('boto3 example')
    print_bucket_names()
    upload_people_json_file()
    get_uploaded_file()
    delete_uploaded_file()


if __name__ == '__main__':
    main()

