from marshmallow import Schema, fields, validate

from src.models.board import Board
from src.models.task import Task


class CreateBoardRequest(Schema):
    id = fields.String(dump_only=True)
    title = fields.String(required=True, validate=validate.Length(min=1, max=100))
    description = fields.String(validate=validate.Length(max=300))
    owner = fields.String(required=True, validate=validate.Length(min=8))
    board_members = fields.List(fields.String(), required=True, validate=validate.Length(min=1))

    class Meta(Schema.Meta):
        model = Board
        fields = ('id', 'title', 'description', 'owner', 'board_members')

