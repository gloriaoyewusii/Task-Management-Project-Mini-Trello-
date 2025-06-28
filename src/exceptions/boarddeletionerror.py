class BoardDeletionError(Exception):
    def __init__(self, message="An error occurred while deleting a board"):
        super().__init__(message)