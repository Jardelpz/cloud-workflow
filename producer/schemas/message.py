from schematics import Model
from schematics.types import StringType


class MessageInputModel(Model):
    name = StringType(required=True, serialized_name="name")
    cpf = StringType(required=True, serialized_name="Cpf")
