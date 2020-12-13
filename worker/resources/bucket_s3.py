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


def list_object(key):
    for obj in s3.list_objects(Bucket=BUCKET_NAME, Prefix=key):
        print(obj)

