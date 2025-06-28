from src.exceptions.task_not_found_error import TaskNotFoundError
from src.models.task import Task


class TaskRepository:

    @staticmethod
    def create_task(title, description, task_status, board, assigned_to, due_date):
        task = Task(
            title=title,
            description=description,
            task_status=task_status,
            board=board,
            assigned_to=assigned_to,
            due_date=due_date,

        )
        task.save()
        return task

    @staticmethod
    def get_task_by_title(title):
        return Task.objects(title=title).first()

    @staticmethod
    def get_tasks_by_board_id(board_id):
        return Task.objects(board=board_id)

    @staticmethod
    def get_task_by_id(id_task):
        return Task.objects(id=id_task).first()

    @staticmethod
    def verify_task_exists(task_id):
        task = TaskRepository.get_task_by_id(task_id)
        if not task:
            raise TaskNotFoundError(f'Task with the ID {task_id} not found')
        return task

