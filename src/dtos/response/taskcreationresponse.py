from marshmallow import Schema, fields

class TaskCreationResponse(Schema):
    id = fields.String()
    title = fields.String()
    description = fields.String()
    task_status = fields.String()
    board = fields.String()
    assigned_to = fields.String()
    due_date = fields.DateTime()
    created_at = fields.DateTime()
