from marshmallow import Schema, fields, validate

from src.models.task import Task


class UpdateTaskRequest(Schema):
    title = fields.String(validate=validate.Length(min=1, max=100))
    description = fields.String(validate=validate.Length(max=300))
    task_status = fields.String(validate=validate.OneOf(["TODO", "DOING", "DONE"]))
    assigned_to = fields.String()
    due_date = fields.DateTime()

    class Meta(Schema.Meta):
        model = Task
        fields = ('id', 'title', 'description', 'task_status', 'assigned_to', 'due_date')
