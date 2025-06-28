from datetime import datetime, timezone


from src.exceptions.board_not_found_error import BoardNotFoundError
from src.exceptions.existingtaskerror import ExistingTaskError
from src.exceptions.task_not_found_error import TaskNotFoundError
from src.exceptions.taskcreationfailederror import TaskCreationFailedError
from src.exceptions.taskdeletionerror import TaskDeletionError
from src.exceptions.user_not_found_error import UserNotFoundError
from src.repositories.board_repository import BoardRepository
from src.repositories.task_repository import TaskRepository

from src.repositories.user_repository import UserRepository


class TaskService:
    @staticmethod
    def create_task(title, description, task_status, board, assigned_to, due_date):
        if not title or not title.strip():
            raise TaskCreationFailedError("Task title is required and cannot be empty.")
        if not description or not description.strip():
            raise TaskCreationFailedError("Task description is required and cannot be empty.")
        if due_date:
            if isinstance(due_date, str):
                try:
                    due_date = datetime.fromisoformat(due_date.replace("Z", "+00:00"))
                except ValueError:
                    raise TaskCreationFailedError("Invalid due date format. Use ISO format like '2025-07-15T14:30:00Z'")
            if due_date < datetime.now(timezone.utc):
                raise TaskCreationFailedError("Due date cannot be in the past.")

        if TaskRepository.get_task_by_title(title):
            raise ExistingTaskError(f'A task with the title {title} already exists')
        task_board = BoardRepository.get_board_by_id(board)
        if not task_board:
            raise BoardNotFoundError(f'Board with ID {board} does not exist.')
        if due_date and due_date < datetime.now(timezone.utc):
            raise TaskCreationFailedError("Due date cannot be in the past.")

        task_doer = UserRepository.get_user_by_id(assigned_to)
        if not task_doer:
            raise UserNotFoundError(f'User with ID {assigned_to} does not exist.')

        valid_task_status = {"To Do", "In Progress", "Done"}
        if task_status not in valid_task_status:
            raise TaskCreationFailedError(f"Invalid task status '{task_status}'. Valid statuses are: {valid_task_status}")

        try:
            task = TaskRepository.create_task(title, description, task_status, board, assigned_to, due_date)
            return task
        except Exception as e:
            raise TaskCreationFailedError(str(e))


    @staticmethod
    def view_task(task_id):
        task = TaskRepository.get_task_by_id(task_id)
        if not task:
            raise TaskNotFoundError(f'Task with ID {task_id} not found')
        return task.to_dict()

    @staticmethod
    def delete_task(task_id):
        task = TaskRepository.get_task_by_id(task_id)
        if not task:
            raise TaskNotFoundError(f'Task with ID {task_id} not found')
        try:
            deletion_outcome = task.delete()
            if deletion_outcome:
                return f'Task with ID {task_id} was successfully deleted.'
            return f'Task with ID {task_id} was not successfully deleted.'
        except Exception as e:
            raise TaskDeletionError(str(e))

    @staticmethod
    def update_task(task_id, new_data):
        task = TaskRepository.get_task_by_id(task_id)
        if not task:
            raise TaskNotFoundError(f'Task with ID {task_id} not found.')

        task_owner = UserRepository.get_user_by_id(new_data['assigned_to'])
        if not task_owner:
            raise UserNotFoundError(f'User with ID {new_data['assigned_to']} not found')
        try:
            updated_task = TaskRepository.update_task(task_id, data)
            return updated_task
        except Exception as e:
            raise TaskCreationFailedError(str(e))
