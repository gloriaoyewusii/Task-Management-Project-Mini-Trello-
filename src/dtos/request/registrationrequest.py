from marshmallow import Schema, fields, validate

from src.models.task import Task


class RegistrationRequest(Schema):
    id = fields.String(dump_only=True)
    username = fields.String(required=True)
    email = fields.Email(required=True, validate=validate.Email())
    password = fields.String(required=True, validate=validate.Length(min=8))

    class Meta(Schema.Meta):
        model = Task
        fields = ('id', 'username', 'email')

