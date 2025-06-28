from werkzeug.security import generate_password_hash, check_password_hash

from src.exceptions.user_not_found_error import UserNotFoundError
from src.models.boarduser import BoardUser


class UserRepository:

    @staticmethod
    def create_user(username, email, password, is_active, created_at, updated_at):
        hashed_password = generate_password_hash(password)
        board_user = BoardUser(
            username=username,
            email=email,
            password=hashed_password,
            is_active=is_active,
            created_at=created_at,
            updated_at=updated_at
        )
        board_user.save()
        return board_user

    @staticmethod
    def get_user_by_username(username):
        return BoardUser.objects(username=username).first()

    @staticmethod
    def get_user_by_email(email):
        return BoardUser.objects(email=email).first()

    @staticmethod
    def get_user_by_id(id_user):
        return BoardUser.objects(id=id_user).first()

    @staticmethod
    def authenticate_user(email, password):
        board_user = UserRepository.get_user_by_email(email)
        password_check = check_password_hash(board_user.password, password)
        if not password_check:
            raise UserNotFoundError(f'Incorrect username or password')
        return board_user