import datetime

from mongoengine import Document, StringField, DateTimeField, EnumField, ReferenceField


class Task(Document):
    title = StringField(required=True, unique=True)
    description = StringField()
    task_status = StringField(choices=['To Do', 'In Progress', 'Done'], default='To Do')
    board = ReferenceField('Board', required=True)
    assigned_to = ReferenceField('BoardUser', required=True)
    due_date = DateTimeField()
    created_at = DateTimeField(default=datetime.datetime.now(datetime.timezone.utc))
    updated_at = DateTimeField(default=datetime.datetime.now(datetime.timezone.utc))

    def to_dict(self):
        return {
            'id': str(self.id),
            'title': self.title,
            'description': self.description,
            'task_status': self.task_status,
            'board': self.board.to_dict() if self.board else None,
            'assigned_to': self.assigned_to.to_dict() if self.assigned_to else None,
            'due_date': self.due_date,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
        }

    meta = {'collection': 'tasks'}