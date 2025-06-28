
from src.models.board import Board


class BoardRepository:

    @staticmethod
    def create_board(title, description, owner, board_members=None):
        board = Board(
            title=title,
            description=description,
            owner=owner,
            board_members=board_members,
        )
        board.save()
        return board

    @staticmethod
    def get_board_by_title(title):
        return Board.objects(title=title).first()

    @staticmethod
    def get_board_by_owner(owner):
        return Board.objects(owner=owner).first()

    @staticmethod
    def get_board_by_id(id_board):
        return Board.objects(id=id_board).first()

