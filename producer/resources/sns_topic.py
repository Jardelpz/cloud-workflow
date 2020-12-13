import json

from flask_restful import Resource
from flask import request
from schematics.exceptions import DataError
from http import HTTPStatus

from constants import TOPIC_ARN
from utils.sns_client import sns
from schemas.message import MessageInputModel


class SnsTopic(Resource):

    def post(self):
        try:
            message = request.json
            message_obj = MessageInputModel(message)
            message_obj.validate()
            published = sns.publish(
                TopicArn=TOPIC_ARN,
                Message=json.dumps(message)
            )

            return {"message": "published"}, HTTPStatus.OK
        except DataError as e:
            print(e)
            return {"message": f"Message bad formated"}, HTTPStatus.BAD_REQUEST