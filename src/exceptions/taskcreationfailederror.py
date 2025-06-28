class TaskCreationFailedError(Exception):
    def __init__(self, message="Task creation failed"):
        super().__init__(message)
