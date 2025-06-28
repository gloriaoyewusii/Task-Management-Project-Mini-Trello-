import datetime

from marshmallow import validate
from mongoengine import Document, StringField, DateTimeField, EmailField, BooleanField


class BoardUser(Document):
    username = StringField(required=True, unique=True)
    email = EmailField(required=True, unique=True)
    password = StringField(required=True)
    is_active = BooleanField(default=True)
    created_at = DateTimeField(default=datetime.datetime.now(datetime.timezone.utc))
    updated_at = DateTimeField(default=datetime.datetime.now(datetime.timezone.utc))

    def to_dict(self):
        return {
            'id': str(self.id),
            'username': self.username,
            'email': self.password,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }

    meta = {'collection': 'board_users'}