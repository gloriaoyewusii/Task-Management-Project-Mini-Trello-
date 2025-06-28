from src.exceptions.existing_user_error import ExistingUserError
from src.exceptions.user_not_found_error import UserNotFoundError

from src.repositories.user_repository import UserRepository


class UserService:
    @staticmethod
    def register_user(username, email, password):
        if UserRepository.get_user_by_username(username):
            raise ExistingUserError(f'User {username} already exists')
        if UserRepository.get_user_by_email(email):
            raise ExistingUserError(f'Email {email} already exists')
        user = UserRepository.create_user(username, email, password)
        return user

    @staticmethod
    def login_user(email, password):
        return UserRepository.authenticate_user(email, password)

    @staticmethod
    def view_profile(email):
        user = UserRepository.get_user_by_email(email)
        if not user:
            raise UserNotFoundError(f'User {email} not found')
        return user.to_dict()
