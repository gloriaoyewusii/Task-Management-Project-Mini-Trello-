class TaskDeletionError(Exception):
    def __init__(self, message="Task failed to delete."):
        super().__init__(message)
    #     self.message = message
    # def __str__(self) -> str:
    #     return self.message