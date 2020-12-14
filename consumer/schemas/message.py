from schematics import Model
from schematics.types import StringType


class MessageOutputModel(Model):
    name = StringType(required=True, serialized_name="name")
    cpf = StringType(required=True, serialized_name="cpf")
