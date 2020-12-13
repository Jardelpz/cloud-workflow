import json
import uuid

from schematics.exceptions import DataError

from utils.sqs_client import sqs
from schemas.message import MessageOutputModel
from resources.bucket_s3 import insert_data
from constants import QUEUE_URL


def receive_messages():

    messages = sqs.receive_message(
        QueueUrl=QUEUE_URL,
        MaxNumberOfMessages=10
    ).get('Messages')

    if messages:
        for message in messages:
            body = json.loads(message.get('Body')).get('Message')
            try:
                schema_obj = MessageOutputModel(json.loads(body))
                schema_obj.validate()
                is_inserted = insert_data(schema_obj.to_primitive(), str(uuid.uuid4()))
                if is_inserted:
                    delete_message(message.get('ReceiptHandle'), body)
            except DataError as e:
                print(e)
                # raise DataError(str(e))


def delete_message(receipt_handle, message):
    deleted = sqs.delete_message(
        QueueUrl=QUEUE_URL,
        ReceiptHandle=receipt_handle
    )

    if deleted:
        print(f"deleting.. {message}")