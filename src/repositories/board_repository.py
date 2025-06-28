from src.exceptions.board_not_found_error import BoardNotFoundError
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

    @staticmethod
    def verify_board_exists(board_id):
        board = BoardRepository.get_board_by_id(board_id)
        if not board:
            raise BoardNotFoundError(f'Board with the ID {board_id} not found')
        return board

