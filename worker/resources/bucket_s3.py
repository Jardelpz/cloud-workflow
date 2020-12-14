import json

from utils.s3 import s3
from constants import BUCKET_NAME


def insert_data(obj, name):
    try:

        s3.put_object(
            Body=json.dumps(obj),
            Bucket=BUCKET_NAME,
            Key=f"users/{name}"
        )

        print(f"{name}... added to s3")

        return True

    except Exception as e:
        print('failed to write data in s3')
        return False


def list_objects():
    for obj in s3.list_objects(Bucket=BUCKET_NAME)['Contents']:
        print(f"{obj['Key']} has the following content: {get_obj(obj['Key'])}")


def get_obj(key):
    obj = s3.get_object(Bucket=BUCKET_NAME, Key=key)
    response = json.loads(obj.get('Body').read())
    if response:
        return response
    else:
        print("object not found")


def delete_obj(key):
    obj = s3.delete_object(Bucket=BUCKET_NAME, Key=key)
    print("deleted from bucket")


list_objects()
# get_obj('users/76820d7f-5af2-4752-8551-79f68cc6c805')
# delete_obj('users/94c88501-a252-4459-b66d-38c54b59d493')
