from marshmallow import Schema, fields, validate

from src.models.task import Task
from src.repositories.board_repository import BoardRepository


class CreateTaskRequest(Schema):
    title = fields.String(required=True, validate=validate.Length(min=1, max=100))
    description = fields.String(validate=validate.Length(max=300))
    task_status = fields.String(required=True, validate=validate.OneOf(["TODO", "DOING", "DONE"]))
    board = fields.String(required=True)
    assigned_to = fields.String(required=True)
    due_date = fields.DateTime(required=False)

    class Meta(Schema.Meta):
        model = Task
        fields = ('id', 'title', 'description', 'task_status', 'board', 'assigned_to', 'due_date')

