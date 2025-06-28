import datetime

from mongoengine import Document, StringField, DateTimeField, ReferenceField, ListField


class Board(Document):
    title = StringField(required=True, unique=True)
    description = StringField(required=True)
    owner = ReferenceField('BoardUser', required=True)
    board_members = ListField((ReferenceField('BoardUser')))
    created_at = DateTimeField(default=datetime.datetime.now(datetime.timezone.utc))
    updated_at = DateTimeField(default=datetime.datetime.now(datetime.timezone.utc))

    def to_dict(self):
        return {
            'id': str(self.id),
            'title': self.title,
            #title here refers to name of the board
            'description': self.description,
            #description here refers to the purpose of the board
            'owner_id': self.owner.to_dict() if self.owner else None,
            'board_members': [member.to_dict() for member in self.board_members],
            'created_at': self.created_at,
            'updated_at': self.updated_at,

        }

    meta = {'collection': 'boards'}