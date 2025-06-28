from src.exceptions.board_not_found_error import BoardNotFoundError
from src.exceptions.boardcreationerror import BoardCreationError
from src.exceptions.boarddeletionerror import BoardDeletionError
from src.exceptions.existing_user_error import ExistingUserError
from src.exceptions.existingboarderror import ExistingBoardError
from src.exceptions.user_not_found_error import UserNotFoundError
from src.repositories.board_repository import BoardRepository

from src.repositories.user_repository import UserRepository


class BoardService:
    @staticmethod
    def create_board(title, description, owner, board_members=None):
        if not title or not title.strip():
            raise BoardCreationError("Board title is required and cannot be empty.")
        if not description or not description.strip():
            raise BoardCreationError("Board description is required and cannot be empty.")

        if board_members is None:
            board_members = []
        if BoardRepository.get_board_by_title(title):
            raise ExistingBoardError(f'Board with board title {title} already exists')
        board_owner = UserRepository.get_user_by_id(owner)
        if not board_owner:
            raise UserNotFoundError(f'Owner with ID {owner} does not exist.')

        board_members_validated = []
        for member_id in board_members:
            user = UserRepository.get_user_by_id(member_id)
            if not user:
                raise UserNotFoundError(f'Board member with ID {member_id} does not exist.')
            board_members_validated.append(user)
        try:
            board = BoardRepository.create_board(title, description, owner, board_members_validated)
            return board
        except Exception as e:
            raise BoardCreationError(str(e))


    @staticmethod
    def view_board(board_id):
        board = BoardRepository.get_board_by_id(board_id)
        if not board:
            raise BoardNotFoundError(f'Board with ID {board_id} not found')
        return board

    @staticmethod
    def delete_board(board_id):
        board = BoardRepository.get_board_by_id(board_id)
        if not board:
            raise BoardNotFoundError(f'Board with ID {board_id} not found')
        try:
            deletion_outcome = board.delete()
            if deletion_outcome:
                return f'Board with ID {board_id} was successfully deleted.'
            return f'Board with ID {board_id} was not successfully deleted.'
        except Exception as e:
            raise BoardDeletionError(str(e))
