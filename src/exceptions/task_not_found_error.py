class TaskNotFoundError(Exception):
    def __init__(self, message="Task does not exist"):
        super().__init__(message)