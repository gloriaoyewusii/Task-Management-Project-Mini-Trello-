
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

