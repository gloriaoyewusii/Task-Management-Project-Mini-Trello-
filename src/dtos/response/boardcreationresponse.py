from marshmallow import Schema, fields

class CreateBoardResponse(Schema):
    id = fields.String()
    title = fields.String()
    description = fields.String()
    owner = fields.String()
    board_members = fields.List(fields.String())
