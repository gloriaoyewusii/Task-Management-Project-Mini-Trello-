class BoardNotFoundError(Exception):
    def __init__(self, message="Board does not exist"):
        super().__init__(message)